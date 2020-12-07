import sys
import os
from PyQt5 import QtWidgets 
from PyQt5 import uic

class InfoGUI(QtWidgets.QMainWindow):
    def __init__(self,uipath):
        super(InfoGUI, self).__init__()
        uic.loadUi(uipath, self)

        # QLCDNumber
        self.lcdCountdown = self.findChild(QtWidgets.QLCDNumber, 'lcdNumber') # Find the button

        self.show()

def displayInfoGUI():
    aptalgui_path = resourcePath("aptal.ui")
    app = QtWidgets.QApplication(sys.argv)
    window = InfoGUI(aptalgui_path)
    app.exec_()

def resourcePath(filename, folders = ""):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, folders, filename)

def checkFirstTime():
    if len(sys.argv) > 1:
        print("print second time show only gui")
        return True
    print("FIRST TIME hack it")
    return False
