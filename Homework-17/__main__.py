import math
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader


#_______________________________________________________________________________
def num_1():
    if len(window.txtbox.text()) < 20:
        window.txtbox.setText(window.txtbox.text()+'1')

def num_2():
    if len(window.txtbox.text()) < 20:
        window.txtbox.setText(window.txtbox.text()+'2')

def num_3():
    if len(window.txtbox.text()) < 20:
        window.txtbox.setText(window.txtbox.text()+'3')

def num_4():
    if len(window.txtbox.text()) < 20:
        window.txtbox.setText(window.txtbox.text()+'4')

def num_5():
    if len(window.txtbox.text()) < 20:
        window.txtbox.setText(window.txtbox.text()+'5')

def num_6():
    if len(window.txtbox.text()) < 20:
        window.txtbox.setText(window.txtbox.text()+'6')

def num_7():
    if len(window.txtbox.text()) < 20:
        window.txtbox.setText(window.txtbox.text()+'7')

def num_8():
    if len(window.txtbox.text()) < 20:
        window.txtbox.setText(window.txtbox.text()+'8')

def num_9():
    if len(window.txtbox.text()) < 20:
        window.txtbox.setText(window.txtbox.text()+'9')

def num_0():
    if len(window.txtbox.text()) < 20:
        window.txtbox.setText(window.txtbox.text()+'0')

def point():
    if len(window.txtbox.text()) < 20:
        window.txtbox.setText(window.txtbox.text()+'.')

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

window = loader.load('calculator.ui')
window.show()

window.num1.clicked.connect(num_1)
window.num2.clicked.connect(num_2)
window.num3.clicked.connect(num_3)
window.num4.clicked.connect(num_4)
window.num5.clicked.connect(num_5)
window.num6.clicked.connect(num_6)
window.num7.clicked.connect(num_7)
window.num8.clicked.connect(num_8)
window.num9.clicked.connect(num_9)
window.num0.clicked.connect(num_0)
window.point.clicked.connect(point)
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