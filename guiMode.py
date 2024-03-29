import sys
import os
from time import sleep
from datetime import datetime, timedelta
from PyQt5 import QtWidgets 
from PyQt5 import uic
from PyQt5 import QtCore

from utils import resourcePath

class SetRemainingTimeThreadClass(QtCore.QThread):
    def __init__(self, lcd, start_time_str):
        super(SetRemainingTimeThreadClass,self).__init__()
        self.lcdCountdown = lcd
        self.start_time_str = start_time_str

    def run(self):
        start_time = datetime.strptime(self.start_time_str, '%d/%m/%Y %H:%M:%S')
        remain_time = self.calculateRemaningTime(start_time,1)

        while True:
            new_value = str(remain_time).split(".")[0]
            self.lcdCountdown.display(new_value)
            sleep(1)
            remain_time = remain_time-timedelta(seconds=1)

    def calculateRemaningTime(self, start_time, doubling_time):
        now = datetime.now()
        end = start_time + timedelta(days=doubling_time) 
        remain = end - now
        return remain

class InfoGUI(QtWidgets.QMainWindow):
    def __init__(self, uipath, start_time_str):
        super(InfoGUI, self).__init__()
        uic.loadUi(uipath, self)

        # QLCDNumber
        self.lcdCountdown = self.findChild(QtWidgets.QLCDNumber, 'lcdNumber') # Find the button

        self.threadclass = SetRemainingTimeThreadClass(self.lcdCountdown, start_time_str)
        self.threadclass.start()
        
        self.show()
    

def readInfectionDate(path):
    with open(path,"r") as datefile:
        for _ in range(2):
            datefile.readline()
        start_time_str = " ".join(datefile.readline().strip().split()[-2:])
    return start_time_str

def displayInfoGUI(aeskeyfile):
    start_time_str = readInfectionDate(aeskeyfile)    
    aptalgui_path = resourcePath("aptal.ui")
    app = QtWidgets.QApplication(sys.argv)
    window = InfoGUI(aptalgui_path, start_time_str)
    sys.exit(app.exec_())