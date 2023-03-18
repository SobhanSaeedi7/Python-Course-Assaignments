import time
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from class_time import Time


class TimerThread(QThread):
    t_signal = Signal(Time)

    def __init__(self, h, m, s):
        super().__init__()
        self.time = Time(h, m, s, 0)
  
    def run(self):
        while True:
            self.time.mines()
            self.t_signal.emit(self.time)
            time.sleep(1)

    def reset(self, h, m, s):
        self.time = Time(h, m, s, 0)