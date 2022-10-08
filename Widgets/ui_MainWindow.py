# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowVvxIeg.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSlider, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QToolButton, QVBoxLayout,
    QWidget)
import imagens.icon.icon_rc
import imagens.imag.img_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1088, 690)
        MainWindow.setMinimumSize(888, 690)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{border: 0px}"
"QWidget{background-color: rgb(56, 58, 89);}\n"
"      QToolTip {\n"
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
"}\n"
"\n"
"/*slider*/\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"/*slider vertical*/\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    height: 100px;\n"
"    wid"
                        "th: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:verticall:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background:rgb(41, 42, 65);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
""
                        "}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
" "
                        "    subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Menu_lateral = QFrame(self.centralwidget)
        self.Menu_lateral.setObjectName(u"Menu_lateral")
        self.Menu_lateral.setMinimumSize(QSize(56, 0))
        self.Menu_lateral.setMaximumSize(QSize(56, 16777215))
        self.Menu_lateral.setStyleSheet(u"background-color: rgb(41, 42, 65);")
        self.Menu_lateral.setFrameShape(QFrame.StyledPanel)
        self.Menu_lateral.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.Menu_lateral)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, 0)
        self.dock_widget_2 = QFrame(self.Menu_lateral)
        self.dock_widget_2.setObjectName(u"dock_widget_2")
        self.dock_widget_2.setMinimumSize(QSize(0, 43))
        self.dock_widget_2.setMaximumSize(QSize(16777215, 40))
        self.dock_widget_2.setStyleSheet(u"background-color: rgb(41, 42, 65);")
        self.dock_widget_2.setFrameShape(QFrame.StyledPanel)
        self.dock_widget_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.dock_widget_2)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.decricao = QFrame(self.dock_widget_2)
        self.decricao.setObjectName(u"decricao")
        self.decricao.setMinimumSize(QSize(240, 40))
        self.decricao.setMaximumSize(QSize(240, 16777215))
        self.decricao.setStyleSheet(u"")
        self.decricao.setFrameShape(QFrame.StyledPanel)
        self.decricao.setFrameShadow(QFrame.Raised)
        self.descricao_ = QFrame(self.decricao)
        self.descricao_.setObjectName(u"descricao_")
        self.descricao_.setGeometry(QRect(8, 4, 200, 41))
        self.descricao_.setMinimumSize(QSize(200, 41))
        self.descricao_.setMaximumSize(QSize(200, 41))
        self.descricao_.setFrameShape(QFrame.StyledPanel)
        self.descricao_.setFrameShadow(QFrame.Raised)
        self.logo1 = QFrame(self.descricao_)
        self.logo1.setObjectName(u"logo1")
        self.logo1.setGeometry(QRect(0, 1, 33, 33))
        self.logo1.setMinimumSize(QSize(33, 33))
        self.logo1.setMaximumSize(QSize(33, 33))
        self.logo1.setStyleSheet(u"border-radius:10px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0,\n"
"stop:0.275992 rgba(248, 118, 205, 255),\n"
" stop:0.286836 rgb(41, 42, 65),\n"
" stop:0.457627 rgb(41, 42, 65),\n"
" stop:0.468927 rgba(248, 118, 205, 255));")
        self.logo1.setFrameShape(QFrame.StyledPanel)
        self.logo1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.logo1)
        self.verticalLayout_16.setSpacing(2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(2, 2, 2, 2)
        self.logo2 = QFrame(self.logo1)
        self.logo2.setObjectName(u"logo2")
        self.logo2.setStyleSheet(u"background-color: rgb(41, 42, 65);\n"
"border-radius:17px;")
        self.logo2.setFrameShape(QFrame.StyledPanel)
        self.logo2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.logo2)
        self.verticalLayout_18.setSpacing(4)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(4, 4, 4, 4)
        self.logo3 = QFrame(self.logo2)
        self.logo3.setObjectName(u"logo3")
        self.logo3.setStyleSheet(u"border-radius: 14px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0\n"
" stop:0.0568182 rgba(248, 118, 205, 255),\n"
" stop:0.829545 rgba(248, 118, 205, 255),\n"
" stop:0.840909 rgb(41, 42, 65),\n"
" stop:0.982955 rgb(41, 42, 65));")
        self.logo3.setFrameShape(QFrame.StyledPanel)
        self.logo3.setFrameShadow(QFrame.Raised)
        self.logo3.setLineWidth(-1)
        self.verticalLayout_19 = QVBoxLayout(self.logo3)
        self.verticalLayout_19.setSpacing(2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(2, 2, 2, 2)
        self.logo4 = QFrame(self.logo3)
        self.logo4.setObjectName(u"logo4")
        self.logo4.setStyleSheet(u"background-color: rgb(41, 42, 65);\n"
"border-radius:12px;")
        self.logo4.setFrameShape(QFrame.StyledPanel)
        self.logo4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.logo4)
        self.verticalLayout_20.setSpacing(4)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(4, 4, 4, 4)
        self.logo5 = QFrame(self.logo4)
        self.logo5.setObjectName(u"logo5")
        self.logo5.setStyleSheet(u"border-radius:8px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0,\n"
" stop:0.0795455 rgba(248, 118, 205, 255),\n"
" stop:0.448864 rgb(41, 42, 65),\n"
" stop:0.676136 rgb(41, 42, 65),\n"
" stop:0.6875 rgba(248, 118, 205, 255));")
        self.logo5.setFrameShape(QFrame.StyledPanel)
        self.logo5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.logo5)
        self.verticalLayout_21.setSpacing(2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(2, 2, 2, 2)
        self.logo6 = QFrame(self.logo5)
        self.logo6.setObjectName(u"logo6")
        self.logo6.setStyleSheet(u"border-Radius:6px;\n"
"background-color: rgb(41, 42, 65);")
        self.logo6.setFrameShape(QFrame.StyledPanel)
        self.logo6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.logo6)
        self.verticalLayout_22.setSpacing(2)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(4, 4, 4, 4)
        self.logo7 = QFrame(self.logo6)
        self.logo7.setObjectName(u"logo7")
        self.logo7.setStyleSheet(u"background-color: rgb(248, 118, 205);\n"
"border-radius:1px;")
        self.logo7.setFrameShape(QFrame.StyledPanel)
        self.logo7.setFrameShadow(QFrame.Raised)

        self.verticalLayout_22.addWidget(self.logo7)


        self.verticalLayout_21.addWidget(self.logo6)


        self.verticalLayout_20.addWidget(self.logo5)


        self.verticalLayout_19.addWidget(self.logo4)


        self.verticalLayout_18.addWidget(self.logo3)


        self.verticalLayout_16.addWidget(self.logo2)

        self.Name_logo_4 = QLabel(self.descricao_)
        self.Name_logo_4.setObjectName(u"Name_logo_4")
        self.Name_logo_4.setGeometry(QRect(48, 20, 154, 14))
        self.Name_logo_4.setMinimumSize(QSize(0, 14))
        self.Name_logo_4.setMaximumSize(QSize(16777215, 14))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(7)
        self.Name_logo_4.setFont(font)
        self.Name_logo_4.setStyleSheet(u"color: rgb(248, 192, 236);")
        self.Name_logo_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Name_logo_5 = QLabel(self.descricao_)
        self.Name_logo_5.setObjectName(u"Name_logo_5")
        self.Name_logo_5.setGeometry(QRect(48, 1, 35, 14))
        self.Name_logo_5.setMinimumSize(QSize(0, 14))
        self.Name_logo_5.setMaximumSize(QSize(16777215, 14))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        self.Name_logo_5.setFont(font1)
        self.Name_logo_5.setStyleSheet(u"color: rgb(248, 118, 205)")
        self.Name_logo_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Name_logo_6 = QLabel(self.descricao_)
        self.Name_logo_6.setObjectName(u"Name_logo_6")
        self.Name_logo_6.setGeometry(QRect(89, 1, 63, 14))
        self.Name_logo_6.setMinimumSize(QSize(0, 14))
        self.Name_logo_6.setMaximumSize(QSize(16777215, 14))
        self.Name_logo_6.setFont(font1)
        self.Name_logo_6.setStyleSheet(u"color: rgb(213, 214, 220);")
        self.Name_logo_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.decricao)


        self.verticalLayout.addWidget(self.dock_widget_2)

        self.frame_btn_top = QFrame(self.Menu_lateral)
        self.frame_btn_top.setObjectName(u"frame_btn_top_2")
        self.frame_btn_top.setMinimumSize(QSize(240, 0))
        self.frame_btn_top.setMaximumSize(QSize(240, 16777215))
        self.frame_btn_top.setStyleSheet(u"QPushButton{\n"
"            color: #c3ccdf;\n"
"            padding-left: 18px;\n"
"            text-align: left;\n"
"            border: none;\n"
"        }\n"
"\n"
"        QPushButton:hover {\n"
"            background-color:rgb(67, 70, 107);\n"
"        }\n"
"\n"
"        QPushButton:pressed {\n"
"		background-color: rgb(186, 135, 245);\n"
"        }")
        self.frame_btn_top.setFrameShape(QFrame.StyledPanel)
        self.frame_btn_top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_btn_top)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.Hilder = QPushButton(self.frame_btn_top)
        self.Hilder.setObjectName(u"Hilder")
        self.Hilder.setMinimumSize(QSize(0, 35))
        self.Hilder.setMaximumSize(QSize(16777215, 35))
        icon = QIcon()
        icon.addFile(u"../imagens/ICons/icon_menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Hilder.setIcon(icon)
        self.Hilder.setIconSize(QSize(100, 100))

        self.verticalLayout_11.addWidget(self.Hilder)

        self.Home = QPushButton(self.frame_btn_top)
        self.Home.setObjectName(u"Home")
        self.Home.setMinimumSize(QSize(0, 35))
        self.Home.setMaximumSize(QSize(16777215, 35))
        self.Home.setStyleSheet("""QPushButton{
                                    color: #c3ccdf;
                                    padding-left: 18px;
                                    text-align: left;
                                    border: none;
                                    border-left: 3px solid rgb(248, 118, 205)
                                }""")

        icon1 = QIcon()
        icon1.addFile(u"../imagens/ICons/cil-home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Home.setIcon(icon1)
        self.Home.setIconSize(QSize(100, 100))

        self.verticalLayout_11.addWidget(self.Home)

        self.Widgets = QPushButton(self.frame_btn_top)
        self.Widgets.setObjectName(u"Widgets")
        self.Widgets.setMinimumSize(QSize(0, 35))
        self.Widgets.setMaximumSize(QSize(16777215, 35))

        icon2 = QIcon()
        icon2.addFile(u"../imagens/ICons/cil-gamepad.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Widgets.setIcon(icon2)
        self.Widgets.setIconSize(QSize(100, 100))

        self.verticalLayout_11.addWidget(self.Widgets)

        self.New = QPushButton(self.frame_btn_top)
        self.New.setObjectName(u"New")
        self.New.setMinimumSize(QSize(0, 35))
        self.New.setMaximumSize(QSize(16777215, 35))

        icon3 = QIcon()
        icon3.addFile(u"../imagens/ICons/document_20px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.New.setIcon(icon3)
        self.New.setIconSize(QSize(100, 100))

        self.verticalLayout_11.addWidget(self.New)

        self.Save = QPushButton(self.frame_btn_top)
        self.Save.setObjectName(u"Save")
        self.Save.setMinimumSize(QSize(0, 35))
        self.Save.setMaximumSize(QSize(16777215, 35))
        self.Save.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"../imagens/ICons/save_20px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Save.setIcon(icon4)
        self.Save.setIconSize(QSize(100, 100))

        self.verticalLayout_11.addWidget(self.Save)

        self.Exit = QPushButton(self.frame_btn_top)
        self.Exit.setObjectName(u"Exit")
        self.Exit.setMinimumSize(QSize(0, 35))
        self.Exit.setMaximumSize(QSize(16777215, 35))
        self.Exit.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u"../imagens/ICons/delete_20px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Exit.setIcon(icon5)
        self.Exit.setIconSize(QSize(100, 100))

        self.verticalLayout_11.addWidget(self.Exit)


        self.verticalLayout.addWidget(self.frame_btn_top)

        self.verticalSpacer = QSpacerItem(17, 101, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame_btn_bottom = QFrame(self.Menu_lateral)
        self.frame_btn_bottom.setObjectName(u"frame_btn_top")
        self.frame_btn_bottom.setMinimumSize(QSize(200, 90))
        self.frame_btn_bottom.setMaximumSize(QSize(240, 90))
        self.frame_btn_bottom.setStyleSheet(u"QPushButton{\n"
"            color: #c3ccdf;\n"
"            padding-left: 18px;\n"
"            text-align: left;\n"
"            border: none;\n"
"        }\n"
"\n"
"        QPushButton:hover {\n"
"            background-color:rgb(67, 70, 107);\n"
"        }\n"
"\n"
"        QPushButton:pressed {\n"
"background-color: rgb(186, 135, 245);\n"
"        }")
        self.frame_btn_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_btn_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_btn_bottom)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.Infor = QPushButton(self.frame_btn_bottom)
        self.Infor.setObjectName(u"Infor")
        self.Infor.setMinimumSize(QSize(0, 35))
        self.Infor.setMaximumSize(QSize(16777215, 35))
        self.Infor.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u"../imagens/ICons/information_20px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Infor.setIcon(icon6)
        self.Infor.setIconSize(QSize(100, 100))

        self.verticalLayout_12.addWidget(self.Infor)

        self.LeftBox = QPushButton(self.frame_btn_bottom)
        self.LeftBox.setObjectName(u"LeftBox")
        self.LeftBox.setMinimumSize(QSize(0, 35))
        self.LeftBox.setMaximumSize(QSize(16777215, 35))
        self.LeftBox.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u"../imagens/ICons/settings_20px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.LeftBox.setIcon(icon7)

        self.verticalLayout_12.addWidget(self.LeftBox)


        self.verticalLayout.addWidget(self.frame_btn_bottom)


        self.horizontalLayout.addWidget(self.Menu_lateral)

        self.settings_menu = QFrame(self.centralwidget)
        self.settings_menu.setObjectName(u"settings_menu")
        self.settings_menu.setMinimumSize(QSize(0, 0))
        self.settings_menu.setMaximumSize(QSize(0, 16777215))
        self.settings_menu.setStyleSheet(u"background-color: rgb(59, 61, 94);")
        self.settings_menu.setFrameShape(QFrame.StyledPanel)
        self.settings_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.settings_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.settings_menu)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: #ba87f5;")
        self.frame.setMinimumHeight(43)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 10, 0)
        self.pushButton_15 = QPushButton(self.frame)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(0, 35))
        self.pushButton_15.setMaximumSize(QSize(16777215, 35))
        self.pushButton_15.setStyleSheet(u"QPushButton{\n"
"            color: #c3ccdf;\n"
" \n"
"	background-color: rgb(186, 135, 245);\n"
"            padding-left: 18px;\n"
"            text-align: left;\n"
"            border: none;\n"
"\n"
"\n"
"        }\n"
"\n"
"")
        self.pushButton_15.setIcon(icon7)

        self.horizontalLayout_2.addWidget(self.pushButton_15)

        self.toolButton_5 = QToolButton(self.frame)
        self.toolButton_5.setObjectName(u"toolButton_5")
        self.toolButton_5.setMinimumSize(QSize(0, 35))
        self.toolButton_5.setMaximumSize(QSize(16777215, 35))
        self.toolButton_5.setStyleSheet(u"QToolButton{\n"
"            color: #c3ccdf;\n"
"	background-color: rgb(186, 135, 245);\n"
"            border: none;\n"
"        }\n"
"\n"
"QToolButton:hover {\n"
"	background-color: rgb(186, 135, 245);\n"
"border: none;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background-color: rgb(186, 135, 245);\n"
"border: none;\n"
"        }")
        self.toolButton_5.setIcon(icon5)

        self.horizontalLayout_2.addWidget(self.toolButton_5)


        self.verticalLayout_3.addWidget(self.frame)

        self.stackedWidget_2 = QStackedWidget(self.settings_menu)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_11 = QLabel(self.page_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 320, 180, 15))
        self.label_11.setStyleSheet(u"color: rgb(254, 121, 199);")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_15 = QLabel(self.page_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 216, 180, 15))
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_15.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.page_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 130, 180, 16))
        self.label_5.setStyleSheet(u"color: rgb(254, 121, 199);")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.page_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 237, 180, 16))
        self.label_7.setStyleSheet(u"color: rgb(186, 135, 245);")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_12 = QLabel(self.page_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 340, 180, 15))
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 195, 180, 21))
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_13 = QLabel(self.page_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 152, 180, 15))
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_14 = QLabel(self.page_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 173, 180, 16))
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_10 = QLabel(self.page_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 280, 180, 16))
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.page_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 259, 180, 15))
        self.label_8.setStyleSheet(u"color: rgb(254, 121, 199);")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.frame_2 = QFrame(self.page_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 10, 191, 111))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_18 = QPushButton(self.frame_2)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(0, 35))
        self.pushButton_18.setMaximumSize(QSize(16777215, 35))
        self.pushButton_18.setStyleSheet(u"QPushButton{\n"
"            color: #c3ccdf;\n"
"            padding-left: 18px;\n"
"            text-align: left;\n"
"            border: none;\n"
"        }\n"
"QPushButton:hover {\n"
"	background-color: rgb(72, 75, 115);\n"
"        }\n"
"\n"
"        QPushButton:pressed {\n"
"background-color: rgb(186, 135, 245);\n"
"        }")
        icon8 = QIcon()
        icon8.addFile(u"../imagens/icon/share_3_18px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_18.setIcon(icon8)

        self.verticalLayout_5.addWidget(self.pushButton_18)

        self.pushButton_16 = QPushButton(self.frame_2)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(0, 35))
        self.pushButton_16.setMaximumSize(QSize(16777215, 35))
        self.pushButton_16.setStyleSheet(u"QPushButton{\n"
"            color: #c3ccdf;\n"
"            padding-left: 18px;\n"
"            text-align: left;\n"
"            border: none;\n"
"        }\n"
"QPushButton:hover {\n"
"	background-color: rgb(72, 75, 115);\n"
"        }\n"
"\n"
"        QPushButton:pressed {\n"
"background-color: rgb(186, 135, 245);\n"
"        }")
        icon9 = QIcon()
        icon9.addFile(u"../imagens/icon/adjust_18px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_16.setIcon(icon9)

        self.verticalLayout_5.addWidget(self.pushButton_16)

        self.pushButton_17 = QPushButton(self.frame_2)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(0, 35))
        self.pushButton_17.setMaximumSize(QSize(16777215, 35))
        self.pushButton_17.setStyleSheet(u"QPushButton{\n"
"            color: #c3ccdf;\n"
"            padding-left: 18px;\n"
"            text-align: left;\n"
"            border: none;\n"
"        }\n"
"QPushButton:hover {\n"
"	background-color: rgb(72, 75, 115);\n"
"        }\n"
"\n"
"        QPushButton:pressed {\n"
"background-color: rgb(186, 135, 245);\n"
"        }")
        icon10 = QIcon()
        icon10.addFile(u"../imagens/icon/netbeans_18px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_17.setIcon(icon10)

        self.verticalLayout_5.addWidget(self.pushButton_17)

        self.label_21 = QLabel(self.page_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 300, 180, 16))
        self.label_21.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_21.setAlignment(Qt.AlignCenter)
        self.label_22 = QLabel(self.page_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 360, 180, 15))
        self.label_22.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_22.setAlignment(Qt.AlignCenter)
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_16 = QLabel(self.page_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(0, 10, 200, 31))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(16)
        self.label_16.setFont(font2)
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_16.setAlignment(Qt.AlignCenter)
        self.layoutWidget = QWidget(self.page_4)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 71, 190, 34))
        self.horizontalLayout_12 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        font3 = QFont()
        font3.setPointSize(12)
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left: 6px;")

        self.horizontalLayout_12.addWidget(self.label_6)

        self.selectTheme = QComboBox(self.layoutWidget)
        self.selectTheme.addItem("")
        self.selectTheme.addItem("")
        self.selectTheme.addItem("")
        self.selectTheme.addItem("")
        self.selectTheme.setObjectName(u"selectTheme")
        self.selectTheme.setMinimumSize(QSize(120, 32))
        self.selectTheme.setMaximumSize(QSize(183, 32))
        self.selectTheme.setStyleSheet("""
                                                QComboBox{
                                                    background-color:rgb(41, 42, 65);
                                                    border-radius: 5px;
                                                    border: 2px solid rgb(204, 97, 170);
                                                    padding: 5px;
                                                    padding-left: 10px;
                                                    color: rgb(255, 255, 255);
                                                }
                                                QComboBox:hover{
                                                    border: 2px solid rgb(255, 121, 213);
                                                }
                                                QComboBox::drop-down {
                                                    subcontrol-origin: padding;
                                                    subcontrol-position: top right;
                                                    width: 25px; 
                                                    border-left-width: 3px;
                                                    border-left-color: rgba(39, 44, 54, 150);
                                                    border-left-style: solid;
                                                    border-top-right-radius: 3px;
                                                    border-bottom-right-radius: 3px;	
                                                    background-image: url(:/icons/cil-arrow-bottom-2.png);
                                                    background-position: center;
                                                    background-repeat: no-reperat;
                                                 }
                                                QComboBox QAbstractItemView {
                                                    color: rgb(255, 121, 198);	
                                                    background-color:rgb(41, 42, 65);
                                                    padding: 10px;
                                                    selection-background-color: rgb(195, 155, 255);
                                                    border:2px solid  rgb(248, 118, 205);
                                                    border_top:none;
                                                    border-radius:5px;
                                                }""")

        self.horizontalLayout_12.addWidget(self.selectTheme)

        self.stackedWidget_2.addWidget(self.page_4)

        self.verticalLayout_3.addWidget(self.stackedWidget_2)

        self.informacao = QFrame(self.settings_menu)
        self.informacao.setObjectName(u"informacao")
        self.informacao.setStyleSheet(u"            color: #c3ccdf;")
        self.informacao.setFrameShape(QFrame.StyledPanel)
        self.informacao.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.informacao)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.informacao)


        self.horizontalLayout.addWidget(self.settings_menu)

        self.cental_frame = QFrame(self.centralwidget)
        self.cental_frame.setObjectName(u"cental_frame")
        self.cental_frame.setMinimumSize(QSize(0, 0))
        self.cental_frame.setFrameShape(QFrame.StyledPanel)
        self.cental_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.cental_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.dock_widget = QFrame(self.cental_frame)
        self.dock_widget.setObjectName(u"dock_widget")
        self.dock_widget.setMinimumSize(QSize(0, 43))
        self.dock_widget.setMaximumSize(QSize(16777215, 40))
        self.dock_widget.setStyleSheet(u"background-color: rgb(41, 42, 65);")
        self.dock_widget.setFrameShape(QFrame.StyledPanel)
        self.dock_widget.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.dock_widget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(7, 0, 0, 0)
        self.label = QLabel(self.dock_widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(213, 214, 220);")

        self.horizontalLayout_4.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(171, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.btns = QFrame(self.dock_widget)
        self.btns.setObjectName(u"btns")
        self.btns.setMinimumSize(QSize(151, 40))
        self.btns.setMaximumSize(QSize(151, 40))
        self.btns.setStyleSheet(u"QToolButton{\n"
"            color: #c3ccdf;\n"
"            border: none;\n"
"			border-radius:3px;\n"
"        }\n"
"\n"
"QToolButton:hover {\n"
"background-color: rgb(67, 70, 107);\n"
"border: none;\n"
"border-radius:3px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
" background-color: rgb(96, 100, 152);\n"
"border: none;\n"
"border-radius:3px;        \n"
"}")
        self.btns.setFrameShape(QFrame.StyledPanel)
        self.btns.setFrameShadow(QFrame.Raised)
        self.unckechd = QToolButton(self.btns)
        self.unckechd.setObjectName(u"unckechd")
        self.unckechd.setGeometry(QRect(80, 10, 25, 19))
        self.unckechd.setStyleSheet(u"")
        icon11 = QIcon()
        icon11.addFile(u"../imagens/ICons/cil-media-stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.unckechd.setIcon(icon11)
        self.Minimu = QToolButton(self.btns)
        self.Minimu.setObjectName(u"Minimu")
        self.Minimu.setGeometry(QRect(50, 10, 25, 19))

        icon12 = QIcon()
        icon12.addFile(u"../imagens/ICons/subtract_20px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Minimu.setIcon(icon12)
        self.close = QToolButton(self.btns)
        self.close.setObjectName(u"close")
        self.close.setGeometry(QRect(110, 10, 25, 19))
        self.close.setStyleSheet(u"")
        icon13 = QIcon()
        icon13.addFile(u"../imagens/ICons/delete_20Bpx.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close.setIcon(icon13)
        self.Settings_right = QToolButton(self.btns)
        self.Settings_right.setObjectName(u"Settings_right")
        self.Settings_right.setGeometry(QRect(20, 10, 25, 19))
        self.Settings_right.setStyleSheet(u"")
        self.Settings_right.setIcon(icon7)

        self.horizontalLayout_4.addWidget(self.btns)


        self.verticalLayout_2.addWidget(self.dock_widget)

        self.frame_central = QFrame(self.cental_frame)
        self.frame_central.setObjectName(u"frame_central")
        self.frame_central.setFrameShape(QFrame.StyledPanel)
        self.frame_central.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_central)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_central)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.Principal_page = QWidget()
        self.Principal_page.setObjectName(u"Principal_page")
        self.Principal_page.setMinimumSize(QSize(0, 0))
        self.verticalLayout_29 = QVBoxLayout(self.Principal_page)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_5 = QFrame(self.Principal_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-image: url(:/img/logo1.png);\n"
"background-position: center;\n"
"background-repeat: no-reperat;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_29.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.Principal_page)
        self.WidgetsPage = QWidget()
        self.WidgetsPage.setObjectName(u"WidgetsPage")
        self.horizontalLayout_18 = QHBoxLayout(self.WidgetsPage)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.Game = QFrame(self.WidgetsPage)
        self.Game.setObjectName(u"Game")
        self.Game.setMinimumSize(QSize(400, 0))
        self.Game.setStyleSheet(u"QFrame{\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Game.setFrameShape(QFrame.StyledPanel)
        self.Game.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.Game)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_3 = QLabel(self.Game)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(80, 30))
        self.label_3.setMaximumSize(QSize(80, 30))
        self.label_3.setFont(font3)

        self.verticalLayout_14.addWidget(self.label_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(6, -1, -1, -1)
        self.lineEdit = QLineEdit(self.Game)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 35))
        self.lineEdit.setMaximumSize(QSize(16777215, 35))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(41, 42, 65);\n"
"	border-color:rgb(41, 42, 65);\n"
"	border-radius:8px\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	background-color: rgb(41, 42, 65);\n"
"	border-color:rgb(41, 42, 65);\n"
"	border: 2px solid rgb(73, 76, 116);\n"
"	border-radius:8px\n"
"}\n"
"QLineEdit:focus {\n"
"	background-color: rgb(41, 42, 65);\n"
"	border-color:rgb(41, 42, 65);\n"
"	border: 2px solid rgb(90, 95, 145);\n"
"	border-radius:8px\n"
"}")

        self.horizontalLayout_9.addWidget(self.lineEdit)

        self.OpenFolder = QPushButton(self.Game)
        self.OpenFolder.setObjectName(u"OpenFolder")
        self.OpenFolder.setMinimumSize(QSize(121, 35))
        self.OpenFolder.setMaximumSize(QSize(121, 35))
        font4 = QFont()
        font4.setPointSize(10)
        self.OpenFolder.setFont(font4)
        self.OpenFolder.setStyleSheet(u"QPushButton{\n"
"	border-radius:8px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(73, 76, 116);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius:8px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(73, 76, 116);\n"
"	border: 2px solid rgb(94, 99, 150);\n"
"}\n"
"QPushButton:pressed{\n"
"	border-radius:8px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(73, 76, 116);\n"
"	padding-top: 3px;\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u"../imagens/ICons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.OpenFolder.setIcon(icon14)

        self.horizontalLayout_9.addWidget(self.OpenFolder)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.label_4 = QLabel(self.Game)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 16))
        self.label_4.setMaximumSize(QSize(100, 16))
        self.label_4.setStyleSheet(u"color:  rgb(124, 130, 198);")

        self.verticalLayout_6.addWidget(self.label_4)


        self.verticalLayout_14.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addLayout(self.verticalLayout_14)

        self.frame_4 = QFrame(self.Game)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 151))
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(20)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.checkBox = QCheckBox(self.frame_4)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(82, 21))
        self.checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(41, 42, 65);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/cil-check-alt.png);\n"
