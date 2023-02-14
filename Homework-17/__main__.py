import math
from functools import partial
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader


#_______________________________________________________________________________
def num(x):
    if len(window.txtbox.text()) < 20:
        window.txtbox.setText(window.txtbox.text()+x)

def ac():
    window.txtbox.setText('')

def sum():
    global fn
    global op
    fn = float(window.txtbox.text())
    op = "sum"
    ac()

def sub():
    global fn
    global op
    fn = float(window.txtbox.text())
    op = "sub"
    ac()

def mul():
    global fn
    global op
    fn = float(window.txtbox.text())
    op = "mul"
    ac()

def divide():
    global fn
    global op
    fn = float(window.txtbox.text())
    op = "divide"
    ac()


def result():
    sn = float(window.txtbox.text())
    if op == "sum":
        r = fn + sn
    elif op == "sub":
        r = fn - sn
    elif op == "mul":
        r = fn * sn
    elif op == "divide":
        r = fn /sn

    if len(str(r)) < 20:
        window.txtbox.setText(str(r))
    else:
       window.txtbox.setText(str(format(r , "e"))) 

def sin():
    r = math.sin(float(window.txtbox.text()))
    if len(str(r)) < 20:
        window.txtbox.setText(str(r))
    else:
       window.txtbox.setText(str(format(r , "e")))

def cos():
    r = math.cos(float(window.txtbox.text()))
    if len(str(r)) < 20:
        window.txtbox.setText(str(r))
    else:
       window.txtbox.setText(str(format(r , "e"))) 

def tan():
    r = math.tan(float(window.txtbox.text()))
    if len(str(r)) < 20:
        window.txtbox.setText(str(r))
    else:
       window.txtbox.setText(str(format(r , "e"))) 

def cot():
    r = 1/math.tan(float(window.txtbox.text()))
    if len(str(r)) < 20:
        window.txtbox.setText(str(r))
    else:
       window.txtbox.setText(str(format(r , "e"))) 

def log():
    r = math.log(float(window.txtbox.text()))
    if len(str(r)) < 20:
        window.txtbox.setText(str(r))
    else:
       window.txtbox.setText(str(format(r , "e"))) 

def sqrt():
    r = math.sqrt(x)(float(window.txtbox.text()))
    if len(str(r)) < 20:
        window.txtbox.setText(str(r))
    else:
       window.txtbox.setText(str(format(r , "e"))) 

def reverse():
    window.txtbox.setText(str(float(window.txtbox.text())*-1))

def percent():
    window.txtbox.setText(str(float(window.txtbox.text())/100))

#____________________________________________________________________________________

app = QApplication()

loader = QUiLoader()

window = loader.load('main_window.ui')
window.show()

window.num1.clicked.connect(partial(num, "1"))
window.num2.clicked.connect(partial(num, "2"))
window.num3.clicked.connect(partial(num, "3"))
window.num4.clicked.connect(partial(num, "4"))
window.num5.clicked.connect(partial(num, "5"))
window.num6.clicked.connect(partial(num, "6"))
window.num7.clicked.connect(partial(num, "7"))
window.num8.clicked.connect(partial(num, "8"))
window.num9.clicked.connect(partial(num, "9"))
window.num0.clicked.connect(partial(num, "0"))
window.point.clicked.connect(partial(num, "."))
window.ac.clicked.connect(ac)
window.sum.clicked.connect(sum)
window.sub.clicked.connect(sub)
window.duplicate.clicked.connect(mul)
window.divide.clicked.connect(divide)
window.sin.clicked.connect(sin)
window.result.clicked.connect(result)
window.cos.clicked.connect(cos)
window.log.clicked.connect(log)
window.cot.clicked.connect(cot)
window.tan.clicked.connect(tan)
window.sqrt.clicked.connect(sqrt)
window.reverse.clicked.connect(reverse)
window.percent.clicked.connect(percent)




app.exec()