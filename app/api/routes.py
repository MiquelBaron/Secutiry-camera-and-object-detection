
"""
Endpoints for the API
/stream: Stream video from the IP camera
/notifications/on|off: Turn notifications on or off
More endpoints can be addes as needed
"""

from loguru import logger
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.services.camera_streamer_mock import CameraStreamerMock
from .dependencies import notifier

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hola esto es una prueba"}


"""
Reproduces the streaming video from the IP camera in the browser.
"""
@router.get("/stream")
def stream():
    streamer = CameraStreamerMock()
    logger.info("Starting video stream")
    return StreamingResponse(streamer.get_frames(), media_type="multipart/x-mixed-replace; boundary=frame")

"""
Turns notifications on
"""
@router.get("/notifications/on")
def notifications_on():
        notifier.enable()
        logger.info("Notifications enabled")
        return{"message": "Notifications are on"}

    
"""
Turns notifications off
"""
@router.get("/notifications/off")
def notifications_off():
    notifier.disable()
    logger.info("Notifications disabled")
    return{"message": "Notifications are off"}




