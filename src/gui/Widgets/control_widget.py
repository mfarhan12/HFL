from PyQt5 import QtGui, QtCore
import sys
import numpy as np
import pyqtgraph as pg


class ContralWidget(QtGui.QWidget):

    def __init__(self, draw_controller):
        super().__init__()
        
        self._grid = QtGui.QGridLayout()
        self._draw_controller = draw_controller

        self._init_controls()
        self._init_layout()

    def _init_controls(self):

        self._square_button = QtGui.QPushButton('Square')
        self._square_button.clicked.connect(self.square_clicked)

        self._select_button = QtGui.QPushButton('Select')
        self._select_button.clicked.connect(self.select_clicked)

        self._circle_button = QtGui.QPushButton('Circle')
        self._wire_button = QtGui.QPushButton('Wire')

    def _init_layout(self):
        
        self._grid.addWidget(self._select_button, 0, 0, 1, 1)
        self._grid.addWidget(self._wire_button, 0, 1, 1, 1)
        self._grid.addWidget(self._square_button, 1, 0, 1, 1)
        self._grid.addWidget(self._circle_button, 1, 1, 1, 1)
        self.setLayout(self._grid)

    def square_clicked(self):
        self._draw_controller.draw_state('state', 'square')

    def select_clicked(self):
        self._draw_controller.draw_state('state', 'select')
