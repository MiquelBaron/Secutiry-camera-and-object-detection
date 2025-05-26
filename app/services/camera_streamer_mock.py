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


    """
    Returns frames from the video file.
    """
    def get_frames(self):
        while True:
            time.sleep(0.11111)
            success, frame = self.cap.read()
            if not success:
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue
            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                continue
            frame_bytes = buffer.tobytes()
            #Formats the frame bytes into a multipart response for streaming
            yield (
                b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n'
            )

    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()