"}\n"
"")

        self.horizontalLayout_22.addWidget(self.checkBox)

        self.radioButton = QRadioButton(self.frame_4)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMinimumSize(QSize(82, 21))
        self.radioButton.setStyleSheet(u"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(41, 42, 65);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(73, 76, 116);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(73, 76, 116);\n"
"	border: 3px solid rgb(41, 42, 65)	\n"
"}")

        self.horizontalLayout_22.addWidget(self.radioButton)


        self.verticalLayout_10.addLayout(self.horizontalLayout_22)

        self.comboBox_2 = QComboBox(self.frame_4)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(183, 32))
        self.comboBox_2.setMaximumSize(QSize(183, 32))
        self.comboBox_2.setStyleSheet(u"\n"
"QComboBox{\n"
"	background-color:rgb(41, 42, 65);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(41, 42, 65);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(73, 76, 116);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/cil-arrow-bottom-2.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color:rgb(41, 42, 65);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(195, 155, 255);\n"
"}\n"
"\n"
"")

        self.verticalLayout_10.addWidget(self.comboBox_2)

        self.horizontalSlider = QSlider(self.frame_4)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMaximumSize(QSize(220, 16777215))
        self.horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal{\n"
"    background-color: rgb(41, 42, 65);\n"
"    border: none;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"	background-color: rgb(195, 155, 255);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_10.addWidget(self.horizontalSlider)


        self.horizontalLayout_10.addLayout(self.verticalLayout_10)

        self.verticalSlider = QSlider(self.frame_4)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"QSlider::groove:vertical{\n"
"	background-color: rgb(41, 42, 65);\n"
"    border: none;\n"
" 	height: 120px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"	background-color: rgb(195, 155, 255);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_10.addWidget(self.verticalSlider)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_17 = QLabel(self.frame_4)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_15.addWidget(self.label_17)

        self.horizontalSlider_2 = QSlider(self.frame_4)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setMinimumSize(QSize(30, 0))
        self.horizontalSlider_2.setStyleSheet(u"QSlider::groove:horizontal{\n"
"    background-color: rgb(41, 42, 65);\n"
"    border: none;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontalal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 0px;\n"
"    width: 25px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:verticall:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}")
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_15.addWidget(self.horizontalSlider_2)

        self.label_18 = QLabel(self.frame_4)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_15.addWidget(self.label_18)


        self.horizontalLayout_11.addLayout(self.verticalLayout_15)

        self.verticalSlider_2 = QSlider(self.frame_4)
        self.verticalSlider_2.setObjectName(u"verticalSlider_2")
        self.verticalSlider_2.setStyleSheet(u"QSlider::groove:vertical{\n"
"	background-color: rgb(41, 42, 65);\n"
"    border: none;\n"
" 	height: 120px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"	background-color: rgb(195, 155, 255);\n"
"    border: none;\n"
"    height: 25px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}")
        self.verticalSlider_2.setOrientation(Qt.Vertical)

        self.horizontalLayout_11.addWidget(self.verticalSlider_2)

        self.scrollArea = QScrollArea(self.frame_4)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"border:none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 218, 218))
        self.scrollAreaWidgetContents_2.setStyleSheet(u"")
        self.verticalLayout_17 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setMaximumSize(QSize(16777215, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(41, 42, 65);\n"
"border-radius:8px;")

        self.verticalLayout_17.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_11.addWidget(self.scrollArea)

        self.commandLinkButton = QCommandLinkButton(self.frame_4)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setMinimumSize(QSize(172, 55))
        self.commandLinkButton.setMaximumSize(QSize(172, 55))
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"QCommandLinkButton{\n"
"color: rgb(195, 155, 255);\n"
"border:none;\n"
"border-radius:7px;\n"
"border: 2px solid rgb(73, 76, 116);}\n"
"\n"
"QCommandLinkButton:hover{\n"
"color: rgb(195, 155, 255);\n"
"border:none;\n"
"border-radius:7px;\n"
"border: 2px solid rgb(116, 91, 153)}\n"
"\n"
"QCommandLinkButton:pressed{\n"
"color: rgb(195, 155, 255);\n"
"border:none;\n"
"border-radius:7px;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        icon15 = QIcon()
        icon15.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon15)

        self.horizontalLayout_11.addWidget(self.commandLinkButton)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_11)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.tableWidget_2 = QTableWidget(self.Game)
        if (self.tableWidget_2.columnCount() < 4):
            self.tableWidget_2.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget_2.rowCount() < 16):
            self.tableWidget_2.setRowCount(16)
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font5);
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setStyleSheet("""
                                                    QTableWidget {	
                                                        color: rgb(0, 0, 0);
                                                        background-color: transparent;
                                                        padding: 10px;
                                                        border-radius: 5px;
                                                        gridline-color: rgb(44, 49, 58);
                                                        border-bottom: 1px solid rgb(44, 49, 60);
                                                    }
                                                    QTableWidget::item{
                                                        border-color: rgb(44, 49, 60);
                                                        padding-left: 5px;
                                                        padding-right: 5px;
                                                        gridline-color: rgb(44, 49, 60);
                                                    }
                                                    QTableWidget::item:selected{
                                                        background-color: rgb(189, 147, 249);
                                                    }
                                                    QHeaderView::section{
                                                        background-color: rgb(33, 37, 43);
                                                        max-width: 30px;
                                                        border: 1px solid rgb(44, 49, 58);
                                                        border-style: none;
                                                        border-bottom: 1px solid rgb(44, 49, 60);
                                                        border-right: 1px solid rgb(44, 49, 60);
                                                    }
                                                    QTableWidget::horizontalHeader {	
                                                        background-color: rgb(33, 37, 43);
                                                    }
                                                    QHeaderView::section:horizontal
                                                    {
                                                        border: 1px solid rgb(33, 37, 43);
                                                        background-color: rgb(33, 37, 43);
                                                        padding: 3px;
                                                        border-top-left-radius: 7px;
                                                        border-top-right-radius: 7px;
                                                    }
                                                    QHeaderView::section:vertical
                                                    {
                                                        border: 1px solid rgb(44, 49, 60);
                                                    }""")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.tableWidget_2.setPalette(palette)
        self.tableWidget_2.setStyleSheet(u"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
""
                        "{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget_2.setFrameShape(QFrame.NoFrame)
        self.tableWidget_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setGridStyle(Qt.SolidLine)
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.verticalHeader().setHighlightSections(False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_7.addWidget(self.tableWidget_2)


        self.horizontalLayout_18.addWidget(self.Game)

        self.stackedWidget.addWidget(self.WidgetsPage)
        self.NewPage = QWidget()
        self.NewPage.setObjectName(u"NewPage")
        self.horizontalLayout_19 = QHBoxLayout(self.NewPage)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_20 = QLabel(self.NewPage)
        self.label_20.setObjectName(u"label_20")
        font6 = QFont()
        font6.setPointSize(17)
        self.label_20.setFont(font6)
        self.label_20.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_20)

        self.stackedWidget.addWidget(self.NewPage)
        self.CatPage = QWidget()
        self.CatPage.setObjectName(u"CatPage")
        self.horizontalLayout_20 = QHBoxLayout(self.CatPage)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_19 = QLabel(self.CatPage)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_19)

        self.stackedWidget.addWidget(self.CatPage)

        self.horizontalLayout_8.addWidget(self.stackedWidget)

        self.settings_menu_2 = QFrame(self.frame_3)
        self.settings_menu_2.setObjectName(u"settings_menu_2")
        self.settings_menu_2.setMinimumSize(QSize(0, 0))
        self.settings_menu_2.setMaximumSize(QSize(0, 16777215))
        self.settings_menu_2.setStyleSheet(u"background-color: rgb(62, 65, 99);")
        self.settings_menu_2.setFrameShape(QFrame.StyledPanel)
        self.settings_menu_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.settings_menu_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.Linha = QFrame(self.settings_menu_2)
        self.Linha.setObjectName(u"Linha")
        self.Linha.setStyleSheet(u"background-color: #ba87f5;")
        self.Linha.setFrameShape(QFrame.StyledPanel)
        self.Linha.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.Linha)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 10, 0)

        self.verticalLayout_9.addWidget(self.Linha)

        self.Btns_right_frame = QFrame(self.settings_menu_2)
        self.Btns_right_frame.setObjectName(u"Btns_right_frame")
        self.Btns_right_frame.setFrameShape(QFrame.StyledPanel)
        self.Btns_right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.Btns_right_frame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.Share = QPushButton(self.Btns_right_frame)
        self.Share.setObjectName(u"Share")
        self.Share.setMinimumSize(QSize(0, 35))
        self.Share.setMaximumSize(QSize(16777215, 35))
        self.Share.setStyleSheet(u"QPushButton{\n"
"            color: #c3ccdf;\n"
"            padding-left: 18px;\n"
"            text-align: left;\n"
"            border: none;\n"
"        }\n"
"QPushButton:hover {\n"
"	background-color: rgb(72, 75, 115);\n"
"        }\n"
"\n"
"        QPushButton:pressed {\n"
"background-color: rgb(186, 135, 245);\n"
"        }")
        icon16 = QIcon()
        icon16.addFile(u"../imagens/ICons/cil-paper-plane.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Share.setIcon(icon16)

        self.verticalLayout_8.addWidget(self.Share)

        self.Print = QPushButton(self.Btns_right_frame)
        self.Print.setObjectName(u"Print")
        self.Print.setMinimumSize(QSize(0, 35))
        self.Print.setMaximumSize(QSize(16777215, 35))
        self.Print.setStyleSheet(u"QPushButton{\n"
"            color: #c3ccdf;\n"
"            padding-left: 18px;\n"
"            text-align: left;\n"
"            border: none;\n"
"        }\n"
"QPushButton:hover {\n"
"	background-color: rgb(72, 75, 115);\n"
"        }\n"
"\n"
"        QPushButton:pressed {\n"
"background-color: rgb(186, 135, 245);\n"
"        }")
        icon17 = QIcon()
        icon17.addFile(u"../imagens/ICons/cil-print.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Print.setIcon(icon17)

        self.verticalLayout_8.addWidget(self.Print)

        self.CatWalking = QPushButton(self.Btns_right_frame)
        self.CatWalking.setObjectName(u"CatWalking")
        self.CatWalking.setMinimumSize(QSize(0, 35))
        self.CatWalking.setMaximumSize(QSize(16777215, 35))
        self.CatWalking.setStyleSheet(u"QPushButton{\n"
"            color: #c3ccdf;\n"
"            padding-left: 18px;\n"
"            text-align: left;\n"
"            border: none;\n"
"        }\n"
"QPushButton:hover {\n"
"	background-color: rgb(72, 75, 115);\n"
"        }\n"
"\n"
"        QPushButton:pressed {\n"
"background-color: rgb(186, 135, 245);\n"
"        }")
        icon18 = QIcon()
        icon18.addFile(u"../imagens/ICons/cat_profile_23px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CatWalking.setIcon(icon18)
        self.CatWalking.setIconSize(QSize(20, 20))

        self.verticalLayout_8.addWidget(self.CatWalking)


        self.verticalLayout_9.addWidget(self.Btns_right_frame)

        self.verticalSpacer_2 = QSpacerItem(20, 481, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)


        self.horizontalLayout_8.addWidget(self.settings_menu_2)


        self.horizontalLayout_7.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.frame_central)

        self.statusBar = QFrame(self.cental_frame)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setMinimumSize(QSize(0, 30))
        self.statusBar.setMaximumSize(QSize(16777215, 30))
        self.statusBar.setStyleSheet(u"background-color: rgb(65, 68, 104);")
        self.statusBar.setFrameShape(QFrame.StyledPanel)
        self.statusBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.statusBar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(7, 0, 0, 0)
        self.label_2 = QLabel(self.statusBar)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(213, 214, 220);")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(360, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.version = QLabel(self.statusBar)
        self.version.setObjectName(u"version")
        self.version.setMinimumSize(QSize(0, 30))
        self.version.setMaximumSize(QSize(11111, 30))
        self.version.setStyleSheet(u"color: #c3ccdf")
        self.version.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.version)

        self.frame_SizeGrip_2 = QFrame(self.statusBar)
        self.frame_SizeGrip_2.setObjectName(u"frame_SizeGrip_2")
        self.frame_SizeGrip_2.setMinimumSize(QSize(10, 10))
        self.frame_SizeGrip_2.setMaximumSize(QSize(10, 10))
        self.frame_SizeGrip_2.setStyleSheet(u"background-image: url(:/icons/cil-size-grip.png);\n"
"background-position: center;\n"
"background-repeat: no-reperat;")
        self.frame_SizeGrip_2.setFrameShape(QFrame.StyledPanel)
        self.frame_SizeGrip_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_SizeGrip_2)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3.addWidget(self.frame_SizeGrip_2, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.statusBar)


        self.horizontalLayout.addWidget(self.cental_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Name_logo_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Moderm GUI/Fast Style/Qt PyThon       </p><p><br/></p></body></html>", None))
        self.Name_logo_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">YOUR</span></p><p><br/></p></body></html>", None))
        self.Name_logo_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>APP NAME</p><p><br/></p></body></html>", None))
        self.Hilder.setText(QCoreApplication.translate("MainWindow", u"     Hilde", None))
        self.Home.setText(QCoreApplication.translate("MainWindow", u"     Home", None))
        self.Widgets.setText(QCoreApplication.translate("MainWindow", u"     Widgets", None))
        self.New.setText(QCoreApplication.translate("MainWindow", u"     New", None))
        self.Save.setText(QCoreApplication.translate("MainWindow", u"     Save", None))
        self.Exit.setText(QCoreApplication.translate("MainWindow", u"     Exit", None))
        self.Infor.setText(QCoreApplication.translate("MainWindow", u"     infor", None))
        self.LeftBox.setText(QCoreApplication.translate("MainWindow", u"      Left Box", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"      Left Box", None))
        self.toolButton_5.setText("")
