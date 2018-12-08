from PyQt5 import QtGui, QtCore
import sys
import numpy as np


class CentralWidget(QtGui.QMenuBar):

    def __init__(self):
        super().__init__()
        
        self.init_layout()

    def init_layout(self):

        self.setLayout(self._grid)

