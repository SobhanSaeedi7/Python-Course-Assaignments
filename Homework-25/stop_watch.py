import sys
import time
from PySide6.QtCore import *
from class_time import Time


class StopWatchThread(QThread):
    sw_signal = Signal(Time)

    def __init__(self): 
        super().__init__()
        self.time = Time(0, 0, 0, 0)

    
    def run(self):
        while True:
            self.time.plus()
            self.sw_signal.emit(self.time)
            time.sleep(0.1)

    def reset(self):
        self.time = Time(0, 0, 0, 0)

