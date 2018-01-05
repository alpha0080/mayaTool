# -*- coding: utf-8 -*-

from PySide2 import QtCore, QtGui, QtWidgets

class buildUI():


    def __init__(self, parent):
        print 'add button'
        #print
        print parent
        #print buttonText
        #print buttonPosition
        #self.buttonAdd = QtWidgets.QPushButton(parent)

    def addButton(self,buttonText,buttonPosition)

        self.buttonAdd.setGeometry(QtCore.QRect(buttonPosition[0],
                                            buttonPosition[1],
                                            buttonPosition[2],
                                            buttonPosition[3]))
        self.buttonAdd.setText(QtWidgets.QApplication.translate("Form", buttonText, None, -1))
        #buttonAdd.setObjectName('sdsd')
