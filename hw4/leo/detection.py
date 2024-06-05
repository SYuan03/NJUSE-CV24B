import os

import cv2
import numpy as np

frames_dir = 'frames'

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
fps = int(cap.get(cv2.CAP_PROP_FPS))
print(f"Total frames: {frame_count}, FPS: {fps}")

frame_interval = fps  # 每秒抽取一帧

current_frame = 0
extracted_frames = 0

if not os.path.exists("frames"):
    os.makedirs("frames")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 抽取帧
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
        edge_boxes.setMaxBoxes(5)  # 设置最大候选区域数量

        # 计算候选区域
        boxes = edge_boxes.getBoundingBoxes(edges, orientation_map)[0]

        # 绘制候选区域
        for box in boxes:
            x, y, w, h = box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # 显示结果
        frame_filename = f"./detections/frame_{extracted_frames}_detect.jpg"
        cv2.imwrite(frame_filename, frame)
        print(f"Detect frame {extracted_frames}")
        extracted_frames += 1

    current_frame += 1

cap.release()
print("Object detection completed.")