#if QT_CONFIG(whatsthis)
        self.label_11.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">YOUR APP NAME</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">converter QRC</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"PyDarculas e no logo espermetal", None))
#if QT_CONFIG(whatsthis)
        self.label_5.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">YOUR APP NAME</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">YOUR APP NAME</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.label_7.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Criado por : Ndonda Daniel</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Criado por : Ndonda Daniel</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"PySide6-rcc icon.qrc -o icon_rc.py", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"com as cores basiadas no", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Esta \u00e9 uma app criada em PyThon ", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"e PySide (Com suporte a PyQt) e", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"ManWindow.u > ManWindow.py", None))
#if QT_CONFIG(whatsthis)
        self.label_8.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">YOUR APP NAME</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">converter UI</span></p></body></html>", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"     Share", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"     adjustments", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"     Hilde", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"SplahScreen.u > SplahScreen.py", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"PySide6-rcc imgqrc -o img_rc.py", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"SETTINGS of THEME", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"THEME", None))
        self.selectTheme.setItemText(0, QCoreApplication.translate("MainWindow", u"1\u00ba  Normal", None))
        self.selectTheme.setItemText(1, QCoreApplication.translate("MainWindow", u"2\u00ba  white", None))
        self.selectTheme.setItemText(2, QCoreApplication.translate("MainWindow", u"3\u00ba  Dark", None))
        self.selectTheme.setItemText(3, QCoreApplication.translate("MainWindow", u"4\u00ba  BlueGreen", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"| APP PyThon - Desenvollvida com PySide6 e Qt Designer", None))
