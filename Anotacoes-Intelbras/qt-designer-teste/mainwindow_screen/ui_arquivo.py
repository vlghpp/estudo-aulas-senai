# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arquivo.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(932, 588)
        MainWindow.setStyleSheet(u"background-color: lightgrey;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"HoloLens MDL2 Assets"])
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: #FFF; color:black;")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 8, 2)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"background-color:#5d82e9; color: white;")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 10, 0, 1, 3)

        self.button_change_tolerance = QPushButton(self.centralwidget)
        self.button_change_tolerance.setObjectName(u"button_change_tolerance")
        font2 = QFont()
        font2.setFamilies([u"HoloLens MDL2 Assets"])
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(False)
        self.button_change_tolerance.setFont(font2)
        self.button_change_tolerance.setStyleSheet(u"background-color:#00C040; color:white; height: 75px; font-weight: bold; ")

        self.gridLayout.addWidget(self.button_change_tolerance, 5, 2, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color:#008000; color: white;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 2, 3)

        self.button_turn_off_buzzer = QPushButton(self.centralwidget)
        self.button_turn_off_buzzer.setObjectName(u"button_turn_off_buzzer")
        font3 = QFont()
        font3.setFamilies([u"HoloLens MDL2 Assets"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.button_turn_off_buzzer.setFont(font3)
        self.button_turn_off_buzzer.setStyleSheet(u"background-color: rgb(177, 11, 11); color: white; font-weight: bold; height: 75px;")

        self.gridLayout.addWidget(self.button_turn_off_buzzer, 7, 2, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_of_errors = QLabel(self.widget)
        self.label_of_errors.setObjectName(u"label_of_errors")
        font4 = QFont()
        font4.setPointSize(12)
        self.label_of_errors.setFont(font4)
        self.label_of_errors.setStyleSheet(u"background-color: white")
        self.label_of_errors.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_of_errors)

        self.label_error_counter = QLabel(self.widget)
        self.label_error_counter.setObjectName(u"label_error_counter")
        font5 = QFont()
        font5.setFamilies([u"Ubuntu"])
        font5.setPointSize(17)
        font5.setBold(False)
        font5.setItalic(False)
        self.label_error_counter.setFont(font5)
        self.label_error_counter.setStyleSheet(u"background-color: white;color:rgb(224, 27, 36); font: 17pt \"Ubuntu\";")
        self.label_error_counter.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_error_counter)


        self.gridLayout.addWidget(self.widget, 2, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"VIDEO", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u" CHECAGEM DO PRODUTO -  XXXXXXXX", None))
        self.button_change_tolerance.setText(QCoreApplication.translate("MainWindow", u"Alterar toler\u00e2ncia de erros", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CHECAGEM AUTOMATIZADA - ESTAMPA", None))
        self.button_turn_off_buzzer.setText(QCoreApplication.translate("MainWindow", u"Desligar Buzzer", None))
        self.label_of_errors.setText(QCoreApplication.translate("MainWindow", u"Contador \n"
" de erros:", None))
        self.label_error_counter.setText(QCoreApplication.translate("MainWindow", u"0/5", None))
    # retranslateUi

