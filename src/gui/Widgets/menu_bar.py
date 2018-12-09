from PyQt5 import QtGui, QtCore
import sys
import numpy as np

from util.logger import print_log

class MenuBar(QtGui.QMenuBar):

    def __init__(self):
        super().__init__()
        
        self._init_file()
        self._init_settings()
        self._init_view()
        self._init_help()

    def _init_file(self):

        close_action = QtGui.QAction("&Close", self)
        close_action.setShortcut("Ctrl+Q")
        close_action.setStatusTip('Close The Application')
        close_action.triggered.connect(self.close_application)

        fileMenu = self.addMenu('&File')
        fileMenu.addAction(close_action)

    def _init_settings(self):

        close_action = QtGui.QAction("&Change Settings", self)
        # close_action.setShortcut("Ctrl+Q")
        # close_action.setStatusTip('Close The Application')
        # close_action.triggered.connect(self.close_application)
        
        fileMenu = self.addMenu('&Settings')
        fileMenu.addAction(close_action)


    def _init_view(self):

        close_action = QtGui.QAction("&Toggle Control", self)
        # close_action.setShortcut("Ctrl+Q")
        # close_action.setStatusTip('Close The Application')
        # close_action.triggered.connect(self.close_application)
        
        fileMenu = self.addMenu('View')
        fileMenu.addAction(close_action)


    def _init_help(self):

        close_action = QtGui.QAction("&About", self)
        close_action.setStatusTip('Close The Application')
        #close_action.triggered.connect(self.close_application)
        
        fileMenu = self.addMenu('&Help')
        fileMenu.addAction(close_action)
    #TODO ADD CONTROLLER TO CLOSE APP
    def close_application(self):
        sys.exit()