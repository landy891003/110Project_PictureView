import imp
from PyQt5 import QtWidgets

from controller import Controller

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Controller()
    window.showMain()
    sys.exit(app.exec_())
