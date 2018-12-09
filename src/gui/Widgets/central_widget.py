from PyQt5 import QtGui, QtCore
import sys
import numpy as np
import pyqtgraph as pg

from .draw_widget import DrawWidget
from .control_widget import ContralWidget
from controller.draw_controller import DrawController
class CentralWidget(QtGui.QWidget):

    def __init__(self):
        super().__init__()
        
        self._grid = QtGui.QGridLayout()
        self._draw_controller = DrawController()
        self._draw_widget = DrawWidget(self._draw_controller)
        self._control_widget = ContralWidget(self._draw_controller)
        
        self.init_layout()

    def init_layout(self):
        self._grid.addWidget(self._control_widget, 0, 0, 1, 1)
        self._grid.addWidget(self._draw_widget, 0, 1, 5, 20)
        
        self.setLayout(self._grid)

