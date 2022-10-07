import sys

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from time import sleep

from ui_MainWindow import Ui_MainWindow
from ui_SplahScreen import Ui_loginSplashScreen
from circular_progress import CircularProgress
from custom_grips import CustomGrip
from database import database


# variaveis globais

counter = 0
counter1 = 0
counter2 = 0
counterBtn = 0
counterLb1 = 0
counterLb2 = 0
counterLogo = 0

GLOBAL_STATE = 0

CORTEMA = None
CORSC = None
openArQ = False
# SplashScreen3
class LoginScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_loginSplashScreen()
        self.ui.setupUi(self)

        # remove title and bar
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # BTNS MINIMIZAR E FECHAR
        self.ui.toolButton.clicked.connect(lambda: self.close())
        self.ui.toolButton_2.clicked.connect(lambda: self.showMinimized())
        self.ui.login_3.clicked.connect(self.login)
        self.ui.ld_Pass.returnPressed.connect(self.login)

        # import circular progress
        self.progress = CircularProgress()

        self.progress.width = 270
        self.progress.height = 270
        self.progress.value = 0
        self.progress.setFixedSize(self.progress.width, self.progress.height)
        self.progress.move(25, 20)
        self.progress.font_size = 12
        self.progress.progress_width = 3
        self.progress.ad_shadow(True)
        self.progress.setParent(self.ui.centralwidget)
        self.progress.show()

        # tema
        global CORSC
        try:
            with open("Tema.txt", "r") as tema:
                atualTema = tema.read()
                CORSC = atualTema
                self.tema(atualTema)
        except:
            with open("Tema.txt", "w") as tema:
                tema.write("1º  Normal")

        # zona do tema

        # ADD LARGAR SOMBRA
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(22, 22, 22, 130))
        self.setGraphicsEffect(self.shadow)

        # FUNCAO PARA MOVER BARRA DE TITULO

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

            # add BARRA ED TITULO NA FUNCAO

        self.ui.centro.mouseMoveEvent = moveWindow

        # QTimer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1)

        self.user_analityTimer = QTimer()
        self.user_analityTimer.timeout.connect(lambda: self.user_anality(len(self.ui.ld_user.text())))

        self.pass_analityTimer = QTimer()
        self.pass_analityTimer.timeout.connect(lambda: self.pass_anality(len(self.ui.ld_Pass.text())))

        self.timerAnimation = QTimer()
        self.timerAnimation.timeout.connect(self.animationEfect)

        self.timerG = QTimer()
        self.timerG.timeout.connect(self.resizeG)

        self.show()

        # ///////  CODIGO DA ANIMACAO /////////////

        # apagando as propriedades da tela
        self.ui.yourApp.close()
        self.ui.discricao.close()
        self.ui.ld_user.close()
        self.ui.ld_Pass.close()
        self.ui.login_3.close()
        self.ui.name.close()
        self.ui.nameYourA.close()
        self.ui.logo.close()

        # receber o estilo com pouca visblidade

        # atribuindo o estilo zerado
        self.ui.ld_user.setStyleSheet(StyleLocal.LEzero)
        self.ui.ld_Pass.setStyleSheet(StyleLocal.LEzero)
        self.ui.login_3.setStyleSheet(StyleLocal.ZeroBtn)
        self.ui.discricao.setStyleSheet(StyleLocal.labelZero)
        self.ui.yourApp.setStyleSheet(StyleLocal.labelZero)

    def resizeG(self):
        pontoAtual = self.pos()
        pontoAtual.y()
        cont = 3
        while True:
            self.move(self.pos().x(), self.pos().y()-cont)
            cont += 3

            if cont == 100:
                break

    def animationEfect(self):
        global counter, counter1, counter2, counterBtn, counterLb1, counterLb2, CORSC

        # self.ui.logo.show()
        test = 90
        if CORSC == "1º  Normal":
            stylesheet = """ 
                       QLineEdit{
                               background-color: rgba(70, 72, 111, {alphaC});
                               color: rgba(220, 203, 216, {alphaC});
                               font: 10pt "MS Shell Dlg 2";
                               border-radius: 10px;
                               padding-left:8px;
                               border:2px solid rgba(255, 120, 213, {alphaB});
                               }
                               QLineEdit:hover{
                               border:3px solid rgba(255, 120, 213, 255)
                               }
                               QLineEdit:focus{
                               border:3px solid rgba(199, 94, 167, {alphaC})
                               
                               }"""
            btnStylesheet = """QPushButton{
                               background-color: rgba(225, 107, 178, {alpha});
                               border-radius:10px;
                               }
                               QPushButton:hover{
                               background-color: rgba(206, 98, 163, 255);
                               border-radius:10px;
                               }
                               QPushButton:pressed{
                               background-color: rgba(254, 121, 199, 255);
                               border-radius:10px;
                               }"""
            Lbstylesheet = """QLabel{color: rgba(98, 114, 164, {Lb})
           }"""
            fLb_stylesheet = """QLabel{color: rgba(254, 121, 199,{rect})
                       }"""

        elif (CORSC == "2º  Light"):
            stylesheet = """ 
                                   QLineEdit{
                                           background-color: rgba(255, 255, 255, {alphaC});
                                           color: rgba(98, 114, 164, {alphaC});
                                           font: 10pt "MS Shell Dlg 2";
                                           border-radius: 10px;
                                           padding-left:8px;
                                           border:2px solid rgba(255, 120, 213, {alphaB});
                                           }
                                           QLineEdit:hover{
                                           border:3px solid rgba(255, 120, 213, 255)
                                           }
                                           QLineEdit:focus{
                                           border:3px solid rgba(199, 94, 167, {alphaC})

                                           }"""
            btnStylesheet = """QPushButton{
                                           background-color: rgba(225, 107, 178, {alpha});
                                           border-radius:10px;
                                           }
                                           QPushButton:hover{
                                           background-color: rgba(206, 98, 163, 255);
                                           border-radius:10px;
                                           }
                                           QPushButton:pressed{
                                           background-color: rgba(254, 121, 199, 255);
                                           border-radius:10px;
                                           }"""
            Lbstylesheet = """QLabel{color: rgba(98, 114, 164, {Lb})
                       }"""
            fLb_stylesheet = """QLabel{color: rgba(254, 121, 199,{rect})
                       }"""

        elif (CORSC == "3º  Dark"):
            stylesheet = """ 
                           QLineEdit{
                           background-color: rgba(61, 67, 79, {alphaC});
                           color: rgba(220, 203, 216, {alphaC});
                           font: 10pt "MS Shell Dlg 2";
                           border-radius: 10px;
                           padding-left:8px;
                           border:2px solid rgba(255, 120, 213, {alphaB});
                           }
                           QLineEdit:hover{
                           border:3px solid rgba(255, 120, 213, 255)
                           }
                           QLineEdit:focus{
                           border:3px solid rgba(199, 94, 167, {alphaC})

                           }"""
            btnStylesheet = """QPushButton{
                               background-color: rgba(225, 107, 178, {alpha});
                               border-radius:10px;
                               }
                               QPushButton:hover{
                               background-color: rgba(206, 98, 163, 255);
                               border-radius:10px;
                               }
                               QPushButton:pressed{
                               background-color: rgba(254, 121, 199, 255);
                               border-radius:10px;
                               }"""
            Lbstylesheet = """QLabel{color: rgba(220, 203, 216, {Lb})
                                   }"""
            fLb_stylesheet = """QLabel{color: rgba(254, 121, 199,{rect})
                       }"""

        elif (CORSC == "4º  BlueGreen"):
            stylesheet = """ 
                           QLineEdit{
                           background-color: rgba(120, 139, 180, {alphaC});
                           color: rgba(220, 203, 216, {alphaC});
                           font: 10pt "MS Shell Dlg 2";
                           border-radius: 10px;
                           padding-left:8px;
                           border:2px solid rgba(255, 120, 213, {alphaB});
                           }
                           QLineEdit:hover{
                           border:3px solid rgba(255, 120, 213, 255)
                           }
                           QLineEdit:focus{
                           border:3px solid rgba(199, 94, 167, {alphaC})

                           }"""
            btnStylesheet = """QPushButton{
                                           background-color: rgba(225, 107, 178, {alpha});
                                           border-radius:10px;
                                           }
                                           QPushButton:hover{
                                           background-color: rgba(206, 98, 163, 255);
                                           border-radius:10px;
                                           }
                                           QPushButton:pressed{
                                           background-color: rgba(254, 121, 199, 255);
                                           border-radius:10px;
                                           }"""
            Lbstylesheet = """QLabel{color: rgba(220, 203, 216, {Lb})}"""
            # rect logo
            fLb_stylesheet = """QLabel{color: rgba(254, 121, 199,{rect})
           }"""


        if counter >= 120 + test and counter <= 254:
            self.ui.name.show()
            self.ui.nameYourA.show()
            self.ui.logo.show()
            counter_rect = counter

            newfLb_stylesheet = fLb_stylesheet.replace("{rect}", str(counter_rect))

            self.ui.name.setStyleSheet(newfLb_stylesheet)
            self.ui.nameYourA.setStyleSheet(newfLb_stylesheet)

        if counter >= 130 + test and counterLb1 <= 254:
            self.ui.yourApp.show()
            a = counter
            b = a - 1
            a = a - b
            counterLb1 += (a + 4)
            newLbstylesheet1 = Lbstylesheet.replace("{Lb}", str(counterLb1))
            self.ui.yourApp.setStyleSheet(newLbstylesheet1)

        if counter >= 140 + test and counterLb2 <= 254:
            self.ui.discricao.show()
            a = counter
            b = a - 1
            a = a - b
            counterLb2 += (a + 4)
            newLbstylesheet2 = Lbstylesheet.replace("{Lb}", str(counterLb2))
            self.ui.discricao.setStyleSheet(newLbstylesheet2)

        if counter >= 160 + test and counter1 <= 254:
            self.ui.ld_user.show()
            a = counter
            b = a - 1
            a = a - b
            counter1 += (a + 4)
            lineEdit = str(counter1)
            borda = str(counter1)
            newstylesheet = stylesheet.replace("{alphaC}", lineEdit).replace("{alphaB}", borda).replace("{alphaC}",
                                                                                                        borda)
            self.ui.ld_user.setStyleSheet(newstylesheet)

        if counter >= 175 + test and counter2 <= 254:
            self.ui.ld_Pass.show()
            a = counter
            b = a - 1
            a = a - b
            counter2 += (a + 4)
            lineEdit2 = str(counter2)
            borda2 = str(counter2)
            newstylesheet2 = stylesheet.replace("{alphaC}", lineEdit2).replace("{alphaB}", borda2).replace("{alphaC}",
                                                                                                           borda2)
            self.ui.ld_Pass.setStyleSheet(newstylesheet2)

        if counter >= 185 + test:
            self.ui.login_3.show()
            a = counter
            b = a - 1
            a = a - b
            counterBtn += (a + 4)
            newbtnStylesheet = btnStylesheet.replace("{alpha}", str(counterBtn))
            self.ui.login_3.setStyleSheet(newbtnStylesheet)

            if counterBtn == 225:
                # STOP TIMER
                self.timerAnimation.stop()

        # INCREASE COUNTER
        counter += 5

    # update progress bar
    def update(self):
        global counter

        # set value to progress bar
        self.progress.set_Value(counter)

        if counter == 99:
            self.progress.progress_width = 5

        # close sphash screen and open main app
        if counter >= 100:
            # stop time
            self.timer.stop()
            sleep(0.10)
            QTimer.singleShot(10, lambda: self.ResizeMainWindow())
            self.progress.close()
            QTimer.singleShot(5, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.login))

            # timer in miliseconds
            self.timerAnimation.start(5)

            #self.timerG.start(5)

        # interface countet
        counter += 1

    def ResizeMainWindow(self):
        # ccreat animation
        width = 341
        heigth = 520
        self.animation = QPropertyAnimation(self, b"size")
        self.animation.setDuration(700)
        self.animation.setEndValue(QSize(width, heigth))
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)

        self.moveAnimtion = QPropertyAnimation(self, b'pos')
        self.moveAnimtion.setStartValue(QPoint(522, 214))
        self.moveAnimtion.setEndValue(QPoint(522, 140))
        self.moveAnimtion.setDuration(700)
        self.moveAnimtion.setEasingCurve(QEasingCurve.InOutCirc)

        self.group_animation = QParallelAnimationGroup()
        self.group_animation.addAnimation(self.animation)
        self.group_animation.addAnimation(self.moveAnimtion)
        self.group_animation.start()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def login(self):
        nome = self.ui.ld_user.text()
        passW = self.ui.ld_Pass.text()

        db = database('SQLite')
        db.connect_database()
        cadastrados = db.select_from('Users')
        db.close_connection_database()

        if nome == cadastrados[0][1]:  # and

            if passW == cadastrados[0][2]:

                self.ui.ld_user.setStyleSheet("border:3px solid rgb(85, 255, 127)")

                self.ui.ld_user.setText("")
                self.ui.ld_Pass.setText("")

                self.mainW = MainWindow()
                QTimer.singleShot(400, lambda: self.mainW.show())
                self.close()
                # self.ui.ld_Pass.setStyleSheet("border:3px solid rgb(85, 255, 127)")

            else:
                with open('Tema.txt', 'r') as cort:
                    cor = cort.read()
                    if (cor == "1º  Normal"):
                        self.ui.ld_Pass.setStyleSheet("QLineEdit{background-color: rgb(70, 72, 111);"
                                                      " border:3px solid rgb(255, 0, 0)}")

                    elif (cor == "2º  Light"):
                        self.ui.ld_Pass.setStyleSheet("QLineEdit{background-color: rgb(255, 255, 255); "
                                                      "border:3px solid rgb(255, 0, 0)}")

                    elif (cor == "3º  Dark"):
                        self.ui.ld_Pass.setStyleSheet("QLineEdit{background-color: rgb(61, 67, 79); "
                                                      "border:3px solid rgb(255, 0, 0)}")

                    elif (cor == "4º  BlueGreen"):
                        self.ui.ld_Pass.setStyleSheet("QLineEdit{background-color: rgb(120, 139, 180);"
                                                      " border:3px solid rgb(255, 0, 0)}")

                self.pass_analityConst = len(self.ui.ld_Pass.text())
                QTimer.singleShot(200, lambda: self.pass_analityTimer.start())
                QTimer.singleShot(210, lambda: self.animatioError())

        else:
            with open('Tema.txt', 'r') as cort:
                cor = cort.read()
                if (cor == "1º  Normal"):
                    self.ui.ld_user.setStyleSheet("QLineEdit{background-color: rgb(70, 72, 111);"
                                                  " border:3px solid rgb(255, 0, 0)}")

                elif (cor == "2º  Light"):
                    self.ui.ld_user.setStyleSheet("QLineEdit{background-color: rgb(255, 255, 255); "
                                                  "border:3px solid rgb(255, 0, 0)}")

                elif (cor == "3º  Dark"):
                    self.ui.ld_user.setStyleSheet("QLineEdit{background-color: rgb(61, 67, 79); "
                                                  "border:3px solid rgb(255, 0, 0)}")

                elif (cor == "4º  BlueGreen"):
                    self.ui.ld_user.setStyleSheet("QLineEdit{background-color: rgb(120, 139, 180);"
                                                  " border:3px solid rgb(255, 0, 0)}")
            self.user_analityConst = len(self.ui.ld_user.text())
            QTimer.singleShot(200, lambda: self.user_analityTimer.start())
            QTimer.singleShot(210, lambda: self.animatioError())

    def user_anality(self, n):

        if n != self.user_analityConst:
            with open('Tema.txt', 'r') as cort:
                cor = cort.read()
                if (cor == "1º  Normal"):
                    self.ui.ld_user.setStyleSheet(u""" 
                            QLineEdit{
                            background-color: rgb(70, 72, 111);
                            color: rgb(220, 203, 216);
                            font: 10pt "MS Shell Dlg 2";
                            border-radius: 10px;
                            padding-left:8px;
                            border	:	2px solid   rgb(255, 120, 213);
                            }
                            QLineEdit:hover{
                            border	:	3px solid   rgb(255, 120, 213)
                            }
                            QLineEdit:focus{
                            border	:	3px solid  rgb(199, 94, 167)
                            }""")

                elif (cor == "2º  Light"):
                    self.ui.ld_user.setStyleSheet(u""" 
                                        QLineEdit{
                                        background-color: rgb(255, 255, 255);
                                        color: rgb(98, 114, 164);
                                        font: 10pt "MS Shell Dlg 2";
                                        border-radius: 10px;
                                        padding-left:8px;
                                        border	:	2px solid   rgb(255, 120, 213);
                                        }
                                        QLineEdit:hover{
                                        border	:	3px solid   rgb(255, 120, 213)
                                        }
                                        QLineEdit:focus{
                                        border	:	3px solid  rgb(199, 94, 167)
                                        }""")

                elif (cor == "3º  Dark"):
                    self.ui.ld_user.setStyleSheet(u""" 
                                        QLineEdit{
                                        background-color: rgb(61, 67, 79);
                                        color: rgb(220, 203, 216);
                                        font: 10pt "MS Shell Dlg 2";
                                        border-radius: 10px;
                                        padding-left:8px;
                                        border	:	2px solid   rgb(255, 120, 213);
                                        }
                                        QLineEdit:hover{
                                        border	:	3px solid   rgb(255, 120, 213)
                                        }
                                        QLineEdit:focus{
                                        border	:	3px solid  rgb(199, 94, 167)
                                        }""")

                elif (cor == "4º  BlueGreen"):
                    self.ui.ld_user.setStyleSheet(u""" 
                                                   QLineEdit{
                                                   background-color: rgb(120, 139, 180);
                                                   color: rgb(220, 203, 216);
                                                   font: 10pt "MS Shell Dlg 2";
                                                   border-radius: 10px;
                                                   padding-left:8px;
                                                   border	:	2px solid   rgb(255, 120, 213);
                                                   }
                                                   QLineEdit:hover{
                                                   border	:	3px solid   rgb(255, 120, 213)
                                                   }
                                                   QLineEdit:focus{
                                                   border	:	3px solid  rgb(199, 94, 167)
                                                   }""")
            self.user_analityTimer.stop()

    def pass_anality(self, n):

        if n != self.pass_analityConst:

            with open('Tema.txt', 'r') as cort:
                cor = cort.read()
                if (cor == "1º  Normal"):
                    self.ui.ld_Pass.setStyleSheet(u""" 
                            QLineEdit{
                            background-color: rgb(70, 72, 111);
                            color: rgb(220, 203, 216);
                            font: 10pt "MS Shell Dlg 2";
                            border-radius: 10px;
                            padding-left:8px;
                            border	:	2px solid   rgb(255, 120, 213);
                            }
                            QLineEdit:hover{
                            border	:	3px solid   rgb(255, 120, 213)
                            }
                            QLineEdit:focus{
                            border	:	3px solid  rgb(199, 94, 167)
                            }""")

                elif (cor == "2º  Light"):
                    self.ui.ld_Pass.setStyleSheet(u""" 
                                        QLineEdit{
                                        background-color: rgb(255, 255, 255);
                                        color: rgb(98, 114, 164);
                                        font: 10pt "MS Shell Dlg 2";
                                        border-radius: 10px;
                                        padding-left:8px
                                        border	:	2px solid   rgb(255, 120, 213);
                                        }
                                        QLineEdit:hover{
                                        border	:	3px solid   rgb(255, 120, 213)
                                        }
                                        QLineEdit:focus{
                                        border	:	3px solid  rgb(199, 94, 167)
                                        }""")

                elif (cor == "3º  Dark"):
                    self.ui.ld_Pass.setStyleSheet(u""" 
                                        QLineEdit{
                                        background-color: rgb(61, 67, 79);
                                        color: rgb(220, 203, 216);
                                        font: 10pt "MS Shell Dlg 2";
                                        border-radius: 10px;
                                        padding-left:8px
                                        border	:	2px solid   rgb(255, 120, 213);
                                        }
                                        QLineEdit:hover{
                                        border	:	3px solid   rgb(255, 120, 213)
                                        }
                                        QLineEdit:focus{
                                        border	:	3px solid  rgb(199, 94, 167)
                                        }""")

                elif (cor == "4º  BlueGreen"):
                    self.ui.ld_Pass.setStyleSheet(u""" 
                                                   QLineEdit{
                                                   background-color: rgb(120, 139, 180);
                                                   color: rgb(220, 203, 216);
                                                   font: 10pt "MS Shell Dlg 2";
                                                   border-radius: 10px;
                                                   padding-left:8px
                                                   border	:	2px solid   rgb(255, 120, 213);
                                                   }
                                                   QLineEdit:hover{
                                                   border	:	3px solid   rgb(255, 120, 213)
                                                   }
                                                   QLineEdit:focus{
                                                   border	:	3px solid  rgb(199, 94, 167)
                                                   }""")

            self.pass_analityTimer.stop()

    def animatioError(self):
        x, y = self.pos().x(), self.pos().y()
        QTimer.singleShot(50, lambda: self.move(QPoint(x+3, y)))
        QTimer.singleShot(100, lambda: self.move(QPoint(x-3, y)))
        QTimer.singleShot(150, lambda: self.move(QPoint(x+3, y)))
        QTimer.singleShot(200, lambda: self.move(QPoint(x-3, y)))
        QTimer.singleShot(250, lambda: self.move(QPoint(x+3, y)))
        QTimer.singleShot(300, lambda: self.move(QPoint(x-3, y)))
        QTimer.singleShot(350, lambda: self.move(QPoint(x, y)))

    def tema(self, cor):

        if(cor == "1º  Normal"):
            self.ui.stackedWidget.setStyleSheet("""
            background-color: rgb(56, 58, 89);
            color:rgb(220, 220, 220);
            border-radius:10px;
            """)
            self.ui.centro.setStyleSheet("""
            QLineEdit{
            background-color: rgb(70, 72, 111);
            color: rgb(220, 203, 216);
            font: 10pt "MS Shell Dlg 2";
            border-radius: 10px;
            border	:	2px solid   rgb(255, 120, 213);
            }
            QLineEdit:hover{
            border	:	3px solid   rgb(255, 120, 213)
            }
            QLineEdit:focus{
            border	:	3px solid  rgb(199, 94, 167)
            }
            """)
            self.ui.yourApp.setStyleSheet("color: rgb(98, 114, 164);")
            self.ui.discricao.setStyleSheet("color: rgb(98, 114, 164);")
            self.progress.progress_color = 0xFF79c6

        elif(cor == "2º  Light"):
            self.ui.stackedWidget.setStyleSheet("""
                        background-color: rgb(255, 255, 255);
                        color:rgb(220, 220, 220);
                        border-radius:10px;
                        """)
            self.ui.centro.setStyleSheet("""
                        QLineEdit{
                        background-color: rgb(255, 255, 255);
                        color: rgb(98, 114, 164);
                        font: 10pt "MS Shell Dlg 2";
                        border-radius: 10px;
                        border	:	2px solid   rgb(255, 120, 213);
                        }
                        QLineEdit:hover{
                        border	:	3px solid   rgb(255, 120, 213)
                        }
                        QLineEdit:focus{
                        border	:	3px solid  rgb(199, 94, 167)
                        }
                        """)
            self.ui.yourApp.setStyleSheet("color: rgb(98, 114, 164);")
            self.ui.discricao.setStyleSheet("color: rgb(98, 114, 164);")
            self.progress.progress_color = 0xFc79d4
            self.ui.by.setStyleSheet('color: rgb(98, 114, 164)')

        elif(cor == "3º  Dark"):
            self.ui.stackedWidget.setStyleSheet("""
                        background-color: rgb(61, 67, 79);
                        color:rgb(220, 220, 220);
                        border-radius:10px;
                        """)
            self.ui.centro.setStyleSheet("""
                        QLineEdit{
                        background-color: rgb(61, 67, 79);
                        color: rgb(255, 255, 255);
                        font: 10pt "MS Shell Dlg 2";
                        border-radius: 10px;
                        border	:	2px solid   rgb(255, 120, 213);
                        }
                        QLineEdit:hover{
                        border	:	3px solid   rgb(255, 120, 213)
                        }
                        QLineEdit:focus{
                        border	:	3px solid  rgb(199, 94, 167)
                        }
                        """)
            self.ui.yourApp.setStyleSheet("color: rgb(220, 203, 216);")
            self.ui.discricao.setStyleSheet("color: rgb(220, 203, 216);")
            self.progress.progress_color = 0xFF79c6

        elif(cor == "4º  BlueGreen"):
            self.ui.stackedWidget.setStyleSheet("""
            background-color: rgb(120, 139, 180);
            color:rgb(220, 203, 216);
            border-radius:10px;""")
            self.ui.centro.setStyleSheet("""
                                   QLineEdit{
                                   background-color: rgb(220, 203, 216);
                                   color: rgb(255, 255, 255);
                                   font: 10pt "MS Shell Dlg 2";
                                   border-radius: 10px;
                                   border	:	2px solid   rgb(255, 120, 213);
                                   }
                                   QLineEdit:hover{
                                   border	:	3px solid   rgb(255, 120, 213)
                                   }
                                   QLineEdit:focus{
                                   border	:	3px solid  rgb(199, 94, 167)
                                   }
                                   """)
            self.ui.yourApp.setStyleSheet("color: rgb(98, 114, 164);")
            self.ui.discricao.setStyleSheet("color: rgb(98, 114, 164);")
            self.progress.progress_color = 0xFF79c6

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.move(150, 40)

        # selecao de tema automatica
        global CORTEMA

        try:
            with open("Tema.txt", "r") as CORTEMA:
                self.ui.atualTema = CORTEMA.read()
                self.tema(self.ui.atualTema)

        except:
            with open("Tema.txt", "w") as CORTEMA:
                CORTEMA.write("1º  Normal")


        # DEFINIR FUNCOES UI
        self.uiDefinicoes()

        # MOSTRAR TELA
        self.show()

        # MAXIMO RESTAURO

    # MAXIMIZARA TELA
    def maximizarRestauro(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        unckechdIcon = QIcon()

        # SE NAO MXIMIZAR
        if status == 0:

            # MUDANCA DE ICON cil-window-restore
            unckechdIcon.addFile(u"../imagens/ICons/cil-window-restore", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.unckechd.setIcon(unckechdIcon)
            self.showMaximized()

            # DEFINI O GLOBAL PARA 1
            GLOBAL_STATE = 1
            self.ui.unckechd.setToolTip("Retaura")
            # retira o redimencinamento
            self.top.hide()
            self.bottom.hide()
            self.left.hide()
            self.right.hide()

        else:

            # MUDANCA DE ICON
            unckechdIcon.addFile(u"../imagens/ICons/cil-media-stop.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.unckechd.setIcon(unckechdIcon)
            self.showNormal()

            # DEFINI O GLOBAL PARA 1
            GLOBAL_STATE = 0
            self.ui.unckechd.setToolTip("Maximizar")
            # vota o redimencionamento
            self.top.show()
            self.bottom.show()
            self.left.show()
            self.right.show()

    # RESTAURO DO MENU ESQUERDO
    def restauroMenuEsq(self, menu):
        tamanho_menu = menu.width()

        tamanho = 56
        if tamanho_menu == 56:
            tamanho = 200

        self.animation = QPropertyAnimation(menu, b"minimumWidth")
        self.animation.setStartValue(tamanho_menu)
        self.animation.setEndValue(tamanho)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()

    # FUNCAO PARA ABRIO O MENU DIREITO
    def restauroMenuDir(self):

        tamanho_principal = self.ui.settings_menu_2.width()
        tamanho_segundario = self.ui.settings_menu.width()

        tamanho = 0
        if tamanho_principal == 0:
            tamanho = 200
            self.corBtn(True)
        else:
            self.corBtn(False)

        if tamanho_principal == 0 and tamanho_segundario == 200:
            self.CaixaAnimacaoGrupo("direita")

        else:
            self.animation = QPropertyAnimation(self.ui.settings_menu_2, b"minimumWidth")
            self.animation.setStartValue(tamanho_principal)
            self.animation.setEndValue(tamanho)
            self.animation.setDuration(500)
            self.animation.setEasingCurve(QEasingCurve.InOutCirc)
            self.animation.start()

    # FUNCAO QUE TROCA A INFORMAVO E ABRE A CONFI TEMA
    def configInf(self, page):
        tamanho_principal = self.ui.settings_menu.width()

        tamanho_segundario = self.ui.settings_menu_2.width()

        tamanho = 0
        if tamanho_principal == 0 and tamanho_segundario == 0:
            tamanho = 200

            self.animation = QPropertyAnimation(self.ui.settings_menu, b"minimumWidth")
            self.animation.setStartValue(tamanho_principal)
            self.animation.setEndValue(tamanho)
            self.animation.setDuration(500)
            self.animation.setEasingCurve(QEasingCurve.InOutCirc)
            self.animation.start()


        elif tamanho_principal == 0 and tamanho_segundario == 200:
            self.CaixaAnimacaoGrupo("esquerda")

        self.ui.stackedWidget_2.addWidget(page)

    # CAIXA DE ANIMACAO
    def CaixaAnimacaoGrupo(self, direcao):

        tamanhoEsq = tamanhoDir = 0

        menuEsq = self.ui.settings_menu
        menuDir = self.ui.settings_menu_2

        if direcao == "esquerda":
            tamanhoEsq = 0
            fE = 200
            self.corBtn(False)
            tamanhoDir = 200
            fD = 0
        if direcao == "direita":
            tamanhoEsq = 200
            fE = 0
            self.corBtn(True)
            tamanhoDir = 0
            fD = 200

        self.animationEsq = QPropertyAnimation(menuEsq, b"minimumWidth")
        self.animationEsq.setStartValue(tamanhoEsq)
        self.animationEsq.setEndValue(fE)
        self.animationEsq.setDuration(500)
        self.animationEsq.setEasingCurve(QEasingCurve.InOutCirc)

        self.animationDir = QPropertyAnimation(menuDir, b"minimumWidth")
        self.animationDir.setStartValue(tamanhoDir)
        self.animationDir.setEndValue(fD)
        self.animationDir.setDuration(500)
        self.animationDir.setEasingCurve(QEasingCurve.InOutCirc)

        self.grupo = QParallelAnimationGroup()
        self.grupo.addAnimation(self.animationEsq)
        self.grupo.addAnimation(self.animationDir)
        self.grupo.start()

    # FUNCAO PARA FECHAR O MENU DE TEMA
    def FecharSI(self):
        self.animation = QPropertyAnimation(self.ui.settings_menu, b"minimumWidth")
        self.animation.setStartValue(200)
        self.animation.setEndValue(0)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()

    # FUNCAO QUE PEGA A POSICAO GERAL DA BARRA DE TITULO
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    # FUNCAO DA COR DO BTN
    def corBtn(self, estado):

        if estado == True:
            self.ui.Settings_right.setStyleSheet(StyleLocal.QtoolRosa)
        else:
            self.ui.Settings_right.setStyleSheet(StyleLocal.QtoolSinza)

    # FUNCAO PARA MUDAR DE TELA
    def troca(self):
        btn = self.sender()
        btnName = btn.objectName()

        mudaBorda = btn.setStyleSheet(StyleLocal.btnPressed)
        self.clickMud(btnName)

        if btnName == "CatPage":
            self.ui.stackedWidget.setCurrentWidget(self.ui.CatPage)
        if btnName == "New":
            self.ui.stackedWidget.setCurrentWidget(self.ui.NewPage)
        if btnName == "Home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.Principal_page)
        if btnName == "Widgets":
            self.ui.stackedWidget.setCurrentWidget(self.ui.WidgetsPage)

    # FUNCATO RESPONSAVEL PARA MUDAR O ESTILO QUANDO CLICKAS
    def clickMud(self, btn):

        if btn == "New":
            self.ui.Widgets.setStyleSheet(StyleLocal.btnNormal)
            self.ui.Home.setStyleSheet(StyleLocal.btnNormal)
        if btn == "Home":
            self.ui.Widgets.setStyleSheet(StyleLocal.btnNormal)
            self.ui.New.setStyleSheet(StyleLocal.btnNormal)
        if btn == "Widgets":
            self.ui.Home.setStyleSheet(StyleLocal.btnNormal)
            self.ui.New.setStyleSheet(StyleLocal.btnNormal)

    def fechar(self):
        self.close()
        quit()

    # DEFINICOES UI(Interface DE Usuario)
    def uiDefinicoes(self):
        # REMOVE A BARRA DE TITULO
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        #  OS BOTOES PRINCIPAL DA PARRA DE TITULO
        self.ui.unckechd.clicked.connect(lambda: self.maximizarRestauro())
        self.ui.Minimu.clicked.connect(lambda: self.showMinimized())
        self.ui.close.clicked.connect(self.fechar)
        self.ui.OpenFolder.clicked.connect(self.openfile)

        # MENU PRINCIPAL
        self.ui.Hilder.clicked.connect(lambda: self.restauroMenuEsq(self.ui.Menu_lateral))

        # MENU DE CONFIG TEMA
        self.ui.LeftBox.clicked.connect(lambda: self.configInf(self.ui.page_3))
        self.ui.Infor.clicked.connect(lambda: self.configInf(self.ui.page_4))
        self.ui.toolButton_5.clicked.connect(lambda: self.FecharSI())

        # MENU DE OUTRAS INFORMACOES
        self.ui.Settings_right.clicked.connect(lambda: self.restauroMenuDir())

        # trocar pagina
        self.ui.Widgets.clicked.connect(self.troca)
        self.ui.Home.clicked.connect(self.troca)
        self.ui.New.clicked.connect(self.troca)

        # mudar tema
        self.ui.selectTheme.currentTextChanged.connect(self.tema)

        #  SIZE GRIP
        self.sizegrip = QSizeGrip(self.ui.frame_SizeGrip_2)

        # FUNCAO PARA MOVER O STATUS
        def moveWindow(event):
            # if self.returnStatu() == 1:
            #    self.maximize_restore()

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # add BARRA ED TITULO NA FUNCAO
        self.ui.dock_widget.mouseMoveEvent = moveWindow

        # PARA RESTAURA ATELA Clicck  DUAS VEZES
        def dobleClickMaximizeRestore(event):
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(250, lambda: self.maximizarRestauro())

        self.ui.dock_widget.mouseDoubleClickEvent = dobleClickMaximizeRestore

        # cumtomGrip e um funcao criada por wanersom pimenta que usa 4 frame
        # avaolta para podermos redimencionar a janela
        # e ela para redimencionar a janela teremos que usar duas funcoes o
        # resizeEvente e uma funcao para mudar as dimwnsoes deles
        self.left = CustomGrip(self, Qt.LeftEdge, True)
        self.right = CustomGrip(self, Qt.RightEdge, True)
        self.top = CustomGrip(self, Qt.TopEdge, True)
        self.bottom = CustomGrip(self, Qt.BottomEdge, True)

    # funcao para mudar tema
    def tema(self, tema):
        global CORTEMA

        if (tema == "1º  Normal"):
            self.ui.btns.setStyleSheet("""QToolButton{
                                        color: #c3ccdf;
                                        border: none;
                                        border-radius:3px;
                                        }
                                        
                                        QToolButton:hover {
                                        background-color: rgb(67, 70, 107);
                                        border: none;
                                        border-radius:3px;
                                        }
                                        
                                        QToolButton:pressed {
                                        background-color: rgb(96, 100, 152);
                                        border: none;
                                        border-radius:3px;        
                                        }
                                        """)
            self.ui.dock_widget.setStyleSheet("background-color: rgb(41, 42, 65);")
            self.ui.Menu_lateral.setStyleSheet("background-color: rgb(41, 42, 65);")  # add o style do tootip
            self.ui.decricao.setStyleSheet("background-color: rgb(41, 42, 65);")
            self.ui.dock_widget_2.setStyleSheet("background-color: rgb(41, 42, 65);")
            self.ui.logo1.setStyleSheet("""border-radius:10px;
                                           border-radius:10px;
                                           background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0,
                                           stop:0.275992 rgba(248, 118, 205, 255),
                                           stop:0.286836 rgb(41, 42, 65),
                                           stop:0.457627 rgb(41, 42, 65),
                                           stop:0.468927 rgba(248, 118, 205, 255));""")
            self.ui.logo2.setStyleSheet("""background-color: rgb(41, 42, 65);
                                            border-radius:17px;""")
            self.ui.logo3.setStyleSheet("""border-radius: 14px;
                                           background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0
                                           stop:0.0568182 rgba(248, 118, 205, 255),
                                           stop:0.829545 rgba(248, 118, 205, 255),
                                           stop:0.840909 rgb(41, 42, 65),
                                           stop:0.982955 rgb(41, 42, 65));""")
            self.ui.logo4.setStyleSheet("""background-color: rgb(41, 42, 65);
                                           border-radius:12px;;""")
            self.ui.logo5.setStyleSheet("""border-radius:8px;
                                           background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0,
                                           stop:0.0795455 rgba(248, 118, 205, 255),
                                           stop:0.448864 rgb(41, 42, 65),
                                           stop:0.676136 rgb(41, 42, 65),
                                           stop:0.6875 rgba(248, 118, 205, 255));""")
            self.ui.logo6.setStyleSheet("""border-Radius:6px;
                                           background-color: rgb(41, 42, 65);""")
            self.ui.logo7.setStyleSheet("""background-color: rgb(248, 118, 205);
                                           border-radius:1px;""")

            self.ui.frame_btn_bottom.setStyleSheet("""QPushButton{
                                                     color: #c3ccdf;
                                                     padding-left: 18px;
                                                     text-align: left;
                                                     border: none;
                                                     }
                                                    
                                                     QPushButton:hover {
                                                     background-color:rgb(67, 70, 107);
                                                     }
                                                    
                                                     QPushButton:pressed {
                                                     background-color: rgb(186, 135, 245);
                                                     }""")
            self.ui.frame_btn_top.setStyleSheet("""QPushButton{
                                                     color: #c3ccdf;
                                                     padding-left: 18px;
                                                     text-align: left;
                                                     border: none;
                                                     }

                                                     QPushButton:hover {
                                                     background-color:rgb(67, 70, 107);
                                                     }

                                                     QPushButton:pressed {
                                                     background-color: rgb(186, 135, 245);
                                                     }""")
            self.ui.statusBar.setStyleSheet("background-color: rgb(65, 68, 104);")
            self.ui.settings_menu.setStyleSheet("background-color: rgb(59, 61, 94);")
            self.ui.label_20.setStyleSheet("color: rgb(255, 255, 255)")
            self.ui.selectTheme.setStyleSheet("""
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

            self.ui.horizontalSlider.setStyleSheet("""QSlider::groove:horizontal{
                                                        background-color: rgb(41, 42, 65);
                                                        border: none;
                                                        margin: 0px;
                                                        border-radius: 5px;
                                                        }
                                                        QSlider::handle:horizontal {
                                                        background-color: rgb(195, 155, 255);
                                                        border: none;
                                                        height: 10px;
                                                        width: 10px;
                                                        margin: 0px;
                                                        border-radius: 5px;
                                                        }
                                                        QSlider::handle:horizontal:hover {
                                                        background-color: rgb(195, 155, 255);
                                                        }
                                                    """)
            self.ui.comboBox_2.setStyleSheet("""
QComboBox{
	background-color:rgb(41, 42, 65);
	border-radius: 5px;
	border: 2px solid rgb(41, 42, 65);
	padding: 5px;
	padding-left: 10px;
	color: rgb(255, 255, 255);
}
QComboBox:hover{
	border: 2px solid rgb(73, 76, 116);
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
}

""")
            self.ui.radioButton.setStyleSheet("""
QRadioButton{color:rgb(255, 255, 255)}
QRadioButton::indicator {
    border: 3px solid rgb(52, 59, 72);
	width: 15px;
	height: 15px;
	border-radius: 10px;
    background: rgb(41, 42, 65);
}
QRadioButton::indicator:hover {
    border: 3px solid rgb(73, 76, 116);
}
QRadioButton::indicator:checked {
    background: 3px solid rgb(73, 76, 116);
	border: 3px solid rgb(41, 42, 65)	
}
""")
            self.ui.checkBox.setStyleSheet("""QCheckBox{color: rgb(255, 255, 255);}

QCheckBox::indicator {
    border: 3px solid rgb(52, 59, 72);
	width: 15px;
	height: 15px;
	border-radius: 10px;
    background: rgb(41, 42, 65);
}
QCheckBox::indicator:hover {
    border: 3px solid rgb(58, 66, 81);
}
QCheckBox::indicator:checked {
    background: 3px solid rgb(52, 59, 72);
	border: 3px solid rgb(52, 59, 72);	
	background-image: url(:/icons/cil-check-alt.png);
}""")
            self.ui.verticalSlider.setStyleSheet("""QSlider::groove:vertical{
	background-color: rgb(41, 42, 65);
    border: none;
 	height: 120px;
    margin: 0px;
	border-radius: 5px;
}
QSlider::handle:vertical {
	background-color: rgb(195, 155, 255);
    border: none;
    height: 10px;
    width: 10px;
    margin: 0px;
	border-radius: 5px;
}
QSlider::handle:horizontal:hover {
    background-color: rgb(195, 155, 255);
}""")

            self.ui.horizontalSlider_2.setStyleSheet("""
                                                        QSlider::groove:horizontal{
                                                        background-color: rgb(41, 42, 65);
                                                        border: none;
                                                        margin: 0px;
                                                        border-radius: 5px;
                                                        }
                                                        
                                                        QSlider::handle:horizontalal {
                                                        background-color: rgb(189, 147, 249);
                                                        border: none;
                                                        height: 0px;
                                                        width: 25px;
                                                        margin: 0px;
                                                        border-radius: 5px;
                                                        }
                                                        QSlider::handle:verticall:hover {
                                                        background-color: rgb(195, 155, 255);
                                                        }""")
            self.ui.plainTextEdit.setStyleSheet("""
            QPlainTextEdit{
            background-color: rgb(41, 42, 65);
            border-radius:8px;}
            
            QPlainTextEdit:hover{
            border: 2px solid rgb(73, 76, 116);}
            
            QPlainTextEdit:focus{
            color: rgb(255, 255, 255);
            border: 2px solid rgb(90, 95, 145)}
            """)
            self.ui.commandLinkButton.setStyleSheet("""QCommandLinkButton{
color: rgb(195, 155, 255);
border:none;
border-radius:7px;
border: 2px solid rgb(73, 76, 116);}

QCommandLinkButton:hover{
color: rgb(195, 155, 255);
border:none;
border-radius:7px;
border: 2px solid rgb(116, 91, 153)}

QCommandLinkButton:pressed{
color: rgb(195, 155, 255);
border:none;
border-radius:7px;

}



            """)
            self.ui.lineEdit.setStyleSheet("""QLineEdit{
	background-color: rgb(41, 42, 65);
	border-color:rgb(41, 42, 65);
	border-radius:8px
}

QLineEdit:hover{
	background-color: rgb(41, 42, 65);
	border-color:rgb(41, 42, 65);
	border: 2px solid rgb(73, 76, 116);
	border-radius:8px
}
QLineEdit:focus {
	background-color: rgb(41, 42, 65);
	border-color:rgb(41, 42, 65);
	border: 2px solid rgb(90, 95, 145);
	border-radius:8px
}""")
            self.ui.OpenFolder.setStyleSheet("""QPushButton{
	border-radius:8px;
	color: rgb(255, 255, 255);
	background-color:rgb(73, 76, 116);
}

QPushButton:hover{
	border-radius:8px;
	color: rgb(255, 255, 255);
	background-color:rgb(73, 76, 116);
	border: 2px solid rgb(94, 99, 150);
}
QPushButton:pressed{
	border-radius:8px;
	color: rgb(255, 255, 255);
	background-color:rgb(73, 76, 116);
	padding-top: 3px;
}""")
            self.ui.verticalSlider.setStyleSheet("""
                                            QSlider::groove:vertical{
                                            background-color: rgb(41, 42, 65);
                                            border: none;
                                            height: 120px;
                                            margin: 0px;
                                            border-radius: 5px;
                                            }
                                            QSlider::handle:vertical {
                                            background-color: rgb(195, 155, 255);
                                            border: none;
                                            height: 10px;
                                            width: 10px;
                                            margin: 0px;
                                            border-radius: 5px;
                                            }
                                            QSlider::handle:horizontal:hover {
                                            background-color: rgb(195, 155, 255);
                                                }""")
            self.ui.tableWidget_2.setStyleSheet("""QTableWidget {	
                                                                    color: rgb(255, 255, 255);
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
                                                                }
                                                                """)
            self.ui.verticalSlider_2.setStyleSheet("""
                                                    QSlider::groove:vertical{
                                                    background-color: rgb(41, 42, 65);
                                                    border: none;
                                                    height: 120px;
                                                    margin: 0px;
                                                    border-radius: 5px;
                                                    }
                                                    QSlider::handle:vertical {
                                                    background-color: rgb(195, 155, 255);
                                                    border: none;
                                                    height: 25px;
                                                    width: 10px;
                                                    margin: 0px;
                                                    border-radius: 5px;
                                                    }
                                                    QSlider::handle:horizontal:hover {
                                                    background-color: rgb(195, 155, 255);
                                                    }""")


            self.ui.stackedWidget.setStyleSheet("background-color: rgb(56, 58, 89);")
            self.ui.settings_menu_2.setStyleSheet("background-color: rgb(62, 65, 99);")
            self.ui.frame_central.setStyleSheet("background-color: rgb(56, 58, 89);")

            with open("Tema.txt", "w") as CORTEMA:
                CORTEMA.write("1º  Normal")

        if (tema == "2º  Light"):
            self.ui.btns.setStyleSheet("""
                                        QToolButton{
                                        color: #c3ccdf;
                                        border: none;
                                        border-radius:3px;
                                        }
                                        
                                        QToolButton:hover {
                                        background-color: rgb(189, 147, 249);
                                        border: none;
                                        border-radius:3px;
                                        }
                                        
                                        QToolButton:pressed {
                                        background-color: rgb(208, 161, 249);
                                        border: none;
                                        border-radius:3px;        
                                        }
                                        """)
            self.ui.dock_widget.setStyleSheet("""background-color: rgb(98, 114, 164);""")  # add o style do tootip
            self.ui.Menu_lateral.setStyleSheet("""background-color: rgb(98, 114, 164);""")
            self.ui.decricao.setStyleSheet("background-color: rgb(98, 114, 164);")
            self.ui.dock_widget_2.setStyleSheet("background-color: rgb(98, 114, 164);")
            self.ui.logo1.setStyleSheet("""border-radius:10px;
                                                        background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0,
                                                        stop:0.275992 rgba(248, 118, 205, 255),
                                                        stop:0.286836 rgb(91, 105, 150),
                                                        stop:0.457627 rgb(91, 105, 150),
                                                        stop:0.468927 rgba(248, 118, 205, 255));""")
            self.ui.logo2.setStyleSheet("""background-color: rgb(98, 114, 164);
                                                         border-radius:17px;""")
            self.ui.logo3.setStyleSheet("""border-radius: 14px;
                                                         background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0
                                                         stop:0.0568182 rgba(248, 118, 205, 255),
                                                         stop:0.829545 rgba(248, 118, 205, 255),
                                                         stop:0.840909 rgb(91, 105, 150),
                                                         stop:0.982955 rgb(91, 105, 150));""")
            self.ui.logo4.setStyleSheet("""background-color: rgb(91, 105, 150);
                                                         border-radius:12px;""")
            self.ui.logo5.setStyleSheet("""border-radius:8px;
                                                         background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0,
                                                         stop:0.0795455 rgba(248, 118, 205, 255),
                                                         stop:0.448864 rgb(91, 105, 150),
                                                         stop:0.676136 rgb(91, 105, 150),
                                                         stop:0.6875 rgba(248, 118, 205, 255));""")
            self.ui.logo6.setStyleSheet("""border-Radius:6px;
                                                         background-color: rgb(91, 105, 150);""")
            self.ui.logo7.setStyleSheet("""background-color: rgb(91, 105, 150);
                                                         border-radius:1px;""")

            self.ui.frame_btn_bottom.setStyleSheet("""QPushButton{
                                                     color: #c3ccdf;
                                                     padding-left: 18px;
                                                     text-align: left;
                                                     border: none;
                                                     }
                                                        
                                                     QPushButton:hover {
                                                     background-color: rgb(86, 99, 136);
                                                     }
                                                    
                                                     QPushButton:pressed {
                                                     background-color: rgb(186, 135, 245);
                                                     }""")
            self.ui.frame_btn_top.setStyleSheet("""QPushButton{
                                                                                  color: #c3ccdf;
                                                                                  padding-left: 18px;
                                                                                  text-align: left;
                                                                                  border: none;
                                                                                  }

                                                                                  QPushButton:hover {
                                                                                  background-color: rgb(86, 99, 136);
                                                                                  }

                                                                                  QPushButton:pressed {
                                                                                  background-color: rgb(186, 135, 245);
                                                                                  }""")
            self.ui.statusBar.setStyleSheet("background-color: rgb(70, 82, 118);")
            self.ui.settings_menu.setStyleSheet("background-color: rgb(70, 82, 118);")
            self.ui.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.ui.label_20.setStyleSheet("color: rgb(0, 0, 0)")
            self.ui.selectTheme.setStyleSheet("""
                                                QComboBox{
                                                    background-color: rgb(98, 114, 164);
                                                    border-radius: 5px;
                                                    border: 2px solid rgb(138, 161, 231);
                                                    padding: 5px;
                                                    padding-left: 10px;
                                                    color: rgb(255, 255, 255);
                                                }
                                                
                                                QComboBox:hover{
                                                    border: 2px solid rgb(178, 199, 255);
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
                                                    color:rgb(255, 255, 255);	
                                                    background-color: rgb(98, 114, 164);
                                                    padding: 10px;
                                                    selection-background-color: rgb(195, 155, 255);
                                                    border:2px solid  rgb(138, 161, 231);
                                                    border_top:none;
                                                    border-radius:5px;
                                                }""")

            self.ui.horizontalSlider.setStyleSheet("""QSlider::groove:horizontal{
                                                        background-color: rgb(98, 114, 164);
                                                        border: none;
                                                        margin: 0px;
                                                        border-radius: 5px;
                                                    }
                                                    QSlider::handle:horizontal {
                                                        background-color: rgb(195, 155, 255);
                                                        border: none;
                                                        height: 10px;
                                                        width: 10px;
                                                        margin: 0px;
                                                        border-radius: 5px;
                                                    }
                                                    QSlider::handle:horizontal:hover {
                                                        background-color: rgb(195, 155, 255);
                                                    }
                                                    """)
            self.ui.comboBox_2.setStyleSheet("""
                                                QComboBox{
                                                    background-color: rgb(98, 114, 164);
                                                    border-radius: 5px;
                                                    border: 2px solid rgb(143, 167, 240);
                                                    padding: 5px;
                                                    padding-left: 10px;
                                                    color: rgb(255, 255, 255);
                                                }
                                                QComboBox:hover{
                                                    border: 2px solid rgb(168, 190, 252);
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
                                                    color: rgb(255, 255, 255);	
                                                    background-color: rgb(98, 114, 164);
                                                    border: 2px solid rgb(143, 167, 240);
                                                    border-radius:5px;
                                                    padding: 10px;
                                                    selection-background-color: rgb(195, 155, 255);
                                                }
                                                
                                                """)
            self.ui.radioButton.setStyleSheet("""QRadioButton{color:rgb(2, 2, 2)}
QRadioButton::indicator {
    border: 3px solid rgb(143, 167, 240);
	width: 15px;
	height: 15px;
	border-radius: 10px;
    background: rgb(98, 114, 164);
}
QRadioButton::indicator:hover {
    border: 3px solid rgb(172, 187, 255);
}
QRadioButton::indicator:checked {
    background: 3px solid rgb(143, 167, 240);
	border: 3px solid rgb(98, 114, 164);	
}""")
            self.ui.checkBox.setStyleSheet("""QCheckBox{color: rgb(2, 2, 2);}
                                                QCheckBox::indicator {
                                                    border: 2px solid rgb(143, 167, 240);
                                                    width: 15px;
                                                    height: 15px;
                                                    border-radius: 9px;
                                                    background: rgb(41, 42, 65);
                                                }
                                                QCheckBox::indicator:hover {
                                                    border: 2px solid rgb(168, 190, 252);
                                                }
                                                QCheckBox::indicator:checked {
                                                    background:rgb(41, 42, 65);
                                                    border: 2px solid rgb(143, 167, 240);
                                                    background-image: url(:/icons/cil-check-alt.png);
                                                }
                                                """)
            self.ui.verticalSlider.setStyleSheet("""QSlider::groove:horizontal{
                                                    background-color: rgb(41, 42, 65);
                                                    border: none;
                                                    margin: 0px;
                                                    border-radius: 5px;
                                                }
                                                QSlider::handle:horizontal {
                                                    background-color: rgb(195, 155, 255);
                                                    border: none;
                                                    height: 10px;
                                                    width: 10px;
                                                    margin: 0px;
                                                    border-radius: 5px;
                                                }
                                                QSlider::handle:horizontal:hover {
                                                    background-color: rgb(195, 155, 255);
                                                }
""")
            self.ui.verticalSlider_2.setStyleSheet("""QSlider::groove:vertical{
	
	background-color: rgb(98, 114, 164);
    border: none;
 	height: 120px;
    margin: 0px;
	border-radius: 5px;
}
QSlider::handle:vertical {
	background-color: rgb(195, 155, 255);
    border: none;
    height: 25px;
    width: 10px;
    margin: 0px;
	border-radius: 5px;
}
QSlider::handle:horizontal:hover {
    background-color: rgb(195, 155, 255);
}""")
            self.ui.horizontalSlider_2.setStyleSheet("""QSlider::groove:horizontal{
                                                                    background-color: rgb(98, 114, 164);
                                                                    border: none;
                                                                    margin: 0px;
                                                                    border-radius: 5px;
                                                                }
                                                                QSlider::handle:horizontal {
                                                                    background-color: rgb(195, 155, 255);
                                                                    border: none;
                                                                    height: 10px;
                                                                    width: 25px;
                                                                    margin: 0px;
                                                                    border-radius: 5px;
                                                                }
                                                                QSlider::handle:horizontal:hover {
                                                                    background-color: rgb(195, 155, 255);
                                                                }
                                                                """)
            self.ui.plainTextEdit.setStyleSheet("""                  
            QPlainTextEdit{
            background-color: rgb(98, 114, 164);
            border-radius:8px;}
            
            QPlainTextEdit:hover{
            border: 2px solid rgb(143, 167, 240);}
            
            QPlainTextEdit:focus{
            color: rgb(255, 255, 255);
            border: 2px solid rgb(174, 189, 240);}""")
            self.ui.commandLinkButton.setStyleSheet("""QCommandLinkButton{
color: rgb(195, 155, 255);
border:none;
border-radius:7px;
border: 2px solid rgb(98, 114, 164);}

QCommandLinkButton:hover{
color: rgb(195, 155, 255);
border:none;
border-radius:7px;
border: 2px solid rgb(143, 167, 240)}

QCommandLinkButton:pressed{
color: rgb(195, 155, 255);
border:none;
border-radius:7px;

}
""")
            self.ui.lineEdit.setStyleSheet("""QLineEdit{
            
	font: 14pt "Segoe UI";
    color: rgb(255, 255, 255);
	background-color: rgb(98, 114, 164);
	border-color:rgb(41, 42, 65);
	border-radius:8px
}

QLineEdit:hover{
	background-color: rgb(98, 114, 164);
	border-color:rgb(41, 42, 65);
	border: 2px solid rgb(143, 167, 240);
	border-radius:8px
}
QLineEdit:focus {
	background-color: rgb(98, 114, 164);
	border-color:rgb(41, 42, 65);
	border: 2px solid rgb(174, 189, 240);
	border-radius:8px
}""")
            self.ui.OpenFolder.setStyleSheet("""QPushButton{
	border-radius:8px;
	color: rgb(255, 255, 255);
	background-color: rgb(80, 105, 150);
}

QPushButton:hover{
	border-radius:8px;
	color: rgb(255, 255, 255);
	background-color: rgb(80, 105, 150);
	border: 2px solid rgb(143, 167, 240);
}
QPushButton:pressed{
	border-radius:8px;
	color: rgb(255, 255, 255);
	background-color: rgb(98, 114, 164);
	padding-top: 3px;
}""")
            self.ui.verticalSlider.setStyleSheet("""QSlider::groove:vertical{
                                                        background-color: rgb(98, 114, 164);
                                                        border: none;
                                                        margin: 0px;
                                                        border-radius: 5px;
                                                    }
                                                    QSlider:::handle:vertical  {
                                                        background-color: rgb(195, 155, 255);
                                                        border: none;
                                                        height: 10px;
                                                        width: 10px;
                                                        margin: 0px;
                                                        border-radius: 5px;
                                                    }
                                                    QSlider::handle:horizontal:hover {
                                                        background-color: rgb(195, 155, 255);
                                                    }""")
            self.ui.tableWidget_2.setStyleSheet("""QTableWidget {	
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
                                                    }
                                                    """)
            self.ui.settings_menu_2.setStyleSheet("background-color: rgb(98, 114, 164);")
            self.ui.frame_central.setStyleSheet("background-color: rgb(255, 255, 255);")

            with open("Tema.txt", "w") as CORTEMA:
                CORTEMA.write("2º  Light")

        if (tema == "3º  Dark"):
            self.ui.btns.setStyleSheet("""QToolButton{
                                                    color: #c3ccdf;
                                                    border: none;
                                                    border-radius:3px;
                                                    }
            
                                                    QToolButton:hover {
                                                    background-color: rgb(40, 44, 52);
                                                    border: none;
                                                    border-radius:3px;
                                                    }
            
                                                    QToolButton:pressed {
                                                    background-color: rgb(96, 100, 152);
                                                    border: none;
                                                    border-radius:3px;        
                                                    }
                                                    """)  #
            self.ui.dock_widget.setStyleSheet("background-color: rgb(33, 37, 43);")
            self.ui.Menu_lateral.setStyleSheet("background-color: rgb(33, 37, 43);")  # add o style do tootip
            self.ui.decricao.setStyleSheet("background-color: rgb(33, 37, 43);")
            self.ui.dock_widget_2.setStyleSheet("background-color: rgb(33, 37, 43);")
            self.ui.logo1.setStyleSheet("""border-radius:10px;
                                                       border-radius:10px;
                                                       background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0,
                                                       stop:0.275992 rgba(248, 118, 205, 255),
                                                       stop:0.286836 rgb(33, 37, 43),
                                                       stop:0.457627 rgb(33, 37, 43),
                                                       stop:0.468927 rgba(248, 118, 205, 255));""")
            self.ui.logo2.setStyleSheet("""background-color: rgb(33, 37, 43);
                                                        border-radius:17px;""")
            self.ui.logo3.setStyleSheet("""border-radius: 14px;
                                                       background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0
                                                       stop:0.0568182 rgba(248, 118, 205, 255),
                                                       stop:0.829545 rgba(248, 118, 205, 255),
                                                       stop:0.840909 rgb(33, 37, 43),
                                                       stop:0.982955 rgb(33, 37, 43));""")
            self.ui.logo4.setStyleSheet("""background-color: rgb(33, 37, 43);
                                                       border-radius:12px;;""")
            self.ui.logo5.setStyleSheet("""border-radius:8px;
                                                       background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0,
                                                       stop:0.0795455 rgba(248, 118, 205, 255),
                                                       stop:0.448864 rgb(33, 37, 43),
                                                       stop:0.676136 rgb(33, 37, 43),
                                                       stop:0.6875 rgba(248, 118, 205, 255));""")
            self.ui.logo6.setStyleSheet("""border-Radius:6px;
                                                       background-color: rgb(33, 37, 43);""")
            self.ui.logo7.setStyleSheet("""background-color: rgb(33, 37, 43);
                                                       border-radius:1px;""")

            self.ui.frame_btn_bottom.setStyleSheet("""QPushButton{
                                                                 color: #c3ccdf;
                                                                 padding-left: 18px;
                                                                 text-align: left;
                                                                 border: none;
                                                                 }
            
                                                                 QPushButton:hover {
                                                                 background-color: rgb(40, 44, 52);
                                                                 }
            
                                                                 QPushButton:pressed {
                                                                 background-color: rgb(186, 135, 245);
                                                                 }""")
            self.ui.frame_btn_top.setStyleSheet("""QPushButton{
                                                                 color: #c3ccdf;
                                                                 padding-left: 18px;
                                                                 text-align: left;
                                                                 border: none;
                                                                 }
            
                                                                 QPushButton:hover {
                                                                 background-color: rgb(40, 44, 52);
                                                                 }
            
                                                                 QPushButton:pressed {
                                                                 background-color: rgb(186, 135, 245);
                                                                 }""")

            self.ui.statusBar.setStyleSheet("background-color: rgb(41, 44, 53);")
            self.ui.settings_menu.setStyleSheet("background-color: rgb(44, 49, 58);")
            self.ui.label_20.setStyleSheet("color: rgb(255, 255, 255)")
            self.ui.selectTheme.setStyleSheet("""
                                                            QComboBox{
                                                                background-color: rgb(40, 44, 52);
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
                                                                background-color: rgb(40, 44, 52);
                                                                padding: 10px;
                                                                selection-background-color: rgb(195, 155, 255);
                                                                border:2px solid  rgb(248, 118, 205);
                                                                border_top:none;
                                                                border-radius:5px;
                                                            }""")

            self.ui.horizontalSlider.setStyleSheet("""QSlider::groove:horizontal{
                                                                    background-color: rgb(52, 59, 72);
                                                                    border: none;
                                                                    margin: 0px;
                                                                    border-radius: 5px;
                                                                    }
                                                                    QSlider::handle:horizontal {
                                                                    background-color: rgb(195, 155, 255);
                                                                    border: none;
                                                                    height: 10px;
                                                                    width: 10px;
                                                                    margin: 0px;
                                                                    border-radius: 5px;
                                                                    }
                                                                    QSlider::handle:horizontal:hover {
                                                                    background-color: rgb(195, 155, 255);
                                                                    }
                                                                """)
            self.ui.comboBox_2.setStyleSheet("""
            QComboBox{
               background-color: rgb(33, 37, 43);
                border-radius: 5px;
                border: 2px solid rgb(41, 42, 65);
                padding: 5px;
                padding-left: 10px;
                color: rgb(255, 255, 255);
            }
            QComboBox:hover{
                border: 2px solid rgb(64, 71, 88);
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
                background-color: rgb(33, 37, 43);
                padding: 10px;
                selection-background-color: rgb(195, 155, 255);
            }
            
            """)
            self.ui.radioButton.setStyleSheet("""
            QRadioButton{color:rgb(255, 255, 255)}
            QRadioButton::indicator {
                border: 3px solid rgb(52, 59, 72);
                width: 15px;
                height: 15px;
                border-radius: 10px;
                background: rgb(41, 42, 65);
            }
            QRadioButton::indicator:hover {
                border: 3px solid rgb(73, 76, 116);
            }
            QRadioButton::indicator:checked {
                background: 3px solid rgb(73, 76, 116);
                border: 3px solid rgb(41, 42, 65)	
            }
            """)
            self.ui.checkBox.setStyleSheet("""QCheckBox{color: rgb(255, 255, 255);}
            
            QCheckBox::indicator {
                border: 3px solid rgb(52, 59, 72);
                width: 15px;
                height: 15px;
                border-radius: 10px;
                background: rgb(41, 42, 65);
            }
            QCheckBox::indicator:hover {
                border: 3px solid rgb(58, 66, 81);
            }
            QCheckBox::indicator:checked {
                background: 3px solid rgb(52, 59, 72);
                border: 3px solid rgb(52, 59, 72);	
                background-image: url(:/icons/cil-check-alt.png);
            }""")
            self.ui.verticalSlider.setStyleSheet(""" 
