import sys
import time
from functools import partial
from plyer import notification
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from main_window import Ui_MainWindow
from class_time import Time
from database import Database
from stop_watch import StopWatchThread
from timer import TimerThread
from world_clock import WorldClockThread
from alarm import AlarmThread

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Stop Watch
        self.thread_stopwatch = StopWatchThread()
        self.ui.start_sw.clicked.connect(self.start_stopwatch)
        self.ui.stop_sw.clicked.connect(self.stop_stopwatch)
        self.ui.reset_sw.clicked.connect(self.reset_stopwatch)
        self.thread_stopwatch.sw_signal.connect(self.show_stopwatch)
        self.ui.flag_sw.clicked.connect(self.flag)
        self.num = 1
        self.first_time = Time(0, 0, 0, 0)
        #Timer
        self.hour = 0
        self.min = 1
        self.sec = 30
        self.notif_t = 0
        self.thread_timer = TimerThread(self.hour, self.min, self.sec)
        self.total = self.thread_timer.time.time_to_sec()
        self.thread_timer.t_signal.connect(self.show_timer)
        self.ui.stop_t.clicked.connect(self.stop_timer)
        self.ui.reset_t.clicked.connect(self.reset_timer)
        self.ui.set.clicked.connect(self.set_timer)
        self.ui.start_t.clicked.connect(self.start_timer)
        #World Clock
        self.thread_worldclock = WorldClockThread()
        self.thread_worldclock.wc_signal.connect(self.show_clock)
        self.thread_worldclock.start()
        #ALarm
        self.db = Database()
        self.read_from_database()
        self.notif_a = 0
        self.ui.add_a.clicked.connect(self.new_alarm)
        self.ui.pushButton.setVisible(False)
        self.thread_alarm = AlarmThread()
        self.thread_alarm.start()
        self.thread_alarm.a_signal.connect(self.alarm)
        


    #Stop Watch Funcs
    def reset_stopwatch(self):
        self.thread_stopwatch.reset()
        self.ui.stop_watch.setText("0:0:0.0")
        for i in reversed(range(self.ui.gl_sw.count())): 
            self.ui.gl_sw.itemAt(i).widget().setParent(None)
        self.num = 1
        self.first_time = Time(0, 0, 0, 0)
        
    def start_stopwatch(self):
        self.thread_stopwatch.start()

    def show_stopwatch(self, time):
        self.ui.stop_watch.setText(f"{time.hour}:{time.min}:{time.sec}.{time.hun_sec}")

    def stop_stopwatch(self):
        self.thread_stopwatch.terminate()

    def flag(self):
        second_time = self.thread_stopwatch.time
        dist = second_time.sub(self.first_time)
        self.first_time = Time(second_time.hour, second_time.min, second_time.sec, second_time.hun_sec)
        l1 = QLabel()
        l2 = QLabel()
        l3 = QLabel()
        l1.setText(f"{self.num}.")
        l2.setText(f"- {dist.hour}:{dist.min}:{dist.sec}.{dist.hun_sec}")
        l3.setText(f"{second_time.hour}:{second_time.min}:{second_time.sec}.{second_time.hun_sec}")
        l1.setStyleSheet("color:white;")
        l2.setStyleSheet("color:white;")
        l3.setStyleSheet("color:white;")
        self.ui.gl_sw.addWidget(l1, self.num-1, 0)
        self.ui.gl_sw.addWidget(l2, self.num-1, 1)
        self.ui.gl_sw.addWidget(l3, self.num-1, 2)
        self.num += 1

    #Timer Funcs
    def show_timer(self, time):
        self.ui.timer_2.setText(f"{time.hour} : {time.min} : {time.sec}")
        if self.total != 0:
            self.ui.progressBar.setValue(time.time_to_sec() * 100 / self.total)
        else:
            self.ui.progressBar.setValue(0)

        if time.hour == 0 and time.min == 0 and time.sec == 0:
            if self.notif_t == 0:
                self.notif_t += 1
                notification.notify(title = 'Clock',message = 'Timer time finished!', timeout = 5)

    def start_timer(self):
        self.thread_timer.start()

    def stop_timer(self):
        self.thread_timer.terminate()

    def reset_timer(self):
        self.ui.timer_2.setText("0 : 1 : 30")
        self.ui.progressBar.setValue(100)
        self.sec = 30
        self.min = 1
        self.hour = 0
        self.thread_timer.reset(self.hour, self.min, self.sec)       
        self.total = self.thread_timer.time.time_to_sec() 
        self.notif_t = 0

    def set_timer(self):
        self.sec = int(self.ui.sec_t.text())
        self.min = int(self.ui.min_t.text())
        self.hour = int(self.ui.hour_t.text())
        self.ui.timer_2.setText(f"{self.hour} : {self.min} : {self.sec}")       
        self.thread_timer.reset(self.hour, self.min, self.sec)       
        self.total = self.thread_timer.time.time_to_sec()
        self.notif_t = 0

    #World Clock
    def show_clock(self, gmt_time, ir_time, us_time, de_time):
        self.ui.gmt.setText(f"{gmt_time.hour} : {gmt_time.min} : {gmt_time.sec}")
        self.ui.tehran.setText(f"{ir_time.hour} : {ir_time.min} : {ir_time.sec}")
        self.ui.washington.setText(f"{us_time.hour} : {us_time.min} : {us_time.sec}")
        self.ui.berlin.setText(f"{de_time.hour} : {de_time.min} : {de_time.sec}")

    #Alarm Funcs
    def read_from_database(self):
        for i in reversed(range(self.ui.gl_a.count())): 
            self.ui.gl_a.itemAt(i).widget().setParent(None)
        
        alarms = self.db.get_alarms()

        for i in range(len(alarms)):
            le = QLineEdit()
            te = QTimeEdit()
            tb1 = QToolButton()
            cb = QCheckBox()
            tb2 = QToolButton()

            le.setText(alarms[i][1])
            le.setReadOnly(True)
            time = QTime()
            time.setHMS(alarms[i][2], alarms[i][3],alarms[i][4])
            te.setDisplayFormat("h:mm ")
            te.setTime(time)
            te.setReadOnly(True)
            tb1.setText("🖊")
            cb.setText("")
            if alarms[i][5] == 0:
                cb.setChecked(True)
            tb2.setText("🗑")

            self.ui.gl_a.addWidget(le, i, 0)
            self.ui.gl_a.addWidget(te, i, 1)
            self.ui.gl_a.addWidget(tb1, i, 2)
            self.ui.gl_a.addWidget(cb, i, 3)
            self.ui.gl_a.addWidget(tb2, i, 4)

            tb1.clicked.connect(partial(self.edit, le, te, alarms[i][0]))
            cb.clicked.connect(partial(self.is_on, alarms[i][0], alarms[i][5]))
            tb2.clicked.connect(partial(self.delete, alarms[i][0]))
            self.notif_a = 0

    def new_alarm(self):
        new_title = self.ui.title_a.text()
        new_hour = self.ui.hour_a.text()
        new_min = self.ui.min_a.text()
        feedback = self.db.add_new_task(new_title, new_hour, new_min)
        if feedback == True:
            self.read_from_database()
            self.ui.title_a.setText("")
            self.ui.hour_a.setValue(12)
            self.ui.min_a.setValue(30)
            self.thread_alarm.update()
        else:
            msg_box = QMessageBox()
            msg_box.setText("There is a prublem")
            msg_box.exec_()

    def edit(self, le, te, id):
        le.setReadOnly(False)
        te.setReadOnly(False)
        self.ui.pushButton.setVisible(True)
        title = le.text()
        time = te.text()
        time2 = time.split(":")
        hour = time2[0]
        min = time2[1]
        self.ui.pushButton.clicked.connect(partial(self.update, id, le, te))

    def update(self, id, le, te):
        title = le.text()
        time = te.text()
        time2 = time.split(":")
        hour = int(time2[0])
        min = int(time2[1])
        feedback = self.db.update(int(id), title, hour, min)
        if feedback == True:
            self.read_from_database()
            self.thread_alarm.update()
        else:
            msg_box = QMessageBox()
            msg_box.setText("There is a prublem")
            msg_box.exec_()
        le.setReadOnly(True)
        te.setReadOnly(True)
        self.ui.pushButton.setVisible(False)

    def is_on(self, id, is_on):
        feedback = self.db.is_on(int(id), int(is_on))
        if feedback == True:
            self.read_from_database()
            self.thread_alarm.update()
        else:
            msg_box = QMessageBox()
            msg_box.setText("There is a prublem")
            msg_box.exec_()

    def delete(self, id):
        feedback = self.db.remove(int(id))
        if feedback == True:
            self.read_from_database()
            self.thread_alarm.update()
        else:
            msg_box = QMessageBox()
            msg_box.setText("There is a prublem")
            msg_box.exec_()

    def alarm(self, title, hour, min):
        if self.notif_t == 0:
                self.notif_t += 1
                notification.notify(title = 'Alarm',message = f'{title}\n{hour} : {min}', timeout = 5)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()