# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arquivoZUdJyw.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 460)
        font = QFont()
        font.setFamilies([u"NimbusSanL"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: #D9D9D9;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 20, 800, 41))
        self.label.setMaximumSize(QSize(800, 100))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: #007A39; color: white;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 80, 761, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.button_model_a = QPushButton(self.horizontalLayoutWidget)
        self.button_model_a.setObjectName(u"button_model_a")
        self.button_model_a.setMaximumSize(QSize(400, 75))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.button_model_a.setFont(font2)
        self.button_model_a.setStyleSheet(u"background-color: #008000; color: white;")

        self.horizontalLayout.addWidget(self.button_model_a)

        self.button_model_b = QPushButton(self.horizontalLayoutWidget)
        self.button_model_b.setObjectName(u"button_model_b")
        self.button_model_b.setMaximumSize(QSize(400, 75))
        self.button_model_b.setFont(font2)
        self.button_model_b.setStyleSheet(u"background-color: #008000; color: white;")

        self.horizontalLayout.addWidget(self.button_model_b)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(20, 200, 761, 80))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.button_model_c = QPushButton(self.horizontalLayoutWidget_2)
        self.button_model_c.setObjectName(u"button_model_c")
        self.button_model_c.setMaximumSize(QSize(400, 75))
        self.button_model_c.setFont(font2)
        self.button_model_c.setStyleSheet(u"background-color: #008000; color: white;")

        self.horizontalLayout_2.addWidget(self.button_model_c)

        self.button_model_d = QPushButton(self.horizontalLayoutWidget_2)
        self.button_model_d.setObjectName(u"button_model_d")
        self.button_model_d.setMaximumSize(QSize(400, 75))
        self.button_model_d.setFont(font2)
        self.button_model_d.setStyleSheet(u"background-color: #008000; color: white;")

        self.horizontalLayout_2.addWidget(self.button_model_d)

        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(20, 330, 761, 80))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.button_model_e = QPushButton(self.horizontalLayoutWidget_3)
        self.button_model_e.setObjectName(u"button_model_e")
        self.button_model_e.setMaximumSize(QSize(400, 75))
        self.button_model_e.setFont(font2)
        self.button_model_e.setStyleSheet(u"background-color: #008000; color: white;")

        self.horizontalLayout_3.addWidget(self.button_model_e)

        self.button_model_f = QPushButton(self.horizontalLayoutWidget_3)
        self.button_model_f.setObjectName(u"button_model_f")
        self.button_model_f.setMaximumSize(QSize(400, 75))
        self.button_model_f.setFont(font2)
        self.button_model_f.setStyleSheet(u"background-color: #008000; color: white;")

        self.horizontalLayout_3.addWidget(self.button_model_f)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 121, 61))
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"background-color: #00A336; color: white; border: 1px solid grey;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ESCOLHA O MODELO SWITCH PARA O TESTE", None))
        self.button_model_a.setText(QCoreApplication.translate("MainWindow", u"Toggle Switch", None))
        self.button_model_b.setText(QCoreApplication.translate("MainWindow", u"Lever Switch", None))
        self.button_model_c.setText(QCoreApplication.translate("MainWindow", u"Key Switch", None))
        self.button_model_d.setText(QCoreApplication.translate("MainWindow", u"Push Button Switch", None))
        self.button_model_e.setText(QCoreApplication.translate("MainWindow", u"Dual In-line Package Switch", None))
        self.button_model_f.setText(QCoreApplication.translate("MainWindow", u"Reed Switch", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"INTELBRAS", None))
    # retranslateUi