#if QT_CONFIG(tooltip)
        self.unckechd.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Aumentar</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.unckechd.setText("")
#if QT_CONFIG(tooltip)
        self.Minimu.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Minimizar</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Minimu.setText("")
#if QT_CONFIG(tooltip)
        self.close.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Fechar</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.close.setText("")
#if QT_CONFIG(tooltip)
        self.Settings_right.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>settings</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Settings_right.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.OpenFolder.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"   Label Descrcition", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"1\u00ba", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"2\u00ba", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"3\u00ba", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"4\u00ba", None))

        self.label_17.setText("")
        self.label_18.setText("")
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget_2.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget_2.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget_2.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget_2.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget_2.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget_2.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget_2.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget_2.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget_2.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget_2.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget_2.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget_2.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget_2.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget_2.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget_2.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget_2.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget_2.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)

        self.label_20.setText(QCoreApplication.translate("MainWindow", u"NEW PAGE", None))
        self.label_19.setText("")
        self.Share.setText(QCoreApplication.translate("MainWindow", u"     Share", None))
        self.Print.setText(QCoreApplication.translate("MainWindow", u"     Hilde", None))
        self.CatWalking.setText(QCoreApplication.translate("MainWindow", u"     cat walking", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Criado por: Ndonda Daniel", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v.1.0.0", None))
    # retranslateUi


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
