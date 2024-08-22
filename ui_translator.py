# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designuRVScf.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(748, 553)
        MainWindow.setWindowTitle(u"Translator")
        MainWindow.setStyleSheet("background-color: seagreen;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.appTitle = QLabel(self.centralwidget)
        self.appTitle.setObjectName(u"appTitle")
        self.appTitle.setGeometry(QRect(290, 20, 133, 33))
        self.appTitle.setStyleSheet(u"font-size: 30px;\n"
"font-family: Arial, Verdana, sans-serif;\n"
"color: lime;\n"
"")
        self.tobetranslated_lang = QComboBox(self.centralwidget)
        self.tobetranslated_lang.setObjectName(u"tobetranslated_lang")
        self.tobetranslated_lang.setGeometry(QRect(10, 110, 270, 31))
        self.tobetranslated_lang.addItem(u"auto")
        self.tobetranslated_lang.setStyleSheet(u"background-color: royalblue;\n"
"color: yellow;\n"
"\n"
"border: none;\n"
"outline: none;\n"
"border-radius: 15px;")
        self.to_arrow = QLabel(self.centralwidget)
        self.to_arrow.setObjectName(u"to_arrow")
        self.to_arrow.setGeometry(QRect(350, 90, 43, 67))
        self.to_arrow.setStyleSheet(u"font-size: 50px;\n"
"font-weight: bold;\n"
"color: yellow;\n"
"")
        self.translated_text = QTextEdit(self.centralwidget)
        self.translated_text.setObjectName(u"textEdit")
        self.translated_text.setGeometry(QRect(450, 170, 281, 251))
        self.translated_text.setStyleSheet(u"background-color: firebrick;\n"
"color: lightgreen;")
        self.translated_text.setReadOnly(True)
        self.translate_lang = QComboBox(self.centralwidget)
        self.translate_lang.setObjectName(u"translate_lang")
        self.translate_lang.setGeometry(QRect(491, 110, 171, 31))
        self.translate_lang.setStyleSheet(u"background-color: royalblue;\n"
"color: yellow;\n"
"\n"
"border: none; outline: none; border-radius: 15px;")
        self.translate_btn = QPushButton(self.centralwidget)
        self.translate_btn.setObjectName(u"translate_btn")
        self.translate_btn.setGeometry(QRect(324, 280, 91, 31))
        self.translate_btn.setStyleSheet(u"background-color: dodgerblue;\n"
"color: yellow;\n"
"\n"
"border: none; outline: none; border-radius: 15%;")
        self.to_be_translated = QTextEdit(self.centralwidget)
        self.to_be_translated.setObjectName(u"to_be_translated")
        self.to_be_translated.setGeometry(QRect(10, 170, 281, 251))
        self.to_be_translated.setStyleSheet(u"background-color: firebrick;\n"
"color: lightgreen;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.appTitle.setText(QCoreApplication.translate("MainWindow", u"Translator", None))
        self.tobetranslated_lang.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter the language of the text to be translated", None))
        self.to_arrow.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
        self.translated_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Translated text", None))
        self.translate_lang.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Translate to language", None))
        self.translate_btn.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
        self.to_be_translated.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.to_be_translated.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter text to be translated", None))
        pass
    # retranslateUi

