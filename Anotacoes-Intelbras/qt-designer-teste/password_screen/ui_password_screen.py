# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'screen.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_PasswordScreen(object):
    def setupUi(self, PasswordScreen):
        if not PasswordScreen.objectName():
            PasswordScreen.setObjectName(u"PasswordScreen")
        PasswordScreen.resize(582, 336)
        PasswordScreen.setStyleSheet(u"background-color: #008000;")
        self.horizontalLayout = QHBoxLayout(PasswordScreen)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(PasswordScreen)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(371, 51))
        font = QFont()
        font.setFamilies([u"Lucida Sans Unicode"])
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font-weight: bold; color: white;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.plaintext_password = QTextEdit(self.widget_3)
        self.plaintext_password.setObjectName(u"plaintext_password")
        self.plaintext_password.setMinimumSize(QSize(411, 61))
        self.plaintext_password.setMaximumSize(QSize(411, 61))
        self.plaintext_password.setStyleSheet(u"background-color: white;")

        self.horizontalLayout_3.addWidget(self.plaintext_password)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.button_insert_password = QPushButton(self.widget_4)
        self.button_insert_password.setObjectName(u"button_insert_password")
        self.button_insert_password.setMinimumSize(QSize(89, 25))
        self.button_insert_password.setMaximumSize(QSize(89, 25))
        self.button_insert_password.setStyleSheet(u"background-color: #98FB98;")

        self.horizontalLayout_4.addWidget(self.button_insert_password)


        self.verticalLayout.addWidget(self.widget_4)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(PasswordScreen)

        QMetaObject.connectSlotsByName(PasswordScreen)
    # setupUi

    def retranslateUi(self, PasswordScreen):
        PasswordScreen.setWindowTitle(QCoreApplication.translate("PasswordScreen", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("PasswordScreen", u"DIGITE A SENHA DE ALTERA\u00c7\u00c3O", None))
        self.button_insert_password.setText(QCoreApplication.translate("PasswordScreen", u"OK", None))
    # retranslateUi

