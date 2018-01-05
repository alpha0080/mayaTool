# -*- coding: utf-8 -*-
#
# It's Pyside2(PYQT5) event-driven modual
#
#

from PySide2 import QtCore, QtGui, QtWidgets

class mouseEvent():

    def mouseMoveEvent(self, e):

        x = e.x()
        y = e.y()

        text = "x: {0},  y: {1}".format(x, y)
        print text
