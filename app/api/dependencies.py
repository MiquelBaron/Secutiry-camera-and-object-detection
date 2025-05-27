""""
This module provides dependencies for the other modules in the app.
Used to share the same instance of Notifier across the app (Singleton pattern)
"""


from app.services.notifier import Notifier
#from app.services.detector_mock import DetectorMock


BOT_TOKEN = "8151479588:AAHbe-HJZow8yIqEyoDn7wdySOyv5v_ybKw"
CHAT_ID = "6644964397"
notifier = Notifier(BOT_TOKEN, CHAT_ID)  # Initialize notifier with bot token and chat ID
#detector = DetectorMock(interval=5) #Setting the interval to 5 seconds for testing the app flow