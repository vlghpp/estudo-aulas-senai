# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainojeggD.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(826, 600)
        MainWindow.setStyleSheet(u"background-color: lightgrey;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_error_counter = QLabel(self.centralwidget)
        self.label_error_counter.setObjectName(u"label_error_counter")
        self.label_error_counter.setGeometry(QRect(700, 170, 81, 51))
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        self.label_error_counter.setFont(font)
        self.label_error_counter.setStyleSheet(u"color:rgb(224, 27, 36);\n"
"font: 17pt \"Ubuntu\";")
        self.label_error_counter.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_of_errors = QLabel(self.centralwidget)
        self.label_of_errors.setObjectName(u"label_of_errors")
        self.label_of_errors.setGeometry(QRect(550, 180, 171, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_of_errors.setFont(font1)
        self.label_of_errors.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_turn_off_buzzer = QPushButton(self.centralwidget)
        self.button_turn_off_buzzer.setObjectName(u"button_turn_off_buzzer")
        self.button_turn_off_buzzer.setGeometry(QRect(570, 330, 181, 71))
        self.button_turn_off_buzzer.setStyleSheet(u"background-color: rgb(177, 11, 11);\n"
"color:rgba(255, 255, 255,0.75);\n"
"font: 700 13pt \"Ubuntu\";")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(570, 240, 181, 71))
        self.pushButton.setStyleSheet(u"background-color:#00C040;\n"
" color:white;\n"
"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-10, -5, 841, 61))
        font2 = QFont()
        font2.setPointSize(18)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"background-color:#008000;\n"
" color: white; ")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 30, 131, 51))
        font3 = QFont()
        font3.setFamilies([u"HoloLens MDL2 Assets"])
        font3.setPointSize(14)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"background-color: #00FF80; color:white;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 100, 551, 401))
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"background-color: #FFF; color:black;")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 826, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_error_counter.setText(QCoreApplication.translate("MainWindow", u"0/5", None))
        self.label_of_errors.setText(QCoreApplication.translate("MainWindow", u"Contador de erros:", None))
        self.button_turn_off_buzzer.setText(QCoreApplication.translate("MainWindow", u"Desligar Buzzer", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Alterar toler\u00e2ncia de erros", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CHECAGEM AUTOMATIZADA - ESTAMPA", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"INTELBRAS", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"VIDEO", None))
    # retranslateUi

