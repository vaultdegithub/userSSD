import cv2

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    return frames

def save_video(frames, video_path):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter(video_path, fourcc, 24.0, (frames[0].shape[1], frames[0].shape[0]))
    for frame in frames:
        video.write(frame)
    video.release()