"""
Class notifier.py is responsible for sending notifications to users.
MAY be a Singleton class, so only one instance is created.
"""


class Notifier:

    def __init__(self):
        self.notifications_enabled = False
    
    def enable(self):
        self.notifications_enabled=True

    def disable(self):
        self.notifications_enabled = False

    def is_enabled(self):
        return self.notifications_enabled