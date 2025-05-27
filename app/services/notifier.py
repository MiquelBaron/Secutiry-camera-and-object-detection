"""
Class notifier.py is responsible for sending notifications to users.
MAY be a Singleton class, so only one instance is created.
"""
from loguru import logger
import requests

class Notifier():

    def __init__(self, bot_token:str, chat_id:str):
        
        self.notifications_enabled = False
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.api_url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"


    def enable(self):
        self.notifications_enabled=True
        logger.info("Notifications enabled.")

    def disable(self):
        self.notifications_enabled = False
        logger.info("Notifications disabled.")

    def is_enabled(self):
        return self.notifications_enabled
    
    def alert(self, message:str):
        if not self.notifications_enabled:
            logger.info("Notifications are disabled. Cannot send alert")
            return
        data = {
            "chat_id": self.chat_id,
            "text": message
        }

        try:
            response = requests.post(self.api_url, data=data)
            if response.status_code == 200:
                logger.info("Notification sent successfully.")
            else:
                logger.error(f"Failed to send notification: {response.status_code}, {response.text}")
        except Exception as e:
            logger.exception(f"Error sending notification: {e}")