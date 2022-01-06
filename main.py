from PyQt5 import QtWidgets
import sys
from View.MainWindow import *

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
