import sys
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from main_window import Ui_MainWindow
from database import Database


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.db = Database()
        
        self.read_from_database()

        self.ui.btn_new_task.clicked.connect(self.new_task)


    def new_task(self):
        new_title = self.ui.tb_new_task_title.text()
        new_description = self.ui.tb_new_task_description.toPlainText()
        new_datetime = self.ui.tb_new_task_datetime.text()
        if self.ui.normal.isChecked():
            new_priority = 0
        elif self.ui.high.isChecked():
            new_priority = 1
        feedback = self.db.add_new_task(new_title, new_description, new_datetime, new_priority)
        if feedback == True:
            self.read_from_database()
            self.ui.tb_new_task_title.setText("")
            self.ui.tb_new_task_description.setText("")
            self.ui.normal.setChecked(True)
        else:
            msg_box = QMessageBox()
            msg_box.setText("There is a prublem")
            msg_box.exec_()



    def task_done(self, task_id, is_done):
         self.db.task_done(task_id, is_done)
         self.read_from_database()

    
    def remove(self, id):
        self.db.remove_task(id)
        # if feedback == True:
        self.read_from_database()
        # else:
        #     msg_box = QMessageBox()
        #     msg_box.setText("There is a prublem")
        #     msg_box.exec_()


    def show_info(self, task, description, datetime):
        msg_box = QMessageBox(text=f"Description : {description}\n\nDate and Time : {datetime}")
        msg_box.setWindowTitle(task)
        msg_box.exec()
        

    def read_from_database(self):
        for i in reversed(range(self.ui.gl_tasks.count())): 
            self.ui.gl_tasks.itemAt(i).widget().setParent(None)
        tasks = self.db.get_tasks()

        for i in range(len(tasks)):
            cb = QCheckBox()
            btn = QToolButton()
            btn2 = QToolButton()

            btn.setText("🗑")
            btn.setStyleSheet("font-size: 12pt; background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 0, 0, 69), stop:0.147727 rgba(255, 0, 219, 145), stop:0.295455 rgba(171, 0, 255, 69), stop:0.426136 rgba(160, 0, 255, 208), stop:0.477581 rgba(71, 160, 255, 130), stop:0.517045 rgba(0, 189, 255, 255), stop:0.642045 rgba(71, 255, 137, 130), stop:0.715909 rgba(204, 255, 0, 130), stop:0.857955 rgba(255, 87, 0, 69), stop:1 rgba(255, 0, 0, 69)); color: red; border-style: outset; border-width:3px; border-radius:5px; border-color: red;")
            btn2.setText("...")
            btn2.setStyleSheet("font-size: 12pt; background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 0, 0, 69), stop:0.147727 rgba(255, 0, 219, 145), stop:0.295455 rgba(171, 0, 255, 69), stop:0.426136 rgba(160, 0, 255, 208), stop:0.477581 rgba(71, 160, 255, 130), stop:0.517045 rgba(0, 189, 255, 255), stop:0.642045 rgba(71, 255, 137, 130), stop:0.715909 rgba(204, 255, 0, 130), stop:0.857955 rgba(255, 87, 0, 69), stop:1 rgba(255, 0, 0, 69)); color: rgb(255, 255, 255); border-style: outset; border-width:3px; border-radius:5px; border-color: white;")
            cb.setText(f"\t{i+1}.{tasks[i][1]}")
            if tasks[i][4] == 0:
                cb.setStyleSheet("font-size: 14pt; background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 0, 0, 69), stop:0.147727 rgba(255, 0, 219, 145), stop:0.295455 rgba(171, 0, 255, 69), stop:0.426136 rgba(160, 0, 255, 208), stop:0.477581 rgba(71, 160, 255, 130), stop:0.517045 rgba(0, 189, 255, 255), stop:0.642045 rgba(71, 255, 137, 130), stop:0.715909 rgba(204, 255, 0, 130), stop:0.857955 rgba(255, 87, 0, 69), stop:1 rgba(255, 0, 0, 69)); color: rgb(255, 255, 255); border-style: outset; border-width:3px; border-radius:5px; border-color: white; font-size: 12pt;")
            else:
                cb.setStyleSheet("font-size: 14pt; background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 0, 0, 69), stop:0.147727 rgba(255, 0, 219, 145), stop:0.295455 rgba(171, 0, 255, 69), stop:0.426136 rgba(160, 0, 255, 208), stop:0.477581 rgba(71, 160, 255, 130), stop:0.517045 rgba(0, 189, 255, 255), stop:0.642045 rgba(71, 255, 137, 130), stop:0.715909 rgba(204, 255, 0, 130), stop:0.857955 rgba(255, 87, 0, 69), stop:1 rgba(255, 0, 0, 69)); color: red; border-style: outset; border-width:3px; border-radius:5px; border-color: red; font-size: 12pt;")

            if tasks[i][5] == 1:
                cb.setChecked(True)
                if tasks[i][4] == 0:
                    cb.setStyleSheet("font-size: 14pt; background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 0, 0, 69), stop:0.147727 rgba(255, 0, 219, 145), stop:0.295455 rgba(171, 0, 255, 69), stop:0.426136 rgba(160, 0, 255, 208), stop:0.477581 rgba(71, 160, 255, 130), stop:0.517045 rgba(0, 189, 255, 255), stop:0.642045 rgba(71, 255, 137, 130), stop:0.715909 rgba(204, 255, 0, 130), stop:0.857955 rgba(255, 87, 0, 69), stop:1 rgba(255, 0, 0, 69)); color: rgb(255, 255, 255); border-style: outset; border-width:3px; border-radius:5px; border-color: white; text-decoration: line-through;")
                else:
                    cb.setStyleSheet("font-size: 14pt; background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 0, 0, 69), stop:0.147727 rgba(255, 0, 219, 145), stop:0.295455 rgba(171, 0, 255, 69), stop:0.426136 rgba(160, 0, 255, 208), stop:0.477581 rgba(71, 160, 255, 130), stop:0.517045 rgba(0, 189, 255, 255), stop:0.642045 rgba(71, 255, 137, 130), stop:0.715909 rgba(204, 255, 0, 130), stop:0.857955 rgba(255, 87, 0, 69), stop:1 rgba(255, 0, 0, 69)); color: red; border-style: outset; border-width:3px; border-radius:5px; border-color: red; text-decoration: line-through;")
            else:
                cb.setChecked(False)
                if tasks[i][4] == 0:
                    cb.setStyleSheet("font-size: 14pt; background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 0, 0, 69), stop:0.147727 rgba(255, 0, 219, 145), stop:0.295455 rgba(171, 0, 255, 69), stop:0.426136 rgba(160, 0, 255, 208), stop:0.477581 rgba(71, 160, 255, 130), stop:0.517045 rgba(0, 189, 255, 255), stop:0.642045 rgba(71, 255, 137, 130), stop:0.715909 rgba(204, 255, 0, 130), stop:0.857955 rgba(255, 87, 0, 69), stop:1 rgba(255, 0, 0, 69)); color: rgb(255, 255, 255); border-style: outset; border-width:3px; border-radius:5px; border-color: white;")
                else:
                    cb.setStyleSheet("font-size: 14pt; background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 0, 0, 69), stop:0.147727 rgba(255, 0, 219, 145), stop:0.295455 rgba(171, 0, 255, 69), stop:0.426136 rgba(160, 0, 255, 208), stop:0.477581 rgba(71, 160, 255, 130), stop:0.517045 rgba(0, 189, 255, 255), stop:0.642045 rgba(71, 255, 137, 130), stop:0.715909 rgba(204, 255, 0, 130), stop:0.857955 rgba(255, 87, 0, 69), stop:1 rgba(255, 0, 0, 69)); color: red; border-style: outset; border-width:3px; border-radius:5px; border-color: red;")


            self.ui.gl_tasks.addWidget(cb, i, 0)
            self.ui.gl_tasks.addWidget(btn, i, 3)
            self.ui.gl_tasks.addWidget(btn2, i, 2)

            cb.clicked.connect(partial(self.task_done, tasks[i][0], tasks[i][5]))
            btn.clicked.connect(partial(self.remove, tasks[i][0]))
            btn2.clicked.connect(partial(self.show_info, tasks[i][1], tasks[i][2], tasks[i][3]))





if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()