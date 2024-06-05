import cv2
import os

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
        frame_filename = f"./frames/frame_{extracted_frames}.jpg"
        cv2.imwrite(frame_filename, frame)
        print(f"Extract frame {extracted_frames}")
        extracted_frames += 1


    current_frame += 1

cap.release()
print("Frame extraction completed.")
