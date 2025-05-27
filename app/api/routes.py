
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
import datetime
from fastapi.responses import RedirectResponse

router = APIRouter()

@router.get("/")
def read_root():
    return RedirectResponse(url="/static/index.html")


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
        return{"message": "Notifications are on"}

    
"""
Turns notifications off
"""
@router.get("/notifications/off")
def notifications_off():
    notifier.disable()
    return{"message": "Notifications are off"}


"""
Endpoint for testing notifications system
"""
@router.get("/notifications/test")
def test_notification():
    if not notifier.is_enabled():
        logger.warning("Notifications are disabled. Cannot send test notification.")
        return {"message": "Notifications are disabled. Cannot send test notification."}
    notifier.alert(f"Simulated notification test")
    logger.info(f"Notification test sent at {datetime.datetime.now()}")
    return {"message": "Notification test sent."}


"""
Returns the current status of notifications: enabled or disabled
"""
@router.get("/notifications/status")
def notifications_status():
    status = "enabled" if notifier.is_enabled() else "disabled"
    logger.info(f"Notifications status checked: {status}")
    return {"notifications_status": status}
