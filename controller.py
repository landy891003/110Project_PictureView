import sys
from PyQt5 import QtCore,QtWidgets

from MainWindow import MainWindow
from RunningWindow import RunningWindow
from IllustrateWindow import MainWindow_controller

class Controller:
    def __init__(self):
        pass
    def showMain(self):
        self.main=MainWindow()
        self.main.switch_window.connect(self.showRun)
        self.main.show()
    def showRun(self):
        self.Run=RunningWindow()
        self.main.close()
        self.Run.switch_window2.connect(self.showillustrate)
        self.Run.show()
    def showillustrate(self):
        self.ill=MainWindow_controller()
        self.Run.close()
        self.ill.show()

# if __name__=='__main__':    
#     app = QtWidgets.QApplication(sys.argv)
#     window = ()
#     window.show()
#     sys.exit(app.exec_())

