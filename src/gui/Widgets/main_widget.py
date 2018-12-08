from PyQt5 import QtGui, QtCore
import sys
import numpy as np
import pyqtgraph as pg
#import GridWidget
from .central_widget import CentralWidget

class MainWidget(QtGui.QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Hardware Functional Tool')
        self._central_widget = CentralWidget()
        self.setCentralWidget(self._central_widget)
    
        self.show()

