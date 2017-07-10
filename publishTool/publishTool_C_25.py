# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha/Documents/GitHub/ribGen/publishTool/createbranchtest_01.ui'
#
# Created: Fri Mar 17 00:34:42 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!
#C:/Program Files/Autodesk/Maya2017/C:/Program Files/Autodesk/Maya2017/icons/
from PySide2 import QtCore, QtGui, QtWidgets
import maya.cmds as cmds
import json , os , getpass,socket ,ctypes.wintypes ,subprocess
from pprint import pprint
import ctypes.wintypes
import sys
import pymel.core as pm
from shutil import copyfile


import datetime

try:
    pm.mel.eval('rmanLoadPlugin')
    rendermanPath = pm.mel.eval('getenv RMANTREE')
    pythonScriptPath = rendermanPath + 'lib/python2.7/Lib/site-packages'
    sys.path.append(pythonScriptPath)
    import ice

except:
    print 'pls import prman plugin'
    pass


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.setFontSize=8
        #setPointSize(self.setFontSize) = setPointSize(self.setFontSize +3)
        #setPointSize(self.setFontSize +3) = setPointSize(self.setFontSize +2)
        #setPointSize(8 ) = setPointSize(self.setFontSize) 

        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(650, 860)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(650, 860))
        MainWindow.setMaximumSize(QtCore.QSize(2000, 2000))
        MainWindow.setSizeIncrement(QtCore.QSize(650, 860))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        MainWindow.setPalette(palette)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setAcceptDrops(False)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget_branch = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_branch.setEnabled(True)
        self.tabWidget_branch.setGeometry(QtCore.QRect(5, 17, 1226, 946))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_branch.sizePolicy().hasHeightForWidth())
        self.tabWidget_branch.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.tabWidget_branch.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.tabWidget_branch.setFont(font)
        self.tabWidget_branch.setAutoFillBackground(True)
        self.tabWidget_branch.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget_branch.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget_branch.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget_branch.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget_branch.setDocumentMode(True)
        self.tabWidget_branch.setTabsClosable(False)
        self.tabWidget_branch.setMovable(False)
        self.tabWidget_branch.setTabBarAutoHide(False)
        self.tabWidget_branch.setObjectName("tabWidget_branch")
        self.tab_branch = QtWidgets.QWidget()
        self.tab_branch.setObjectName("tab_branch")
        self.frame_5 = QtWidgets.QFrame(self.tab_branch)
        self.frame_5.setGeometry(QtCore.QRect(850, 450, 46, 56))
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
        self.frame_11 = QtWidgets.QFrame(self.tab_branch)
        self.frame_11.setGeometry(QtCore.QRect(0, 0, 578, 56))
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
        self.comboBox_selectProj = QtWidgets.QComboBox(self.frame_11)
        self.comboBox_selectProj.setGeometry(QtCore.QRect(190, 25, 211, 22))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 226, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(92, 99, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 132, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 226, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 226, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(92, 99, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 132, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 226, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(92, 99, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 226, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(92, 99, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 132, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(92, 99, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(92, 99, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 198, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.comboBox_selectProj.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_selectProj.setFont(font)
        self.comboBox_selectProj.setObjectName("comboBox_selectProj")
        self.comboBox_selectProj.addItem("")
        self.pushButton_recent = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_recent.setEnabled(True)
        self.pushButton_recent.setGeometry(QtCore.QRect(55, 20, 30, 30))
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
        self.pushButton_recent.setPalette(palette)
        self.pushButton_recent.setAutoFillBackground(False)
        self.pushButton_recent.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/projSelect_recentB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/projSelect_recentA.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_recent.setIcon(icon)
        self.pushButton_recent.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_recent.setCheckable(True)
        self.pushButton_recent.setChecked(False)
        self.pushButton_recent.setAutoRepeat(False)
        self.pushButton_recent.setAutoExclusive(False)
        self.pushButton_recent.setAutoDefault(False)
        self.pushButton_recent.setDefault(False)
        self.pushButton_recent.setFlat(True)
        self.pushButton_recent.setObjectName("pushButton_recent")
        self.pushButton_complete = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_complete.setEnabled(True)
        self.pushButton_complete.setGeometry(QtCore.QRect(115, 20, 30, 30))
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
        self.pushButton_complete.setPalette(palette)
        self.pushButton_complete.setAutoFillBackground(False)
        self.pushButton_complete.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/projSelect_completeB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/projSelect_completeA.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_complete.setIcon(icon1)
        self.pushButton_complete.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_complete.setCheckable(True)
        self.pushButton_complete.setChecked(False)
        self.pushButton_complete.setAutoRepeat(False)
        self.pushButton_complete.setAutoExclusive(False)
        self.pushButton_complete.setAutoDefault(False)
        self.pushButton_complete.setDefault(False)
        self.pushButton_complete.setFlat(True)
        self.pushButton_complete.setObjectName("pushButton_complete")
        self.pushButton_inProgress = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_inProgress.setEnabled(True)
        self.pushButton_inProgress.setGeometry(QtCore.QRect(10, 20, 30, 30))
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
        self.pushButton_inProgress.setPalette(palette)
        self.pushButton_inProgress.setAutoFillBackground(False)
        self.pushButton_inProgress.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/projSelect_inProgressB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/projSelect_inProgressA.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_inProgress.setIcon(icon2)
        self.pushButton_inProgress.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_inProgress.setCheckable(True)
        self.pushButton_inProgress.setChecked(False)
        self.pushButton_inProgress.setAutoRepeat(False)
        self.pushButton_inProgress.setAutoExclusive(False)
        self.pushButton_inProgress.setAutoDefault(False)
        self.pushButton_inProgress.setDefault(False)
        self.pushButton_inProgress.setFlat(True)
        self.pushButton_inProgress.setObjectName("pushButton_inProgress")
        self.pushButton_reNewBranchDict = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_reNewBranchDict.setGeometry(QtCore.QRect(535, 20, 31, 31))
        self.pushButton_reNewBranchDict.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/wrench2-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_reNewBranchDict.setIcon(icon3)
        self.pushButton_reNewBranchDict.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_reNewBranchDict.setAutoDefault(False)
        self.pushButton_reNewBranchDict.setDefault(False)
        self.pushButton_reNewBranchDict.setFlat(True)
        self.pushButton_reNewBranchDict.setObjectName("pushButton_reNewBranchDict")
        self.pushButton_setting = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_setting.setGeometry(QtCore.QRect(505, 20, 31, 31))
        self.pushButton_setting.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/gear2-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_setting.setIcon(icon4)
        self.pushButton_setting.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_setting.setAutoDefault(False)
        self.pushButton_setting.setDefault(False)
        self.pushButton_setting.setFlat(True)
        self.pushButton_setting.setObjectName("pushButton_setting")
        self.pushButton_syncFile = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_syncFile.setGeometry(QtCore.QRect(445, 20, 31, 31))
        self.pushButton_syncFile.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/radial_arrows2-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_syncFile.setIcon(icon5)
        self.pushButton_syncFile.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_syncFile.setAutoDefault(False)
        self.pushButton_syncFile.setDefault(False)
        self.pushButton_syncFile.setFlat(True)
        self.pushButton_syncFile.setObjectName("pushButton_syncFile")
        self.pushButton_buildFolder = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_buildFolder.setGeometry(QtCore.QRect(415, 20, 31, 31))
        self.pushButton_buildFolder.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/masterB2-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_buildFolder.setIcon(icon6)
        self.pushButton_buildFolder.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_buildFolder.setAutoDefault(False)
        self.pushButton_buildFolder.setDefault(False)
        self.pushButton_buildFolder.setFlat(True)
        self.pushButton_buildFolder.setObjectName("pushButton_buildFolder")
        self.label_fileData_29 = QtWidgets.QLabel(self.frame_11)
        self.label_fileData_29.setGeometry(QtCore.QRect(415, 0, 30, 20))
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
        self.label_fileData_29.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_29.setFont(font)
        self.label_fileData_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_29.setObjectName("label_fileData_29")
        self.label_fileData_36 = QtWidgets.QLabel(self.frame_11)
        self.label_fileData_36.setGeometry(QtCore.QRect(10, 0, 30, 20))
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
        self.label_fileData_36.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_36.setFont(font)
        self.label_fileData_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_36.setObjectName("label_fileData_36")
        self.label_fileData_37 = QtWidgets.QLabel(self.frame_11)
        self.label_fileData_37.setGeometry(QtCore.QRect(47, 0, 46, 20))
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
        self.label_fileData_37.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_37.setFont(font)
        self.label_fileData_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_37.setObjectName("label_fileData_37")
        self.label_fileData_38 = QtWidgets.QLabel(self.frame_11)
        self.label_fileData_38.setGeometry(QtCore.QRect(100, 0, 56, 20))
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
        self.label_fileData_38.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_38.setFont(font)
        self.label_fileData_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_38.setObjectName("label_fileData_38")
        self.label_fileData_47 = QtWidgets.QLabel(self.frame_11)
        self.label_fileData_47.setGeometry(QtCore.QRect(190, 0, 116, 20))
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
        self.label_fileData_47.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_47.setFont(font)
        self.label_fileData_47.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_47.setObjectName("label_fileData_47")
        self.frame_12 = QtWidgets.QFrame(self.tab_branch)
        self.frame_12.setGeometry(QtCore.QRect(0, 60, 636, 746))
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
        self.frame_12.setPalette(palette)
        self.frame_12.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setLineWidth(1)
        self.frame_12.setMidLineWidth(0)
        self.frame_12.setObjectName("frame_12")
        self.frame_10 = QtWidgets.QFrame(self.frame_12)
        self.frame_10.setGeometry(QtCore.QRect(580, 475, 51, 261))
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
        self.label_fileData_33 = QtWidgets.QLabel(self.frame_10)
        self.label_fileData_33.setGeometry(QtCore.QRect(10, 5, 31, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 170, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 170, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 170, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.label_fileData_33.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_33.setFont(font)
        self.label_fileData_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_33.setObjectName("label_fileData_33")
        self.pushButton_openFolder = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_openFolder.setEnabled(True)
        self.pushButton_openFolder.setGeometry(QtCore.QRect(5, 95, 40, 40))
        self.pushButton_openFolder.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/view-details-60.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_openFolder.setIcon(icon7)
        self.pushButton_openFolder.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_openFolder.setCheckable(True)
        self.pushButton_openFolder.setAutoDefault(False)
        self.pushButton_openFolder.setDefault(False)
        self.pushButton_openFolder.setFlat(True)
        self.pushButton_openFolder.setObjectName("pushButton_openFolder")
        self.pushButton_editFileInfo = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_editFileInfo.setEnabled(True)
        self.pushButton_editFileInfo.setGeometry(QtCore.QRect(5, 25, 40, 40))
        self.pushButton_editFileInfo.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/pencil_and_paper-60.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_editFileInfo.setIcon(icon8)
        self.pushButton_editFileInfo.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_editFileInfo.setCheckable(True)
        self.pushButton_editFileInfo.setAutoDefault(False)
        self.pushButton_editFileInfo.setDefault(False)
        self.pushButton_editFileInfo.setFlat(True)
        self.pushButton_editFileInfo.setObjectName("pushButton_editFileInfo")
        self.label_fileData_46 = QtWidgets.QLabel(self.frame_10)
        self.label_fileData_46.setGeometry(QtCore.QRect(10, 75, 31, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 170, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 170, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 170, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.label_fileData_46.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_46.setFont(font)
        self.label_fileData_46.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_46.setObjectName("label_fileData_46")
        self.frame = QtWidgets.QFrame(self.frame_12)
        self.frame.setGeometry(QtCore.QRect(225, 5, 353, 56))
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
        self.pushButton_processSimulation = QtWidgets.QPushButton(self.frame)
        self.pushButton_processSimulation.setEnabled(True)
        self.pushButton_processSimulation.setGeometry(QtCore.QRect(300, 20, 21, 30))
        self.pushButton_processSimulation.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/simulation_3Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon9.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/simulation_3Open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_processSimulation.setIcon(icon9)
        self.pushButton_processSimulation.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_processSimulation.setCheckable(True)
        self.pushButton_processSimulation.setAutoDefault(False)
        self.pushButton_processSimulation.setDefault(False)
        self.pushButton_processSimulation.setFlat(True)
        self.pushButton_processSimulation.setObjectName("pushButton_processSimulation")
        self.pushButton_processAnimation = QtWidgets.QPushButton(self.frame)
        self.pushButton_processAnimation.setEnabled(True)
        self.pushButton_processAnimation.setGeometry(QtCore.QRect(210, 20, 30, 30))
        self.pushButton_processAnimation.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/animation_3Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon10.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/animation_3Open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_processAnimation.setIcon(icon10)
        self.pushButton_processAnimation.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_processAnimation.setCheckable(True)
        self.pushButton_processAnimation.setAutoDefault(False)
        self.pushButton_processAnimation.setDefault(False)
        self.pushButton_processAnimation.setFlat(True)
        self.pushButton_processAnimation.setObjectName("pushButton_processAnimation")
        self.pushButton_processEffects = QtWidgets.QPushButton(self.frame)
        self.pushButton_processEffects.setEnabled(True)
        self.pushButton_processEffects.setGeometry(QtCore.QRect(270, 20, 30, 30))
        self.pushButton_processEffects.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/effect_3Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon11.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/effect_3Open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_processEffects.setIcon(icon11)
        self.pushButton_processEffects.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_processEffects.setCheckable(True)
        self.pushButton_processEffects.setAutoDefault(False)
        self.pushButton_processEffects.setDefault(False)
        self.pushButton_processEffects.setFlat(True)
        self.pushButton_processEffects.setObjectName("pushButton_processEffects")
        self.pushButton_processLighting = QtWidgets.QPushButton(self.frame)
        self.pushButton_processLighting.setEnabled(True)
        self.pushButton_processLighting.setGeometry(QtCore.QRect(240, 20, 30, 30))
        self.pushButton_processLighting.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/lighting_3Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon12.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/lighting_3Open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_processLighting.setIcon(icon12)
        self.pushButton_processLighting.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_processLighting.setCheckable(True)
        self.pushButton_processLighting.setAutoDefault(False)
        self.pushButton_processLighting.setDefault(False)
        self.pushButton_processLighting.setFlat(True)
        self.pushButton_processLighting.setObjectName("pushButton_processLighting")
        self.pushButton_processLayout = QtWidgets.QPushButton(self.frame)
        self.pushButton_processLayout.setEnabled(True)
        self.pushButton_processLayout.setGeometry(QtCore.QRect(180, 20, 30, 30))
        self.pushButton_processLayout.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/layout_3Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon13.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/layout_3Open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_processLayout.setIcon(icon13)
        self.pushButton_processLayout.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_processLayout.setCheckable(True)
        self.pushButton_processLayout.setAutoDefault(False)
        self.pushButton_processLayout.setDefault(False)
        self.pushButton_processLayout.setFlat(True)
        self.pushButton_processLayout.setObjectName("pushButton_processLayout")
        self.pushButton_processRigging = QtWidgets.QPushButton(self.frame)
        self.pushButton_processRigging.setEnabled(True)
        self.pushButton_processRigging.setGeometry(QtCore.QRect(95, 20, 30, 30))
        self.pushButton_processRigging.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/rigging_3Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon14.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/rigging_3Open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_processRigging.setIcon(icon14)
        self.pushButton_processRigging.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_processRigging.setCheckable(True)
        self.pushButton_processRigging.setAutoDefault(False)
        self.pushButton_processRigging.setDefault(False)
        self.pushButton_processRigging.setFlat(True)
        self.pushButton_processRigging.setObjectName("pushButton_processRigging")
        self.pushButton_processTexture = QtWidgets.QPushButton(self.frame)
        self.pushButton_processTexture.setEnabled(True)
        self.pushButton_processTexture.setGeometry(QtCore.QRect(65, 20, 30, 30))
        self.pushButton_processTexture.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/texture_3Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon15.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/texture_3Open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_processTexture.setIcon(icon15)
        self.pushButton_processTexture.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_processTexture.setCheckable(True)
        self.pushButton_processTexture.setAutoDefault(False)
        self.pushButton_processTexture.setDefault(False)
        self.pushButton_processTexture.setFlat(True)
        self.pushButton_processTexture.setObjectName("pushButton_processTexture")
        self.pushButton_processConcept = QtWidgets.QPushButton(self.frame)
        self.pushButton_processConcept.setGeometry(QtCore.QRect(5, 20, 30, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_processConcept.sizePolicy().hasHeightForWidth())
        self.pushButton_processConcept.setSizePolicy(sizePolicy)
        self.pushButton_processConcept.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/concept_3Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon16.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/concept3_open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_processConcept.setIcon(icon16)
        self.pushButton_processConcept.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_processConcept.setCheckable(True)
        self.pushButton_processConcept.setAutoDefault(False)
        self.pushButton_processConcept.setDefault(False)
        self.pushButton_processConcept.setFlat(True)
        self.pushButton_processConcept.setObjectName("pushButton_processConcept")
        self.pushButton_processModeling = QtWidgets.QPushButton(self.frame)
        self.pushButton_processModeling.setEnabled(True)
        self.pushButton_processModeling.setGeometry(QtCore.QRect(35, 20, 30, 30))
        self.pushButton_processModeling.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/modeling_3Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon17.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/modeling_3Open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_processModeling.setIcon(icon17)
        self.pushButton_processModeling.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_processModeling.setCheckable(True)
        self.pushButton_processModeling.setAutoDefault(False)
        self.pushButton_processModeling.setDefault(False)
        self.pushButton_processModeling.setFlat(True)
        self.pushButton_processModeling.setObjectName("pushButton_processModeling")
        self.label_fileData_9 = QtWidgets.QLabel(self.frame)
        self.label_fileData_9.setGeometry(QtCore.QRect(300, 0, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_9.setFont(font)
        self.label_fileData_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_9.setObjectName("label_fileData_9")
        self.label_fileData = QtWidgets.QLabel(self.frame)
        self.label_fileData.setGeometry(QtCore.QRect(10, 0, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData.setFont(font)
        self.label_fileData.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData.setObjectName("label_fileData")
        self.label_fileData_4 = QtWidgets.QLabel(self.frame)
        self.label_fileData_4.setGeometry(QtCore.QRect(100, 0, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_4.setFont(font)
        self.label_fileData_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_4.setObjectName("label_fileData_4")
        self.label_fileData_3 = QtWidgets.QLabel(self.frame)
        self.label_fileData_3.setGeometry(QtCore.QRect(70, 0, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_3.setFont(font)
        self.label_fileData_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_3.setObjectName("label_fileData_3")
        self.label_fileData_8 = QtWidgets.QLabel(self.frame)
        self.label_fileData_8.setGeometry(QtCore.QRect(270, 0, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_8.setFont(font)
        self.label_fileData_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_8.setObjectName("label_fileData_8")
        self.label_fileData_7 = QtWidgets.QLabel(self.frame)
        self.label_fileData_7.setGeometry(QtCore.QRect(240, 0, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_7.setFont(font)
        self.label_fileData_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_7.setObjectName("label_fileData_7")
        self.label_fileData_2 = QtWidgets.QLabel(self.frame)
        self.label_fileData_2.setGeometry(QtCore.QRect(40, 0, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_2.setFont(font)
        self.label_fileData_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_2.setObjectName("label_fileData_2")
        self.label_fileData_5 = QtWidgets.QLabel(self.frame)
        self.label_fileData_5.setGeometry(QtCore.QRect(180, 0, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_5.setFont(font)
        self.label_fileData_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_5.setObjectName("label_fileData_5")
        self.label_fileData_6 = QtWidgets.QLabel(self.frame)
        self.label_fileData_6.setGeometry(QtCore.QRect(210, 0, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_6.setFont(font)
        self.label_fileData_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_6.setObjectName("label_fileData_6")
        self.frame_4 = QtWidgets.QFrame(self.frame_12)
        self.frame_4.setGeometry(QtCore.QRect(10, 65, 46, 56))
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
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/shotS5Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon18.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/shotS5Open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_shot.setIcon(icon18)
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
        self.frame_6 = QtWidgets.QFrame(self.frame_12)
        self.frame_6.setGeometry(QtCore.QRect(60, 65, 518, 406))
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
        self.lineEdit_currentFileName = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_currentFileName.setGeometry(QtCore.QRect(162, 370, 353, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.lineEdit_currentFileName.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.lineEdit_currentFileName.setFont(font)
        self.lineEdit_currentFileName.setObjectName("lineEdit_currentFileName")
        self.treeWidget_branches = QtWidgets.QTreeWidget(self.frame_6)
        self.treeWidget_branches.setEnabled(True)
        self.treeWidget_branches.setGeometry(QtCore.QRect(162, 35, 353, 178))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.treeWidget_branches.setPalette(palette)
        self.treeWidget_branches.setAlternatingRowColors(False)
        self.treeWidget_branches.setAutoExpandDelay(1)
        self.treeWidget_branches.setAllColumnsShowFocus(True)
        self.treeWidget_branches.setHeaderHidden(True)
        self.treeWidget_branches.setExpandsOnDoubleClick(True)
        self.treeWidget_branches.setObjectName("treeWidget_branches")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_branches)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        brush = QtGui.QBrush(QtGui.QColor(247, 126, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        item_0.setForeground(0, brush)
        self.treeWidget_branches.header().setVisible(False)
        self.treeWidget_branches.header().setCascadingSectionResizes(False)
        self.treeWidget_branches.header().setDefaultSectionSize(311)
        self.treeWidget_branches.header().setMinimumSectionSize(4)
        self.treeWidget_branches.header().setSortIndicatorShown(False)
        self.treeWidget_branches.header().setStretchLastSection(False)
        self.lineEdit_branchName = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_branchName.setGeometry(QtCore.QRect(162, 4, 353, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.lineEdit_branchName.setPalette(palette)
        self.lineEdit_branchName.setText("")
        self.lineEdit_branchName.setObjectName("lineEdit_branchName")
        self.tableWidget_FileList = QtWidgets.QTableWidget(self.frame_6)
        self.tableWidget_FileList.setGeometry(QtCore.QRect(162, 215, 353, 156))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 34, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 51, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 42, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(11, 17, 15))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(15, 22, 20))
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
        brush = QtGui.QBrush(QtGui.QColor(23, 34, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 43, 38))
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
        brush = QtGui.QBrush(QtGui.QColor(23, 34, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 51, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 42, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(11, 17, 15))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(15, 22, 20))
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
        brush = QtGui.QBrush(QtGui.QColor(23, 34, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 43, 38))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(11, 17, 15))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 34, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 51, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 42, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(11, 17, 15))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(15, 22, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(11, 17, 15))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(11, 17, 15))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 34, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 34, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 43, 38))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.tableWidget_FileList.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableWidget_FileList.setFont(font)
        self.tableWidget_FileList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget_FileList.setAutoScrollMargin(16)
        self.tableWidget_FileList.setAlternatingRowColors(True)
        self.tableWidget_FileList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_FileList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_FileList.setObjectName("tableWidget_FileList")
        self.tableWidget_FileList.setColumnCount(3)
        self.tableWidget_FileList.setRowCount(15)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setHorizontalHeaderItem(2, item)
        brush = QtGui.QBrush(QtGui.QColor(192, 231, 248))
        brush.setStyle(QtCore.Qt.NoBrush)
        item = QtWidgets.QTableWidgetItem()
        item.setForeground(brush)
        self.tableWidget_FileList.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setItem(8, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setItem(9, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setItem(10, 1, item)
        self.tableWidget_FileList.horizontalHeader().setVisible(False)
        self.tableWidget_FileList.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_FileList.horizontalHeader().setDefaultSectionSize(60)
        self.tableWidget_FileList.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_FileList.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_FileList.verticalHeader().setVisible(False)
        self.tableWidget_FileList.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_FileList.verticalHeader().setDefaultSectionSize(21)
        self.listWidget_assetProj = QtWidgets.QListWidget(self.frame_6)
        self.listWidget_assetProj.setGeometry(QtCore.QRect(5, 5, 155, 396))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.listWidget_assetProj.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.listWidget_assetProj.setFont(font)
        self.listWidget_assetProj.setObjectName("listWidget_assetProj")
        QtWidgets.QListWidgetItem(self.listWidget_assetProj)
        QtWidgets.QListWidgetItem(self.listWidget_assetProj)
        QtWidgets.QListWidgetItem(self.listWidget_assetProj)
        QtWidgets.QListWidgetItem(self.listWidget_assetProj)
        QtWidgets.QListWidgetItem(self.listWidget_assetProj)
        QtWidgets.QListWidgetItem(self.listWidget_assetProj)
        QtWidgets.QListWidgetItem(self.listWidget_assetProj)
        QtWidgets.QListWidgetItem(self.listWidget_assetProj)
        QtWidgets.QListWidgetItem(self.listWidget_assetProj)
        QtWidgets.QListWidgetItem(self.listWidget_assetProj)
        self.frame_2 = QtWidgets.QFrame(self.frame_12)
        self.frame_2.setGeometry(QtCore.QRect(60, 5, 161, 56))
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
        self.frame_2.setPalette(palette)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(1)
        self.frame_2.setMidLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_others = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_others.setEnabled(True)
        self.pushButton_others.setGeometry(QtCore.QRect(130, 20, 21, 30))
        self.pushButton_others.setText("")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/otherS5Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon19.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/otherS5Open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_others.setIcon(icon19)
        self.pushButton_others.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_others.setCheckable(True)
        self.pushButton_others.setAutoDefault(False)
        self.pushButton_others.setDefault(False)
        self.pushButton_others.setFlat(True)
        self.pushButton_others.setObjectName("pushButton_others")
        self.pushButton_vehicle = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_vehicle.setEnabled(True)
        self.pushButton_vehicle.setGeometry(QtCore.QRect(40, 20, 30, 30))
        self.pushButton_vehicle.setText("")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/vehS5Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon20.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/vehS5_open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_vehicle.setIcon(icon20)
        self.pushButton_vehicle.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_vehicle.setCheckable(True)
        self.pushButton_vehicle.setAutoDefault(False)
        self.pushButton_vehicle.setDefault(False)
        self.pushButton_vehicle.setFlat(True)
        self.pushButton_vehicle.setObjectName("pushButton_vehicle")
        self.pushButton_character = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_character.setEnabled(True)
        self.pushButton_character.setGeometry(QtCore.QRect(10, 20, 30, 30))
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
        self.pushButton_character.setPalette(palette)
        self.pushButton_character.setAutoFillBackground(False)
        self.pushButton_character.setText("")
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/chaS5Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon21.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/chaS5Open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_character.setIcon(icon21)
        self.pushButton_character.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_character.setCheckable(True)
        self.pushButton_character.setChecked(False)
        self.pushButton_character.setAutoRepeat(False)
        self.pushButton_character.setAutoExclusive(False)
        self.pushButton_character.setAutoDefault(False)
        self.pushButton_character.setDefault(False)
        self.pushButton_character.setFlat(True)
        self.pushButton_character.setObjectName("pushButton_character")
        self.pushButton_set = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_set.setEnabled(True)
        self.pushButton_set.setGeometry(QtCore.QRect(70, 16, 30, 30))
        self.pushButton_set.setText("")
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/setS5Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon22.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/setS5Open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_set.setIcon(icon22)
        self.pushButton_set.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_set.setCheckable(True)
        self.pushButton_set.setAutoDefault(False)
        self.pushButton_set.setDefault(False)
        self.pushButton_set.setFlat(True)
        self.pushButton_set.setObjectName("pushButton_set")
        self.pushButton_props = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_props.setEnabled(True)
        self.pushButton_props.setGeometry(QtCore.QRect(100, 18, 30, 30))
        self.pushButton_props.setText("")
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/propsS5Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon23.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/propsS5Open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_props.setIcon(icon23)
        self.pushButton_props.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_props.setCheckable(True)
        self.pushButton_props.setAutoDefault(False)
        self.pushButton_props.setDefault(False)
        self.pushButton_props.setFlat(True)
        self.pushButton_props.setObjectName("pushButton_props")
        self.label_fileData_15 = QtWidgets.QLabel(self.frame_2)
        self.label_fileData_15.setGeometry(QtCore.QRect(135, 0, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_15.setFont(font)
        self.label_fileData_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_15.setObjectName("label_fileData_15")
        self.label_fileData_12 = QtWidgets.QLabel(self.frame_2)
        self.label_fileData_12.setGeometry(QtCore.QRect(45, 0, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_12.setFont(font)
        self.label_fileData_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_12.setObjectName("label_fileData_12")
        self.label_fileData_11 = QtWidgets.QLabel(self.frame_2)
        self.label_fileData_11.setGeometry(QtCore.QRect(15, 0, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_11.setFont(font)
        self.label_fileData_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_11.setObjectName("label_fileData_11")
        self.label_fileData_13 = QtWidgets.QLabel(self.frame_2)
        self.label_fileData_13.setGeometry(QtCore.QRect(75, 0, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_13.setFont(font)
        self.label_fileData_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_13.setObjectName("label_fileData_13")
        self.label_fileData_14 = QtWidgets.QLabel(self.frame_2)
        self.label_fileData_14.setGeometry(QtCore.QRect(105, 0, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_14.setFont(font)
        self.label_fileData_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_14.setObjectName("label_fileData_14")
        self.frame_3 = QtWidgets.QFrame(self.frame_12)
        self.frame_3.setGeometry(QtCore.QRect(10, 5, 46, 56))
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
        self.frame_3.setPalette(palette)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setLineWidth(1)
        self.frame_3.setMidLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_all = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_all.setEnabled(True)
        self.pushButton_all.setGeometry(QtCore.QRect(10, 20, 25, 25))
        self.pushButton_all.setText("")
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/AllS5close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon24.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/AllS5Open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_all.setIcon(icon24)
        self.pushButton_all.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_all.setCheckable(True)
        self.pushButton_all.setAutoDefault(False)
        self.pushButton_all.setDefault(False)
        self.pushButton_all.setFlat(True)
        self.pushButton_all.setObjectName("pushButton_all")
        self.label_fileData_10 = QtWidgets.QLabel(self.frame_3)
        self.label_fileData_10.setGeometry(QtCore.QRect(14, 0, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_10.setFont(font)
        self.label_fileData_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_10.setObjectName("label_fileData_10")
        self.frame_9 = QtWidgets.QFrame(self.frame_12)
        self.frame_9.setGeometry(QtCore.QRect(580, 100, 51, 371))
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
        self.pushButton_openBranchJson = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_openBranchJson.setEnabled(True)
        self.pushButton_openBranchJson.setGeometry(QtCore.QRect(5, 93, 40, 40))
        self.pushButton_openBranchJson.setText("")
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/option2-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_openBranchJson.setIcon(icon25)
        self.pushButton_openBranchJson.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_openBranchJson.setCheckable(True)
        self.pushButton_openBranchJson.setAutoDefault(False)
        self.pushButton_openBranchJson.setDefault(False)
        self.pushButton_openBranchJson.setFlat(True)
        self.pushButton_openBranchJson.setObjectName("pushButton_openBranchJson")
        self.label_fileData_26 = QtWidgets.QLabel(self.frame_9)
        self.label_fileData_26.setGeometry(QtCore.QRect(10, 12, 26, 17))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 170, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 170, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 170, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.label_fileData_26.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_26.setFont(font)
        self.label_fileData_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_26.setObjectName("label_fileData_26")
        self.pushButton_createNewBranch = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_createNewBranch.setEnabled(True)
        self.pushButton_createNewBranch.setGeometry(QtCore.QRect(5, 33, 40, 40))
        self.pushButton_createNewBranch.setText("")
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/newBranch2-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_createNewBranch.setIcon(icon26)
        self.pushButton_createNewBranch.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_createNewBranch.setCheckable(True)
        self.pushButton_createNewBranch.setAutoDefault(False)
        self.pushButton_createNewBranch.setDefault(False)
        self.pushButton_createNewBranch.setFlat(True)
        self.pushButton_createNewBranch.setObjectName("pushButton_createNewBranch")
        self.label_fileData_30 = QtWidgets.QLabel(self.frame_9)
        self.label_fileData_30.setGeometry(QtCore.QRect(10, 75, 31, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 170, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 170, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 170, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.label_fileData_30.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_30.setFont(font)
        self.label_fileData_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_30.setObjectName("label_fileData_30")
        self.pushButton_loadFile = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_loadFile.setEnabled(True)
        self.pushButton_loadFile.setGeometry(QtCore.QRect(5, 295, 40, 40))
        self.pushButton_loadFile.setText("")
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/load60.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_loadFile.setIcon(icon27)
        self.pushButton_loadFile.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_loadFile.setCheckable(True)
        self.pushButton_loadFile.setAutoDefault(False)
        self.pushButton_loadFile.setDefault(False)
        self.pushButton_loadFile.setFlat(True)
        self.pushButton_loadFile.setObjectName("pushButton_loadFile")
        self.pushButton_saveFile = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_saveFile.setEnabled(True)
        self.pushButton_saveFile.setGeometry(QtCore.QRect(5, 235, 40, 40))
        self.pushButton_saveFile.setText("")
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/save60.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_saveFile.setIcon(icon28)
        self.pushButton_saveFile.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_saveFile.setCheckable(True)
        self.pushButton_saveFile.setAutoDefault(False)
        self.pushButton_saveFile.setDefault(False)
        self.pushButton_saveFile.setFlat(True)
        self.pushButton_saveFile.setObjectName("pushButton_saveFile")
        self.label_fileData_32 = QtWidgets.QLabel(self.frame_9)
        self.label_fileData_32.setGeometry(QtCore.QRect(8, 275, 31, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 170, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 170, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 170, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.label_fileData_32.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_32.setFont(font)
        self.label_fileData_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_32.setObjectName("label_fileData_32")
        self.label_fileData_31 = QtWidgets.QLabel(self.frame_9)
        self.label_fileData_31.setGeometry(QtCore.QRect(8, 215, 31, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 170, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 170, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 170, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.label_fileData_31.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_31.setFont(font)
        self.label_fileData_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_31.setObjectName("label_fileData_31")
        self.pushButton_mergeToMaster = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_mergeToMaster.setEnabled(True)
        self.pushButton_mergeToMaster.setGeometry(QtCore.QRect(5, 155, 40, 40))
        self.pushButton_mergeToMaster.setText("")
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/merge2-60.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_mergeToMaster.setIcon(icon29)
        self.pushButton_mergeToMaster.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_mergeToMaster.setCheckable(True)
        self.pushButton_mergeToMaster.setAutoDefault(False)
        self.pushButton_mergeToMaster.setDefault(False)
        self.pushButton_mergeToMaster.setFlat(True)
        self.pushButton_mergeToMaster.setObjectName("pushButton_mergeToMaster")
        self.label_fileData_45 = QtWidgets.QLabel(self.frame_9)
        self.label_fileData_45.setGeometry(QtCore.QRect(10, 135, 31, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 170, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 170, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 170, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 127, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.label_fileData_45.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_45.setFont(font)
        self.label_fileData_45.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_45.setObjectName("label_fileData_45")
        self.frame_8 = QtWidgets.QFrame(self.frame_12)
        self.frame_8.setGeometry(QtCore.QRect(222, 475, 356, 261))
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
        self.plainTextEdit_BranchFileInfo = QtWidgets.QPlainTextEdit(self.frame_8)
        self.plainTextEdit_BranchFileInfo.setGeometry(QtCore.QRect(4, 2, 349, 256))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.plainTextEdit_BranchFileInfo.setPalette(palette)
        self.plainTextEdit_BranchFileInfo.setObjectName("plainTextEdit_BranchFileInfo")
        self.frame_7 = QtWidgets.QFrame(self.frame_12)
        self.frame_7.setGeometry(QtCore.QRect(10, 475, 211, 201))
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
        self.label_showImage = QtWidgets.QLabel(self.frame_7)
        self.label_showImage.setGeometry(QtCore.QRect(5, 7, 196, 186))
        self.label_showImage.setText("")
        self.label_showImage.setPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/picture-01-150.png"))
        self.label_showImage.setObjectName("label_showImage")
        self.frame_13 = QtWidgets.QFrame(self.frame_12)
        self.frame_13.setGeometry(QtCore.QRect(10, 125, 46, 346))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
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
        brush = QtGui.QBrush(QtGui.QColor(67, 100, 90))
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
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
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
        brush = QtGui.QBrush(QtGui.QColor(67, 100, 90))
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
        brush = QtGui.QBrush(QtGui.QColor(67, 100, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(67, 100, 90))
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
        self.frame_13.setPalette(palette)
        self.frame_13.setAutoFillBackground(True)
        self.frame_13.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setLineWidth(1)
        self.frame_13.setMidLineWidth(0)
        self.frame_13.setObjectName("frame_13")
        self.pushButton_uploadSync = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_uploadSync.setEnabled(True)
        self.pushButton_uploadSync.setGeometry(QtCore.QRect(130, 690, 40, 40))
        self.pushButton_uploadSync.setText("")
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/Live_Sync_D60.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_uploadSync.setIcon(icon30)
        self.pushButton_uploadSync.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_uploadSync.setCheckable(True)
        self.pushButton_uploadSync.setAutoDefault(False)
        self.pushButton_uploadSync.setDefault(False)
        self.pushButton_uploadSync.setFlat(True)
        self.pushButton_uploadSync.setObjectName("pushButton_uploadSync")
        self.pushButton_uploadPublish = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_uploadPublish.setEnabled(True)
        self.pushButton_uploadPublish.setGeometry(QtCore.QRect(175, 690, 40, 40))
        self.pushButton_uploadPublish.setText("")
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/uploadPublishC_60.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_uploadPublish.setIcon(icon31)
        self.pushButton_uploadPublish.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_uploadPublish.setCheckable(True)
        self.pushButton_uploadPublish.setAutoDefault(False)
        self.pushButton_uploadPublish.setDefault(False)
        self.pushButton_uploadPublish.setFlat(True)
        self.pushButton_uploadPublish.setObjectName("pushButton_uploadPublish")
        self.pushButton_gotPublish = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_gotPublish.setEnabled(False)
        self.pushButton_gotPublish.setGeometry(QtCore.QRect(585, 10, 41, 46))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_gotPublish.sizePolicy().hasHeightForWidth())
        self.pushButton_gotPublish.setSizePolicy(sizePolicy)
        self.pushButton_gotPublish.setText("")
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/emoji-32-512C3.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon32.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/emoji-32-512C4.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon32.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/emoji-32-512C4.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon32.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/emoji-32-512C3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon32.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/emoji-32-512C3.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon32.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/emoji-32-512D2.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon32.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/emoji-32-512C3.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        icon32.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/emoji-32-512C3.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_gotPublish.setIcon(icon32)
        self.pushButton_gotPublish.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_gotPublish.setCheckable(True)
        self.pushButton_gotPublish.setAutoRepeatDelay(5)
        self.pushButton_gotPublish.setAutoRepeatInterval(5)
        self.pushButton_gotPublish.setAutoDefault(False)
        self.pushButton_gotPublish.setDefault(True)
        self.pushButton_gotPublish.setFlat(False)
        self.pushButton_gotPublish.setObjectName("pushButton_gotPublish")
        self.frame_24 = QtWidgets.QFrame(self.frame_12)
        self.frame_24.setGeometry(QtCore.QRect(580, 65, 50, 30))
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
        self.frame_24.setPalette(palette)
        self.frame_24.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setLineWidth(1)
        self.frame_24.setMidLineWidth(0)
        self.frame_24.setObjectName("frame_24")
        self.pushButton_gotoPublishFolder = QtWidgets.QPushButton(self.frame_24)
        self.pushButton_gotoPublishFolder.setEnabled(True)
        self.pushButton_gotoPublishFolder.setGeometry(QtCore.QRect(6, 4, 36, 21))
        self.pushButton_gotoPublishFolder.setText("")
        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/gotoA.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_gotoPublishFolder.setIcon(icon33)
        self.pushButton_gotoPublishFolder.setIconSize(QtCore.QSize(48, 28))
        self.pushButton_gotoPublishFolder.setCheckable(True)
        self.pushButton_gotoPublishFolder.setAutoDefault(False)
        self.pushButton_gotoPublishFolder.setDefault(False)
        self.pushButton_gotoPublishFolder.setFlat(True)
        self.pushButton_gotoPublishFolder.setObjectName("pushButton_gotoPublishFolder")
        self.frame_14 = QtWidgets.QFrame(self.tab_branch)
        self.frame_14.setGeometry(QtCore.QRect(705, 650, 46, 161))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
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
        brush = QtGui.QBrush(QtGui.QColor(67, 100, 90))
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
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
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
        brush = QtGui.QBrush(QtGui.QColor(67, 100, 90))
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
        brush = QtGui.QBrush(QtGui.QColor(67, 100, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(67, 100, 90))
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
        self.frame_14.setPalette(palette)
        self.frame_14.setAutoFillBackground(True)
        self.frame_14.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setLineWidth(1)
        self.frame_14.setMidLineWidth(0)
        self.frame_14.setObjectName("frame_14")
        self.label_fileData_34 = QtWidgets.QLabel(self.tab_branch)
        self.label_fileData_34.setGeometry(QtCore.QRect(950, 125, 51, 20))
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
        self.label_fileData_34.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_34.setFont(font)
        self.label_fileData_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_34.setObjectName("label_fileData_34")
        self.label_fileData_28 = QtWidgets.QLabel(self.tab_branch)
        self.label_fileData_28.setGeometry(QtCore.QRect(790, 125, 41, 20))
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
        self.label_fileData_28.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_28.setFont(font)
        self.label_fileData_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_28.setObjectName("label_fileData_28")
        self.frame_21 = QtWidgets.QFrame(self.tab_branch)
        self.frame_21.setGeometry(QtCore.QRect(580, 0, 56, 56))
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
        self.pushButton_changePageA = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_changePageA.setEnabled(True)
        self.pushButton_changePageA.setGeometry(QtCore.QRect(2, 3, 25, 25))
        self.pushButton_changePageA.setText("")
        icon34 = QtGui.QIcon()
        icon34.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/connerA.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_changePageA.setIcon(icon34)
        self.pushButton_changePageA.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_changePageA.setCheckable(True)
        self.pushButton_changePageA.setAutoDefault(False)
        self.pushButton_changePageA.setDefault(False)
        self.pushButton_changePageA.setFlat(True)
        self.pushButton_changePageA.setObjectName("pushButton_changePageA")
        self.pushButton_changePageB = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_changePageB.setEnabled(True)
        self.pushButton_changePageB.setGeometry(QtCore.QRect(27, 3, 25, 25))
        self.pushButton_changePageB.setText("")
        icon35 = QtGui.QIcon()
        icon35.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/connerB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_changePageB.setIcon(icon35)
        self.pushButton_changePageB.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_changePageB.setCheckable(True)
        self.pushButton_changePageB.setAutoDefault(False)
        self.pushButton_changePageB.setDefault(False)
        self.pushButton_changePageB.setFlat(True)
        self.pushButton_changePageB.setObjectName("pushButton_changePageB")
        self.pushButton_changePageC = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_changePageC.setEnabled(True)
        self.pushButton_changePageC.setGeometry(QtCore.QRect(2, 28, 25, 25))
        self.pushButton_changePageC.setText("")
        icon36 = QtGui.QIcon()
        icon36.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/connerC.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_changePageC.setIcon(icon36)
        self.pushButton_changePageC.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_changePageC.setCheckable(True)
        self.pushButton_changePageC.setAutoDefault(False)
        self.pushButton_changePageC.setDefault(False)
        self.pushButton_changePageC.setFlat(True)
        self.pushButton_changePageC.setObjectName("pushButton_changePageC")
        self.pushButton_changePageD = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_changePageD.setEnabled(True)
        self.pushButton_changePageD.setGeometry(QtCore.QRect(27, 28, 25, 25))
        self.pushButton_changePageD.setText("")
        icon37 = QtGui.QIcon()
        icon37.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/connerD.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_changePageD.setIcon(icon37)
        self.pushButton_changePageD.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_changePageD.setCheckable(True)
        self.pushButton_changePageD.setAutoDefault(False)
        self.pushButton_changePageD.setDefault(False)
        self.pushButton_changePageD.setFlat(True)
        self.pushButton_changePageD.setObjectName("pushButton_changePageD")
        self.pushButton_publishAll_topPage = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_publishAll_topPage.setGeometry(QtCore.QRect(260, 855, 150, 75))
        self.pushButton_publishAll_topPage.setText("")
        icon38 = QtGui.QIcon()
        icon38.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/eggA.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_publishAll_topPage.setIcon(icon38)
        self.pushButton_publishAll_topPage.setIconSize(QtCore.QSize(150, 75))
        self.pushButton_publishAll_topPage.setFlat(True)
        self.pushButton_publishAll_topPage.setObjectName("pushButton_publishAll_topPage")
        self.tabWidget_branch.addTab(self.tab_branch, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.frame_15 = QtWidgets.QFrame(self.tab)
        self.frame_15.setGeometry(QtCore.QRect(0, 60, 636, 746))
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
        self.treeWidget_filesList = QtWidgets.QTreeWidget(self.frame_15)
        self.treeWidget_filesList.setGeometry(QtCore.QRect(5, 34, 440, 396))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_filesList.sizePolicy().hasHeightForWidth())
        self.treeWidget_filesList.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 134, 134))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 111, 111))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 59, 59))
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
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 44, 44))
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
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 134, 134))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 111, 111))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 59, 59))
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
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 134, 134))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 111, 111))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 59, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.treeWidget_filesList.setPalette(palette)
        self.treeWidget_filesList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget_filesList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget_filesList.setAutoScrollMargin(16)
        self.treeWidget_filesList.setAlternatingRowColors(True)
        self.treeWidget_filesList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.treeWidget_filesList.setTextElideMode(QtCore.Qt.ElideRight)
        self.treeWidget_filesList.setIndentation(20)
        self.treeWidget_filesList.setRootIsDecorated(True)
        self.treeWidget_filesList.setUniformRowHeights(False)
        self.treeWidget_filesList.setItemsExpandable(True)
        self.treeWidget_filesList.setAllColumnsShowFocus(False)
        self.treeWidget_filesList.setWordWrap(True)
        self.treeWidget_filesList.setExpandsOnDoubleClick(True)
        self.treeWidget_filesList.setColumnCount(2)
        self.treeWidget_filesList.setObjectName("treeWidget_filesList")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_filesList)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_filesList)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_filesList)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_filesList)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_filesList)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_filesList)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_filesList)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_filesList)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_filesList)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_filesList)
        self.treeWidget_filesList.header().setVisible(False)
        self.treeWidget_filesList.header().setCascadingSectionResizes(False)
        self.treeWidget_filesList.header().setDefaultSectionSize(250)
        self.treeWidget_filesList.header().setHighlightSections(True)
        self.treeWidget_filesList.header().setMinimumSectionSize(15)
        self.treeWidget_filesList.header().setSortIndicatorShown(False)
        self.lineEdit_showFileName = QtWidgets.QLineEdit(self.frame_15)
        self.lineEdit_showFileName.setGeometry(QtCore.QRect(5, 3, 440, 31))
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
        self.lineEdit_showFileName.setPalette(palette)
        self.lineEdit_showFileName.setObjectName("lineEdit_showFileName")
        self.treeWidget_FiletOption = QtWidgets.QTreeWidget(self.frame_15)
        self.treeWidget_FiletOption.setGeometry(QtCore.QRect(449, 5, 181, 436))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
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
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
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
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
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
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
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
        self.treeWidget_FiletOption.setPalette(palette)
        self.treeWidget_FiletOption.setAutoFillBackground(True)
        self.treeWidget_FiletOption.setAutoExpandDelay(-1)
        self.treeWidget_FiletOption.setIndentation(11)
        self.treeWidget_FiletOption.setItemsExpandable(True)
        self.treeWidget_FiletOption.setAllColumnsShowFocus(False)
        self.treeWidget_FiletOption.setExpandsOnDoubleClick(True)
        self.treeWidget_FiletOption.setObjectName("treeWidget_FiletOption")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_FiletOption)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_FiletOption)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_FiletOption)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_FiletOption)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.treeWidget_FiletOption.header().setVisible(False)
        self.treeWidget_FiletOption.header().setMinimumSectionSize(27)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame_15)
        self.plainTextEdit.setGeometry(QtCore.QRect(5, 445, 440, 291))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.plainTextEdit.setPalette(palette)
        self.plainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.frame_16 = QtWidgets.QFrame(self.frame_15)
        self.frame_16.setGeometry(QtCore.QRect(450, 445, 181, 161))
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
        self.frame_16.setPalette(palette)
        self.frame_16.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setLineWidth(1)
        self.frame_16.setMidLineWidth(0)
        self.frame_16.setObjectName("frame_16")
        self.lineEdit_reduceSizeCustomer = QtWidgets.QLineEdit(self.frame_16)
        self.lineEdit_reduceSizeCustomer.setEnabled(False)
        self.lineEdit_reduceSizeCustomer.setGeometry(QtCore.QRect(105, 120, 66, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
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
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
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
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
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
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
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
        self.lineEdit_reduceSizeCustomer.setPalette(palette)
        self.lineEdit_reduceSizeCustomer.setObjectName("lineEdit_reduceSizeCustomer")
        self.pushButton_convertToPng = QtWidgets.QPushButton(self.frame_16)
        self.pushButton_convertToPng.setGeometry(QtCore.QRect(90, 10, 40, 40))
        self.pushButton_convertToPng.setText("")
        icon39 = QtGui.QIcon()
        icon39.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/PNG-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_convertToPng.setIcon(icon39)
        self.pushButton_convertToPng.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_convertToPng.setFlat(True)
        self.pushButton_convertToPng.setObjectName("pushButton_convertToPng")
        self.pushButton_convertToJpg = QtWidgets.QPushButton(self.frame_16)
        self.pushButton_convertToJpg.setGeometry(QtCore.QRect(130, 10, 40, 40))
        self.pushButton_convertToJpg.setText("")
        icon40 = QtGui.QIcon()
        icon40.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/jpgs-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_convertToJpg.setIcon(icon40)
        self.pushButton_convertToJpg.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_convertToJpg.setFlat(True)
        self.pushButton_convertToJpg.setObjectName("pushButton_convertToJpg")
        self.radioButton_customer = QtWidgets.QRadioButton(self.frame_16)
        self.radioButton_customer.setGeometry(QtCore.QRect(10, 125, 111, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.radioButton_customer.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.radioButton_customer.setFont(font)
        self.radioButton_customer.setChecked(False)
        self.radioButton_customer.setObjectName("radioButton_customer")
        self.pushButton_convertToTex = QtWidgets.QPushButton(self.frame_16)
        self.pushButton_convertToTex.setGeometry(QtCore.QRect(10, 10, 40, 40))
        self.pushButton_convertToTex.setText("")
        icon41 = QtGui.QIcon()
        icon41.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/TEX-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_convertToTex.setIcon(icon41)
        self.pushButton_convertToTex.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_convertToTex.setFlat(True)
        self.pushButton_convertToTex.setObjectName("pushButton_convertToTex")
        self.pushButton_convertToExr = QtWidgets.QPushButton(self.frame_16)
        self.pushButton_convertToExr.setGeometry(QtCore.QRect(50, 10, 40, 40))
        self.pushButton_convertToExr.setText("")
        icon42 = QtGui.QIcon()
        icon42.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/EXR-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_convertToExr.setIcon(icon42)
        self.pushButton_convertToExr.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_convertToExr.setFlat(True)
        self.pushButton_convertToExr.setObjectName("pushButton_convertToExr")
        self.radioButton_Half = QtWidgets.QRadioButton(self.frame_16)
        self.radioButton_Half.setGeometry(QtCore.QRect(10, 85, 83, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.radioButton_Half.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.radioButton_Half.setFont(font)
        self.radioButton_Half.setChecked(False)
        self.radioButton_Half.setObjectName("radioButton_Half")
        self.radioButton_Quarter = QtWidgets.QRadioButton(self.frame_16)
        self.radioButton_Quarter.setGeometry(QtCore.QRect(10, 105, 83, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.radioButton_Quarter.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.radioButton_Quarter.setFont(font)
        self.radioButton_Quarter.setChecked(False)
        self.radioButton_Quarter.setObjectName("radioButton_Quarter")
        self.radioButton_Original = QtWidgets.QRadioButton(self.frame_16)
        self.radioButton_Original.setGeometry(QtCore.QRect(10, 65, 83, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.radioButton_Original.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.radioButton_Original.setFont(font)
        self.radioButton_Original.setChecked(True)
        self.radioButton_Original.setObjectName("radioButton_Original")
        self.pushButton_replaceFileRoot = QtWidgets.QPushButton(self.frame_15)
        self.pushButton_replaceFileRoot.setEnabled(True)
        self.pushButton_replaceFileRoot.setGeometry(QtCore.QRect(585, 700, 30, 30))
        self.pushButton_replaceFileRoot.setText("")
        icon43 = QtGui.QIcon()
        icon43.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/replaceRoot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_replaceFileRoot.setIcon(icon43)
        self.pushButton_replaceFileRoot.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_replaceFileRoot.setFlat(True)
        self.pushButton_replaceFileRoot.setObjectName("pushButton_replaceFileRoot")
        self.lineEdit_file_sources = QtWidgets.QLineEdit(self.frame_15)
        self.lineEdit_file_sources.setEnabled(True)
        self.lineEdit_file_sources.setGeometry(QtCore.QRect(455, 670, 121, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
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
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
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
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
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
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
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
        self.lineEdit_file_sources.setPalette(palette)
        self.lineEdit_file_sources.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_file_sources.setObjectName("lineEdit_file_sources")
        self.lineEdit_file_sources_2 = QtWidgets.QLineEdit(self.frame_15)
        self.lineEdit_file_sources_2.setEnabled(True)
        self.lineEdit_file_sources_2.setGeometry(QtCore.QRect(455, 700, 121, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
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
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
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
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
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
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
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
        self.lineEdit_file_sources_2.setPalette(palette)
        self.lineEdit_file_sources_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_file_sources_2.setObjectName("lineEdit_file_sources_2")
        self.progressBar = QtWidgets.QProgressBar(self.frame_15)
        self.progressBar.setGeometry(QtCore.QRect(5, 431, 440, 11))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(213, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 255, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(213, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 255, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(213, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 255, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.progressBar.setPalette(palette)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.frame_17 = QtWidgets.QFrame(self.tab)
        self.frame_17.setGeometry(QtCore.QRect(0, 0, 446, 56))
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
        self.frame_17.setPalette(palette)
        self.frame_17.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setLineWidth(1)
        self.frame_17.setMidLineWidth(0)
        self.frame_17.setObjectName("frame_17")
        self.pushButton_getSelectedNode = QtWidgets.QPushButton(self.frame_17)
        self.pushButton_getSelectedNode.setGeometry(QtCore.QRect(60, 15, 35, 35))
        self.pushButton_getSelectedNode.setText("")
        icon44 = QtGui.QIcon()
        icon44.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/getSelectItemPublishB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_getSelectedNode.setIcon(icon44)
        self.pushButton_getSelectedNode.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_getSelectedNode.setFlat(True)
        self.pushButton_getSelectedNode.setObjectName("pushButton_getSelectedNode")
        self.pushButton_refreshList = QtWidgets.QPushButton(self.frame_17)
        self.pushButton_refreshList.setGeometry(QtCore.QRect(15, 15, 35, 35))
        self.pushButton_refreshList.setText("")
        icon45 = QtGui.QIcon()
        icon45.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/refreshPublishB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_refreshList.setIcon(icon45)
        self.pushButton_refreshList.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_refreshList.setFlat(True)
        self.pushButton_refreshList.setObjectName("pushButton_refreshList")
        self.pushButton_reName = QtWidgets.QPushButton(self.frame_17)
        self.pushButton_reName.setGeometry(QtCore.QRect(195, 20, 30, 30))
        self.pushButton_reName.setText("")
        icon46 = QtGui.QIcon()
        icon46.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/reNameB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_reName.setIcon(icon46)
        self.pushButton_reName.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_reName.setFlat(True)
        self.pushButton_reName.setObjectName("pushButton_reName")
        self.pushButton_unCheckAll = QtWidgets.QPushButton(self.frame_17)
        self.pushButton_unCheckAll.setGeometry(QtCore.QRect(145, 20, 30, 30))
        self.pushButton_unCheckAll.setText("")
        icon47 = QtGui.QIcon()
        icon47.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/unCheckB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_unCheckAll.setIcon(icon47)
        self.pushButton_unCheckAll.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_unCheckAll.setFlat(True)
        self.pushButton_unCheckAll.setObjectName("pushButton_unCheckAll")
        self.lineEdit_prefixName = QtWidgets.QLineEdit(self.frame_17)
        self.lineEdit_prefixName.setEnabled(True)
        self.lineEdit_prefixName.setGeometry(QtCore.QRect(245, 20, 91, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
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
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
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
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
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
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 49, 44))
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
        self.lineEdit_prefixName.setPalette(palette)
        self.lineEdit_prefixName.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_prefixName.setObjectName("lineEdit_prefixName")
        self.pushButton_delectSelectItems = QtWidgets.QPushButton(self.frame_17)
        self.pushButton_delectSelectItems.setGeometry(QtCore.QRect(345, 20, 30, 30))
        self.pushButton_delectSelectItems.setText("")
        icon48 = QtGui.QIcon()
        icon48.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/deletePublishB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_delectSelectItems.setIcon(icon48)
        self.pushButton_delectSelectItems.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_delectSelectItems.setFlat(True)
        self.pushButton_delectSelectItems.setObjectName("pushButton_delectSelectItems")
        self.label_fileData_39 = QtWidgets.QLabel(self.frame_17)
        self.label_fileData_39.setGeometry(QtCore.QRect(10, -3, 46, 20))
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
        self.label_fileData_40 = QtWidgets.QLabel(self.frame_17)
        self.label_fileData_40.setGeometry(QtCore.QRect(55, -3, 46, 20))
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
        self.label_fileData_41 = QtWidgets.QLabel(self.frame_17)
        self.label_fileData_41.setGeometry(QtCore.QRect(137, 0, 46, 20))
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
        self.label_fileData_41.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_41.setFont(font)
        self.label_fileData_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_41.setObjectName("label_fileData_41")
        self.label_fileData_42 = QtWidgets.QLabel(self.frame_17)
        self.label_fileData_42.setGeometry(QtCore.QRect(188, 0, 46, 20))
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
        self.label_fileData_42.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_42.setFont(font)
        self.label_fileData_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_42.setObjectName("label_fileData_42")
        self.label_fileData_43 = QtWidgets.QLabel(self.frame_17)
        self.label_fileData_43.setGeometry(QtCore.QRect(340, 0, 46, 20))
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
        self.label_fileData_44 = QtWidgets.QLabel(self.frame_17)
        self.label_fileData_44.setGeometry(QtCore.QRect(250, 0, 76, 20))
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
        self.label_fileData_44.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_44.setFont(font)
        self.label_fileData_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_44.setObjectName("label_fileData_44")
        self.frame_18 = QtWidgets.QFrame(self.tab)
        self.frame_18.setGeometry(QtCore.QRect(450, 0, 128, 56))
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
        self.frame_18.setPalette(palette)
        self.frame_18.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setLineWidth(1)
        self.frame_18.setMidLineWidth(0)
        self.frame_18.setObjectName("frame_18")
        self.pushButton_publishAll = QtWidgets.QPushButton(self.frame_18)
        self.pushButton_publishAll.setEnabled(True)
        self.pushButton_publishAll.setGeometry(QtCore.QRect(8, 8, 40, 40))
        self.pushButton_publishAll.setText("")
        self.pushButton_publishAll.setIcon(icon31)
        self.pushButton_publishAll.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_publishAll.setCheckable(True)
        self.pushButton_publishAll.setAutoDefault(False)
        self.pushButton_publishAll.setDefault(False)
        self.pushButton_publishAll.setFlat(True)
        self.pushButton_publishAll.setObjectName("pushButton_publishAll")
        self.pushButton_uploadSyncA = QtWidgets.QPushButton(self.frame_18)
        self.pushButton_uploadSyncA.setEnabled(True)
        self.pushButton_uploadSyncA.setGeometry(QtCore.QRect(67, 8, 40, 40))
        self.pushButton_uploadSyncA.setText("")
        self.pushButton_uploadSyncA.setIcon(icon30)
        self.pushButton_uploadSyncA.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_uploadSyncA.setCheckable(True)
        self.pushButton_uploadSyncA.setAutoDefault(False)
        self.pushButton_uploadSyncA.setDefault(False)
        self.pushButton_uploadSyncA.setFlat(True)
        self.pushButton_uploadSyncA.setObjectName("pushButton_uploadSyncA")
        self.frame_22 = QtWidgets.QFrame(self.tab)
        self.frame_22.setGeometry(QtCore.QRect(580, 0, 56, 56))
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
        self.frame_22.setPalette(palette)
        self.frame_22.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setLineWidth(1)
        self.frame_22.setMidLineWidth(0)
        self.frame_22.setObjectName("frame_22")
        self.pushButton_changePageA_2 = QtWidgets.QPushButton(self.frame_22)
        self.pushButton_changePageA_2.setEnabled(True)
        self.pushButton_changePageA_2.setGeometry(QtCore.QRect(2, 3, 25, 25))
        self.pushButton_changePageA_2.setText("")
        self.pushButton_changePageA_2.setIcon(icon34)
        self.pushButton_changePageA_2.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_changePageA_2.setCheckable(True)
        self.pushButton_changePageA_2.setAutoDefault(False)
        self.pushButton_changePageA_2.setDefault(False)
        self.pushButton_changePageA_2.setFlat(True)
        self.pushButton_changePageA_2.setObjectName("pushButton_changePageA_2")
        self.pushButton_changePageB_2 = QtWidgets.QPushButton(self.frame_22)
        self.pushButton_changePageB_2.setEnabled(True)
        self.pushButton_changePageB_2.setGeometry(QtCore.QRect(27, 3, 25, 25))
        self.pushButton_changePageB_2.setText("")
        self.pushButton_changePageB_2.setIcon(icon35)
        self.pushButton_changePageB_2.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_changePageB_2.setCheckable(True)
        self.pushButton_changePageB_2.setAutoDefault(False)
        self.pushButton_changePageB_2.setDefault(False)
        self.pushButton_changePageB_2.setFlat(True)
        self.pushButton_changePageB_2.setObjectName("pushButton_changePageB_2")
        self.pushButton_changePageC_2 = QtWidgets.QPushButton(self.frame_22)
        self.pushButton_changePageC_2.setEnabled(True)
        self.pushButton_changePageC_2.setGeometry(QtCore.QRect(2, 28, 25, 25))
        self.pushButton_changePageC_2.setText("")
        self.pushButton_changePageC_2.setIcon(icon36)
        self.pushButton_changePageC_2.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_changePageC_2.setCheckable(True)
        self.pushButton_changePageC_2.setAutoDefault(False)
        self.pushButton_changePageC_2.setDefault(False)
        self.pushButton_changePageC_2.setFlat(True)
        self.pushButton_changePageC_2.setObjectName("pushButton_changePageC_2")
        self.pushButton_changePageD_2 = QtWidgets.QPushButton(self.frame_22)
        self.pushButton_changePageD_2.setEnabled(True)
        self.pushButton_changePageD_2.setGeometry(QtCore.QRect(27, 28, 25, 25))
        self.pushButton_changePageD_2.setText("")
        self.pushButton_changePageD_2.setIcon(icon37)
        self.pushButton_changePageD_2.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_changePageD_2.setCheckable(True)
        self.pushButton_changePageD_2.setAutoDefault(False)
        self.pushButton_changePageD_2.setDefault(False)
        self.pushButton_changePageD_2.setFlat(True)
        self.pushButton_changePageD_2.setObjectName("pushButton_changePageD_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(760, 130, 171, 46))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton_publishAll2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_publishAll2.setGeometry(QtCore.QRect(780, 0, 120, 50))
        self.pushButton_publishAll2.setText("")
        icon49 = QtGui.QIcon()
        icon49.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/eggD_240.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_publishAll2.setIcon(icon49)
        self.pushButton_publishAll2.setIconSize(QtCore.QSize(120, 60))
        self.pushButton_publishAll2.setFlat(True)
        self.pushButton_publishAll2.setObjectName("pushButton_publishAll2")
        self.frame_23 = QtWidgets.QFrame(self.tab)
        self.frame_23.setGeometry(QtCore.QRect(765, 240, 186, 26))
        self.frame_23.setMaximumSize(QtCore.QSize(650, 16777215))
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
        self.frame_23.setPalette(palette)
        self.frame_23.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setLineWidth(1)
        self.frame_23.setMidLineWidth(0)
        self.frame_23.setObjectName("frame_23")
        self.radioButton_publishMode = QtWidgets.QRadioButton(self.frame_23)
        self.radioButton_publishMode.setGeometry(QtCore.QRect(5, 5, 76, 16))
        self.radioButton_publishMode.setMaximumSize(QtCore.QSize(650, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(213, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 255, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(213, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 255, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(213, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 255, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.radioButton_publishMode.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.radioButton_publishMode.setFont(font)
        self.radioButton_publishMode.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_publishMode.setChecked(False)
        self.radioButton_publishMode.setObjectName("radioButton_publishMode")
        self.radioButton_syncMode = QtWidgets.QRadioButton(self.frame_23)
        self.radioButton_syncMode.setGeometry(QtCore.QRect(105, 5, 76, 16))
        self.radioButton_syncMode.setMaximumSize(QtCore.QSize(650, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(213, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 255, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(213, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 255, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 255, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(213, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 255, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.radioButton_syncMode.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.radioButton_syncMode.setFont(font)
        self.radioButton_syncMode.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_syncMode.setChecked(False)
        self.radioButton_syncMode.setObjectName("radioButton_syncMode")
        self.tabWidget_branch.addTab(self.tab, "")
        self.tab_job_assemble = QtWidgets.QWidget()
        self.tab_job_assemble.setObjectName("tab_job_assemble")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_job_assemble)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(750, 80, 82, 128))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_8 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout.addWidget(self.pushButton_8)
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_7.setEnabled(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_job_assemble)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(750, 240, 82, 194))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_3.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_3.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_3.addWidget(self.pushButton_11)
        self.pushButton_25 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_25.setObjectName("pushButton_25")
        self.verticalLayout_3.addWidget(self.pushButton_25)
        self.pushButton_24 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_24.setObjectName("pushButton_24")
        self.verticalLayout_3.addWidget(self.pushButton_24)
        self.pushButton_12 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_3.addWidget(self.pushButton_12)
        self.frame_20 = QtWidgets.QFrame(self.tab_job_assemble)
        self.frame_20.setGeometry(QtCore.QRect(40, 80, 366, 671))
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
        self.frame_20.setPalette(palette)
        self.frame_20.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setLineWidth(1)
        self.frame_20.setMidLineWidth(0)
        self.frame_20.setObjectName("frame_20")
        self.treeWidget = QtWidgets.QTreeWidget(self.frame_20)
        self.treeWidget.setGeometry(QtCore.QRect(40, 130, 256, 192))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.header().setVisible(False)
        self.tabWidget_branch.addTab(self.tab_job_assemble, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_optionPage_projDescription = QtWidgets.QLabel(self.tab_2)
        self.label_optionPage_projDescription.setGeometry(QtCore.QRect(30, 40, 130, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(6)
        self.label_optionPage_projDescription.setFont(font)
        self.label_optionPage_projDescription.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_optionPage_projDescription.setObjectName("label_optionPage_projDescription")
        self.label_optionPage_showFileType = QtWidgets.QLabel(self.tab_2)
        self.label_optionPage_showFileType.setGeometry(QtCore.QRect(30, 340, 130, 16))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_optionPage_showFileType.setFont(font)
        self.label_optionPage_showFileType.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_optionPage_showFileType.setObjectName("label_optionPage_showFileType")
        self.label_optionPage_tempB = QtWidgets.QLabel(self.tab_2)
        self.label_optionPage_tempB.setGeometry(QtCore.QRect(30, 390, 130, 16))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_optionPage_tempB.setFont(font)
        self.label_optionPage_tempB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_optionPage_tempB.setObjectName("label_optionPage_tempB")
        self.label_optionPage_userPref = QtWidgets.QLabel(self.tab_2)
        self.label_optionPage_userPref.setGeometry(QtCore.QRect(30, 280, 130, 16))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_optionPage_userPref.setFont(font)
        self.label_optionPage_userPref.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_optionPage_userPref.setObjectName("label_optionPage_userPref")
        self.label_optionPage_User = QtWidgets.QLabel(self.tab_2)
        self.label_optionPage_User.setGeometry(QtCore.QRect(30, 230, 130, 16))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_optionPage_User.setFont(font)
        self.label_optionPage_User.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_optionPage_User.setObjectName("label_optionPage_User")
        self.label_optionPage_workProj = QtWidgets.QLabel(self.tab_2)
        self.label_optionPage_workProj.setGeometry(QtCore.QRect(30, 100, 130, 16))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_optionPage_workProj.setFont(font)
        self.label_optionPage_workProj.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_optionPage_workProj.setObjectName("label_optionPage_workProj")
        self.label_optionPage_branchFileInfo = QtWidgets.QLabel(self.tab_2)
        self.label_optionPage_branchFileInfo.setGeometry(QtCore.QRect(30, 160, 130, 16))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_optionPage_branchFileInfo.setFont(font)
        self.label_optionPage_branchFileInfo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_optionPage_branchFileInfo.setObjectName("label_optionPage_branchFileInfo")
        self.plainTextEdit_optionPage_projDescription = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_optionPage_projDescription.setGeometry(QtCore.QRect(170, 40, 351, 50))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.plainTextEdit_optionPage_projDescription.setFont(font)
        self.plainTextEdit_optionPage_projDescription.setReadOnly(True)
        self.plainTextEdit_optionPage_projDescription.setPlainText("")
        self.plainTextEdit_optionPage_projDescription.setObjectName("plainTextEdit_optionPage_projDescription")
        self.plainTextEdit_optionPage_workProj = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_optionPage_workProj.setGeometry(QtCore.QRect(170, 100, 351, 50))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.plainTextEdit_optionPage_workProj.setFont(font)
        self.plainTextEdit_optionPage_workProj.setReadOnly(True)
        self.plainTextEdit_optionPage_workProj.setObjectName("plainTextEdit_optionPage_workProj")
        self.plainTextEdit_optionPage_branchInfoPos = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_optionPage_branchInfoPos.setGeometry(QtCore.QRect(170, 160, 351, 50))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.plainTextEdit_optionPage_branchInfoPos.setFont(font)
        self.plainTextEdit_optionPage_branchInfoPos.setReadOnly(True)
        self.plainTextEdit_optionPage_branchInfoPos.setObjectName("plainTextEdit_optionPage_branchInfoPos")
        self.plainTextEdit_optionPage_currentUser = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_optionPage_currentUser.setGeometry(QtCore.QRect(170, 230, 351, 40))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.plainTextEdit_optionPage_currentUser.setFont(font)
        self.plainTextEdit_optionPage_currentUser.setReadOnly(True)
        self.plainTextEdit_optionPage_currentUser.setObjectName("plainTextEdit_optionPage_currentUser")
        self.plainTextEdit_optionPage_userPref = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_optionPage_userPref.setGeometry(QtCore.QRect(170, 280, 351, 50))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.plainTextEdit_optionPage_userPref.setFont(font)
        self.plainTextEdit_optionPage_userPref.setReadOnly(True)
        self.plainTextEdit_optionPage_userPref.setObjectName("plainTextEdit_optionPage_userPref")
        self.plainTextEdit_optionPage_showFileType = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_optionPage_showFileType.setGeometry(QtCore.QRect(170, 340, 351, 40))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.plainTextEdit_optionPage_showFileType.setFont(font)
        self.plainTextEdit_optionPage_showFileType.setReadOnly(False)
        self.plainTextEdit_optionPage_showFileType.setObjectName("plainTextEdit_optionPage_showFileType")
        self.plainTextEdit_optionPage_tempB = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_optionPage_tempB.setGeometry(QtCore.QRect(170, 390, 351, 40))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.plainTextEdit_optionPage_tempB.setFont(font)
        self.plainTextEdit_optionPage_tempB.setReadOnly(True)
        self.plainTextEdit_optionPage_tempB.setObjectName("plainTextEdit_optionPage_tempB")
        self.frame_19 = QtWidgets.QFrame(self.tab_2)
        self.frame_19.setGeometry(QtCore.QRect(75, 460, 426, 241))
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
        self.frame_19.setPalette(palette)
        self.frame_19.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setLineWidth(1)
        self.frame_19.setMidLineWidth(0)
        self.frame_19.setObjectName("frame_19")
        self.label_optionPage_tempB_2 = QtWidgets.QLabel(self.frame_19)
        self.label_optionPage_tempB_2.setGeometry(QtCore.QRect(10, 15, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_optionPage_tempB_2.setFont(font)
        self.label_optionPage_tempB_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_optionPage_tempB_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_optionPage_tempB_2.setObjectName("label_optionPage_tempB_2")
        self.lineEdit_setRoot = QtWidgets.QLineEdit(self.frame_19)
        self.lineEdit_setRoot.setGeometry(QtCore.QRect(70, 10, 321, 26))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
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
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
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
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
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
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.lineEdit_setRoot.setPalette(palette)
        self.lineEdit_setRoot.setObjectName("lineEdit_setRoot")
        self.plainTextEdit_rootInput = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_rootInput.setGeometry(QtCore.QRect(670, 465, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.plainTextEdit_rootInput.setFont(font)
        self.plainTextEdit_rootInput.setReadOnly(True)
        self.plainTextEdit_rootInput.setObjectName("plainTextEdit_rootInput")
        self.tabWidget_branch.addTab(self.tab_2, "")
        self.label_fileDescription = QtWidgets.QLabel(self.centralwidget)
        self.label_fileDescription.setGeometry(QtCore.QRect(1320, 150, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_fileDescription.setFont(font)
        self.label_fileDescription.setObjectName("label_fileDescription")
        self.label_selectProject = QtWidgets.QLabel(self.centralwidget)
        self.label_selectProject.setGeometry(QtCore.QRect(1310, 610, 141, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label_selectProject.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_selectProject.setFont(font)
        self.label_selectProject.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_selectProject.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_selectProject.setObjectName("label_selectProject")
        self.label_currentProj = QtWidgets.QLabel(self.centralwidget)
        self.label_currentProj.setGeometry(QtCore.QRect(1310, 30, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_currentProj.setFont(font)
        self.label_currentProj.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_currentProj.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_currentProj.setObjectName("label_currentProj")
        self.pushButton_closeBranch = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_closeBranch.setGeometry(QtCore.QRect(1390, 330, 31, 31))
        self.pushButton_closeBranch.setText("")
        icon50 = QtGui.QIcon()
        icon50.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/delete2_512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_closeBranch.setIcon(icon50)
        self.pushButton_closeBranch.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_closeBranch.setAutoDefault(False)
        self.pushButton_closeBranch.setDefault(False)
        self.pushButton_closeBranch.setFlat(True)
        self.pushButton_closeBranch.setObjectName("pushButton_closeBranch")
        self.pushButton_openFileJson = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_openFileJson.setGeometry(QtCore.QRect(1360, 250, 31, 31))
        self.pushButton_openFileJson.setText("")
        icon51 = QtGui.QIcon()
        icon51.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/document2-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_openFileJson.setIcon(icon51)
        self.pushButton_openFileJson.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_openFileJson.setAutoDefault(False)
        self.pushButton_openFileJson.setDefault(False)
        self.pushButton_openFileJson.setFlat(True)
        self.pushButton_openFileJson.setObjectName("pushButton_openFileJson")
        self.label_metaData = QtWidgets.QLabel(self.centralwidget)
        self.label_metaData.setGeometry(QtCore.QRect(1330, 680, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_metaData.setFont(font)
        self.label_metaData.setObjectName("label_metaData")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1340, 420, 161, 21))
        self.label.setMaximumSize(QtCore.QSize(650, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_processComp = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_processComp.setEnabled(True)
        self.pushButton_processComp.setGeometry(QtCore.QRect(1340, 550, 29, 29))
        self.pushButton_processComp.setText("")
        icon52 = QtGui.QIcon()
        icon52.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/comp_3Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon52.addPixmap(QtGui.QPixmap("//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/comp_3Open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_processComp.setIcon(icon52)
        self.pushButton_processComp.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_processComp.setCheckable(True)
        self.pushButton_processComp.setAutoDefault(False)
        self.pushButton_processComp.setDefault(False)
        self.pushButton_processComp.setFlat(True)
        self.pushButton_processComp.setObjectName("pushButton_processComp")
        self.label_fileData_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_fileData_35.setGeometry(QtCore.QRect(1220, 20, 30, 20))
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
        self.label_fileData_35.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_fileData_35.setFont(font)
        self.label_fileData_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileData_35.setObjectName("label_fileData_35")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget_branch.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "PublishTool Ver.0.91", None, -1))
        self.comboBox_selectProj.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "select project", None, -1))
        self.label_fileData_29.setText(QtWidgets.QApplication.translate("MainWindow", "Build", None, -1))
        self.label_fileData_36.setText(QtWidgets.QApplication.translate("MainWindow", "Now", None, -1))
        self.label_fileData_37.setText(QtWidgets.QApplication.translate("MainWindow", "Recent", None, -1))
        self.label_fileData_38.setText(QtWidgets.QApplication.translate("MainWindow", "Completed", None, -1))
        self.label_fileData_47.setText(QtWidgets.QApplication.translate("MainWindow", "Current Project Select", None, -1))
        self.label_fileData_33.setText(QtWidgets.QApplication.translate("MainWindow", "Edit", None, -1))
        self.label_fileData_46.setText(QtWidgets.QApplication.translate("MainWindow", "Info", None, -1))
        self.label_fileData_9.setText(QtWidgets.QApplication.translate("MainWindow", "Sim", None, -1))
        self.label_fileData.setText(QtWidgets.QApplication.translate("MainWindow", "Con", None, -1))
        self.label_fileData_4.setText(QtWidgets.QApplication.translate("MainWindow", "Rig", None, -1))
        self.label_fileData_3.setText(QtWidgets.QApplication.translate("MainWindow", "Tex", None, -1))
        self.label_fileData_8.setText(QtWidgets.QApplication.translate("MainWindow", "Eff", None, -1))
        self.label_fileData_7.setText(QtWidgets.QApplication.translate("MainWindow", "Lig", None, -1))
        self.label_fileData_2.setText(QtWidgets.QApplication.translate("MainWindow", "Mod", None, -1))
        self.label_fileData_5.setText(QtWidgets.QApplication.translate("MainWindow", "Lay", None, -1))
        self.label_fileData_6.setText(QtWidgets.QApplication.translate("MainWindow", "Ani", None, -1))
        self.label_fileData_17.setText(QtWidgets.QApplication.translate("MainWindow", "Shot", None, -1))
        self.lineEdit_currentFileName.setText(QtWidgets.QApplication.translate("MainWindow", "SelectFile:", None, -1))
        self.treeWidget_branches.headerItem().setText(0, QtWidgets.QApplication.translate("MainWindow", "branch Info", None, -1))
        __sortingEnabled = self.treeWidget_branches.isSortingEnabled()
        self.treeWidget_branches.setSortingEnabled(False)
        self.treeWidget_branches.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "master", None, -1))
        self.treeWidget_branches.setSortingEnabled(__sortingEnabled)
        self.tableWidget_FileList.verticalHeaderItem(0).setText(QtWidgets.QApplication.translate("MainWindow", "01", None, -1))
        self.tableWidget_FileList.verticalHeaderItem(1).setText(QtWidgets.QApplication.translate("MainWindow", "02", None, -1))
        self.tableWidget_FileList.verticalHeaderItem(2).setText(QtWidgets.QApplication.translate("MainWindow", "03", None, -1))
        self.tableWidget_FileList.verticalHeaderItem(3).setText(QtWidgets.QApplication.translate("MainWindow", "04", None, -1))
        self.tableWidget_FileList.verticalHeaderItem(4).setText(QtWidgets.QApplication.translate("MainWindow", "05", None, -1))
        self.tableWidget_FileList.verticalHeaderItem(5).setText(QtWidgets.QApplication.translate("MainWindow", "06", None, -1))
        self.tableWidget_FileList.verticalHeaderItem(6).setText(QtWidgets.QApplication.translate("MainWindow", "07", None, -1))
        self.tableWidget_FileList.verticalHeaderItem(7).setText(QtWidgets.QApplication.translate("MainWindow", "08", None, -1))
        self.tableWidget_FileList.verticalHeaderItem(8).setText(QtWidgets.QApplication.translate("MainWindow", "09", None, -1))
        self.tableWidget_FileList.verticalHeaderItem(9).setText(QtWidgets.QApplication.translate("MainWindow", "10", None, -1))
        self.tableWidget_FileList.verticalHeaderItem(10).setText(QtWidgets.QApplication.translate("MainWindow", "11", None, -1))
        self.tableWidget_FileList.verticalHeaderItem(11).setText(QtWidgets.QApplication.translate("MainWindow", "12", None, -1))
        self.tableWidget_FileList.verticalHeaderItem(12).setText(QtWidgets.QApplication.translate("MainWindow", "13", None, -1))
        self.tableWidget_FileList.verticalHeaderItem(13).setText(QtWidgets.QApplication.translate("MainWindow", "14", None, -1))
        self.tableWidget_FileList.verticalHeaderItem(14).setText(QtWidgets.QApplication.translate("MainWindow", "15", None, -1))
        self.tableWidget_FileList.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("MainWindow", "Ver.", None, -1))
        self.tableWidget_FileList.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("MainWindow", "UserName", None, -1))
        self.tableWidget_FileList.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("MainWindow", "Date..................................................", None, -1))
        __sortingEnabled = self.tableWidget_FileList.isSortingEnabled()
        self.tableWidget_FileList.setSortingEnabled(False)
        self.tableWidget_FileList.item(0, 0).setText(QtWidgets.QApplication.translate("MainWindow", "v009", None, -1))
        self.tableWidget_FileList.item(0, 1).setText(QtWidgets.QApplication.translate("MainWindow", "alpha", None, -1))
        self.tableWidget_FileList.item(0, 2).setText(QtWidgets.QApplication.translate("MainWindow", "2017.03/28 10:00", None, -1))
        self.tableWidget_FileList.item(1, 0).setText(QtWidgets.QApplication.translate("MainWindow", "v008", None, -1))
        self.tableWidget_FileList.item(1, 1).setText(QtWidgets.QApplication.translate("MainWindow", "alpha", None, -1))
        self.tableWidget_FileList.item(1, 2).setText(QtWidgets.QApplication.translate("MainWindow", "2017.03/28 10:00", None, -1))
        self.tableWidget_FileList.item(2, 0).setText(QtWidgets.QApplication.translate("MainWindow", "v007", None, -1))
        self.tableWidget_FileList.item(2, 1).setText(QtWidgets.QApplication.translate("MainWindow", "alpha", None, -1))
        self.tableWidget_FileList.item(2, 2).setText(QtWidgets.QApplication.translate("MainWindow", "2017.03/28 10:00", None, -1))
        self.tableWidget_FileList.item(3, 0).setText(QtWidgets.QApplication.translate("MainWindow", "v006", None, -1))
        self.tableWidget_FileList.item(3, 1).setText(QtWidgets.QApplication.translate("MainWindow", "alpha", None, -1))
        self.tableWidget_FileList.item(3, 2).setText(QtWidgets.QApplication.translate("MainWindow", "2017.03/28 10:00", None, -1))
        self.tableWidget_FileList.item(4, 0).setText(QtWidgets.QApplication.translate("MainWindow", "v005", None, -1))
        self.tableWidget_FileList.item(4, 1).setText(QtWidgets.QApplication.translate("MainWindow", "alpha", None, -1))
        self.tableWidget_FileList.item(4, 2).setText(QtWidgets.QApplication.translate("MainWindow", "2017.03/28 10:00", None, -1))
        self.tableWidget_FileList.item(5, 0).setText(QtWidgets.QApplication.translate("MainWindow", "v004", None, -1))
        self.tableWidget_FileList.item(5, 1).setText(QtWidgets.QApplication.translate("MainWindow", "alpha", None, -1))
        self.tableWidget_FileList.item(5, 2).setText(QtWidgets.QApplication.translate("MainWindow", "2017.03/28 10:00", None, -1))
        self.tableWidget_FileList.item(6, 0).setText(QtWidgets.QApplication.translate("MainWindow", "v003", None, -1))
        self.tableWidget_FileList.item(6, 1).setText(QtWidgets.QApplication.translate("MainWindow", "alpha", None, -1))
        self.tableWidget_FileList.item(6, 2).setText(QtWidgets.QApplication.translate("MainWindow", "2017.03/28 10:00", None, -1))
        self.tableWidget_FileList.item(7, 0).setText(QtWidgets.QApplication.translate("MainWindow", "v002", None, -1))
        self.tableWidget_FileList.item(7, 1).setText(QtWidgets.QApplication.translate("MainWindow", "alpha", None, -1))
        self.tableWidget_FileList.item(7, 2).setText(QtWidgets.QApplication.translate("MainWindow", "2017.03/28 10:00", None, -1))
        self.tableWidget_FileList.item(8, 0).setText(QtWidgets.QApplication.translate("MainWindow", "v001", None, -1))
        self.tableWidget_FileList.item(8, 1).setText(QtWidgets.QApplication.translate("MainWindow", "alpha", None, -1))
        self.tableWidget_FileList.item(8, 2).setText(QtWidgets.QApplication.translate("MainWindow", "2017.03/28 10:00", None, -1))
        self.tableWidget_FileList.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_assetProj.isSortingEnabled()
        self.listWidget_assetProj.setSortingEnabled(False)
        self.listWidget_assetProj.item(0).setText(QtWidgets.QApplication.translate("MainWindow", "concept", None, -1))
        self.listWidget_assetProj.item(1).setText(QtWidgets.QApplication.translate("MainWindow", "modeling", None, -1))
        self.listWidget_assetProj.item(2).setText(QtWidgets.QApplication.translate("MainWindow", "texture", None, -1))
        self.listWidget_assetProj.item(3).setText(QtWidgets.QApplication.translate("MainWindow", "rigging", None, -1))
        self.listWidget_assetProj.item(4).setText(QtWidgets.QApplication.translate("MainWindow", "animatic", None, -1))
        self.listWidget_assetProj.item(5).setText(QtWidgets.QApplication.translate("MainWindow", "layout", None, -1))
        self.listWidget_assetProj.item(6).setText(QtWidgets.QApplication.translate("MainWindow", "animation", None, -1))
        self.listWidget_assetProj.item(7).setText(QtWidgets.QApplication.translate("MainWindow", "effect", None, -1))
        self.listWidget_assetProj.item(8).setText(QtWidgets.QApplication.translate("MainWindow", "simulation", None, -1))
        self.listWidget_assetProj.item(9).setText(QtWidgets.QApplication.translate("MainWindow", "lighting", None, -1))
        self.listWidget_assetProj.setSortingEnabled(__sortingEnabled)
        self.label_fileData_15.setText(QtWidgets.QApplication.translate("MainWindow", "Oth", None, -1))
        self.label_fileData_12.setText(QtWidgets.QApplication.translate("MainWindow", "Veh", None, -1))
        self.label_fileData_11.setText(QtWidgets.QApplication.translate("MainWindow", "Cha", None, -1))
        self.label_fileData_13.setText(QtWidgets.QApplication.translate("MainWindow", "Set", None, -1))
        self.label_fileData_14.setText(QtWidgets.QApplication.translate("MainWindow", "Pro", None, -1))
        self.label_fileData_10.setText(QtWidgets.QApplication.translate("MainWindow", "All", None, -1))
        self.label_fileData_26.setText(QtWidgets.QApplication.translate("MainWindow", "New", None, -1))
        self.label_fileData_30.setText(QtWidgets.QApplication.translate("MainWindow", "Open", None, -1))
        self.label_fileData_32.setText(QtWidgets.QApplication.translate("MainWindow", "Load", None, -1))
        self.label_fileData_31.setText(QtWidgets.QApplication.translate("MainWindow", "Save", None, -1))
        self.label_fileData_45.setText(QtWidgets.QApplication.translate("MainWindow", "Merge", None, -1))
        self.label_fileData_34.setText(QtWidgets.QApplication.translate("MainWindow", "Process", None, -1))
        self.label_fileData_28.setText(QtWidgets.QApplication.translate("MainWindow", "Assets", None, -1))
        self.tabWidget_branch.setTabText(self.tabWidget_branch.indexOf(self.tab_branch), QtWidgets.QApplication.translate("MainWindow", "branch Edit", None, -1))
        self.treeWidget_filesList.headerItem().setText(0, QtWidgets.QApplication.translate("MainWindow", "items", None, -1))
        self.treeWidget_filesList.headerItem().setText(1, QtWidgets.QApplication.translate("MainWindow", "location                                                                                                                                                                                                                                                             ", None, -1))
        __sortingEnabled = self.treeWidget_filesList.isSortingEnabled()
        self.treeWidget_filesList.setSortingEnabled(False)
        self.treeWidget_filesList.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "PrmanTextures", None, -1))
        self.treeWidget_filesList.topLevelItem(0).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "file", None, -1))
        self.treeWidget_filesList.topLevelItem(0).child(0).setText(1, QtWidgets.QApplication.translate("MainWindow", "c:\\temp", None, -1))
        self.treeWidget_filesList.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "mayaTextures", None, -1))
        self.treeWidget_filesList.topLevelItem(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "gpuCaches", None, -1))
        self.treeWidget_filesList.topLevelItem(3).setText(0, QtWidgets.QApplication.translate("MainWindow", "RibArhives", None, -1))
        self.treeWidget_filesList.topLevelItem(4).setText(0, QtWidgets.QApplication.translate("MainWindow", "alembics", None, -1))
        self.treeWidget_filesList.topLevelItem(5).setText(0, QtWidgets.QApplication.translate("MainWindow", "cameras", None, -1))
        self.treeWidget_filesList.topLevelItem(6).setText(0, QtWidgets.QApplication.translate("MainWindow", "PrmanLights", None, -1))
        self.treeWidget_filesList.topLevelItem(7).setText(0, QtWidgets.QApplication.translate("MainWindow", "mayaLights", None, -1))
        self.treeWidget_filesList.topLevelItem(8).setText(0, QtWidgets.QApplication.translate("MainWindow", "fluidCaches", None, -1))
        self.treeWidget_filesList.topLevelItem(9).setText(0, QtWidgets.QApplication.translate("MainWindow", "particleCaches", None, -1))
        self.treeWidget_filesList.setSortingEnabled(__sortingEnabled)
        self.treeWidget_FiletOption.headerItem().setText(0, QtWidgets.QApplication.translate("MainWindow", "Filter Option", None, -1))
        __sortingEnabled = self.treeWidget_FiletOption.isSortingEnabled()
        self.treeWidget_FiletOption.setSortingEnabled(False)
        self.treeWidget_FiletOption.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "Collect Files", None, -1))
        self.treeWidget_FiletOption.topLevelItem(0).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "Prman Texture", None, -1))
        self.treeWidget_FiletOption.topLevelItem(0).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "Maya Texture", None, -1))
        self.treeWidget_FiletOption.topLevelItem(0).child(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "GpuCache", None, -1))
        self.treeWidget_FiletOption.topLevelItem(0).child(3).setText(0, QtWidgets.QApplication.translate("MainWindow", "RibArchive", None, -1))
        self.treeWidget_FiletOption.topLevelItem(0).child(4).setText(0, QtWidgets.QApplication.translate("MainWindow", "Alembic Cache", None, -1))
        self.treeWidget_FiletOption.topLevelItem(0).child(5).setText(0, QtWidgets.QApplication.translate("MainWindow", "Prman Light", None, -1))
        self.treeWidget_FiletOption.topLevelItem(0).child(6).setText(0, QtWidgets.QApplication.translate("MainWindow", "Maya Fluid", None, -1))
        self.treeWidget_FiletOption.topLevelItem(0).child(7).setText(0, QtWidgets.QApplication.translate("MainWindow", "Maya nParticle Cache", None, -1))
        self.treeWidget_FiletOption.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "Check Plugin", None, -1))
        self.treeWidget_FiletOption.topLevelItem(1).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "Delete Unused Plugin", None, -1))
        self.treeWidget_FiletOption.topLevelItem(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "Check Asset Unit", None, -1))
        self.treeWidget_FiletOption.topLevelItem(2).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "Check BB", None, -1))
        self.treeWidget_FiletOption.topLevelItem(2).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "Check Position", None, -1))
        self.treeWidget_FiletOption.topLevelItem(2).child(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "Check Repeat", None, -1))
        self.treeWidget_FiletOption.topLevelItem(2).child(3).setText(0, QtWidgets.QApplication.translate("MainWindow", "ReName SG", None, -1))
        self.treeWidget_FiletOption.topLevelItem(3).setText(0, QtWidgets.QApplication.translate("MainWindow", "Duplicated ShapeName", None, -1))
        self.treeWidget_FiletOption.topLevelItem(3).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "RibArchive_Shape", None, -1))
        self.treeWidget_FiletOption.topLevelItem(3).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "GpuCache_Shpae", None, -1))
        self.treeWidget_FiletOption.topLevelItem(3).child(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "alembic_Shape", None, -1))
        self.treeWidget_FiletOption.topLevelItem(3).child(3).setText(0, QtWidgets.QApplication.translate("MainWindow", "fluidShapes_Shape", None, -1))
        self.treeWidget_FiletOption.topLevelItem(3).child(4).setText(0, QtWidgets.QApplication.translate("MainWindow", "particle_Shape", None, -1))
        self.treeWidget_FiletOption.setSortingEnabled(__sortingEnabled)
        self.plainTextEdit.setPlainText(QtWidgets.QApplication.translate("MainWindow", "#metaData", None, -1))
        self.radioButton_customer.setText(QtWidgets.QApplication.translate("MainWindow", "Customer Size", None, -1))
        self.radioButton_Half.setText(QtWidgets.QApplication.translate("MainWindow", "Half Size", None, -1))
        self.radioButton_Quarter.setText(QtWidgets.QApplication.translate("MainWindow", "Quarter Size", None, -1))
        self.radioButton_Original.setText(QtWidgets.QApplication.translate("MainWindow", "Original Size", None, -1))
        self.lineEdit_file_sources.setText(QtWidgets.QApplication.translate("MainWindow", "//mcd-server", None, -1))
        self.lineEdit_file_sources_2.setText(QtWidgets.QApplication.translate("MainWindow", "fileDesc", None, -1))
        self.lineEdit_prefixName.setText(QtWidgets.QApplication.translate("MainWindow", "Prefix", None, -1))
        self.label_fileData_39.setText(QtWidgets.QApplication.translate("MainWindow", "Refresh", None, -1))
        self.label_fileData_40.setText(QtWidgets.QApplication.translate("MainWindow", "Select", None, -1))
        self.label_fileData_41.setText(QtWidgets.QApplication.translate("MainWindow", "UnCheck", None, -1))
        self.label_fileData_42.setText(QtWidgets.QApplication.translate("MainWindow", "ReName", None, -1))
        self.label_fileData_43.setText(QtWidgets.QApplication.translate("MainWindow", "Delete", None, -1))
        self.label_fileData_44.setText(QtWidgets.QApplication.translate("MainWindow", "Prefix_Name", None, -1))
        self.radioButton_publishMode.setText(QtWidgets.QApplication.translate("MainWindow", "Publish", None, -1))
        self.radioButton_syncMode.setText(QtWidgets.QApplication.translate("MainWindow", "Sync", None, -1))
        self.tabWidget_branch.setTabText(self.tabWidget_branch.indexOf(self.tab), QtWidgets.QApplication.translate("MainWindow", "PublishTool", None, -1))
        self.pushButton_6.setText(QtWidgets.QApplication.translate("MainWindow", "concept", None, -1))
        self.pushButton_4.setText(QtWidgets.QApplication.translate("MainWindow", "model", None, -1))
        self.pushButton_8.setText(QtWidgets.QApplication.translate("MainWindow", "texture", None, -1))
        self.pushButton_7.setText(QtWidgets.QApplication.translate("MainWindow", "rigging", None, -1))
        self.pushButton_9.setText(QtWidgets.QApplication.translate("MainWindow", "layout", None, -1))
        self.pushButton_10.setText(QtWidgets.QApplication.translate("MainWindow", "animation", None, -1))
        self.pushButton_11.setText(QtWidgets.QApplication.translate("MainWindow", "lighting", None, -1))
        self.pushButton_25.setText(QtWidgets.QApplication.translate("MainWindow", "effect", None, -1))
        self.pushButton_24.setText(QtWidgets.QApplication.translate("MainWindow", "simulation", None, -1))
        self.pushButton_12.setText(QtWidgets.QApplication.translate("MainWindow", "comp", None, -1))
        self.treeWidget.headerItem().setText(0, QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "Character", None, -1))
        self.treeWidget.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "Vehicle", None, -1))
        self.treeWidget.topLevelItem(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "Set", None, -1))
        self.treeWidget.topLevelItem(3).setText(0, QtWidgets.QApplication.translate("MainWindow", "Prop", None, -1))
        self.treeWidget.topLevelItem(4).setText(0, QtWidgets.QApplication.translate("MainWindow", "Other", None, -1))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget_branch.setTabText(self.tabWidget_branch.indexOf(self.tab_job_assemble), QtWidgets.QApplication.translate("MainWindow", "job Assemble", None, -1))
        self.label_optionPage_projDescription.setText(QtWidgets.QApplication.translate("MainWindow", "project Description:", None, -1))
        self.label_optionPage_showFileType.setText(QtWidgets.QApplication.translate("MainWindow", "show File Type:", None, -1))
        self.label_optionPage_tempB.setText(QtWidgets.QApplication.translate("MainWindow", "temp_B:", None, -1))
        self.label_optionPage_userPref.setText(QtWidgets.QApplication.translate("MainWindow", "User Pref:", None, -1))
        self.label_optionPage_User.setText(QtWidgets.QApplication.translate("MainWindow", "current User:", None, -1))
        self.label_optionPage_workProj.setText(QtWidgets.QApplication.translate("MainWindow", "working Project :", None, -1))
        self.label_optionPage_branchFileInfo.setText(QtWidgets.QApplication.translate("MainWindow", "branch File Info position:", None, -1))
        self.plainTextEdit_optionPage_showFileType.setPlainText(QtWidgets.QApplication.translate("MainWindow", "ma,mb,rib,ass,zip", None, -1))
        self.label_optionPage_tempB_2.setText(QtWidgets.QApplication.translate("MainWindow", "Root :", None, -1))
        self.lineEdit_setRoot.setText(QtWidgets.QApplication.translate("MainWindow", "//mcd-3d/art_3d_project", None, -1))
        self.plainTextEdit_rootInput.setPlainText(QtWidgets.QApplication.translate("MainWindow", "//mcd-server", None, -1))
        self.tabWidget_branch.setTabText(self.tabWidget_branch.indexOf(self.tab_2), QtWidgets.QApplication.translate("MainWindow", "option Edit", None, -1))
        self.label_fileDescription.setText(QtWidgets.QApplication.translate("MainWindow", "File description:", None, -1))
        self.label_selectProject.setText(QtWidgets.QApplication.translate("MainWindow", "select Project", None, -1))
        self.label_currentProj.setText(QtWidgets.QApplication.translate("MainWindow", "current WorkSpace", None, -1))
        self.label_metaData.setText(QtWidgets.QApplication.translate("MainWindow", "Meta Data", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Create New Branch", None, -1))
        self.label_fileData_35.setText(QtWidgets.QApplication.translate("MainWindow", "Build", None, -1))


        #self.pushButton_saveFile.whatsThis.showText()





       ## self.tableWidget_FileList.verticalHeader().setDefaultSectionSize(28)#tableWidge verticalHeader space

       ## self.tableWidget_FileList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)   #add more control


        #setToolTips for all button
        #self.pushButton_inProgress.setToolTip("show the project in progress")
        #self.pushButton_recent.setToolTip("show the project recently, recent 20")
        #self.pushButton_complete.setToolTip("show the project, completed")
        
        self.pushButton_inProgress.setToolTip(("顯示正在執行中的專案").decode('big5'))
        
        self.pushButton_recent.setToolTip(("顯示最近20個專案").decode('big5'))
        self.pushButton_complete.setToolTip(("顯示已完成的專案").decode('big5'))


        self.pushButton_character.setToolTip(("角色").decode('big5'))
        
        self.pushButton_vehicle.setToolTip(("交通工具").decode('big5'))   
        self.pushButton_set.setToolTip(("場景").decode('big5'))   
        self.pushButton_props.setToolTip(("道具").decode('big5'))   
        self.pushButton_others.setToolTip(("其他").decode('big5'))   
        self.pushButton_all.setToolTip(("全部").decode('big5'))   
        self.pushButton_shot.setToolTip(u"shots")   
        
        self.pushButton_processConcept.setToolTip(u"concept")   
        self.pushButton_processModeling.setToolTip(u"modeling")   
        self.pushButton_processTexture.setToolTip(u"texture")   
        self.pushButton_processRigging.setToolTip(u"rigging")   
        self.pushButton_processLayout.setToolTip(u"layout")   
        self.pushButton_processAnimation.setToolTip(u"animation")   
        self.pushButton_processLighting.setToolTip(u"lighting")   
        self.pushButton_processEffects.setToolTip(u"effect")   
        self.pushButton_processSimulation.setToolTip(u"simulation")   
        self.pushButton_processComp.setToolTip(u"comp")   
        
        
        self.pushButton_createNewBranch.setToolTip(("創建新的分支，需填入分支名稱").decode('big5'))   
        #self.pushButton_mergeToMaster.setToolTip(u"儲存檔案到所選的分支，或master中")   
        #self.pushButton_openBranchJson.setToolTip(u"儲存檔案到所選的分支，或master中")  
         
        self.pushButton_saveFile.setToolTip(("儲存檔案到所選的分支，或master中").decode('big5'))   
        self.pushButton_loadFile.setToolTip(("讀取檔案").decode('big5'))   
        #self.pushButton_openFileJson.setToolTip(u"儲存檔案到所選的分支，或master中")   
        #self.pushButton_closeBranch.setToolTip(u"儲存檔案到所選的分支，或master中")  
         
        self.pushButton_editFileInfo.setToolTip(("寫入註解").decode('big5'))   
        #self.pushButton_openFolder.setToolTip(u"儲存檔案到所選的分支，或master中")  
         
        #self.pushButton_publish.setToolTip(u"儲存檔案到所選的分支，或master中")   
        #self.pushButton_syncFile.setToolTip(u"儲存檔案到所選的分支，或master中")   
        #self.pushButton_setting.setToolTip(u"儲存檔案到所選的分支，或master中")   
        #self.pushButton_reNewBranchDict.setToolTip(u"儲存檔案到所選的分支，或master中")   
        

    #user pref
    


        

class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #self.QTITEM.ACTION.connect(self.MODDEF)
        self.setupUi(self)
        
        #lock button not to use
        self.tabWidget_branch.setCurrentIndex(0)

        self.pushButton_mergeToMaster.setEnabled(False)
        
        try:
            pm.mel.eval('rmanLoadPlugin')
            rendermanPath = pm.mel.eval('getenv RMANTREE')
            pythonScriptPath = rendermanPath + 'lib/python2.7/Lib/site-packages'
            sys.path.append(pythonScriptPath)
            import ice

        except:
            print 'pls import prman plugin'
            pass

        
        

        #define project root
        #self.root = "C:/mayaProjs" #test in home
        self.root = "//mcd-server/art_3d_project"   # projects root in company
        #self.root = "//mcd-3d/art_3d_project"
        #self.root = self.lineEdit_setRoot.text()
        #self.doFromAdmin()
        
        self.getDataFromTactic()

        

        
        
        #creat projects Info in self.root
        #self.pushButton_setting.clicked.connect(self.doFromAdmin)
        
        
        

        #clear treeWidger_branches, all Clear
        #self.treeWidget_branches.clear()   #branch system
        #self.tableWidget_FileList.clear()  #branch system
        self.defineFont()
        #self.printOutProjectInfo()    #branch system
        
        self.initialItemBuild()

        #self.assetsOnOffTable = [0,0,0,0,0,1,0]
        #self.clickAssetShotSelectButton()
        #self.branchDict={"0":{"master":{}}} 
        
        self.pushButton_openBranchJson.clicked.connect(self.openFolder)
        #select project filter from tactic:
        self.pushButton_inProgress.clicked.connect(self.click_pushButton_inProgress)
        self.pushButton_recent.clicked.connect(self.click_pushButton_recent)
        self.pushButton_complete.clicked.connect(self.click_pushButton_complete)
        
        
        
        #select item from assetProj List_widget
        self.listWidget_assetProj.itemClicked.connect(self.click_assetProjListWidget)
        
        
        
        
       # self.pushButton_reNewBranchDict.clicked.connect(self.checkPublishToolTempFolder)
        
        self.pushButton_createNewBranch.clicked.connect(self.createNewBranchCombo)


        self.pushButton_mergeToMaster.clicked.connect(self.getSavingFile)
        
        self.treeWidget_branches.itemClicked.connect(self.createFileTable)
        
        self.tableWidget_FileList.itemClicked.connect(self.printOutFileInfo)
        
        self.pushButton_editFileInfo.clicked.connect(self.addDescriptionToTextFile)
        
        self.pushButton_saveFile.clicked.connect(self.getSavingFile)
        
        self.pushButton_loadFile.clicked.connect(self.openSelectFile)
        
        self.pushButton_openFolder.clicked.connect(self.readFileInof)
        
        #asset and Shot button def
        #1 character
        self.pushButton_character.clicked.connect(self.clickCharacterButton)
        #2 pushButton_vehicle
        self.pushButton_vehicle.clicked.connect(self.clickVehicleButton)
        #3 set
        self.pushButton_set.clicked.connect(self.clickSetButton)
        #4 props
        self.pushButton_props.clicked.connect(self.clickPropsButton)
        #5 others
        self.pushButton_others.clicked.connect(self.clickOthersButton)
        #6 all asset
        self.pushButton_all.clicked.connect(self.clickAllButton)
        #7 shot
        self.pushButton_shot.clicked.connect(self.clickShotButton)
        
        
        #process Type buttonb click
        self.pushButton_processConcept.clicked.connect(self.clickProcessConceptButton)
        self.pushButton_processModeling.clicked.connect(self.clickProcessModelingButton)
        self.pushButton_processTexture.clicked.connect(self.clickProcessTextureButton)
                                                            
        self.pushButton_processRigging.clicked.connect(self.clickProcessRiggingButton)
        self.pushButton_processLayout.clicked.connect(self.clickProcessLayoutButton)
        self.pushButton_processAnimation.clicked.connect(self.clickProcessAnimationButton)
        self.pushButton_processLighting.clicked.connect(self.clickProcessLightingButton)
        self.pushButton_processEffects.clicked.connect(self.clickProcessEffectsButton)
        self.pushButton_processSimulation.clicked.connect(self.clickProcessSimulationButton)
        self.pushButton_processComp.clicked.connect(self.clickProcessCompButton)
        self.pushButton_buildFolder.clicked.connect(self.buildProjectRequestFolderFromTactic)
        self.pushButton_gotPublish.clicked.connect(self.findAssetClassGaveAssetName)
        self.pushButton_gotoPublishFolder.clicked.connect(self.openPublishFolder)

        #selectProject ComboBox
        self.comboBox_selectProj.currentIndexChanged.connect(self.selectWorkingProjectInGlobalFromTactic)

        #test--------------------pushButton_setting
        #self.pushButton_syncFile.clicked.connect(self.defineWorkingProjectAssemble)
       # self.pushButton_publish.clicked.connect(self.test_processProjectGlobal)

        self.getCurrentLevelList = []
        
        #self.runUserPref()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    ######## Page publishTool
        ####initial UI#########
        
        
        
       # self.treeWidget_FiletOption.setExpanded   #自動展開 .setCheckState(0, QtCore.Qt.Checked) #設定勾選
        self.treeWidget_FiletOption.topLevelItem(0).setExpanded(1)#自動展開
        self.treeWidget_FiletOption.topLevelItem(1).setExpanded(1)#自動展開
        self.treeWidget_FiletOption.topLevelItem(2).setExpanded(1)#自動展開
        self.treeWidget_FiletOption.topLevelItem(3).setExpanded(1)#自動展開
     
       # self.treeWidget_FiletOption.topLevelItem(0).setCheckState(0, QtCore.Qt.Checked)#設定勾選   Collect Files
        self.treeWidget_FiletOption.topLevelItem(0).child(0).setCheckState(0, QtCore.Qt.Checked)#設定勾選   Prman Texture
        self.treeWidget_FiletOption.topLevelItem(0).child(1).setCheckState(0, QtCore.Qt.Checked)#設定勾選   Maya Texture
        self.treeWidget_FiletOption.topLevelItem(0).child(2).setCheckState(0, QtCore.Qt.Checked)#設定勾選   GpuCache
        self.treeWidget_FiletOption.topLevelItem(0).child(3).setCheckState(0, QtCore.Qt.Checked)#設定勾選   RibArchive
        self.treeWidget_FiletOption.topLevelItem(0).child(4).setCheckState(0, QtCore.Qt.Checked)#設定勾選   Alembic
        self.treeWidget_FiletOption.topLevelItem(0).child(5).setCheckState(0, QtCore.Qt.Unchecked)#設定勾選   Prman Light
        self.treeWidget_FiletOption.topLevelItem(0).child(6).setCheckState(0, QtCore.Qt.Unchecked)#設定勾選   Maya Fluid
        self.treeWidget_FiletOption.topLevelItem(0).child(7).setCheckState(0, QtCore.Qt.Unchecked)#設定勾選   Maya nParticle Cache
      #  self.treeWidget_FiletOption.topLevelItem(0).child(8).setCheckState(0, QtCore.Qt.Checked)#設定勾選
       # self.treeWidget_FiletOption.topLevelItem(0).child(9).setCheckState(0, QtCore.Qt.Checked)#設定勾選
    
       # self.treeWidget_FiletOption.topLevelItem(1).setCheckState(0, QtCore.Qt.Checked)#設定勾選  Check Plugin
        self.treeWidget_FiletOption.topLevelItem(1).child(0).setCheckState(0, QtCore.Qt.Checked)#設定勾選 unUsed Plugin
       # self.treeWidget_FiletOption.topLevelItem(1).child(9).setCheckState(0, QtCore.Qt.Checked)#設定勾選 
        
        
        
       # self.treeWidget_FiletOption.topLevelItem(2).setCheckState(0, QtCore.Qt.Checked)#設定勾選 Check Asset Unit
        self.treeWidget_FiletOption.topLevelItem(2).child(0).setCheckState(0, QtCore.Qt.Checked)#設定勾選 Check BB
        self.treeWidget_FiletOption.topLevelItem(2).child(1).setCheckState(0, QtCore.Qt.Checked)#設定勾選 Check Position
        self.treeWidget_FiletOption.topLevelItem(2).child(2).setCheckState(0, QtCore.Qt.Checked)#設定勾選 Check Repeat
        self.treeWidget_FiletOption.topLevelItem(2).child(3).setCheckState(0, QtCore.Qt.Checked)#設定勾選 ReName SG
        
        #self.treeWidget_FiletOption.topLevelItem(3).setCheckState(0, QtCore.Qt.Checked)#設定勾選 Duplicated ShapeName
        self.treeWidget_FiletOption.topLevelItem(3).child(0).setCheckState(0, QtCore.Qt.Checked)#設定勾選 #ribArchive shapes
        self.treeWidget_FiletOption.topLevelItem(3).child(1).setCheckState(0, QtCore.Qt.Checked)#設定勾選 #gpuCache shapes
        self.treeWidget_FiletOption.topLevelItem(3).child(2).setCheckState(0, QtCore.Qt.Checked)#設定勾選 #alembic shapes
        self.treeWidget_FiletOption.topLevelItem(3).child(3).setCheckState(0, QtCore.Qt.Unchecked)#設定勾選 #fluid shapes
        self.treeWidget_FiletOption.topLevelItem(3).child(4).setCheckState(0, QtCore.Qt.Unchecked)#設定勾選 #nparticle shapes
        #self.treeWidget_filesList.topLevelItem(0).setCheckState(0, QtCore.Qt.Unchecked)
        #set publishFileMode , default is publish Mode
        self.radioButton_publishMode.setChecked(True)
        
        
        self.treeWidget_filesList.clicked.connect(self.showFileName)
        self.pushButton_getSelectedNode.clicked.connect(self.getSelectedNode)
        
        self.pushButton_publishAll.clicked.connect(self.copyAllFilesToNewLocation)
        
        
        self.pushButton_uploadSyncA.clicked.connect(self.copyAllFilesToNewLocationSync)
        
        self.pushButton_refreshList.clicked.connect(self.reflashTree)
        self.pushButton_delectSelectItems.clicked.connect(self.delectChecked)
        
        self.treeWidget_filesList.doubleClicked.connect(self.replaceFile)
        
        self.pushButton_reName.clicked.connect(self.reNameDuplicateShapeName)
        
        self.pushButton_replaceFileRoot.clicked.connect(self.replaceFileRoot)   #replace all files root
        
        #self.pushButton_unCheckAll.clicked.connect(self.unSelectCheck)
        
        #self.treeWidget_filesList.itemClicked.connect(self.unSelectCheck)
        #self.treeWidget_filesList.
        self.linkingFilePreMoveDict = {}
        
        
        #define allDuplicateShapeNameDict,
        self.allDuplicateShapeNameDict ={'pxrTexture':{},
                                         'mayaTexture':{},
                                         'gpuCache':{},
                                         'ribArchive':{},
                                         'alembic':{},
                                         'pxrLight':{},
                                         'mayaFluid':{},
                                         'mayanParticle':{}
                                         }

        self.defineFont()

        self.countN1 = 0
        self.countN2 = 0
        self.countN3 = 0
        self.countN4 = 0
        self.countN5 = 0
        self.countN6 = 0
        self.countN7 = 0
        #countN8 = 0 
        self.countN9 = 0
        self.countN10 = 0
        self.countN11 = 0

        self.buildItemTree()
         
        #self.createNewItem()         
        
        ##############page 4 init###############
        
       # self.lineEdit_setRoot.textChanged.connect(self.reSetRoot)
        
        
        
        
        
        
        
    def openPublishFolder(self):
        
        if self.isAsset == True:
            
            openFolder = self.root +'/' +self.project +'/' + 'publish' +'/'+ 'assets'+'/'+ self.assetClass  +'/'+ self.assetNow +'/'+self.processNow +'/' +'scenes'
        else:            
        
            openFolder = self.root +'/' +self.project +'/' + 'publish' +'/'+ 'shot'+'/'+ self.assetNow +'/'+self.processNow  +'/' +'scenes'
            
        self.openFolderTypical(openFolder)



        
        
        
        
    def runUserPref(self):
        '''
        try:
            self.root = self.userPrefDict['self.root']
            self.lineEdit_setRoot.setText(self.root)
        except:
            self.root ="//mcd-3d/art_3d_project"
        '''    
            
        self.isAsset =True
        #userPrefFile = 
    #def self.comboBox_selectProj
        CSIDL_PERSONAL = 5       # My Documents
        SHGFP_TYPE_CURRENT = 0   # Get current, not default value

        buf= ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
        ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)

        self.userDoctFolder = (buf.value)
        
        self.userPrefFile = ""
        tempUserPrefFile = self.userDoctFolder + '/' + 'publishToolUserPref.json'
        
        for i in tempUserPrefFile:
            if i == '\\' :
                self.userPrefFile = self.userPrefFile + '/'
            else :
                self.userPrefFile = self.userPrefFile + i
        #self.userPrefFile = 'c:/temp/publishToolUserPref.json'
       
       # print' self.userPrefFile', self.userPrefFile
      #  f = open(self.userPrefFile,'w')
        
        
       # data = 'sdasdadasd'    
        #data = json.dumps(self.userPrefDict, sort_keys=True , indent =4)  #編譯成json 且賦予格式 控四格
       # f.write(data)
       # f.close
       # self.writeToUserPref() userPrefDict
        

    def writeToUserPref(self):
        f = open(self.userPrefFile,'w')
        
        
        #data = 'hello world'    
        data = json.dumps(self.userPrefDict, sort_keys=True , indent =4)  #編譯成json 且賦予格式 控四格
        f.write(data)
        f.close
       # dataName = open(fileName)
    
    
    def checkUserPrefFileExist(self):
        self.runUserPref()
        

        if os.path.isfile(self.userPrefFile) == True:
            print "the user pref file existed, and restored data from file"
            try:
                self.restoreUserPref()
            except:
                pass

        else:
            "publishToolUserPref, user/doctument/publishToolUserPref.json is not exist"
            self.userPrefDict= {}

            self.getDataFromTactic()

        #print self.userPrefDict
    def reSetRoot(self):
        self.root = self.lineEdit_setRoot.text()
       # print self.root
        self.userPrefDict.update({'self.root':self.root})
        self.writeToUserPref()
        
        
    def restoreUserPref(self):
        
        print 'restoreUserPref start'
        
        with open(self.userPrefFile) as data_file:    
            self.userPrefDict = json.load(data_file)
                
        print 'len of self.userPrefDict',len(self.userPrefDict)
        if len(self.userPrefDict) >= 1:
            
            #try:

            self.project = self.userPrefDict['self.project']
            print 'self.project',self.project
            self.setFromUserPref()
            #self.setFromUserPref()
            
                
            #except:
               # print "publishToolUserPref, user/doctument/publishToolUserPref.json is empty"

        else:

            print  "publishToolUserPref, user/doctument/publishToolUserPref.json is empty"

            self.userPrefDict= {}
            self.writeToUserPref()
        #self.isAsset = self.userPrefDict['self.isAsset']
        #print 'self.isAsset',self.isAsset

        
    
    
    
        #self.userPrefRestore = open(self.userPrefFile,'r')
        print 'restore self.userPrefDict from file', self.userPrefDict
        print 'restoreUserPref end'
  
  
    def setAssetShotButtonFromUserPref(self):
        #userPrefDict
        
        print " setAssetShotButtonFromUserPref start "
        self.checkIsAssetValue()
            
        print 'self.isAsset',self.isAsset

        
        self.assetClass = self.userPrefDict['self.assetClass']
        print 'self.assetClass',self.assetClass

        self.pushButton_character.setChecked(int(self.userPrefDict['assetsOnOffTable'][0]))
        self.pushButton_vehicle.setChecked(int(self.userPrefDict['assetsOnOffTable'][1]))
        self.pushButton_set.setChecked(int(self.userPrefDict['assetsOnOffTable'][2]))
        self.pushButton_props.setChecked(int(self.userPrefDict['assetsOnOffTable'][3]))
        self.pushButton_others.setChecked(int(self.userPrefDict['assetsOnOffTable'][4]))
        self.pushButton_all.setChecked(int(self.userPrefDict['assetsOnOffTable'][5]))
        self.pushButton_shot.setChecked(int(self.userPrefDict['assetsOnOffTable'][6]))
        #print 'self.isAsset',self.isAsset
        
        if  self.isAsset == True:
            self.pushButton_processConcept.setEnabled(True)
            self.pushButton_processModeling.setEnabled(True)
            self.pushButton_processTexture.setEnabled(True)
            self.pushButton_processRigging.setEnabled(True)
            self.pushButton_processLayout.setEnabled(False)
            self.pushButton_processAnimation.setEnabled(False)
            self.pushButton_processLighting.setEnabled(False)
            self.pushButton_processEffects.setEnabled(False)
            self.pushButton_processSimulation.setEnabled(False)
            self. pushButton_processComp.setEnabled(False)
            
        else:
            self.pushButton_processConcept.setEnabled(False)
            self.pushButton_processModeling.setEnabled(False)
            self.pushButton_processTexture.setEnabled(False)
            self.pushButton_processRigging.setEnabled(False)
            self.pushButton_processLayout.setEnabled(True)
            self.pushButton_processAnimation.setEnabled(True)
            self.pushButton_processLighting.setEnabled(True)
            self.pushButton_processEffects.setEnabled(True)
            self.pushButton_processSimulation.setEnabled(True)
            self. pushButton_processComp.setEnabled(True)
            
        
        self.buildAssetsList()
        self.listWidget_assetProj.setCurrentRow(int(self.userPrefDict['self.assetListItemRow']))
       # self.assetClass = self.userPrefDict['self.assetClass']
        print " setAssetShotButtonFromUserPref end "

        
        
    def setAssetProjListWidgetFromUserPref(self):
        print 'setAssetProjListWidgetFromUserPref start'
        #self.assetNow
        #self.assetListItemRow
        self.treeWidget_branches.clear
        self.checkIsAssetValue()
        self.assetNow = self.userPrefDict['self.assetNow']
        self.assetListItemRow = self.userPrefDict['self.assetListItemRow']

        
        self.pushButton_processConcept.setChecked(int(self.userPrefDict['self.processOnOffTable'][0]))
        self.pushButton_processModeling.setChecked(int(self.userPrefDict['self.processOnOffTable'][1]))
        self.pushButton_processTexture.setChecked(int(self.userPrefDict['self.processOnOffTable'][2]))
        self.pushButton_processRigging.setChecked(int(self.userPrefDict['self.processOnOffTable'][3]))
        self.pushButton_processLayout.setChecked(int(self.userPrefDict['self.processOnOffTable'][4]))
        self.pushButton_processAnimation.setChecked(int(self.userPrefDict['self.processOnOffTable'][5]))
        self.pushButton_processLighting.setChecked(int(self.userPrefDict['self.processOnOffTable'][6]))
        self.pushButton_processEffects.setChecked(int(self.userPrefDict['self.processOnOffTable'][7]))
        self.pushButton_processSimulation.setChecked(int(self.userPrefDict['self.processOnOffTable'][8]))
        self.pushButton_processComp.setChecked(int(self.userPrefDict['self.processOnOffTable'][9]))
        
        
        self.processNow = self.userPrefDict['self.processNow']

       # self.checkIsAssetValue()
        #print 'self.isAsset', type(self.isAsset)
        
        if self.isAsset == True:
           # print 'self.root',self.root
           # print 'self.project',self.project
            self.assetName= self.userPrefDict['self.assetName']
           # print 'self.processNow',self.processNow
            
            self.workProject = self.root + "/" + self.project + "/" + self.assetName + "/" + self.processNow
        else:

           # print 'self.root',self.root
           # print 'self.project',self.project
            self.shotName = self.userPrefDict['self.shotName']
          #  print 'self.processNow',self.processNow
            self.workProject = self.root + "/" + self.project + "/" + self.shotName + "/" + self.processNow
                        
            
        #print 'self.workProject',self.workProject 
        self.branchFileStore = self.userPrefDict['self.branchFileStore']
                                         #    aa['self.branchFileStore']
       # print "self.branchInfoFile.........:",self.userPrefDict['self.branchFileStore']

        self.checkMasterExist()
        self.buildExistFileInfoTree()
        self.buildTreeFromExistFileData()
    
        print 'setAssetProjListWidgetFromUserPref end'

        
        
        
        
        
        
        
    def setFromUserPref(self):
        print 'setFromUserPref start'

        self.setPushButton_ProjectSelect()    #restore what fillet button was checked
       # self.pushButton_inProgress.isChecked(True) 
        self.setWorkingProjFromUserPref()     #load project info, assets, shots from tactic data
        self.setAssetShotButtonFromUserPref() #restore what asset/shot class was checked
        self.setAssetProjListWidgetFromUserPref()
        
        
        self.setBranchItemSelectFromUserPref()
        self.getBranchInfoFromJson()

        try:
            self.setFileTableFromUserPref()
           # print 'self.branchDict',self.branchDict
            self.createFileTable()
            self.fileInfoLocation = self.userPrefDict['self.assetBranchFileDir']
          #  print 'self.fileInfoLocation',self.fileInfoLocation

        except:
            pass
        #self.fileInfoLocation = self.userPrefDict['self.assetBranchFileDir']
        #print 'self.fileInfoLocation',self.fileInfoLocation

       # self.printOutFileInfo()
     #   print 'self.root',self.root
      #  print 'self.project',self.project
      #  print 'self.assetClass',self.assetClass
      #  print 'self.assetNow ',self.assetNow 
        
        self.fileInfoLocation
        self.findAssetClass()
        
        
        
    def findAssetClass(self):
        
        
        
        
        allAssetList = {}
        
        self.projectAssembleDescriptionFile = self.userPrefDict['self.projectAssembleDescriptionFile'] 
        print 'self.projectAssembleDescriptionFile',self.projectAssembleDescriptionFile
        with open(self.projectAssembleDescriptionFile) as data_file:    
            self.projectAssembleDescription = json.load(data_file) 
            
        
        for assetClass in self.projectAssembleDescription['assets'].keys():   
            for assetItem in self.projectAssembleDescription['assets'][assetClass]:
                #print assetItem
                allAssetList.update({assetItem.split('.')[0]:assetItem.split('.')[1]})
                
        if self.isAsset == True:
                
            self.realSelectItemAssetClass = allAssetList[self.assetNow]
            
        else:
            pass
                
        #self.assetClass = self.realSelectItemAssetClass
       # print 'allAssetList',allAssetList
      #  print 'self.realSelectItemAssetClass',self.realSelectItemAssetClass
      


      
    def findAssetClassGaveAssetName(self):
        print 'findAssetClassGaveAssetName start'

        cmds.file( self.openPublishFileName, open=True,f=True )
        
    def getBranchInfoFromJson(self):
        fileName =  self.userPrefDict['self.branchFileStore']
        with open(fileName) as data_file:    
            data = json.load(data_file)
            
    

        self.branchDict={'0':{'master':{}}}
        for i in range(1,len(data.keys())):
            top = data[str(i)].keys()[0]
            self.branchDict.update({str(i):{top:{}}})
            for sec in data[str(i)][top]['folder'].keys():

                self.branchDict[str(i)][top].update({sec:{}})
                
                for third in data[str(i)][top]['folder'][sec]['folder'].keys():

                    self.branchDict[str(i)][top][sec].update({third:{}})



        
        
    def setFileTableFromUserPref(self):
        print 'setFileTableFromUserPref start'
        self.tableWidget_FileList.clear()
        #pprint(data)
        
    #def asss(self):
        print" run createFileTable function start..................."
        
        self.itemSelect =  self.treeWidget_branches.currentItem().text(0)
      #  print 'self.itemSelect',self.itemSelect
        
      #  print 'index',self.treeWidget_branches.indexOfTopLevelItem(self.treeWidget_branches.currentItem())
        self.getFilesInfoFromJson()
        

    def setBranchItemSelectFromUserPref(self):
        #select tree item from userPref
        
        print  "setBranchItemSelectFromUserPref   start"
      #  print self.userPrefDict['self.fullItemIndex']
       # print self.treeWidget_branches.topLevelWidget()
        #self.tree_widget.setCurrentItem(self.tree_widget.topLevelItem(0))

        if len(self.userPrefDict['self.fullItemIndex']) > 0 :
            print 'select branch item from user Pref'
    
            if self.userPrefDict['self.fullItemIndex'][0] == 'none':
                #print ' aaaa'
                pass
            else:
               # print 'bbb'
                topLevelIndex = int(self.userPrefDict['self.fullItemIndex'][0])
                self.treeWidget_branches.setCurrentItem(self.treeWidget_branches.topLevelItem(topLevelIndex))

             
                if self.userPrefDict['self.fullItemIndex'][1] == 'none':
                    pass
                else:
                    secLevelIndex =  int(self.userPrefDict['self.fullItemIndex'][1])
                    self.treeWidget_branches.setCurrentItem(self.treeWidget_branches.topLevelItem(topLevelIndex).child(secLevelIndex))
                                                   
                    if self.userPrefDict['self.fullItemIndex'][2] == 'none':
                        pass
                    else:
                        thirdLevelIndex = int(self.userPrefDict['self.fullItemIndex'][2])
                        self.treeWidget_branches.setCurrentItem(self.treeWidget_branches.topLevelItem(topLevelIndex).child(secLevelIndex).child(thirdLevelIndex))
    
        else:
            pass
            
          
                    
        #self.treeWidget_branches.setCurrentItem(self.treeWidget_branches.topLevelItem(0).child().child())
       # self.treeWidget_branches.

    def getDataFromTactic(self):
        print "run getDataFromTactic start"
        scripts_path = "//Art-1405260002/d/assets"
        sys.path.append(scripts_path +  "/client")
        sys.path.append(scripts_path + "/scripts/tactic_scripts/ui")
        from tactic_client_lib import TacticServerStub

        server = TacticServerStub(setup=False)
       # tactic_server_ip = socket.gethostbyname("vg.com")
        
        
        try:
            tactic_server_ip = socket.gethostbyname("vg.com")
        except:
            tactic_server_ip = "192.168.163.60"


        server.set_server(tactic_server_ip)
        server.set_project("simpleslot")
        ticket = server.get_ticket("julio", "1234")
        server.set_ticket(ticket)

        # export projects in Tactic
        expr = "@SOBJECT(simpleslot/game)"
        self.projectsInTactic = server.eval(expr)


        # export assets
        expr = "@SOBJECT(simpleslot/assets)"
        self.assetsInTactic = server.eval(expr)

        # export shots
        expr = "@SOBJECT(simpleslot/shot)"
        self.shotsInTactic = server.eval(expr)
        print "run getDataFromTactic End"
        
        
        
    def getDataFromTacticFile(self):

        tacticProjectFile = "C:/mayaProjs/global/projectInTactic.json"

        tacticssetsFile = "C:/mayaProjs/global/assetsInTactic.json"

        tacticShotsFile = "C:/mayaProjs/global/shotsInTactic.json"


        import json
        from pprint import pprint

        with open(tacticProjectFile, 'r') as f:
            self.projectsInTactic = json.load(f)
            
        with open(tacticssetsFile, 'r') as f:
            self.assetsInTactic = json.load(f)
            
        with open(tacticShotsFile, 'r') as f:
            self.shotsInTactic = json.load(f)
            
            
            
    #----------------------click push button, inProgress, _recent, _complete-----------------------------------------------------------
    def setPushButton_ProjectSelect(self):
        print "setPushButton_ProjectSelect start"
        
        
        self.pushButton_inProgress.setChecked(int(self.userPrefDict['projectFilectButtonChecked'][0]))
        self.pushButton_recent.setChecked(int(self.userPrefDict['projectFilectButtonChecked'][1]))

        self.pushButton_complete.setChecked(int(self.userPrefDict['projectFilectButtonChecked'][2]))

        self.progressType = self.userPrefDict['self.progressType']
      #  print 'self.progressType,check setPushButton_a01',self.progressType
        
        self.selectProjectFromTactic()

        
            
    def click_pushButton_inProgress(self):
        print "set to in Progress"
        self.pushButton_inProgress.setChecked(True)
        self.pushButton_recent.setChecked(False)
        self.pushButton_complete.setChecked(False)
        self.progressType = "inProgress"
        self.selectProjectFromTactic()
        
        self.userPrefDict.update({'projectFilectButtonChecked':['1','0','0']})
        self.userPrefDict.update({'self.progressType':'inProgress'})
        
        self.writeToUserPref()
        
    def click_pushButton_recent(self):
        print "set to recent"
        self.pushButton_inProgress.setChecked(False)
        self.pushButton_recent.setChecked(True)
        self.pushButton_complete.setChecked(False)
        self.progressType = "recent"
        self.selectProjectFromTactic()
        
        self.userPrefDict.update({'projectFilectButtonChecked':['0','1','0']})
        self.userPrefDict.update({'self.progressType':'recent'})
        
        self.writeToUserPref()
        
        
    def click_pushButton_complete(self):
        print "set to complete"
        self.pushButton_inProgress.setChecked(False)
        self.pushButton_recent.setChecked(False)
        self.pushButton_complete.setChecked(True)
        self.progressType = "complete"
        self.selectProjectFromTactic()
        
        self.userPrefDict.update({'projectFilectButtonChecked':['0','0','1']})
        self.userPrefDict.update({'self.progressType':'complete'})
        
        self.writeToUserPref()
    #-----------------------------------------------------------------------------------------------------------------------





    #---------------------------selectProjectFromTactic----------------------------------

        
    def selectProjectFromTactic(self):
        
        print 'run selectProjectFromTactic'
        
        #self.getDataFromTactic() projectsInTactic
        # input self.progressType
        
        #self.projectsInTactic , all projects in Tactics
        tempProjList = []
        self.projectFilter = []
        if self.progressType == "inProgress":
            print "set to in Progress"
            
            
            for i in self.projectsInTactic:
                if i['project_status'] == '.In Progress':
                    self.projectFilter.append(i['name'])
            
        elif self.progressType == "recent":
            print "set to recent"
            
            for i in self.projectsInTactic:
                #print i['timestamp']
                #tempProjList.append(i['timestamp'])
                tempProjList.append({i['timestamp']:i['name']})
                
               
            for i in tempProjList[-10:]:
                self.projectFilter.append(i[i.keys()[0]])
            
            
        else:
            print "set to complete"
            for i in self.projectsInTactic:
                if i['project_status'] == '.Complete':
                    #print i['name']
                    self.projectFilter.append(i['name'])
                
        self.buildProjectComboBox()
        #self.writeToUserPref()
        #self.comboBox_selectProj.setCurrentIndex(33)
        #self.comboBox_selectProj.

    #-----------------------------------------------------------------------------------------------------------------------    

            
            
            
    #----------------------------------------selectWorkingProjectInGlobalFromTactic----------------------------------------------------
    def setWorkingProjFromUserPref(self):
        print "setWorkingProjFromUserPref start"
        
        
        
        
        #print 'self.comboBox_selectProj.setCurrentIndex' , self.userPrefDict['itemSelectIndexInComboBox']
        
       # print 'self.comboBox_selectProj.itemName',self.userPrefDict['itemSelectNameInComboBox']
     
        self.comboBox_selectProj.setCurrentIndex(int(self.userPrefDict['itemSelectIndexInComboBox']))
   
        self.assetsSelectInfoFromTactic = []
        self.shotsSelectInfoFromTactic = []
        
        # get project info from select item on comboBox ,date in tactic  , export self.projectSelectInfoFromTactic,self.project,self.projectCode
                
        for i in self.projectsInTactic:
            if i['name'] == self.project:
                self.projectSelectInfoFromTactic = i
                self.project = i['name']
                self.projectCode = i['code']
                
       # print self.projectCode
       # print self.assetsInTactic
       # print self.shotsInTactic
        
                
        # get assets info from select item on comboBox ,date in tactic
        for i in self.assetsInTactic:
            if i['game_code'] == self.projectCode:
                if i['asset_type_code'] == 'ASSET_TYPE00002' :
                    i['asset_type_code'] = 'character'
                    
                elif i['asset_type_code'] == 'ASSET_TYPE00003' :
                    i['asset_type_code'] = 'vehicle'
            
                elif i['asset_type_code'] == 'ASSET_TYPE00004' :
                    i['asset_type_code'] = 'set'
                    
                elif i['asset_type_code'] == 'ASSET_TYPE00005' :
                    i['asset_type_code'] = 'prop'
                    
                elif i['asset_type_code'] == 'ASSET_TYPE00006' :
                    i['asset_type_code'] = 'other'
                    
                    
                   # selectWorkingProjectInGlobalFromTactic
                self.assetsSelectInfoFromTactic.append(i)

                
        for i in self.shotsInTactic:
            if i['game_code'] == self.projectCode:
                self.shotsSelectInfoFromTactic.append(i)
        
        self.defineWorkingProjectAssembleFromTactic()
        
        self.listWidget_assetProj.clear()
        self.clickAssetShotSelectButton()
        #self.clickAllButton()
        
        print "setWorkingProjFromUserPref end"

        
    def selectWorkingProjectInGlobalFromTactic(self):
        #1. input self.project from select combobox item
        #2. output self.project           , item Name in comboBox
        #3. output self.currentProjectComboBoxIndex, item index in comboBox selectWorkingProjectInGlobalFromTactic
        #4. output 

     
        print "run selectWorkingProjectInGlobalFromTactic moudle start"
        print "choose a project and list all data from select in Tactic"
        self.project = self.comboBox_selectProj.currentText()  #1. input self.project from select combobox item
        
        self.currentProjectComboBoxIndex = self.comboBox_selectProj.currentIndex()
        
        self.userPrefDict.update({'itemSelectNameInComboBox':self.project})
        self.userPrefDict.update({'itemSelectIndexInComboBox':self.currentProjectComboBoxIndex})
        self.userPrefDict.update({'self.project':self.project})
        #print 'self.userPrefDict',self.userPrefDict
      
        self.writeToUserPref()

        self.assetsSelectInfoFromTactic = []
        self.shotsSelectInfoFromTactic = []
        
        # get project info from select item on comboBox ,date in tactic  , export self.projectSelectInfoFromTactic,self.project,self.projectCode
                
        for i in self.projectsInTactic:
            if i['name'] == self.project:
                self.projectSelectInfoFromTactic = i
                self.project = i['name']
                self.projectCode = i['code']
                

        for i in self.assetsInTactic:
            if i['game_code'] == self.projectCode:
                if i['asset_type_code'] == 'ASSET_TYPE00002' :
                    i['asset_type_code'] = 'character'
                    
                elif i['asset_type_code'] == 'ASSET_TYPE00003' :
                    i['asset_type_code'] = 'vehicle'
            
                elif i['asset_type_code'] == 'ASSET_TYPE00004' :
                    i['asset_type_code'] = 'set'
                    
                elif i['asset_type_code'] == 'ASSET_TYPE00005' :
                    i['asset_type_code'] = 'prop'
                    
                elif i['asset_type_code'] == 'ASSET_TYPE00006' :
                    i['asset_type_code'] = 'other'
                    
                    
                   # selectWorkingProjectInGlobalFromTactic
                self.assetsSelectInfoFromTactic.append(i)

        for i in self.shotsInTactic:
            if i['game_code'] == self.projectCode:
                self.shotsSelectInfoFromTactic.append(i)
      

        self.defineWorkingProjectAssembleFromTactic()
        
        self.listWidget_assetProj.clear()
        self.clickAssetShotSelectButton()
        self.clickAllButton()
        

        print "run selectWorkingProjectInGlobalFromTactic moudle End"

                
    #---------------------------------------------------------------------------------------------------------------------------------
    
    
    
    ##################################### build all default folder start   #################################
    def buildProjectRequestFolderFromTactic(self):
        print 'buildProjectRequestFolderFromTactic start '
        #build all request folder when push button, self.pushButton_buildFolder()
        self.plainTextEdit_BranchFileInfo.clear()
        self.plainTextEdit_BranchFileInfo.setPlainText('build all folders from tactic info')

        #projectAssembleDescriptionFile = self.root +'/' +self.project +'/'+'global'+'/'+self.project+'_assembleDescription.json'
        #print projectAssembleDescriptionFile
        creatProjectFolder = self.root + '/' +self.project
        self.createNewFolder(creatProjectFolder)

        self.getAllRequestFolder()

    def createAllRequestFolder(self):
        self.requestFolder= ['assets',
                            'assets/character',
                            'assets/vehicle',
                            'assets/set',
                            'assets/prop',
                            'assets/other',                        
                            'shot',
                            'output',
                            'publish',
                            'publish/global',                            
                            'publish/shot',
                            'publish/assets',
                            'publish/assets/character',
                            'publish/assets/vehicle',
                            'publish/assets/set',
                            'publish/assets/prop',
                            'publish/assets/other',                            
                            'QC',
                            'global',
                            'global/shot',
                            'global/assets',
                            'global/assets/character',
                            'global/assets/vehicle',
                            'global/assets/set',
                            'global/assets/prop',
                            'global/assets/other',                     
                            'reference']    
        
        
        for i in self.requestFolder:
            requestSiginalFolder = self.root + '/' +self.project +'/' +i
            self.createNewFolder(requestSiginalFolder)

    def createNewFolder(self,createFolder):
        
        try:
            os.mkdir(createFolder)
        except:
            pass
        
            
    def getAllRequestFolder(self):
        self.getDataFromTactic() #
        self.getSelectProjectInfoFromTactic()
   
        self.defineWorkingProjectAssembleFromTactic()
        self.projectAssembleDescription['shot']
        
        self.projectAssembleDescription['assets']
        
        allShots = self.projectAssembleDescription['shot'].keys() # get all shots items
            
        #print 'allShots',allShots
        allAssets = []
        for i in range(0,len(self.projectAssembleDescription['assets'].keys())):
            #print self.projectAssembleDescription['assets'][self.projectAssembleDescription['assets'].keys()[i]] # get all assets types,character,set,other
            for j in range(0,len(self.projectAssembleDescription['assets'][self.projectAssembleDescription['assets'].keys()[i]].keys())):
                allAssets.append(self.projectAssembleDescription['assets'][self.projectAssembleDescription['assets'].keys()[i]].keys()[j])
                
        self.createAllRequestFolder()
        

                
        mayaDefaultFolderList =['data','data/alembic','data/mayaFluidCache','data/nParticleCache','images','sourceimages','scenes','scenes/master','renderman','renderman/ribarchives/']

        #build all assets folder
        for i in allAssets:
            #requestSiginalPublishRootFolder = self.root + '/' +self.project +'/' + 'publish'+ '/' + 'assets'+ '/' +i.split('.')[1]
           # requestSiginalGlobalRootFolder = self.root + '/' +self.project +'/' + 'global'+ '/' + 'assets'+ '/' +i.split('.')[1]
            requestSiginalFolder = self.root + '/' +self.project +'/' + 'assets'+ '/' +i.split('.')[1] +'/'+ i.split('.')[0]
            requestSiginalFolderInPublish = self.root + '/' +self.project +'/' + 'publish'+'/' + 'assets'+ '/' +i.split('.')[1] +'/'+ i.split('.')[0]
            requestSiginalFolderInGlobal = self.root + '/' +self.project +'/' + 'global' +'/'+ 'assets'+ '/' +i.split('.')[1] +'/'+ i.split('.')[0]
           # print 'requestSiginalPublishRootFolder',requestSiginalPublishRootFolder
           # print 'requestSiginalGlobalRootFolder',requestSiginalGlobalRootFolder

            #print 'requestSiginalFolder',requestSiginalFolder
           # print 'requestSiginalFolderInPublish',requestSiginalFolderInPublish
           # print 'requestSiginalFolderInGlobal',requestSiginalFolderInGlobal
            self.createNewFolder(requestSiginalFolder)
            self.createNewFolder(requestSiginalFolderInGlobal)
            self.createNewFolder(requestSiginalFolderInPublish)

            processList = ['concept','model','texture','rigging']
            for j in processList : 
                createFolder = requestSiginalFolder +'/' + j
                createFolderInPublish = requestSiginalFolderInPublish +'/' + j
               # print createFolder
               # print createFolderInPublish
                self.createNewFolder(createFolder)
                self.createNewFolder(createFolderInPublish)

                for folder in mayaDefaultFolderList:
                    mayaDefaultFolderListCreatePath = createFolder + '/'+ folder
                    mayaDefaultFolderListCreatePathInPublish = createFolderInPublish + '/'+ folder
                   #print mayaDefaultFolderListCreatePath
                   # print mayaDefaultFolderListCreatePathInPublish
                    self.createNewFolder(mayaDefaultFolderListCreatePath)
                    self.createNewFolder(mayaDefaultFolderListCreatePathInPublish)


    
        #biild all Shots Folder
        
        for i in allShots:          
            requestShotSiginalFolder = self.root + '/' +self.project +'/' + 'shot'+ '/' +i
            requestShotSiginalFolderInPublish = self.root + '/' +self.project +'/'+'publish'+'/' + 'shot'+ '/' +i
            requestShotSiginalFolderInGlobal = self.root + '/' +self.project +'/'+'global'+'/' + 'shot'+ '/' +i

            #print requestShotSiginalFolder
            #print requestShotSiginalFolderInPublish
            #print requestShotSiginalFolderInGlobal
            self.createNewFolder(requestShotSiginalFolder)
            self.createNewFolder(requestShotSiginalFolderInPublish)
            self.createNewFolder(requestShotSiginalFolderInGlobal)

            processList = ['layout','animation','lighting','effects','simulation']
            for j in processList : 
                createFolder = requestShotSiginalFolder +'/' + j
                createFolderInPublish = requestShotSiginalFolderInPublish +'/' + j
               # print createFolder
               # print createFolderInPublish
                self.createNewFolder(createFolder)
                self.createNewFolder(createFolderInPublish)

                                        

                for folder in mayaDefaultFolderList:
                    mayaDefaultFolderListCreatePath = createFolder + '/'+ folder
                    mayaDefaultFolderListCreatePathInPublish = createFolderInPublish + '/'+ folder
                    self.createNewFolder(mayaDefaultFolderListCreatePath)
                    self.createNewFolder(mayaDefaultFolderListCreatePathInPublish)

        #print self.project
       # print self.shotsSelectInfoFromTactic
       # print self.assetsSelectInfoFromTactic
    ##################################### build all default folder end   #################################
              
        
        


    def getSelectProjectInfoFromTactic(self):
        
        
        
        self.assetsSelectInfoFromTactic = []
        self.shotsSelectInfoFromTactic = []
        
                
        for i in self.projectsInTactic:
            if i['name'] == self.project:
                self.projectSelectInfoFromTactic = i
                self.project = i['name']
                self.projectCode = i['code']
       # print self.projectCode

        for i in self.assetsInTactic:
            if i['game_code'] == self.projectCode:
                if i['asset_type_code'] == 'ASSET_TYPE00002' :
                    i['asset_type_code'] = 'character'
                    
                elif i['asset_type_code'] == 'ASSET_TYPE00003' :
                    i['asset_type_code'] = 'vehicle'
            
                elif i['asset_type_code'] == 'ASSET_TYPE00004' :
                    i['asset_type_code'] = 'set'
                    
                elif i['asset_type_code'] == 'ASSET_TYPE00005' :
                    i['asset_type_code'] = 'prop'
                    
                elif i['asset_type_code'] == 'ASSET_TYPE00006' :
                    i['asset_type_code'] = 'other'
                    
                    
                   # selectWorkingProjectInGlobalFromTactic
                self.assetsSelectInfoFromTactic.append(i)

        for i in self.shotsInTactic:
            if i['game_code'] == self.projectCode:
                self.shotsSelectInfoFromTactic.append(i)
                
        #print self.project
        #print self.shotsSelectInfoFromTactic
        #print self.assetsSelectInfoFromTactic
              
    
    
    
    def selectWorkingProjectInGlobal(self):
        #print "run select working project"
        
        self.project = self.comboBox_selectProj.currentText()
       # print self.project
        

       # self.assetClass = 'all'
        self.defineWorkingProjectAssemble()       
        #self.clickAllButton() 
       # checkAssetsFolder = self.root + '/' + self.project + '/' +'assets'
        #check the assets folder in self.project is exist
        #檢查在專案目錄下 assets資料夾是否存在
       # if os.path.isdir(checkAssetsFolder) == True:
       #     self.buildAssetsList()
       # else:
        #    pass projectCode
    
    

        
    def buildAssetsList(self):
        print "build list from workingProjectAssemble description file"
        # 1.get data form dictionary , self.projectAssembleDescription
        # 2. self.projectAssembleDescription stored in self.projectAssembleDescriptionFile
        # 3. show all assets in list, defaut set button to click 'all' setAssetTypeSelect
        # 
       # self.defineWorkingProjectAssemble() isAsset
        
        f= open(self.projectAssembleDescriptionFile, 'r')
        data = json.load(f)
        #print data
        #self.projectAssembleDescription = json.dumps(data, sort_keys=True , indent =4) 
        self.projectAssembleDescription = data
        #print self.projectAssembleDescription.keys()
       # print self.projectAssembleDescription['assets'] selectWorkingProjectInGlobal buildAssetsList setAssetTypeSelect
        assetTempListNoSort = []
        if self.assetClass == "all":
            print "asset Type is all"
            for i in self.projectAssembleDescription['assets'].keys():
               # print i
                for j in self.projectAssembleDescription['assets'][i].keys():
                    assetTempListNoSort.append(j)
           # print assetTempList
            assetTempList=sorted(assetTempListNoSort)
            
            #build assets list
            listIndexCount = len(assetTempList)
            self.listWidget_assetProj.clear()
            for indexNum in range(0 ,listIndexCount):
               # print indexNum
                
                QtWidgets.QListWidgetItem(self.listWidget_assetProj)
                self.listWidget_assetProj.item(indexNum).setText(QtWidgets.QApplication.translate("MainWindow", "tempName", None, -1))
                self.listWidget_assetProj.item(indexNum).setText(assetTempList[indexNum].split('.')[0])
            
        elif self.assetClass == "character":
            print "asset Type is character"

            for i in self.projectAssembleDescription['assets']['character'].keys():
                    assetTempListNoSort.append(i)
                    
            
            assetTempList =sorted(assetTempListNoSort)
            listIndexCount = len(assetTempList)
            self.listWidget_assetProj.clear()
            for indexNum in range(0 ,listIndexCount):
                
                QtWidgets.QListWidgetItem(self.listWidget_assetProj)
                self.listWidget_assetProj.item(indexNum).setText(QtWidgets.QApplication.translate("MainWindow", "tempName", None, -1))
                self.listWidget_assetProj.item(indexNum).setText(assetTempList[indexNum].split('.')[0])
            

        elif self.assetClass == "vehicle":
            print "asset Type is vehicle"
            
            for i in self.projectAssembleDescription['assets']['vehicle'].keys():
                    assetTempListNoSort.append(i)
            assetTempList=sorted(assetTempListNoSort)
            listIndexCount = len(assetTempList)
            self.listWidget_assetProj.clear()
            for indexNum in range(0 ,listIndexCount):
                
                QtWidgets.QListWidgetItem(self.listWidget_assetProj)
                self.listWidget_assetProj.item(indexNum).setText(QtWidgets.QApplication.translate("MainWindow", "tempName", None, -1))
                self.listWidget_assetProj.item(indexNum).setText(assetTempList[indexNum].split('.')[0])
                

        elif self.assetClass == "set":
            print "asset Type is set"
            
            for i in self.projectAssembleDescription['assets']['set'].keys():
                    assetTempListNoSort.append(i)
            assetTempList=sorted(assetTempListNoSort)
            listIndexCount = len(assetTempList)
            self.listWidget_assetProj.clear()
            for indexNum in range(0 ,listIndexCount):
                
                QtWidgets.QListWidgetItem(self.listWidget_assetProj)
                self.listWidget_assetProj.item(indexNum).setText(QtWidgets.QApplication.translate("MainWindow", "tempName", None, -1))
                self.listWidget_assetProj.item(indexNum).setText(assetTempList[indexNum].split('.')[0])
                
        elif self.assetClass == "prop":
            print "asset Type is prop"

            for i in self.projectAssembleDescription['assets']['prop'].keys():
                    assetTempListNoSort.append(i)
            assetTempList=sorted(assetTempListNoSort)
            listIndexCount = len(assetTempList)
            self.listWidget_assetProj.clear()
            for indexNum in range(0 ,listIndexCount):
                
                QtWidgets.QListWidgetItem(self.listWidget_assetProj)
                self.listWidget_assetProj.item(indexNum).setText(QtWidgets.QApplication.translate("MainWindow", "tempName", None, -1))
                self.listWidget_assetProj.item(indexNum).setText(assetTempList[indexNum].split('.')[0])
    
        elif self.assetClass == "other":
            print "asset Type is other"

            for i in self.projectAssembleDescription['assets']['other'].keys():
                    assetTempListNoSort.append(i)
            assetTempList=sorted(assetTempListNoSort)
            listIndexCount = len(assetTempList)
            self.listWidget_assetProj.clear()
            for indexNum in range(0 ,listIndexCount):
                
                QtWidgets.QListWidgetItem(self.listWidget_assetProj)
                self.listWidget_assetProj.item(indexNum).setText(QtWidgets.QApplication.translate("MainWindow", "tempName", None, -1))
                self.listWidget_assetProj.item(indexNum).setText(assetTempList[indexNum].split('.')[0])
                                            
        elif self.assetClass == "shot":
            print "asset Type is shot"

            for i in self.projectAssembleDescription['shot'].keys():
                    assetTempListNoSort.append(i)
            assetTempList=sorted(assetTempListNoSort)
            listIndexCount = len(assetTempList)
            self.listWidget_assetProj.clear()
            for indexNum in range(0 ,listIndexCount):
                
                QtWidgets.QListWidgetItem(self.listWidget_assetProj)
                self.listWidget_assetProj.item(indexNum).setText(QtWidgets.QApplication.translate("MainWindow", "tempName", None, -1))
                self.listWidget_assetProj.item(indexNum).setText(assetTempList[indexNum].split('.')[0])
                
        else:
            pass
                                                        
            
            
            
            
        
        

    def doFromAdmin(self):
       # print self.root
        self.selectProj()
        self.saveProjectsInGlobalFile()        
        
        
        
        
        
        
    
    def test_processProjectGlobal(self):
        
        print "run test_processProjectGlobal start" 
        self.buildProjectComboBox()
        self.defineWorkingProjectAssemble()
        print "run test_processProjectGlobal End" 
        
        
        
        
        
        
    
    def selectProj(self):
    # get all folder in self.root
    # 取得所有位於self.root 的所有資料夾
    # 
        searchFolder = os.listdir(self.root)
        self.allProjectsInRoot = {}
        for i in searchFolder:
            searchFile = self.root + '/' +i
           # print os.path.isdir(searchFile)

            if os.path.isdir(searchFile) == True:
                self.allProjectsInRoot.update({i:{}})
        #print self.allProjectsInRoot
                

    def saveProjectsInGlobalFile(self):
        # 1. define the all projects in root global file name.
        # 2. store all folder description in file.
        # 1. 定義 所有的project描述檔案的檔名
        # 2. 儲存定義檔於 global
        
        self.projectsGlobalFile = self.root + '/' + 'global' + '/' + 'allProjectDescription.json'
        f = open( self.projectsGlobalFile , 'w')
        data = json.dumps(self.allProjectsInRoot, sort_keys=True , indent =4) 
        f.write(data)
        f.close
        
    def buildProjectComboBoxB(self):  # get project from home disk
        
        print "run buildProjectComboBox start"
        #1. get info from projects description file.
        #2. build comboBox form info file.
        #1. 取得現有專案資料
        #2. 建立 comboBox
        #self.projectFilter
        ## get data from json file
        self.projectsGlobalFile = self.root + '/' + 'global' + '/' + 'allProjectDescription.json'
        #print self.projectsGlobalFile
        f = open(self.projectsGlobalFile)
        data = json.load(f)
        # print json.dumps(data, sort_keys=True , indent =4) 
        f.close
        
        items = data.keys()
        itemsTotalIndexNum = len(items)
        self.comboBox_selectProj.clear()
        for i in range(0,itemsTotalIndexNum):
            self.comboBox_selectProj.addItem("")
            self.comboBox_selectProj.setItemText(i, QtWidgets.QApplication.translate("MainWindow",'tmepName', None, -1))
            self.comboBox_selectProj.setItemText(i,items[i])

        print "run buildProjectComboBox End"

        
    def buildProjectComboBox(self):  # get project from tactic
        
        print "run buildProjectComboBox start"
        #1. get info from self.projectFilter, from tactic
        #2. build comboBox form info file.
        #1. 取得現有專案資料
        #2. 建立 comboBox
        #self.projectFilter

        items = sorted(self.projectFilter)
        itemsTotalIndexNum = len(items)
        self.comboBox_selectProj.clear()
        for i in range(0,itemsTotalIndexNum):
            self.comboBox_selectProj.addItem("")
            self.comboBox_selectProj.setItemText(i, QtWidgets.QApplication.translate("MainWindow",'tmepName', None, -1))
            self.comboBox_selectProj.setItemText(i,items[i])

        print "run buildProjectComboBox End"
        
    def defineWorkingProjectAssembleFromTactic(self):
        
        
       # print self.projectSelectInfoFromTactic
       # print self.project
       # print self.projectCode
       # print self.assetsSelectInfoFromTactic
       # print self.shotsSelectInfoFromTactic
        print "run defineWorkingProjectAssemble from Tactic start"
        print "build all request folder in selected project folder"
        self.project = self.comboBox_selectProj.currentText()

        #default folder in self.project
        requestFolder= ['assets',
                        'assets/character',
                        'assets/vehicle',
                        'assets/set',
                        'assets/prop',
                        'assets/other',                        
                        'shot',
                        'output',
                        'publish',
                        'QC',
                        'global',
                        'global/shot',
                        'global/assets',
                        'global/assets/character',
                        'global/assets/vehicle',
                        'global/assets/set',
                        'global/assets/prop',
                        'global/assets/other',                     
                        'reference']


        #print requestFolder
        #check the request folder is exist in self.project ,and create folder

        for i in requestFolder:
            searchFolder = self.root + '/' + self.project +'/' + i
            self.createNewFolder(searchFolder)


        print "built all request folder done"
        
                
                
                
        self.projectAssembleDescription ={'assets':{'character':{},
                                                    'vehicle':{},
                                                    'set':{},
                                                    'prop':{},
                                                    'other':{}},
                                          'shot':{}}
        
        

        self.allAssetTempList = []

        for i in self.assetsSelectInfoFromTactic:    
            assetClassItem= i['asset_type_code']
            assetItem = i['name']
            

            self.projectAssembleDescription['assets'][assetClassItem].update({'%s.%s'%(assetItem,assetClassItem):{}})
            self.allAssetTempList.append('%s.%s'%(assetItem,assetClassItem))

        for i in self.shotsSelectInfoFromTactic:
            shotItem = i['name']
                #print shotItem
            self.projectAssembleDescription['shot'].update({shotItem:{}})
            self.allAssetTempList.append('%s.shot'%shotItem)
        print "define self.projectAssembleDescriptionFile,in %s/global/%s__assembleDescription.json"%(self.project,self.project)
        self.projectAssembleDescriptionFile = self.root + '/' + self.project + '/' +'global'+ '/' + self.project + '_assembleDescription.json'
       # print 'self.projectAssembleDescriptionFile',self.projectAssembleDescriptionFile
        
        #if os.path.isfile(self.projectAssembleDescriptionFile) == True:
        #    f = open(self.projectAssembleDescriptionFile,'r+')
        #else:       
        f = open(self.projectAssembleDescriptionFile,'w')
            
        data = json.dumps(self.projectAssembleDescription, sort_keys=True , indent =4) 
        f.write(data)
        f.close
        self.userPrefDict.update({'self.projectAssembleDescriptionFile':self.projectAssembleDescriptionFile})
        self.writeToUserPref
       # print 'self.projectAssembleDescription',self.projectAssembleDescription
        print "run defineWorkingProjectAssemble End"


    
    def defineWorkingProjectAssemble(self):  
        # 1. 輸入 self.root,   
        # 1.2 check 專案下的folder是否存在, 創建 assets, shot, output, publish, QC, reference,global
        # 1.2.1 check self.root / self.project / global /assets
        # 1.2.1.1 check self.root / self.project / global /assets/    charcter,vehicle,set,prop,other


        # 1.2.2 check self.root / self.project / global /shot

        # 2. 輸入 執行的專案資料夾, self.project,
        # 3. 輸出 專案組成的 dictionary, self.projectAssembleDescription
        # 
        # 4. 輸出 寫入到 cache檔案, self.root / self.project / global / self.project + '_assembleDescription.json'
        #self.root = "//mcd-server/art_3d_project" #at company
        #get self.project
        #itemsTotalIndexNum
        print "run defineWorkingProjectAssemble start"
        print "build all request folder in selected project folder"
        self.project = self.comboBox_selectProj.currentText()

        #default folder in self.project
        requestFolder= ['assets',
                        'assets/character',
                        'assets/vehicle',
                        'assets/set',
                        'assets/prop',
                        'assets/other',                        
                        'shot',
                        'output',
                        'publish',
                        'QC',
                        'global',
                        'global/shot',
                        'global/assets',
                        'global/assets/character',
                        'global/assets/vehicle',
                        'global/assets/set',
                        'global/assets/prop',
                        'global/assets/other',                    
                        'reference']


        #print requestFolder
        #check the request folder is exist in self.project ,and create folder

        for i in requestFolder:
            searchFolder = self.root + '/' + self.project +'/' + i

            self.createNewFolder(searchFolder)

        self.projectAssembleDescription ={'assets':{'character':{},
                                                    'vehicle':{},
                                                    'set':{},
                                                    'prop':{},
                                                    'other':{}},
                                          'shot':{}}


        projectFolder = self.root + '/' + self.project
        assetsFolder = projectFolder + '/' + 'assets'
        #print assetsFolder 
        shotFolder = projectFolder + '/' + 'shot'
        #print shotFolder



        self.allAssetTempList = []

        for assetItem in self.projectAssembleDescription['assets'].keys():    
            searchAssetFolder = assetsFolder +'/' + assetItem
           # print assetItem
           # print searchAssetFolder
            try:
                for assetClassItem in os.listdir(searchAssetFolder):
                    self.projectAssembleDescription['assets'][assetItem].update({'%s.%s'%(assetClassItem,assetItem):{}})
                    self.allAssetTempList.append('%s.%s'%(assetClassItem,assetItem))
            except:
                pass

            
        try:
            for shotItem in os.listdir(shotFolder):
                #print shotItem
                self.projectAssembleDescription['shot'].update({shotItem:{}})
                self.allAssetTempList.append('%s.shot'%shotItem)

        except:
            pass
                
        print "define self.projectAssembleDescriptionFile,in %s/global/%s__assembleDescription.json"%(self.project,self.project)
        self.projectAssembleDescriptionFile = self.root + '/' + self.project + '/' +'global'+ '/' + self.project + '_assembleDescription.json'
        
        #if os.path.isfile(self.projectAssembleDescriptionFile) == True:
        #    f = open(self.projectAssembleDescriptionFile,'r+')
        #else:       
        f = open(self.projectAssembleDescriptionFile,'w')
            
        data = json.dumps(self.projectAssembleDescription, sort_keys=True , indent =4) 
        f.write(data)
        f.close


        print "run defineWorkingProjectAssemble End"
        
       # print self.projectAssembleDescription


        
        
######-------------------------------store userPref start-------------------------------------------------------------------        

    def checkPublishToolTempFolder(self):
        #check folder, \Documents\maya\maya\mayaVer\prefs\publishToolFolder , is exist
        #if not mkdir
        #定義使用者設定檔案
        
      
      
        
        print "check the publishToolTemp folder"
        mayaVer = cmds.about(version=True)

        CSIDL_PERSONAL = 5       # My Documents
        SHGFP_TYPE_CURRENT = 0   # Get current, not default value

        buf= ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
        ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)

        userDocFolder = buf.value
        
    
        mayaPrefsPath = os.path.join(userDocFolder,'maya',mayaVer,'prefs')
        tempPath = os.path.join(mayaPrefsPath,'publishToolTemp')
        if os.path.isdir(tempPath) == True:
            print "publishToolTemp folder is existed"
        else:
            self.createNewFolder(tempPath)
            #os.mkdir(tempPath)
            print "created the publishTempPath"
            print "folder: %s"%tempPath
        self.publishTempPath = ""
        for cha in tempPath:
            if cha == "\\" :
                self.publishTempPath = self.publishTempPath + "/"
            else:
                self.publishTempPath= self.publishTempPath + cha

        self.creatUserPrefFile()
        
    def userPrefStore(self):   
        #define user last setting
        #儲存使用者最後使用資訊
        self.root ="//mcd-server/art_3d_project"
        self.project = "3d_pipeline_test"
        self.assetClass ="character"
        self.assetNow = "shot_02"
        self.processNow ="lighting"
        self.isAsset = False
        self.currentUser = getpass.getuser()
        
        userPrefInfo = {'self.root':'',
                        'self.project':'',
                        'self.assetClass':'',
                        'self.processNow':'',
                        'self.currentBranchSelect':'',
                        'self.workingFile':''
                        }
                        
                        

        
        
        
        
    def creatUserPrefFile(self):
        userPrefName = "publishToolUserPref.json"
        userPrefFullName = os.path.join(self.publishTempPath , userPrefName)

        self.userPrefFileName = ""
        for cha in userPrefFullName:
            if cha == "\\" :
                self.userPrefFileName = self.userPrefFileName + "/"
            else:
                self.userPrefFileName= self.userPrefFileName + cha
                
     #   print self.userPrefFileName 
        fileOpen = open(self.userPrefFileName,'w')
        fileOpen.write
        
    #    print "created %s"%self.userPrefFileName 
    
######-------------------------------store userPref End-------------------------------------------------------------------        
    
                
    def clickCharacterButton(self):
        "print select assetType , character"
        #self.assetsOnOffTable = [1,0,0,0,0,0,0]
        
                
        self.assetClass = "character"
        self.isAsset = True
        
        self.userPrefDict.update({'self.assetClass':self.assetClass})
        self.userPrefDict.update({'assetsOnOffTable': ['1','0','0','0','0','0','0']})
        self.userPrefDict.update({'self.isAsset':'True'})
        self.isAsset = True

        self.clickAssetShotSelectButton()

        
        self.pushButton_character.setChecked(True)
        
        self.buildAssetsList()
    def clickVehicleButton(self):
        "print select assetType , vehicle"
        
        
                        
        self.assetClass = "vehicle"
        self.isAsset = True
        self.userPrefDict.update({'self.assetClass':self.assetClass})
        self.userPrefDict.update({'assetsOnOffTable': ['0','1','0','0','0','0','0']})
        self.userPrefDict.update({'self.isAsset':'True'})
        self.isAsset = True

        self.clickAssetShotSelectButton()


        self.pushButton_vehicle.setChecked(True)

        self.buildAssetsList()


    def clickSetButton(self):
        "print select assetType , set"
        
                        
        self.assetClass = "set"
        self.isAsset = True
        self.userPrefDict.update({'self.assetClass':self.assetClass})
        self.userPrefDict.update({'assetsOnOffTable': ['0','0','1','0','0','0','0']})
        self.userPrefDict.update({'self.isAsset':'True'})
        self.isAsset = True

        self.clickAssetShotSelectButton()
                
        

        self.pushButton_set.setChecked(True)

        self.buildAssetsList()



    def clickPropsButton(self):
        "print select assetType , prop"
        
        self.assetClass = "prop"
        self.isAsset = True
        
        self.userPrefDict.update({'self.assetClass':self.assetClass})
        self.userPrefDict.update({'assetsOnOffTable': ['0','0','0','1','0','0','0']})
        self.userPrefDict.update({'self.isAsset':'True'})
        self.isAsset = True

        self.clickAssetShotSelectButton()
                
                
        

        self.pushButton_props.setChecked(True)

        
        self.buildAssetsList()
        
        
        

    def clickOthersButton(self):
        "print select assetType , other"
        
        self.assetClass = "other"
        self.isAsset = True
        
        self.userPrefDict.update({'self.assetClass':self.assetClass})
        self.userPrefDict.update({'assetsOnOffTable': ['0','0','0','0','1','0','0']})
        self.userPrefDict.update({'self.isAsset':'True'})
        self.isAsset = True

        self.clickAssetShotSelectButton()
                        
        
        

        self.pushButton_others.setChecked(True)
        


        self.buildAssetsList()



    def clickAllButton(self):
        "print select assetType , all"

        
        self.assetClass = "all"
        
       # self.assetClass = self.realSelectItemAssetClass
        self.isAsset = True
        self.userPrefDict.update({'self.assetClass':self.assetClass})
        self.userPrefDict.update({'assetsOnOffTable': ['0','0','0','0','0','1','0']})
        self.userPrefDict.update({'self.isAsset':'True'})
       # self.writeToUserPref()
        self.clickAssetShotSelectButton()
        self.isAsset = True

        self.pushButton_all.setChecked(True)



        self.buildAssetsList()
        
        
    def clickShotButton(self):
        "print select assetType , shot"

        self.assetClass = "shot"
        self.isAsset = False
        self.userPrefDict.update({'self.assetClass':self.assetClass})
        self.userPrefDict.update({'assetsOnOffTable': ['0','0','0','0','0','0','1']})
        self.userPrefDict.update({'self.isAsset':'False'})
        self.clickAssetShotSelectButton()
                        
        


        self.pushButton_shot.setChecked(True)


        self.buildAssetsList()
       
        
    def clickAssetShotSelectButton(self):
        self.writeToUserPref()
        self.pushButton_gotPublish.setEnabled(False) 

        #self.assetsOnOffTable read on off


        
        self.pushButton_character.setChecked(False)
        self.pushButton_vehicle.setChecked(False)
        self.pushButton_set.setChecked(False)
        self.pushButton_props.setChecked(False)
        self.pushButton_others.setChecked(False)
        self.pushButton_all.setChecked(False)
        self.pushButton_shot.setChecked(False)
        #print 'self.isAsset',self.isAsset
        
        if  self.isAsset == True:
            self.pushButton_processConcept.setEnabled(True)
            self.pushButton_processModeling.setEnabled(True)
            self.pushButton_processTexture.setEnabled(True)
            self.pushButton_processRigging.setEnabled(True)
            self.pushButton_processLayout.setEnabled(False)
            self.pushButton_processAnimation.setEnabled(False)
            self.pushButton_processLighting.setEnabled(False)
            self.pushButton_processEffects.setEnabled(False)
            self.pushButton_processSimulation.setEnabled(False)
            self. pushButton_processComp.setEnabled(False)
            
        else:
            self.pushButton_processConcept.setEnabled(False)
            self.pushButton_processModeling.setEnabled(False)
            self.pushButton_processTexture.setEnabled(False)
            self.pushButton_processRigging.setEnabled(False)
            self.pushButton_processLayout.setEnabled(True)
            self.pushButton_processAnimation.setEnabled(True)
            self.pushButton_processLighting.setEnabled(True)
            self.pushButton_processEffects.setEnabled(True)
            self.pushButton_processSimulation.setEnabled(True)
            self. pushButton_processComp.setEnabled(True)
            
        
        
    def checkPublishFileIsExist(self):
      #  print self.isAsset
      #  print self.assetNow
     #   print self.assetClass
      #  print self.processNow
        tempName = self.assetNow +'.'+self.assetClass
      #  print 'tempName' ,tempName
        mayaFileName ='none'
        iconFileName = 'none'
        
        
        fileName = self.root +'/' +self.project +'/' +'publish' +'/' +'global' +'/' +self.project + '_publishAnnonce.json'
        
        if os.path.isfile(fileName) ==True:
            
        
            #print fileName
            try:
                with open(fileName) as data_file:    
                    data = json.load(data_file)
      #          print data
            except:
                pass
            
            if self.isAsset == True:
               # assetOrShot = 'assets'
                #print data['assets']['character']['tiger.character'].keys()
                if self.processNow in data['assets'][self.assetClass][tempName].keys():

                    if os.path.isfile(data['assets'][self.assetClass][tempName][self.processNow]['state']['fileName']) == True:
                        #print 'filename',data['assets'][self.assetClass][tempName][self.processNow]['state']['fileName']

                        mayaFileName = data['assets'][self.assetClass][tempName][self.processNow]['state']['fileName']
                        self.pushButton_gotPublish.setEnabled(True) 
                    else:
                        pass
                    if os.path.isfile(data['assets'][self.assetClass][tempName][self.processNow]['state']['fileIcon']) == True:
         
                        iconFileName = data['assets'][self.assetClass][tempName][self.processNow]['state']['fileIcon']
                        self.label_showImage.setGeometry(QtCore.QRect(5, 5, 200, 200))
                        self.label_showImage.setPixmap(QtGui.QPixmap(iconFileName))
                    else:
                        pass
                        
                else:
                    mayaFileName ='none'
                    iconFileName = 'none'
                    self.pushButton_gotPublish.setEnabled(False) 
            


            else:
                if self.processNow in data['shot'][self.assetNow].keys():
                    if os.path.isfile(data['shot'][self.assetNow][self.processNow]['state']['fileName']) == True:
                        mayaFileName = data['shot'][self.assetNow][self.processNow]['state']['fileName']
                        
                        self.pushButton_gotPublish.setEnabled(True) 
                    else:
                        pass
                     
                    if os.path.isfile(data['shot'][self.assetNow][self.processNow]['state']['fileIcon']) == True:
                        iconFileName = data['shot'][self.assetNow][self.processNow]['state']['fileIcon']
                        self.label_showImage.setGeometry(QtCore.QRect(5, 5, 200, 200))
                        self.label_showImage.setPixmap(QtGui.QPixmap(iconFileName))
                    else:
                        pass
                    
                else:
                    mayaFileName ='none'
                    iconFileName = 'none'
                    self.pushButton_gotPublish.setEnabled(False) 
                    


           
      #      print 'mayafileName',mayaFileName   


       #     print 'iconFileName',iconFileName
            
            self.openPublishFileName = mayaFileName   
        else:
            pass
            

      
      #  self.openPublishFileName = fileName
        
            
        

        
    def click_assetProjListWidget(self):
        print "select one asset/shot"
        self.treeWidget_branches.clear()

        # get self.assetNow
       # self.userPrefDict.update({'self.assetName':self.assetName})

        self.assetNow = self.listWidget_assetProj.currentItem().text()
        self.assetName = 'shot'+'/'+self.assetNow 
        self.assetListItemRow = self.listWidget_assetProj.currentRow()
        self.findAssetClass()

        if self.isAsset == True:
            self.assetClass = self.realSelectItemAssetClass
        else:
            self.assetClass = 'shot'
        #self.userPrefDict.update({'self.assetClass':self.assetClass})
     #   print 'self.isAsset',self.isAsset
     #   print 'self.assetNow',self.assetNow
     #   print 'self.assetListItemRow',self.assetListItemRow
     #   print 'self.assetClass',self.assetClass
        #print 'self.realSelectItemAssetClass',self.realSelectItemAssetClass
        
        self.userPrefDict.update({'self.assetName':self.assetName})
        self.userPrefDict.update({'self.assetClass':self.assetClass})
        self.userPrefDict.update({'self.assetNow':self.assetNow})
        self.userPrefDict.update({'self.assetListItemRow':self.assetListItemRow})
        #self.userPrefDict.update({'self.self.assetListItemIndex':self.assetListItemIndex})

        #print self.allAssetTempList
        for i in self.allAssetTempList:
            if i.split('.')[0] == self.assetNow:
                self.assetClass = i.split('.')[1]
            
        self.writeToUserPref()
       # print self.assetClass
        self.clickProcessTypeSelectButton()
        

    def clickProcessConceptButton(self):
        self.clickProcessTypeSelectButton()
        self.pushButton_processConcept.setChecked(True)
        
        #self.root + '/' + self.project + '/' + 'assets' +
        self.processNow = 'concept'
        
        self.isAsset = True

        
        self.userPrefDict.update({'self.processNow':self.processNow})
        self.userPrefDict.update({'self.processOnOffTable':['1','0','0','0','0','0','0','0','0','0']})

    
        
        
        self.processTypeSelectedRun()
        
        
        
        

    def clickProcessModelingButton(self):
        self.clickProcessTypeSelectButton()
        self.pushButton_processModeling.setChecked(True)
        self.processNow = 'model'
        
        self.isAsset = True
        
        
        self.userPrefDict.update({'self.processNow':self.processNow})
        self.userPrefDict.update({'self.processOnOffTable':['0','1','0','0','0','0','0','0','0','0']})


        self.processTypeSelectedRun()


        
    def clickProcessTextureButton(self):
        self.clickProcessTypeSelectButton()
        self.pushButton_processTexture.setChecked(True)
        
        self.processNow = 'texture'
        self.isAsset = True
        
        self.userPrefDict.update({'self.processNow':self.processNow})
        self.userPrefDict.update({'self.processOnOffTable':['0','0','1','0','0','0','0','0','0','0']})


        self.processTypeSelectedRun()


    def clickProcessRiggingButton(self):
        self.clickProcessTypeSelectButton()
        self.pushButton_processRigging.setChecked(True)
        self.processNow = 'rigging'
        self.isAsset = True
        
        self.userPrefDict.update({'self.processNow':self.processNow})
        self.userPrefDict.update({'self.processOnOffTable':['0','0','0','1','0','0','0','0','0','0']})


        self.processTypeSelectedRun()


    def clickProcessLayoutButton(self):
        self.clickProcessTypeSelectButton()
        self.pushButton_processLayout.setChecked(True)

        self.processNow = 'layout'
        self.isAsset = False
        
        self.userPrefDict.update({'self.processNow':self.processNow})
        self.userPrefDict.update({'self.processOnOffTable':['0','0','0','0','1','0','0','0','0','0']})


        self.processTypeSelectedRun()


    def clickProcessAnimationButton(self):
        self.clickProcessTypeSelectButton()
        self.pushButton_processAnimation.setChecked(True)
        self.processNow = 'animation'
        self.isAsset = False        
        self.userPrefDict.update({'self.processNow':self.processNow})
        self.userPrefDict.update({'self.processOnOffTable':['0','0','0','0','0','1','0','0','0','0']})


        self.processTypeSelectedRun()




    def clickProcessLightingButton(self):
        self.clickProcessTypeSelectButton()
        self.pushButton_processLighting.setChecked(True)
        self.processNow = 'lighting'
        self.isAsset = False        
        self.userPrefDict.update({'self.processNow':self.processNow})
        self.userPrefDict.update({'self.processOnOffTable':['0','0','0','0','0','0','1','0','0','0']})


        self.processTypeSelectedRun()




    def clickProcessEffectsButton(self):
        self.clickProcessTypeSelectButton()
        self.pushButton_processEffects.setChecked(True)
        
        self.processNow = 'effects'
        self.isAsset = False        
        self.userPrefDict.update({'self.processNow':self.processNow})
        self.userPrefDict.update({'self.processOnOffTable':['0','0','0','0','0','0','0','1','0','0']})


        self.processTypeSelectedRun()




    def clickProcessSimulationButton(self):
        self.clickProcessTypeSelectButton()
        self.pushButton_processSimulation.setChecked(True)
        self.processNow = 'simulation'
        self.isAsset = False        
        
        self.userPrefDict.update({'self.processNow':self.processNow})
        self.userPrefDict.update({'self.processOnOffTable':['0','0','0','0','0','0','0','0','1','0']})


        self.processTypeSelectedRun()


    
        
        


    def clickProcessCompButton(self):
        self.clickProcessTypeSelectButton()
        self.pushButton_processComp.setChecked(True)
        self.processNow = 'comp'
        self.isAsset = False

        self.userPrefDict.update({'self.processNow':self.processNow})
        self.userPrefDict.update({'self.processOnOffTable':['0','0','0','0','0','0','0','0','0','1']})


        self.processTypeSelectedRun()


    def storeSavingFolderInfo(self):

        if self.isAsset == True:
        
            self.savingFolder = self.root + '/'+self.project +'/' + 'assets'+'/' +self.assetClass +'/' +self.assetNow +'/' +self.processNow
            
        else:
            self.savingFolder = self.root + '/'+self.project +'/' + 'shot'+'/' +self.assetNow +'/' +self.processNow
            
        
        self.userPrefDict.update({'self.savingFolder':self.savingFolder})
        self.writeToUserPref()



        
    def clickProcessTypeSelectButton(self):
        
        
        print "clickProcessTypeSelectButton start"
        #print 'self.isAsset',self.isAsset ,'type is' ,type(self.isAsset)

        self.pushButton_processConcept.setChecked(False)
        self.pushButton_processModeling.setChecked(False)
        self.pushButton_processTexture.setChecked(False)
        self.pushButton_processRigging.setChecked(False)
        self.pushButton_processLayout.setChecked(False)
        self.pushButton_processAnimation.setChecked(False)
        self.pushButton_processLighting.setChecked(False)
        self.pushButton_processEffects.setChecked(False)
        self.pushButton_processSimulation.setChecked(False)
        self.pushButton_processComp.setChecked(False)
        

        print "clickProcessTypeSelectButton end"
        
        
    def processTypeSelectedRun(self):
        # after click process button , run this to proces via module
        # 點選流程分類按鈕後執行此一模組,以呼叫數個模組
        print "run processTypeSelectedRun start"
        if self.isAsset ==True:
            
            try:
                self.branchFileStore = self.root +'/'+ self.project +'/'+'global' +'/'+'assets'+'/'+self.assetClass +'/'+self.assetNow +'/'+self.assetNow +'_'+self.processNow+'.json'
            except:
                pass
        else:
            try:
                self.branchFileStore = self.root +'/'+ self.project +'/'+'global' +'/'+'shot'+'/' +self.assetNow +'/'+self.assetNow +'_'+self.processNow+'.json'
            except:
                pass
        try:
            self.userPrefDict.update({'self.branchFileStore':self.branchFileStore})
            self.writeToUserPref()
        except:
            pass
        
        
        self.storeSavingFolderInfo()
        self.writeIsAssetToUserPref()
     
        
        #self.writeToUserPref()
        #self.printOutProjectInfo()
        self.currentUser = getpass.getuser()

        self.hostName = socket.gethostname()
        self.projectDescription()    
        self.plainTextEdit_optionPage_currentUser.setPlainText(self.currentUser + "@" +self.hostName)
        self.checkMasterExist()
        
        self.buildExistFileInfoTree()    
        self.buildTreeFromExistFileData()	
        self.tableWidget_FileList.clear()

        self.checkPublishFileIsExist()

        
        print "run processTypeSelectedRun end"
   
        
        
    def clear(self):
        
        self.tableWidget_FileList.clear()
        
    def printOutProjectInfo(self):
        # input project infomation, project root, name,asset name, shot name, isAsset Value
        print "get input info"
        ##self.root = "C:/mayaProjs"
       # self.root ="//mcd-server/art_3d_project"
        #self.project = "3d_pipeline_test"
        #self.assetClass ="character"
        #self.assetNow = "shot_02"
        ##self.processNow ="lighting"
      #  self.isAsset = False
        self.currentUser = getpass.getuser()

        self.hostName = socket.gethostname()
        
      #  print "self.root" ,self.root
      #  print "self.project" ,self.project
     #   print "self.assetClass", self.assetClass
     #   print "self.assetNow", self.assetNow   # if select assets
     #   print "self.processNow", self.processNow
     #   print "self.isAsset", self.isAsset
        
        

        self.projectDescription()    
      
        self.plainTextEdit_optionPage_currentUser.setPlainText(self.currentUser + "@" +self.hostName)
       # print "workProject", self.workProject
       # print "project Structure",self.projectStructureName
       # print "Branch File Store",self.shotBranchFileStore
        #print "shot Root Dir",self.shotRootDir
       # print "Export brancg File Dir",self.branchFileStore
        
        self.checkMasterExist()
    def checkIsAssetValue(self):
        
        if self.userPrefDict['self.isAsset'] == 'True':
            self.isAsset = True
        else:
            self.isAsset = False
    
    def writeIsAssetToUserPref(self):
        
        if self.isAsset == True :
            self.userPrefDict['self.isAsset'] == 'True'
        else:
            self.userPrefDict['self.isAsset'] == 'False'
            
        self.writeToUserPref()
        
    
    
        
   
    def projectDescription(self):
        
       # self.assetNow = self.userPrefDict['self.assetNow']
        print "projectDescription Start    p01"
        self.assetClass = self.userPrefDict['self.assetClass']
   #     print "self.root",self.root 
   #     print "self.project" ,self.project
   #     print "self.assetClass", self.assetClass
   #     print "self.assetNow", self.assetNow   # if select assets
    #    print "self.processNow", self.processNow
    #    print "self.isAsset", self.isAsset ,type(self.isAsset)
        
        #self.checkIsAssetValue()

        try:
            if self.isAsset == True:
                self.assetName = "assets" + "/" + self.assetClass + "/" + self.assetNow
            else:
                self.assetName = "shot" +"/" +self.assetNow
    #        print "self.assetName", self.assetName
        except:
            pass
        try:
            self.shotName = "shot"+"/"+ self.assetNow
        
    #        print "self.shotName" , self.shotName
        except:
            pass
        
        self.projectGlobal = self.root + "/" + self.project + "/" +"global"
        
   #     print "self.projectGlobal", self.projectGlobal
        #projectStructure.json  -- projectName_Structure.json branchPreDict
        self.projectStructureName = self.projectGlobal + "/" + self.project+"_struction.json"
        
   #     print "self.projectStructureName", self.projectStructureName
        self.userPrefDict.update({'self.assetName':self.assetName})
  
        self.userPrefDict.update({'self.shotName':self.shotName})
        self.userPrefDict.update({'self.projectGlobal':self.projectGlobal})
        self.userPrefDict.update({'self.projectStructureName':self.projectStructureName})
        self.writeToUserPref()
    #    print 'self.processNow',self.processNow
       
        print "projectDescription check point 01"
        if self.isAsset == True:
        #assetBranchFileInfo.json  -- assetName_process.json
            self.assetBranchFileName = self.assetNow + "_" + self.processNow +".json"       #assetBranchFileStore FileName
            print "projectDescription check point 02"

            self.assetRootDir = self.projectGlobal + "/" + "assets"
            self.assetClassDir = self.assetRootDir + "/" + self.assetClass
            self.assetBranchFileDir = self.assetClassDir + "/"+ self.assetNow #assetBranchFileStore Folder
            self.assetBranchFileStore = self.assetBranchFileDir + "/" + self.assetBranchFileName    #export Path + fileName
            self.workProject = self.root + "/" + self.project + "/" + self.assetName + "/" + self.processNow
            self.assetDir = self.root + "/" + self.project + "/" + self.assetName
            
      #      print "self.assetBranchFileDir",self.assetBranchFileDir

            if os.path.isdir(self.assetDir) == True:
                pass
            else:
                self.createNewFolder(self.assetDir)


            if os.path.isdir(self.assetBranchFileDir) == True:
                pass
            else:
                self.createNewFolder(self.assetBranchFileDir)

           # print "self.assetBranchFileDir",self.assetBranchFileDir
           # print "self.assetBranchFileStore", self.assetBranchFileStore
          #  print "self.workProject", self.workProject
            self.userPrefDict.update({'self.assetBranchFileDir':self.assetBranchFileDir})
            self.userPrefDict.update({'self.assetBranchFileStore':self.assetBranchFileStore})
            self.userPrefDict.update({'self.workProject':self.workProject})
            try:
                self.userPrefDict.update({'self.branchFileStore':self.branchFileStore})
            except:
                pass
            
        else:
            
            
            

            self.assetBranchFileDir = self.root +'/' +self.project +'/' + 'global' +'shot'+'/' +self.assetNow

            self.assetBranchFileStore = self.root +'/' +self.project +'/' + 'global' +'shot'+'/' +self.assetNow +'/' +self.assetNow+'_'+self.processNow+'.json'

                
            self.branchFileStore = self.assetBranchFileStore
            

        #shotBranchFileInfo.json  -- shotName_process.json
            print "projectDescription check point 03"

            self.shotBranchFileName = self.assetNow + "_" + self.processNow +".json"        #shotBranchFileStore FileName
       #     print 'self.shotBranchFileName ',self.shotBranchFileName 
            self.shotRootDir = self.projectGlobal + "/" + "shot"
        #    print 'self.shotRootDir',self.shotRootDir
            self.shotBranchFileDir = self.shotRootDir + "/"+ self.assetNow # shotBranchFileStore Folder
        #    print 'self.shotBranchFileDir',self.shotBranchFileDir
            self.shotBranchFileStore = self.shotBranchFileDir + "/" + self.shotBranchFileName    #export Path + fileName
         #   print 'self.shotBranchFileStore',self.shotBranchFileStore
            self.workProject = self.root + "/" + self.project + "/" + self.shotName + "/" + self.processNow
        #   print 'self.workProject',self.workProject
            self.shotDir = self.root + "/" + self.project + "/" + self.shotName 
        #    print 'self.shotDir',self.shotDir
          #  
          
            print "projectDescription check point 04"
            if os.path.isdir(self.shotDir) == True:
                pass
            else:
                self.createNewFolder(self.shotDir)

                 
          
          
            if os.path.isdir(self.shotBranchFileDir) == True:
                pass
            else:
                self.createNewFolder(self.shotBranchFileDir)

            print "projectDescription check point 05"
        
            self.branchFileStore = self.shotBranchFileStore
            
            self.userPrefDict.update({'self.assetBranchFileDir':self.assetBranchFileDir})
            self.userPrefDict.update({'self.assetBranchFileStore':self.assetBranchFileStore})
            self.userPrefDict.update({'self.workProject':self.workProject})
            self.userPrefDict.update({'self.branchFileStore':self.branchFileStore})
           # print "self.shotBranchFileDir", self.shotBranchFileDir
           # print "self.shotBranchFileStore",self.shotBranchFileStore
           # print "self.workProject", self.workProject    
           # print "projectDescription check point 05.1"

           # self.userPrefDict.update({'self.branchFileStore',self.branchFileStore})
             
           # print "projectDescription check point 05.2"

           # self.userPrefDict.update({'self.shotBranchFileStore',self.shotBranchFileStore})
           # print "projectDescription check point 05.3"

            #self.userPrefDict.update({'self.workProject',self.workProject})
           # print "projectDescription check point 05.4"

            #self.userPrefDict.update({'self.branchFileStore',self.branchFileStore})

           # print "projectDescription check point 06"

                
       # try:
          #  os.mkdir(self.projectGlobal + "/" + self.assetNow)
       # except:
          #  pass
        self.plainTextEdit_optionPage_projDescription.setPlainText(self.projectStructureName)
        self.plainTextEdit_optionPage_workProj.setPlainText(self.workProject)
        self.plainTextEdit_optionPage_branchInfoPos.setPlainText(self.branchFileStore)
        print 'self.branchFileStore',self.branchFileStore

        self.writeToUserPref()
        print "check, run projectDescription End"

        
   

    def checkMasterExist(self):
        #---------1. check /scenes/master exist
        #.........2. check branchInfoFile exist, in global/assets(shot)/assetName(shotName)/assetName(shotName)_process.json,ex. shot_02_lighting.json
        print "run checkMasterExist start"
        print "check /scenes/master exist"
        print "check branchInfoFile exist"
        print 'checkMasterExist checkpoint a01'

        #get self.workProject, check master /scenes/master folder exist
        #get self.branchFileStore ,check the branchInfoFile ,json file exist
       # print "self.workProject............:" , self.workProject 
        print 'checkMasterExist checkpoint a02'

     ##   print "self.branchFileStore.........:",self.branchFileStore
       # self.branchInfoFile = self.userPrefDict['self.branchFileStore']
        print 'checkMasterExist checkpoint a03'
        
        self.workProjectScenesFolder = self.workProject +'/'+'scenes'
        self.workProjectData = self.workProject +'/'+'data'
        self.workProjectDataCache = self.workProject +'/'+'data' +'/' +'cache'
        self.workProjectDataExport = self.workProject +'/'+'data' +'/' +'export'
        self.workProjectDataAlembic =self.workProject +'/'+'data' +'/' +'alembic'
        self.workProjectDataFluid = self.workProject +'/'+'data' +'/' + 'fluid'
        self.workProjectDataVdb =self.workProject +'/'+'data' +'/' + 'vdb'
        self.workProjectParticles =self.workProject +'/'+'data' +'/' + 'particles'
        self.workProjectImages =self.workProject +'/'+'images' 
        self.workProjectSourceimages =self.workProject +'/'+'sourceimages' 
        self.masterFolder = self.workProject +'/'+'scenes'+ '/' + 'master'
      #  print "masterFolder",self.masterFolder
      #  print "master folder exist....:" ,os.path.isdir(self.masterFolder)
      #  print "branch Info File exist.:", os.path.isfile(self.branchFileStore)
        #timeNow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # .......1. check /scenes/master exist
        
        #pre build folders ,in workProject
        preBuildWorkProjectFolders = [self.workProject,
                                      self.workProjectScenesFolder,
                                      self.masterFolder,
                                      self.workProjectData,
                                      self.workProjectDataCache,
                                      self.workProjectDataExport,
                                      self.workProjectDataAlembic,
                                      self.workProjectDataFluid,
                                      self.workProjectDataVdb,
                                      self.workProjectParticles,
                                      self.workProjectImages,
                                      self.workProjectSourceimages]
        
        for i in preBuildWorkProjectFolders:
            if os.path.isdir(i) == True:
                print  "folder, %s, was existed"%i
                pass
            else:
                self.createNewFolder(i)

               # os.mkdir(i)
                print "build %s"%i
                                      

        if os.path.isfile(self.branchFileStore) == True:
            print "the branch Info File exist already"

           # branchInfoFileBuild = open(self.branchFileStore,'a')
           # branchInfoFileBuild.write("\n"+"#"+"update Time:"+"    "+ "%s"%timeNow)
           # branchInfoFileBuild.close
        else:
            
            try:
                branchInfoFileBuild = open(self.branchFileStore,'w')
               # branchInfoFileBuild.write("#"+"build branchInfoFile,"+"%s"%self.branchFileStore)
                branchInfoFileBuild.close
                print "the branch Info File was built"
            except:
                pass
        self.userPrefDict.update({'self.branchFileStore':self.branchFileStore})

        print "run checkMasterExist END"
        
        
   # def buildInfoTreeFromTactic(self):
        


    def buildExistFileInfoTree(self):
        print "run buildExistFileInfoTree process         ------------start" 

        #update the json file begining
    

        #branchFileStore
        #currentProject = "//mcd-server/art_3d_project/3d_pipeline_test/shot/shot_02/lighting/"    #test project
        #print "self.workProject",self.workProject
        topLevelDirFileSearch = self.workProjectScenesFolder
        #print 'topLevelDirFileSearch' ,topLevelDirFileSearch
        
        topLevelDirList = ['master']
        branchPreDict = {"0":{"master":{}}}        

        #build topLevelDir List------------------------------------------------------------------


        for dir,path,file in os.walk(topLevelDirFileSearch):

            allDir = dir.split(topLevelDirFileSearch)[1]

            try:

                if allDir.split("\\")[1] in topLevelDirList:
                    pass
                elif allDir.split("\\")[1] == '.mayaSwatches':
                    pass
                else:
                    
                    topLevelDirList.append(allDir.split("\\")[1])
                 #   print allDir.split("\\")[1]
                
            except:
                pass



        for i in range(0,len(topLevelDirList)):

            branchPreDict.update({str(i):{topLevelDirList[i]:{}}})

        #------analyze 2nd level dir and files-------------------
        #----------1.for i in branchPreDict.keys(): get search folder from branchPreDict dictionary, make sure index and branch name match
        #-------------2.for secLevelItem in os.listdir(secLevelDirSearch):, update 2nd level item into branchPreDict
        #----------------3 for thirdLevelItem in os.listdir(thirdLevelDirSearch):, update 3rd level item into branchPreDict
        #--------------------4. for fourLevelItem in os.listdir(fourLevelDirSearch): update 4th level item into branchPreDict ,only folder
        #--------------os.path.isdir(path),check the path is folder or file
        for i in branchPreDict.keys():
            secLevelDirSearch = topLevelDirFileSearch+ '/' + branchPreDict[i].keys()[0]  
         #   print 'topLevelDirFileSearch',topLevelDirFileSearch
        #    print 'branchPreDict',branchPreDict
         #   print 'secLevelDirSearch',secLevelDirSearch 
            
            branchPreDict[i][branchPreDict[i].keys()[0]].update({'folder':{}})
            branchPreDict[i][branchPreDict[i].keys()[0]].update({'file':{}})
            for secLevelItem in os.listdir(secLevelDirSearch):
                thirdLevelDirSearch = topLevelDirFileSearch+ '/' + branchPreDict[i].keys()[0]+'/'+ secLevelItem       
                if os.path.isdir(thirdLevelDirSearch) == True:
                    branchPreDict[i][branchPreDict[i].keys()[0]]['folder'].update({secLevelItem:{}})
                    
                    
                else:
                    branchPreDict[i][branchPreDict[i].keys()[0]]['file'].update({secLevelItem:[]})

                
                
                if os.path.isdir(thirdLevelDirSearch) == True:
                    branchPreDict[i][branchPreDict[i].keys()[0]]['folder'][secLevelItem].update({'folder':{}})
                    branchPreDict[i][branchPreDict[i].keys()[0]]['folder'][secLevelItem].update({'file':{}})
                    
                    for thirdLevelItem in os.listdir(thirdLevelDirSearch):

                        fourLevelDirSearch = thirdLevelDirSearch +'/'+ thirdLevelItem

                        
                        if os.path.isdir(fourLevelDirSearch) == True:
                            branchPreDict[i][branchPreDict[i].keys()[0]]['folder'][secLevelItem]['folder'].update({thirdLevelItem:{}})
                            branchPreDict[i][branchPreDict[i].keys()[0]]['folder'][secLevelItem]['folder'][thirdLevelItem].update({'file':{}})
                        else:
                            branchPreDict[i][branchPreDict[i].keys()[0]]['folder'][secLevelItem]['file'].update({thirdLevelItem:[]})   

                            
                        if os.path.isdir(fourLevelDirSearch) == True:
                            for fourLevelItem in os.listdir(fourLevelDirSearch):
                                branchPreDict[i][branchPreDict[i].keys()[0]]['folder'][secLevelItem]['folder'][thirdLevelItem]['file'].update({fourLevelItem:[]}) 
                            
                                        


                
        self.branchPreDict = branchPreDict
        exportDate = json.dumps(self.branchPreDict, sort_keys=True , indent =4)
        #export json file
       # print exportDate 
       # print "--------------",self.branchFileStore
        self.userPrefDict.update({'self.branchFileStore':self.branchFileStore})
        with open(self.branchFileStore, 'w') as f:
            f.write(exportDate)
                
        
        self.writeToUserPref()
        
        print "run buildExistFileInfoTree process         ------------End" 


        
    def initialItemBuild(self):
        
        print "run initialItemBuild start"

        self.currentUser = getpass.getuser()
        self.checkUserPrefFileExist()
        #self.setFromUserPref()
        self.branchDict={"0":{"master":{}}}    #default Master Item
        self.branch_index = 0
        
        #self.isAsset = True
        
        #self.test_processProjectGlobal()
        #self.getDataFromTacticFile()
        #runUserPref
        #self.setFromUserPref()
        #print 'self.userPrefFile',self.userPrefFile

       # print self.projectsInTactic 
        #print self.assetsInTactic 
       # print self.shotsInTactic
        print "run initialItemBuild End"

    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def setTreeFromUserPref(self):
        self.treeWidget_branches.clear()

    
        QtWidgets.QTreeWidgetItem(self.treeWidget_branches).setForeground(0,self.brushLevelOne)  #create contain master ,and define font color
        
        #1.default exist , master should exist in top of treeWidget
        self.treeWidget_branches.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "master", None, -1))
        self.treeWidget_branches.topLevelItem(0).setFont(0,self.fontLevelOne)#define font size

    
    
    
    
    
    
    
    
    
        
        
    #---------------Load Exist Branch Data From Dictionary Start-------------------------------------------------------------------------------------------------------
    def buildTreeFromExistFileData(self):
        #--------build Tree from Exist folders and files--------------------
        #----------1. define default ,master, that should be exist------------
        #----------2.get file info tree
        #----------3.for topLevelIndex in range(1,topLevelIndexCount): build top Level items 
        #----------4.for topLevelIndex in range(0,topLevelIndexCount): build sec Level items 
        #----------5. build 2nd level item in treeWidget    
        #----------6. build 3rd level item in treeWidget    
        print "run buildTreeFromExistFileData start"
        print "initial all Tree Data"
     
        self.treeWidget_branches.clear()
        QtWidgets.QTreeWidgetItem(self.treeWidget_branches).setForeground(0,self.brushLevelOne)  #create contain master ,and define font color
        
        #1.default exist , master should exist in top of treeWidget
        self.treeWidget_branches.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "master", None, -1))
        self.treeWidget_branches.topLevelItem(0).setFont(0,self.fontLevelOne)#define font size

        #2.get file info tree
        topLevelIndexStringList = sorted(self.branchPreDict.keys())
        topLevelIndexCount = len(topLevelIndexStringList) #get topLevelIndex 
        
        #3.for topLevelIndex in range(1,topLevelIndexCount): build top Level items 
        try:
            for topLevelIndex in range(1,topLevelIndexCount):
                QtWidgets.QTreeWidgetItem(self.treeWidget_branches).setForeground(0,self.brushLevelTwo)
                self.treeWidget_branches.topLevelItem(topLevelIndex).setText(0, QtWidgets.QApplication.translate("MainWindow", "master", None, -1))
                self.treeWidget_branches.topLevelItem(topLevelIndex).setText(0,self.branchPreDict[str(topLevelIndex)].keys()[0])
                self.treeWidget_branches.topLevelItem(topLevelIndex).setFont(0,self.fontLevelTwo)      #set font
        except:
            pass

        #4.for topLevelIndex in range(0,topLevelIndexCount): build sec Level items 
        try:
            for topLevelIndex in range(0,topLevelIndexCount):
                topLevelDirDict = self.branchPreDict[str(topLevelIndex)][self.branchPreDict[str(topLevelIndex)].keys()[0]]
                secLevelDirList = topLevelDirDict['folder'].keys()
                secLevelDirCount = len(secLevelDirList)


            #5. build 2nd level item in treeWidget    
                for secLevelItemIndex in range(0,secLevelDirCount):
                    QtWidgets.QTreeWidgetItem(self.treeWidget_branches.topLevelItem(topLevelIndex)).setForeground(0,self.brushLevelThree)  #build new item from index

                    self.treeWidget_branches.topLevelItem(topLevelIndex).child(secLevelItemIndex).setFont(0,self.fontLevelThree)
                    self.treeWidget_branches.topLevelItem(topLevelIndex).child(secLevelItemIndex).setText(0,secLevelDirList[secLevelItemIndex])

                    thirdLevelDirList = topLevelDirDict['folder'][secLevelDirList[secLevelItemIndex]]['folder'].keys()
                    thirdLevelDirCount = len(thirdLevelDirList)
                    #6. build 3rd level item in treeWidget   
                    
                    for thirdLevelItemIndex in range(0,thirdLevelDirCount):
                        QtWidgets.QTreeWidgetItem(self.treeWidget_branches.topLevelItem(topLevelIndex).child(secLevelItemIndex)).setForeground(0,self.brushLevelFour)  #set 4rd level brush
                        self.treeWidget_branches.topLevelItem(topLevelIndex).child(secLevelItemIndex).child(thirdLevelItemIndex).setFont(0,self.fontLevelFour)  #set 4rd level font
                        self.treeWidget_branches.topLevelItem(topLevelIndex).child(secLevelItemIndex).child(thirdLevelItemIndex).setText(0,thirdLevelDirList[thirdLevelItemIndex])   #named the newItem , from typeIn line edit
        except:
            pass
        print "run buildTreeFromExistFileData END"

    #---------------Load Exist Branch Data From Dictionary End-------------------------------------------------------------------------------------------------------
     





    #---------------Load Exist File Information From Dictionary Start-------------------------------------------------------------------------------------------------------
    
    def loadExistFileInfo(self):
        
        self.tableItem = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setItem(0, 0, self.tableItem)
        self.tableItem = QtWidgets.QTableWidgetItem()
        self.tableWidget_FileList.setItem(0, 1, self.tableItem)

        

        
        self.tableWidget_FileList.item(0, 0).setText(QtWidgets.QApplication.translate("MainWindow", "v009", None, -1))
        self.tableWidget_FileList.item(0, 1).setText(QtWidgets.QApplication.translate("MainWindow", "alpha", None, -1))
       # self.tableWidget_FileList.item(0, 2).setText(QtWidgets.QApplication.translate("MainWindow", "2017.03/28 10:00", None, -1))
       # self.tableWidget_FileList.item(1, 0).setText(QtWidgets.QApplication.translate("MainWindow", "v008", None, -1))
       # self.tableWidget_FileList.item(1, 1).setText(QtWidgets.QApplication.translate("MainWindow", "alpha", None, -1))

        
    #---------------Load Exist File Information From Dictionary END-------------------------------------------------------------------------------------------------------
     
        
    def testFileInfoDict(self):
        
        self.fileInfoDict = {'01':["projectName_assetClass_assetName_process_v001_alpha.mb","alpha","2017/03/28    10:28","info xxxxxxxxxxxxxxxxxxxxxx"],
                             '02':["projectName_assetClass_assetName_process_v002_alpha.mb","alpha","2017/03/28    10:29"],
                             '03':["projectName_assetClass_assetName_process_v003_alpha.mb","alpha","2017/03/28    10:30"],
                             '04':["projectName_assetClass_assetName_process_v004_alpha.mb","alpha","2017/03/28    10:31"],
                             '05':["projectName_assetClass_assetName_process_v005_alpha.mb","alpha","2017/03/28    10:32"],
                             '06':["projectName_assetClass_assetName_process_v006_alpha.mb","alpha","2017/03/28    10:33"],
                             '07':["projectName_assetClass_assetName_process_v007_alpha.mb","alpha","2017/03/28    10:34"],
                             '08':["projectName_assetClass_assetName_process_v008_alpha.mb","alpha","2017/03/28    10:35"],
                             '09':["projectName_assetClass_assetName_process_v009_alpha.mb","alpha","2017/03/28    10:36"],
                             '10':["projectName_assetClass_assetName_process_v010_alpha.mb","alpha","2017/03/28    10:37"],
                             '11':["projectName_assetClass_assetName_process_v011_alpha.mb","alpha","2017/03/28    10:38"],
                             '12':["projectName_assetClass_assetName_process_v012_alpha.mb","alpha","2017/03/28    10:39"],
                             '13':["projectName_assetClass_assetName_process_v013_alpha.mb","alpha","2017/03/28    10:40","info vcvcxvcccccccc"],
                             '14':["projectName_assetClass_assetName_process_v014_alpha.mb","alpha","2017/03/28    10:41"],
                             '15':["projectName_assetClass_assetName_process_v015_alpha.mb","alpha","2017/03/28    10:42"],
                             '16':["projectName_assetClass_assetName_process_v016_alpha.mb","alpha","2017/03/28    10:43"],
                             '17':["projectName_assetClass_assetName_process_v017_alpha.mb","alpha","2017/03/28    10:44"],
                             '18':["projectName_assetClass_assetName_process_v018_alpha.mb","alpha","2017/03/28    10:45"],
                             '19':["projectName_assetClass_assetName_process_v019_alpha.mb","alpha","2017/03/28    10:46"],
                             '20':["projectName_assetClass_assetName_process_v020_alpha.mb","alpha","2017/03/28    10:47"],
                             '21':["projectName_assetClass_assetName_process_v021_alpha.mb","alpha","2017/03/28    10:48"]
                             }
        



    def defineFont(self):
                
        fontSizeAdj = self.setFontSize
        self.fontLevelOne = QtGui.QFont()
        self.fontLevelOne.setPointSize((fontSizeAdj+2))
        self.fontLevelOne.setWeight(75)
        self.fontLevelOne.setBold(True)
        self.fontLevelOne.setUnderline(True)


        self.brushLevelOne = QtGui.QBrush(QtGui.QColor(247, 126, 128))
        self.brushLevelOne.setStyle(QtCore.Qt.NoBrush)
        

        self.fontLevelTwo = QtGui.QFont()
        self.fontLevelTwo.setPointSize(fontSizeAdj+2)
        self.fontLevelTwo.setWeight(75)
        self.fontLevelTwo.setBold(0)
        #self.fontLevelTwo.setItalic(True)
        
        self.brushLevelTwo = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        self.brushLevelTwo.setStyle(QtCore.Qt.NoBrush)

        self.fontLevelThree = QtGui.QFont()
        self.fontLevelThree.setPointSize(fontSizeAdj+1)
        self.fontLevelThree.setWeight(75)
        self.fontLevelThree.setBold(True)

        self.fontLevelThree.setItalic(True)
        self.brushLevelThree = QtGui.QBrush(QtGui.QColor(100, 200, 100))
        self.brushLevelThree.setStyle(QtCore.Qt.NoBrush)
       # item_0.setForeground(0, brush)

        self.fontLevelFour = QtGui.QFont()
        self.fontLevelFour.setPointSize(fontSizeAdj+1)
        self.fontLevelFour.setWeight(75)
        self.fontLevelFour.setBold(0)

        self.fontLevelFour.setItalic(True)
        self.brushLevelFour = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        self.brushLevelFour.setStyle(QtCore.Qt.NoBrush)

        
        
        
    def createFileTable(self):
        #self.getSaveingBranchFolder()
      #  self.readBranchJsonFile()
        
       # with open('data.json') as data_file:    
        #data = json.load(data_file)
       # self.getFilesInfoFromJson()
      #  print 'self.branchDict',self.branchDict
        #tableWidget_FileList
        self.tableWidget_FileList.clear()

        #pprint(data)
        
    #def asss(self):
        print" run createFileTable function start..................."
        self.itemSelect =  self.treeWidget_branches.currentItem().text(0)
      #  print 'self.itemSelect',self.itemSelect
        
       # print 'index',self.treeWidget_branches.indexOfTopLevelItem(self.treeWidget_branches.currentItem())
        
 
        # self.buildExistFileInfoTree()
        self.getFilesInfoFromJson()

        try:                   
            tableIndex = sorted(self.fileInfoDict.keys())  #string
            
            verIndex = sorted(self.fileInfoDict.keys(), reverse = True )        
       #     print "verIndex",verIndex
      #      print 'self.fileInfoDict',self.fileInfoDict
            print "createFileTable check point 01"
            if len(tableIndex) > 0:
                for i in range(0,len(tableIndex)):
                   # print i,verIndex[i],self.fileInfoDict[str(verIndex[i])]  #i indexNum,verIndex[i]--->version,self.fileInfoDict[str(verIndex[i])--->fileName
                    itemVer = "v"+verIndex[i]
                    #print itemVer
                    #print 'fileName', self.fileInfoDict[str(verIndex[i])]
                    self.tableItem = QtWidgets.QTableWidgetItem()
                    self.tableWidget_FileList.setItem(i, 0, self.tableItem)
                    self.tableItem = QtWidgets.QTableWidgetItem()
                    self.tableWidget_FileList.setItem(i, 1, self.tableItem)
                    self.tableItem = QtWidgets.QTableWidgetItem()
                    self.tableWidget_FileList.setItem(i, 2, self.tableItem)
                   # self.tableWidget_FileList.setItem(i, 3, self.tableItem)
                   # print self.fileInfoDict[str(verIndex[i])]# ,type(self.tableWidget_FileList.setItem(i, 0, self.tableItem)[2])

                    
                    itemUser = self.fileInfoDict[str(verIndex[i])][1]
                   # print 'itemUser',itemUser
                    itemDateTemp = datetime.datetime.fromtimestamp(float(self.fileInfoDict[str(verIndex[i])][2]))
                    itemDate = str(itemDateTemp.date())+' '+(str(itemDateTemp.time())).split('.')[0]
                    itemFileName = self.fileInfoDict[str(verIndex[i])][0]
                    self.tableWidget_FileList.item(i, 0).setText(QtWidgets.QApplication.translate("MainWindow", itemVer, None, -1))


                    self.tableWidget_FileList.item(i, 1).setText(QtWidgets.QApplication.translate("MainWindow", 'tempName', None, -1))
                    self.tableWidget_FileList.item(i, 1).setText(itemUser)
                    self.tableWidget_FileList.item(i, 2).setText(QtWidgets.QApplication.translate("MainWindow", itemDate, None, -1))
                   # self.tableWidget_FileList.item(i, 3).setText(QtWidgets.QApplication.translate("MainWindow", itemFileName, None, -1))

                  #  self.textBrowser_BranchFileInfo.setText("sssssssssssss")
                   # print itemFileName self.assetName
            else:
                pass
                
            self.currentSelectedFile = itemFileName
        except:
            pass
        self.savingFolder= self.filesStoreBranchFolder
        self.userPrefDict.update({'self.savingFolder':self.savingFolder})
        self.writeToUserPref()
        print" run createFileTable function End..................."

    #--------------------------get linking fileInfo json----------------------------start----------------------------
    
    def getGlobalFolderLocation(self):
        self.findAssetClass()
        if self.isAsset == True:
            #self.realSelectItemAssetClass 
            #self.fileInfoLocation = self.root +'/'+ self.project +'/' + 'global' + '/' +"assets"+ '/'+ self.assetClass + '/'+ self.assetNow 
            self.fileInfoLocation = self.root +'/'+ self.project +'/' + 'global' + '/' +"assets"+ '/'+ self.realSelectItemAssetClass  + '/'+ self.assetNow 
            
        else:
            self.fileInfoLocation = self.root +'/'+ self.project +'/' + 'global' + '/' +"shot"+ '/'+ self.assetNow 
       # print 'self.fileInfoLocation',self.fileInfoLocation
            
    
    
    
    def getLinkingFileInfoText(self):
        # 1. define asset/shot description file location.
        # 2. create an empty text file in folder
        
     #   print "getFileInfo from %s"%self.lineEdit_currentFileName.text()
        self.getGlobalFolderLocation()
       # if self.isAsset == True:
        #    fileInfoLocation = self.root +'/'+ self.project +'/' + 'global' + '/' +"assets"+ '/'+ self.assetClass + '/'+ self.assetNow 
            
       # else:
        #    fileInfoLocation = self.root +'/'+ self.project +'/' + 'global' + '/' +"shot"+ '/'+ self.assetNow 
            
    
        fileInfoName = self.lineEdit_currentFileName.text().split('.')[0] +'.txt'  #define the file description Text file name
        #thumbFileName = self.lineEdit_currentFileName.text().split('.')[0]

        if os.path.isdir(self.fileInfoLocation) == False:
            self.createNewFolder(self.fileInfoLocation)

            #os.mkdir(self.fileInfoLocation) 
        else:
            pass
        #thumbFileName = self.lineEdit_currentFileName.text().split('.')[0]
    
        self.fullFileInfoName = self.fileInfoLocation + '/' + fileInfoName
        #self.fullFileThumbName = fileInfoLocation + '/' + thumbFileName
        

        
        timeNow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if os.path.isfile(self.fullFileInfoName) == False:
            fileInfoText = open(self.fullFileInfoName,'w')
            fileInfoText.write("### File Info ###"+"\n")
            fileInfoText.write("builtTime: "+timeNow +"\n") 
            fileInfoText.write("creator: "+self.currentUser +"\n")    
            fileInfoText.write("#################"+"\n")     
            fileInfoText.write("\n")
            fileInfoText.write("\n")
            fileInfoText.write("\n")   
            fileInfoText.close
            
            
            
        else:
            pass
    #--------------------------get linking fileInfo json----------------------------END----------------------------
    
    
    
    
    
        
    def addDescriptionToTextFile(self):
        #add more description when push edit button
        f = open(self.fullFileInfoName,'w')
        dataEdit = self.plainTextEdit_BranchFileInfo.toPlainText().encode('utf-8')
      #  print dataEdit
        f.write(dataEdit)
        f.close
        
        #self.makeThumbnail()
        
        
    def makeThumbnail(self):
        #filename = self.fullFileThumbName
        

        currentFrame = cmds.currentTime(query=True)
       
        cmds.select(cl=True)
        screenShot = cmds.playblast(st=currentFrame, et=currentFrame, format="image", filename=self.fullFileThumbName, forceOverwrite=True, sequenceTime=False, clearCache=True, viewer=False, showOrnaments=False, framePadding=4, percent=100, compression="png", quality=70, width=150, height=150)
       # print 'screenShotAAA',screenShot
        
        thumbNameCheckKey = self.fullFileThumbName.split('/')[-1]
      #  print 'thumbNameCheckKey',thumbNameCheckKey
        for i in os.listdir(self.fileInfoLocation):
            
            if i.split('.')[-1] == 'png':
                if i.split('.')[0] == thumbNameCheckKey:
                    reNameThumbFileName = self.fullFileThumbName +'.0001.png'
                    srcName = self.fileInfoLocation +'/'+ i
                    os.rename( srcName, reNameThumbFileName)
       #             print 'srcName',srcName
       #             print 'reNameThumbFileName',reNameThumbFileName    
        
        self.screenShot = screenShot.split('.')[0]+'.0001.png'
      ##  print self.screenShot
        #self.getThumbnail()
        
        
        
        
    def makeThumbnailTypical(self,thumbnailFileName,resX,resY,setFrame):
        #input thumbnailName
        #set currentTimeTo frame = setFrame #float num
        #size resX * resY
        

        currentFrame = cmds.currentTime(setFrame,e=True)
       
        cmds.select(cl=True)
        screenShot = cmds.playblast(st=currentFrame, et=currentFrame, format="image", filename=thumbnailFileName, forceOverwrite=True, sequenceTime=False, clearCache=True, viewer=False, showOrnaments=False, framePadding=4, percent=100, compression="png", quality=70, width=resX, height=resY)
        print 'screenShotAAA',screenShot
        
        thumbNameCheckKey = thumbnailFileName.split('/')[-1]
        fileInfoLocation = thumbnailFileName.split(thumbNameCheckKey)[0]
        reNameThumbFileName = fileInfoLocation +  thumbNameCheckKey+'.png'
        #print tempReNameThumbFileName

         
       # print 'thumbNameCheckKey',thumbNameCheckKey ,fileInfoLocation
        compareTimeTempList = []
        for i in os.listdir(fileInfoLocation):
            
            if i.split('.')[-1] == 'png':
                if i.split('.')[0] == thumbNameCheckKey:
                    fullFileName = fileInfoLocation+i
          #          print fullFileName
                    try:
                        fileTime =  os.path.getmtime(fullFileName) 
                        compareTimeTempList.append(str(fileTime)+'_._'+fullFileName)
                    except:
                        pass
 
      #  print compareTimeTempList[0]
        srcName = compareTimeTempList[0].split('_._')[-1]
        try:
            os.remove(reNameThumbFileName)
        except:
            pass
 
        
        os.rename(srcName,reNameThumbFileName)
     
        '''
        print 'srcName' ,srcName
        print 'reNameThumbFileName',reNameThumbFileName
        try:
            os.remove(reNameThumbFileName)
        except:
            pass
 
        os.rename(srcName,reNameThumbFileName)
        

      #  os.rename(srcName,reNameThumbFileName)
        oldFolder = fileInfoLocation+'/'+'old'
        try:
            os.mkdir(oldFolder)
            
        except:
            pass
           
        for i in range( 1,len(compareTimeTempList)):
            print i
            
            
            src= compareTimeTempList[i].split('_._')[-1]
            desc = oldFolder+'/'+compareTimeTempList[i].split('_._')[-1].split('/')[-1]
            #print src,desc
            try:
                os.rename(src,desc)
            except:
                pass
            #print 'srcName',srcName
           # print 'reNameThumbFileName',reNameThumbFileName   
       ''' 
    def compareFileTime(self,inputFolder,fileFormat):
        #compareFileTime(self,string,list)

        fileExceptList = ['Thumbs.db','thumbs.db']

        compareTimeTempList = []

        for i in os.listdir(inputFolder):
            #print i
            #print os.path.relpath(i)
                if i.split('.')[-1] in fileFormat:
                    fullFileName = string +'/' +i
                    if os.path.isfile(fullFileName) == True:
                        #print fullFileName
                        fileTime =  os.path.getmtime(fullFileName) 
                        compareTimeTempList.append(str(fileTime)+'_._'+fullFileName)
                        
        exportFileTimeList = sorted(compareTimeTempList)
                 
        
        
    def getThumbnail(self):

        try:
            self.label_showImage.setPixmap(QtGui.QPixmap(self.screenShot))
        except:
            pass
        
        
        
    def getSaveingBranchFolder(self):

        """Returns Current top level item and child index.
        If no child is selected, returns -1. 
        """
        
        
        
        #Check if top level item is selected or child selected 
        if self.treeWidget_branches.indexOfTopLevelItem(self.treeWidget_branches.currentItem())==-1:
            try:
                if len(self.treeWidget_branches.currentItem().parent().parent().text(0)) > 0 :
                    self.currentBranchFolder = self.treeWidget_branches.currentItem().parent().parent().text(0) + '/' + self.treeWidget_branches.currentItem().parent().text(0) +'/'+ self.treeWidget_branches.currentItem().text(0)
                    #print currentBranchFolder
            except:
                if len(self.treeWidget_branches.currentItem().parent().text(0)) > 0 :
                    self.currentBranchFolder = self.treeWidget_branches.currentItem().parent().text(0) + '/'+ self.treeWidget_branches.currentItem().text(0)
                    #print currentBranchFolder           
        else: 
            self.currentBranchFolder =   self.treeWidget_branches.currentItem().text(0)
            #print currentBranchFolder

    def openSelectFile(self):
        print "openSelectFile start"
        #print 'self.filesStoreBranchFolder',self.filesStoreBranchFolder
        #print 'self.fileInfoDict',self.fileInfoDict
        try:
            self.savingFolder = self.userPrefDict['self.savingFolder']
        except:
            pass
        fileName = self.lineEdit_currentFileName.text()
        fullFileName = self.filesStoreBranchFolder +'/' +fileName
        cmds.file( fullFileName, open=True,f=True ) #open file
        
        cmds.workspace(self.workProject, o=True) #set project
        
       # print 'workspace' ,cmds.workspace(q=True, rd=True) #check workspace
     #   print '%s'%fileName + ' was opened'
       # print 'self.workProject',self.workProject
        print "openSelectFile end"

        
            



    def getSavingFile(self):
        # print self.workProject
        cmds.workspace(self.workProject,o=True) #set proj
        #print self.getFilesInfoFromJson()
        #print self.filesStoreBranchFolder  #, export branch folder
      #  print "self.fileInfoDict" ,self.fileInfoDict
        #self.root ="//mcd-server/art_3d_project"
        #self.project = "3d_pipeline_test"
        #self.assetClass ="character"
        #self.assetNow = "shot_02"
        #self.processNow ="lighting" 
       # print self.fileInfoDict.keys()       

        
        currentBranch = self.itemSelect 
     #   print 'currentBranch', currentBranch
        

        #-------------define project initial
        '''
        self.projectInitial = ""
        for par in self.project.split('_'):
            self.projectInitial = self.projectInitial + par[0]
        '''

        nameExcept = ['v01','v02','v03','v04','v05','v06','v07','cf','web','pc','v001','v002','v003','v004','v005','v006','v007',]
        namePartVerCharControl = ['v0','v1','v2','v3','v4','v5','v6','v7','v8','v9']
        projectInitial = ""
        nameOtherParts = []
        newprojectInitial = ""
        for par in self.project.split('_'):
            if par in nameExcept:
                nameOtherParts.append(par)
                
            else:
                projectInitial = projectInitial + par[0]
                
        for i in nameOtherParts:
            newprojectInitial = newprojectInitial +'_'+ i
            
        projectInitial = projectInitial + newprojectInitial
                
        self.projectInitial = projectInitial  
        
        projInitLength = len(self.projectInitial)
     #   print 'projInitLength',projInitLength
    
     #   print 'self.projectInitial', self.projectInitial
        #-----------finding last version, illegal
        tempVerList= []
        if len(self.fileInfoDict.keys()) >0:
            print "the folder is not empty"

            for verKey in self.fileInfoDict.keys():
      #          print self.fileInfoDict[verKey][0]
                fileNameLength = len(self.fileInfoDict[verKey][0])
      #          print 'fileNameLength',fileNameLength
                
                cutProjInit_fileName = self.fileInfoDict[verKey][0][projInitLength:fileNameLength]
      #          print 'cutProjInit_fileName',cutProjInit_fileName
      #          print 'check getSavingFile point A01'

                for i in cutProjInit_fileName.split('_'):
                   # print i
                    if i[0:2] in namePartVerCharControl:
                        existVerNum = i.split('v')[1]
      #                  print existVerNum

                print 'check getSavingFile point A02'

                
               # print verKey , self.fileInfoDict[verKey][0]
                #existVerNum = self.fileInfoDict[verKey][0].split('%s'%self.itemSelect)[1].split('_')[1].split('v')[1]
                
                
                
                
                tempVerList.append(existVerNum)
                
                
            
            tempNextVerNum = int(sorted(tempVerList)[-1])+1
            nextVerNum = 'v'+'%03d'%tempNextVerNum
            
        else:
            
            nextVerNum= 'v001'
            
        print 'check getSavingFile point B01'
        #------------define savingFileName in branch fileInfoDict
        getSavingName = self.projectInitial + '_' + self.assetNow +'_'+ self.processNow[0:3] + '_' + currentBranch +'_'+ nextVerNum +'_'+self.currentUser +'.mb'
        
    #    print 'getSavingName',getSavingName
        self.getSaveingBranchFolder()  #get saving folder
        self.longSavingName = self.workProject + '/' +'scenes' + '/' + self.currentBranchFolder +'/'  +getSavingName
        self.savingFolder = self.workProject + '/' +'scenes' + '/' + self.currentBranchFolder
        self.userPrefDict.update({'self.savingFolder':self.savingFolder})
        self.writeToUserPref()

     #   print 'self.longSavingName' ,self.longSavingName
        
        
        #cmds.file(self.longSavingName,rename=True)

        cmds.file( rename=self.longSavingName )
        cmds.file( save=True, type='mayaBinary' )
        
        #self.initialItemBuild()
        #self.getFilesInfoFromJson()
        self.buildExistFileInfoTree()
        self.createFileTable()  # create file list 
        self.getLinkingFileInfoText()   # create file description file fileName.txt in global folder
        
        thumbFileName = getSavingName.split('.')[0]
        self.getGlobalFolderLocation()
        #self.fullFileInfoName = fileInfoLocation + '/' + fileInfoName
        self.fullFileThumbName = self.fileInfoLocation + '/' + thumbFileName
        #print self.fullFileThumbName
        

        self.makeThumbnail()

        print "reNew file Table"
        
    

    
    def readFileInof(self):
        
        printText = self.plainTextEdit_BranchFileInfo.toPlainText()
        
   #     print printText
        
    
    
    

    def getFilesInfoFromJson(self):
        #   1.  export files to list_widget ,build from branchInfoFile as json ,ex. globals/shot/shot_02/shot02/shot_02_lighting.json
        #   2.  check the select tree item depth, 
        #   3.  export file dict, self.branchFilesInListDict       
        #   
        #   4.  return current branch select self.itemSelect
        #   5.  return current branch folder self.filesStoreBranchFolder
        #   6.  return all files dictionary in current branch self.branchFilesInListDict
        #   7.  return illegal files dictionary in current branch self.fileInfoDict  
        #
        #
        #
        #
        #
        #
        
        
        #initial all cache in dictionary
        self.branchFilesInListDict ={}
        self.fileInfoDict ={}
       # print 'self.branchFileStore',self.branchFileStore
        
        fileTypeFillet = self.plainTextEdit_optionPage_showFileType.toPlainText().split(',')
        #print fileTypeFillet
        print "run getFilesInfoFromJson starting......................."
        print "finding files in the branch"
        self.itemSelect =  self.treeWidget_branches.currentItem().text(0)
       # print 'self.branchFileStore',self.branchFileStore
        with open(self.branchFileStore, 'r') as f:
            self.branchPreDict = json.load(f)
          

            

       # print "self.branchPreDict.keys()",self.branchPreDict.keys()
        topLevelItemCount = len(self.branchPreDict.keys())    

        self.getExistBranchDict()
        self.buildExistFileInfoTree()
        print 'check point self.getFilesInfoFromJson A1'
       # print 'self.branchPreDict', self.branchPreDict


  #  def sdsafdg(self):  

        self.getSelectItemLevel()
        print 'check point self.getFilesInfoFromJson B1'

        
        tempTimeFileCompareDict = {}  # temp dictionary , that store file modify datetime and file name
        
       # print "self.branchPreDict", self.branchPreDict
       # t = os.path.getmtime(fileName)
       # print "self.fullItemIndex",self.fullItemIndex

    # datetime.datetime.fromtimestamp(t)
       
        if len(self.fullItemIndex) == 1:
            

            #print self.itemSelect
            self.branchFilesInListDict = self.branchPreDict[str(self.fullItemIndex[0])][self.itemSelect]['file']
            
            fileCount = len(self.branchPreDict[str(self.fullItemIndex[0])][self.itemSelect]['file'].keys())

            self.filesStoreBranchFolder = self.workProject + '/' +'scenes' + '/' + self.itemSelect
            #print fileTypeFillet

            countDiff = 0.1  # countDiff is for different file,that has the same modify time.
 
            for file in self.branchFilesInListDict.keys():  # get fileName List in the folder,self.filesStoreBranchFolder
                checkSingleFileNamePath = self.filesStoreBranchFolder +'/' +file
                if os.path.splitext(checkSingleFileNamePath)[1].split('.')[1] in fileTypeFillet:
                    t = (os.path.getmtime(checkSingleFileNamePath))+countDiff

                    tempTimeFileCompareDict.update({('%.2f'%t):checkSingleFileNamePath})

                    countDiff = countDiff + 0.1

    
                else:
                    pass
           
           # print "tempTimeFileCompareDict",tempTimeFileCompareDict
        elif len(self.fullItemIndex) == 2:
            
            secLevelItem = self.branchPreDict[str(self.fullItemIndex[0])][self.branchPreDict[str(self.fullItemIndex[0])].keys()[0]]['folder'][self.itemSelect]

          #  print "secLevelItem['file'].keys()",secLevelItem['folder']
            self.branchFilesInListDict = secLevelItem['file']
            secLevelFolder = self.branchPreDict[str(self.fullItemIndex[0])].keys()[0]

            self.filesStoreBranchFolder = self.workProject + '/' +'scenes' + '/' + secLevelFolder + '/' + self.itemSelect
          #  print self.filesStoreBranchFolder
           # print "self.branchFilesInListDict.keys()",self.branchFilesInListDict.keys()

            countDiff = 0.1  # countDiff is for different file,that has the same modify time.
           
            for file in self.branchFilesInListDict.keys():  # get fileName List in the folder,self.filesStoreBranchFolder
                checkSingleFileNamePath = self.filesStoreBranchFolder +'/' + file
 
                if checkSingleFileNamePath.split('.')[-1] in fileTypeFillet:

                    t = (os.path.getmtime(checkSingleFileNamePath))+countDiff

                    tempTimeFileCompareDict.update({('%.2f'%t):checkSingleFileNamePath})

                    countDiff = countDiff + 0.1
                  
                else:
                    pass
                    
    


        else:
            print "getFilesInfoFromJson check point C"

            topLayerItem = self.branchPreDict[str(self.fullItemIndex[0])].keys()[0]

            secLevelItem = self.branchPreDict[str(self.fullItemIndex[0])][self.branchPreDict[str(self.fullItemIndex[0])].keys()[0]]['folder']#[self.fullItemIndex[0]]]#]['folder'][self.itemSelect]['folder'].keys()[0]
            parSecLevelItem = secLevelItem.keys()[self.fullItemIndex[1]]
            thirdLevelItem = secLevelItem[parSecLevelItem]
            
            fourLevelItem = thirdLevelItem['folder'][self.itemSelect]['file']
            #print fourLevelItem
            self.branchFilesInListDict = fourLevelItem
            
            self.filesStoreBranchFolder = self.workProject + '/' +'scenes' + '/'+ topLayerItem + '/' + parSecLevelItem +'/'+self.itemSelect
            
          #  print self.filesStoreBranchFolder 
            countDiff = 0.1  # countDiff is for different file,that has the same modify time.

            for file in self.branchFilesInListDict.keys():  # get fileName List in the folder,self.filesStoreBranchFolder
                checkSingleFileNamePath = self.filesStoreBranchFolder +'/' + file
 
                if checkSingleFileNamePath.split('.')[-1] in fileTypeFillet:

                    t = (os.path.getmtime(checkSingleFileNamePath))+countDiff

                    tempTimeFileCompareDict.update({('%.2f'%t):checkSingleFileNamePath})

                    countDiff = countDiff + 0.1
                  
                    
                else:
                    pass
                    
    
            

        sortTimeList = sorted(tempTimeFileCompareDict.keys())  #sorted key in list
        fileCount = len(sortTimeList)

        #  self.fileInfoDict = {'01':["projectName_assetClass_assetName_process_v001_alpha.mb","alpha","2017/03/28    10:28","info xxxxxxxxxxxxxxxxxxxxxx"],
        #                     '02':["projectName_assetClass_assetName_process_v002_alpha.mb","alpha","2017/03/28    10:29"],
        #                     '03':["projectName_assetClass_assetName_process_v003_alpha.mb","alpha","2017/03/28    10:30"],
        #                     '04':["projectName_assetClass_assetName_process_v004_alpha.mb","alpha","2017/03/28    10:31"],
        #
        #   store file information into dictionary, self.fileInfoDict
        self.fileInfoDict ={} # define a new empty fileInfoDict
        for n in range(0,fileCount):
            serNum = sortTimeList[n]  #get file modify time
            indexNum = n +1
           # print  serNum
          #  print (n+1),datetime.datetime.fromtimestamp(float(serNum)) , tempTimeFileCompareDict[serNum].split('/')[-1],self.currentUser
            try:                                                     #split('.')[0].split('_v')[-1].split('_')
                #creatorName = tempTimeFileCompareDict[serNum].split('/')[-1].split('.')[0].split('_')[-2]
                creatorName = ''
                #creatorName = tempTimeFileCompareDict[serNum].split('/')[-1].split('.')[0].split('_')[-1].split('_v')[-1]
                if len(tempTimeFileCompareDict[serNum].split('/')[-1].split('.')[0].split('_v')[-1].split('_')) == 2:
                    creatorName = tempTimeFileCompareDict[serNum].split('/')[-1].split('.')[0].split('_v')[-1].split('_')[1]
                if len(tempTimeFileCompareDict[serNum].split('/')[-1].split('.')[0].split('_v')[-1].split('_')) == 3:
                    creatorName = tempTimeFileCompareDict[serNum].split('/')[-1].split('.')[0].split('_v')[-1].split('_')[1] +'_'+tempTimeFileCompareDict[serNum].split('/')[-1].split('.')[0].split('_v')[-1].split('_')[2] 
                
                if len(tempTimeFileCompareDict[serNum].split('/')[-1].split('.')[0].split('_v')[-1].split('_')) == 4:
                    creatorName = tempTimeFileCompareDict[serNum].split('/')[-1].split('.')[0].split('_v')[-1].split('_')[1] +'_'+tempTimeFileCompareDict[serNum].split('/')[-1].split('.')[0].split('_v')[-1].split('_')[2] +'_'+tempTimeFileCompareDict[serNum].split('/')[-1].split('.')[0].split('_v')[-1].split('_')[3] 
                
                #   print 'a'
               # creatorName
            except:
                creatorName = 'unKnow'
                
            self.fileInfoDict.update({"%03d"%indexNum:[tempTimeFileCompareDict[serNum].split('/')[-1],creatorName,serNum]})
            #print 'tempTimeFileCompareDict[serNum].split_user',tempTimeFileCompareDict[serNum].split('/')[-1].split('.')[0].split('_')[-1]



        
        print "run getFilesInfoFromJson End......................."
        #print self.fileInfoDict
        #print "self.branchFilesInListDict" ,self.branchFilesInListDict
        #print 'tempTimeFileCompareDict',tempTimeFileCompareDict
      
 #-----------------print out file info in textBrowser function start-------------------------------------------------------------------     
    def printOutFileInfo(self):
        # print self.fileInfoDict
        # get information form self.fileInfoDict
        # find selectItem row ,cloumn,
        
        getFileRow =self.tableWidget_FileList.currentItem().row()
        getFileColumn= self.tableWidget_FileList.currentItem().column()
        
        
        getFileKey = self.tableWidget_FileList.item(getFileRow,0).text()[1:]
        getFileName  = self.fileInfoDict[getFileKey][0]

        self.lineEdit_currentFileName.setText(getFileName)

        self.getLinkingFileInfoText()
        
        f = open(self.fullFileInfoName,'r')
        data = f.readlines()
        f.close
        #print data
        load = ""
        for line in data:
      #      print line
            load = load + line
            
     #   print load
        self.plainTextEdit_BranchFileInfo.setPlainText(load)
        
        self.getGlobalFolderLocation()

            
        selectScreenShotFileName = getFileName.split('.')[0] + '.0001.png'
        self.screenShot = self.fileInfoLocation + '/' +selectScreenShotFileName
        #print self.screenShotFileName
        
        self.getThumbnail()
        
     #   print 'self.branchDict',self.branchDict
     #   print 'self.screenShot',self.screenShot
    

 #-----------------print out file info in textBrowser function End-------------------------------------------------------------------     

    def getChildIndexCount(self):
        
        itemSelect = self.treeWidget_branches.currentItem()
    #    print itemSelect.text(0)

       # self.treeWidget_branches.current

    def createBranchDict(self):            #push button
        print "create New Branch"
        #self.newBranch = self.lineEdit_branchName.text()
        self.getNewBranchName()
     ##   print self.newBranch
        
        self.getBranchTopFromTreeList()    # ------------1
   #     print self.treeWidget_branches.currentIndex().row()


  #  def getBranchTopFromTreeListB(self): #---------1
     #   print "ggggggggg"
     #   print self.treeWidget_branches.topLevelItemCount()
        #print self.treeWidget_branches.indexOfTopLevelItem(1)

             
    def getBranchTopFromTreeList(self): #---------1
        self.getBranchInfoDict()
        
        print "getBranchTopFromTreeList"
        
        
        
        self.treeWidget_branches.clear()   #get assetDict 
        
        self.currentLevelItems = self.branchInfoDict.keys()   #get toLevelList ,as branch in every process, master branch01 branch02.....
        
        #self.createCurrentLevelItems()
        self.creatrTreeItems()
        #print topLevelItem
       # print "create topLevel Items"
       # self.itemCount = len(self.itemList)
       # print self.itemCount
        #print self.itemList
        
        
    def createNewBranchB(self):
        
        
        if len(self.treeWidget_branches.selectedItems()) == 0:
            print "aa"
            
        else:
            print"ggg"
               

        
        
        
    def getSelectItemLevel(self):  
        
        itemSelect = self.treeWidget_branches.currentItem()


        
     #   print self.topLayerItemList
        
        try:
            if len(itemSelect.parent().text(0)) >= 1:
                self.depth = 1             
                try:
                    if len(itemSelect.parent().parent().text(0)) >= 1:

                        self.depth = 2                   
                except:
                        pass               
        except:
            print "the Item is topLevelItem"
            self.depth =0            
                            
                            
        print self.depth        

        self.findParentTopLevelItem(self.depth)
        
        
        
        
        
    #----------find the topLevelItem, with parent from selected Item, and get the all level index---------------------------------------------------------------------------------
    #----------build all level index into self.fullItemIndex,<list>
    
    def findParentTopLevelItem(self,depth):
        print 'run findParentTopLevelItem start'
        

        
        selectItem = self.treeWidget_branches.currentItem().text(0)
        
        #topLayerItemDict
        print selectItem

        ##finding top Level Item topLevelItem(topItemLayerIndex)
        if self.depth == 0:
            print "top level item"

            topLevelItemIndex = self.topLayerItemDict[selectItem]
        
       # print "selectItem          :",selectItem
       # print "topLevelItem  :",selectItem
      #  print "topLevelItemIndex   :",topLevelItemIndex  
            self.fullItemIndex = [topLevelItemIndex]

            self.userPrefDict.update({'self.fullItemIndex':['%s'%topLevelItemIndex,'none','none']})

            
        #finding 2nd level item topLevelItemIndex and childIndex ,     topLevelItem(topLevelItemIndex).child(secLevelItemIndex)
        elif self.depth == 1 :
            print "2nd level item"
            

            topLayerItem = self.treeWidget_branches.currentItem().parent().text(0)
            
            topLevelItemIndex = self.topLayerItemDict[topLayerItem]
            
           # print self.secLayerItemDict
            secLevelItemIndex = self.secLayerItemDict[selectItem]
          
         #   print "selectItem          :",selectItem
          #  print "topLevelItem  :",topLayerItem
          #  print "topLevelItemIndex   :",topLevelItemIndex         
          #  print "secLevelItemIndex   :",secLevelItemIndex
            
            self.fullItemIndex = [topLevelItemIndex,secLevelItemIndex]
            self.userPrefDict.update({'self.fullItemIndex':['%s'%topLevelItemIndex,'%s'%secLevelItemIndex,'none']})


        #finding 3rd level item topLevelItemIndex and childIndex ,     topLevelItem(topLevelItemIndex).child(secLevelItemIndex).chile(thirdLevelItemIndex)            
        else:
            print "3rd level item"
            

            thirdLevelItemIndex = self.thirdLayerItemDict[selectItem]     
            

                        
            secLayerItem = self.treeWidget_branches.currentItem().parent().text(0)  
            
            secLevelItemIndex = self.secLayerItemDict[secLayerItem]
            
            topLayerItem = self.treeWidget_branches.currentItem().parent().parent().text(0)
            
            topLevelItemIndex =self.topLayerItemDict[topLayerItem]

           
            


            
          #  print "selectItem          :",selectItem
          #  print "parentTopLevelItem  :",topLayerItem
           # print "parentSecLayerItem  :",secLayerItem
          #  print "topLevelItemIndex   :",topLevelItemIndex          #topLevelItem(topLevelItemIndex).child(1)
          #  print "secLevelItemIndex   :",secLevelItemIndex
           # print "thirdLevelItemIndex :",thirdLevelItemIndex fullItemIndex
            
            self.fullItemIndex = [topLevelItemIndex,secLevelItemIndex,thirdLevelItemIndex]
            #self.fullItemIndexStore = [str(topLevelItemIndex),str(secLevelItemIndex),str(thirdLevelItemIndex)]
            #'%s'%str(topLevelItemIndex),'%s'%str(secLevelItemIndex),'%s'%str(thirdLevelItemIndex)

    
            self.userPrefDict.update({'self.fullItemIndex':['%s'%topLevelItemIndex,'%s'%secLevelItemIndex,'%s'%thirdLevelItemIndex]})

        self.writeToUserPref()
       # print 'self.fullItemIndex',self.fullItemIndex

        print 'run findParentTopLevelItem End'


    



        
    def createNewBranchCombo(self):  # creat New Branch Test  
        print "run createNewBranchCombo start"
        itemSelect = self.treeWidget_branches.currentItem()
        #self.newBranch = self.lineEdit_branchName.text()
        self.getNewBranchName()
        topLayerItem = []
        
        self.getExistBranchDict()
      #  print itemSelect.text(0)
        
        try:
            if len(self.treeWidget_branches.selectedItems()) == 0:
                
                print "create topLayerItem"

                
                if self.newBranch in self.topLayerItemDict.keys(): #check if the new branch Name exist on topLevelItem Dict 
                    print "change a new Branch Name"

                    
                else:
                    print "create a new topLevelItem"
                    self.createNewBranchTopLevel()



            else:
                pass
                
                self.getSelectItemLevel()
                self.createNewBranchChildLevel()
            
            self.checkMasterExist()  
            self.buildExistFileInfoTree()     
            self.buildTreeFromExistFileData()
                        
        except:
            pass
       # self.initialItemBuild()   #reNew treeWidget
        self.lineEdit_branchName.setText('')

        print "run createNewBranchCombo End"
                
                
    def updateAssetBranchFileInfo(self,levelList):
        print "update assetBranchFileInfo.json"
        path = "C:/mayaProjs/3d_pipeline_test/global/"
        fileName = "shot_02_lighting.json"
        storeFileName = path + fileName
        #storeFile = open(storeFileName,'r')
        
        
        
        #storeFile.close
        
        
        
       # fileName = "C:/mayaProjs/3d_pipeline_test/global/shot_02_lighting.json"

        #with open(fileName, 'r') as f:
    
       # data = json.load(f)
        
        



    # create New Branch on Top Level ----------------------------------------------------------------------------------------------------------------------
    def createNewBranchTopLevel(self):      
        print "......createNewBranchTopLevel function Start............."
      #  self.defineFontLevelTwo()
        #self.newBranch = self.lineEdit_branchName.text()
        self.getNewBranchName()
     #   print self.newBranch 
     
        #self.creatrTreeItems()
        #print "new Branch" ,self.newBranch
    ##  --------------------------UI------------------------------------------------------------------------------------
        ##create Top Level Branch  ,the same level as master
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_branches).setForeground(0,self.brushLevelTwo)
        self.topLayerBranchIndex =(self.treeWidget_branches.topLevelItemCount()-1)
       # print type(self.topLayerBranchIndex) , self.topLayerBranchIndex
        

        #self.treeWidget_branches.topLevelItem(self.topLayerBranchIndex).setForeground(0,self.brushLevelTwo)
        self.treeWidget_branches.topLevelItem(self.topLayerBranchIndex).setText(0,QtWidgets.QApplication.translate("MainWindow", "tempName", None, -1))
        self.treeWidget_branches.topLevelItem(self.topLayerBranchIndex).setText(0,self.newBranch )
  
        self.treeWidget_branches.topLevelItem(self.topLayerBranchIndex).setFont(0,self.fontLevelTwo) #define font size     

        
    ##-------------------------creader folder---------------------------------------------------------  

        createTopLayerFoder = self.workProject + '/' +'scenes'+ '/'+ self.newBranch 
      #  print os.path.isdir(createTopLayerFoder)
        if os.path.isdir(createTopLayerFoder) == True:
            print "already has "+"%s"%createTopLayerFoder + " folder"
            
        else:
            self.createNewFolder(createTopLayerFoder)

           # os.mkdir(createTopLayerFoder)
            
                
     #   print createTopLayerFoder
        
        #   update self.branchDict, the dictionary of all branches   
    
        # topLevelItemCount = len(self.branchDict.keys())
        
        # self.branchDict.update({str(topLevelItemCount):{self.newBranch:{}}})
                          


        

    #   update assetBranchFileInfo.json
  
       # self.getFilesInfoFromJson()           #reNew jsonFile and dirctionary
 
        print "......createNewBranchTopLevel function End............."
        
        
        
        
        
        
        
        
        
    
    # create New Branch on Child Level ----------------------------------------------------------------------------------------------------------------------
    def createNewBranchChildLevel(self): 
     #   print"ggg"
      #  print len(self.fullItemIndex)    
     #   print self.fullItemIndex 
       # self.getExistBranchDict()
        itemSelect = self.treeWidget_branches.currentItem().text(0)
        #self.newBranch = self.lineEdit_branchName.text()
        self.getNewBranchName()
    ##    print self.newBranch

        topLevelIndex = int(self.fullItemIndex[0])
        
        try:                     #get second Level index, because,it,may not exist, used try
            secondLevelIndex = int(self.fullItemIndex[1])
        except:
            pass
        


    
        if len(self.fullItemIndex) == 1:     # create 2nd Level Item under select item
            print "Create level 2 branch"

            existLevelCount = len(self.branchDict[str(self.fullItemIndex[0])][itemSelect].keys())   # = child,secLevelIndex
      #      print existLevelCount
            secItemList = self.branchDict[str(self.fullItemIndex[0])][itemSelect].keys()
       #     print secItemList

      #      print "topLevelIndex",topLevelIndex

            if self.newBranch in secItemList:
        #        print
         #       print "Change New Branch Name"
                pass
                
                
            else:
                print "build 2nd level item"
                pass
                
         
                try:
                    # addChild sanple:       QtWidgets.QTreeWidgetItem(self.treeWidget_branches.topLevelItem(0)).addChild(0)
                    
                   

       #             print 'topLevelIndex, existLevelCount',topLevelIndex, existLevelCount
                    
                    
                    print "create New 2nd Item"
                    QtWidgets.QTreeWidgetItem(self.treeWidget_branches.topLevelItem(topLevelIndex)).setForeground(0,self.brushLevelThree)  #build new item from index

                    self.treeWidget_branches.topLevelItem(topLevelIndex).child(existLevelCount).setFont(0,self.fontLevelThree)
    


                except:
                    #pass
                
                    print "change Name"
       #             print topLevelIndex, existLevelCount
                    
            self.treeWidget_branches.topLevelItem(topLevelIndex).child(existLevelCount).setText(0,self.newBranch)   #named the newItem , from typeIn line edit
            # create folder
            createTopLayerFoder = self.workProject + '/' +'scenes'+ '/' + itemSelect +'/' + self.newBranch
       #     print createTopLayerFoder
       #     print os.path.isdir(createTopLayerFoder)
            if os.path.isdir(createTopLayerFoder) == True:
                print "already has %s folder"%createTopLayerFoder
            else:
        #        print "create %s folder"%createTopLayerFoder
              #  os.mkdir(createTopLayerFoder)
                self.createNewFolder(createTopLayerFoder)





        elif len(self.fullItemIndex) == 2: # create 2nd Level Item under select item
            print "Create level 3 branch"
      #      print self.fullItemIndex
            
            thirdItemList = self.branchDict[str(self.fullItemIndex[0])][self.branchDict[str(self.fullItemIndex[0])].keys()[0]][itemSelect].keys()
       #     print thirdItemList
            existThirdLevelCount = len(thirdItemList)
            
            if self.newBranch in thirdItemList:
                print"Change New Branch Name"
                
            else:
                print"check point C01"
                try:
                    QtWidgets.QTreeWidgetItem(self.treeWidget_branches.topLevelItem(topLevelIndex).child(secondLevelIndex)).setForeground(0,self.brushLevelFour)  #set 4rd level brush
                    self.treeWidget_branches.topLevelItem(topLevelIndex).child(secondLevelIndex).child(existThirdLevelCount).setFont(0,self.fontLevelFour)  #set 4rd level font

                except:
                  #  pass
                
                    print "change Name"
              #      print topLevelIndex, existLevelCount
                    
            self.treeWidget_branches.topLevelItem(topLevelIndex).child(secondLevelIndex).child(existThirdLevelCount).setText(0,self.newBranch)   #named the newItem , from typeIn line edit

            # create folder
            getTopLevelItem = self.branchDict[str(self.fullItemIndex[0])].keys()[0] 

          #  getSecLevelItem = self.branchDict[str(self.fullItemIndex[0])][self.branchDict[str(self.fullItemIndex[0])].keys()[0]].keys()[self.fullItemIndex[1]]
            createTopLayerFoder = self.workProject + '/' +'scenes'+ '/' +getTopLevelItem +'/' + itemSelect +'/' + self.newBranch
         #   print createTopLayerFoder
       #     print os.path.isdir(createTopLayerFoder)
            if os.path.isdir(createTopLayerFoder) == True:
                print "already has %s folder"%createTopLayerFoder
            else:
                print "create %s folder"%createTopLayerFoder
               # os.mkdir(createTopLayerFoder)
                self.createNewFolder(createTopLayerFoder)




        else:
            print"too many Branch Eevels"
            print self.fullItemIndex
            
            
        self.updateMasterDateInBranchDict()
        self.getExistBranchDict()
      
        
        
    def changeName(self):
        print "change branch name"
       # print self.treeWidget_branches.currentItem().text(0)
        self.treeWidget_branches.topLevelItem(0).child(0).setText(0,"sdsdsd")
        #self.treeWidget_branches.topLevelItem(0).setText(0,QtWidgets.QApplication.translate("MainWindow", "tempName", None, -1))
       # self.treeWidget_branches.topLevelItem(self.topLayerBranchIndex).setText(0,self.newBranch )
        
        
        #self.treeWidget_branches.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "gggg", None, -1))
        
        
    def getNewBranchName(self):
        print "run getNewBranchName start"
        
        self.newBranch = self.lineEdit_branchName.text()
        
        if self.newBranch == "master":
            print "change other name, not master"
            pass
            
        else:
            pass

        print "run getNewBranchName End"
        
        
        
        
        
        
        
    def createTestTreeDictB(self):  # creat New Branch Test  
        
        selectItem = self.treeWidget_branches.currentItem()
        
        print selectItem.text(0)
        
         
        selectItemLevel = selectItem.parent()
        print selectItemLevel.text(0)
        
        if selectItemLevel.isEnable() == "True":
        #if len(selectItemLevel.text(0)) >= 1:
            print "aaa"
            #print selectItemLevel.text(0)
            depth = 1
           # selectItemLevel = selectItemLevel.parent()
           # if len(selectItemLevel.text(0)) >= 1:
              #  depth = 2
                
          #  else:
  
            
        else:
            print "it is topLevelItem"
            pass
                
        print depth
                 
        #print selectItemLevel
       # print len(selectItemLevel)
        
        
        
    def createTestTreeDictC(self):  # creat New Branch Test  
        print " test test test test test"  
        
        #find topLevelItems and store in List
        
        topLayerItems = []
        topLayerCount = self.treeWidget_branches.topLevelItemCount()
        for item in range(0,topLayerCount):
            topLayerItems.append(self.treeWidget_branches.topLevelItem(item).text(0))
        print topLayerItems
        
        
        #check the new branch exist
        #self.newBranch = self.lineEdit_branchName.text()
        self.getNewBranchName()
        print self.newBranch
        
        if self.newBranch in topLayerItems:
            print "the branch Name is already exist"
            
        else:
            print "new Branch" ,self.newBranch
        
        #   #create Top Level Branch  ,the same level as master
            item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_branches)
            
            
            tempName = "tempName"

            self.treeWidget_branches.topLevelItem(topLayerCount).setText(0, QtWidgets.QApplication.translate("MainWindow", str(self.newBranch), None, -1))
            
        
        
    def checkCurrentItemLevel(self):
        
        # check parent is exist
        item = self.treeWidget_branches.currentItem()
        print item.parent().text(0)
        
        
    def updateMasterDateInBranchDict(self):
        print"reNew the Master data in Branch Dictionary"

        masterBranchSecCount = self.treeWidget_branches.topLevelItem(0).childCount()
        print "masterBranchSecCount       :",   masterBranchSecCount, type(masterBranchSecCount)
        newMasterBranchSecCount = (masterBranchSecCount-1)
        
       # for count in (0,masterBranchSecCount):
        newMasterBranch = self.treeWidget_branches.topLevelItem(0).child(newMasterBranchSecCount).text(0)
        print newMasterBranch 
            
        self.branchDict['0']['master'].update({str(newMasterBranch):{}})   #update MasterBranch in Master, BranchDict

      #  print self.branchDict['0']
        self.getExistBranchDict()
        #self.buildExistFileInfoTree()
        
        
        
##    build tree list , store in dictionary
        
    def getExistBranchDict(self):
        '''finding all data, folder ,and files in the select process,lightin,animation....,
        and export to json file'''
        
        print "run getExistBranchDict start"
        
        
        masterBranchDictData = self.branchDict['0']['master']
        
        self.branchDict['0']['master'].update(masterBranchDictData)
        
       # self.branchDict={"0":{"master":{}}}
        
        self.topLayerCount = self.treeWidget_branches.topLevelItemCount()
        
        self.allLayerItemsDict = {'master':'0'}
        
        #self.topLayerItemList = [{'master':"0"}]
        
        self.topLayerItemDict = {'master':'0'}
        self.secLayerItemDict ={}
        self.thirdLayerItemDict={}
                               
        
        self.secLayerItemList = []
        
        self.thirdLayerItemList = [] 
        
        #print self.branchDict

        
        for itemCount in range(1,self.topLayerCount):
            topLevelKeyNum = itemCount
            
            # update topLevelItem
            self.branchDict.update({"%s"%topLevelKeyNum:{self.treeWidget_branches.topLevelItem(itemCount).text(0):{}}})

            #self.topLayerDict.update({"%s"%topLevelKeyNum:self.treeWidget_branches.topLevelItem(itemCount).text(0)})
            
            #self.allLayerItemsDict.update({self.treeWidget_branches.topLevelItem(itemCount).text(0):'0'})   
           # self.topLayerItemList.append({self.treeWidget_branches.topLevelItem(itemCount).text(0):itemCount}) #add to all items in top Layer into List
            
            self.topLayerItemDict.update({self.treeWidget_branches.topLevelItem(itemCount).text(0):itemCount})
            
        for itemCount in range(1,self.topLayerCount):   # add secLevelItems except Master
        
            itemName = self.treeWidget_branches.topLevelItem(itemCount).text(0)
            
            secLayerItemCount = self.treeWidget_branches.topLevelItem(itemCount).childCount()

            # update 2nd level items
            if secLayerItemCount == 0:
              #  print "0"
                pass
            else:
                for secLayerItemNum in range(0,secLayerItemCount):
                    secLayerItemName = self.treeWidget_branches.topLevelItem(itemCount).child(secLayerItemNum).text(0)

 
                    self.branchDict[str(itemCount)][(self.branchDict[str(itemCount)].keys()[0])].update({secLayerItemName:{}})
                    
                    thirdLevelCount = self.treeWidget_branches.topLevelItem(itemCount).child(secLayerItemNum).childCount()
                    
                   # self.allLayerItemsDict.update({secLayerItemName:'1'})    #add to allLayerItemsDict in 2nd Layer
                   
                    #self.secLayerItemList.append({secLayerItemName:secLayerItemNum}) #add to all items in 2nd Layer into List
                    self.secLayerItemDict.update({secLayerItemName:secLayerItemNum}) #add to all items in 2nd Layer into Dictionary
                    # update 3rd level items
                    
                    for thirdLevelItemNum in range(0,thirdLevelCount):
                        
                        thirdLevelItemIndex = self.treeWidget_branches.topLevelItem(itemCount).child(secLayerItemNum)
                        
                        thirdLevelItemName = self.treeWidget_branches.topLevelItem(itemCount).child(secLayerItemNum).child(thirdLevelItemNum).text(0)
                        
                        self.branchDict[str(itemCount)][(self.branchDict[str(itemCount)].keys()[0])][secLayerItemName].update({thirdLevelItemName:{}})
                        
                      #  self.allLayerItemsDict.update({thirdLevelItemName:'2'}) #add to allLayerItemsDict in 3rd Layer
                        #self.thirdLayerItemList.append({thirdLevelItemName:thirdLevelItemNum})  #add to all items in 2nd Layer into List
                        self.thirdLayerItemDict.update({thirdLevelItemName:thirdLevelItemNum}) #add to all items in 2nd Layer into dictionary
                        #print thirdLevelItemName 
                    
                    #print thirdLevelCount
                    

      #  print self.branchDict
       # self.exportBranchJsonFile()    #export dictionary to json file
        
       # print self.topLayerItemList
       # print self.topLayerItemDict
       # print self.secLayerItemDict
       # print self.thirdLayerItemDict
        
        
        print "run getExistBranchDict End"
       

    def readBranchJsonFile(self):
        if self.isAsset == True:
            branchDictFile = self.assetBranchFileStore
        else:
            branchDictFile = self.shotBranchFileStore
            
        with open(branchDictFile) as data_file:    
            data = json.load(data_file)
        print data
       # self.getFilesInfoFromJson()
       # print 'self.self.branchDict',self.branchDict
        
        
            
    def exportBranchJsonFile(self):  
        '''export self.branchDict to json file '''
        
          
        formatedBranchDict = json.dumps(self.branchDict, sort_keys=True , indent =4)  
               
        #branchDictFile = "c:/temp/"+"%s"%self.assetName + "_branchDictFile.json"
        if self.isAsset == True:
            branchDictFile = self.assetBranchFileStore
        else:
            branchDictFile = self.shotBranchFileStore
        
        storeFile = open(branchDictFile,'w')
        
        storeFile.write(formatedBranchDict)
        
        storeFile.close
                    

       # print formatedBranchDict
        
        
    
        
        
        
        
        
        
        

        
        
        
        
        
        
        


        

    def creatrTreeItems(self):
        
        
        #self.newBranch = self.lineEdit_branchName.text()
        
       # item = self.treeWidget_branches.currentItem()
        item = self.treeWidget_branches.currentItem()
        print item.text(0)
       # count = self.treeWidget_branches.currentIndex().column()
       # rowCount = self.treeWidget_branches.currentIndex().row()
        #topLevelItem = self.treeWidget_branches.topLevelItem(0)
        columnCount = self.treeWidget_branches.columnCount()

        #topLevelItem = self.treeWidget_branches.indexFromItem(1)

        print columnCount
        
        headerItem = self.treeWidget_branches.headerItem()
        
        print headerItem
        #print rowCount
        #print topLevelItem.topLevelIndex()
    
       # count = self.treeWidget_branches.topLevelItemCount()
        #self.assetSelect = item.text()
       # topLevelItem = self.treeWidget_branches.itemAbove()
        
       # print topLevelItem
       # print self.assetSelect
        #print self.treeWidget_branches.currentItem().text()



        
        
        
        

    def createTestTreeDictC(self):
            
       # dictFileName = "c:/temp/testTreeDict.json"
      #  preLoadData = open(dictFileName,'r')
        
        #content = preLoadData.read()
       # 
        #aa = json.dumps(preLoadData, sort_keys=True , indent =4,ensure_ascii=False) 
       # print content
       # preLoadData.close
        
        print "initCurrentLevelKeyList" , self.getCurrentLevelList
        
        #testTreeDict = {}
        #tempTreeDictKey =""
        #tempTreeDictValue ={}
        
        #self.newBranch = self.lineEdit_branchName.text()
        self.getNewBranchName()
        
        tempTreeDictKey = self.newBranch.split(';')[0]
        
        tempTreeDictValue = self.newBranch.split(';')[1]
        
        print "tempTreeDictKey",tempTreeDictKey
        
        self.getCurrentLevelList.append(tempTreeDictKey)
        

        
        #testTreeDict.update({tempTreeDictKey:tempTreeDictValue})
        
        print self.getCurrentLevelList

        
        #print "newBranch" ,newBranch
        
       # tempList = {underBranch:newBranch}
        
        
        
      #  print "tempList",testTreeDict
        #
        #testTreeDict[underBranch].update(newBranch)
        
        
        
        #dictWrite = open(dictFileName,'w')
        
        #data = json.dumps(tempList, sort_keys=True , indent =4,ensure_ascii=False) 
      #  print testTreeDict
       # dictWrite.write(data)
        
       # dictWrite.close
        
    def openFolder(self):
        self.savingFolder = self.userPrefDict['self.savingFolder']
        print self.savingFolder

        currentProjWin =''
        for cha in self.savingFolder:
            if cha =="/":
                currentProjWin += '\\'
            else:    
                currentProjWin += cha 
        openCmd = "explorer "+'%s'%currentProjWin
        subprocess.call(openCmd)


        
    def openFolderTypical(self,tempfolder):
        
        
        openTypicalFolder =''
        for cha in tempfolder:
            if cha =="/":
                openTypicalFolder += '\\'
            else:    
                openTypicalFolder += cha 
        openCmd = "explorer "+'%s'%openTypicalFolder
        subprocess.call(openCmd)


        
    def createCurrentLevelItems(self):
        
        self.itemCount = len(self.currentLevelItems)
        
        
        print self.currentLevelItems
        
        print self.itemCount
        
        
        num_item_0 =1
        while num_item_0 < (self.itemCount +1):
            item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_branches)
            num_item_0 = num_item_0 +1
            print self.treeWidget_branches.currentIndex().row()

            


        for i in range(0,self.itemCount):
            #print i
            topLevelItem = self.treeWidget_branches.topLevelItem(i)
            tempName = "tempName"
            topLevelItem.setText(0,QtWidgets.QApplication.translate("MainWindow",tempName))  #topLevelItem named "tempName"
   # def temp(self):            
           # print topLevelItem
            print self.currentLevelItems[i]
            topLevelItem.setText(0,self.currentLevelItems[i])  #change tempName to folder Name , in isDirList

        #print self.treeWidget_branches.topLevelItem()[0]
        
       
        
        





        
        
    def getBranchInfoDict(self):
        
        self.branchInfoDict = {'master':{},
                              'branch_01':{},
                              'branch_02_alpha':{},
                              'test_01':{},
                              'extea_01':{},
                              'temp':{}
                              }


        self.branchInfoDictB = {'0':{'master':{},
                                    'branch_01':{},
                                    'branch_02_alpha':{},
                                    'test_01':{},
                                    'extea_01':{},
                                    'temp':{}
                                    }
        }
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
####################page publishTool
    def a_page2_split(self):
        print "page 2 start"
    
    
    def unSelectCheck(self):
        print "aasdasdasdd"
       # if self.treeWidget_filesList.topLevelItem(0).child(0).checkState(0) == QtCore.Qt.CheckState.Checked:
       # if self.treeWidget_filesList.topLevelItem(0).checkState(0) == QtCore.Qt.CheckState.Checked:
        #    print self.treeWidget_filesList.topLevelItem(0).text(0)
           
        '''
        self.treeWidget_FiletOption.topLevelItem(0).setExpanded(1)#自動展開
        self.treeWidget_FiletOption.topLevelItem(1).setExpanded(1)#自動展開
        self.treeWidget_FiletOption.topLevelItem(2).setExpanded(1)#自動展開
        self.treeWidget_FiletOption.topLevelItem(3).setExpanded(1)#自動展開
     
        self.treeWidget_FiletOption.topLevelItem(0).setCheckState(0, QtCore.Qt.Checked)#設定勾選   Collect Files
        self.treeWidget_FiletOption.topLevelItem(0).child(0).setCheckState(0, QtCore.Qt.Checked)#設定勾選   Prman Texture
        self.treeWidget_FiletOption.topLevelItem(0).child(1).setCheckState(0, QtCore.Qt.Checked)#設定勾選   Maya Texture
        self.treeWidget_FiletOption.topLevelItem(0).child(2).setCheckState(0, QtCore.Qt.Checked)#設定勾選   GpuCache
        self.treeWidget_FiletOption.topLevelItem(0).child(3).setCheckState(0, QtCore.Qt.Checked)#設定勾選   RibArchive
        self.treeWidget_FiletOption.topLevelItem(0).child(4).setCheckState(0, QtCore.Qt.Checked)#設定勾選   Alembic
        self.treeWidget_FiletOption.topLevelItem(0).child(5).setCheckState(0, QtCore.Qt.Unchecked)#設定勾選   Prman Light
        self.treeWidget_FiletOption.topLevelItem(0).child(6).setCheckState(0, QtCore.Qt.Unchecked)#設定勾選   Maya Fluid
        self.treeWidget_FiletOption.topLevelItem(0).child(7).setCheckState(0, QtCore.Qt.Unchecked)#設定勾選   Maya nParticle Cache
        self.treeWidget_FiletOption.topLevelItem(0).child(8).setCheckState(0, QtCore.Qt.Checked)#設定勾選
        self.treeWidget_FiletOption.topLevelItem(0).child(9).setCheckState(0, QtCore.Qt.Checked)#設定勾選
    
        self.treeWidget_FiletOption.topLevelItem(1).setCheckState(0, QtCore.Qt.Checked)#設定勾選  Check Plugin
        self.treeWidget_FiletOption.topLevelItem(1).child(0).setCheckState(0, QtCore.Qt.Checked)#設定勾選 unUsed Plugin
        self.treeWidget_FiletOption.topLevelItem(1).child(9).setCheckState(0, QtCore.Qt.Checked)#設定勾選 
        
        
        
        self.treeWidget_FiletOption.topLevelItem(2).setCheckState(0, QtCore.Qt.Checked)#設定勾選 Check Asset Unit
        self.treeWidget_FiletOption.topLevelItem(2).child(0).setCheckState(0, QtCore.Qt.Checked)#設定勾選 Check BB
        self.treeWidget_FiletOption.topLevelItem(2).child(1).setCheckState(0, QtCore.Qt.Checked)#設定勾選 Check Position
        self.treeWidget_FiletOption.topLevelItem(2).child(2).setCheckState(0, QtCore.Qt.Checked)#設定勾選 Check Repeat
        self.treeWidget_FiletOption.topLevelItem(2).child(3).setCheckState(0, QtCore.Qt.Checked)#設定勾選 ReName SG
        
        #self.treeWidget_FiletOption.topLevelItem(3).setCheckState(0, QtCore.Qt.Checked)#設定勾選 Duplicated ShapeName
        self.treeWidget_FiletOption.topLevelItem(3).child(0).setCheckState(0, QtCore.Qt.Checked)#設定勾選 #ribArchive shapes
        self.treeWidget_FiletOption.topLevelItem(3).child(1).setCheckState(0, QtCore.Qt.Checked)#設定勾選 #gpuCache shapes
        self.treeWidget_FiletOption.topLevelItem(3).child(2).setCheckState(0, QtCore.Qt.Checked)#設定勾選 #alembic shapes
        self.treeWidget_FiletOption.topLevelItem(3).child(3).setCheckState(0, QtCore.Qt.Unchecked)#設定勾選 #fluid shapes
        self.treeWidget_FiletOption.topLevelItem(3).child(4).setCheckState(0, QtCore.Qt.Unchecked)#設定
        '''
    def reflashTree(self):

        self.buildItemTree()  
        self.createCopyFileInfoDictInit()    #initial  self.createCopyFileInfoDictInit    
        self.allCopyFileInfoDictItemsValue = 0 #initial  self.allCopyFileInfoDictItemsValue    

        self.allNodeNameFileNameDict={}  #for replace root
        
        if self.treeWidget_FiletOption.topLevelItem(0).child(0).checkState(0) == QtCore.Qt.CheckState.Checked:# check rib ischecked
            try:
                self.findPrmanTexture()
            except:
                pass
        if self.treeWidget_FiletOption.topLevelItem(0).child(1).checkState(0) == QtCore.Qt.CheckState.Checked:# check rib ischecked
            try:
                self.findMayaTexture()
            except:
                pass
        if self.treeWidget_FiletOption.topLevelItem(0).child(2).checkState(0) == QtCore.Qt.CheckState.Checked:# check rib ischecked
        
            try:
                self.findGpuCaches()
            except:
                pass
                
        if self.treeWidget_FiletOption.topLevelItem(0).child(3).checkState(0) == QtCore.Qt.CheckState.Checked:# check rib ischecked
        
            try:
                self.findRibArchives()
            except:
                pass

        if self.treeWidget_FiletOption.topLevelItem(0).child(4).checkState(0) == QtCore.Qt.CheckState.Checked:# check rib ischecked
        
            try:
                self.findAlembics()
            except:
                pass            

        if self.treeWidget_FiletOption.topLevelItem(0).child(5).checkState(0) == QtCore.Qt.CheckState.Checked:# check rib ischecked
            
            try:
                self.findPrmanLights()
            except:
                pass            
        if self.treeWidget_FiletOption.topLevelItem(0).child(6).checkState(0) == QtCore.Qt.CheckState.Checked:# check rib ischecked
                 
            try:
                self.mayaFluidCache()
            except:
                pass            
        if self.treeWidget_FiletOption.topLevelItem(0).child(7).checkState(0) == QtCore.Qt.CheckState.Checked:# check rib ischecked
             
            try:
                self.mayanParticleCache()
            except:
                pass      
                
        if self.treeWidget_FiletOption.topLevelItem(1).child(0).checkState(0) == QtCore.Qt.CheckState.Checked:# check rib ischecked
                 
            try:
                self.findPlugin()  
            except:
                 pass   
                 
        #if self.treeWidget_FiletOption.topLevelItem(3).checkState(0) == QtCore.Qt.CheckState.Checked:# check rib ischecked
                 
                     
        try:
            self.storeDuplicateNameDictToJson()
        except:
            pass
            
       # print 'self.allCopyFileInfoDict',self.allCopyFileInfoDict

 #      



    def replaceFile(self):
        print "replaceFile start"
        
        #cmds.setAttr('PxrTexture9.filename','C:/Users/alpha.DESKTOP-1S1STEK/Pictures/IMG_1483.PNG',typ = "string")
        newFileLocation = cmds.fileDialog2(fm=1,rf=True)[0]
       # print newFileLocation
        #C:/Users/alpha.DESKTOP-1S1STEK/Pictures/IMG_1485.PNG
        cmds.setAttr('%s%s'%(self.treeWidget_filesList.currentItem().text(0),self.treeWidget_filesList.currentItem().text(3)),newFileLocation,typ="string")
        #print self.treeWidget.currentItem().text(0) +self.treeWidget.currentItem().text(3),newFileLocation
        self.treeWidget_filesList.topLevelItem(int(self.treeWidget_filesList.currentItem().text(4))).child(int(self.treeWidget_filesList.currentItem().text(5))).setText(1,newFileLocation.split('/')[-1])
        
    def getSelectedNode(self):
        cmds.select(self.treeWidget_filesList.currentItem().text(6))
        
        
        
    def showFileName(self):
        if self.treeWidget_filesList.indexOfTopLevelItem(self.treeWidget_filesList.currentItem()) ==-1:  #get select File Name
            self.lineEdit_showFileName.setText(self.treeWidget_filesList.currentItem().text(2))
            mode = self.treeWidget_filesList.currentItem().text(3)
            fileName = self.treeWidget_filesList.currentItem().text(2)
            self.showFileMetaData(fileName,mode)
        else:
            pass
           # print self.treeWidget_filesList.indexOfTopLevelItem(self.treeWidget_filesList.currentItem()) 
            
         #   print self.treeWidget_filesList.topLevelItem(0).checkState(0) #== QtCore.Qt.CheckState.Checked
         #   print self.treeWidget_filesList.topLevelItem(1).checkState(0)
           # print "aaa"
           # return self.treeWidget_filesList.currentItem().parent(),self.treeWidget.currentItem().parent().indexOfChild(self.treeWidget.currentItem())
     #   else:  
       #     print "bbbb" 
            #return self.treeWidget_filesList.currentItem(),-1
        #print self.treeWidget_filesList.currentItem().text(2)

    
    def delectChecked(self):
        self.searchIsChecked()
        delectList = self.checkNodeDict.keys()
        
       # deleteTable= self.checkNodeDict.keys() treeWidget
        for i in self.checkNodeDict.keys():
            try:
                if len(cmds.listRelatives( i, p=True )) > 0:
                    
                    #print cmds.listRelatives( i, p=True )
                    delectList.append(cmds.listRelatives( i, p=True )[0])

            except:
                pass
        
       # print delectList
        cmds.delete(delectList)
        self.checkNodeDict = {}
        self.delectBadPlugin()  # delect checked Plugin
        self.reflashTree()

       # cmds.relationship('PxrTexture2',q=True)
    def delectBadPlugin(self):
        for plugin in self.badPluginNodeList.keys():
            try:
                cmds.unknownPlugin(plugin,r=True)
            except:
                pass   
               
        
        
    def searchIsChecked(self):
        self.checkNodeDict = {}
        topLayerCounts = self.treeWidget_filesList.topLevelItemCount()
       # print topLayerCounts
        for i in range( 0,topLayerCounts-1):
            for j in range(0,self.treeWidget_filesList.topLevelItem(i).childCount()):


                if self.treeWidget_filesList.topLevelItem(i).child(j).checkState(0) == QtCore.Qt.CheckState.Checked:

                    self.checkNodeDict.update({self.treeWidget_filesList.topLevelItem(i).child(j).text(0):{}})
    def searchPluginIsChecked(self):
        self.badPluginNodeList = {}
        topLayerCounts = self.treeWidget_filesList.topLevelItemCount()
       # print topLayerCounts

        for i in range(0,self.treeWidget_filesList.topLevelItem(9).childCount()):


            if self.treeWidget_filesList.topLevelItem(9).child(i).checkState(0) == QtCore.Qt.CheckState.Checked:

                    self.badPluginNodeList.update({self.treeWidget_filesList.topLevelItem(9).child(i).text(0):{}})
               # else:
                 #   pass
       # print self.checkNodeDict
            
       # self.delectChecked()
       # self.reflashTree()
    #def showProgressBar(self,processPresentValue):
       # self.progressBar.setValue(processPresentValue)
       
       
################publish Data announce#####################################      

    def key_pyblishFile(self,publishFileName,thumbnailPathToAnnoun,userName):
        #typical fileName = projInt_assetTypeInit_assetName_assetProcessInit_master.mb
        #example: ow_cf_c_angelFish_mod_master.mb
        
        self.typicalPublishDateDict ={'key_publishFile':{'projectWorkSpace':'workSpace',
                                                         'fileName':publishFileName,
                                                         'fileIcon':thumbnailPathToAnnoun,
                                                         'ribArchive':{'ribArchivePath':{'high':{},'mid':{},'low':{}},
                                                                       'parentGPUCache':{'high':{},'mid':{},'low':{}},
                                                                       'startFrame':{},
                                                                       'endFrame':{},
                                                                       'frameRate':{},
                                                                       'isMotionBlur':{}},                                                       
                                                         'gpuCache':'gpuCachePath',
                                                         'publishTime':'time',
                                                         'metaData':{},
                                                         'user':userName}}
        
    def addPublishFileAnnounceInfoToAssembleFile(self,assetOrShot,assetClass,assetNow,processNow):
        
        fileName =  self.root +'/' +self.project +'/' +'publish' +'/' +'global' +'/' +self.project + '_publishAnnonce.json'
        
        if os.path.isfile(fileName) == True:
            with open(fileName) as data_file:    
                data = json.load(data_file)
            #print data
            self.publishAnnounceDescriptionDict = data
        else:
            
            self.publishAnnounceDescriptionDict = self.projectAssembleDescription
        
        #print assetNow,

        tempName = assetNow +'.'+assetClass
       # print tempName
        #print self.projectAssembleDescription[assetOrShot][assetClass]#[tempName]
       # self.projectAssembleDescription['assets'][assetClass][tempName].update({processNow:{'state':{}}})
        #print self.projectAssembleDescription
        if self.radioButton_syncMode.isChecked()  == True:
            pass
        else:
        
            if assetOrShot == 'assets' :

                self.publishAnnounceDescriptionDict['assets'][assetClass][tempName].update({processNow:{'state':{}}})
                try:
                    self.publishAnnounceDescriptionDict['assets'][assetClass][tempName][processNow]['state'].update(self.typicalPublishDateDict['key_publishFile'])
                except:
                    pass
            else:

                self.publishAnnounceDescriptionDict['shot'][assetNow].update({processNow:{'state':{}}})
                try:
                    self.publishAnnounceDescriptionDict['shot'][assetNow][processNow]['state'].update(self.typicalPublishDateDict['key_publishFile'])
                except:
                    pass
                    
        #print self.projectAssembleDescription
        
        
        
        
    def storeProjectAssembleDescriptionFile(self):
        fileName =  self.root +'/' +self.project +'/' +'publish' +'/' +'global' +'/' +self.project + '_publishAnnonce.json'

        f = open(fileName,'w')
        
        data= json.dumps(self.publishAnnounceDescriptionDict, sort_keys=True , indent =4)
        #data = self.projectAssembleDescription
        #print data

        f.write(data)
        f.close
       
       
       
       
       
       
    def defineDictReadyToCopy(self):
        self.readyToCopyDict ={'udimTexture':{},
                      'pxrTexture':{},
                      'mayaTexture':{},
                      'gpuCache':{},
                      'ribArchive':{},
                      'alembic':{},
                      'pxrLight':{},
                      'mayaFluid':{},
                      'mayanParticle':{}}
        
        self.readyToAssigForNode= {}
        
        
       # print 'self.readyToAssigForNode',self.readyToAssigForNode 
            
        
        
    def storeDictReadyToCopy(self):
        fileName = self.root +'/' +self.project +'/' + 'publish' +'/'
               
        
    
    def copyAllFilesToNewLocation(self): #copy all select Files to New Location, pubish mode or sync mode
        print 'copyAllFilesToNewLocation start'
        self.reflashTree()
        self.defineDictReadyToCopy()
        
        
        

        if self.isAsset == True:

            copyDescProjectRoot = self.root +'/' +self.project +'/' + 'publish' +'/'+ 'assets'+'/'+ self.assetClass +'/' +self.assetNow +'/'+self.processNow
           

 
        else:

            copyDescProjectRoot = self.root +'/' +self.project +'/' + 'publish' +'/'+ 'shot'+'/'+ self.assetNow +'/'+self.processNow
 


        confirmAnswer= cmds.confirmDialog( title='Confirm Destination Folder', message='Destination Folder is %s ?'%copyDescProjectRoot, button=['Yes','No'], defaultButton='Yes', cancelButton='No', dismissString='No' )
        if confirmAnswer == "No":
            print 'change a new Destination Folder'
            copyDescProjectRoot= cmds.fileDialog2(fm=2)[0]
            self.checkFileSourceAndDest(copyDescProjectRoot)
      
        elif confirmAnswer == 'Yes':
            self.checkFileSourceAndDest(copyDescProjectRoot)
            
        dest = copyDescProjectRoot +'/' +'scenes' 
            
        self.publishMayaFile(dest)
            






    def copyAllFilesToNewLocationSync(self): #copy all select Files to New Location, pubish mode or sync mode
        print 'copyAllFilesToNewLocation start'
        self.reflashTree()
        self.defineDictReadyToCopy()
        

        if self.isAsset == True:               
            copyDescProjectRoot = self.root +'/' +self.project +'/'+ 'assets'+'/'+ self.assetClass +'/' +self.assetNow +'/'+self.processNow 


 
        else:
            copyDescProjectRoot = self.root +'/' +self.project +'/'+ 'shot'+'/'+ self.assetNow +'/'+self.processNow

        confirmAnswer= cmds.confirmDialog( title='Confirm Destination Folder', message='Destination Folder is %s ?'%copyDescProjectRoot, button=['Yes','No'], defaultButton='Yes', cancelButton='No', dismissString='No' )
        if confirmAnswer == "No":
            print 'change a new Destination Folder'
            copyDescProjectRoot= cmds.fileDialog2(fm=2)[0]
            self.checkFileSourceAndDest(copyDescProjectRoot)
      
        elif confirmAnswer == 'Yes':
            self.checkFileSourceAndDest(copyDescProjectRoot)
            
        dest = copyDescProjectRoot +'/' +'scenes' 
            
        self.publishMayaFile(dest)
            
            

            
            
        #mayaFileName = copyDescProjectRoot +'/' +'scenes' +'/' +
            
    def publishMayaFile(self,dest):
        nameExcept = ['v01','v02','v03','v04','v05','v06','v07','cf','web','pc','v001','v002','v003','v004','v005','v006','v007',]
        namePartVerCharControl = ['v0','v1','v2','v3','v4','v5','v6','v7','v8','v9']
        projectInitial = ""
        nameOtherParts = []
        newprojectInitial = ""
        for par in self.project.split('_'):
            if par in nameExcept:
                nameOtherParts.append(par)
                
            else:
                projectInitial = projectInitial + par[0]
                
        for i in nameOtherParts:
            newprojectInitial = newprojectInitial +'_'+ i
            
        
        projectInitial = projectInitial + newprojectInitial
        #print 'projectInitial',projectInitial
        if self.isAsset ==True:
           # exportMasterFileMB = dest +'/' +projectInitial+'_'+self.assetClass[0] +'_'+ self.processNow[0:3] +'_'+ self.assetName.split('/')[-1]+'_master.mb'

            exportMasterFileMB = dest +'/' +projectInitial+'_'+self.assetClass[0] +'_'+ self.processNow[0:3] +'_'+ self.assetNow+'_master.mb'
            exportMasterFileMA = dest +'/' +projectInitial+'_'+self.assetClass[0] +'_'+ self.processNow[0:3] +'_'+ self.assetNow+'_master.ma'
            
        else:
            exportMasterFileMB = dest +'/' +projectInitial+'_'+self.assetClass[0] +'_'+ self.processNow[0:3] +'_'+ self.assetNow+'_master.mb'
            exportMasterFileMA = dest +'/' +projectInitial+'_'+self.assetClass[0] +'_'+ self.processNow[0:3] +'_'+ self.assetNow+'_master.ma'


            
        
        cmds.file( rename=exportMasterFileMB )
        cmds.file( s=True, typ='mayaBinary')
        #cmds.file(exportMasterFileMA, s=True, typ='mayaAscii')
        cmds.file( rename=exportMasterFileMA )
        cmds.file( s=True, typ='mayaAscii')
        
        #self.checkIsAssetValue()
        #print self.isAsset
        
        
        if self.isAsset == True:
            assetOrShot = 'assets'
        else:
            assetOrShot = 'shot'
            
        assetClass = self.assetClass
        assetNow = self.assetNow
        processNow = self.processNow
        #print assetClass,assetNow,processNow
        thumbnailPathToAnnoun = dest +'/' +projectInitial+'_'+self.assetClass[0] +'_'+ self.processNow[0:3] +'_'+ self.assetNow+'_master.png'
        userName = getpass.getuser()
        self.key_pyblishFile(exportMasterFileMB,thumbnailPathToAnnoun,userName) #store all information to publish_key
        self.addPublishFileAnnounceInfoToAssembleFile(assetOrShot,assetClass,assetNow,processNow)
        self.storeProjectAssembleDescriptionFile()
        
        thumbnailFileName = dest +'/' +projectInitial+'_'+self.assetClass[0] +'_'+ self.processNow[0:3] +'_'+ self.assetNow+'_master'
        self.makeThumbnailTypical( thumbnailFileName,200,200,1)

        

    def checkFileSourceAndDest(self,copyDescProjectRoot):
        count = 0

        for i in self.allCopyFileInfoDict.keys():

            for j in range(0, len(self.allCopyFileInfoDict[i].keys())):
    

                count = count +1
                processPresentValue = int(float('%.2f'%(float(count)/ self.allCopyFileInfoDictItemsValue))*100)
             #   print 'processPresentValue',processPresentValue
                self.progressBar.setValue(processPresentValue)
                resetAttribute = self.allCopyFileInfoDict[i].keys()[j].split('*.*')[1] + self.allCopyFileInfoDict[i].keys()[j].split('*.*')[2]
                fileName = self.allCopyFileInfoDict[i].keys()[j].split('*.*')[0] 
          
                
               # print 'nodeName',self.allCopyFileInfoDict[i].keys()[j].split('*.*')[1]
               # print 'resetAttribute',resetAttribute
                if i == 'udimTexture':
                    tempResetAttribute  = self.allCopyFileInfoDict[i][self.allCopyFileInfoDict[i].keys()[j]].split('*.*')[0] + self.allCopyFileInfoDict[i].keys()[j].split('*.*')[2]
                    #print 'resetAttribute',resetAttribute
                    try:
                        resetAttribute = tempResetAttribute.replace('//sourceimages','/sourceimages')
                    except:
                        resetAttribute = tempResetAttribute
                                            
                    
                    fileName=self.allCopyFileInfoDict[i].keys()[j].split('*.*')[0] 
                    tempUUidAttr = self.allCopyFileInfoDict[i].keys()[j].split('*.*')[1].split('/')[-1]
                    tempAssignUUidAttr = copyDescProjectRoot +'/'+'sourceimages'+'/'+tempUUidAttr
                    try:
                        assignUUidAttr = tempAssignUUidAttr.replace('//sourceimages','/sourceimages')
                    except:
                        assignUUidAttr = tempAssignUUidAttr
                                            
                    
                   # print 'assignUuidNodeName',resetAttribute
                   # print 'assignUUidAttr',assignUUidAttr
                    tempfileSource = fileName
                    try:
                        fileSource = tempfileSource.replace('//sourceimages','/sourceimages')
                    except:
                        fileSource = tempfileSource
                        
                    tempfileDesc = copyDescProjectRoot +'/' + 'sourceimages' +'/' +fileName.split('/')[-1]
                    try:
                        fileDesc = tempfileDesc.replace('//sourceimages','/sourceimages')
                    except:
                        fileDesc = tempfileDesc
                    #print 'fileSource,fileDesc',fileSource,fileDesc
                        
                    self.readyToCopyDict['udimTexture'].update({fileSource:fileDesc})
                    self.readyToAssigForNode.update({resetAttribute:assignUUidAttr})

                    
                if i == 'pxrTexture':
                    
                    
                    fileSource = fileName
                    
                    
                    fileDesc = copyDescProjectRoot +'/' + 'sourceimages' +'/' +fileName.split('/')[-1]
                    #print 'fileSource,fileDesc',fileSource,fileDesc
                   # print 'resetAttribute',resetAttribute
                    self.readyToCopyDict['pxrTexture'].update({fileSource:fileDesc})
                    #check node is pxrMultiTexture

                    if len(self.allCopyFileInfoDict[i][self.allCopyFileInfoDict[i].keys()[j]].split('*.*')[0].split('_._')) > 1:
                        
                        resetAttribute = self.allCopyFileInfoDict[i][self.allCopyFileInfoDict[i].keys()[j]].split('*.*')[0].split('_._')[0] + self.allCopyFileInfoDict[i].keys()[j].split('*.*')[2] + str(self.allCopyFileInfoDict[i][self.allCopyFileInfoDict[i].keys()[j]].split('*.*')[0].split('_._')[1])
                        
       #                 print 'resetAttribute',resetAttribute
                    else:
                        pass
                       # print 'resetAttribute',resetAttribute
                    
                    self.readyToAssigForNode.update({resetAttribute:fileDesc})
                if i == 'mayaTexture':
                    fileSource = fileName
                    fileDesc = copyDescProjectRoot +'/' + 'sourceimages' +'/' +fileName.split('/')[-1]
                   # print 'fileSource,fileDesc',fileSource,fileDesc
                    self.readyToCopyDict['mayaTexture'].update({fileSource:fileDesc})
                    txFileSource = fileSource.split('.')[0]+'.tx'
                    tfFileDesc = fileDesc.split('.')[0]+'.tx'
                    self.readyToCopyDict['mayaTexture'].update({txFileSource:tfFileDesc})
                    #print 'txFileSource ,tfFileDesc',txFileSource,tfFileDesc

                    self.readyToAssigForNode.update({resetAttribute:fileDesc})


                if i == 'gpuCache':
                    fileSource = fileName
                    createRibArchiveFolder = copyDescProjectRoot +'/' + 'renderman/ribarchives' +'/'+ fileName.split('/')[-1].split('.')[0]
                    #print createRibArchiveFolder
                    self.createNewFolder(createRibArchiveFolder)
  
                    fileDesc = createRibArchiveFolder +'/' +fileName.split('/')[-1]
                    #print 'fileSource,fileDesc',fileSource,fileDesc
                    self.readyToCopyDict['gpuCache'].update({fileSource:fileDesc})
                    self.readyToAssigForNode.update({resetAttribute:fileDesc})

                                       
                if i == 'ribArchive':
                    fileSource = fileName
                    createRibArchiveFolder = copyDescProjectRoot +'/' + 'renderman/ribarchives' +'/'+ fileName.split('/')[-1].split('.')[0]
                    self.createNewFolder(createRibArchiveFolder)


                        
                    fileDesc = createRibArchiveFolder +'/' +fileName.split('/')[-1]
                   # print 'fileSource,fileDesc',fileSource,fileDesc
                    self.readyToCopyDict['ribArchive'].update({fileSource:fileDesc})
                    self.readyToAssigForNode.update({resetAttribute:fileDesc})

                if i == 'alembic':
                    fileSource = fileName
                    fileDesc = copyDescProjectRoot +'/' + 'data/alembic' +'/' +fileName.split('/')[-1]
                    #print 'fileSource,fileDesc',fileSource,fileDesc
                    self.readyToCopyDict['alembic'].update({fileSource:fileDesc})
                    self.readyToAssigForNode.update({resetAttribute:fileDesc})
                                                                   
                if i == 'pxrLight':
                    fileSource = fileName
                    fileDesc = copyDescProjectRoot +'/' + 'sourceimages' +'/' +fileName.split('/')[-1]
                    #print 'fileSource,fileDesc',fileSource,fileDesc
                    self.readyToCopyDict['pxrLight'].update({fileSource:fileDesc})
                    self.readyToAssigForNode.update({resetAttribute:fileDesc})
                                                              
                if i == 'mayaFluid':
                    fileSource = fileName
                    fileDesc = copyDescProjectRoot +'/' + 'data/mayaFluidCache' +'/' +fileName.split('/')[-1]
                    #print 'fileSource,fileDesc',fileSource,fileDesc
                    self.readyToCopyDict['mayaFluid'].update({fileSource:fileDesc})
                    self.readyToAssigForNode.update({resetAttribute:fileDesc})
                                                           
                if i == 'mayanParticle':
                    fileSource = fileName
                    fileDesc = copyDescProjectRoot +'/' + 'data/nParticleCache' +'/' +fileName.split('/')[-1]
                    self.readyToCopyDict['mayanParticle'].update({fileSource:fileDesc})
                    self.readyToAssigForNode.update({resetAttribute:fileDesc})


        #print self.readyToCopyDict
        #print 'self.readyToCopyDict',self.readyToCopyDict
        #print 'self.readyToAssigForNode',self.readyToAssigForNode

                
                
        confirmAnswer= cmds.confirmDialog( title='Confirm Copy And Reset Attribute To New Location', message='Ready To Copy', button=['Yes','No'], defaultButton='Yes', cancelButton='No', dismissString='No' )
        #print 'answer',confirmAnswer
        
        if confirmAnswer == "No":
            pass

            
            
        elif confirmAnswer == 'Yes':

            
            print ' Copy And Reset Attribute To New Location'
            count = 0
            for i in self.readyToCopyDict.keys():
               # print self.readyToCopyDict[i]
                for j in range(0,len( self.readyToCopyDict[i])):
                    source = self.readyToCopyDict[i].keys()[j]
                    dect = self.readyToCopyDict[i][self.readyToCopyDict[i].keys()[j]]
                   # print source, dect
                    self.copyFile(source,dect)
                   # print self.allCopyFileInfoDictItemsValue
                   # print count
                    count = count +1
                    processPresentValue = int(float('%.2f'%(float(count)/ self.allCopyFileInfoDictItemsValue))*100)
                   # print 'processPresentValue',processPresentValue
                    self.progressBar.setValue(processPresentValue)            
                
            self.progressBar.setValue(100) 
                    
            for i in self.readyToAssigForNode.keys():
                nodeAttr = i
                newAttr = self.readyToAssigForNode[i]
                #print nodeAttr,newAttr
                self.assignNewAttr(nodeAttr,newAttr)
         #       print i




    def copyFile(self,source,dect):
        try:
            copyfile(source, dect)
        except:
            pass

    def assignNewAttr(self,nodeAttr,newAttr):
        pm.setAttr(nodeAttr,newAttr)

                                               
    def createCopyFileInfoDictInit(self):
        print 'createCopyFileInfoDictInit start'
        
        self.allCopyFileInfoDict = {'udimTexture':{},
                                    'pxrTexture':{},
                                         'mayaTexture':{},
                                         'gpuCache':{},
                                         'ribArchive':{},
                                         'alembic':{},
                                         'pxrLight':{},
                                         'mayaFluid':{},
                                         'mayanParticle':{}
                                         }
        
        
    def createCopyFileInfoDictUpdate(self,checkMode,nodeName,linkingFile,attrKey):
        #print 'createCopyFileInfoDictUpdate start'
        mariUdimFormat = ['1021','1022','1023','1024','1025','1026','1027','1028',
                          '1029','1030','1011','1012','1013','1014','1015','1016',
                          '1017','1018','1019','1020','1001','1002','1003','1004',
                          '1005','1006','1007','1008','1009','1010',
                          'u0_v0','u1_v0','u2_v0','u3_v0','u4_v0','u5_v0','u6_v0',
                          'u0_v1','u1_v0','u2_v0','u3_v0','u4_v0','u5_v0','u6_v0',
                          'u0_v2','u1_v0','u2_v0','u3_v0','u4_v0','u5_v0','u6_v0',
                          'u0_v3','u1_v0','u2_v0','u3_v0','u4_v0','u5_v0','u6_v0',
                          'u0_v4','u1_v0','u2_v0','u3_v0','u4_v0','u5_v0','u6_v0',
                          'u0_v5','u1_v0','u2_v0','u3_v0','u4_v0','u5_v0','u6_v0',
                          'u0_v6','u1_v0','u2_v0','u3_v0','u4_v0','u5_v0','u6_v0']

       # print checkMode, nodeName,linkingFile

        if checkMode == 'pxrTexture':
            if linkingFile.split('.tex')[0][-8:] == '__MAPID_' :
                
                for i in mariUdimFormat:

                    
                    udimFileName = linkingFile.split('.tex')[0][0:-8] +'_'+i+'.tex'
                    if os.path.isfile(udimFileName) == True :
                        #self.udimFileNameListudimFileNameList.append(udimFileName)
                        #print 'udimFileName ',udimFileName
                        nodeNameExt = nodeName + '*.*'+ linkingFile.split('//')[0]+linkingFile.split('//')[1]
                        fileNameExt = udimFileName + '*.*'+ linkingFile +'*.*'+attrKey
                        self.allCopyFileInfoDict['udimTexture'].update({fileNameExt:nodeNameExt})
                        self.allCopyFileInfoDictItemsValue = self.allCopyFileInfoDictItemsValue +1
           #             print 'nodeNameExt',nodeNameExt
           #             print 'fileNameExt',fileNameExt
                    else:
                        pass
                #self.allCopyFileInfoDict['pxrTexture'].update({nodeName:{self.udimFileNameListudimFileNameList}})    
                        
            else:
                nodeNameExt = nodeName + '*.*'+ 'none'
                fileNameExt = linkingFile + '*.*'+ nodeName  +'*.*'+attrKey
                self.allCopyFileInfoDict['pxrTexture'].update({fileNameExt:nodeNameExt})
                self.allCopyFileInfoDictItemsValue = self.allCopyFileInfoDictItemsValue +1

        elif checkMode == 'mayaTexture':
          #  print 'nodeName,linkingFile',nodeName,linkingFile
            nodeNameExt = nodeName + '*.*'+ 'none'
            fileNameExt = linkingFile + '*.*'+ nodeName  +'*.*'+attrKey
        

            self.allCopyFileInfoDict['mayaTexture'].update({fileNameExt:nodeNameExt})
            self.allCopyFileInfoDictItemsValue = self.allCopyFileInfoDictItemsValue +1
 
        elif checkMode == 'gpuCache':
            nodeNameExt = nodeName + '*.*'+ 'none'
            fileNameExt = linkingFile + '*.*'+ nodeName +'*.*'+attrKey
            self.allCopyFileInfoDict['gpuCache'].update({fileNameExt:nodeNameExt})
            self.allCopyFileInfoDictItemsValue = self.allCopyFileInfoDictItemsValue +1
            
        elif checkMode == 'ribArchive':
            nodeNameExt = nodeName + '*.*'+ 'none'
            fileNameExt = linkingFile + '*.*'+ nodeName +'*.*'+attrKey
        #    print 'fileNameExt',fileNameExt
            self.allCopyFileInfoDict['ribArchive'].update({fileNameExt:nodeNameExt})
            self.allCopyFileInfoDictItemsValue = self.allCopyFileInfoDictItemsValue +1
                  
            
        elif checkMode == 'alembic':
            nodeNameExt = nodeName + '*.*'+ 'none'
            fileNameExt = linkingFile + '*.*'+ nodeName +'*.*'+attrKey
            self.allCopyFileInfoDict['alembic'].update({fileNameExt:nodeNameExt})
            self.allCopyFileInfoDictItemsValue = self.allCopyFileInfoDictItemsValue +1
          
            
        elif checkMode == 'pxrLight':
            nodeNameExt = nodeName + '*.*'+ 'none'
            fileNameExt = linkingFile + '*.*'+ nodeName +'*.*'+attrKey
            self.allCopyFileInfoDict['pxrLight'].update({fileNameExt:nodeNameExt})
            self.allCopyFileInfoDictItemsValue = self.allCopyFileInfoDictItemsValue +1

            
        elif checkMode == 'mayaFluid':
            nodeNameExt = nodeName + '*.*'+ 'none'
            fileNameExt = linkingFile + '*.*'+ nodeName +'*.*'+attrKey
            self.allCopyFileInfoDict['mayaFluid'].update({fileNameExt:nodeNameExt})
            self.allCopyFileInfoDictItemsValue = self.allCopyFileInfoDictItemsValue +1
                      
            
        elif checkMode == 'mayanParticle':
            nodeNameExt = nodeName + '*.*'+ 'none'
            fileNameExt = linkingFile + '*.*'+ nodeName +'*.*'+attrKey
            self.allCopyFileInfoDict['mayanParticle'].update({fileNameExt:nodeNameExt})
            self.allCopyFileInfoDictItemsValue = self.allCopyFileInfoDictItemsValue +1
            
        
       # print 'self.udimFileNameList',self.udimFileNameList
      #  print 'self.allCopyFileInfoDict',self.allCopyFileInfoDict
          # print linkingFile.split('/')[-1]
    def checkFileSize(self,fileName):
        
        fileSizeBt = os.stat(fileName).st_size /1024
        if fileSizeBt < 1024:
            fileSize = str(fileSizeBt) +'KB'
        elif fileSizeBt <1024*1024:
            fileSize = '%.3f'%(fileSizeBt/1024.0) +'MB'
            
        else:
            
            fileSize='%.3f'%(fileSizeBt/1024.0/1024.0) +'GB'

        '''
            
        
       # image = ice.Load(linkingFile)
        if checkMode == 'pxrTexture' :
            imageMetaData = image.GetMetaData()
            originalSize = imageMetaData['Original Size']
            originalFileFormat = imageMetaData['Original File Format']
            originalBitsPerSample = imageMetaData['Original Bits Per Sample']
            self.allCopyFileInfoDict['pxrTexture'].update({nodeName:{}})
           # fileSize = imageMetaData['File Size']
            #fileInfo = [{'linkingFile':linkingFile},{'fileState':self.fileState},{'Original Size':originalSize},{'Original File Format':originalFileFormat},{'Original Bits Per Sample':originalBitsPerSample},{'File Size':fileSize},{'checkState':self.checkState},{'duplicateShapeNameState': self.duplicateShapeNameState}]
            #self.allCopyFileInfoDict[checkMode].update({nodeName:fileInfo})
        
        if checkMode == 'mayaTexture':
            self.allCopyFileInfoDict[checkMode].update({nodeName:[{'linkingFile':udimFileNameList},{'fileState':self.fileState},{'Original Size':originalSize},{'Original File Format':originalFileFormat},{'Original Bits Per Sample':originalBitsPerSample},{'File Size':fileSize},{'checkState':self.checkState},{'duplicateShapeNameState': self.duplicateShapeNameState}]})
        else: 
            self.allCopyFileInfoDict[checkMode].update({nodeName:[{'linkingFile':udimFileNameList},{'fileState':self.fileState},{'Original Size':'none'},{'Original File Format':'none'},{'Original Bits Per Sample':'none'},{'File Size':fileSize},{'checkState':self.checkState},{'duplicateShapeNameState': self.duplicateShapeNameState}]})
    
        print 'self.allCopyFileInfoDict',self.allCopyFileInfoDict
        '''
            
            
    def createNewItem(self,checkItemTopLayerIndex,index,nodeName,linkingFile,fontColor,attrKey):
        #fontColor = self.fontColor
        #print index,nodeName,linkingFile,self.fontColor
        if len(linkingFile) > 0:
            pass
        else:
            linkingFile = 'None'
       # print 'topLayerIndex',topLayerIndex
       # print 'index',index
       # print 'nodeName',nodeName
       # print 'linkingFile',linkingFile
       # print 'self.fontColor',self.fontColor
        if len(nodeName.split('|')) > 1:
            showName = nodeName.split('|')[-1]
        else:
            showName =nodeName
        

        textColor = (int(self.fontColor[0]), int(self.fontColor[1]), int(self.fontColor[2]))
        #        QtWidgets.QTreeWidgetItem(self.treeWidget).setForeground(0,self.brushLevelOne)  #create contain master ,and define font color
      #  QtWidgets.QTreeWidgetItem(self.treeWidget).setForeground(0,QtGui.QBrush(QtGui.QColor(247, 126, 128)))  #create contain master ,and define font color
        
       # #1.default exist , master should exist in top of treeWidget
       # self.treeWidget.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "master", None, -1))
      #  self.treeWidget.topLevelItem(0)#.setFont(0,self.fontLevelOne)#define font size
      
        QtWidgets.QTreeWidgetItem(self.treeWidget_filesList.topLevelItem(checkItemTopLayerIndex))#.setForeground(0,self.brushLevelThree)  #build new item from index
        
        self.treeWidget_filesList.topLevelItem(checkItemTopLayerIndex).child(index).setForeground(0,QtGui.QBrush(QtGui.QColor(int(self.fontColor[0]), int(self.fontColor[1]), int(self.fontColor[2]))))#.setFont(0,self.fontLevelThree)
        self.treeWidget_filesList.topLevelItem(checkItemTopLayerIndex).child(index).setText(0, QtWidgets.QApplication.translate("MainWindow", 'tempName', None, -1))
        self.treeWidget_filesList.topLevelItem(checkItemTopLayerIndex).child(index).setText(0,showName)
        self.treeWidget_filesList.topLevelItem(checkItemTopLayerIndex).child(index).setText(6,nodeName)
        
        if self.checkState == 'Unchecked':
            self.treeWidget_filesList.topLevelItem(checkItemTopLayerIndex).child(index).setCheckState(0, QtCore.Qt.Unchecked)
        else:
            self.treeWidget_filesList.topLevelItem(checkItemTopLayerIndex).child(index).setCheckState(0, QtCore.Qt.Checked)
            
        self.treeWidget_filesList.topLevelItem(checkItemTopLayerIndex).child(index).setForeground(1,QtGui.QBrush(QtGui.QColor(int(self.fontColor[0]), int(self.fontColor[1]), int(self.fontColor[2]))))#.setFont(0,self.fontLevelThree)

       
        self.treeWidget_filesList.topLevelItem(checkItemTopLayerIndex).child(index).setText(1,linkingFile.split('/')[-1])  #add shot Name into treeWidget in column 2
        self.treeWidget_filesList.topLevelItem(checkItemTopLayerIndex).child(index).setText(2,linkingFile) #add fullName into treeWidget in column 3
        self.treeWidget_filesList.topLevelItem(checkItemTopLayerIndex).child(index).setText(3,attrKey) #add nodePath into treeWidget in column 3
        self.treeWidget_filesList.topLevelItem(checkItemTopLayerIndex).child(index).setText(4,str(checkItemTopLayerIndex))
        self.treeWidget_filesList.topLevelItem(checkItemTopLayerIndex).child(index).setText(5,str(index))
  
  
  #topLayerIndex
    def checkDuplicateName(self,checkMode,shapeName,checkItemTopLayerIndex,index):  # call from self.findRibArchives()
        #print 'checkDuplicateName start'
        #print shapeName, len(shapeName.split('|'))
        if len(shapeName.split('|')) >= 4: 
            self.shapeCheckDict.update({shapeName.split('|')[-3]:{shapeName.split('|')[-2]:{shapeName.split('|')[-1]:{}}}})
        elif len(shapeName.split('|')) == 3 : 
            
            self.shapeCheckDict.update({shapeName.split('|')[-3]:{shapeName.split('|')[-2]:{shapeName.split('|')[-1]:{}}}})
            
        elif len(shapeName.split('|')) == 2 : 
            
            self.shapeCheckDict.update({'none':{shapeName.split('|')[-2]:{shapeName.split('|')[-1]:{}}}})
            
        elif len(shapeName.split('|')) == 1 : 
            
            self.shapeCheckDict.update({'none':{'none':{shapeName.split('|')[-1]:{}}}})
        else:
            pass
        if shapeName.split('|')[-1] in self.shapeLastParName:
           # print "got duplicate shpae Name"
            self.duplicateItemCount = self.duplicateItemCount +1
            self.fontColor =(180,180,255)
           # print 'shapeName ',shapeName
            #self.allDuplicateShapeNameDict.update({'ribArchive':{shapeName:{'itemLevelIndex':[checkItemTopLayerIndex,index]}}})
            self.allDuplicateShapeNameDict[checkMode].update({shapeName:{'itemLevelIndex':[checkItemTopLayerIndex,index,'duplicateName']}})
            self.duplicateShapeNameState = 'True'
        
        else:
            self.shapeLastParName.append(shapeName.split('|')[-1])
            self.allDuplicateShapeNameDict[checkMode].update({shapeName:{'itemLevelIndex':[checkItemTopLayerIndex,index,'noneDuplicateName']}})
            self.duplicateShapeNameState = 'False'
        
        #print shapeName
        

    def checkFileExist(self,linkingFile,checkMode):  #checkMode = pxrTexture,mayaTexture,gpuCache,ribArchive,alembic,pxrLight,mayaFluid,mayanParticle
       # print 'check file is existed'
        #print 'linkingFile,checkMode', linkingFile,checkMode
        #print os.path.isfile(linkingFile)
        if os.path.isfile(linkingFile) == True:
            #print os.path.isfile(linkingFile)
            if checkMode == 'pxrTexture':
              #  print 'check the file is pxr texture'
                if linkingFile.split('.')[-1] == 'tex':
                    self.fontColor = (0,255,0)
     
                else:
                    self.fontColor =(255,255,0)
                    self.yellowCount = self.yellowCount +1

                self.checkState = 'Unchecked'


                    
            elif checkMode == 'mayaTexture':
              #  print 'check the file is surport maya image format'
                if linkingFile.split('.')[-1] in ['jpg','tif','png','exr','tga','iff','bmp','psd','dds','hdr']:
                    self.fontColor = (0,255,0)
                else:
                    self.fontColor =(255,255,0)
                    self.yellowCount = self.yellowCount +1
                self.checkState = 'Unchecked'


                    
            elif checkMode == 'gpuCache':
               # print 'check the file is surport gpuCache format'
                if linkingFile.split('.')[-1] in ['abc']:
                    self.fontColor = (0,255,0)
                else:
                    self.fontColor =(255,255,0)
                    self.yellowCount = self.yellowCount +1
                self.checkState = 'Unchecked'


                                 
            elif checkMode == 'ribArchive':
               # print 'check the file is surport ribArchive format'
                if linkingFile.split('.')[-1] in ['rib','zip','zip','7z','gz']:
                    self.fontColor = (0,255,0)
                 #   print "aaaaaaaaaaa"
                else:
                    self.fontColor =(255,255,0)
                    self.yellowCount = self.yellowCount +1      
                  #  print "bbbbbbbbbb"
                self.checkState = 'Unchecked'


                                 
            elif checkMode == 'alembic':
            #    print 'check the file is surport alembic format'
                if linkingFile.split('.')[-1] in ['abc']:
                    self.fontColor = (0,255,0)
                else:
                    self.fontColor =(255,255,0)
                    self.yellowCount = self.yellowCount +1
                self.checkState = 'Unchecked'


                                 
            elif checkMode == 'pxrLight':
              #  print 'check the file is surport pxrLight format'
                if linkingFile.split('.')[-1] in ['tex','exr','tex']:
                    self.fontColor = (0,255,0)
                else:
                    self.fontColor =(255,255,0)
                    self.yellowCount = self.yellowCount +1
                self.checkState = 'Unchecked'
                                 
                                                                                                                                      
            elif checkMode == 'mayaFluid':
             #   print 'check the file is surport mayaFluid format'
                if linkingFile.split('.')[-1] in ['xml']:
                    self.fontColor = (0,255,0)
                else:
                    self.fontColor =(255,255,0)
                    self.yellowCount = self.yellowCount +1
                                                     
                self.checkState = 'Unchecked'
                    
                                                                                                                                      
            elif checkMode == 'mayanParticle':
            #    print 'check the file is surport mayanParticle format'
                if linkingFile.split('.')[-1] in ['xml']:
                    self.fontColor = (0,255,0)
                else:
                    self.fontColor =(255,255,0)
                    self.yellowCount = self.yellowCount +1
                                                     
                                        
                self.checkState = 'Unchecked'

                    
             
            else:
                self.checkState = 'Unchecked'

               # pass
                

            self.fileState= 'Exist'
        else:
            if checkMode == 'pxrLight':
                self.checkState = 'Unchecked'

            else:
                self.fontColor =(255,0,0)
                self.setCheck = 1
                self.redCount = self.redCount +1
                self.checkState = 'Checked'
            self.fileState= 'False'

          #  print "cccccccc"

            
        '''
        if redCount > 0:

            self.topLayerColor = (255,0,0)
        
        else:
            
            if yellowCount >0 :
                self.topLayerColor = (255,255,0)
                
            else:
                self.topLayerColor = (255,255,255)
                
        '''


            
            

                
            

            
            
        #self.fontColor = fontColor
        


        
    def defineFontB(self):
                
        fontSizeAdj = 8
        self.fontLevelOne = QtGui.QFont()
        self.fontLevelOne.setPointSize((fontSizeAdj+2))
        self.fontLevelOne.setWeight(75)
        self.fontLevelOne.setBold(True)
        self.fontLevelOne.setUnderline(True)


        self.brushLevelOne = QtGui.QBrush(QtGui.QColor(247, 126, 128))
        self.brushLevelOne.setStyle(QtCore.Qt.NoBrush)
        

        self.fontLevelTwo = QtGui.QFont()
        self.fontLevelTwo.setPointSize(fontSizeAdj+2)
        self.fontLevelTwo.setWeight(75)
        self.fontLevelTwo.setBold(0)
        #self.fontLevelTwo.setItalic(True)
        
        self.brushLevelTwo = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        self.brushLevelTwo.setStyle(QtCore.Qt.NoBrush)

        self.fontLevelThree = QtGui.QFont()
        self.fontLevelThree.setPointSize(fontSizeAdj+1)
        self.fontLevelThree.setWeight(75)
        self.fontLevelThree.setBold(True)

        self.fontLevelThree.setItalic(True)
        self.brushLevelThree = QtGui.QBrush(QtGui.QColor(100, 200, 100))
        self.brushLevelThree.setStyle(QtCore.Qt.NoBrush)
       # item_0.setForeground(0, brush)

        self.fontLevelFour = QtGui.QFont()
        self.fontLevelFour.setPointSize(fontSizeAdj+1)
        self.fontLevelFour.setWeight(75)
        self.fontLevelFour.setBold(0)

        self.fontLevelFour.setItalic(True)
        self.brushLevelFour = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        self.brushLevelFour.setStyle(QtCore.Qt.NoBrush)

    
            
    def buildItemTree(self):
        
        self.treeWidget_filesList.clear()
    
    
    
    
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_filesList)   #0  Prman Texture
        item_0.setCheckState(0, QtCore.Qt.Checked)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_filesList)  #1  Maya Texture
        item_0.setCheckState(0, QtCore.Qt.Checked)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_filesList)   #2 GpuCache
        item_0.setCheckState(0, QtCore.Qt.Checked)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_filesList)  #3 RibArchive
        item_0.setCheckState(0, QtCore.Qt.Checked)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_filesList)   #4 Alembic
        item_0.setCheckState(0, QtCore.Qt.Checked)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_filesList)  #5 camera
        item_0.setCheckState(0, QtCore.Qt.Unchecked)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_filesList)  #6 prman light
        item_0.setCheckState(0, QtCore.Qt.Unchecked)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_filesList)  #7 fluid cache
        item_0.setCheckState(0, QtCore.Qt.Unchecked)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_filesList)  #8 nParticle Cache
        item_0.setCheckState(0, QtCore.Qt.Unchecked)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_filesList)  #9 plugin
        item_0.setCheckState(0, QtCore.Qt.Checked)

        self.checkFiletOptionCheckState()
        
        
        
        

        self.itemName_prmanTextures = "PrmanTextures"+'__('+'%03d'%self.countN1+')'  #0
        self.itemName_mayaTextures = "mayaTextures"+'__('+'%03d'%self.countN2+')'    #1
        self.itemName_gpuCaches = "gpuCaches"+'__('+'%03d'%self.countN3+')'          #2
        self.itemName_RibArchives = "RibArchives"+'__('+'%03d'%self.countN4+')'      #3
        self.itemName_alembics = "alembics"+'__('+'%03d'%self.countN5+')'            #4
        self.itemName_cameras = "cameras"+'__('+'%03d'%self.countN6+')'              #5   
        self.itemName_PrmanLights = "PrmanLights"+'__('+'%03d'%self.countN7+')'      #6
        #self.itemName_mayaLights = "mayaLights"+'__('+'%03d'%countN8+')'            #7
        self.itemName_fluidCaches = "fluidCaches"+'__('+'%03d'%self.countN9+')'      #8
        self.itemName_nParticleCaches = "particleCaches"+'__('+'%03d'%self.countN10+')'  #9
        self.itemName_plugin = "plungin"+'__('+'%03d'%self.countN11+')'   #10
        

        

        
        self.treeWidget_filesList.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_prmanTextures, None, -1))
        self.treeWidget_filesList.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_mayaTextures, None, -1))
        self.treeWidget_filesList.topLevelItem(2).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_gpuCaches, None, -1))
        self.treeWidget_filesList.topLevelItem(3).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_RibArchives, None, -1))
        self.treeWidget_filesList.topLevelItem(4).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_alembics, None, -1))
        self.treeWidget_filesList.topLevelItem(5).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_cameras, None, -1))
        self.treeWidget_filesList.topLevelItem(6).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_PrmanLights, None, -1))
        self.treeWidget_filesList.topLevelItem(7).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_fluidCaches, None, -1))
        self.treeWidget_filesList.topLevelItem(8).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_nParticleCaches, None, -1))
        self.treeWidget_filesList.topLevelItem(9).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_plugin, None, -1))



    def checkFiletOptionCheckState(self):
        if  self.treeWidget_FiletOption.topLevelItem(0).child(0).checkState(0) == QtCore.Qt.CheckState.Checked:  #check  Prman Texture
            self.treeWidget_filesList.topLevelItem(0).setCheckState(0, QtCore.Qt.Checked)
        else:
            self.treeWidget_filesList.topLevelItem(0).setCheckState(0, QtCore.Qt.Unchecked)
            
        if  self.treeWidget_FiletOption.topLevelItem(0).child(1).checkState(0) == QtCore.Qt.CheckState.Checked: #check  Maya Texture
            self.treeWidget_filesList.topLevelItem(1).setCheckState(0, QtCore.Qt.Checked)
        else:
            self.treeWidget_filesList.topLevelItem(1).setCheckState(0, QtCore.Qt.Unchecked)
            
        if  self.treeWidget_FiletOption.topLevelItem(0).child(2).checkState(0) == QtCore.Qt.CheckState.Checked: #check  GpuCache
            self.treeWidget_filesList.topLevelItem(2).setCheckState(0, QtCore.Qt.Checked)
        else:
            self.treeWidget_filesList.topLevelItem(2).setCheckState(0, QtCore.Qt.Unchecked)
            
        if  self.treeWidget_FiletOption.topLevelItem(0).child(3).checkState(0) == QtCore.Qt.CheckState.Checked: #check  RibArchive
            self.treeWidget_filesList.topLevelItem(3).setCheckState(0, QtCore.Qt.Checked)
        else:
            self.treeWidget_filesList.topLevelItem(3).setCheckState(0, QtCore.Qt.Unchecked)
            
        if  self.treeWidget_FiletOption.topLevelItem(0).child(4).checkState(0) == QtCore.Qt.CheckState.Checked: #check  Alembic
            self.treeWidget_filesList.topLevelItem(4).setCheckState(0, QtCore.Qt.Checked)
        else:
            self.treeWidget_filesList.topLevelItem(4).setCheckState(0, QtCore.Qt.Unchecked)
            
        if  self.treeWidget_FiletOption.topLevelItem(0).child(5).checkState(0) == QtCore.Qt.CheckState.Checked: #check  Prman Light
            self.treeWidget_filesList.topLevelItem(6).setCheckState(0, QtCore.Qt.Checked)
        else:
            self.treeWidget_filesList.topLevelItem(6).setCheckState(0, QtCore.Qt.Unchecked)
            
        if  self.treeWidget_FiletOption.topLevelItem(0).child(6).checkState(0) == QtCore.Qt.CheckState.Checked: #check  Maya Fluid
            self.treeWidget_filesList.topLevelItem(7).setCheckState(0, QtCore.Qt.Checked)
        else:
            self.treeWidget_filesList.topLevelItem(7).setCheckState(0, QtCore.Qt.Unchecked)
            
        if  self.treeWidget_FiletOption.topLevelItem(0).child(7).checkState(0) == QtCore.Qt.CheckState.Checked: #check  Maya nParticle Cache
            self.treeWidget_filesList.topLevelItem(8).setCheckState(0, QtCore.Qt.Checked)
        else:
            self.treeWidget_filesList.topLevelItem(8).setCheckState(0, QtCore.Qt.Unchecked)
            
        if  self.treeWidget_FiletOption.topLevelItem(1).child(0).checkState(0) == QtCore.Qt.CheckState.Checked: #check  Maya nParticle Cache
            self.treeWidget_filesList.topLevelItem(9).setCheckState(0, QtCore.Qt.Checked)
        else:
            self.treeWidget_filesList.topLevelItem(9).setCheckState(0, QtCore.Qt.Unchecked)
                                                                                             
                                                                                                


        
    def findCameras(self): # store cameras NodeName and location 
        
        exceptCameraList = [ 'topShape', 'perspShape', 'frontShape', 'sideShape']
        cameraNodes = cmds.ls( typ ='camera')
        realCameraList = []
        for i in cameraNodes:
            if i in exceptCameraList:
                pass
            else:
                realCameraList.append(i)
                
        camerasInfo = {}
        for i in realCameraList:

            fov = cmds.getAttr('%s.focalLength'%i)
            nearClip = cmds.getAttr('%s.nearClipPlane'%i)
            farClip = cmds.getAttr('%s.farClipPlane'%i)
            
            camerasInfo.update({i:{'fov':fov,'nearClip':nearClip,'farClip':farClip}})
            #camerasInfo.update({i+'nearClip':nearClip})
            #camerasInfo.update({i+'farClip':farClip})

            
        self.countN6 = len(realCameraList)
            
       # print camerasInfo
      #  print self.countN6

    def runProgressBar(self,totalCount,count):
        
        count = count +1
        processPresentValue = int(float('%.2f'%(float(count)/ self.allCopyFileInfoDictItemsValue))*100)
        self.progressBar.setValue(processPresentValue)


    
        
            
    def findPrmanTexture(self):  # store PrmanTextures NodeName and location 
        print 'findPrmanTexture start'
        self.plainTextEdit.setPlainText('finding PxrTexture')
        '''
        pxrNodes = cmds.ls( typ ='PxrTexture')
        pxrTexturePath = {}
        for i in pxrNodes:
            path = cmds.getAttr('%s.filename'%i)
            pxrTexturePath.update({i:{'linkingFile':path}})
            self.linkingFilePreMoveDict.update({'pxrTexture':{i:{path:{}}}})
        self.countN1 = len(pxrNodes)
        '''
        
        pxrTextureNodeTypeList = ['PxrTexture','PxrNormalMap','PxrBump','PxrMultiTexture']
        pxrMultiTexturePathList = ['filename0','filename1','filename2','filename3','filename4','filename5','filename6','filename7','filename8','filename9',]
        pxrTexturePath = {}
        pxrNodes = []
        for i in pxrTextureNodeTypeList:
            for j in cmds.ls(typ =i):
                pxrNodes.append(j+'_._'+i)

        for i in pxrNodes:
    #        print i
            if i.split('_._')[1] == 'PxrMultiTexture':
                for j,k in zip(pxrMultiTexturePathList,range(0,10)):
                    #print i.split('_._')[0], cmds.getAttr(i.split('_._')[0]+'.'+j)
                    path = cmds.getAttr(i.split('_._')[0]+'.'+j)
                    if len(path) == 0 :
                        pass
                    else:
                        pxrTexturePath.update({(i.split('_._')[0]+'_._'+str(k)):{'linkingFile':path}})

            else:
                path = cmds.getAttr(i.split('_._')[0]+'.'+'filename')
                pxrTexturePath.update({i.split('_._')[0]:{'linkingFile':path}})


        self.countN1 = len(pxrTexturePath.keys())      
                
        
        
        
        
        
      #  print self.countN1
        self.yellowCount = 0
        self.redCount = 0
        attrKey = '.filename'
        self.shapeCheckDict ={}     #new
        self.shapeLastParName = [] #new
        self.udimFileNameList =[]
        for index in range(0,len(pxrTexturePath.keys())):
            nodeName = pxrTexturePath.keys()[index]
            linkingFile = pxrTexturePath[nodeName]['linkingFile']
            #print linkingFile
            self.checkFileExist(linkingFile,'pxrTexture')   

            checkItemTopLayerIndex = 0
            self.createNewItem(checkItemTopLayerIndex,index,nodeName,linkingFile,self.fontColor,attrKey)
            self.checkDuplicateName('pxrTexture',nodeName,checkItemTopLayerIndex,index) #new
            #print nodeName,linkingFile
            self.allNodeNameFileNameDict.update({nodeName + attrKey:linkingFile})
            self.createCopyFileInfoDictUpdate('pxrTexture',nodeName,linkingFile,attrKey)
           # createCopyFileInfoDictUpdate(self,checkMode,nodeName,linkingFile):

       # print pxrTexturePath
        topLayerItemName = "PrmanTextures"+'__('+'%03d'%self.countN1+')'

        self.setTopLayerItemColor(checkItemTopLayerIndex,topLayerItemName)         
        

        
        
     #cmds.nodeType('file2')   topLayerIndex     
         #aa= cmds.ls(typ='file') 
        # cmds.select(aa)
    def findMayaTexture(self):  # store mayaNodeName and location 
        self.plainTextEdit.setPlainText('finding mayaFiles')
     
        mayaTextureFileNode = cmds.ls( typ ='file')
        mayaTextureFilePath = {}
        for i in mayaTextureFileNode:
            path = cmds.getAttr('%s.fileTextureName'%i)
            mayaTextureFilePath.update({i:{'linkingFile':path}})
            self.linkingFilePreMoveDict.update({'mayaTexture':{i:{path:{}}}})

        attrKey = '.fileTextureName'
      
        self.countN2 = len(mayaTextureFileNode)
        self.yellowCount = 0
        self.redCount = 0    
        self.shapeCheckDict ={}    
        self.shapeLastParName = [] 
       # print self.countN2
        for index in range(0,len(mayaTextureFilePath.keys())):
            nodeName = mayaTextureFilePath.keys()[index]
            linkingFile = mayaTextureFilePath[nodeName]['linkingFile']
            self.checkFileExist(linkingFile,'mayaTexture')   
            #print 'index',index
           # print 'nodeName',nodeName
            #print 'linkingFile',linkingFile
            #print 'self.fontColor',self.fontColor
            checkItemTopLayerIndex = 1
            self.checkDuplicateName('mayaTexture',nodeName,checkItemTopLayerIndex,index) #new
            self.createNewItem(checkItemTopLayerIndex,index,nodeName,linkingFile,self.fontColor,attrKey)
            self.allNodeNameFileNameDict.update({nodeName + attrKey:linkingFile})
            self.createCopyFileInfoDictUpdate('mayaTexture',nodeName,linkingFile,attrKey)

        topLayerItemName = "mayaTextures"+'__('+'%03d'%self.countN2+')'

        self.setTopLayerItemColor(checkItemTopLayerIndex,topLayerItemName)         
        
        
            
                        
            
            
            
            
            
            
        



#cmds.nodeType('pCone1RibArchiveGPUCacheShape')
    def findGpuCaches(self): # store mayaTextures NodeName and location  
      #  pxrFilePath = 'file.fileTextureName'
        self.plainTextEdit.setPlainText('finding GpuCache')
        
        gpuCacheNodes = cmds.ls( typ ='gpuCache')
        gpuCachePath = {}
        for i in gpuCacheNodes:
            if cmds.getAttr('%s.cacheFileName'%i).split('/')[0] == 'renderman':
                path = self.workProject +'/'+cmds.getAttr('%s.cacheFileName'%i)
                gpuCachePath.update({i:{'linkingFile':path}})

            else:
                path = cmds.getAttr('%s.cacheFileName'%i)
                gpuCachePath.update({i:{'linkingFile':path}})
                


        self.countN3 = len(gpuCacheNodes)
        self.yellowCount = 0
        self.redCount = 0              

        attrKey = '.cacheFileName'
        self.shapeCheckDict ={}   
        self.shapeLastParName = [] 
        
        self.duplicateItemCount = 0

        for index in range(0,len(gpuCachePath.keys())):
            nodeName = gpuCachePath.keys()[index]
            linkingFile = gpuCachePath[nodeName]['linkingFile']
            self.checkFileExist(linkingFile,'gpuCache')
            #print 'index',index
           # print 'nodeName',nodeName
            #print 'linkingFile',linkingFile
            #print 'self.fontColor',self.fontColor
            checkItemTopLayerIndex = 2
            self.checkDuplicateName('gpuCache',nodeName,checkItemTopLayerIndex,index) #new   

            self.createNewItem(checkItemTopLayerIndex,index,nodeName,linkingFile,self.fontColor,attrKey)
            self.allNodeNameFileNameDict.update({nodeName + attrKey:linkingFile})
            self.createCopyFileInfoDictUpdate('gpuCache',nodeName,linkingFile,attrKey)


        topLayerItemName = "gpuCaches"+'__('+'%03d'%self.countN3+')'+'_'+'('+'%03d'%self.duplicateItemCount+')'

        self.setTopLayerItemColor(checkItemTopLayerIndex,topLayerItemName)         
        
        
            
                        
            
            

            
    def findRibArchives(self): # store RibArchives NodeName and location 
        print 'findRibArchives start'
        self.plainTextEdit.setPlainText('finding RibArchive')

        RibArchivesNodes = cmds.ls( typ ='RenderManArchive')
        totalCount = len(RibArchivesNodes)
        count = 0
        RibArchivesPath = {}
        for i in RibArchivesNodes:
           # print 'adsd',cmds.getAttr('%s.filename'%i).split('/')
            if cmds.getAttr('%s.filename'%i).split('/')[0] == 'renderman':
                path = self.workProject +'/'+cmds.getAttr('%s.filename'%i)
                RibArchivesPath.update({i:{'linkingFile':path}})

                #print path
            else:
                path = cmds.getAttr('%s.filename'%i)
                RibArchivesPath.update({i:{'linkingFile':path}})
                self.linkingFilePreMoveDict.update({'ribArchive':{i:{path:{}}}})
        #print 'RibArchivesPath',RibArchivesPath
        self.countN4 = len(RibArchivesNodes)
       # print' self.countN4',self.countN4
        self.yellowCount = 0
        self.redCount = 0   

        attrKey = '.filename'
       # checkMode = 'ribArchive'  
        self.shapeCheckDict ={}
        self.shapeLastParName = []
        self.duplicateItemCount = 0
        for index in range(0,len(RibArchivesPath.keys())):
           # print index
            nodeName = RibArchivesPath.keys()[index]
            linkingFile = RibArchivesPath[nodeName]['linkingFile']
          #  print 'linkingFile',linkingFile
            self.checkFileExist(linkingFile,'ribArchive')   
            checkItemTopLayerIndex = 3
            self.checkDuplicateName('ribArchive',nodeName,checkItemTopLayerIndex,index)

            self.allNodeNameFileNameDict.update({nodeName + attrKey:linkingFile})

            self.createNewItem(checkItemTopLayerIndex,index,nodeName,linkingFile,self.fontColor,attrKey)
            self.createCopyFileInfoDictUpdate('ribArchive',nodeName,linkingFile,attrKey)
            self.runProgressBar(totalCount,count)


        #print 'self.shapeCheckDict',self.shapeCheckDict
        #print 'self.shapeLastParName',self.shapeLastParName
        #print 'self.allDuplicateShapeNameDict',self.allDuplicateShapeNameDict
        topLayerItemName =  "RibArchives"+'__('+'%03d'%self.countN4+')'+'_'+'('+'%03d'%self.duplicateItemCount+')'

        self.setTopLayerItemColor(checkItemTopLayerIndex,topLayerItemName)         
        
    def findAlembics(self): # store alembics NodeName and location 
        self.plainTextEdit.setPlainText('finding alembic cache')

        alembicNodes = cmds.ls( typ ='AlembicNode')
        alembicPath = {}
        for i in alembicNodes:
            path = cmds.getAttr('%s.abc_File'%i)
            alembicPath.update({i:{'linkingFile':path}})
            self.linkingFilePreMoveDict.update({'alembic':{i:{path:{}}}})
      
        self.countN5 = len(alembicNodes)
        self.yellowCount = 0
        self.redCount = 0         
        attrKey = '.abc_File'
        self.shapeCheckDict ={}     
        self.shapeLastParName = [] 
        self.duplicateItemCount = 0

        for index in range(0,len(alembicPath.keys())):
            nodeName = alembicPath.keys()[index]
            linkingFile = alembicPath[nodeName]['linkingFile']
            self.checkFileExist(linkingFile,'alembic')   
            checkItemTopLayerIndex = 4
            self.checkDuplicateName('alembic',nodeName,checkItemTopLayerIndex,index)
            self.createNewItem(checkItemTopLayerIndex,index,nodeName,linkingFile,self.fontColor,attrKey)
            self.allNodeNameFileNameDict.update({nodeName + attrKey:linkingFile})
            self.createCopyFileInfoDictUpdate('alembic',nodeName,linkingFile,attrKey)

        topLayerItemName = "alembics"+'__('+'%03d'%self.countN5+')'+'_'+'('+'%03d'%self.duplicateItemCount+')'

        self.setTopLayerItemColor(checkItemTopLayerIndex,topLayerItemName)  
        
        
        
        
    def findPrmanLights(self): # store PrmanLights NodeName and location 
        print 'findPrmanLights start'
        self.plainTextEdit.setPlainText('finding Prman Light')

        prmanLightType =['PxrRectLight','PxrDiskLight','PxrDistantLight','PxrSphereLight','PxrDomeLight','PxrEnvDayLight','PxrMeshLight']
        prmanLightNodes = []
        prmanLightInfo = {}
        for prmanNodeType in prmanLightType:
            prmanLightNodes = prmanLightNodes + cmds.ls( typ =prmanNodeType)
  
       # print prmanLightNodes 
        self.yellowCount = 0
        self.redCount = 0      
        attrKey = '.lightColorMap'
        self.shapeCheckDict ={}     
        self.shapeLastParName = [] 
        for i in prmanLightNodes:
            intensity = cmds.getAttr('%s.intensity'%i)
            exposure = cmds.getAttr('%s.exposure'%i)
            if cmds.nodeType(i) == 'PxrEnvDayLight' :  
                lightColor = 'None'
            else :
                lightColor = cmds.getAttr('%s.lightColor'%i)  
                
                                     
            if cmds.nodeType(i) == 'PxrRectLight' :           
                lightColorMap = cmds.getAttr('%s.lightColorMap'%i)
            else:
                lightColorMap = 'None'
                
            if cmds.nodeType(i) == 'PxrDomeLight' :           
                lightColorMap = cmds.getAttr('%s.lightColorMap'%i)
            else:
                lightColorMap = 'None'
                
                             
            if cmds.nodeType(i) == 'PxrMeshLight' :           
                textureColor = cmds.getAttr('%s.textureColor'%i)
            else:
                textureColor = 'None' 
                
                
            if cmds.nodeType(i) == 'PxrDistantLight' :           
                angleExtent = cmds.getAttr('%s.angleExtent'%i)
            else:
                angleExtent = 'None'
            
            prmanLightInfo.update({i:{'intensity':intensity,
                                      'exposure':exposure,
                                      'lightColor':lightColor,
                                      'linkingFile':lightColorMap, #lightColorMap
                                      'angleExtent':angleExtent,
                                      'textureColor':textureColor,
                                      
                                      }})
            self.linkingFilePreMoveDict.update({'pxrLight':{i:{lightColorMap:{}}}})

        self.countN7 = len(prmanLightInfo.keys())
        
        for index in range(0,len(prmanLightInfo.keys())):
            nodeName = prmanLightInfo.keys()[index]
            linkingFile = prmanLightInfo[nodeName]['linkingFile']
            self.checkFileExist(linkingFile,'pxrLight')   
            checkItemTopLayerIndex = 6

            self.checkDuplicateName('pxrLight',nodeName,checkItemTopLayerIndex,index)
            self.createNewItem(checkItemTopLayerIndex,index,nodeName,linkingFile,self.fontColor,attrKey)
            self.allNodeNameFileNameDict.update({nodeName + attrKey:linkingFile})
            
            self.createCopyFileInfoDictUpdate('pxrLight',nodeName,linkingFile,attrKey)
 
        topLayerItemName = "PrmanLights"+'__('+'%03d'%self.countN7+')'

        self.setTopLayerItemColor(checkItemTopLayerIndex,topLayerItemName)  
        
        
        
#cmds.listConnections('nParticleShape1')        
    def mayaFluidCache(self): # store mayaTextures NodeName and location 
      #  pxrFilePath = 'file.fileTextureName'
        self.plainTextEdit.setPlainText('finding mayaFluidCache')
      
        mayaFluidCacheInfo = {}
        
        mayaFileNodes = cmds.ls( typ ='fluidShape')
        attrKey = '.cacheName'
        
        for i in mayaFileNodes:
            for fluidCache in cmds.listConnections(i):
                if cmds.nodeType(fluidCache) == 'cacheFile':
                   # print fluidShape
                    baseDirectory = cmds.getAttr('%s.cachePath'%fluidCache)
                    baseName = cmds.getAttr('%s.cacheName'%fluidCache)
                    isEnable = cmds.getAttr('%s.enable'%fluidCache)
                    startFrame = cmds.getAttr('%s.startFrame'%fluidCache)
                    scale = cmds.getAttr('%s.scale'%fluidCache)
                    hold = cmds.getAttr('%s.hold'%fluidCache)
                    preCycle = cmds.getAttr('%s.preCycle'%fluidCache)
                    postCycle = cmds.getAttr('%s.postCycle'%fluidCache)
                    sourceStart = cmds.getAttr('%s.sourceStart'%fluidCache)
                    sourceEnd = cmds.getAttr('%s.sourceEnd'%fluidCache)
                    originalStart = cmds.getAttr('%s.originalStart'%fluidCache)
                    originalEnd= cmds.getAttr('%s.originalEnd'%fluidCache)
                    path = baseDirectory + baseName +'.xml'
                    mayaFluidCacheInfo.update({i:{'baseDirectory':baseDirectory,
                                                  'baseName':baseName,
                                                  'isEnable':isEnable,
                                                  'startFrame':startFrame,
                                                  'scale':scale,
                                                  'hold':hold,
                                                  'preCycle':preCycle,
                                                  'postCycle':postCycle,
                                                  'sourceStart':sourceStart,
                                                  'sourceEnd':sourceEnd,
                                                  'originalStart':originalStart,
                                                  'originalEnd':originalEnd,
                                                  'linkingFile':path}})
          
                    self.linkingFilePreMoveDict.update({'mayaFluid':{i:{path:{}}}})

        self.countN9 = len(mayaFluidCacheInfo.keys())
        self.yellowCount = 0
        self.redCount = 0        
        
        self.shapeCheckDict ={}     
        self.shapeLastParName = []       
        self.duplicateItemCount = 0
             
        for index in range(0,len(mayaFluidCacheInfo.keys())):
            nodeName = mayaFluidCacheInfo.keys()[index]
            linkingFile = mayaFluidCacheInfo[nodeName]['linkingFile']
            self.checkFileExist(linkingFile,'mayaFluid')   
            checkItemTopLayerIndex = 7
            self.checkDuplicateName('mayaFluid',nodeName,checkItemTopLayerIndex,index)
            self.createNewItem(checkItemTopLayerIndex,index,nodeName,linkingFile,self.fontColor,attrKey)
            self.allNodeNameFileNameDict.update({nodeName + attrKey:linkingFile})
            self.createCopyFileInfoDictUpdate('mayaFluid',nodeName,linkingFile,attrKey)
            
            
        topLayerItemName = "fluidCaches"+'__('+'%03d'%self.countN9+')'+'_'+'('+'%03d'%self.duplicateItemCount+')'
        

        self.setTopLayerItemColor(checkItemTopLayerIndex,topLayerItemName)      

       # print 'mayaFluidCacheInfo',mayaFluidCacheInfo
    def mayanParticleCache(self): # store mayanParticle NodeName and location fluidCache
        self.plainTextEdit.setPlainText('finding maya nParticle')
     
        mayanParticleCacheInfo = {}
        
        mayanParticleNodes = cmds.ls( typ ='nParticle')
        for nParticleShape in mayanParticleNodes:
            for i in cmds.listConnections(nParticleShape):
                if cmds.nodeType(i) == 'cacheFile':
                    baseDirectory = cmds.getAttr('%s.cachePath'%i)
                    baseName = cmds.getAttr('%s.cacheName'%i)
                    isEnable = cmds.getAttr('%s.enable'%i)
                    startFrame = cmds.getAttr('%s.startFrame'%i)
                    scale = cmds.getAttr('%s.scale'%i)
                    hold = cmds.getAttr('%s.hold'%i)
                    preCycle = cmds.getAttr('%s.preCycle'%i)
                    postCycle = cmds.getAttr('%s.postCycle'%i)
                    sourceStart = cmds.getAttr('%s.sourceStart'%i)
                    sourceEnd = cmds.getAttr('%s.sourceEnd'%i)
                    originalStart = cmds.getAttr('%s.originalStart'%i)
                    originalEnd= cmds.getAttr('%s.originalEnd'%i)
                    path = baseDirectory + baseName +'.xml'

                    mayanParticleCacheInfo.update({i:{'baseDirectory':baseDirectory,
                                                  'baseName':baseName,
                                                  'isEnable':isEnable,
                                                  'startFrame':startFrame,
                                                  'scale':scale,
                                                  'hold':hold,
                                                  'preCycle':preCycle,
                                                  'postCycle':postCycle,
                                                  'sourceStart':sourceStart,
                                                  'sourceEnd':sourceEnd,
                                                  'originalStart':originalStart,
                                                  'originalEnd':originalEnd,
                                                  'linkingFile':path}})       
                    
                    self.linkingFilePreMoveDict.update({'mayanParticle':{i:{path:{}}}})
        attrKey = '.cacheName'
             
        self.yellowCount = 0
        self.redCount = 0          
        
        self.shapeCheckDict ={}     
        self.shapeLastParName = []       
        self.duplicateItemCount = 0
                  
        for index in range(0,len(mayanParticleCacheInfo.keys())):
            nodeName = mayanParticleCacheInfo.keys()[index]
            linkingFile = mayanParticleCacheInfo[nodeName]['linkingFile']
            self.checkFileExist(linkingFile,'mayanParticle')   
            checkItemTopLayerIndex = 8
            self.checkDuplicateName('mayanParticle',nodeName,checkItemTopLayerIndex,index)

            self.createNewItem(checkItemTopLayerIndex,index,nodeName,linkingFile,self.fontColor,attrKey)
            self.allNodeNameFileNameDict.update({nodeName + attrKey:linkingFile})
            self.createCopyFileInfoDictUpdate('mayanParticle',nodeName,linkingFile,attrKey)
     
        
        topLayerItemName ="particleCaches"+'__('+'%03d'%self.countN10+')'+'_'+'('+'%03d'%self.duplicateItemCount+')'


        self.setTopLayerItemColor(checkItemTopLayerIndex,topLayerItemName)      





    def findPlugin(self): # store plugin NodeName and location 
        print 'findPlugin start'
        

        pluginNode = cmds.pluginInfo( q=True, listPlugins=True, av=True )
        allPlugInNode = {}
        for i in pluginNode:
            allPlugInNode.update({i:{}})
            
        badplugins = cmds.unknownPlugin(q=True, l=True)

                
       # print 'allPlugInNode',allPlugInNode
        #print 'badplugins',badplugins
        loadCound = len(pluginNode)
        try: 
            if len(badplugins) > 0:
                #print 'aaaa'
                badCount = len(badplugins)
        except:
            
            badCount = 0
            
    #    print badCount
    #    print 'badCount',badCount
        self.countN11 = badCount + loadCound

     #   print self.countN11 ,badCount,loadCound

        
        for index in range(0,badCount):
            nodeName = badplugins[index]

            QtWidgets.QTreeWidgetItem(self.treeWidget_filesList.topLevelItem(9))
            self.treeWidget_filesList.topLevelItem(9).child(index).setForeground(0,QtGui.QBrush(QtGui.QColor(255,0,0)))

            self.treeWidget_filesList.topLevelItem(9).child(index).setText(0, QtWidgets.QApplication.translate("MainWindow", 'tempName', None, -1))
            self.treeWidget_filesList.topLevelItem(9).child(index).setText(0,nodeName)
            self.treeWidget_filesList.topLevelItem(9).child(index).setCheckState(0, QtCore.Qt.Checked)
           # print index
        #print 'break'
        for index in range(badCount,self.countN11) :
            #print index
           # for i in range(0,loadCound):
                 
            nodeName = allPlugInNode.keys()[index-badCount]
           # print nodeName
            
            QtWidgets.QTreeWidgetItem(self.treeWidget_filesList.topLevelItem(9))
            self.treeWidget_filesList.topLevelItem(9).child(index).setForeground(0,QtGui.QBrush(QtGui.QColor(0,255,0)))

            self.treeWidget_filesList.topLevelItem(9).child(index).setText(0, QtWidgets.QApplication.translate("MainWindow", 'tempName', None, -1))
            self.treeWidget_filesList.topLevelItem(9).child(index).setText(0,nodeName)
            self.treeWidget_filesList.topLevelItem(9).child(index).setCheckState(0, QtCore.Qt.Unchecked)
        self.searchPluginIsChecked()   
        self.itemName_plugin = "plungin"+'__('+'%03d'%self.countN11+')' 
        if badCount > 0:

        

            self.treeWidget_filesList.topLevelItem(9).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_plugin, None, -1))
       
            self.treeWidget_filesList.topLevelItem(9).setForeground(0,QtGui.QBrush(QtGui.QColor(255,0,0)))
      
        
        else:
            
               

            self.treeWidget_filesList.topLevelItem(9).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_plugin, None, -1))
           
            self.treeWidget_filesList.topLevelItem(9).setForeground(0,QtGui.QBrush(QtGui.QColor(255,255,255)))
          
    def replaceFileRoot(self):
        #print 'self.allNodeNameFileNameDict',self.allNodeNameFileNameDict
        for i in range(0,len(self.allNodeNameFileNameDict.keys())):
        #for i in range(0,5):

            #print self.allNodeNameFileNameDict.keys()[i]
            #source = self.lineEdit_file_sources_2.text()
            #dect = 
            nodeName = self.allNodeNameFileNameDict.keys()[i]
            newName = self.lineEdit_file_sources_2.text()+self.allNodeNameFileNameDict[self.allNodeNameFileNameDict.keys()[i]].split(self.lineEdit_file_sources.text())[-1]
            #print nodeName,newName
            
            cmds.setAttr('%s'%nodeName,'%s'%newName)
        
                
#cmds.setAttr('UDS_actinia_e_GPU_Shape_0001.filename','///mcd-3D/art_3d_project/ocean_world_2016_cf/assets/other/master/rigging/data/cache/actinia_e_mesh/actinia_e_mesh.zip')
#cmds.select('UDS_coral_e_GPU_Shape_1')
       # print 'self.badPluginNodeList',self.badPluginNodeList
        
        
        
        
        
        
    def setTopLayerItemColor(self,checkItemTopLayerIndex,topLayerItemName):
        if self.redCount > 0:

            self.topLayerColor = (255,0,0)
        
        else:
            
            if self.yellowCount >0 :
                self.topLayerColor = (255,255,0)
                
            else:
                self.topLayerColor = (255,255,255)
        self.treeWidget_filesList.topLevelItem(checkItemTopLayerIndex).setText(0, QtWidgets.QApplication.translate("MainWindow",topLayerItemName, None, -1))
       
        self.treeWidget_filesList.topLevelItem(checkItemTopLayerIndex).setForeground(0,QtGui.QBrush(QtGui.QColor(int(self.topLayerColor[0]), int(self.topLayerColor[1]), int(self.topLayerColor[2]))))
                
    def storeDuplicateNameDictToJson(self):
        storeFileName = self.userPrefDict['self.assetBranchFileDir'] + '/' + self.userPrefDict['self.assetNow'] +'_duplicateNameDict.json'
        f = open(storeFileName, 'w')
        data = json.dumps(self.allDuplicateShapeNameDict, sort_keys=True , indent =4)
        f.write(data)
        f.close
        #storeFileInfoName = self.userPrefDict['self.assetBranchFileDir'] + '/' + self.userPrefDict['self.assetNow'] +'_fileInfoReadyToCopy.json'
        #f = open(storeFileInfoName, 'w')
        #dataB = json.dumps(self.allCopyFileInfoDict, sort_keys=True , indent =4)
        #f.write(dataB)
        #f.close
        storeFileName = self.userPrefDict['self.assetBranchFileDir'] + '/' + self.userPrefDict['self.assetNow'] +'_allNodesLocation.json'
        f = open(storeFileName, 'w')
        data = json.dumps(self.allNodeNameFileNameDict, sort_keys=True , indent =4)
        f.write(data)
        f.close    

   # def reNameDuplicateShape(self):reNameDuplicateShapeName

    def reNameDuplicateShapeName(self):
        print 'reNameDuplicateShapeName start'
        self.checkParentItemNameDuplicate()
        self.reflashTree()
        self.storeDuplicateNameDictToJson()

        
    def reNameDuplicateShapeNameB(self):
        print 'reNameDuplicateShapeName start'
        if self.lineEdit_prefixName.text() == 'Prefix':
            self.prefix =''
        else:
            self.prefix = self.lineEdit_prefixName.text()
        
        if self.treeWidget_FiletOption.topLevelItem(3).child(0).checkState(0) == QtCore.Qt.CheckState.Checked:# check rib ischecked
            self.doReNameDuplicateShapeName('ribArchive')
        if self.treeWidget_FiletOption.topLevelItem(3).child(1).checkState(0) == QtCore.Qt.CheckState.Checked: # check gpu ischecked    
            self.doReNameDuplicateShapeName('gpuCache')
        if self.treeWidget_FiletOption.topLevelItem(3).child(2).checkState(0) == QtCore.Qt.CheckState.Checked:  #check abc ischecked  
            self.doReNameDuplicateShapeName('alembic') 
        if self.treeWidget_FiletOption.topLevelItem(3).child(3).checkState(0) == QtCore.Qt.CheckState.Checked:  # check fluid ischecked    
            self.doReNameDuplicateShapeName('mayaFluid')
        if self.treeWidget_FiletOption.topLevelItem(3).child(4).checkState(0) == QtCore.Qt.CheckState.Checked: # check nparticle ischecked    
            self.doReNameDuplicateShapeName('mayanParticle')
            
        self.reflashTree()
        self.storeDuplicateNameDictToJson()
        
        
    def doReNameDuplicateShapeName(self,mode):
        reNameTempDict={}
        for i in self.allDuplicateShapeNameDict[mode].keys():
            if self.allDuplicateShapeNameDict[mode][i]['itemLevelIndex'][2] == 'duplicateName':
                reNameTempDict.update({i.split('|')[-1]:0})
            else:
                pass
        for i in self.allDuplicateShapeNameDict[mode].keys():
            if i.split('|')[-1] in reNameTempDict.keys():
                count = reNameTempDict[i.split('|')[-1]]+1
                #print i#.split('|')[-1],count
                reNameTempDict.update({i.split('|')[-1]:count})
                if self.prefix == '':
                    newName = i.split('|')[-1]+'_'+'%04d'%count
                else:
                    
                    newName = self.prefix+'_'+ i.split('|')[-1]+'_'+'%04d'%count
                transformName = newName.split('Shape')[0]+'_'+'%04d'%count

                try:
     
                   # transformSelect = cmds.select(cmds.listRelatives(i,p=True,f=True))
                    
                    cmds.rename(i,newName)
                  #  cmds.rename(cmds.select(cmds.listRelatives(newName,p=True,f=True)),transformName)
                except:
                    pass
                    
        
    def checkParentItemNameDuplicate(self):
       # storeFileName = self.userPrefDict['self.assetBranchFileDir'] + '/' + self.userPrefDict['self.assetNow'] +'_duplicateNameDict.json'

       # with open(storeFileName) as data_file:    
        #    data = json.load(data_file)
        data = self.allDuplicateShapeNameDict    

        maxNodeNameLength = [] #get max length of nodeName that split('|')
        checkDuplictShapeBuffer = {}
        checkNodeNameLengthBuffer = {}
        for i in range(0,len(data.keys())):
            totalNodeCountByMode = len(data[data.keys()[i]].keys())
            
            for j in range(0,totalNodeCountByMode):
             #   if j >500 :
                #    pass
             #   else:
                nodeName = data[data.keys()[i]].keys()[j]

                nodeNameLength = len(nodeName.split('|'))
                checkNodeNameLengthBuffer.update({nodeName:nodeNameLength})
                if nodeNameLength in maxNodeNameLength:
                    pass
                else:
                    maxNodeNameLength.append(nodeNameLength)
                #print nodeNameLength
                if nodeNameLength >1:
                   # print data[data.keys()[i]].keys()[j]
                   # print nodeName

                    finalShapeName = nodeName.split('|')[-1]
                   # print finalShapeName
                    
                    if finalShapeName not in checkDuplictShapeBuffer.keys():
                       # print checkDuplictShapeBuffer[finalShapeName]
                        #int(checkDuplictShapeBuffer[finalShapeName]) = int(checkDuplictShapeBuffer[finalShapeName]) +1
                   # else:
                    #checkDuplictShapeBuffer.update({finalShapeName:(checkDuplictShapeBuffer[finalShapeName]+1)})
                        checkDuplictShapeBuffer.update({finalShapeName:0}) 
                        count = checkDuplictShapeBuffer[finalShapeName]
                    else:
                        count = count +1
                        checkDuplictShapeBuffer.update({finalShapeName:count}) 
                        
                        newLastLevelShapeName = finalShapeName +'_'+ '%04d'%count
                        #for k in range(0,len(nodeName.split('|'))):
                        #    print k , len(nodeName.split('|'))-k
                        max =nodeNameLength +1
                #        print nodeNameLength
                #        print 'nodeName',nodeName
                        maxReverse = max-1 
                        for c in range(0,max-1):
                            listAdd = ''
                            for d in range(1,maxReverse+1):
                                listAdd= listAdd +'|'+  nodeName.split('|')[(d-1)]
                            maxReverse = maxReverse -1

                            sourceNodeName = listAdd[1:]
                            dectNodeName = sourceNodeName.split('|')[-1] +'_'+'%04d'%count
                 #           print sourceNodeName ,dectNodeName
                           # try:
                         #   cmds.rename(sourceNodeName,dectNodeName)
                           # except:
                           #     pass
                else:
                    pass
                            
                            
    
        
 #cmds.select('UDS_actinia_e_0001|UDS_actinia_e_GPU_Shape_25_0001|UDS_actinia_e_GPU_Shape_25_0001|UDS_actinia_e_GPU_Shape_25_000Shape_1')  
 #cmds.rename('UDS_ribAssetGrp_0003|UDS_coral_a2_GPU_Shape_7_0003|UDS_coral_a2_topGrp_9','UDS_coral_a2_topGrp_9_0017')
#cmds.ls(typ='UDS_actinia_f_GPU_Shape_10')    
      #  self.treeWidget_FiletOption.topLevelItem(3).child(1).checkState(0) == QtCore.Qt.CheckState.Checked: # check gpu ischecked
      #  self.treeWidget_FiletOption.topLevelItem(3).child(2).checkState(0) == QtCore.Qt.CheckState.Checked: # check abc ischecked
      #  self.treeWidget_FiletOption.topLevelItem(3).child(3).checkState(0) == QtCore.Qt.CheckState.Checked:  # check fluid ischecked
       # self.treeWidget_FiletOption.topLevelItem(3).child(4).checkState(0) == QtCore.Qt.CheckState.Checked: # check nparticle ischecked

    def showFileMetaData(self,fileName,mode):
        print 'showFileMetaData start'
        image = ice.Load(fileName)
        showText=""
        for i in range(0,len(image.GetMetaData().keys())):
            showText = showText +  str(image.GetMetaData().keys()[i]) +"  :  " +str(image.GetMetaData()[image.GetMetaData().keys()[i]]) +"\n"
        self.plainTextEdit.setPlainText(showText)

def main():
#def publishToolMain():
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


 
 
 
 
 
 