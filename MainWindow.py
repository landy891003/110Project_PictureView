import sys
from PyQt5 import QtCore,QtWidgets

from main import Ui_MainWindow as main_ui

class MainWindow(QtWidgets.QMainWindow,main_ui):
    switch_window=QtCore.pyqtSignal()
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.RealTime.clicked.connect(self.goRunning)
    def goRunning(self):
        self.switch_window.emit()