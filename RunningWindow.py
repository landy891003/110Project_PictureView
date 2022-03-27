import sys
from PyQt5 import QtCore,QtWidgets

from running import Ui_MainWindow as running_ui

class RunningWindow(QtWidgets.QMainWindow,running_ui):
    switch_window2=QtCore.pyqtSignal()
    def __init__(self):
        super(RunningWindow,self).__init__()
        self.setupUi(self)
        self.next.clicked.connect(self.goIllustrating)
    def goIllustrating(self):
        self.switch_window2.emit()