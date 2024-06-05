import os.path

import cv2


cap = cv2.VideoCapture('../video.mp4')

frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
print(f"Total frames: {frame_count}, FPS: {fps}")

frame_interval = fps  # 每秒抽取一帧

# 初始化多目标跟踪器
multi_tracker = cv2.legacy.MultiTracker_create()

# 读取第一帧
ret, frame = cap.read()
if not ret:
    print("无法读取视频文件")
    exit()

# 在第一帧上手动标注目标
bboxes = []
while True:
    bbox = cv2.selectROI('MultiTracker', frame)
    if bbox != (0, 0, 0, 0):
        bboxes.append(bbox)
        print("已选择的框:", bbox)
    k = cv2.waitKey(0) & 0xFF
    if k == 27:  # 按Esc键退出
        break

total_obj = len(bboxes)

# 添加KCF跟踪器
for bbox in bboxes:
    multi_tracker.add(cv2.legacy.TrackerKCF_create(), frame, bbox)

current_frame = 0
extracted_frames = 0

if not os.path.exists('trackings'):
    os.makedirs('trackings')


# 用于存储丢失物体的索引和丢失的起始帧数
lost_objects = {}

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break


    ret, boxes = multi_tracker.update(frame)
    # 绘制跟踪结果
    for i, newbox in enumerate(boxes):
        p1 = (int(newbox[0]), int(newbox[1]))
        p2 = (int(newbox[0] + newbox[2]), int(newbox[1] + newbox[3]))
        if newbox[2] > 0 and newbox[3] > 0:
            cv2.rectangle(frame, p1, p2, (0, 255, 0), 2, 1)
            cv2.putText(frame, f'Object {i + 1}', (p1[0], p1[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow('MultiTracker', frame)

    if current_frame % frame_interval == 0:
        frame_filename = f"./trackings/frame_{extracted_frames}_track.jpg"
        cv2.imwrite(frame_filename, frame)
        print(f"Tracking frame {extracted_frames}")
        extracted_frames += 1


    current_frame += 1

    if cv2.waitKey(1) & 0xFF == 27:  # 按Esc键退出
        break

cap.release()
cv2.destroyAllWindows()
