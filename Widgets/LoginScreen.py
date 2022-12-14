# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Splah_Screen_L_circul.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_loginSplashScreen(object):
    def setupUi(self, loginSplashScreen):
        loginSplashScreen.setObjectName("loginSplashScreen")
        loginSplashScreen.resize(341, 341)
        loginSplashScreen.setMinimumSize(341, 341)
        loginSplashScreen.setMaximumSize(QtCore.QSize(600, 520))
        self.centralwidget = QtWidgets.QWidget(loginSplashScreen)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 311))
        self.centralwidget.setMaximumSize(QtCore.QSize(600, 520))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("background-color: rgb(56, 58, 89);\n"
"color:rgb(220, 220, 220);\n"
"border-radius:10px;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.SpashScreen = QtWidgets.QWidget()
        self.SpashScreen.setObjectName("SpashScreen")
        self.stackedWidget.addWidget(self.SpashScreen)
        self.login = QtWidgets.QWidget()
        self.login.setObjectName("login")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.login)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.principal_frame = QtWidgets.QFrame(self.login)
        self.principal_frame.setMaximumSize(QtCore.QSize(16777215, 500))
        self.principal_frame.setStyleSheet("background-color: rgb(56, 58, 89);\n"
"color:rgb(220, 220, 220);\n"
"border-radius:10px;")
        self.principal_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.principal_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.principal_frame.setObjectName("principal_frame")
        self.rect_logo = QtWidgets.QFrame(self.principal_frame)
        self.rect_logo.setGeometry(QtCore.QRect(0, 50, 321, 91))
        self.rect_logo.setMinimumSize(QtCore.QSize(0, 0))
        self.rect_logo.setMaximumSize(QtCore.QSize(321, 91))
        self.rect_logo.setStyleSheet("border-radius:10px;")
        self.rect_logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rect_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rect_logo.setObjectName("rect_logo")
        self.nameY = QtWidgets.QLabel(self.rect_logo)
        self.nameY.setGeometry(QtCore.QRect(101, 50, 189, 43))
        self.nameY.setMinimumSize(QtCore.QSize(0, 43))
        self.nameY.setMaximumSize(QtCore.QSize(16777215, 43))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(30)
        self.nameY.setFont(font)
        self.nameY.setStyleSheet("color: rgb(254, 121, 199);")
        self.nameY.setAlignment(QtCore.Qt.AlignCenter)
        self.nameY.setObjectName("nameY")
        self.nameYourA = QtWidgets.QLabel(self.rect_logo)
        self.nameYourA.setGeometry(QtCore.QRect(101, 10, 189, 43))
        self.nameYourA.setMinimumSize(QtCore.QSize(0, 43))
        self.nameYourA.setMaximumSize(QtCore.QSize(16777215, 43))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(30)
        self.nameYourA.setFont(font)
        self.nameYourA.setStyleSheet("color: rgb(254, 121, 199);")
        self.nameYourA.setAlignment(QtCore.Qt.AlignCenter)
        self.nameYourA.setObjectName("nameYourA")
        self.logo = QtWidgets.QLabel(self.rect_logo)
        self.logo.setGeometry(QtCore.QRect(10, 0, 90, 90))
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.discricao = QtWidgets.QLabel(self.principal_frame)
        self.discricao.setGeometry(QtCore.QRect(0, 260, 320, 20))
        self.discricao.setMaximumSize(QtCore.QSize(1234, 1234))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.discricao.setFont(font)
        self.discricao.setStyleSheet("QLabel{color: rgba(98, 114, 164, 255)}")
        self.discricao.setAlignment(QtCore.Qt.AlignCenter)
        self.discricao.setObjectName("discricao")
        self.ld_Pass = QtWidgets.QLineEdit(self.principal_frame)
        self.ld_Pass.setGeometry(QtCore.QRect(20, 340, 280, 40))
        self.ld_Pass.setMaximumSize(QtCore.QSize(280, 40))
        self.ld_Pass.setStyleSheet("QLineEdit{\n"
"background-color: rgba(98, 114, 164, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;\n"
"border    :    2px solid    rgba(98, 114, 164, 255);\n"
"}\n"
"QLineEdit:hover{\n"
"border    :    3px solid   rgba(123, 61, 184, 255)\n"
"}\n"
"QLineEdit:focus{\n"
"border    :    3px solid  rgba(171, 85, 255, 255)\n"
"}")
        self.ld_Pass.setText("")
        self.ld_Pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ld_Pass.setObjectName("ld_Pass")
        self.logar = QtWidgets.QPushButton(self.principal_frame)
        self.logar.setGeometry(QtCore.QRect(40, 390, 240, 41))
        self.logar.setMaximumSize(QtCore.QSize(240, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.logar.setFont(font)
        self.logar.setStyleSheet("QPushButton{\n"
"background-color: rgba(225, 107, 178, 255);\n"
"border-radius:10px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(206, 98, 163, 255);\n"
"border-radius:10px;}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgba(254, 121, 199, 255);\n"
"border-radius:10px;\n"
"\n"
"}")
        self.logar.setObjectName("loguin")
        self.ld_user = QtWidgets.QLineEdit(self.principal_frame)
        self.ld_user.setGeometry(QtCore.QRect(20, 290, 280, 40))
        self.ld_user.setMaximumSize(QtCore.QSize(280, 40))
        self.ld_user.setStyleSheet("QLineEdit{\n"
"background-color: rgba(98, 114, 164, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;\n"
"border    :    2px solid    rgba(98, 114, 164, 255);\n"
"}\n"
"QLineEdit:hover{\n"
"border    :    3px solid   rgba(123, 61, 184, 255)\n"
"}\n"
"QLineEdit:focus{\n"
"border    :    3px solid  rgba(171, 85, 255, 255)\n"
"}")
        self.ld_user.setInputMask("")
        self.ld_user.setText("")
        self.ld_user.setObjectName("ld_user")
        self.yourApp = QtWidgets.QLabel(self.principal_frame)
        self.yourApp.setGeometry(QtCore.QRect(0, 220, 320, 31))
        self.yourApp.setMaximumSize(QtCore.QSize(341, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.yourApp.setFont(font)
        self.yourApp.setStyleSheet("color: rgb(98, 114, 164);")
        self.yourApp.setAlignment(QtCore.Qt.AlignCenter)
        self.yourApp.setObjectName("yourApp")
        self.dock_frame = QtWidgets.QFrame(self.principal_frame)
        self.dock_frame.setGeometry(QtCore.QRect(0, 0, 321, 40))
        self.dock_frame.setStyleSheet("background-color: rgb(65, 68, 104);\n"
"border-bottom-right-radius:0px;\n"
"border-bottom-left-radius:0px;")
        self.dock_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dock_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dock_frame.setObjectName("dock_frame")
        self.fechar = QtWidgets.QPushButton(self.dock_frame)
        self.fechar.setGeometry(QtCore.QRect(290, 10, 20, 21))
        self.fechar.setStyleSheet("QPushButton{\n"
"background-color: rgb(254, 121, 199);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(254, 201, 239);\n"
"border-radius:5px;\n"
"}")
        self.fechar.setIconSize(QtCore.QSize(16, 18))
        self.fechar.setObjectName("fechar")
        self.verticalLayout_4.addWidget(self.principal_frame)
        self.stackedWidget.addWidget(self.login)
        self.verticalLayout.addWidget(self.stackedWidget)
        loginSplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(loginSplashScreen)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(loginSplashScreen)

    def retranslateUi(self, loginSplashScreen):
        _translate = QtCore.QCoreApplication.translate
        loginSplashScreen.setWindowTitle(_translate("loginSplashScreen", "MainWindow"))
        self.nameY.setText(_translate("loginSplashScreen", "<html><head/><body><p><span style=\" font-size:20pt;\">NAME</span></p></body></html>"))
        self.nameYourA.setText(_translate("loginSplashScreen", "<html><head/><body><p><span style=\" font-weight:600;\">YOUR</span> APP</p><p>    </p></body></html>"))
        self.discricao.setText(_translate("loginSplashScreen", "Username or email address and password"))
        self.ld_Pass.setPlaceholderText(_translate("loginSplashScreen", " Password"))
        self.logar.setText(_translate("loginSplashScreen", "Sign in"))
        self.ld_user.setPlaceholderText(_translate("loginSplashScreen", " Username or Email"))
        self.yourApp.setText(_translate("loginSplashScreen", "Sign in Your App"))
        self.fechar.setText(_translate("loginSplashScreen", "X"))
        self.logo.setPixmap(QtGui.QPixmap('../imagens/yourApp.png'))
        self.stackedWidget.setCurrentWidget(self.principal_frame)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginSplashScreen = QtWidgets.QMainWindow()
    ui = Ui_loginSplashScreen()
    ui.setupUi(loginSplashScreen)
    loginSplashScreen.show()
    sys.exit(app.exec())
