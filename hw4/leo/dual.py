import os
import cv2
import numpy as np

# 创建文件夹
if not os.path.exists("detections"):
    os.makedirs("detections")

# 加载模型和创建边缘检测对象
model = 'model.yml.gz'
edge_detector = cv2.ximgproc.createStructuredEdgeDetection(model)

# 打开视频文件
video_path = '../video.mp4'
cap = cv2.VideoCapture(video_path)

# 检查视频是否成功打开
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
print(f"Total frames: {frame_count}, FPS: {fps}")

frame_interval = fps  # 每秒抽取一帧

current_frame = 0

output_video_path = 'output.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 使用MP4格式
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))


# 初始化多目标跟踪器
multi_tracker = cv2.legacy.MultiTracker_create()

# 初始化目标ID
object_id = 0
object_ids = []

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 每隔 frame_interval 帧进行目标检测
    if current_frame % frame_interval == 0:
        # 将图像转换为 32 位浮点型
        rgb_image = frame.astype(np.float32) / 255.0

        # 检测边缘
        edges = edge_detector.detectEdges(rgb_image)

        # 计算方向图
        orientation_map = edge_detector.computeOrientation(edges)

        # 抑制非最大值
        edges = edge_detector.edgesNms(edges, orientation_map)

        # 创建 Edge Boxes 对象
        edge_boxes = cv2.ximgproc.createEdgeBoxes()
        edge_boxes.setMaxBoxes(3)  # 设置最大候选区域数量

        # 计算候选区域
        boxes = edge_boxes.getBoundingBoxes(edges, orientation_map)[0]

        # 初始化新的跟踪器和目标ID
        new_multi_tracker = cv2.legacy.MultiTracker_create()
        new_object_ids = []

        # 合并新的跟踪器和现有跟踪器
        for i in range(len(object_ids)):
            new_multi_tracker.add(cv2.legacy.TrackerKCF_create(), frame, multi_tracker.getObjects()[i])
            new_object_ids.append(object_ids[i])

        # 初始化跟踪器和目标ID
        for box in boxes:
            if len(new_object_ids) < 3:
                x, y, w, h = box
                new_multi_tracker.add(cv2.legacy.TrackerKCF_create(), frame, (x, y, w, h))
                new_object_ids.append(object_id)
                object_id += 1

        multi_tracker = new_multi_tracker
        object_ids = new_object_ids

        # 显示检测结果
        for box, obj_id in zip(boxes, new_object_ids):
            x, y, w, h = box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f'ID {obj_id}', (x + 5, y + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


    # 更新多目标跟踪器
    ret, boxes = multi_tracker.update(frame)
    to_remove = set()
    for i, newbox in enumerate(boxes):
        p1 = (int(newbox[0]), int(newbox[1]))
        p2 = (int(newbox[0] + newbox[2]), int(newbox[1] + newbox[3]))
        if newbox[2] > 0 and newbox[3] > 0:
            cv2.rectangle(frame, p1, p2, (0, 255, 0), 2, 1)
            cv2.putText(frame, f'ID {object_ids[i]}', (p1[0] + 5, p1[1] + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0),
                        2)
        else:
            to_remove.add(i)

    if len(to_remove) > 0:
        new_multi_tracker = cv2.legacy.MultiTracker_create()
        new_object_ids = []
        for i in range(len(object_ids)):
            if i not in to_remove:
                new_multi_tracker.add(cv2.legacy.TrackerKCF_create(), frame, multi_tracker.getObjects()[i])
                new_object_ids.append(object_ids[i])
        multi_tracker = new_multi_tracker
        object_ids = new_object_ids


    current_frame += 1
    print(current_frame)

    out.write(frame)

    cv2.imshow('MultiTracker', frame)

    if cv2.waitKey(1) & 0xFF == 27:  # 按Esc键退出
        break

cap.release()
out.release()
cv2.destroyAllWindows()
print("Object detection and tracking completed.")
