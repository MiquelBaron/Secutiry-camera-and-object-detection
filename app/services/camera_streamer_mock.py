import cv2
import os
import time


class CameraStreamerMock:
    """
    Initializes a mock camera streamer that reads from a video file
    """
    def __init__(self, video_path: str = "static/sample_video.mp4"):
        if not os.path.exists(video_path):
            raise FileNotFoundError(f"Video file not found: {video_path}")
        self.cap = cv2.VideoCapture(video_path) #Abre una fuente de video, video.mp4 en este caso, y la asigna a la variable cap. Esta variable es un objeto de OpenCV
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)

    """
    Returns frames from the video file.
    """
    def get_frames(self):
        while True:
            success, frame = self.cap.read()
            if not success:
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue
            frame = cv2.resize(frame, (480, 270))  # o (480, 270) si necesitas menos peso
            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                continue
            frame_bytes = buffer.tobytes()
            #Formats the frame bytes into a multipart response for streaming
            yield (
                b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n'
            )
            time.sleep(1 / self.fps)

    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()

