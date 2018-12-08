from PyQt5 import QtGui, QtCore
import sys
import numpy as np
import pyqtgraph as pg

from .draw_widget import DrawWidget
class CentralWidget(QtGui.QWidget):

    def __init__(self):
        super().__init__()
        
        self._grid = QtGui.QGridLayout()
        self._draw_widget = DrawWidget()
        self.init_layout()

    def init_layout(self):
        
        self._grid.addWidget(self._draw_widget, 1, 1, 5, 5)
        self.setLayout(self._grid)

