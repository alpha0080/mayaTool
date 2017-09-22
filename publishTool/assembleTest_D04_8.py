# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha.DESKTOP-1S1STEK/Documents/GitHub/mayaTool/publishTool/assembleTest_B01.ui'
#
# Created: Thu Jul 06 16:28:26 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

import maya.cmds as cmds
import pymel.core as pm

import json
import os
from pprint import pprint
import datetime

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 860)
        MainWindow.setMinimumSize(QtCore.QSize(650, 860))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 91, 82))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 76, 68))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 30, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 40, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 30, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 91, 82))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 76, 68))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 30, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 40, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 30, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 30, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 91, 82))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 76, 68))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 30, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 40, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 30, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 30, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_15 = QtWidgets.QFrame(self.centralwidget)
        self.frame_15.setGeometry(QtCore.QRect(5, 90, 609, 751))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.frame_15.setPalette(palette)
        self.frame_15.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setLineWidth(1)
        self.frame_15.setMidLineWidth(0)
        self.frame_15.setObjectName("frame_15")
        self.frame_9 = QtWidgets.QFrame(self.frame_15)
        self.frame_9.setGeometry(QtCore.QRect(5, 5, 191, 741))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.frame_9.setPalette(palette)
        self.frame_9.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setLineWidth(1)
        self.frame_9.setMidLineWidth(0)
        self.frame_9.setObjectName("frame_9")
        self.treeWidget_sceneAssembleTree = QtWidgets.QTreeWidget(self.frame_9)
        self.treeWidget_sceneAssembleTree.setGeometry(QtCore.QRect(2, 2, 186, 531))
        self.treeWidget_sceneAssembleTree.setDragEnabled(True)
        self.treeWidget_sceneAssembleTree.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.treeWidget_sceneAssembleTree.setColumnCount(2)
        self.treeWidget_sceneAssembleTree.setObjectName("treeWidget_sceneAssembleTree")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_sceneAssembleTree)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_sceneAssembleTree)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_sceneAssembleTree)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_sceneAssembleTree)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_sceneAssembleTree)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_sceneAssembleTree)
        self.treeWidget_sceneAssembleTree.header().setVisible(False)
        self.treeWidget_sceneAssembleTree.header().setCascadingSectionResizes(False)
        self.treeWidget_sceneAssembleTree.header().setDefaultSectionSize(150)
        self.treeWidget_sceneAssembleTree.header().setHighlightSections(False)
        self.treeWidget_sceneAssembleTree.header().setMinimumSectionSize(25)
        self.frame_7 = QtWidgets.QFrame(self.frame_9)
        self.frame_7.setGeometry(QtCore.QRect(5, 535, 181, 201))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.frame_7.setPalette(palette)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setLineWidth(1)
        self.frame_7.setMidLineWidth(0)
        self.frame_7.setObjectName("frame_7")
        self.label_showImage_2 = QtWidgets.QLabel(self.frame_7)
        self.label_showImage_2.setGeometry(QtCore.QRect(0, 15, 196, 185))
        self.label_showImage_2.setText("")
        self.label_showImage_2.setPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/picture-01-150.png"))
        self.label_showImage_2.setObjectName("label_showImage_2")
        self.frame_10 = QtWidgets.QFrame(self.frame_15)
        self.frame_10.setGeometry(QtCore.QRect(220, 5, 386, 741))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.frame_10.setPalette(palette)
        self.frame_10.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setLineWidth(1)
        self.frame_10.setMidLineWidth(0)
        self.frame_10.setObjectName("frame_10")
        self.tableWidget_AssetItemList = QtWidgets.QTableWidget(self.frame_10)
        self.tableWidget_AssetItemList.setGeometry(QtCore.QRect(3, 1, 381, 531))
        self.tableWidget_AssetItemList.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget_AssetItemList.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tableWidget_AssetItemList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_AssetItemList.setDragEnabled(True)
        self.tableWidget_AssetItemList.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.tableWidget_AssetItemList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_AssetItemList.setIconSize(QtCore.QSize(60, 60))
        self.tableWidget_AssetItemList.setTextElideMode(QtCore.Qt.ElideNone)
        self.tableWidget_AssetItemList.setRowCount(2)
        self.tableWidget_AssetItemList.setColumnCount(2)
        self.tableWidget_AssetItemList.setObjectName("tableWidget_AssetItemList")
        self.tableWidget_AssetItemList.setColumnCount(2)
        self.tableWidget_AssetItemList.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_AssetItemList.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_AssetItemList.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_AssetItemList.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_AssetItemList.setItem(1, 1, item)
        self.tableWidget_AssetItemList.horizontalHeader().setVisible(False)
        self.tableWidget_AssetItemList.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_AssetItemList.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget_AssetItemList.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget_AssetItemList.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_AssetItemList.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_AssetItemList.verticalHeader().setVisible(False)
        self.tableWidget_AssetItemList.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_AssetItemList.verticalHeader().setDefaultSectionSize(120)
        self.tableWidget_AssetItemList.verticalHeader().setHighlightSections(True)
        self.tableWidget_AssetItemList.verticalHeader().setMinimumSectionSize(25)
        self.plainTextEdit_assetMetaData = QtWidgets.QPlainTextEdit(self.frame_10)
        self.plainTextEdit_assetMetaData.setGeometry(QtCore.QRect(2, 535, 381, 201))
        self.plainTextEdit_assetMetaData.setObjectName("plainTextEdit_assetMetaData")
        self.pushButton_P3addItemToLeftA = QtWidgets.QPushButton(self.frame_15)
        self.pushButton_P3addItemToLeftA.setGeometry(QtCore.QRect(195, 8, 25, 50))
        self.pushButton_P3addItemToLeftA.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/addToLeftA.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_P3addItemToLeftA.setIcon(icon)
        self.pushButton_P3addItemToLeftA.setIconSize(QtCore.QSize(30, 120))
        self.pushButton_P3addItemToLeftA.setFlat(True)
        self.pushButton_P3addItemToLeftA.setObjectName("pushButton_P3addItemToLeftA")
        self.pushButton_P3addItemToLeftC = QtWidgets.QPushButton(self.frame_15)
        self.pushButton_P3addItemToLeftC.setGeometry(QtCore.QRect(195, 112, 25, 50))
        self.pushButton_P3addItemToLeftC.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/addToLeftC.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_P3addItemToLeftC.setIcon(icon1)
        self.pushButton_P3addItemToLeftC.setIconSize(QtCore.QSize(25, 120))
        self.pushButton_P3addItemToLeftC.setFlat(True)
        self.pushButton_P3addItemToLeftC.setObjectName("pushButton_P3addItemToLeftC")
        self.pushButton_P3addItemToLeftB = QtWidgets.QPushButton(self.frame_15)
        self.pushButton_P3addItemToLeftB.setGeometry(QtCore.QRect(195, 60, 25, 50))
        self.pushButton_P3addItemToLeftB.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/addToLeftB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_P3addItemToLeftB.setIcon(icon2)
        self.pushButton_P3addItemToLeftB.setIconSize(QtCore.QSize(25, 120))
        self.pushButton_P3addItemToLeftB.setFlat(True)
        self.pushButton_P3addItemToLeftB.setObjectName("pushButton_P3addItemToLeftB")
        self.pushButton_P3_deleteItem = QtWidgets.QPushButton(self.frame_15)
        self.pushButton_P3_deleteItem.setGeometry(QtCore.QRect(198, 510, 20, 26))
        self.pushButton_P3_deleteItem.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/deleteB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_P3_deleteItem.setIcon(icon3)
        self.pushButton_P3_deleteItem.setIconSize(QtCore.QSize(20, 80))
        self.pushButton_P3_deleteItem.setFlat(True)
        self.pushButton_P3_deleteItem.setObjectName("pushButton_P3_deleteItem")
        self.pushButton_P3_addItem = QtWidgets.QPushButton(self.frame_15)
        self.pushButton_P3_addItem.setGeometry(QtCore.QRect(198, 478, 20, 31))
        self.pushButton_P3_addItem.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/addB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_P3_addItem.setIcon(icon4)
        self.pushButton_P3_addItem.setIconSize(QtCore.QSize(20, 80))
        self.pushButton_P3_addItem.setFlat(True)
        self.pushButton_P3_addItem.setObjectName("pushButton_P3_addItem")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(1265, 85, 46, 56))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.frame_4.setPalette(palette)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setLineWidth(1)
        self.frame_4.setMidLineWidth(0)
        self.frame_4.setObjectName("frame_4")
        self.pushButton_shot = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_shot.setEnabled(True)
        self.pushButton_shot.setGeometry(QtCore.QRect(9, 20, 31, 31))
        self.pushButton_shot.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/shotS5Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/shotS5Open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_shot.setIcon(icon5)
        self.pushButton_shot.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_shot.setCheckable(True)
        self.pushButton_shot.setAutoDefault(False)
        self.pushButton_shot.setDefault(False)
        self.pushButton_shot.setFlat(True)
        self.pushButton_shot.setObjectName("pushButton_shot")
        self.label_fileData_17 = QtWidgets.QLabel(self.frame_4)
        self.label_fileData_17.setGeometry(QtCore.QRect(10, 0, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_17.setFont(font)
        self.label_fileData_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_17.setObjectName("label_fileData_17")
        self.pushButton_inProgress_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_inProgress_3.setEnabled(True)
        self.pushButton_inProgress_3.setGeometry(QtCore.QRect(1280, 185, 30, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pushButton_inProgress_3.setPalette(palette)
        self.pushButton_inProgress_3.setAutoFillBackground(False)
        self.pushButton_inProgress_3.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/projSelect_inProgressB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon6.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/projSelect_inProgressA.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_inProgress_3.setIcon(icon6)
        self.pushButton_inProgress_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_inProgress_3.setCheckable(True)
        self.pushButton_inProgress_3.setChecked(False)
        self.pushButton_inProgress_3.setAutoRepeat(False)
        self.pushButton_inProgress_3.setAutoExclusive(False)
        self.pushButton_inProgress_3.setAutoDefault(False)
        self.pushButton_inProgress_3.setDefault(False)
        self.pushButton_inProgress_3.setFlat(True)
        self.pushButton_inProgress_3.setObjectName("pushButton_inProgress_3")
        self.tableWidget_all_inputItemList = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_all_inputItemList.setGeometry(QtCore.QRect(665, 10, 576, 861))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 30, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.tableWidget_all_inputItemList.setPalette(palette)
        self.tableWidget_all_inputItemList.setObjectName("tableWidget_all_inputItemList")
        self.tableWidget_all_inputItemList.setColumnCount(3)
        self.tableWidget_all_inputItemList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_all_inputItemList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_all_inputItemList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_all_inputItemList.setHorizontalHeaderItem(2, item)
        self.tableWidget_all_inputItemList.horizontalHeader().setVisible(True)
        self.tableWidget_all_inputItemList.horizontalHeader().setDefaultSectionSize(120)
        self.frame_21 = QtWidgets.QFrame(self.centralwidget)
        self.frame_21.setGeometry(QtCore.QRect(590, 31, 56, 56))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.frame_21.setPalette(palette)
        self.frame_21.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setLineWidth(1)
        self.frame_21.setMidLineWidth(0)
        self.frame_21.setObjectName("frame_21")
        self.pushButton_P3_changePageA = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_P3_changePageA.setEnabled(True)
        self.pushButton_P3_changePageA.setGeometry(QtCore.QRect(2, 3, 25, 25))
        self.pushButton_P3_changePageA.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/connerA.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_P3_changePageA.setIcon(icon7)
        self.pushButton_P3_changePageA.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_P3_changePageA.setCheckable(True)
        self.pushButton_P3_changePageA.setAutoDefault(False)
        self.pushButton_P3_changePageA.setDefault(False)
        self.pushButton_P3_changePageA.setFlat(True)
        self.pushButton_P3_changePageA.setObjectName("pushButton_P3_changePageA")
        self.pushButton_P3_changePageB = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_P3_changePageB.setEnabled(True)
        self.pushButton_P3_changePageB.setGeometry(QtCore.QRect(27, 3, 25, 25))
        self.pushButton_P3_changePageB.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/connerB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_P3_changePageB.setIcon(icon8)
        self.pushButton_P3_changePageB.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_P3_changePageB.setCheckable(True)
        self.pushButton_P3_changePageB.setAutoDefault(False)
        self.pushButton_P3_changePageB.setDefault(False)
        self.pushButton_P3_changePageB.setFlat(True)
        self.pushButton_P3_changePageB.setObjectName("pushButton_P3_changePageB")
        self.pushButton_P3_changePageC = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_P3_changePageC.setEnabled(True)
        self.pushButton_P3_changePageC.setGeometry(QtCore.QRect(2, 28, 25, 25))
        self.pushButton_P3_changePageC.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/connerC.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_P3_changePageC.setIcon(icon9)
        self.pushButton_P3_changePageC.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_P3_changePageC.setCheckable(True)
        self.pushButton_P3_changePageC.setAutoDefault(False)
        self.pushButton_P3_changePageC.setDefault(False)
        self.pushButton_P3_changePageC.setFlat(True)
        self.pushButton_P3_changePageC.setObjectName("pushButton_P3_changePageC")
        self.pushButton_P3_changePageD = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_P3_changePageD.setEnabled(True)
        self.pushButton_P3_changePageD.setGeometry(QtCore.QRect(27, 28, 25, 25))
        self.pushButton_P3_changePageD.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/connerD.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_P3_changePageD.setIcon(icon10)
        self.pushButton_P3_changePageD.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_P3_changePageD.setCheckable(True)
        self.pushButton_P3_changePageD.setAutoDefault(False)
        self.pushButton_P3_changePageD.setDefault(False)
        self.pushButton_P3_changePageD.setFlat(True)
        self.pushButton_P3_changePageD.setObjectName("pushButton_P3_changePageD")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(1265, 250, 121, 56))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.frame.setPalette(palette)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(435, 32, 151, 56))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.frame_5.setPalette(palette)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setLineWidth(1)
        self.frame_5.setMidLineWidth(0)
        self.frame_5.setObjectName("frame_5")
        self.label_fileData_19 = QtWidgets.QLabel(self.frame_5)
        self.label_fileData_19.setGeometry(QtCore.QRect(50, 0, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_19.setFont(font)
        self.label_fileData_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_19.setObjectName("label_fileData_19")
        self.label_fileData_20 = QtWidgets.QLabel(self.frame_5)
        self.label_fileData_20.setGeometry(QtCore.QRect(15, 0, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_20.setFont(font)
        self.label_fileData_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_20.setObjectName("label_fileData_20")
        self.label_fileData_21 = QtWidgets.QLabel(self.frame_5)
        self.label_fileData_21.setGeometry(QtCore.QRect(85, 0, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_21.setFont(font)
        self.label_fileData_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_21.setObjectName("label_fileData_21")
        self.label_fileData_22 = QtWidgets.QLabel(self.frame_5)
        self.label_fileData_22.setGeometry(QtCore.QRect(120, 0, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_22.setFont(font)
        self.label_fileData_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_22.setObjectName("label_fileData_22")
        self.pushButton_P3_largeIcon = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_P3_largeIcon.setEnabled(True)
        self.pushButton_P3_largeIcon.setGeometry(QtCore.QRect(10, 20, 30, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pushButton_P3_largeIcon.setPalette(palette)
        self.pushButton_P3_largeIcon.setAutoFillBackground(False)
        self.pushButton_P3_largeIcon.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/sizeChoose_Large_Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon11.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/sizeChooseLarge.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon11.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/sizeChooseLarge.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        icon11.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/sizeChooseLarge.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.pushButton_P3_largeIcon.setIcon(icon11)
        self.pushButton_P3_largeIcon.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_P3_largeIcon.setCheckable(True)
        self.pushButton_P3_largeIcon.setChecked(False)
        self.pushButton_P3_largeIcon.setAutoRepeat(False)
        self.pushButton_P3_largeIcon.setAutoExclusive(False)
        self.pushButton_P3_largeIcon.setAutoDefault(False)
        self.pushButton_P3_largeIcon.setDefault(False)
        self.pushButton_P3_largeIcon.setFlat(True)
        self.pushButton_P3_largeIcon.setObjectName("pushButton_P3_largeIcon")
        self.pushButton_P3_MidIcon = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_P3_MidIcon.setEnabled(True)
        self.pushButton_P3_MidIcon.setGeometry(QtCore.QRect(45, 20, 30, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pushButton_P3_MidIcon.setPalette(palette)
        self.pushButton_P3_MidIcon.setAutoFillBackground(False)
        self.pushButton_P3_MidIcon.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/sizeChoose_Mid_Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon12.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/sizeChooseMid.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon12.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/sizeChooseMid.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon12.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/sizeChooseMid.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        icon12.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/sizeChooseMid.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.pushButton_P3_MidIcon.setIcon(icon12)
        self.pushButton_P3_MidIcon.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_P3_MidIcon.setCheckable(True)
        self.pushButton_P3_MidIcon.setChecked(False)
        self.pushButton_P3_MidIcon.setAutoRepeat(False)
        self.pushButton_P3_MidIcon.setAutoExclusive(False)
        self.pushButton_P3_MidIcon.setAutoDefault(False)
        self.pushButton_P3_MidIcon.setDefault(False)
        self.pushButton_P3_MidIcon.setFlat(True)
        self.pushButton_P3_MidIcon.setObjectName("pushButton_P3_MidIcon")
        self.pushButton_P3_smallIcon = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_P3_smallIcon.setEnabled(True)
        self.pushButton_P3_smallIcon.setGeometry(QtCore.QRect(80, 20, 30, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pushButton_P3_smallIcon.setPalette(palette)
        self.pushButton_P3_smallIcon.setAutoFillBackground(False)
        self.pushButton_P3_smallIcon.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/sizeChoose_Small_Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon13.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/sizeChooseSmall.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon13.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/sizeChooseSmall.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon13.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/sizeChooseSmall.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        icon13.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/sizeChooseSmall.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.pushButton_P3_smallIcon.setIcon(icon13)
        self.pushButton_P3_smallIcon.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_P3_smallIcon.setCheckable(True)
        self.pushButton_P3_smallIcon.setChecked(False)
        self.pushButton_P3_smallIcon.setAutoRepeat(False)
        self.pushButton_P3_smallIcon.setAutoExclusive(False)
        self.pushButton_P3_smallIcon.setAutoDefault(False)
        self.pushButton_P3_smallIcon.setDefault(False)
        self.pushButton_P3_smallIcon.setFlat(True)
        self.pushButton_P3_smallIcon.setObjectName("pushButton_P3_smallIcon")
        self.pushButton_P3_text = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_P3_text.setEnabled(True)
        self.pushButton_P3_text.setGeometry(QtCore.QRect(115, 20, 30, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pushButton_P3_text.setPalette(palette)
        self.pushButton_P3_text.setAutoFillBackground(False)
        self.pushButton_P3_text.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/sizeChoose_Text_Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon14.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/sizeChooseText.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon14.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/sizeChooseText.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        icon14.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/sizeChooseText.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.pushButton_P3_text.setIcon(icon14)
        self.pushButton_P3_text.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_P3_text.setCheckable(True)
        self.pushButton_P3_text.setChecked(False)
        self.pushButton_P3_text.setAutoRepeat(False)
        self.pushButton_P3_text.setAutoExclusive(False)
        self.pushButton_P3_text.setAutoDefault(False)
        self.pushButton_P3_text.setDefault(False)
        self.pushButton_P3_text.setFlat(True)
        self.pushButton_P3_text.setObjectName("pushButton_P3_text")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(5, 32, 221, 56))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.frame_6.setPalette(palette)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setLineWidth(1)
        self.frame_6.setMidLineWidth(0)
        self.frame_6.setObjectName("frame_6")
        self.pushButton_P3_deletSelectItem = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_P3_deletSelectItem.setGeometry(QtCore.QRect(150, 20, 30, 30))
        self.pushButton_P3_deletSelectItem.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/deletePublishB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_P3_deletSelectItem.setIcon(icon15)
        self.pushButton_P3_deletSelectItem.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_P3_deletSelectItem.setFlat(True)
        self.pushButton_P3_deletSelectItem.setObjectName("pushButton_P3_deletSelectItem")
        self.pushButton_P3_selectItem = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_P3_selectItem.setGeometry(QtCore.QRect(50, 15, 35, 35))
        self.pushButton_P3_selectItem.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/getSelectItemPublishB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_P3_selectItem.setIcon(icon16)
        self.pushButton_P3_selectItem.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_P3_selectItem.setFlat(True)
        self.pushButton_P3_selectItem.setObjectName("pushButton_P3_selectItem")
        self.label_fileData_43 = QtWidgets.QLabel(self.frame_6)
        self.label_fileData_43.setGeometry(QtCore.QRect(145, 0, 46, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_fileData_43.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_43.setFont(font)
        self.label_fileData_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_43.setObjectName("label_fileData_43")
        self.label_fileData_40 = QtWidgets.QLabel(self.frame_6)
        self.label_fileData_40.setGeometry(QtCore.QRect(45, -3, 46, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_fileData_40.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_40.setFont(font)
        self.label_fileData_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_40.setObjectName("label_fileData_40")
        self.pushButton_P3_refreshInputItem = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_P3_refreshInputItem.setGeometry(QtCore.QRect(5, 15, 35, 35))
        self.pushButton_P3_refreshInputItem.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/refreshPublishB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_P3_refreshInputItem.setIcon(icon17)
        self.pushButton_P3_refreshInputItem.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_P3_refreshInputItem.setFlat(True)
        self.pushButton_P3_refreshInputItem.setObjectName("pushButton_P3_refreshInputItem")
        self.label_fileData_39 = QtWidgets.QLabel(self.frame_6)
        self.label_fileData_39.setGeometry(QtCore.QRect(0, -3, 46, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_fileData_39.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_39.setFont(font)
        self.label_fileData_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_39.setObjectName("label_fileData_39")
        self.frame_8 = QtWidgets.QFrame(self.centralwidget)
        self.frame_8.setGeometry(QtCore.QRect(615, 90, 36, 531))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.frame_8.setPalette(palette)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setLineWidth(1)
        self.frame_8.setMidLineWidth(0)
        self.frame_8.setObjectName("frame_8")
        self.pushButton_P3_openBranchJson = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_P3_openBranchJson.setEnabled(True)
        self.pushButton_P3_openBranchJson.setGeometry(QtCore.QRect(3, 472, 25, 25))
        self.pushButton_P3_openBranchJson.setText("")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/option2-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_P3_openBranchJson.setIcon(icon18)
        self.pushButton_P3_openBranchJson.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_P3_openBranchJson.setCheckable(True)
        self.pushButton_P3_openBranchJson.setAutoDefault(False)
        self.pushButton_P3_openBranchJson.setDefault(False)
        self.pushButton_P3_openBranchJson.setFlat(True)
        self.pushButton_P3_openBranchJson.setObjectName("pushButton_P3_openBranchJson")
        self.pushButton_P3_loadFile = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_P3_loadFile.setEnabled(True)
        self.pushButton_P3_loadFile.setGeometry(QtCore.QRect(3, 440, 25, 25))
        self.pushButton_P3_loadFile.setText("")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/load60.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_P3_loadFile.setIcon(icon19)
        self.pushButton_P3_loadFile.setIconSize(QtCore.QSize(27, 25))
        self.pushButton_P3_loadFile.setCheckable(True)
        self.pushButton_P3_loadFile.setAutoDefault(False)
        self.pushButton_P3_loadFile.setDefault(False)
        self.pushButton_P3_loadFile.setFlat(True)
        self.pushButton_P3_loadFile.setObjectName("pushButton_P3_loadFile")
        self.pushButton_P3_processModeling = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_P3_processModeling.setEnabled(True)
        self.pushButton_P3_processModeling.setGeometry(QtCore.QRect(5, 5, 25, 25))
        self.pushButton_P3_processModeling.setText("")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/processMod_C_OFF.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon20.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/processMod_C_ON.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon20.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/processMod_C_OFF.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon20.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/processMod_C_ON.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        icon20.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/processMod_C_OFF.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.pushButton_P3_processModeling.setIcon(icon20)
        self.pushButton_P3_processModeling.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_P3_processModeling.setCheckable(True)
        self.pushButton_P3_processModeling.setAutoDefault(False)
        self.pushButton_P3_processModeling.setDefault(False)
        self.pushButton_P3_processModeling.setFlat(True)
        self.pushButton_P3_processModeling.setObjectName("pushButton_P3_processModeling")
        self.pushButton_P3_processTexture = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_P3_processTexture.setEnabled(True)
        self.pushButton_P3_processTexture.setGeometry(QtCore.QRect(5, 31, 25, 25))
        self.pushButton_P3_processTexture.setText("")
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/processTex_C_ON.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon21.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/processText_C_OFF.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon21.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/processText_C_OFF.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon21.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/processText_C_OFF.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon21.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/processText_C_OFF.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon21.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/processTex_C_ON.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        icon21.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/processTex_C_ON.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_P3_processTexture.setIcon(icon21)
        self.pushButton_P3_processTexture.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_P3_processTexture.setCheckable(True)
        self.pushButton_P3_processTexture.setAutoDefault(False)
        self.pushButton_P3_processTexture.setDefault(False)
        self.pushButton_P3_processTexture.setFlat(True)
        self.pushButton_P3_processTexture.setObjectName("pushButton_P3_processTexture")
        self.pushButton_P3_processRigging = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_P3_processRigging.setEnabled(True)
        self.pushButton_P3_processRigging.setGeometry(QtCore.QRect(5, 57, 25, 25))
        self.pushButton_P3_processRigging.setText("")
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/processRig_C_ON.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon22.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/processRig_C_OFF.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon22.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/processRig_C_OFF.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon22.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/processRig_C_OFF.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon22.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/processRig_C_OFF.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon22.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/processRig_C_ON.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.pushButton_P3_processRigging.setIcon(icon22)
        self.pushButton_P3_processRigging.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_P3_processRigging.setCheckable(True)
        self.pushButton_P3_processRigging.setAutoDefault(False)
        self.pushButton_P3_processRigging.setDefault(False)
        self.pushButton_P3_processRigging.setFlat(True)
        self.pushButton_P3_processRigging.setObjectName("pushButton_P3_processRigging")
        self.pushButton_P3_inputMayaOn = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_P3_inputMayaOn.setEnabled(True)
        self.pushButton_P3_inputMayaOn.setGeometry(QtCore.QRect(3, 230, 25, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pushButton_P3_inputMayaOn.setPalette(palette)
        self.pushButton_P3_inputMayaOn.setAutoFillBackground(False)
        self.pushButton_P3_inputMayaOn.setText("")
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/InputOption_Maya_ON.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon23.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/InputOption_maya_Off.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon23.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/InputOption_maya_Off.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon23.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/InputOption_maya_Off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon23.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/InputOption_Maya_ON.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon23.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/InputOption_maya_Off.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon23.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/InputOption_Maya_ON.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        icon23.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/InputOption_Maya_ON.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_P3_inputMayaOn.setIcon(icon23)
        self.pushButton_P3_inputMayaOn.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_P3_inputMayaOn.setCheckable(True)
        self.pushButton_P3_inputMayaOn.setChecked(False)
        self.pushButton_P3_inputMayaOn.setAutoRepeat(False)
        self.pushButton_P3_inputMayaOn.setAutoExclusive(False)
        self.pushButton_P3_inputMayaOn.setAutoDefault(False)
        self.pushButton_P3_inputMayaOn.setDefault(False)
        self.pushButton_P3_inputMayaOn.setFlat(True)
        self.pushButton_P3_inputMayaOn.setObjectName("pushButton_P3_inputMayaOn")
        self.pushButton_P3_inputRibOn = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_P3_inputRibOn.setEnabled(True)
        self.pushButton_P3_inputRibOn.setGeometry(QtCore.QRect(3, 265, 25, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pushButton_P3_inputRibOn.setPalette(palette)
        self.pushButton_P3_inputRibOn.setAutoFillBackground(False)
        self.pushButton_P3_inputRibOn.setText("")
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/InputOptionRIB_On.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon24.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/InputOption_Rib_Off.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon24.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/InputOption_Rib_Off.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon24.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/InputOption_Rib_Off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon24.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/InputOptionRIB_On.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon24.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/InputOption_Rib_Off.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon24.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/InputOptionRIB_On.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        icon24.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/InputOptionRIB_On.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_P3_inputRibOn.setIcon(icon24)
        self.pushButton_P3_inputRibOn.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_P3_inputRibOn.setCheckable(True)
        self.pushButton_P3_inputRibOn.setChecked(False)
        self.pushButton_P3_inputRibOn.setAutoRepeat(False)
        self.pushButton_P3_inputRibOn.setAutoExclusive(False)
        self.pushButton_P3_inputRibOn.setAutoDefault(False)
        self.pushButton_P3_inputRibOn.setDefault(False)
        self.pushButton_P3_inputRibOn.setFlat(True)
        self.pushButton_P3_inputRibOn.setObjectName("pushButton_P3_inputRibOn")
        self.pushButton_P3_NA = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_P3_NA.setEnabled(True)
        self.pushButton_P3_NA.setGeometry(QtCore.QRect(5, 83, 25, 25))
        self.pushButton_P3_NA.setText("")
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/processNA_C_ON.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon25.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/processNA_C_OFF.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon25.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/processNA_C_OFF.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon25.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/processNA_C_OFF.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon25.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/processNA_C_OFF.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon25.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/processNA_C_ON.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.pushButton_P3_NA.setIcon(icon25)
        self.pushButton_P3_NA.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_P3_NA.setCheckable(True)
        self.pushButton_P3_NA.setAutoDefault(False)
        self.pushButton_P3_NA.setDefault(False)
        self.pushButton_P3_NA.setFlat(True)
        self.pushButton_P3_NA.setObjectName("pushButton_P3_NA")
        self.pushButton_P3_packageAll = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_P3_packageAll.setGeometry(QtCore.QRect(3, 501, 25, 25))
        self.pushButton_P3_packageAll.setText("")
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/package.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_P3_packageAll.setIcon(icon26)
        self.pushButton_P3_packageAll.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_P3_packageAll.setFlat(True)
        self.pushButton_P3_packageAll.setObjectName("pushButton_P3_packageAll")
        self.label_fileData_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_fileData_16.setGeometry(QtCore.QRect(680, 895, 76, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_16.setFont(font)
        self.label_fileData_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_16.setObjectName("label_fileData_16")
        self.label_projInfo = QtWidgets.QLabel(self.centralwidget)
        self.label_projInfo.setGeometry(QtCore.QRect(755, 895, 251, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_projInfo.setFont(font)
        self.label_projInfo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_projInfo.setObjectName("label_projInfo")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(360, 5, 286, 22))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.comboBox.setPalette(palette)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.frame_11 = QtWidgets.QFrame(self.centralwidget)
        self.frame_11.setGeometry(QtCore.QRect(227, 32, 206, 56))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 182, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 151, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 80, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 121, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.frame_11.setPalette(palette)
        self.frame_11.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setLineWidth(1)
        self.frame_11.setMidLineWidth(0)
        self.frame_11.setObjectName("frame_11")
        self.pushButton_page3_other = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_page3_other.setEnabled(True)
        self.pushButton_page3_other.setGeometry(QtCore.QRect(170, 20, 30, 30))
        self.pushButton_page3_other.setText("")
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_other_ON.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon27.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_other_OFF.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon27.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_other_OFF.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon27.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_other_OFF.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon27.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_other_OFF.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon27.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_other_ON.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.pushButton_page3_other.setIcon(icon27)
        self.pushButton_page3_other.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_page3_other.setCheckable(True)
        self.pushButton_page3_other.setAutoDefault(False)
        self.pushButton_page3_other.setDefault(False)
        self.pushButton_page3_other.setFlat(True)
        self.pushButton_page3_other.setObjectName("pushButton_page3_other")
        self.pushButton_page3_vehicle = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_page3_vehicle.setEnabled(True)
        self.pushButton_page3_vehicle.setGeometry(QtCore.QRect(77, 20, 30, 30))
        self.pushButton_page3_vehicle.setText("")
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_veh_ON.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon28.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_veh_OFF.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon28.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_veh_OFF.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon28.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_veh_OFF.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon28.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_veh_OFF.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon28.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_veh_OFF.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon28.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_veh_ON.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        icon28.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_veh_ON.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_page3_vehicle.setIcon(icon28)
        self.pushButton_page3_vehicle.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_page3_vehicle.setCheckable(True)
        self.pushButton_page3_vehicle.setAutoDefault(False)
        self.pushButton_page3_vehicle.setDefault(False)
        self.pushButton_page3_vehicle.setFlat(True)
        self.pushButton_page3_vehicle.setObjectName("pushButton_page3_vehicle")
        self.pushButton_page3_all = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_page3_all.setEnabled(True)
        self.pushButton_page3_all.setGeometry(QtCore.QRect(10, 20, 30, 30))
        self.pushButton_page3_all.setText("")
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_all_ON.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon29.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_all_OFF.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon29.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_all_OFF.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon29.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_all_OFF.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon29.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_all_OFF.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon29.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_all_ON.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.pushButton_page3_all.setIcon(icon29)
        self.pushButton_page3_all.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_page3_all.setCheckable(True)
        self.pushButton_page3_all.setAutoDefault(False)
        self.pushButton_page3_all.setDefault(False)
        self.pushButton_page3_all.setFlat(True)
        self.pushButton_page3_all.setObjectName("pushButton_page3_all")
        self.pushButton_page3_props = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_page3_props.setEnabled(True)
        self.pushButton_page3_props.setGeometry(QtCore.QRect(139, 20, 30, 30))
        self.pushButton_page3_props.setText("")
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_prop_ON.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon30.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_prop_OFF.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon30.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_prop_OFF.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon30.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_prop_OFF.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon30.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_prop_OFF.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon30.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_prop_ON.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.pushButton_page3_props.setIcon(icon30)
        self.pushButton_page3_props.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_page3_props.setCheckable(True)
        self.pushButton_page3_props.setAutoDefault(False)
        self.pushButton_page3_props.setDefault(False)
        self.pushButton_page3_props.setFlat(True)
        self.pushButton_page3_props.setObjectName("pushButton_page3_props")
        self.pushButton_page3_character = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_page3_character.setEnabled(True)
        self.pushButton_page3_character.setGeometry(QtCore.QRect(46, 20, 30, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pushButton_page3_character.setPalette(palette)
        self.pushButton_page3_character.setAutoFillBackground(False)
        self.pushButton_page3_character.setText("")
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_cha_ON.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon31.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_cha_OFF.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon31.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_cha_OFF.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon31.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_cha_OFF.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon31.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_cha_OFF.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon31.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_cha_OFF.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon31.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_cha_ON.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        icon31.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_cha_ON.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_page3_character.setIcon(icon31)
        self.pushButton_page3_character.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_page3_character.setCheckable(True)
        self.pushButton_page3_character.setChecked(False)
        self.pushButton_page3_character.setAutoRepeat(False)
        self.pushButton_page3_character.setAutoExclusive(False)
        self.pushButton_page3_character.setAutoDefault(False)
        self.pushButton_page3_character.setDefault(False)
        self.pushButton_page3_character.setFlat(True)
        self.pushButton_page3_character.setObjectName("pushButton_page3_character")
        self.pushButton_page3_set = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_page3_set.setEnabled(True)
        self.pushButton_page3_set.setGeometry(QtCore.QRect(108, 20, 30, 30))
        self.pushButton_page3_set.setText("")
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_set_OFF.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon32.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_set_OFF.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon32.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_set_OFF.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon32.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_set_OFF.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon32.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_set_ON.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        icon32.addPixmap(QtGui.QPixmap("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/assetType_set_ON.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_page3_set.setIcon(icon32)
        self.pushButton_page3_set.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_page3_set.setCheckable(True)
        self.pushButton_page3_set.setAutoDefault(False)
        self.pushButton_page3_set.setDefault(False)
        self.pushButton_page3_set.setFlat(True)
        self.pushButton_page3_set.setObjectName("pushButton_page3_set")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.treeWidget_sceneAssembleTree.headerItem().setText(0, QtWidgets.QApplication.translate("MainWindow", "assetName", None, -1))
        self.treeWidget_sceneAssembleTree.headerItem().setText(1, QtWidgets.QApplication.translate("MainWindow", "assetProcess", None, -1))
        __sortingEnabled = self.treeWidget_sceneAssembleTree.isSortingEnabled()
        self.treeWidget_sceneAssembleTree.setSortingEnabled(False)
        self.treeWidget_sceneAssembleTree.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "Character", None, -1))
        self.treeWidget_sceneAssembleTree.topLevelItem(0).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "anna", None, -1))
        self.treeWidget_sceneAssembleTree.topLevelItem(0).child(0).setText(1, QtWidgets.QApplication.translate("MainWindow", "model", None, -1))
        self.treeWidget_sceneAssembleTree.topLevelItem(0).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "tiger", None, -1))
        self.treeWidget_sceneAssembleTree.topLevelItem(0).child(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "joey", None, -1))
        self.treeWidget_sceneAssembleTree.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "Vehicle", None, -1))
        self.treeWidget_sceneAssembleTree.topLevelItem(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "Set", None, -1))
        self.treeWidget_sceneAssembleTree.topLevelItem(3).setText(0, QtWidgets.QApplication.translate("MainWindow", "Prop", None, -1))
        self.treeWidget_sceneAssembleTree.topLevelItem(4).setText(0, QtWidgets.QApplication.translate("MainWindow", "Other", None, -1))
        self.treeWidget_sceneAssembleTree.topLevelItem(5).setText(0, QtWidgets.QApplication.translate("MainWindow", "Effect", None, -1))
        self.treeWidget_sceneAssembleTree.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.tableWidget_AssetItemList.isSortingEnabled()
        self.tableWidget_AssetItemList.setSortingEnabled(False)
        self.tableWidget_AssetItemList.item(0, 0).setText(QtWidgets.QApplication.translate("MainWindow", "a", None, -1))
        self.tableWidget_AssetItemList.item(0, 1).setText(QtWidgets.QApplication.translate("MainWindow", "a", None, -1))
        self.tableWidget_AssetItemList.item(1, 0).setText(QtWidgets.QApplication.translate("MainWindow", "a", None, -1))
        self.tableWidget_AssetItemList.item(1, 1).setText(QtWidgets.QApplication.translate("MainWindow", "a", None, -1))
        self.tableWidget_AssetItemList.setSortingEnabled(__sortingEnabled)
        self.label_fileData_17.setText(QtWidgets.QApplication.translate("MainWindow", "Shot", None, -1))
        self.tableWidget_all_inputItemList.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("MainWindow", "index", None, -1))
        self.tableWidget_all_inputItemList.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("MainWindow", "itemName", None, -1))
        self.tableWidget_all_inputItemList.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("MainWindow", "count", None, -1))
        self.label_fileData_19.setText(QtWidgets.QApplication.translate("MainWindow", "M", None, -1))
        self.label_fileData_20.setText(QtWidgets.QApplication.translate("MainWindow", "L", None, -1))
        self.label_fileData_21.setText(QtWidgets.QApplication.translate("MainWindow", "S", None, -1))
        self.label_fileData_22.setText(QtWidgets.QApplication.translate("MainWindow", "T", None, -1))
        self.label_fileData_43.setText(QtWidgets.QApplication.translate("MainWindow", "Delete", None, -1))
        self.label_fileData_40.setText(QtWidgets.QApplication.translate("MainWindow", "Select", None, -1))
        self.label_fileData_39.setText(QtWidgets.QApplication.translate("MainWindow", "Refresh", None, -1))
        self.label_fileData_16.setText(QtWidgets.QApplication.translate("MainWindow", "Current Proj.", None, -1))
        self.label_projInfo.setText(QtWidgets.QApplication.translate("MainWindow", "abcd", None, -1))
        self.comboBox.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Select Asset Pref Table", None, -1))


        

class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)

        self.setupUi(self)
        self.typeListAllowDict = {'transform':[255,255,255],     #item list could be move and edit
        'mesh':[100,190,70],
        'RenderManArchive':[200,100,100],
        'gpuCache':[30,230,230],
        'moreThanOneItemTheSameName':[255,0,0]
        }   

        
        self.treeWidget_sceneAssembleTree.setDragEnabled(True)
        self.treeWidget_sceneAssembleTree.setDragDropOverwriteMode(True)
        self.treeWidget_sceneAssembleTree.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.treeWidget_sceneAssembleTree.setDefaultDropAction(QtCore.Qt.LinkAction)
        
        #self.treeWidget_sceneAssembleTree.itemClicked.connect(self.treeItemClick)
        self.treeWidget_sceneAssembleTree.itemPressed.connect(self.treeItemClick)  #



        self.pushButton_P3_largeIcon.clicked.connect(self.setLargeAssetIcon)
        self.pushButton_P3_MidIcon.clicked.connect(self.setMidAssetIcon)
        self.pushButton_P3_smallIcon.clicked.connect(self.setSmallAssetIcon)
        self.pushButton_P3_text.clicked.connect(self.setTextAssetMain)
        self.tableWidget_AssetItemList.itemClicked.connect(self.showAssetMetaDataFromSelect)
        self.itemDict ={}
        self.iconFile = QtGui.QIcon("//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/NA120ENPTY.png")
        self.currentIconSize = 'large' #default set to large size icon

        
        #self.tableWidget_AssetItemList.setSortingEnabled(True)
       # self.tableWidget_AssetItemList.pressed.connect(self.dragTest)
        
      #  drag = QtGui.QDrag(self)
       # print 'dragTest',drag.mimeData()
        
        #print drag,type(drag)
        
        
        # initial button checked
        self.pushButton_page3_all.setChecked(True)
        self.pushButton_P3_processModeling.setChecked(True)
        self.pushButton_P3_processTexture.setChecked(True)
        self.pushButton_P3_processRigging.setChecked(True)
        self.pushButton_P3_inputMayaOn.setChecked(True)
        self.pushButton_P3_NA.setChecked(False)
        self.clickAssetFilletAll()
       # self.allAssetClassFillet = ['character','vehicle','set','prop','other']
        
        #button click sing
        self.pushButton_page3_all.clicked.connect(self.clickAssetFilletAll)
        self.pushButton_page3_character.clicked.connect(self.clickAssetFilletCharacter)
        self.pushButton_page3_vehicle.clicked.connect(self.clickAssetFilletVehicle)
        self.pushButton_page3_set.clicked.connect(self.clickAssetFilletSet)
        self.pushButton_page3_props.clicked.connect(self.clickAssetFilletProps)
        self.pushButton_page3_other.clicked.connect(self.clickAssetFilletOther)
        self.pushButton_P3_addItem.clicked.connect(self.addOutlineGroup)
        
        self.pushButton_P3_processModeling.clicked.connect(self.clickProcessFilletChange)
        self.pushButton_P3_processTexture.clicked.connect(self.clickProcessFilletChange)
        self.pushButton_P3_processRigging.clicked.connect(self.clickProcessFilletChange)
        self.pushButton_P3_NA.clicked.connect(self.clickProcessFilletChange)
         
         
        self.pushButton_P3_refreshInputItem.clicked.connect(self.reflashOutLinerTree)
         
         
            
       # self.pushButton_P3addItemToLeftA.clicked.connect(self.runBuildItemLevelTree)
       # self.pushButton_P3addItemToLeftB.clicked.connect(self.storeOutLineStructure)
        self.pushButton_P3addItemToLeftC.clicked.connect(self.ttt)
     
        ## modify treeWidget_sceneAssembleTree start----------------------------------------------------
        #self.treeWidget_sceneAssembleTree.itemChanged.connect(self.itemChangedName)



        self.treeWidget_sceneAssembleTree.setColumnCount(1)
        self.treeWidget_sceneAssembleTree.header().setDefaultSectionSize(350)

        self.treeWidget_sceneAssembleTree.header().setMinimumSectionSize(25)

        self.storeOutLineStructure()
        self.runBuildItemLevelTree()
        self.treeWidget_sceneAssembleTree.doubleClicked.connect(self.editItem)
        self.pushButton_P3_deletSelectItem.clicked.connect(self.deleteSelectTreeItem)
        #self.treeWidget_sceneAssembleTree.dra
        
        ## modify treeWidget_sceneAssembleTree end----------------------------------------------------
        
        self.setFontC()
        
    def deleteSelectTreeItem(self):
        
        selectItem = self.treeWidget_sceneAssembleTree.currentItem()
        selectItemFullNameList = [selectItem.text(0)]
       # selectItem.depth()
        #checkSelectItemLen = cmds.
       # self.getFullName(selectItem)
        print self.treeWidget_sceneAssembleTree.indexOfTopLevelItem(selectItem)
        while self.treeWidget_sceneAssembleTree.indexOfTopLevelItem(selectItem) == -1:

            print selectItem.text(0)
            selectItem = selectItem.parent()
            #selectItemName = 
            selectItemFullNameList.append(selectItem.text(0).split('__')[0])

        selectItemInOutLiner = '|'.join(reversed(selectItemFullNameList))
       # print selectItemInOutLiner
      #  cmds.select(selectItemInOutLiner)
        cmds.delete(selectItemInOutLiner)
        
                
            

            #print selectItem.topLevelItem().text(0)
       # self.treeWidget_sceneAssembleTree.topLevelItem    
        '''
        if self.treeWidget_sceneAssembleTree.indexOfTopLevelItem(selectItem) == -1:
            selectItemParent = selectItem.parent()#.text(0)
            selectItemParent.removeChild(selectItem)
            cmds.delete(selectItem.text(0))
            
        else:
            print 'can not remove topLayerItem'
        '''
            
    def getFullName(self,childItem):
        
        print 'getFullName'
        if self.treeWidget_sceneAssembleTree.indexOfTopLevelItem(childItem) == -1:

            parentItem = childItem.parent()
            parentItemName = childItem.parent().text(0)
            self.selectItemFullNameLis.append(parentItemName)
        else:
            pass
            
        
    def reflashOutLinerTree(self):
        print 'reflash tree'
        self.storeItemDateInDict (3)
        #self.treeWidget_sceneAssembleTree.clear()
        self.storeOutLineStructure()
        self.runBuildItemLevelTree()
                
    def runChangeItemName(self):
        print 'runChangeItemName'
        try:
            if self.treeWidget_sceneAssembleTree.currentItem().text(0) == self.newGroupName:
                pass

            else:
                self.itemChangedName()
        except:
            pass
        
        

    def treeItemClick(self):
        print 'check 01'
        print 'treeItemClick'
        takeItem = self.treeWidget_sceneAssembleTree.currentItem()
        #print self.treeWidget_sceneAssembleTree.currentItem().text(0)
        self.getTreeLocation(takeItem)
        
    def getTreeLocation(self,takeItem):
        print 'check 02'

        print 'run getTreeLocation'
        print takeItem.text(0)#.currentColumn()
        getTopLayerIndex = self.treeWidget_sceneAssembleTree.indexOfTopLevelItem(takeItem)  # get toplayerIndex
        if getTopLayerIndex == -1:
            getParent = takeItem.parent().text(0)  
        else:
            getParent = 'none'
        print takeItem.childCount()
        print getParent
        
        
#cmds.select('aa4')
       
    def runBuildItemLevelTree(self):
        
        print 'check 03'
       # self.storeOutLineStructure()
       # self.getOutLinerStructure() 
        
        
        
        print 'start to build itemTree'
      #  self.addOutlineGroup()
       # self.storeOutLineStructure()
        self.treeWidget_sceneAssembleTree.clear()
        self.buildDefaultTopLayerItem()


        print 'build tree'
        totalIteCount = len(self.allAssetGrpDepthDict.keys())   # get how many items in self.allAssetGrpDepthDict  ，獲得outline中所有層級的名稱總數量
        self.errorItem = {'character':{'0':[]},'vehicle':{'1':[]},'set':{'2':[]},'prop':{'3':[]},'other':{'4':[]},'effect':{'5':[]}}
        for i in range(0,totalIteCount):
            
           # print i
            eachItemFullName =  self.allAssetGrpDepthDict.keys()[i]        #獲得每個層級group名稱,fullName 完整名稱
            eachItemShortName = eachItemFullName.split('|')[-1]
            eachItemDepthList = self.allAssetGrpDepthDict[self.allAssetGrpDepthDict.keys()[i]] #獲得每個層級group 所對應的層級List
            eachItemFullDepth = len(eachItemDepthList) #獲得物件所在層級， 每個物件的總層級

            topLayerItemIndex = int(eachItemDepthList[0])
            topLayerItemSelect = self.treeWidget_sceneAssembleTree.topLevelItem(topLayerItemIndex)
            parentItem = topLayerItemSelect
            parentItemForSetName = topLayerItemSelect
            
            

            for depth in range(1,eachItemFullDepth):
               # print 'depth',depth
                currentCount = parentItem.childCount()

                maxCount = int(eachItemDepthList[depth])+1

                placeIndex = int(eachItemDepthList[depth])

                delta = maxCount - currentCount

                if delta <= 0:

                    parentItem = parentItem.child(placeIndex)

                else:
                    self.createChildItem(delta,currentCount,parentItem,eachItemShortName)
                
                #try:
                    parentItem = self.childItem.parent().child(placeIndex)   #回傳在第幾個分支
            moreThanOne = 0
            self.checkIsMoreThanOne(eachItemShortName)
          #  print 'moreThanOne',self.moreThanOne
           # 
            self.defineItemAddress(parentItemForSetName,eachItemDepthList,eachItemShortName,topLayerItemSelect,topLayerItemIndex)

        print self.errorItem
        self.changeTopLayerItemName()
        
        
        
    def changeTopLayerItemName(self):
        print 'check 04'

        for i in range(0,len(self.errorItem.keys())):
         
            print self.errorItem[self.errorItem.keys()[i]]#.keys()[0]#,self.errorItem[self.errorItem.keys()[i]]
            topLayerItem = self.treeWidget_sceneAssembleTree.topLevelItem(i)
            errorCount = len(self.errorItem[topLayerItem.text(0)][self.errorItem[topLayerItem.text(0)].keys()[0]])
            newTopLayerItemName = topLayerItem.text(0) +'__('+str(errorCount)+')'
            print newTopLayerItemName
           # print topLayerItem.text(0)
            topLayerItem.setText(0,newTopLayerItemName)
            
        
        
        #self.treeWidget_sceneAssembleTree.itemChanged.connect(self.itemChangedName)

           # print self.errorItem[topLayerItem.text(0)][self.errorItem[topLayerItem.text(0)].keys()[0]]
        
        
    def checkIsMoreThanOne(self,eachItemShortName):
        print 'check 05'
        
       # print 'checkIsMoreThanOne' 
        checkList = cmds.ls(eachItemShortName)
      #  print checkList
        if len(checkList) >1 :
            self.moreThanOne = 1
        else:
            self.moreThanOne = 0
       # return moreThanOne
       # print moreThanOne errorCount
            

            
    def defineItemAddress(self,parentItemForSetName,eachItemDepthList,eachItemShortName,topLayerItemSelect,topLayerItemIndex):  #定義物件的位置，如果是有重複名稱的物件會顯示紅色
        print 'check 06'

        depthLength = len(eachItemDepthList)
        itemSelect = parentItemForSetName
        for childIndex in range(1,depthLength):

        
            itemSelect = itemSelect.child(int(eachItemDepthList[childIndex]))

        itemSelect.setText(0,eachItemShortName)
        if self.moreThanOne == 0:
            pass
        else:
            itemTypeColor = self.typeListAllowDict['moreThanOneItemTheSameName']
            itemSelect.setForeground(0,QtGui.QBrush(QtGui.QColor(int(itemTypeColor[0]), int(itemTypeColor[1]), int(itemTypeColor[2]))))#.setFont(0,self.fontLevelThree)
           # print itemSelect.topLayerItem()
           # print self.treeWidget_sceneAssembleTree.topLevelWidget(itemSelect)
          #  print 'topLayerItem',topLayerItemSelect.text(0),topLayerItemIndex
            self.errorItem[topLayerItemSelect.text(0)][self.errorItem[topLayerItemSelect.text(0)].keys()[0]].append(eachItemShortName)
            
            
            
    def buildDefaultTopLayerItem(self):
        print 'check 07'

        defaultTopLayerItem = ['character','vehicle','set','prop','other','effect']
        for i in defaultTopLayerItem:
            #itemName = defaultTopLayerItem[i]
            topLayerItem = QtWidgets.QTreeWidgetItem(self.treeWidget_sceneAssembleTree) 
            topLayerItem.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

            topLayerItem.setText(0,'%s'%i)
    
     
    def createChildItem(self,delta,currentCount,parentItem,eachItemShortName):   # maxCount 為該層級需要創建幾個物件
        print 'check 08'


        for i in range(0,delta):
            
            self.childItem =  QtWidgets.QTreeWidgetItem(parentItem)
            self.childItem.setText(0,eachItemShortName)

 

    def getOutLinerStructure(self,searchAsset):
        print 'check 09'

        tempBuildDefaultGrpList = []
        tempBuildDefaultGrpList.append(searchAsset)


        countList= []
                    
        allInTransformGrp = cmds.listRelatives(searchAsset, children=True, pa=True,ad=True)

        if allInTransformGrp == None:
            pass
        else:
            for j in allInTransformGrp:
                grpLingName =  cmds.ls(j,l=True)[0]
                tempBuildDefaultGrpList.append(grpLingName)
                countList.append(len(grpLingName.split('|')))
                        
        maxDepth = sorted(countList)[-1]-1
        elementEveryLevelCount = {}
        itemHierarchy = {}
        depthDict = {}

        for i in range(0, maxDepth):
            depthDict.update({i:{}})
            
        for i in range(1,maxDepth):
            elementEveryLevelCount.update({i:[]})
          
        allItemReleationShipDist = {}  

            
        refChildDict = {}
        
            
        for i in tempBuildDefaultGrpList:

            refChild = cmds.listRelatives(i, children=True, pa=True,ad=0)  
            refChildList = []
            try:
                refMaxCount= len(refChild)
                for j in range(0,refMaxCount):
                    indexOfItem = refChild[j].split('|')[-1]+'.'+str(j)

                    refChildList.append(indexOfItem)
                    objNodeType = cmds.nodeType(refChild[j])
                    self.itemLevelDict.update({refChild[j].split('|')[-1]:[str(j),objNodeType]})
                refChildDict.update({i.split('|')[-1]:refChildList})
            except:
                refMaxCount = 'none'
                refChildDict.update({i.split('|')[-1]:'None'})
            refParent = cmds.listRelatives(i, children=True, p=True,ad=0) 

            refChildSerNum = []
    
    
    def getItemStructure(self,searchAsset,assetIndex):
        print 'check 10'
        
        allItemInTopLayerItem = cmds.listRelatives(searchAsset, children=True, pa=True,ad=True,f=True)
        for i in allItemInTopLayerItem:
            tempItemLevelList = [assetIndex]
            #check i not in except list
            nodeTypeExceptList= ['joint','airField','nucleus','vortexField','turbulenceField','pointEmitter','dragField','gravityField','newtonField','uniformField','volumeAxisField']
            if i in nodeTypeExceptList:
                pass
            else:
                for j in i.split('|'):
                    try:
                        getPartDepthLevel = self.itemLevelDict[j][0]  #get index of each depth level #itemLevelDict
                        tempItemLevelList.append(str(getPartDepthLevel))

                    except:
                        pass
                    
                self.allAssetGrpDepthDict.update({i:tempItemLevelList})
            
            
        




    def storeOutLineStructure(self):
        print 'check 12'
        
        
       # print 'aaaa'
        self.itemLevelDict = {}    #create empty itemLevelDict ,item dictionary
        self.allAssetGrpDepthDict = {}    #create empty dict, that reference group depth and index to each item and grp
        
        self.defaultAssetBuildDict = {'character':'0','vehicle':'1','set':'2','prop':'3','other':'4','effect':'5'}
        for i in self.defaultAssetBuildDict:
            try:
                self.getOutLinerStructure(i)
            #print i
            except:
                pass
        print 'itemLevelDict',self.itemLevelDict
        
        for i in self.defaultAssetBuildDict.keys():
            try:
                self.getItemStructure(i,self.defaultAssetBuildDict[i])
            except:
                pass
        print 'self.allAssetGrpDepthDict', self.allAssetGrpDepthDict
                
    

        
    def getOutLinerStructure(self,searchAsset):
        print 'check 13'

        tempBuildDefaultGrpList = []
        tempBuildDefaultGrpList.append(searchAsset)


        countList= []
                    
        allInTransformGrp = cmds.listRelatives(searchAsset, children=True, pa=True,ad=True)


        if allInTransformGrp == None:
            pass
        else:
            for j in allInTransformGrp:
                grpLingName =  cmds.ls(j,l=True)[0]
                tempBuildDefaultGrpList.append(grpLingName)
              #  print grpLingName
                countList.append(len(grpLingName.split('|')))
                        
        maxDepth = sorted(countList)[-1]-1
       # print 'maxDepth',maxDepth
        elementEveryLevelCount = {}
        itemHierarchy = {}
        depthDict = {}

        for i in range(0, maxDepth):
            depthDict.update({i:{}})
            
        #print depthDict
        for i in range(1,maxDepth):
            elementEveryLevelCount.update({i:[]})
          
        allItemReleationShipDist = {}  
          
        #for i in tempBuildDefaultGrpList:
        #    print i 
            
            
        refChildDict = {}
        
            
        for i in tempBuildDefaultGrpList:
           # print i
            #chaList =  i.split('|')
            refChild = cmds.listRelatives(i, children=True, pa=True,ad=0)  
            #print 'refChild',refChild,type(refChild)
            refChildList = []
            try:
                refMaxCount= len(refChild)
               # print 'refMaxCount',refMaxCount
                for j in range(0,refMaxCount):
                    indexOfItem = refChild[j].split('|')[-1]+'.'+str(j)
                    #print j ,refChild[j]
                   # print indexOfItem
                    refChildList.append(indexOfItem)
                    objNodeType = cmds.nodeType(refChild[j])
                  #  print objNodeType
                    self.itemLevelDict.update({refChild[j].split('|')[-1]:[str(j),objNodeType]})
                refChildDict.update({i.split('|')[-1]:refChildList})
            except:
                refMaxCount = 'none'
                refChildDict.update({i.split('|')[-1]:'None'})
            refParent = cmds.listRelatives(i, children=True, p=True,ad=0) 

            refChildSerNum = []
            
##--------------get info from maya group structure END ---------------------------------------------------------------------------------------------------------------------   
        
    
    

    

             


   

    def setFontC(self):
        print 'check 14'
      
        self.fontC = QtGui.QFont()
        self.fontC.setFamily("Calibri")
        self.fontC.setPointSize(10) 
        self.brushC = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        self.brushC.setStyle(QtCore.Qt.NoBrush)
        
        
  
    def addOutlineGroup(self):
        print 'check 15'
        
        
        print 'addOutlineGroup'
        currentSelectItem = self.treeWidget_sceneAssembleTree.currentItem()
        newItemTheSameNameList = []
        for i in cmds.ls(typ= 'transform'):
            #print i[0:7]
            if i[0:7] == 'newItem':
                print i
                newItemTheSameNameList.append(i)
        print 'newItemTheSameNameList',newItemTheSameNameList
        newItemTheSameNameCount  = len(newItemTheSameNameList)
        newItemName = 'newItem'+'%04d'%(newItemTheSameNameCount+1)
        print 'newItemName  '+ newItemName
       # print 'newItemTheSameNameCount', newItemTheSameNameCount

         #  cmd     
        
        if currentSelectItem.isSelected() == False:
            print 'create A new Group in TopLayer'
            allTopLayerCount = int(self.treeWidget_sceneAssembleTree.topLevelItemCount())
            print allTopLayerCount
            newItem = QtWidgets.QTreeWidgetItem(self.treeWidget_sceneAssembleTree)
            newItemInOutLine = self.treeWidget_sceneAssembleTree.topLevelItem(allTopLayerCount).setText(0, QtWidgets.QApplication.translate("MainWindow", newItemName, None, -1))
            print 'newItemInOutLine', newItemInOutLine
            #newTopLayerGroupName = self.treeWidget_sceneAssembleTree.topLevelItem(allTopLayerCount).text(0)
           # print 'newTopLayerGroupName ',newTopLayerGroupName
            if newItemName not in self.allTopLayerItemsInOutline:
                cmds.createNode('transform', n=newItemName)
                self.allTopLayerItemsInOutline.append(newItemName)
            else:
                pass
            #self.allTopLayerItemsInOutline 
        else:
            print currentSelectItem.text(0)
            print self.treeWidget_sceneAssembleTree.indexOfTopLevelItem(currentSelectItem)  #get selectItem topLayerIndex
            if self.treeWidget_sceneAssembleTree.indexOfTopLevelItem(currentSelectItem) == -1:
                print 'currentSelectItem.parent()',currentSelectItem.parent().text(0)
            else:
                pass
               # print currentSelectItem.parent()#,currentSelectItem.currentItem().parent().indexOfChild(self.treeWidget.currentItem())
            
            
        #QtWidgets.QTreeWidgetItem(self.treeWidget_filesList.topLevelItem(checkItemTopLayerIndex))#.setForeground(0,self.brushLevelThree)  #build new item from index
        
       # self.treeWidget_filesList.topLevelItem(checkItemTopLayerIndex).child(index).setForeground(0,QtGui.QBrush(QtGui.QColor(int(self.fontColor[0]), int(self.fontColor[1]), int(self.fontColor[2]))))#.setFont(0,self.fontLevelThree)
       # self.treeWidget_filesList.topLevelItem(checkItemTopLayerIndex).child(index).setText(0, QtWidgets.QApplication.translate("MainWindow", 'tempName', None, -1))
       # self.treeWidget_filesList.topLevelItem(checkItemTopLayerIndex).child(index).setText(0,showName)
       # self.treeWidget_filesList.topLevelItem(checkItemTopLayerIndex).child(index).setText(6,nodeName)
        
       # self.createAllItemsInAssembleTree()
        '''    
       # print item =currentSelectItem,currentSelectItem.text(0)
       # item.setFlags(QtCore.Qt.ItemIsSelectable)
        #if currentSelectItem.currentItem()QtCore.Qt.NoItemFlags
        #print 'selected item Name' ,currentSelectItem.currentItem().text(0)
        #print 'selected item index row',currentSelectItem.currentIndex().row()
       # print 'selected item index column',currentSelectItem.currentIndex().column()
       # print 'selected item is topLevelItem', currentSelectItem.indexOfTopLevelItem(currentSelectItem.currentItem())
       # print currentSelectItem.currentItem().parent().text(0)
       # print currentSelectItem.currentItem().parent().indexOfChild(currentSelectItem.currentItem())
        
        self.treeWidget_sceneAssembleTree.setFont(self.fontC)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_sceneAssembleTree)
       # item_0.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
        self.treeWidget_sceneAssembleTree.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "newItem", None, -1))
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_sceneAssembleTree)
       # item_0.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
        self.treeWidget_sceneAssembleTree.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "newItem", None, -1))
       # self.treeWidget_sceneAssembleTree.ed
       '''
    def changeTreeItemName(self):
        print 'check 16'
        
        
        print 'changeTreeItemName'


    def editItem(self):  ## modify item name in tree   ，修改物件名稱 doubleClick run
        print 'check 17'
        
        
        checkTopLayerIndex = self.treeWidget_sceneAssembleTree.indexOfTopLevelItem(self.treeWidget_sceneAssembleTree.currentItem())
        if checkTopLayerIndex == -1 :  # 檢查是否為第一層物件
            
            item = self.treeWidget_sceneAssembleTree.itemFromIndex(self.treeWidget_sceneAssembleTree.selectedIndexes()[0])  #get select Item Name
            self.origialGroupName = item.text(0)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsEditable)
           # self.newGroupName = self.treeWidget_sceneAssembleTree.currentItem().text(0)
          #  print self.origialGroupName
          #  self.moreThanOneList =  cmds.ls(self.newGroupName)
          #  self.moreThanOneListCount = len(self.moreThanOneList)

            
            
                

            
        else:
            print 'it count not change name'
            pass
       # self.runBuildItemLevelTree()
        self.newGroupName = self.treeWidget_sceneAssembleTree.currentItem().text(0)

        self.treeWidget_sceneAssembleTree.itemChanged.connect(self.runChangeItemName)

    def itemChangedName(self):
        print 'check 18'
        
        
        
        print 'chaned item Name'
        
       # self.newGroupName = self.treeWidget_sceneAssembleTree.currentItem().text(0)
        self.moreThanOneList =  cmds.ls(self.newGroupName)
        print 'self.moreThanOneList',self.moreThanOneList
        self.moreThanOneListCount = len(self.moreThanOneList)

        print 'self.moreThanOneListCount',self.moreThanOneListCount

        if self.moreThanOneListCount > 1:
            #tempName = self.newGroupName
            tempName = self.treeWidget_sceneAssembleTree.currentItem().text(0)
            for i in range(0,self.moreThanOneListCount): 
                self.origialGroupName = self.moreThanOneList[i]
                self.newGroupName = tempName + '_' +'%04d'%i
                print 'self.origialGroupName,self.newGroupName',self.origialGroupName,self.newGroupName
                cmds.rename(self.origialGroupName,self.newGroupName)
        else:
            
            self.newGroupName = self.treeWidget_sceneAssembleTree.currentItem().text(0)
            print 'self.origialGroupName,self.newGroupName',self.origialGroupName,self.newGroupName

            cmds.rename(self.origialGroupName,self.newGroupName)
           # except:
             #   pass
       # self.runBuildItemLevelTree()
       # self.runBuildItemLevelTree()itemChangedName


    def ttt(self):
        print 'check 19'
        
        
       # print self.treeWidget_sceneAssembleTree.currentItem().text(1)
       # print self.treeWidget_sceneAssembleTree.currentItem().text(0)
       # print self.treeWidget_sceneAssembleTree.currentItem().text(2)
      #  print self.treeWidget_sceneAssembleTree.currentItem().icon(0).name()
      #  print self.treeWidget_sceneAssembleTree.currentItem().icon(0)
        print self.treeWidget_sceneAssembleTree.currentItem().text(0)

       

            #    iconFile =QtGui.QIcon('//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/NA120B.png')
      # self.tableWidget_AssetItemList.item(row, column).setIcon(iconFile)
    def itemDropInAssembleTree(self):
        print 'check 20'
        
        
        
        #print 'drop drop dopr'
        print self.treeWidget_sceneAssembleTree.currentItem().text(0)
        #widget = QtWidgets.QTreeWidget()
        #slectFlag = self.treeWidget_sceneAssembleTree.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        #self.treeWidget_sceneAssembleTree.setSelection([QtWidgets.QTreeWidgetItem(self.itemDrag)],slectFlag)
       # self.treeWidget_sceneAssembleTree.addTopLevelItems([QtWidgets.QTreeWidgetItem(self.itemDrag)])
        #widget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
       # widget.selectAll()
       # print self.treeWidget_sceneAssembleTree.findItems(self.itemDrag,QtCore.Qt.MatchExactly,column=0)[0]

       # print self.treeWidget_sceneAssembleTree.topLevelItem(0).text(0)
       # for i in self.treeWidget_sceneAssembleTree.findItems(self.itemDrag,QtCore.Qt.MatchExactly):
      #   #   print i

        #self.treeWidget_sceneAssembleTree.      
    def dragTest(self):
        print 'check 21'
        
        #print self.treeWidget_sceneAssembleTree.currentItem
        #searchKey = self.tableWidget_AssetItemList.currentItem().text()
        selectedAssetItemColumn = self.tableWidget_AssetItemList.currentColumn()
        selectedAssetItemRow = self.tableWidget_AssetItemList.currentRow()
        searchKey = str(selectedAssetItemColumn)+'_._'+str(selectedAssetItemRow)
       # print searchKey

        data = self.tableItemListInfoDict[searchKey]
       # print data.keys()[0]
    
        #mimeData = QtCore.QMimeData()
       #     print mimeData.
       # drag = QtGui.QDrag(self)
        
        self.itemDrag = self.tableWidget_AssetItemList.currentItem().text()
        #print self.treeWidget_sceneAssembleTree.findItems(itemDrag)
       # print itemDrag
        #self.treeWidget_sceneAssembleTree.indexFromItem(itemDrag,0)
      #  print self.treeWidget_sceneAssembleTree.findItems(itemDrag,QtCore.Qt.MatchExactly)
        #self.table.findItems(
            #self.edit.text(), QtCore.Qt.MatchExactly)


        
    def test(self):
        print 'check 22'
        
        print self.pushButton_P3_processModeling.isChecked()
        print self.pushButton_P3_processTexture.isChecked()
        print self.pushButton_P3_processRigging.isChecked()
        print self.pushButton_P3_NA.isChecked()
        
    def clickProcessFilletChange(self):
        print 'check 23_0'

        self.clickAssetClass(self.assetClassSelectMode)
        
        
    
    def clickAssetFilletAll(self):
        print 'check 23_0'
        
        self.assetClassSelectMode = 'all'
        self.clickAssetClass('all')
        
    def clickAssetFilletCharacter(self):
        print 'check 23_0'
        
        self.clickAssetClass('character')
        self.assetClassSelectMode = 'character'

    def clickAssetFilletVehicle(self):
        print 'check 23_0'
        
        self.clickAssetClass('vehicle')
        self.assetClassSelectMode = 'vehicle'

    def clickAssetFilletSet(self):
        print 'check 23_0'
        
        self.clickAssetClass('set')
        self.assetClassSelectMode = 'set'

    def clickAssetFilletProps(self):
        print 'check 23_0'
        
        self.clickAssetClass('props')
        self.assetClassSelectMode = 'props'
                         
    def clickAssetFilletOther(self):
        print 'check 23_0'
        
        self.clickAssetClass('other')
               
        self.assetClassSelectMode = 'other'

    def clickAssetClass(self,classMode):
        print 'check 23'
        
        print classMode
        self.pushButton_page3_all.setChecked(False)
        self.pushButton_page3_character.setChecked(False)
        self.pushButton_page3_vehicle.setChecked(False)
        self.pushButton_page3_set.setChecked(False)
        self.pushButton_page3_props.setChecked(False)
        self.pushButton_page3_other.setChecked(False)
        
        if classMode == 'all':
            self.pushButton_page3_all.setChecked(True)
            self.allAssetClassFillet = ['character','vehicle','set','prop','other']

            
        if classMode == 'character':
            self.pushButton_page3_character.setChecked(True)    
            self.allAssetClassFillet = ['character']


        if classMode == 'vehicle':
            self.pushButton_page3_vehicle.setChecked(True)
            self.allAssetClassFillet = ['vehicle']

            
        if classMode == 'set':
            self.pushButton_page3_set.setChecked(True)            
            self.allAssetClassFillet = ['set']
     
        if classMode == 'props':
            self.pushButton_page3_props.setChecked(True)            
            self.allAssetClassFillet = ['prop']
           
        if classMode == 'other':
            self.pushButton_page3_other.setChecked(True)            
            self.allAssetClassFillet = ['other']
        
        self.loadPublishedData()    
        
        if self.currentIconSize == 'large':
            self.setLargeAssetIcon()
            
        if self.currentIconSize == 'mid':
            self.setMidAssetIcon()
            
        if self.currentIconSize == 'small':
            self.setSmallAssetIcon()
            
        if self.currentIconSize == 'text':
            self.setTextAssetMain()
            
    def showAssetMetaDataFromSelect(self):
        print 'check 24'
        
        
        print 'showAssetMetaDataFromSelect start'
        #searchKey = self.tableWidget_AssetItemList.currentItem().text()
        selectedAssetItemColumn = self.tableWidget_AssetItemList.currentColumn()
        selectedAssetItemRow = self.tableWidget_AssetItemList.currentRow()
        searchKey = str(selectedAssetItemColumn)+'_._'+str(selectedAssetItemRow)
        print searchKey

        data = self.tableItemListInfoDict[searchKey]
        print data
       # for i in data
        showItemName = 'asset Name :  %s'%data.keys()[0].split('.')[0] +'\n'
        showItemAssetType = 'asset Type : %s'%data.keys()[0].split('.')[1] +'\n'
        showItemAssetProcessNow = 'asset Progress Now : %s'%data.keys()[0].split('.')[2] +'\n'+'\n'
        showFileName = 'asset File Name : %s'%data[data.keys()[0]]['fileName'] +'\n'+'\n'
        showAssetCreator = 'asset Creator :%s'%data[data.keys()[0]]['user'] +'\n'
        filePublishTime = 'asset Publish Time :%s'%datetime.datetime.fromtimestamp(os.path.getmtime(data[data.keys()[0]]['fileName']))+'\n'

        showRibArchive = 'asset RibArchive :%s'%data[data.keys()[0]]['ribArchive']['ribArchivePath'] +'\n'
        showRibArchive = 'asset RibArchive :%s'%data[data.keys()[0]]['ribArchive']['ribArchivePath'] +'\n'
        publishTimeFromFile = str(datetime.datetime.fromtimestamp(os.path.getmtime(data[data.keys()[0]]['fileName'])))
        filePublishTime = 'asset Publish Time :%s'%publishTimeFromFile.split('.')[0]+'\n'
        iconFileName = data[data.keys()[0]]['fileIcon']
        #print filePublishTime,type(filePublishTime)
        self.checkFileSize(data[data.keys()[0]]['fileName'])
        print self.fileSize
        showAssetMayaFileSize = 'asset mayaFileSize :%s'%self.fileSize +'\n'
        
       # self.checkFileSize(data[data.keys()[0]]['fileName'])        
        showList = [showItemName,showItemAssetType,showItemAssetProcessNow,showFileName,showAssetCreator,filePublishTime,showAssetMayaFileSize,showRibArchive]
        showInPlainText = ''
        for i in showList:
            showInPlainText = showInPlainText +i
        print showInPlainText
        
        self.plainTextEdit_assetMetaData.setPlainText(showInPlainText)

        self.label_showImage_2.setGeometry(QtCore.QRect(5, 5, 200, 200))
        self.label_showImage_2.setPixmap(QtGui.QPixmap(iconFileName))



    def checkFileSize(self,fileName):
        print 'check 25'
        
        
        fileSizeBt = os.stat(fileName).st_size /1024
        if fileSizeBt < 1024:
            fileSize = str(fileSizeBt) +'KB'
        elif fileSizeBt <1024*1024:
            fileSize = '%.3f'%(fileSizeBt/1024.0) +'MB'
            
        else:
            
            fileSize='%.3f'%(fileSizeBt/1024.0/1024.0) +'GB'
        self.fileSize = fileSize
                
    def loadPublishedData(self):
        print 'check 26'
        
        
        file = '//mcd-one/3d_project/ocean_world_2016_cf/publish/global/ocean_world_2016_cf_publishAnnonce.json'
        with open(file) as data_file:    
            data = json.load(data_file)
            
       # self.allAssetClassFillet = ['character','vehicle','set','prop','other']  #allAssetClass
       
        allProcesType = ['layout','animation','lighting','effects','simulation']



        allItemDict = {}
        assetTempDict ={}
        shotTempDict = {}

        for i in self.allAssetClassFillet:
            for j in data['assets'][i].keys():
               # print 'jjjjj',j
                if len(data['assets'][i][j]) == 0:
                    assetTempDict.update({j+'.'+'not available':{}})

                else:
                    for k in data['assets'][i][j].keys():

                        
                        assetTempDict.update({j+'.'+k:data['assets'][i][j][k]['state']})

                
        for i in data['shot'].keys():  #shotName.shot.processType:{}

            for j in allProcesType:
                if len(data['shot'][i]) == 0:
                    itemKey = i +'.shot.not available'
                    shotTempDict.update({itemKey:{}})
                else:
                    itemKey = i + '.shot.'+ j

                    if j in data['shot'][i].keys():

                        shotTempDict.update({itemKey:data['shot'][i][j]['state']})
                   

        allItemDict.update(assetTempDict)
       # allItemDict.update(shotTempDict)  #if want to show shot use this line
        #print 'allItemDict',allItemDict
       
        #is 'texture','model','rigging' icon is checked
        textureTempDict = {}
        for i in allItemDict.keys():
            if i.split('.')[2] == 'texture':
                textureTempDict.update({i:allItemDict[i]})
            
        modelTempDict = {}    
        for i in allItemDict.keys():
            if i.split('.')[2] == 'model':
                modelTempDict.update({i:allItemDict[i]})
                
        riggingTempDict = {}    
        for i in allItemDict.keys():
            if i.split('.')[2] == 'rigging':
                riggingTempDict.update({i:allItemDict[i]})       
          
         
        NATempDict = {}    
        for i in allItemDict.keys():
            if i.split('.')[2] == 'not available':
                NATempDict.update({i:allItemDict[i]})       
        #print 'hjghfjg',self.pushButton_P3_processModeling.isChecked()
        
       # self.pushButton_P3_processModeling
        #print 'self.pushButton_P3_NA.isChecked()',self.pushButton_P3_NA.isChecked()
        #self.test()
            
        newItemDict={}
        if  self.pushButton_P3_processModeling.isChecked() == True:
            newItemDict.update(modelTempDict)
        if  self.pushButton_P3_processTexture.isChecked() == True:
            newItemDict.update(textureTempDict)
        if  self.pushButton_P3_processRigging.isChecked() == True:            
            newItemDict.update(riggingTempDict)
        if  self.pushButton_P3_NA.isChecked() == True:      
            newItemDict.update(NATempDict)



        self.itemDict = newItemDict
        self.totalItemCount = len(self.itemDict)
       # print 'self.itemDict',self.itemDict
       # print 'newItemDict',newItemDict
        #print sorted(newItemDict)

    def storeItemDateInDict(self,cloumnCount):
        print 'check 27'
        
        print 'storeItemDateInDict start'
        infoSearchList = ['fileName','fileIcon','gpuCache','ribArchive','user','publishTime','metaData']
        rowCount = 0
        self.tableItemListInfoDict= {}
        
        tempItemInDictList = []
        notAvailableItem = []
     #   print 'self.itemDict.keys()',self.itemDict.keys()
        for i in self.itemDict.keys():
            if i.split('.')[2] == 'not available':
                notAvailableItem.append(i)
            else:
                tempItemInDictList.append(i)
        sortedTempItemList = sorted(tempItemInDictList) + notAvailableItem

       # print 'sortedTempItemList',sortedTempItemList

        for i in range(0,self.totalItemCount ):
            self.tempInfoDictPreItem = {}

            if cloumnCount == 1:
                column = 2
                row = i
                
            else:
                column = i % cloumnCount
            
                row = i/cloumnCount *2
            
            tempKey = str(column) +'_._'+ str(row)
           # print 'tempKey',tempKey
            item = sortedTempItemList[i]
           # print 'item',item
            tempItemList = {}
            for j in infoSearchList:
                try:
                    secondItem = self.itemDict[sortedTempItemList[i]][j]
                except:
                    secondItem = {}
                tempItemList.update({j:secondItem})
               # print 'secondItem',secondItem
            self.tableItemListInfoDict.update({tempKey:{item:tempItemList}})



       # print 'self.tableItemListInfoDict',self.tableItemListInfoDict
        if cloumnCount == 1:
            rowSize = 30
            columnSize =400
            textRowSize =30

        if cloumnCount == 3:
            rowSize = 120
            columnSize =120
            textRowSize =20
 
        if cloumnCount == 4:
            rowSize = 80
            columnSize =80
            textRowSize =20

            
        if cloumnCount == 6:
            rowSize = 60
            columnSize =60
            textRowSize =20
                
        #setItemText(self,cloumnCount,rowSize,columnSize)
        self.setItemIcon(columnSize,rowSize)

        self.setItemText(cloumnCount,columnSize,textRowSize)


    def setItemIcon(self,columnSize,rowSize):
        print 'check 28'
        
        
        print 'setItemIcon start'
        #print 'self.tableItemListInfoDict',self.tableItemListInfoDict
        tempIconFileDict={}
        for i in self.tableItemListInfoDict.keys():
            row = int(i.split('_._')[1])
            column = int(i.split('_._')[0])

            if len(self.tableItemListInfoDict[i][self.tableItemListInfoDict[i].keys()[0]]['fileIcon']) == 0:
                iconFile =QtGui.QIcon('//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/NA120B.png')
            else:


                iconFile = QtGui.QIcon(self.tableItemListInfoDict[i][self.tableItemListInfoDict[i].keys()[0]]['fileIcon'])#.keys()
            item = QtWidgets.QTableWidgetItem()
            itemName = self.tableItemListInfoDict[i].keys()[0]
            item.setText(itemName)
    
            self.tableWidget_AssetItemList.setItem(row, column, item)
            self.tableWidget_AssetItemList.horizontalHeader().setDefaultSectionSize(columnSize)
            self.tableWidget_AssetItemList.verticalHeader().setDefaultSectionSize(rowSize)
            self.tableWidget_AssetItemList.item(row, column).setIcon(iconFile)
            


 
    def setItemText(self,cloumnCount,columnSize,textRowSize):
        print 'check 29'
        
        #print self.tableItemListInfoDict.keys()
        #print 'cloumnCount',cloumnCount
        for i in self.tableItemListInfoDict.keys():
           # print 'self.tableItemListInfoDict.keys()',self.tableItemListInfoDict.keys()
            if cloumnCount == 1:
                row = int(i.split('_._')[1])
                column = 0
            else:
                row = int(i.split('_._')[1])+1
                #print 'row',row
                column = int(i.split('_._')[0])
            itemName = str(self.tableItemListInfoDict[i].keys()[0]).split('.')[0]
           # print 'itemText',i,self.tableItemListInfoDict[i]
            #print itemName
            #print row ,column

            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_AssetItemList.setItem(row, column, item)
           # self.tableWidget_AssetItemList.setRowHeight(100,60) #set text row height
            # self.tableWidget_AssetItemList.setIconSize(QtCore.QSize(40,40))
            #self.tableWidget_AssetItemList.horizontalHeader().setDefaultSectionSize(columnSize)
            #self.tableWidget_AssetItemList.verticalHeader().setDefaultSectionSize(rowSize)
            self.tableWidget_AssetItemList.setRowHeight(row,textRowSize) #set text row height

            self.tableWidget_AssetItemList.item(row, column).setText(QtWidgets.QApplication.translate("MainWindow",'aaa', None,-1))
            self.tableWidget_AssetItemList.item(row, column).setText(QtWidgets.QApplication.translate("MainWindow",itemName, None,-1))
            
    def setTextMode(self):
        print 'check 30'
        
        
        self.tableWidget_AssetItemList.clear()
        
        self.pushButton_P3_largeIcon.setChecked(True) 
        self.pushButton_P3_MidIcon.setChecked(False) 
        self.pushButton_P3_smallIcon.setChecked(False) 
        self.pushButton_P3_text.setChecked(False) 
        
        setRow = self.totalItemCount +1
        self.tableWidget_AssetItemList.setColumnCount(3)
        self.tableWidget_AssetItemList.setRowCount(setRow)
        
        
        
     
    def setLargeAssetIcon(self):
        print 'check 31'
        
        self.tableWidget_AssetItemList.clear()
        
        self.pushButton_P3_largeIcon.setChecked(True) 
        self.pushButton_P3_MidIcon.setChecked(False) 
        self.pushButton_P3_smallIcon.setChecked(False) 
        self.pushButton_P3_text.setChecked(False) 
        
        
        
        print 'setLargeAssetIcon'
        self.tableWidget_AssetItemList.clear()
        
        self.pushButton_P3_largeIcon.setChecked(True) 
        self.pushButton_P3_MidIcon.setChecked(False) 
        self.pushButton_P3_smallIcon.setChecked(False) 
        self.pushButton_P3_text.setChecked(False) 
        
        if self.totalItemCount%3 == 0:
            setRow = ((self.totalItemCount / 3) *2) +1
        else: 
            setRow = ((self.totalItemCount / 3) *2) +2
            
     #   print setRow
        
        #setRow = self.totalItemCount / 2 *2 +2
        
        
        self.tableWidget_AssetItemList.setColumnCount(3)
        self.tableWidget_AssetItemList.setRowCount(setRow)
              
        #self.tableWidget_AssetItemList.horizontalHeader().setDefaultSectionSize(120)
        #self.tableWidget_AssetItemList.verticalHeader().setDefaultSectionSize(120)
        iconFile = self.iconFile
        tableItemIndex={}
        
        for column in range(0,3): #set icon 
            for row in range(0,setRow,2):

                self.createTableItem(column,row,iconFile,120)

                
        for column in range(0,3):
            for row in range(1,setRow,2):
                self.setTableItemText(column,row)
      
        self.storeItemDateInDict (3)  # create Item Dict

        self.currentIconSize = 'large'
      

    def setMidAssetIcon(self):
        print 'check 32'
        
        print 'setMidAssetIcon'
        self.tableWidget_AssetItemList.clear()

        self.pushButton_P3_largeIcon.setChecked(False) 
        self.pushButton_P3_MidIcon.setChecked(True) 
        self.pushButton_P3_smallIcon.setChecked(False) 
        self.pushButton_P3_text.setChecked(False) 
        
        if self.totalItemCount%4 == 0:
            setRow = ((self.totalItemCount / 4) *2) +1
        else: 
            setRow = ((self.totalItemCount / 4) *2) +2
            
     #   print setRow
    #    
        
        self.tableWidget_AssetItemList.setColumnCount(4)
        self.tableWidget_AssetItemList.setRowCount(setRow)
              
       # self.tableWidget_AssetItemList.horizontalHeader().setDefaultSectionSize(80)
       # self.tableWidget_AssetItemList.verticalHeader().setDefaultSectionSize(80)
        iconFile = self.iconFile
        
        for column in range(0,4): #set icon setItemText
            for row in range(0,setRow,2):
              #  print row
                self.createTableItem(column,row,iconFile,80)
                
        for column in range(0,4):
            for row in range(1,setRow,2):
             #   print row
                self.setTableItemText(column,row)
                
        self.storeItemDateInDict (4)
        
        self.currentIconSize = 'mid'
 
        
        
    def setSmallAssetIcon(self):
        print 'check 33'
        
        print 'setSmallAssetIcon'
        self.tableWidget_AssetItemList.clear()

        self.pushButton_P3_largeIcon.setChecked(False) 
        self.pushButton_P3_MidIcon.setChecked(False) 
        self.pushButton_P3_smallIcon.setChecked(True) 
        self.pushButton_P3_text.setChecked(False)  
        if self.totalItemCount%6 == 0:
            setRow = ((self.totalItemCount / 6) *2) +1
        else: 
            setRow = ((self.totalItemCount / 6) *2) +2
            
      #  print setRow
        
        
        self.tableWidget_AssetItemList.setColumnCount(6)
        self.tableWidget_AssetItemList.setRowCount(setRow)
              
       # self.tableWidget_AssetItemList.horizontalHeader().setDefaultSectionSize(60)
       # self.tableWidget_AssetItemList.verticalHeader().setDefaultSectionSize(60)
        iconFile = self.iconFile
        
        for column in range(0,6): #set icon 
            for row in range(0,setRow,2):
                self.createTableItem(column,row,iconFile,60)
                
        for column in range(0,6):
            for row in range(1,setRow,2):
             #   print row
                self.setTableItemText(column,row)
        self.storeItemDateInDict (6)
        self.currentIconSize = 'small'
        

    def setTextAssetMain(self):
        print 'check 34'
        
        self.setTextAsset(30)
                
        
    def setTextAsset(self,size):
        print 'check 35'
        
        print 'setTextAsset~~'
        self.tableWidget_AssetItemList.clear()

        self.pushButton_P3_largeIcon.setChecked(False) 
        self.pushButton_P3_MidIcon.setChecked(False) 
        self.pushButton_P3_smallIcon.setChecked(False) 
        self.pushButton_P3_text.setChecked(True) 
        setRow = self.totalItemCount #+ 1
        self.tableWidget_AssetItemList.setColumnCount(3)
        self.tableWidget_AssetItemList.setRowCount(setRow)  
        self.storeItemDateInDict(1)
      #  print 'self.tableItemListInfoDict',self.tableItemListInfoDict.keys()
        iconFile =self.iconFile
        for row in range(0, setRow):
            item = QtWidgets.QTableWidgetItem()

            self.tableWidget_AssetItemList.setColumnWidth(0,size)     #index ser number
            self.tableWidget_AssetItemList.setRowHeight(row , size) #set text row height
            self.tableWidget_AssetItemList.setItem(row, 0, item)
            self.tableWidget_AssetItemList.item(row, 0).setText(QtWidgets.QApplication.translate("MainWindow", "serNum", None,-1))
            self.tableWidget_AssetItemList.item(row, 0).setText(QtWidgets.QApplication.translate("MainWindow", str(row), None,-1))

            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_AssetItemList.setColumnWidth(1,size)     #index ser number
            
            self.tableWidget_AssetItemList.setRowHeight(row , size) #set text row height
            self.tableWidget_AssetItemList.setItem(row, 1, item)
            self.tableWidget_AssetItemList.item(row, 1).setIcon(iconFile)
             

            item = QtWidgets.QTableWidgetItem()


            self.tableWidget_AssetItemList.setColumnWidth(2,300)     #index ser number
            
           # self.tableWidget_AssetItemList.setRowHeight(row , size) #set text row height
            self.tableWidget_AssetItemList.setItem(row, 2, item)
            self.tableWidget_AssetItemList.item(row, 2).setText(QtWidgets.QApplication.translate("MainWindow", "icon", None,-1))


        for i in self.tableItemListInfoDict.keys()  :
            row = int(i.split('_._')[1])
            self.tableWidget_AssetItemList.setRowHeight(row , size) #set text row height

            itemName = str(self.tableItemListInfoDict[i].keys()[0])
            
            self.tableWidget_AssetItemList.item(row, 2).setText(QtWidgets.QApplication.translate("MainWindow", itemName, None,-1))

 
        for i in self.tableItemListInfoDict.keys()  :
            row = int(i.split('_._')[1])

     
            itemIconFile = str(self.tableItemListInfoDict[i][self.tableItemListInfoDict[i].keys()[0]]['fileIcon'])
          #  itemIconFile='//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/NA120B.png'
            if len(itemIconFile) == 2:
               # print 'itemIconFile','not available'
                itemIconFile = '//mcd-one/database/assets/scripts/maya_scripts/icons/publishToolIcon/NA120B.png'
                self.tableWidget_AssetItemList.item(row, 1).setIcon(QtGui.QIcon(itemIconFile))
                self.tableWidget_AssetItemList.setIconSize(QtCore.QSize(size,size))

                pass
            else:
               # print 'itemIconFile'itemIconFile
               # print 'itemIconFile',itemIconFile
                self.tableWidget_AssetItemList.item(row, 1).setIcon(QtGui.QIcon(itemIconFile))

                self.tableWidget_AssetItemList.setIconSize(QtCore.QSize(size,size))
            
            
            
       # for row in range(0, setRow):
       #     item = QtWidgets.QTableWidgetItem()

       #     self.tableWidget_AssetItemList.setColumnWidth(3,size)     #index ser number
       #     self.tableWidget_AssetItemList.setRowHeight(row , size)
            
            
        self.currentIconSize = 'text'

        
        
        
                                    
        
    def initialTableWidgetAssetList(self):
        print 'check 36'
        
        self.tableWidget_AssetItemList.clear()
        #self.tableWidget_AssetItemList.setRowCount(2)
        #self.tableWidget_AssetItemList.setColumnCount(2)

        self.tableWidget_AssetItemList.setColumnCount(3)
        self.tableWidget_AssetItemList.setRowCount(4)
      
        self.tableWidget_AssetItemList.horizontalHeader().setDefaultSectionSize(60)
        self.tableWidget_AssetItemList.verticalHeader().setDefaultSectionSize(60)


    def createTableItem(self,column,row,iconFile,iconSize):
        print 'check 37'
        

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_AssetItemList.setItem(row, column, item)
        self.tableWidget_AssetItemList.item(row, column).setText(QtWidgets.QApplication.translate("MainWindow", "ItemIconHere", None,-1))

        self.tableWidget_AssetItemList.item(row, column).setIcon(iconFile)
        self.tableWidget_AssetItemList.setIconSize(QtCore.QSize(iconSize,iconSize))

        
    def createItemB(self,column,row,iconFile):
        print 'check 38'
        
       # icon = QtGui.QIcon("C:/Program Files/Autodesk/Maya2017/icons/publishToolIcon/animation.png")
        #iconFile = QtGui.QIcon("C:/Program Files/Autodesk/Maya2017/icons/publishToolIcon/animation.png")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_AssetItemList.setItem(row, column, item)
        #self.tableWidget_AssetItemList.item(row, column).setText(QtWidgets.QApplication.translate("MainWindow", "ItemIcon", None,-1))
        self.tableWidget_AssetItemList.item(row, column).setIcon(iconFile)
        self.tableWidget_AssetItemList.setIconSize(QtCore.QSize(60,60))
       # self.tableWidget.item(1, 2).setIconText('aaa')
       # item.

        # add text Item
    def setTableItemText(self,column,row):
        print 'check 39'
        
        item = QtWidgets.QTableWidgetItem()
       # textRow = row+1
        self.tableWidget_AssetItemList.setRowHeight(row , 20) #set text row height
        self.tableWidget_AssetItemList.setItem(row, column, item)
       # self.tableWidget_AssetItemList.setIconSize(QtCore.QSize(40,40))
        self.tableWidget_AssetItemList.item(row, column).setText(QtWidgets.QApplication.translate("MainWindow", "ItemName", None,-1))
        #item.setTextAlignment(-20)

      #  self.tableWidget.setRowHeight(1 , 20)  

             
      


def main():
    global ui
    app = QtWidgets.QApplication.instance()
    if app == None: app = QtWidgets.QApplication(sys.argv)
    try:
        ui.close()
        ui.deleteLater()
    except: pass
    ui = mod_MainWindow()
    ui.show()
 
if __name__ == '__main__':
    main()


 
 