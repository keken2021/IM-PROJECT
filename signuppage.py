from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_signupwindow(object):
    def openSignIn(self):
        from loginpage import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show() 
        signupwindow.hide()

    def setupUi(self, signupwindow):
        signupwindow.setObjectName("signupwindow")
        signupwindow.resize(1182, 739)
        signupwindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(signupwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 460, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:#6c757d;\n"
"padding-bottom:8px;\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 170, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:#6c757d;\n"
"padding-bottom:8px;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 320, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:#6c757d;\n"
"padding-bottom:8px;\n"
"")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(700, 320, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:#6c757d;\n"
"padding-bottom:8px;\n"
"")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(700, 170, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:#6c757d;\n"
"padding-bottom:8px;\n"
"")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(700, 460, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:#6c757d;\n"
"padding-bottom:8px;\n"
"")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(500, 650, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Inter Light")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.signUpbutton = QtWidgets.QPushButton(self.centralwidget)
        self.signUpbutton.setGeometry(QtCore.QRect(390, 570, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.signUpbutton.setFont(font)
        self.signUpbutton.setStyleSheet("background-color: rgb(0, 122, 255);\n"
"border-radius:12px;\n"
"color:#fff;")
        self.signUpbutton.setObjectName("signUpbutton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 100, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Inter Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 40, 501, 61))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 122, 255);")
        self.label.setObjectName("label")
        self.SignInbutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.openSignIn())
        self.SignInbutton.setGeometry(QtCore.QRect(510, 680, 161, 28))
        font = QtGui.QFont()
        font.setFamily("Inter SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.SignInbutton.setFont(font)
        self.SignInbutton.setStyleSheet("color: rgb(0, 122, 255);\n"
"border:none;\n"
"text-align: center;")
        self.SignInbutton.setObjectName("SignInbutton")
        signupwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(signupwindow)
        self.statusbar.setObjectName("statusbar")
        signupwindow.setStatusBar(self.statusbar)

        self.retranslateUi(signupwindow)
        QtCore.QMetaObject.connectSlotsByName(signupwindow)

    def retranslateUi(self, signupwindow):
        _translate = QtCore.QCoreApplication.translate
        signupwindow.setWindowTitle(_translate("signupwindow", "MainWindow"))
        self.lineEdit_2.setText(_translate("signupwindow", "Phone number"))
        self.lineEdit_2.setPlaceholderText(_translate("signupwindow", "Password"))
        self.lineEdit.setText(_translate("signupwindow", "First name"))
        self.lineEdit.setPlaceholderText(_translate("signupwindow", "Username"))
        self.lineEdit_3.setText(_translate("signupwindow", "Last name"))
        self.lineEdit_3.setPlaceholderText(_translate("signupwindow", "Username"))
        self.lineEdit_4.setText(_translate("signupwindow", "Username"))
        self.lineEdit_4.setPlaceholderText(_translate("signupwindow", "Username"))
        self.lineEdit_5.setText(_translate("signupwindow", "Email"))
        self.lineEdit_5.setPlaceholderText(_translate("signupwindow", "Username"))
        self.lineEdit_6.setText(_translate("signupwindow", "Password"))
        self.lineEdit_6.setPlaceholderText(_translate("signupwindow", "Password"))
        self.label_4.setText(_translate("signupwindow", "Already have an account?"))
        self.signUpbutton.setText(_translate("signupwindow", "Sign up"))
        self.label_2.setText(_translate("signupwindow", "Get started today!"))
        self.label.setText(_translate("signupwindow", "Create account"))
        self.SignInbutton.setText(_translate("signupwindow", "Sign in"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    signupwindow = QtWidgets.QMainWindow()
    ui = Ui_signupwindow()
    ui.setupUi(signupwindow)
    signupwindow.show()
    sys.exit(app.exec_())
