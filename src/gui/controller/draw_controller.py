from PyQt5 import QtGui, QtCore
DrawState = {"state": "select"}

class DrawController():

    draw_signal = QtCore.pyqtSignal()
    def __init__(self):

        self._draw_state = DrawState
     #   self._init_signals()

    #def _init_signals(self):

        

    def draw_state(self, key, item):
        self._draw_state[key] = item
        self.draw_signal.emit()

        print('changed draw state to %s' % item)