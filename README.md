# translator

Translator is a free and easy to use app for translating text cross-language.

## Features

- Built using Google Translator API
- Has all supported languages
- "Translate from?" and "Translate to?" dropdown options with 'auto' option
- Text boxes for the "translate from?" text and the translated text in another textbox.
- Error handling

## Installation

Just download the `.exe` file from the [Releases](https://github.com/agnivomallick/translator/releases)

## Building from source

This project can be built from source or run from source too.

### Requirements
Python 3.11+ for building

The PySide6 and deep_translator PIP packages. (`pip install PySide6` and `pip install deep_translator`)

But there will be a file named `requirements.txt` You type `pip install -r requirements.txt` to install the packages.

**DO NOT MODIFY THE FILE.**

Plus, I recommend virtual environment for continuing. (not required, but preferred.)

### Setup and Building
- Clone the repo or download a zip. For cloning, you need **Git**
- Go to the cloned directory (will be translator/)
- Now here you can run the `translator.py` file with python: `python translator.py` (**THE PACKAGES ARE REQUIRED. They are in the requirements section.**)
- Now you can make an `.exe` file with PyInstaller/cx_freeze/py2exe or any other tool
- If you want to distribute you can make an installer out of it
- **BUT ADHERE TO THE [MIT LICENSE](https://github.com/agnivomallick/translator/blob/main/LICENSE), WHATEVER YOU DO.**
- You can modify the file, however follow the terms of the [MIT License](https://github.com/agnivomallick/translator/blob/main/LICENSE)

## Tools/Packages Used

For GUI, I used Qt 6.7 (PySide6) and the Google Translator API was provided by deep_translator (link in the file)

There is also usage of `ctypes` and `os` libraries of the Python standard library. Their usages are all explained in the file.

## Licensing

This product is licensed under the terms of the [MIT License](https://github.com/agnivomallick/translator/blob/main/LICENSE)
