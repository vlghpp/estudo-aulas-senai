# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arquivofsBusO.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 480)
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
        font1.setFamilies([u"Helvetica Now Var Micro Medium"])
        font1.setPointSize(16)
        font1.setBold(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: #007A39; color: white;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 121, 61))
        font2 = QFont()
        font2.setFamilies([u"Helvetica Now Var Text Black"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"background-color: #00A336; color: white; border: 1px solid grey;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(0, 60, 801, 401))
        self.verticalLayout = QVBoxLayout(self.widget_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.widget_4)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_model_a = QPushButton(self.widget)
        self.button_model_a.setObjectName(u"button_model_a")
        self.button_model_a.setMaximumSize(QSize(400, 75))
        font3 = QFont()
        font3.setFamilies([u"Helvetica Now Var Micro Medium"])
        font3.setPointSize(12)
        font3.setBold(False)
        self.button_model_a.setFont(font3)
        self.button_model_a.setStyleSheet(u"background-color: #008000; color: white;")

        self.horizontalLayout.addWidget(self.button_model_a)

        self.button_model_b = QPushButton(self.widget)
        self.button_model_b.setObjectName(u"button_model_b")
        self.button_model_b.setMaximumSize(QSize(400, 75))
        self.button_model_b.setFont(font3)
        self.button_model_b.setStyleSheet(u"background-color: #008000; color: white;")

        self.horizontalLayout.addWidget(self.button_model_b)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.widget)

        self.widget_3 = QWidget(self.widget_4)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.button_model_c = QPushButton(self.widget_3)
        self.button_model_c.setObjectName(u"button_model_c")
        self.button_model_c.setMaximumSize(QSize(400, 75))
        self.button_model_c.setFont(font3)
        self.button_model_c.setStyleSheet(u"background-color: #008000; color: white;")

        self.horizontalLayout_2.addWidget(self.button_model_c)

        self.button_model_d = QPushButton(self.widget_3)
        self.button_model_d.setObjectName(u"button_model_d")
        self.button_model_d.setMaximumSize(QSize(400, 75))
        font4 = QFont()
        font4.setFamilies([u"Helvetica Now Var Text Medium"])
        font4.setPointSize(12)
        font4.setBold(False)
        self.button_model_d.setFont(font4)
        self.button_model_d.setStyleSheet(u"background-color: #008000; color: white;")

        self.horizontalLayout_2.addWidget(self.button_model_d)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.widget_4)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.button_model_e = QPushButton(self.widget_2)
        self.button_model_e.setObjectName(u"button_model_e")
        self.button_model_e.setMaximumSize(QSize(400, 75))
        self.button_model_e.setFont(font4)
        self.button_model_e.setStyleSheet(u"background-color: #008000; color: white;")

        self.horizontalLayout_3.addWidget(self.button_model_e)

        self.button_model_f = QPushButton(self.widget_2)
        self.button_model_f.setObjectName(u"button_model_f")
        self.button_model_f.setMaximumSize(QSize(400, 75))
        self.button_model_f.setFont(font3)
        self.button_model_f.setStyleSheet(u"background-color: #008000; color: white;")

        self.horizontalLayout_3.addWidget(self.button_model_f)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.widget_4.raise_()
        self.label_2.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ESCOLHA O MODELO SWITCH PARA O TESTE", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"INTELBRAS", None))
        self.button_model_a.setText(QCoreApplication.translate("MainWindow", u"Toggle Switch", None))
        self.button_model_b.setText(QCoreApplication.translate("MainWindow", u"Lever Switch", None))
        self.button_model_c.setText(QCoreApplication.translate("MainWindow", u"Key Switch", None))
        self.button_model_d.setText(QCoreApplication.translate("MainWindow", u"Push Button Switch", None))
        self.button_model_e.setText(QCoreApplication.translate("MainWindow", u"Dual In-line Package Switch", None))
        self.button_model_f.setText(QCoreApplication.translate("MainWindow", u"Reed Switch", None))
    # retranslateUi

