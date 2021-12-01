import sys
import random
from PySide6 import QtCore, QtWidgets



class MyWidget(QtWidgets.QWidget):
    def __init__(self):



        super().__init__()

        self.number1 = ""
        self.number2 = ""
        self.result = 0
        self.okay = False
        self.islem = ""
        self.processcount = 0

        self.setWindowTitle("Calculator")
        self.setFixedWidth(450)
        self.setFixedHeight(600)

        self.setStyleSheet("background-color: black")

        self.firststylesheet = """
            QPushButton{
                background-color: #D4D4D2;
                font-size: 25px;
                color: black;
                padding: 15px;
                border-radius: 25px;
                font-family: Helvetica, Sans-Serif;
            }
        """

        self.secondstylesheet = """
            QPushButton{
                background-color: #505050;
                font-size: 25px;
                color: white;
                padding: 15px;
                border-radius: 25px;
                font-family: Helvetica, Sans-Serif;
            }
        """

        self.thirdstylesheet = """
            QPushButton{
                background-color: #FF9500;
                font-size: 25px;
                color: white;
                padding: 15px;
                border-radius: 25px;
                font-family: Helvetica, Sans-Serif;
            }
        """




        self.layout = QtWidgets.QGridLayout()

        self.OutputScreen = QtWidgets.QLabel("0");
        self.OutputScreen.setStyleSheet("color: white; font-size:50px; font-family: Helvetica, Sans-Serif;")
        self.OutputScreen.setFixedHeight(200)
        self.OutputScreen.setAlignment(QtCore.Qt.AlignVCenter)

        self.buttonclr = QtWidgets.QPushButton("C")
        self.buttonminus = QtWidgets.QPushButton("-/+")
        self.buttonmod = QtWidgets.QPushButton("%")
        self.buttoncomma = QtWidgets.QPushButton(",")
        self.buttondiv = QtWidgets.QPushButton("÷")
        self.buttonmulti = QtWidgets.QPushButton("*")
        self.buttondelete = QtWidgets.QPushButton("-")
        self.buttonplus = QtWidgets.QPushButton("+")
        self.buttonequal = QtWidgets.QPushButton("=")
        self.button0 = QtWidgets.QPushButton("0")
        self.button1 = QtWidgets.QPushButton("1")
        self.button2 = QtWidgets.QPushButton("2")
        self.button3 = QtWidgets.QPushButton("3")
        self.button4 = QtWidgets.QPushButton("4")
        self.button5 = QtWidgets.QPushButton("5")
        self.button6 = QtWidgets.QPushButton("6")
        self.button7 = QtWidgets.QPushButton("7")
        self.button8 = QtWidgets.QPushButton("8")
        self.button9 = QtWidgets.QPushButton("9")

        self.buttonclr.setStyleSheet(self.firststylesheet)
        self.buttonminus.setStyleSheet(self.firststylesheet)
        self.buttonmod.setStyleSheet(self.firststylesheet)
        self.buttondiv.setStyleSheet(self.thirdstylesheet)
        self.button7.setStyleSheet(self.secondstylesheet)
        self.button8.setStyleSheet(self.secondstylesheet)
        self.button9.setStyleSheet(self.secondstylesheet)
        self.buttonmulti.setStyleSheet(self.thirdstylesheet)

        self.button4.setStyleSheet(self.secondstylesheet)
        self.button5.setStyleSheet(self.secondstylesheet)
        self.button6.setStyleSheet(self.secondstylesheet)
        self.buttondelete.setStyleSheet(self.thirdstylesheet)

        self.button1.setStyleSheet(self.secondstylesheet)
        self.button2.setStyleSheet(self.secondstylesheet)
        self.button3.setStyleSheet(self.secondstylesheet)
        self.buttonplus.setStyleSheet(self.thirdstylesheet)

        self.button0.setStyleSheet(self.secondstylesheet)
        self.buttoncomma.setStyleSheet(self.secondstylesheet)
        self.buttonequal.setStyleSheet(self.thirdstylesheet)


        self.layout.addWidget(self.OutputScreen, 0, 0, 1, 4)
        self.layout.setSpacing(10)
        self.layout.addWidget(self.buttonclr, 1, 0)
        self.layout.addWidget(self.buttonminus, 1, 1)
        self.layout.addWidget(self.buttonmod, 1, 2)
        self.layout.addWidget(self.buttondiv, 1, 3)
        self.layout.addWidget(self.button7, 2, 0)
        self.layout.addWidget(self.button8, 2, 1)
        self.layout.addWidget(self.button9, 2, 2)
        self.layout.addWidget(self.buttonmulti, 2, 3)
        self.layout.addWidget(self.button4, 3, 0)
        self.layout.addWidget(self.button5, 3, 1)
        self.layout.addWidget(self.button6, 3, 2)
        self.layout.addWidget(self.buttondelete, 3, 3)
        self.layout.addWidget(self.button1, 4, 0)
        self.layout.addWidget(self.button2, 4, 1)
        self.layout.addWidget(self.button3, 4, 2)
        self.layout.addWidget(self.buttonplus, 4, 3)
        self.layout.addWidget(self.button0, 5, 0, 1, 2)
        self.layout.addWidget(self.buttoncomma, 5, 2)
        self.layout.addWidget(self.buttonequal, 5, 3)

        self.buttonclr.setCursor(QtCore.Qt.PointingHandCursor)
        self.buttonminus.setCursor(QtCore.Qt.PointingHandCursor)
        self.buttonmod.setCursor(QtCore.Qt.PointingHandCursor)
        self.buttoncomma.setCursor(QtCore.Qt.PointingHandCursor)
        self.buttondiv.setCursor(QtCore.Qt.PointingHandCursor)
        self.buttonmulti.setCursor(QtCore.Qt.PointingHandCursor)
        self.buttondelete.setCursor(QtCore.Qt.PointingHandCursor)
        self.buttonplus.setCursor(QtCore.Qt.PointingHandCursor)
        self.buttonequal.setCursor(QtCore.Qt.PointingHandCursor)
        self.button0.setCursor(QtCore.Qt.PointingHandCursor)
        self.button1.setCursor(QtCore.Qt.PointingHandCursor)
        self.button2.setCursor(QtCore.Qt.PointingHandCursor)
        self.button3.setCursor(QtCore.Qt.PointingHandCursor)
        self.button4.setCursor(QtCore.Qt.PointingHandCursor)
        self.button5.setCursor(QtCore.Qt.PointingHandCursor)
        self.button6.setCursor(QtCore.Qt.PointingHandCursor)
        self.button7.setCursor(QtCore.Qt.PointingHandCursor)
        self.button8.setCursor(QtCore.Qt.PointingHandCursor)
        self.button9.setCursor(QtCore.Qt.PointingHandCursor)

        self.button0.clicked.connect(self.click0event)
        self.button1.clicked.connect(self.click1event)
        self.button2.clicked.connect(self.click2event)
        self.button3.clicked.connect(self.click3event)
        self.button4.clicked.connect(self.click4event)
        self.button5.clicked.connect(self.click5event)
        self.button6.clicked.connect(self.click6event)
        self.button7.clicked.connect(self.click7event)
        self.button8.clicked.connect(self.click8event)
        self.button9.clicked.connect(self.click9event)
        self.buttonclr.clicked.connect(self.clickClear)
        self.buttonplus.clicked.connect(self.clickplus)
        self.buttondelete.clicked.connect(self.clickminus)
        self.buttonmulti.clicked.connect(self.clickmulti)
        self.buttondiv.clicked.connect(self.clickdiv)
        self.buttonequal.clicked.connect(self.giveResult)

        print(self.heightForWidth)


        self.setLayout(self.layout)


    def click1event(self):
        self.OutputScreen.setText("")
        if not self.okay:
            self.number1 += "1";
            self.OutputScreen.setText(self.number1)
            print(self.number1)

    def click1event(self):
        self.OutputScreen.setText("")
        if not self.okay:
            self.number1 += "1";
            self.OutputScreen.setText(self.number1)
            print(self.number1)

    def click0event(self):
        self.OutputScreen.setText("")
        if not self.okay:
            self.number1 += "0"
            self.OutputScreen.setText(self.number1)
            print(self.number1)

        else:
            self.number2 += "0"
            self.OutputScreen.setText(self.number2)
            print(self.number2)

    def click1event(self):
        self.OutputScreen.setText("")
        if not self.okay:
            self.number1 += "1"
            self.OutputScreen.setText(self.number1)
            print(self.number1)

        else:
            self.number2 += "1"
            self.OutputScreen.setText(self.number2)
            print(self.number2)

    def click2event(self):
        self.OutputScreen.setText("")
        if not self.okay:
            self.number1 += "2"
            self.OutputScreen.setText(self.number1)
            print(self.number1)

        else:
            self.number2 += "2"
            self.OutputScreen.setText(self.number2)
            print(self.number2)

    def click3event(self):
        self.OutputScreen.setText("")
        if not self.okay:
            self.number1 += "3"
            self.OutputScreen.setText(self.number1)
            print(self.number1)

        else:
            self.number2 += "3"
            self.OutputScreen.setText(self.number2)
            print(self.number2)

    def click4event(self):
        self.OutputScreen.setText("")
        if not self.okay:
            self.number1 += "4"
            self.OutputScreen.setText(self.number1)
            print(self.number1)

        else:
            self.number2 += "4"
            self.OutputScreen.setText(self.number2)
            print(self.number2)

    def click5event(self):
        self.OutputScreen.setText("")
        if not self.okay:
            self.number1 += "5"
            self.OutputScreen.setText(self.number1)
            print(self.number1)

        else:
            self.number2 += "5"
            self.OutputScreen.setText(self.number2)
            print(self.number2)

    def click6event(self):
        self.OutputScreen.setText("")
        if not self.okay:
            self.number1 += "6"
            self.OutputScreen.setText(self.number1)
            print(self.number1)

        else:
            self.number2 += "6"
            self.OutputScreen.setText(self.number2)
            print(self.number2)

    def click7event(self):
        self.OutputScreen.setText("")
        if not self.okay:
            self.number1 += "7"
            self.OutputScreen.setText(self.number1)
            print(self.number1)

        else:
            self.number2 += "7"
            self.OutputScreen.setText(self.number2)
            print(self.number2)

    def click8event(self):
        self.OutputScreen.setText("")
        if not self.okay:
            self.number1 += "8"
            self.OutputScreen.setText(self.number1)
            print(self.number1)

        else:
            self.number2 += "8"
            self.OutputScreen.setText(self.number2)
            print(self.number2)

    def click9event(self):
        self.OutputScreen.setText("")
        if not self.okay:
            self.number1 += "9"
            self.OutputScreen.setText(self.number1)
            print(self.number1)

        else:
            self.number2 += "9"
            self.OutputScreen.setText(self.number2)
            print(self.number2)

    def clickClear(self):
        print("clicked clear button numbers are resetting")
        self.OutputScreen.setText("0")
        self.number1 = ""
        self.number2 = ""
        self.islem = ""
        self.result = 0
        self.okay = False
        self.processcount = 0

    def clickplus(self):
        print("clicked plus numbers are changed")
        self.OutputScreen.setText("")
        self.islem = "plus"
        if not self.okay:
            self.okay = True
        else:
            self.okay = False




    def clickminus(self):
        print("clicked minus numbers are changed")
        self.OutputScreen.setText("")
        self.islem = "minus"
        if not self.okay:
            self.okay = True
        else:
            self.okay = False

    def clickmulti(self):
        print("clicked multi numbers are changed")
        self.OutputScreen.setText("")
        self.islem = "multi"
        if not self.okay:
            self.okay = True
        else:
            self.okay = False

    def clickdiv(self):
        print("clicked div numbers are changed")
        self.OutputScreen.setText("")
        self.islem = "div"
        if not self.okay:
            self.okay = True
        else:
            self.okay = False

    def giveResult(self):
        print("clicked equals calculating result and reset number")
        if self.islem == "plus":
            self.result = int(self.number1) + int(self.number2)
            self.OutputScreen.setText(str(self.result))
            self.number1 = ""
            self.number2 = ""

        elif self.islem == "minus":
            if int(self.number1) >= int(self.number2):
                self.result = int(self.number1) - int(self.number2)
                self.OutputScreen.setText(str(self.result))
                self.number1 = ""
                self.number2 = ""
            else:
                self.result = int(self.number2) - int(self.number1)
                self.OutputScreen.setText(str(self.result))
                self.number1 = ""
                self.number2 = ""

        elif self.islem == "multi":
            self.result = int(self.number1) * int(self.number2)
            self.OutputScreen.setText(str(self.result))
            self.number1 = ""
            self.number2 = ""

        elif self.islem == "div":
            if int(self.number1) >= int(self.number2):
                self.result = int(self.number1) / int(self.number2)
                self.OutputScreen.setText(str(self.result))
                self.number1 = ""
                self.number2 = ""
            else:
                self.result = int(self.number2) / int(self.number1)
                self.OutputScreen.setText(str(self.result))
                self.number1 = ""
                self.number2 = ""


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
