import time
from datetime import datetime
from PySide6.QtCore import *
from class_time import Time

class WorldClockThread(QThread):
    wc_signal = Signal(Time, Time, Time, Time)

    def __init__(self):
        super().__init__()
  
    def run(self):
        while True:
            fulltime = datetime.now()
            nowtime = time.strftime("%H:%M:%S")
            splittime = nowtime.split(":")
            ir_time = Time(int(splittime[0]), int(splittime[1]), int(splittime[2]), 0)
            gmt_ir = Time(3, 30, 0, 0)
            gmt_time = ir_time.sub_clock(gmt_ir)
            de_ir = Time(2, 30, 0, 0)
            de_time = ir_time.sub_clock(de_ir)
            us_ir = Time(7, 30, 0, 0) 
            us_time = ir_time.sub_clock(us_ir)
            self.wc_signal.emit(gmt_time, ir_time, us_time, de_time)
            time.sleep(1)
