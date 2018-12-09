from PyQt5 import QtGui, QtCore
import sys
import numpy as np
import pyqtgraph as pg
#import GridWidget
from .central_widget import CentralWidget
from .menu_bar import MenuBar

class MainWidget(QtGui.QMainWindow):
    
    def __init__(self):
        super().__init__()
        self._init_menubar()
        self._init_ui()
        
    def _init_menubar(self):

        self._menubar = MenuBar()
        self.setMenuBar(self._menubar)
        
    def _init_ui(self):
        
        #TODO scale with screen resolution
        self.setGeometry(400, 100, 1200, 820)

        #TODO: Move this to database
        self.setWindowTitle('Hardware Functional Tool')
        self._central_widget = CentralWidget()
        self.setCentralWidget(self._central_widget)
    
        self.show()

