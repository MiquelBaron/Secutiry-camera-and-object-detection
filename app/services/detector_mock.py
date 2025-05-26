import time
import threading
from loguru import logger
from app.api.dependencies import notifier


class DetectorMock:
    def __init__(self, interval=5):
        self.interval = interval  # seconds
        self.running = False

    def start(self):
        if not self.running:
            self.running = True
            thread = threading.Thread(target=self.run, daemon=True)
            thread.start()
            logger.info("Detector started.")

    def run(self):

        while self.running:
            time.sleep(self.interval)
            logger.info("Simulated detection triggered.")

            if notifier.enabled:
                notifier.alert("¡Simulación de detección!")
            else:
                logger.info("Detection ignored, notifier disabled.")

    def stop(self):
        self.running = False
        logger.info("Detector stopped.")