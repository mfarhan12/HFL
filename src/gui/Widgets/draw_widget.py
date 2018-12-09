from PyQt5 import QtGui, QtCore
import sys
import numpy as np
import pyqtgraph as pg
from util.logger import print_log

class DrawWidget(QtGui.QWidget):
    
    def __init__(self, draw_controller):
        super().__init__()
        self._grid = QtGui.QGridLayout()
        self._draw_controller = draw_controller
        self.initUI()
        
        
    def initUI(self):

        self._main_plot = pg.PlotWidget()
        print_log(2, "Initializing widget")

        self._main_plot.hideAxis('bottom')
        self._main_plot.hideAxis('left')
        self._main_plot.setRange(xRange = (-50, 50), yRange = (-50, 50))
        self._main_plot.showGrid(False, False)

        self._grid.addWidget(self._main_plot, 1, 1, 5, 5)
        self.setLayout(self._grid)
  