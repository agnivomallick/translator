"""
Created by Agnivo Mallick
github.com/agnivomallick
Version: 1.0.0

This app is a translator app.
It uses the Deep Translator library (PyPi url: https://pypi.org/project/deep-translator/)
The Google Translator API is used.

It translates to all languages supported by Google Translator.

Licensed under the terms of the MIT License.

"""

# module imports

# Qt 6.7 import
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from ui_translator import Ui_MainWindow  # UI file import

from deep_translator import GoogleTranslator as gt  # Google translator api

import os

basedir = os.path.dirname(__file__)  # basedir. All paths extend from here.

# ONLY WORKS ON MICROSOFT WINDOWS. CHANGES THE TASKBAR ICON TO THAT OF THE APP.
try:
    from ctypes import windll
    appid = "mycompany.myproduct.subproduct.version"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)

except ImportError:
    pass


# Main Window Class
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # initialise UI

        self.icon = QIcon()
        self.icon.addFile(os.path.join(basedir, "translator_app.ico"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.setWindowIcon(self.icon)  # set window icon

        self.setFixedSize(748, 553)  # set fixed size

        self.translator = gt
        # initializing Google Translator as a class-wide attribute, to be used in translator function.

        self.ui.tobetranslated_lang.addItems(self.translator().get_supported_languages(as_dict=True).keys())
        self.ui.translate_lang.addItems(self.translator().get_supported_languages(as_dict=True).keys())
        # initialize google translator. Get supported languages (as a dictionary). Get the keys. Add to the combo box.

        self.ui.translate_btn.clicked.connect(self.translate_text)  # translate text connection

    def translate_text(self):
        """
        Translate text.

        How this works:
        This is an if-else loop (almost).

        1 The first if-else loop checks if there is any text in the text to be translated box.

        2 If not it raises error

        3 Else it continues with another if-else loop

        4 It now checks if the "translate from" box is set to auto or not

        5 If auto is set it sets the source of translation to auto and the target to the "translate to" box value

        6 Else it sets the source of translation to the "translate from" box value and the target to the "translate to"
        box value

        :return: None
        """

        if not self.ui.to_be_translated.toPlainText():
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Error")
            msg_box.setWindowIcon(self.icon)
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Nothing to translate.")

            execute = msg_box.exec()

            # basic message box configuration

        else:
            # checking if auto
            if self.ui.tobetranslated_lang.currentText() == 'auto':
                translated_text = self.translator(
                    source="auto",  # setting source to auto
                    target=self.ui.translate_lang.currentText()
                ).translate(
                    text=self.ui.to_be_translated.toPlainText())

                self.ui.translated_text.setText(translated_text)
            else:
                # else it sets the source to be the "translate from" combobox value.
                translated_text = self.translator(
                    source=self.ui.tobetranslated_lang.currentText(),
                    target=self.ui.translate_lang.currentText()
                ).translate(text=self.ui.to_be_translated.toPlainText())

                self.ui.translated_text.setText(translated_text)

# starting app


if __name__ == '__main__':
    app = QApplication()
    win = MainWindow()
    win.show()
    app.exec()