QSlider::groove:vertical{
	background-color: rgb(52, 59, 72);
    border: none;
 	height: 120px;
    margin: 0px;
	border-radius: 5px;
}
QSlider::handle:vertical {
	background-color: rgb(195, 155, 255);
    border: none;
    height: 10px;
    width: 10px;
    margin: 0px;
	border-radius: 5px;
}
QSlider::handle:horizontal:hover {
    background-color: rgb(195, 155, 255);
}""")
            self.ui.verticalSlider_2.setStyleSheet("""QSlider::groove:horizontal{
                background-color: rgb(41, 42, 65);
                border: none;
                height: 120px;
                margin: 0px;
                border-radius: 5px;

            }
            
            QSlider::handle:horizontalal {
                background-color: rgb(189, 147, 249);
                border: none;
                height: 25px;
                width: 10px;
                margin: 0px;
                border-radius: 5px;
            }
            QSlider::handle:verticall:hover {
                background-color: rgb(195, 155, 255);
            }""")
            self.ui.horizontalSlider_2.setStyleSheet("""
                                                    QSlider::groove:horizontal{   
                                                    background-color: rgb(52, 59, 72);
                                                    border: none;
                                                    margin: 0px;
                                                    border-radius: 5px;
                                                    }
                                                    QSlider::handle:horizontalal {
                                                    background-color: rgb(189, 147, 249);
                                                    border: none;
                                                    height: 0px;
                                                    width: 25px;
                                                    margin: 0px;
                                                    border-radius: 5px;
                                                    }
                                                    QSlider::handle:verticall:hover {
                                                    background-color: rgb(195, 155, 255);
                                                    }""")
            self.ui.plainTextEdit.setStyleSheet("""
            QPlainTextEdit{
            background-color: rgb(33, 37, 43);
            border-radius:8px;}
            
            QPlainTextEdit:hover{
            border: 2px solid rgb(64, 71, 88);}
            
            QPlainTextEdit:focus{
            color: rgb(255, 255, 255);
            border: 2px solid rgb(91, 101, 124)}
            """)
            self.ui.commandLinkButton.setStyleSheet("""QCommandLinkButton{
            color: rgb(195, 155, 255);
            border:none;
            border-radius:7px;
            border: 2px solid rgb(73, 76, 116);}
            
            QCommandLinkButton:hover{
            color: rgb(195, 155, 255);
            border:none;
            border-radius:7px;
            border: 2px solid rgb(116, 91, 153)}
            
            QCommandLinkButton:pressed{
            color: rgb(195, 155, 255);
            border:none;
            border-radius:7px;
            
            }
            
            
            
                        """)
            self.ui.lineEdit.setStyleSheet("""
                                            QLineEdit {
                                            color: rgb(255, 255, 255);
                                            background-color: rgb(33, 37, 43);
                                            border-radius: 8px;
                                            border: 2px solid rgb(33, 37, 43);
                                            padding-left: 10px;
                                            selection-color: rgb(255, 255, 255);
                                            selection-background-color: rgb(255, 121, 198);
                                            }
                                            QLineEdit:hover {
                                            border: 2px solid rgb(64, 71, 88);
                                            }
                                            QLineEdit:focus {
                                             color: rgb(255, 255, 255);
                                            border: 2px solid rgb(91, 101, 124);
                                            }
                                            """)
            self.ui.OpenFolder.setStyleSheet("""QPushButton{
                border-radius:8px;
                color: rgb(255, 255, 255);
                background-color: rgb(52, 59, 72);
            }
            
            QPushButton:hover{
                border-radius:8px;
                color: rgb(255, 255, 255);
                background-color: rgb(52, 59, 72);
                border: 2px solid rgb(80, 91, 111);;
            }
            QPushButton:pressed{
                border-radius:8px;
                color: rgb(255, 255, 255);
                background-color: rgb(52, 59, 72);
                padding-top: 3px;
            }""")

            self.ui.tableWidget_2.setStyleSheet("""QTableWidget {	
                                                                                color: rgb(255, 255, 255);
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
                                                                            }
                                                                            """)

            self.ui.stackedWidget.setStyleSheet("background-color: rgb(40, 44, 52);")
            self.ui.settings_menu_2.setStyleSheet("background-color: rgb(44, 49, 58);")
            self.ui.frame_central.setStyleSheet("background-color: rgb(40, 44, 52);")

            with open("Tema.txt", "w") as CORTEMA:
                CORTEMA.write("3º  Dark")

        if (tema == "4º  BlueGreen"):
            self.ui.btns.setStyleSheet("""
                                                           QToolButton{
                                                           color: #c3ccdf;
                                                           border: none;
                                                           border-radius:3px;
                                                           }
        
                                                           QToolButton:hover {
                                                           background-color: rgb(189, 147, 249);
                                                           border: none;
                                                           border-radius:3px;
                                                           }
        
                                                           QToolButton:pressed {
                                                           background-color: rgb(208, 161, 249);
                                                           border: none;
                                                           border-radius:3px;        
                                                           }
                                                           """)
            self.ui.dock_widget.setStyleSheet("""background-color: rgb(98, 114, 164);""")  # add o style do tootip
            self.ui.Menu_lateral.setStyleSheet("""background-color: rgb(98, 114, 164);""")
            self.ui.decricao.setStyleSheet("background-color: rgb(98, 114, 164);")
            self.ui.dock_widget_2.setStyleSheet("background-color: rgb(98, 114, 164);")
            self.ui.logo1.setStyleSheet("""border-radius:10px;
                                                                           background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0,
                                                                           stop:0.275992 rgba(248, 118, 205, 255),
                                                                           stop:0.286836 rgb(91, 105, 150),
                                                                           stop:0.457627 rgb(91, 105, 150),
                                                                           stop:0.468927 rgba(248, 118, 205, 255));""")
            self.ui.logo2.setStyleSheet("""background-color: rgb(98, 114, 164);
                                                                            border-radius:17px;""")
            self.ui.logo3.setStyleSheet("""border-radius: 14px;
                                                                            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0
                                                                            stop:0.0568182 rgba(248, 118, 205, 255),
                                                                            stop:0.829545 rgba(248, 118, 205, 255),
                                                                            stop:0.840909 rgb(91, 105, 150),
                                                                            stop:0.982955 rgb(91, 105, 150));""")
            self.ui.logo4.setStyleSheet("""background-color: rgb(91, 105, 150);
                                                                            border-radius:12px;""")
            self.ui.logo5.setStyleSheet("""border-radius:8px;
                                                                            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0,
                                                                            stop:0.0795455 rgba(248, 118, 205, 255),
                                                                            stop:0.448864 rgb(91, 105, 150),
                                                                            stop:0.676136 rgb(91, 105, 150),
                                                                            stop:0.6875 rgba(248, 118, 205, 255));""")
            self.ui.logo6.setStyleSheet("""border-Radius:6px;
                                                                            background-color: rgb(91, 105, 150);""")
            self.ui.logo7.setStyleSheet("""background-color: rgb(91, 105, 150);
                                                                            border-radius:1px;""")

            self.ui.frame_btn_bottom.setStyleSheet("""QPushButton{
                                                                        color: #c3ccdf;
                                                                        padding-left: 18px;
                                                                        text-align: left;
                                                                        border: none;
                                                                        }
        
                                                                        QPushButton:hover {
                                                                        background-color: rgb(86, 99, 136);
                                                                        }
        
                                                                        QPushButton:pressed {
                                                                        background-color: rgb(186, 135, 245);
                                                                        }""")
            self.ui.frame_btn_top.setStyleSheet("""QPushButton{
                                                                        color: #c3ccdf;
                                                                        padding-left: 18px;
                                                                        text-align: left;
                                                                        border: none;
                                                                        }
        
                                                                        QPushButton:hover {
                                                                        background-color: rgb(86, 99, 136);
                                                                        }
        
                                                                        QPushButton:pressed {
                                                                        background-color: rgb(186, 135, 245);
                                                                        }""")
            self.ui.statusBar.setStyleSheet("background-color: rgb(70, 82, 118);")
            self.ui.settings_menu.setStyleSheet("background-color: rgb(70, 82, 118);")
            self.ui.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.ui.label_20.setStyleSheet("color: rgb(255, 255, 255)")
            self.ui.selectTheme.setStyleSheet("""
                                                                   QComboBox{
                                                                       background-color: rgb(98, 114, 164);
                                                                       border-radius: 5px;
                                                                       border: 2px solid rgb(138, 161, 231);
                                                                       padding: 5px;
                                                                       padding-left: 10px;
                                                                       color: rgb(255, 255, 255);
                                                                   }
        
                                                                   QComboBox:hover{
                                                                       border: 2px solid rgb(178, 199, 255);
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
                                                                       color:rgb(255, 255, 255);	
                                                                       background-color: rgb(98, 114, 164);
                                                                       padding: 10px;
                                                                       selection-background-color: rgb(195, 155, 255);
                                                                       border:2px solid  rgb(138, 161, 231);
                                                                       border_top:none;
                                                                       border-radius:5px;
                                                                   }""")

            self.ui.horizontalSlider.setStyleSheet("""QSlider::groove:horizontal{
                                                                           background-color: rgb(98, 114, 164);
                                                                           border: none;
                                                                           margin: 0px;
                                                                           border-radius: 5px;
                                                                       }
                                                                       QSlider::handle:horizontal {
                                                                           background-color: rgb(195, 155, 255);
                                                                           border: none;
                                                                           height: 10px;
                                                                           width: 10px;
                                                                           margin: 0px;
                                                                           border-radius: 5px;
                                                                       }
                                                                       QSlider::handle:horizontal:hover {
                                                                           background-color: rgb(195, 155, 255);
                                                                       }
                                                                       """)
            self.ui.comboBox_2.setStyleSheet("""
                                                                   QComboBox{
                                                                       background-color: rgb(98, 114, 164);
                                                                       border-radius: 5px;
                                                                       border: 2px solid rgb(143, 167, 240);
                                                                       padding: 5px;
                                                                       padding-left: 10px;
                                                                       color: rgb(255, 255, 255);
                                                                   }
                                                                   QComboBox:hover{
                                                                       border: 2px solid rgb(168, 190, 252);
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
                                                                       color: rgb(255, 255, 255);	
                                                                       background-color: rgb(98, 114, 164);
                                                                       border: 2px solid rgb(143, 167, 240);
                                                                       border-radius:5px;
                                                                       padding: 10px;
                                                                       selection-background-color: rgb(195, 155, 255);
                                                                   }
        
                                                                   """)
            self.ui.radioButton.setStyleSheet("""QRadioButton{color:rgb(255, 255, 255)}
                   QRadioButton::indicator {
                       border: 3px solid rgb(143, 167, 240);
                    width: 15px;
                    height: 15px;
                    border-radius: 10px;
                       background: rgb(98, 114, 164);
                   }
                   QRadioButton::indicator:hover {
                       border: 3px solid rgb(172, 187, 255);
                   }
                   QRadioButton::indicator:checked {
                       background: 3px solid rgb(143, 167, 240);
                    border: 3px solid rgb(98, 114, 164);	
                   }""")
            self.ui.checkBox.setStyleSheet("""QCheckBox{color: rgb(255, 255, 255);}
                                                                   QCheckBox::indicator {
                                                                       border: 2px solid rgb(143, 167, 240);
                                                                       width: 15px;
                                                                       height: 15px;
                                                                       border-radius: 9px;
                                                                       background: rgb(41, 42, 65);
                                                                   }
                                                                   QCheckBox::indicator:hover {
                                                                       border: 2px solid rgb(168, 190, 252);
                                                                   }
                                                                   QCheckBox::indicator:checked {
                                                                       background:rgb(41, 42, 65);
                                                                       border: 2px solid rgb(143, 167, 240);
                                                                       background-image: url(:/icons/cil-check-alt.png);
                                                                   }
                                                                   """)
            self.ui.verticalSlider.setStyleSheet("""QSlider::groove:horizontal{
                                                                       background-color: rgb(41, 42, 65);
                                                                       border: none;
                                                                       margin: 0px;
                                                                       border-radius: 5px;
                                                                   }
                                                                   QSlider::handle:horizontal {
                                                                       background-color: rgb(195, 155, 255);
                                                                       border: none;
                                                                       height: 10px;
                                                                       width: 10px;
                                                                       margin: 0px;
                                                                       border-radius: 5px;
                                                                   }
                                                                   QSlider::handle:horizontal:hover {
                                                                       background-color: rgb(195, 155, 255);
                                                                   }
                   """)
            self.ui.plainTextEdit.setStyleSheet("""
                               
            QPlainTextEdit{
            background-color: rgb(98, 114, 164);
            border-radius:8px;}
            
            QPlainTextEdit:hover{
            border: 2px solid rgb(143, 167, 240);}
            
            QPlainTextEdit:focus{
            color: rgb(255, 255, 255);
            border: 2px solid rgb(174, 189, 240);}""")
            self.ui.commandLinkButton.setStyleSheet("""QCommandLinkButton{
                   color: rgb(195, 155, 255);
                   border:none;
                   border-radius:7px;
                   border: 2px solid rgb(98, 114, 164);}
        
                   QCommandLinkButton:hover{
                   color: rgb(195, 155, 255);
                   border:none;
                   border-radius:7px;
                   border: 2px solid rgb(143, 167, 240)}
        
                   QCommandLinkButton:pressed{
                   color: rgb(195, 155, 255);
                   border:none;
                   border-radius:7px;
        
                   }
                   """)
            self.ui.lineEdit.setStyleSheet("""QLineEdit{
        
                    font: 14pt "Segoe UI";
                       color: rgb(255, 255, 255);
                    background-color: rgb(98, 114, 164);
                    border-color:rgb(41, 42, 65);
                    border-radius:8px
                   }
        
                   QLineEdit:hover{
                    background-color: rgb(98, 114, 164);
                    border-color:rgb(41, 42, 65);
                    border: 2px solid rgb(143, 167, 240);
                    border-radius:8px
                   }
                   QLineEdit:focus {
                    background-color: rgb(98, 114, 164);
                    border-color:rgb(41, 42, 65);
                    border: 2px solid rgb(174, 189, 240);
                    border-radius:8px
                   }""")
            self.ui.OpenFolder.setStyleSheet("""QPushButton{
                    border-radius:8px;
                    color: rgb(255, 255, 255);
                    background-color: rgb(80, 105, 150);
                   }
        
                   QPushButton:hover{
                    border-radius:8px;
                    color: rgb(255, 255, 255);
                    background-color: rgb(80, 105, 150);
                    border: 2px solid rgb(143, 167, 240);
                   }
                   QPushButton:pressed{
                    border-radius:8px;
                    color: rgb(255, 255, 255);
                    background-color: rgb(98, 114, 164);
                    padding-top: 3px;
                   }""")
            self.ui.verticalSlider.setStyleSheet("""QSlider::groove:vertical{
                                                                           background-color: rgb(98, 114, 164);
                                                                           border: none;
                                                                           margin: 0px;
                                                                           border-radius: 5px;
                                                                       }
                                                                       QSlider:::handle:vertical  {
                                                                           background-color: rgb(195, 155, 255);
                                                                           border: none;
                                                                           height: 10px;
                                                                           width: 10px;
                                                                           margin: 0px;
                                                                           border-radius: 5px;
                                                                       }
                                                                       QSlider::handle:horizontal:hover {
                                                                           background-color: rgb(195, 155, 255);
                                                                       }""")
            self.ui.tableWidget_2.setStyleSheet("""QTableWidget {	
                                                                           color: rgb(255, 255, 255);
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
                                                                       }
                                                                       """)
            self.ui.verticalSlider_2.setStyleSheet("""
                                                                QSlider::groove:vertical{
                                                                background-color: rgb(98, 114, 164);
                                                                border: none;
                                                                height: 120px;
                                                                margin: 0px;
                                                                border-radius: 5px;
                                                                }
                                                                QSlider::handle:vertical {
                                                                background-color: rgb(195, 155, 255);
                                                                border: none;
                                                                height: 25px;
                                                                width: 10px;
                                                                margin: 0px;
                                                                border-radius: 5px;
                                                                }
                                                                QSlider::handle:horizontal:hover {
                                                                background-color: rgb(195, 155, 255);
                                                                }""")
            self.ui.horizontalSlider_2.setStyleSheet("""
                                                                    QSlider::groove:horizontal{
                                                                     background-color: rgb(98, 114, 164);
                                                                    border: none;
                                                                    margin: 0px;
                                                                    border-radius: 5px;
                                                                    }

                                                                    QSlider::handle:horizontalal {
                                                                    background-color: rgb(189, 147, 249);
                                                                    border: none;
                                                                    height: 0px;
                                                                    width: 25px;
                                                                    margin: 0px;
                                                                    border-radius: 5px;
                                                                    }
                                                                    QSlider::handle:verticall:hover {
                                                                    background-color: rgb(195, 155, 255);
                                                                    }""")

            self.ui.stackedWidget.setStyleSheet("background-color: rgb(120, 139, 180);")
            self.ui.settings_menu_2.setStyleSheet("background-color: rgb(98, 114, 164);")
            self.ui.frame_central.setStyleSheet("background-color: rgb(120, 139, 180);")

            with open("Tema.txt", "w") as CORTEMA:
                CORTEMA.write("4º  BlueGreen")

    def returnStatu(self):
        return GLOBAL_STATE

    # esta funcao vai redimencionar o tamnho dos grips para queos grips
    # estejam sempre no mesmo tamnho do tem MainWindow
    def resizeGrips(self):
        self.left.setGeometry(0, 10, 10, self.height())
        self.right.setGeometry(self.width() - 10, 10, 10, self.height())
        self.top.setGeometry(0, 0, self.width(), 10)
        self.bottom.setGeometry(0, self.height() - 10, self.width(), 10)

    # esta funcao faz alguma coisa quando redimencionares o a tua janela
    def resizeEvent(self, event):
        self.resizeGrips()

    def openfile(self):
        global openArQ

        if not openArQ:
            openAr = QFileDialog.getOpenFileName(parent=self, caption=self.tr('Open File'),
                                                 filter=self.tr('Text file (*.txt)'))

            if not openAr[0] == '':
                with open(openAr[0], 'r') as file:
                    self.ui.plainTextEdit.setPlainText(file.read())

class StyleLocal:
    btnPressed = """QPushButton{
                                    color: #c3ccdf;
                                    padding-left: 18px;
                                    text-align: left;
                                    border: none;
                                    border-left: 3px solid rgb(248, 118, 205)
                                    }"""
    btnNormal = """ QPushButton{
                        color: #c3ccdf;
                        padding-left: 18px;
                        text-align: left;
                        border: none;
                        }"""

    QtoolRosa = """QToolButton{
                               color: #c3ccdf;
                               background-color: ;
                               background-color: rgb(254, 121, 199);
                               border: none;
                               border-radius:3px;
                               }

                               QToolButton:hover {
                                background-color: rgb(254, 121, 199);
                               border: none;
                               border-radius:3px;
                               }

                               QToolButton:pressed {
                                background-color: rgb(254, 121, 199);
                               border: none;
                               border-radius:3px;}"""
    QtoolSinza = """QToolButton{
                                color: #c3ccdf;
                                border: none;
                                border-radius:3px;
                                }

                                QToolButton:hover {
                                background-color: rgb(67, 70, 107);
                                border: none;
                                border-radius:3px;
                                }

                                QToolButton:pressed {
                                background-color: rgb(96, 100, 152);
                                border: none;
                                border-radius:3px;}"""
    labelZero = """QLabel{color: rgba(98, 114, 164, 0)}
        """
    ZeroBtn = """QPushButton{
                        background-color: rgba(225, 107, 178, 0);
                        border-radius:10px;

                        }
                        QPushButton:hover{
                        background-color: rgba(206, 98, 163, 255);
                        border-radius:10px;}


                        QPushButton:pressed{
                        background-color: rgba(254, 121, 199, 255);
                        border-radius:10px;

                        }"""
    LEzero = """QLineEdit{
                            background-color: rgba(98, 114, 164, 0);
                            font: 10pt "MS Shell Dlg 2";
                            border-radius: 10px;
                            border	:	2px solid    rgba(98, 114, 164, 0);
                            }
                            QLineEdit:hover{
                            border	:	3px solid   rgba(123, 61, 184, 255)
                            }
                            QLineEdit:focus{
                            border	:	3px solid  rgba(171, 85, 255, 0)
                            }"""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginScreen()
    sys.exit(app.exec())
