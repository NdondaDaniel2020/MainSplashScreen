# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SplahScreenkmSUTE.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QToolButton, QVBoxLayout, QWidget)
import imagens.imag.img_rc

class Ui_loginSplashScreen(object):
    def setupUi(self, loginSplashScreen):
        if not loginSplashScreen.objectName():
            loginSplashScreen.setObjectName(u"loginSplashScreen")
        loginSplashScreen.resize(322, 300)
        loginSplashScreen.setMaximumSize(QSize(600, 520))
        self.centralwidget = QWidget(loginSplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 300))
        self.centralwidget.setMaximumSize(QSize(600, 520))
        self.centralwidget.setStyleSheet(u"\n"
"QToolTip {\n"
" 	color: #ffffff;\n"
"	background-color:rgb(56, 58, 89);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid #fe00c7;\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"	border-radius:none;\n"
"	\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(300, 0))
        self.stackedWidget.setMaximumSize(QSize(300, 16777215))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(56, 58, 89);\n"
"color:rgb(220, 220, 220);\n"
"border-radius:10px;")
        self.SpashScreen = QWidget()
        self.SpashScreen.setObjectName(u"SpashScreen")
        self.stackedWidget.addWidget(self.SpashScreen)
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.verticalLayout_4 = QVBoxLayout(self.login)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.principal_frame = QFrame(self.login)
        self.principal_frame.setObjectName(u"principal_frame")
        self.principal_frame.setMaximumSize(QSize(16777215, 500))
        self.principal_frame.setFrameShape(QFrame.StyledPanel)
        self.principal_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.principal_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.centro = QFrame(self.principal_frame)
        self.centro.setObjectName(u"centro")
        self.centro.setStyleSheet(u"")
        self.centro.setFrameShape(QFrame.StyledPanel)
        self.centro.setFrameShadow(QFrame.Raised)
        self.rect_logo = QFrame(self.centro)
        self.rect_logo.setObjectName(u"rect_logo")
        self.rect_logo.setGeometry(QRect(9, 50, 291, 100))
        self.rect_logo.setMinimumSize(QSize(0, 100))
        self.rect_logo.setMaximumSize(QSize(328, 100))
        self.rect_logo.setStyleSheet(u"border-radius:10px;")
        self.rect_logo.setFrameShape(QFrame.StyledPanel)
        self.rect_logo.setFrameShadow(QFrame.Raised)
        self.logo = QLabel(self.rect_logo)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(0, -11, 90, 111))
        self.logo.setMinimumSize(QSize(90, 90))
        self.logo.setStyleSheet(u"background-image: url(:/img/logo2.png);\n"
"background-position: center;\n"
"background-repeat: no-reperat;")
        self.name = QLabel(self.rect_logo)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(140, 53, 81, 31))
        font = QFont()
        font.setPointSize(21)
        self.name.setFont(font)
        self.name.setStyleSheet(u"color: rgb(255, 120, 213);")
        self.nameYourA = QLabel(self.rect_logo)
        self.nameYourA.setObjectName(u"nameYourA")
        self.nameYourA.setGeometry(QRect(97, 10, 186, 51))
        self.nameYourA.setMinimumSize(QSize(0, 0))
        self.nameYourA.setMaximumSize(QSize(16777215, 1234))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(30)
        self.nameYourA.setFont(font1)
        self.nameYourA.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"")
        self.nameYourA.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.yourApp = QLabel(self.centro)
        self.yourApp.setObjectName(u"yourApp")
        self.yourApp.setGeometry(QRect(0, 195, 300, 34))
        self.yourApp.setMaximumSize(QSize(341, 34))
        font2 = QFont()
        font2.setPointSize(20)
        self.yourApp.setFont(font2)
        self.yourApp.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.yourApp.setAlignment(Qt.AlignCenter)
        self.discricao = QLabel(self.centro)
        self.discricao.setObjectName(u"discricao")
        self.discricao.setGeometry(QRect(-1, 245, 300, 20))
        self.discricao.setMinimumSize(QSize(0, 20))
        self.discricao.setMaximumSize(QSize(1234, 20))
        font3 = QFont()
        font3.setPointSize(10)
        self.discricao.setFont(font3)
        self.discricao.setStyleSheet(u"QLabel{color: rgba(98, 114, 164, 255)}")
        self.discricao.setAlignment(Qt.AlignCenter)
        self.ld_user = QLineEdit(self.centro)
        self.ld_user.setObjectName(u"ld_user")
        self.ld_user.setGeometry(QRect(25, 275, 250, 40))
        self.ld_user.setMinimumSize(QSize(250, 40))
        self.ld_user.setMaximumSize(QSize(250, 40))
        font4 = QFont()
        font4.setFamilies([u"MS Shell Dlg 2"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        self.ld_user.setFont(font4)
        self.ld_user.setStyleSheet(u"QLineEdit{\n"
"background-color: rgba(98, 114, 164, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;\n"
"border	:	2px solid    rgba(98, 114, 164, 255);\n"
"}\n"
"QLineEdit:hover{\n"
"border	:	3px solid   rgba(123, 61, 184, 255)\n"
"}\n"
"QLineEdit:focus{\n"
"border	:	3px solid  rgba(171, 85, 255, 255)\n"
"}")
        self.ld_Pass = QLineEdit(self.centro)
        self.ld_Pass.setObjectName(u"ld_Pass")
        self.ld_Pass.setGeometry(QRect(25, 329, 250, 40))
        self.ld_Pass.setMinimumSize(QSize(250, 40))
        self.ld_Pass.setMaximumSize(QSize(250, 40))
        self.ld_Pass.setStyleSheet(u"QLineEdit{\n"
"background-color: rgba(98, 114, 164, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;\n"
"border	:	2px solid    rgba(98, 114, 164, 255);\n"
"}\n"
"QLineEdit:hover{\n"
"border	:	3px solid   rgba(123, 61, 184, 255)\n"
"}\n"
"QLineEdit:focus{\n"
"border	:	3px solid  rgba(171, 85, 255, 255)\n"
"}")
        self.ld_Pass.setEchoMode(QLineEdit.Password)
        self.login_2 = QPushButton(self.centro)
        self.login_2.setObjectName(u"login_2")
        self.login_2.setGeometry(QRect(45, 381, 210, 41))
        self.login_2.setMinimumSize(QSize(210, 41))
        self.login_2.setMaximumSize(QSize(210, 41))
        font5 = QFont()
        font5.setPointSize(12)
        self.login_2.setFont(font5)
        self.login_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 120, 213);\n"
"border-radius:10px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(206, 98, 163, 255);\n"
"border-radius:10px;}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(254, 121, 199, 255);\n"
"border-radius:10px;\n"
"\n"
"}")
        self.by = QLabel(self.centro)
        self.by.setObjectName(u"by")
        self.by.setGeometry(QRect(10, 470, 100, 20))
        self.toolButton_2 = QToolButton(self.centro)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setGeometry(QRect(245, 10, 20, 19))
        self.toolButton_2.setMinimumSize(QSize(20, 19))
        self.toolButton_2.setStyleSheet(u"QToolButton{\n"
"background-color: rgb(254, 121, 199);\n"
"border-radius:3px;\n"
"}\n"
"QToolButton:hover{\n"
"background-color:rgb(254, 154, 214);\n"
"border-radius:3px;\n"
"}\n"
"QToolButton:pressed{\n"
"background-color:rgb(254, 121, 199);\n"
"border-radius:3px;\n"
"}\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"../imagens/ICons/subtract_20px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_2.setIcon(icon)
        self.toolButton = QToolButton(self.centro)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(270, 10, 20, 19))
        self.toolButton.setMinimumSize(QSize(20, 19))
        self.toolButton.setStyleSheet(u"QToolButton{\n"
"background-color: rgb(254, 121, 199);\n"
"border-radius:3px;\n"
"}\n"
"QToolButton:hover{\n"
"background-color:rgb(254, 154, 214);\n"
"border-radius:3px;\n"
"}\n"
"QToolButton:pressed{\n"
"background-color:rgb(254, 121, 199);\n"
"border-radius:3px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../imagens/ICons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.centro)


        self.verticalLayout_4.addWidget(self.principal_frame)

        self.stackedWidget.addWidget(self.login)

        self.verticalLayout.addWidget(self.stackedWidget)

        loginSplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(loginSplashScreen)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(loginSplashScreen)
    # setupUi

    def retranslateUi(self, loginSplashScreen):
        loginSplashScreen.setWindowTitle(QCoreApplication.translate("loginSplashScreen", u"MainWindow", None))
        self.logo.setText("")
        self.name.setText(QCoreApplication.translate("loginSplashScreen", u"NAME", None))
        self.nameYourA.setText(QCoreApplication.translate("loginSplashScreen", u"<html><head/><body><p><span style=\" font-weight:600;\">  YOUR</span> APP</p><p><br/></p></body></html>", None))
        self.yourApp.setText(QCoreApplication.translate("loginSplashScreen", u"Sign in Your App", None))
        self.discricao.setText(QCoreApplication.translate("loginSplashScreen", u"Email address and password", None))
        self.ld_user.setInputMask("")
        self.ld_user.setText("")
        self.ld_user.setPlaceholderText(QCoreApplication.translate("loginSplashScreen", u"  Email", None))
        self.ld_Pass.setText("")
        self.ld_Pass.setPlaceholderText(QCoreApplication.translate("loginSplashScreen", u"  Password", None))
        self.login_2.setText(QCoreApplication.translate("loginSplashScreen", u"login", None))
        self.by.setText(QCoreApplication.translate("loginSplashScreen", u"by: Ndonda Daniel", None))
#if QT_CONFIG(tooltip)
        self.toolButton_2.setToolTip(QCoreApplication.translate("loginSplashScreen", u"Minimizar", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_2.setText("")
#if QT_CONFIG(tooltip)
        self.toolButton.setToolTip(QCoreApplication.translate("loginSplashScreen", u"Fechar", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton.setText("")
    # retranslateUi

