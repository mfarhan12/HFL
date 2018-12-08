from PyQt5 import QtGui, QtCore
import sys
import numpy as np
import pyqtgraph as pg

from Widgets.main_widget import MainWidget

if __name__ == '__main__':
    
    app = QtGui.QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())
