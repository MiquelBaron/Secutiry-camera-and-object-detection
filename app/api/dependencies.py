""""
This module provides dependencies for the other modules in the app.
Used to share the same instance of Notifier across the app (Singleton pattern)
"""


from app.services.notifier import Notifier

notifier = Notifier()