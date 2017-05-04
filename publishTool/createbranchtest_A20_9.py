# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha/Documents/GitHub/ribGen/publishTool/createbranchtest_01.ui'
#
# Created: Fri Mar 17 00:34:42 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import maya.cmds as cmds
import json , os , getpass,socket ,ctypes.wintypes
import datetime


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.setFontSize=8
        #setPointSize(self.setFontSize +3) = setPointSize(self.setFontSize +3)
        #setPointSize(self.setFontSize +3) = setPointSize(self.setFontSize +2)
        #setPointSize(8 ) = setPointSize(self.setFontSize) 
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(846, 708)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setAcceptDrops(False)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget_branch = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_branch.setGeometry(QtCore.QRect(0, 0, 841, 681))
        palette = QtGui.QPalette()
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
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        self.tabWidget_branch.setPalette(palette)
        self.tabWidget_branch.setAutoFillBackground(True)
        self.tabWidget_branch.setObjectName("tabWidget_branch")
        self.tab_job_assemble = QtWidgets.QWidget()
        self.tab_job_assemble.setObjectName("tab_job_assemble")
        self.label_2 = QtWidgets.QLabel(self.tab_job_assemble)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 81, 12))
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
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(self.setFontSize) 
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_job_assemble)
        self.lineEdit.setGeometry(QtCore.QRect(100, 30, 113, 12))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 31, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 26, 23))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(7, 10, 9))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(9, 14, 12))
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
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(7, 10, 9))
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
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 31, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 26, 23))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(7, 10, 9))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(9, 14, 12))
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
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(7, 10, 9))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(7, 10, 9))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 31, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 26, 23))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(7, 10, 9))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(9, 14, 12))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(7, 10, 9))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(7, 10, 9))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.lineEdit.setPalette(palette)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.tab_job_assemble)
        self.pushButton.setGeometry(QtCore.QRect(220, 30, 80, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize) 
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(self.tab_job_assemble)
        self.listWidget.setGeometry(QtCore.QRect(30, 90, 181, 521))
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
        self.listWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        QtWidgets.QListWidgetItem(self.listWidget)
        QtWidgets.QListWidgetItem(self.listWidget)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_job_assemble)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 70, 80, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_job_assemble)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 70, 80, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_job_assemble)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(750, 80, 81, 112))
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
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(750, 240, 81, 170))
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
        self.pushButton_26 = QtWidgets.QPushButton(self.tab_job_assemble)
        self.pushButton_26.setGeometry(QtCore.QRect(360, 50, 80, 20))
        self.pushButton_26.setObjectName("pushButton_26")
        self.listWidget_3 = QtWidgets.QListWidget(self.tab_job_assemble)
        self.listWidget_3.setGeometry(QtCore.QRect(250, 90, 181, 521))
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
        self.listWidget_3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.listWidget_3.setFont(font)
        self.listWidget_3.setObjectName("listWidget_3")
        QtWidgets.QListWidgetItem(self.listWidget_3)
        QtWidgets.QListWidgetItem(self.listWidget_3)
        self.tabWidget_branch.addTab(self.tab_job_assemble, "")
        self.tab_branch = QtWidgets.QWidget()
        self.tab_branch.setObjectName("tab_branch")
        self.lineEdit_branchName = QtWidgets.QLineEdit(self.tab_branch)
        self.lineEdit_branchName.setGeometry(QtCore.QRect(250, 401, 171, 40))
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
        self.pushButton_editFileInfo = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_editFileInfo.setGeometry(QtCore.QRect(790, 270, 31, 31))
        self.pushButton_editFileInfo.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/publishToolIcon/edit2_512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_editFileInfo.setIcon(icon)
        self.pushButton_editFileInfo.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_editFileInfo.setAutoDefault(False)
        self.pushButton_editFileInfo.setDefault(False)
        self.pushButton_editFileInfo.setFlat(True)
        self.pushButton_editFileInfo.setObjectName("pushButton_editFileInfo")
        self.label = QtWidgets.QLabel(self.tab_branch)
        self.label.setGeometry(QtCore.QRect(250, 380, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.treeWidget_branches = QtWidgets.QTreeWidget(self.tab_branch)
        self.treeWidget_branches.setGeometry(QtCore.QRect(250, 70, 171, 311))
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
        self.tableWidget_FileList = QtWidgets.QTableWidget(self.tab_branch)
        self.tableWidget_FileList.setGeometry(QtCore.QRect(440, 70, 351, 151))
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
        self.tableWidget_FileList.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(self.setFontSize) 
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
        self.lineEdit_currentFileName = QtWidgets.QLineEdit(self.tab_branch)
        self.lineEdit_currentFileName.setGeometry(QtCore.QRect(440, 220, 351, 27))
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
        self.pushButton_saveFile = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_saveFile.setGeometry(QtCore.QRect(790, 70, 31, 31))
        self.pushButton_saveFile.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/publishToolIcon/upload2-512 C.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_saveFile.setIcon(icon1)
        self.pushButton_saveFile.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_saveFile.setAutoDefault(False)
        self.pushButton_saveFile.setDefault(False)
        self.pushButton_saveFile.setFlat(True)
        self.pushButton_saveFile.setObjectName("pushButton_saveFile")
        self.pushButton_loadFile = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_loadFile.setGeometry(QtCore.QRect(790, 100, 31, 31))
        self.pushButton_loadFile.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/publishToolIcon/download2-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_loadFile.setIcon(icon2)
        self.pushButton_loadFile.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_loadFile.setAutoDefault(False)
        self.pushButton_loadFile.setDefault(False)
        self.pushButton_loadFile.setFlat(True)
        self.pushButton_loadFile.setObjectName("pushButton_loadFile")
        self.pushButton_openFolder = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_openFolder.setGeometry(QtCore.QRect(790, 300, 31, 31))
        self.pushButton_openFolder.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/publishToolIcon/openFolder2-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_openFolder.setIcon(icon3)
        self.pushButton_openFolder.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_openFolder.setAutoDefault(False)
        self.pushButton_openFolder.setDefault(False)
        self.pushButton_openFolder.setFlat(True)
        self.pushButton_openFolder.setObjectName("pushButton_openFolder")
        self.label_fileDescription = QtWidgets.QLabel(self.tab_branch)
        self.label_fileDescription.setGeometry(QtCore.QRect(440, 250, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_fileDescription.setFont(font)
        self.label_fileDescription.setObjectName("label_fileDescription")
        self.pushButton_createNewBranch = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_createNewBranch.setGeometry(QtCore.QRect(250, 440, 31, 31))
        self.pushButton_createNewBranch.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/publishToolIcon/newBranch2-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_createNewBranch.setIcon(icon4)
        self.pushButton_createNewBranch.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_createNewBranch.setAutoDefault(False)
        self.pushButton_createNewBranch.setDefault(False)
        self.pushButton_createNewBranch.setFlat(True)
        self.pushButton_createNewBranch.setObjectName("pushButton_createNewBranch")
        self.pushButton_mergeToMaster = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_mergeToMaster.setGeometry(QtCore.QRect(280, 440, 31, 31))
        self.pushButton_mergeToMaster.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/publishToolIcon/merge2-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_mergeToMaster.setIcon(icon5)
        self.pushButton_mergeToMaster.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_mergeToMaster.setAutoDefault(False)
        self.pushButton_mergeToMaster.setDefault(False)
        self.pushButton_mergeToMaster.setFlat(True)
        self.pushButton_mergeToMaster.setObjectName("pushButton_mergeToMaster")
        self.pushButton_closeBranch = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_closeBranch.setGeometry(QtCore.QRect(790, 160, 31, 31))
        self.pushButton_closeBranch.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/publishToolIcon/delete2_512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_closeBranch.setIcon(icon6)
        self.pushButton_closeBranch.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_closeBranch.setAutoDefault(False)
        self.pushButton_closeBranch.setDefault(False)
        self.pushButton_closeBranch.setFlat(True)
        self.pushButton_closeBranch.setObjectName("pushButton_closeBranch")
        self.pushButton_openFileJson = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_openFileJson.setGeometry(QtCore.QRect(790, 130, 31, 31))
        self.pushButton_openFileJson.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/publishToolIcon/document2-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_openFileJson.setIcon(icon7)
        self.pushButton_openFileJson.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_openFileJson.setAutoDefault(False)
        self.pushButton_openFileJson.setDefault(False)
        self.pushButton_openFileJson.setFlat(True)
        self.pushButton_openFileJson.setObjectName("pushButton_openFileJson")
        self.pushButton_openBranchJson = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_openBranchJson.setGeometry(QtCore.QRect(390, 440, 31, 31))
        self.pushButton_openBranchJson.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/publishToolIcon/option2-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_openBranchJson.setIcon(icon8)
        self.pushButton_openBranchJson.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_openBranchJson.setAutoDefault(False)
        self.pushButton_openBranchJson.setDefault(False)
        self.pushButton_openBranchJson.setFlat(True)
        self.pushButton_openBranchJson.setObjectName("pushButton_openBranchJson")
        self.label_fileData = QtWidgets.QLabel(self.tab_branch)
        self.label_fileData.setGeometry(QtCore.QRect(440, 50, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_fileData.setFont(font)
        self.label_fileData.setObjectName("label_fileData")
        self.plainTextEdit_BranchFileInfo = QtWidgets.QPlainTextEdit(self.tab_branch)
        self.plainTextEdit_BranchFileInfo.setGeometry(QtCore.QRect(440, 270, 351, 171))
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
        self.plainTextEdit_metaData = QtWidgets.QPlainTextEdit(self.tab_branch)
        self.plainTextEdit_metaData.setGeometry(QtCore.QRect(440, 467, 351, 61))
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
        self.plainTextEdit_metaData.setPalette(palette)
        self.plainTextEdit_metaData.setObjectName("plainTextEdit_metaData")
        self.pushButton_character = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_character.setEnabled(True)
        self.pushButton_character.setGeometry(QtCore.QRect(40, 70, 30, 30))
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
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/publishToolIcon/chaS5Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon9.addPixmap(QtGui.QPixmap("icons/publishToolIcon/chaS5Open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_character.setIcon(icon9)
        self.pushButton_character.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_character.setCheckable(True)
        self.pushButton_character.setChecked(False)
        self.pushButton_character.setAutoRepeat(False)
        self.pushButton_character.setAutoExclusive(False)
        self.pushButton_character.setAutoDefault(False)
        self.pushButton_character.setDefault(False)
        self.pushButton_character.setFlat(True)
        self.pushButton_character.setObjectName("pushButton_character")
        self.listWidget_assetProj = QtWidgets.QListWidget(self.tab_branch)
        self.listWidget_assetProj.setGeometry(QtCore.QRect(70, 70, 151, 371))
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
        font.setPointSize(self.setFontSize) 
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
        self.pushButton_setting = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_setting.setGeometry(QtCore.QRect(40, 600, 31, 31))
        self.pushButton_setting.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/publishToolIcon/gear2-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_setting.setIcon(icon10)
        self.pushButton_setting.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_setting.setAutoDefault(False)
        self.pushButton_setting.setDefault(False)
        self.pushButton_setting.setFlat(True)
        self.pushButton_setting.setObjectName("pushButton_setting")
        self.pushButton_publish = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_publish.setGeometry(QtCore.QRect(40, 560, 31, 31))
        self.pushButton_publish.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/publishToolIcon/masterB2-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_publish.setIcon(icon11)
        self.pushButton_publish.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_publish.setAutoDefault(False)
        self.pushButton_publish.setDefault(False)
        self.pushButton_publish.setFlat(True)
        self.pushButton_publish.setObjectName("pushButton_publish")
        self.pushButton_syncFile = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_syncFile.setGeometry(QtCore.QRect(70, 560, 31, 31))
        self.pushButton_syncFile.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons/publishToolIcon/radial_arrows2-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_syncFile.setIcon(icon12)
        self.pushButton_syncFile.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_syncFile.setAutoDefault(False)
        self.pushButton_syncFile.setDefault(False)
        self.pushButton_syncFile.setFlat(True)
        self.pushButton_syncFile.setObjectName("pushButton_syncFile")
        self.pushButton_reNewBranchDict = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_reNewBranchDict.setGeometry(QtCore.QRect(70, 600, 31, 31))
        self.pushButton_reNewBranchDict.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icons/publishToolIcon/wrench2-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_reNewBranchDict.setIcon(icon13)
        self.pushButton_reNewBranchDict.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_reNewBranchDict.setAutoDefault(False)
        self.pushButton_reNewBranchDict.setDefault(False)
        self.pushButton_reNewBranchDict.setFlat(True)
        self.pushButton_reNewBranchDict.setObjectName("pushButton_reNewBranchDict")
        self.checkBox_collectFile = QtWidgets.QCheckBox(self.tab_branch)
        self.checkBox_collectFile.setGeometry(QtCore.QRect(10, 530, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.checkBox_collectFile.setFont(font)
        self.checkBox_collectFile.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_collectFile.setObjectName("checkBox_collectFile")
        self.checkBox_errorCheck = QtWidgets.QCheckBox(self.tab_branch)
        self.checkBox_errorCheck.setGeometry(QtCore.QRect(10, 510, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.checkBox_errorCheck.setFont(font)
        self.checkBox_errorCheck.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_errorCheck.setObjectName("checkBox_errorCheck")
        self.label_metaData = QtWidgets.QLabel(self.tab_branch)
        self.label_metaData.setGeometry(QtCore.QRect(440, 450, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_metaData.setFont(font)
        self.label_metaData.setObjectName("label_metaData")
        self.pushButton_vehicle = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_vehicle.setEnabled(True)
        self.pushButton_vehicle.setGeometry(QtCore.QRect(40, 100, 30, 30))
        self.pushButton_vehicle.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("icons/publishToolIcon/vehS5Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon14.addPixmap(QtGui.QPixmap("icons/publishToolIcon/vehS5_open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_vehicle.setIcon(icon14)
        self.pushButton_vehicle.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_vehicle.setCheckable(True)
        self.pushButton_vehicle.setAutoDefault(False)
        self.pushButton_vehicle.setDefault(False)
        self.pushButton_vehicle.setFlat(True)
        self.pushButton_vehicle.setObjectName("pushButton_vehicle")
        self.pushButton_set = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_set.setEnabled(True)
        self.pushButton_set.setGeometry(QtCore.QRect(40, 130, 30, 30))
        self.pushButton_set.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("icons/publishToolIcon/setS5Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon15.addPixmap(QtGui.QPixmap("icons/publishToolIcon/setS5Open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_set.setIcon(icon15)
        self.pushButton_set.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_set.setCheckable(True)
        self.pushButton_set.setAutoDefault(False)
        self.pushButton_set.setDefault(False)
        self.pushButton_set.setFlat(True)
        self.pushButton_set.setObjectName("pushButton_set")
        self.pushButton_props = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_props.setEnabled(True)
        self.pushButton_props.setGeometry(QtCore.QRect(40, 160, 30, 30))
        self.pushButton_props.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("icons/publishToolIcon/propsS5Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon16.addPixmap(QtGui.QPixmap("icons/publishToolIcon/propsS5Open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_props.setIcon(icon16)
        self.pushButton_props.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_props.setCheckable(True)
        self.pushButton_props.setAutoDefault(False)
        self.pushButton_props.setDefault(False)
        self.pushButton_props.setFlat(True)
        self.pushButton_props.setObjectName("pushButton_props")
        self.pushButton_others = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_others.setEnabled(True)
        self.pushButton_others.setGeometry(QtCore.QRect(40, 190, 30, 30))
        self.pushButton_others.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("icons/publishToolIcon/otherS5Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon17.addPixmap(QtGui.QPixmap("icons/publishToolIcon/otherS5Open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_others.setIcon(icon17)
        self.pushButton_others.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_others.setCheckable(True)
        self.pushButton_others.setAutoDefault(False)
        self.pushButton_others.setDefault(False)
        self.pushButton_others.setFlat(True)
        self.pushButton_others.setObjectName("pushButton_others")
        self.pushButton_all = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_all.setEnabled(True)
        self.pushButton_all.setGeometry(QtCore.QRect(40, 250, 30, 30))
        self.pushButton_all.setText("")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("icons/publishToolIcon/AllS5close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon18.addPixmap(QtGui.QPixmap("icons/publishToolIcon/AllS5Open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_all.setIcon(icon18)
        self.pushButton_all.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_all.setCheckable(True)
        self.pushButton_all.setAutoDefault(False)
        self.pushButton_all.setDefault(False)
        self.pushButton_all.setFlat(True)
        self.pushButton_all.setObjectName("pushButton_all")
        self.pushButton_shot = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_shot.setEnabled(True)
        self.pushButton_shot.setGeometry(QtCore.QRect(40, 300, 30, 30))
        self.pushButton_shot.setText("")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("icons/publishToolIcon/shotS5Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon19.addPixmap(QtGui.QPixmap("icons/publishToolIcon/shotS5Open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_shot.setIcon(icon19)
        self.pushButton_shot.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_shot.setCheckable(True)
        self.pushButton_shot.setAutoDefault(False)
        self.pushButton_shot.setDefault(False)
        self.pushButton_shot.setFlat(True)
        self.pushButton_shot.setObjectName("pushButton_shot")
        self.pushButton_processConcept = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_processConcept.setGeometry(QtCore.QRect(220, 70, 30, 30))
        self.pushButton_processConcept.setText("")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("icons/publishToolIcon/concept_3Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon20.addPixmap(QtGui.QPixmap("icons/publishToolIcon/concept3_open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_processConcept.setIcon(icon20)
        self.pushButton_processConcept.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_processConcept.setCheckable(True)
        self.pushButton_processConcept.setAutoDefault(False)
        self.pushButton_processConcept.setDefault(False)
        self.pushButton_processConcept.setFlat(True)
        self.pushButton_processConcept.setObjectName("pushButton_processConcept")
        self.pushButton_processModeling = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_processModeling.setEnabled(True)
        self.pushButton_processModeling.setGeometry(QtCore.QRect(220, 100, 30, 30))
        self.pushButton_processModeling.setText("")
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("icons/publishToolIcon/modeling_3Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon21.addPixmap(QtGui.QPixmap("icons/publishToolIcon/modeling_3Open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_processModeling.setIcon(icon21)
        self.pushButton_processModeling.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_processModeling.setCheckable(True)
        self.pushButton_processModeling.setAutoDefault(False)
        self.pushButton_processModeling.setDefault(False)
        self.pushButton_processModeling.setFlat(True)
        self.pushButton_processModeling.setObjectName("pushButton_processModeling")
        self.pushButton_processTexture = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_processTexture.setEnabled(True)
        self.pushButton_processTexture.setGeometry(QtCore.QRect(220, 130, 30, 30))
        self.pushButton_processTexture.setText("")
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("icons/publishToolIcon/texture_3Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon22.addPixmap(QtGui.QPixmap("icons/publishToolIcon/texture_3Open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_processTexture.setIcon(icon22)
        self.pushButton_processTexture.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_processTexture.setCheckable(True)
        self.pushButton_processTexture.setAutoDefault(False)
        self.pushButton_processTexture.setDefault(False)
        self.pushButton_processTexture.setFlat(True)
        self.pushButton_processTexture.setObjectName("pushButton_processTexture")
        self.pushButton_processRigging = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_processRigging.setEnabled(True)
        self.pushButton_processRigging.setGeometry(QtCore.QRect(220, 160, 30, 30))
        self.pushButton_processRigging.setText("")
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("icons/publishToolIcon/rigging_3Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon23.addPixmap(QtGui.QPixmap("icons/publishToolIcon/rigging_3Open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_processRigging.setIcon(icon23)
        self.pushButton_processRigging.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_processRigging.setCheckable(True)
        self.pushButton_processRigging.setAutoDefault(False)
        self.pushButton_processRigging.setDefault(False)
        self.pushButton_processRigging.setFlat(True)
        self.pushButton_processRigging.setObjectName("pushButton_processRigging")
        self.pushButton_processLayout = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_processLayout.setEnabled(True)
        self.pushButton_processLayout.setGeometry(QtCore.QRect(220, 220, 30, 30))
        self.pushButton_processLayout.setText("")
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap("icons/publishToolIcon/layout_3Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon24.addPixmap(QtGui.QPixmap("icons/publishToolIcon/layout_3Open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_processLayout.setIcon(icon24)
        self.pushButton_processLayout.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_processLayout.setCheckable(True)
        self.pushButton_processLayout.setAutoDefault(False)
        self.pushButton_processLayout.setDefault(False)
        self.pushButton_processLayout.setFlat(True)
        self.pushButton_processLayout.setObjectName("pushButton_processLayout")
        self.pushButton_processAnimation = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_processAnimation.setEnabled(True)
        self.pushButton_processAnimation.setGeometry(QtCore.QRect(220, 250, 30, 30))
        self.pushButton_processAnimation.setText("")
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap("icons/publishToolIcon/animation_3Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon25.addPixmap(QtGui.QPixmap("icons/publishToolIcon/animation_3Open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_processAnimation.setIcon(icon25)
        self.pushButton_processAnimation.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_processAnimation.setCheckable(True)
        self.pushButton_processAnimation.setAutoDefault(False)
        self.pushButton_processAnimation.setDefault(False)
        self.pushButton_processAnimation.setFlat(True)
        self.pushButton_processAnimation.setObjectName("pushButton_processAnimation")
        self.pushButton_processLighting = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_processLighting.setEnabled(True)
        self.pushButton_processLighting.setGeometry(QtCore.QRect(220, 280, 30, 30))
        self.pushButton_processLighting.setText("")
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap("icons/publishToolIcon/lighting_3Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon26.addPixmap(QtGui.QPixmap("icons/publishToolIcon/lighting_3Open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_processLighting.setIcon(icon26)
        self.pushButton_processLighting.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_processLighting.setCheckable(True)
        self.pushButton_processLighting.setAutoDefault(False)
        self.pushButton_processLighting.setDefault(False)
        self.pushButton_processLighting.setFlat(True)
        self.pushButton_processLighting.setObjectName("pushButton_processLighting")
        self.pushButton_processEffects = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_processEffects.setEnabled(True)
        self.pushButton_processEffects.setGeometry(QtCore.QRect(220, 310, 30, 30))
        self.pushButton_processEffects.setText("")
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap("icons/publishToolIcon/effect_3Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon27.addPixmap(QtGui.QPixmap("icons/publishToolIcon/effect_3Open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_processEffects.setIcon(icon27)
        self.pushButton_processEffects.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_processEffects.setCheckable(True)
        self.pushButton_processEffects.setAutoDefault(False)
        self.pushButton_processEffects.setDefault(False)
        self.pushButton_processEffects.setFlat(True)
        self.pushButton_processEffects.setObjectName("pushButton_processEffects")
        self.pushButton_processSimulation = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_processSimulation.setEnabled(True)
        self.pushButton_processSimulation.setGeometry(QtCore.QRect(220, 340, 30, 30))
        self.pushButton_processSimulation.setText("")
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap("icons/publishToolIcon/simulation_3Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon28.addPixmap(QtGui.QPixmap("icons/publishToolIcon/simulation_3Open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_processSimulation.setIcon(icon28)
        self.pushButton_processSimulation.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_processSimulation.setCheckable(True)
        self.pushButton_processSimulation.setAutoDefault(False)
        self.pushButton_processSimulation.setDefault(False)
        self.pushButton_processSimulation.setFlat(True)
        self.pushButton_processSimulation.setObjectName("pushButton_processSimulation")
        self.pushButton_processComp = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_processComp.setEnabled(True)
        self.pushButton_processComp.setGeometry(QtCore.QRect(220, 370, 30, 30))
        self.pushButton_processComp.setText("")
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap("icons/publishToolIcon/comp_3Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon29.addPixmap(QtGui.QPixmap("icons/publishToolIcon/comp_3Open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_processComp.setIcon(icon29)
        self.pushButton_processComp.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_processComp.setCheckable(True)
        self.pushButton_processComp.setAutoDefault(False)
        self.pushButton_processComp.setDefault(False)
        self.pushButton_processComp.setFlat(True)
        self.pushButton_processComp.setObjectName("pushButton_processComp")
        self.label_currentProj = QtWidgets.QLabel(self.tab_branch)
        self.label_currentProj.setGeometry(QtCore.QRect(450, 10, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_currentProj.setFont(font)
        self.label_currentProj.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_currentProj.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_currentProj.setObjectName("label_currentProj")
        self.lineEdit_currentProj = QtWidgets.QLineEdit(self.tab_branch)
        self.lineEdit_currentProj.setGeometry(QtCore.QRect(520, 10, 251, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.lineEdit_currentProj.setPalette(palette)
        self.lineEdit_currentProj.setReadOnly(True)
        self.lineEdit_currentProj.setObjectName("lineEdit_currentProj")
        self.comboBox_selectProj = QtWidgets.QComboBox(self.tab_branch)
        self.comboBox_selectProj.setGeometry(QtCore.QRect(70, 30, 351, 22))
        self.comboBox_selectProj.setObjectName("comboBox_selectProj")
        self.comboBox_selectProj.addItem("")
        self.comboBox_selectProj.addItem("")
        self.comboBox_selectProj.addItem("")
        self.label_selectProject = QtWidgets.QLabel(self.tab_branch)
        self.label_selectProject.setGeometry(QtCore.QRect(70, 10, 141, 20))
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
        self.tabWidget_branch.addTab(self.tab_branch, "")
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
        self.tabWidget_branch.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget_branch.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "project Name :", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "getProject", None, -1))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.item(0).setText(QtWidgets.QApplication.translate("MainWindow", "jack", None, -1))
        self.listWidget.item(1).setText(QtWidgets.QApplication.translate("MainWindow", "anna", None, -1))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "assets", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("MainWindow", "shot", None, -1))
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
        self.pushButton_26.setText(QtWidgets.QApplication.translate("MainWindow", "add", None, -1))
        __sortingEnabled = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        self.listWidget_3.item(0).setText(QtWidgets.QApplication.translate("MainWindow", "jack", None, -1))
        self.listWidget_3.item(1).setText(QtWidgets.QApplication.translate("MainWindow", "anna", None, -1))
        self.listWidget_3.setSortingEnabled(__sortingEnabled)
        self.tabWidget_branch.setTabText(self.tabWidget_branch.indexOf(self.tab_job_assemble), QtWidgets.QApplication.translate("MainWindow", "job Assemble", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Branch Name", None, -1))
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
        self.lineEdit_currentFileName.setText(QtWidgets.QApplication.translate("MainWindow", "SelectFile:", None, -1))
        self.label_fileDescription.setText(QtWidgets.QApplication.translate("MainWindow", "File description:", None, -1))
        self.label_fileData.setText(QtWidgets.QApplication.translate("MainWindow", "File Data", None, -1))
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
        self.checkBox_collectFile.setText(QtWidgets.QApplication.translate("MainWindow", "Collect File", None, -1))
        self.checkBox_errorCheck.setText(QtWidgets.QApplication.translate("MainWindow", "Error Check", None, -1))
        self.label_metaData.setText(QtWidgets.QApplication.translate("MainWindow", "Meta Data", None, -1))
        self.label_currentProj.setText(QtWidgets.QApplication.translate("MainWindow", "current WorkSpace", None, -1))
        self.comboBox_selectProj.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "a1", None, -1))
        self.comboBox_selectProj.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "a2", None, -1))
        self.comboBox_selectProj.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "a3", None, -1))
        self.label_selectProject.setText(QtWidgets.QApplication.translate("MainWindow", "select Project", None, -1))
        self.tabWidget_branch.setTabText(self.tabWidget_branch.indexOf(self.tab_branch), QtWidgets.QApplication.translate("MainWindow", "branch Edit", None, -1))
        self.label_optionPage_projDescription.setText(QtWidgets.QApplication.translate("MainWindow", "project Description:", None, -1))
        self.label_optionPage_showFileType.setText(QtWidgets.QApplication.translate("MainWindow", "show File Type:", None, -1))
        self.label_optionPage_tempB.setText(QtWidgets.QApplication.translate("MainWindow", "temp_B:", None, -1))
        self.label_optionPage_userPref.setText(QtWidgets.QApplication.translate("MainWindow", "User Pref:", None, -1))
        self.label_optionPage_User.setText(QtWidgets.QApplication.translate("MainWindow", "current User:", None, -1))
        self.label_optionPage_workProj.setText(QtWidgets.QApplication.translate("MainWindow", "working Project :", None, -1))
        self.label_optionPage_branchFileInfo.setText(QtWidgets.QApplication.translate("MainWindow", "branch File Info position:", None, -1))
        self.plainTextEdit_optionPage_showFileType.setPlainText(QtWidgets.QApplication.translate("MainWindow", "ma,mb,rib,ass,zip", None, -1))
        self.tabWidget_branch.setTabText(self.tabWidget_branch.indexOf(self.tab_2), QtWidgets.QApplication.translate("MainWindow", "option Edit", None, -1))




       ## self.tableWidget_FileList.verticalHeader().setDefaultSectionSize(28)#tableWidge verticalHeader space

       ## self.tableWidget_FileList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)   #add more control



 

        

class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #self.QTITEM.ACTION.connect(self.MODDEF)
        self.setupUi(self)
        

        #define project root
        #self.root = "C:/mayaProjs" #test in home
        self.root = "//mcd-server/art_3d_project"   # projects root in company
        
        
        #creat projects Info in self.root
        self.pushButton_setting.clicked.connect(self.doFromAdmin)
        
        
        

        #clear treeWidger_branches, all Clear
        #self.treeWidget_branches.clear()   #branch system
        #self.tableWidget_FileList.clear()  #branch system
        self.defineFont()
        #self.printOutProjectInfo()    #branch system
        
        self.branch_index = 0
        #self.assetsOnOffTable = [0,0,0,0,0,1,0]
        #self.clickAssetShotSelectButton()
        self.assetName  = "anna"
        self.branchDict={"0":{"master":{}}} 
        
        
        self.pushButton_reNewBranchDict.clicked.connect(self.checkPublishToolTempFolder)
        
        self.pushButton_createNewBranch.clicked.connect(self.createNewBranchCombo)


        self.pushButton_mergeToMaster.clicked.connect(self.getSavingFile)
        
        self.treeWidget_branches.itemClicked.connect(self.createFileTable)
        
        self.tableWidget_FileList.itemClicked.connect(self.printOutFileInfo)
        
        self.pushButton_editFileInfo.clicked.connect(self.addDescriptionToTextFile)
        
        self.pushButton_saveFile.clicked.connect(self.getSavingFile)
        
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


        #selectProject ComboBox
        self.comboBox_selectProj.currentIndexChanged.connect(self.selectWorkingProjectInGlobal)

        #test--------------------
        #self.pushButton_syncFile.clicked.connect(self.defineWorkingProjectAssemble)
        self.pushButton_publish.clicked.connect(self.test_processProjectGlobal)

        self.getCurrentLevelList = []
        self.initialItemBuild()
    
    def selectWorkingProjectInGlobal(self):
        #print "run select working project"
        
        self.project = self.comboBox_selectProj.currentText()
       # print self.project
        
        self.defineWorkingProjectAssemble()
        self.buildAssetsList()
        
        
        
    def buildAssetsList(self):
        print "build list from workingProjectAssemble description file"
        # 1.get data form dictionary , self.projectAssembleDescription
        # 2. self.projectAssembleDescription stored in self.projectAssembleDescriptionFile
        # 3. show all assets in list, defaut set button to click 'all' setAssetTypeSelect
        
        f= open(self.projectAssembleDescriptionFile, 'r')
        data = json.load(f)
        #print data
        #self.projectAssembleDescription = json.dumps(data, sort_keys=True , indent =4) 
        self.projectAssembleDescription = data
        #print self.projectAssembleDescription.keys()
       # print self.projectAssembleDescription['assets']
        assetTempList = []
        if self.setAssetTypeSelect == "all":
            for i in self.projectAssembleDescription['assets'].keys():
               # print i
                for j in self.projectAssembleDescription['assets'][i].keys():
                    assetTempList.append(j)
           # print assetTempList
            #build assets list
            listIndexCount = len(assetTempList)
            self.listWidget_assetProj.clear()
            for indexNum in range(0 ,listIndexCount):
               # print indexNum
                
                QtWidgets.QListWidgetItem(self.listWidget_assetProj)
                self.listWidget_assetProj.item(indexNum).setText(QtWidgets.QApplication.translate("MainWindow", "tempName", None, -1))
                self.listWidget_assetProj.item(indexNum).setText(assetTempList[indexNum])
            
        elif self.setAssetTypeSelect == "Character":
            for i in self.projectAssembleDescription['assets']['character'].keys():
                    assetTempList.append(i)
            #build assets list
            listIndexCount = len(assetTempList)
            self.listWidget_assetProj.clear()
            for indexNum in range(0 ,listIndexCount):
                #print indexNum
                
                QtWidgets.QListWidgetItem(self.listWidget_assetProj)
                self.listWidget_assetProj.item(indexNum).setText(QtWidgets.QApplication.translate("MainWindow", "tempName", None, -1))
                self.listWidget_assetProj.item(indexNum).setText(assetTempList[indexNum])
            
            
            
        
        

    def doFromAdmin(self):
        print self.root
        self.selectProj()
        self.saveProjectsInGlobalFile()        
        
        
        
        
        
        
    
    def test_processProjectGlobal(self):

        self.buildProjectComboBox()
    
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
        
    def buildProjectComboBox(self):
        #1. get info from projects description file.
        #2. build comboBox form info file.
        #1. 取得現有專案資料
        #2. 建立 comboBox
        
        ## get data from json file
        self.projectsGlobalFile = self.root + '/' + 'global' + '/' + 'allProjectDescription.json'
        #print self.projectsGlobalFile
        f = open(self.projectsGlobalFile)
        data = json.load(f)
        # print json.dumps(data, sort_keys=True , indent =4) 
        f.close
        
        items = data.keys()
        itemsTotalIndexNum = len(items)
       # print items
        #print itemsTotalIndexNum
        self.comboBox_selectProj.clear()
        for i in range(0,itemsTotalIndexNum):
            self.comboBox_selectProj.addItem("")
            self.comboBox_selectProj.setItemText(i, QtWidgets.QApplication.translate("MainWindow",'tmepName', None, -1))
            self.comboBox_selectProj.setItemText(i,items[i])
          #  print i
           # print items[i]
            
        #self.comboBox_selectProj.addItem("")
        #self.comboBox_selectProj.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "a1", None, -1))
        
        
       # dataName = open(fileName)
        #json.load(dataName)           
       ## f = json.load( self.projectsGlobalFile ) 
       # data = f.read
       # print data
        
    
    

    
    
    
    
    
    
    def defineWorkingProjectAssemble(self):
        # 1. 輸入 self.root,   
        # 1.2 check 專案下的folder是否存在, 創建 assets, shot, output, publish, QC, reference,global
        # 2. 輸入 執行的專案資料夾, self.project,
        # 3. 輸出 專案組成的 dictionary, self.projectAssembleDescription
        # 
        # 4. 輸出 寫入到 cache檔案, self.root / self.project / global / self.project + '_assembleDescription.json'
        #self.root = "//mcd-server/art_3d_project" #at company
        #get self.project
        #
        
        
        
        #default folder in self.project
        requestFolder= ['assets','shot','output','publish','QC','global','reference']
        #print requestFolder
        #check the request folder is exist in self.project ,and create folder
        
        for i in requestFolder:
            searchFolder = self.root + '/' + self.project +'/' + i
            if os.path.isdir(searchFolder) == True:
                pass
            else:
                os.mkdir(searchFolder)

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
        

        for assetItem in self.projectAssembleDescription['assets'].keys():    
            searchAssetFolder = assetsFolder +'/' + assetItem
           # print assetItem
           # print searchAssetFolder
            try:
                for assetClassItem in os.listdir(searchAssetFolder):
                    self.projectAssembleDescription['assets'][assetItem].update({assetClassItem:{}})
            except:
                pass

            
        try:
            for shotItem in os.listdir(shotFolder):
                #print shotItem
                self.projectAssembleDescription['shot'].update({shotItem:{}})
        except:
            pass
                

        self.projectAssembleDescriptionFile = self.root + '/' + self.project + '/' +'global'+ '/' + self.project + '_assembleDescription.json'

        f = open(self.projectAssembleDescriptionFile,'w')
        data = json.dumps(self.projectAssembleDescription, sort_keys=True , indent =4) 
        f.write(data)
        f.close
        
        
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
            os.mkdir(tempPath)
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
                
        print self.userPrefFileName 
        fileOpen = open(self.userPrefFileName,'w')
        fileOpen.write
        
        print "created %s"%self.userPrefFileName 
    
######-------------------------------store userPref End-------------------------------------------------------------------        
    
                
    def clickCharacterButton(self):
        "print select assetType , Character"
        self.clickAssetShotSelectButton()
        #self.assetsOnOffTable = [1,0,0,0,0,0,0]
        
                
        self.setAssetTypeSelect = "Character"
        self.isAsset = 1
        
        
        self.pushButton_character.setChecked(True)
        
        self.buildAssetsList()
    def clickVehicleButton(self):
        "print select assetType , Vehicle"
        self.clickAssetShotSelectButton()
        
        
                        
        self.setAssetTypeSelect = "Vehicle"
        self.isAsset = 1
        

        self.pushButton_vehicle.setChecked(True)

    def clickSetButton(self):
        "print select assetType , set"
        self.clickAssetShotSelectButton()
        
                        
        self.setAssetTypeSelect = "set"
        self.isAsset = 1
                
        

        self.pushButton_set.setChecked(True)

    def clickPropsButton(self):
        "print select assetType , props"
        self.clickAssetShotSelectButton()
        
        self.setAssetTypeSelect = "props"
        self.isAsset = 1
                
                
        

        self.pushButton_props.setChecked(True)

    def clickOthersButton(self):
        "print select assetType , others"
        self.clickAssetShotSelectButton()
        
        self.setAssetTypeSelect = "others"
        self.isAsset = 1
                        
        
        

        self.pushButton_others.setChecked(True)

    def clickAllButton(self):
        "print select assetType , All"
        self.clickAssetShotSelectButton()

        self.pushButton_all.setChecked(True)
        
        self.setAssetTypeSelect = "all"
        self.isAsset = 1

        self.buildAssetsList()
    def clickShotButton(self):
        "print select assetType , Shot"
        self.clickAssetShotSelectButton()

        self.setAssetTypeSelect = "Shot"
        self.isAsset = 0
                        
        


        self.pushButton_shot.setChecked(True)

        

        
    def clickAssetShotSelectButton(self):
        
        #self.assetsOnOffTable read on off
        self.pushButton_character.setChecked(False)
        self.pushButton_vehicle.setChecked(False)
        self.pushButton_set.setChecked(False)
        self.pushButton_props.setChecked(False)
        self.pushButton_others.setChecked(False)
        self.pushButton_all.setChecked(False)
        self.pushButton_shot.setChecked(False)
        
        
        
        
        
        
    def clear(self):
        
        self.tableWidget_FileList.clear()
        
    def printOutProjectInfo(self):
        # input project infomation, project root, name,asset name, shot name, isAsset Value
        print "get input info"
        self.root = "C:/mayaProjs"
       # self.root ="//mcd-server/art_3d_project"
        self.project = "3d_pipeline_test"
        self.assetClass ="character"
        self.assetNow = "shot_02"
        self.processNow ="lighting"
        self.isAsset = False
        self.currentUser = getpass.getuser()

        self.hostName = socket.gethostname()
        self.projectDescription()    
      
        self.plainTextEdit_optionPage_currentUser.setPlainText(self.currentUser + "@" +self.hostName)
       # print "workProject", self.workProject
       # print "project Structure",self.projectStructureName
       # print "Branch File Store",self.shotBranchFileStore
        #print "shot Root Dir",self.shotRootDir
       # print "Export brancg File Dir",self.branchFileStore
        
        self.checkMasterExist()

   
    def projectDescription(self):
        print self.isAsset
        
        #self.root 
        #self.project 
        #self.assetClass 
        #self.processNow
        self.assetName = "assets" + "/" + self.assetClass + "/" + self.assetNow
        self.shotName = "shot"+"/"+ self.assetNow
        
        
        self.projectGlobal = self.root + "/" + self.project + "/" +"global"
        
        #print self.shotProject
        
        #projectStructure.json  -- projectName_Structure.json
        self.projectStructureName = self.projectGlobal + "/" + self.project+"_struction.json"
        
        if self.isAsset == True:
        #assetBranchFileInfo.json  -- assetName_process.json
            self.assetBranchFileName = self.assetNow + "_" + self.processNow +".json"       #assetBranchFileStore FileName
            self.assetRootDir = self.projectGlobal + "/" + "assets"
            self.assetClassDir = self.assetRootDir + "/" + self.assetClass
            self.assetBranchFileDir = self.assetClassDir + "/"+ self.assetNow #assetBranchFileStore Folder
            self.assetBranchFileStore = self.assetBranchFileDir + "/" + self.assetBranchFileName    #export Path + fileName
            self.workProject = self.root + "/" + self.project + "/" + self.assetName + "/" + self.processNow

            if os.path.isdir(self.assetBranchFileDir) == True:
                pass
            else:
                os.mkdir(self.assetBranchFileDir)
                
            self.branchFileStore = self.assetBranchFileStore

       
            
        else:
        #shotBranchFileInfo.json  -- shotName_process.json
            self.shotBranchFileName = self.assetNow + "_" + self.processNow +".json"        #shotBranchFileStore FileName
            self.shotRootDir = self.projectGlobal + "/" + "shot"
            self.shotBranchFileDir = self.shotRootDir + "/"+ self.assetNow # shotBranchFileStore Folder
            self.shotBranchFileStore = self.shotBranchFileDir + "/" + self.shotBranchFileName    #export Path + fileName
            self.workProject = self.root + "/" + self.project + "/" + self.shotName + "/" + self.processNow

          #  
            if os.path.isdir(self.shotBranchFileDir) == True:
                pass
            else:
                os.mkdir(self.shotBranchFileDir)
                
            self.branchFileStore = self.shotBranchFileStore
                
                
       # try:
          #  os.mkdir(self.projectGlobal + "/" + self.assetNow)
       # except:
          #  pass
        self.plainTextEdit_optionPage_projDescription.setPlainText(self.projectStructureName)
        self.plainTextEdit_optionPage_workProj.setPlainText(self.workProject)
        self.plainTextEdit_optionPage_branchInfoPos.setPlainText(self.branchFileStore)
        


        
   

    def checkMasterExist(self):
        #---------1. check /scenes/master exist
        #.........2. check branchInfoFile exist, in global/assets(shot)/assetName(shotName)/assetName(shotName)_process.json,ex. shot_02_lighting.json
        
        print "check /scenes/master exist"
        print "check branchInfoFile exist"
        #get self.workProject, check master /scenes/master folder exist
        #get self.branchFileStore ,check the branchInfoFile ,json file exist
        print "workProject............:" , self.workProject 
        print "branchInfoFile.........:",self.branchFileStore
        masterFolder = self.workProject +'/'+'scenes'+ '/' + 'master'
        print "masterFolder",masterFolder
        print "master folder exist....:" ,os.path.isdir(masterFolder)
        print "branch Info File exist.:", os.path.isfile(self.branchFileStore)
        #timeNow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # .......1. check /scenes/master exist
        if os.path.isdir(masterFolder) == True:
            print "the /scense/master exist already"
        else:
            
            try:

                os.mkdir(masterFolder)
                print"the /scenes/master was built"
            except:
                pass
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



    def buildExistFileInfoTree(self):
        print "run buildExistFileInfoTree process         ------------start" 

        #update the json file begining
    

        
        #currentProject = "//mcd-server/art_3d_project/3d_pipeline_test/shot/shot_02/lighting/"    #test project
        print "self.workProject",self.workProject
        topLevelDirFileSearch = self.workProject +'/'+ "scenes"

        topLevelDirList = ['master']
        branchPreDict = {"0":{"master":{}}}        

        #build topLevelDir List------------------------------------------------------------------


        for dir,path,file in os.walk(topLevelDirFileSearch):

            allDir = dir.split(topLevelDirFileSearch)[1]

            try:

                if allDir.split("\\")[1] in topLevelDirList:
                    pass
                else:
                    topLevelDirList.append(allDir.split("\\")[1])
                
            except:
                pass



        for i in range(0,len(topLevelDirList)):
           # print i
            branchPreDict.update({str(i):{topLevelDirList[i]:{}}})

        #------analyze 2nd level dir and files-------------------
        #----------1.for i in branchPreDict.keys(): get search folder from branchPreDict dictionary, make sure index and branch name match
        #-------------2.for secLevelItem in os.listdir(secLevelDirSearch):, update 2nd level item into branchPreDict
        #----------------3 for thirdLevelItem in os.listdir(thirdLevelDirSearch):, update 3rd level item into branchPreDict
        #--------------------4. for fourLevelItem in os.listdir(fourLevelDirSearch): update 4th level item into branchPreDict ,only folder
        #--------------os.path.isdir(path),check the path is folder or file
        for i in branchPreDict.keys():
            secLevelDirSearch = topLevelDirFileSearch+ '/' + branchPreDict[i].keys()[0]  
            
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
        print "--------------",self.branchFileStore

        with open(self.branchFileStore, 'w') as f:
            f.write(exportDate)
                
        
        
        
        print "run buildExistFileInfoTree process         ------------End" 


        
    def initialItemBuild(self):
        
        #initial self.branchDict dictionary
        #self.root = "C:/mayaProjs"
        self.branchDict={"0":{"master":{}}}    #default Master Item
        
        #self.buildExistFileInfoTree()        #branch system
        #self.buildTreeFromExistFileData()      #branch system
        
        
        #initial button
        self.test_processProjectGlobal()
        self.clickAllButton()
        
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
    #---------------Load Exist Branch Data From Dictionary Start-------------------------------------------------------------------------------------------------------
    def buildTreeFromExistFileData(self):
        #--------build Tree from Exist folders and files--------------------
        #----------1. define default ,master, that should be exist------------
        #----------2.get file info tree
        #----------3.for topLevelIndex in range(1,topLevelIndexCount): build top Level items 
        #----------4.for topLevelIndex in range(0,topLevelIndexCount): build sec Level items 
        #----------5. build 2nd level item in treeWidget    
        #----------6. build 3rd level item in treeWidget    

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
        for topLevelIndex in range(1,topLevelIndexCount):
            QtWidgets.QTreeWidgetItem(self.treeWidget_branches).setForeground(0,self.brushLevelTwo)
            self.treeWidget_branches.topLevelItem(topLevelIndex).setText(0, QtWidgets.QApplication.translate("MainWindow", "master", None, -1))
            self.treeWidget_branches.topLevelItem(topLevelIndex).setText(0,self.branchPreDict[str(topLevelIndex)].keys()[0])
            self.treeWidget_branches.topLevelItem(topLevelIndex).setFont(0,self.fontLevelTwo)

        #4.for topLevelIndex in range(0,topLevelIndexCount): build sec Level items 
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
        self.fontLevelOne.setPointSize((fontSizeAdj+4))
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
        print" run createFileTable function start..................."
        self.itemSelect =  self.treeWidget_branches.currentItem().text(0)

        self.getFilesInfoFormJson()
        self.tableWidget_FileList.clear()

                             
        tableIndex = sorted(self.fileInfoDict.keys())  #string
        
        verIndex = sorted(self.fileInfoDict.keys(), reverse = True )        
        print "verIndex",verIndex
        print "createFileTable check point 01"
        if len(tableIndex) > 0:
            for i in range(0,len(tableIndex)):
               # print i,verIndex[i],self.fileInfoDict[str(verIndex[i])]  #i indexNum,verIndex[i]--->version,self.fileInfoDict[str(verIndex[i])--->fileName
                itemVer = "v"+verIndex[i]
                #print itemVer

                self.tableItem = QtWidgets.QTableWidgetItem()
                self.tableWidget_FileList.setItem(i, 0, self.tableItem)
                self.tableItem = QtWidgets.QTableWidgetItem()
                self.tableWidget_FileList.setItem(i, 1, self.tableItem)
                self.tableItem = QtWidgets.QTableWidgetItem()
                self.tableWidget_FileList.setItem(i, 2, self.tableItem)
               # self.tableWidget_FileList.setItem(i, 3, self.tableItem)
               # print self.fileInfoDict[str(verIndex[i])]# ,type(self.tableWidget_FileList.setItem(i, 0, self.tableItem)[2])

                
                itemUser = self.currentUser
                itemDateTemp = datetime.datetime.fromtimestamp(float(self.fileInfoDict[str(verIndex[i])][2]))
                itemDate = str(itemDateTemp.date())+' '+(str(itemDateTemp.time())).split('.')[0]
                itemFileName = self.fileInfoDict[str(verIndex[i])][0]
                self.tableWidget_FileList.item(i, 0).setText(QtWidgets.QApplication.translate("MainWindow", itemVer, None, -1))


                self.tableWidget_FileList.item(i, 1).setText(QtWidgets.QApplication.translate("MainWindow", itemUser, None, -1))
                self.tableWidget_FileList.item(i, 2).setText(QtWidgets.QApplication.translate("MainWindow", itemDate, None, -1))
               # self.tableWidget_FileList.item(i, 3).setText(QtWidgets.QApplication.translate("MainWindow", itemFileName, None, -1))

              #  self.textBrowser_BranchFileInfo.setText("sssssssssssss")
                print itemFileName
        else:
            pass
            
        self.currentSelectedFile = itemFileName
        print" run createFileTable function End..................."

    #--------------------------get linking fileInfo json----------------------------start----------------------------
    
    def getLinkingFileInfoText(self):
        # 1. define asset/shot description file location.
        # 2. create an empty text file in folder
        
        print "getFileInfo from %s"%self.lineEdit_currentFileName.text()
        if self.isAsset == True:
            fileInfoLocation = self.root +'/'+ self.project +'/' + 'global' + '/' +"assets"+ '/'+ self.assetNow 
            
        else:
            fileInfoLocation = self.root +'/'+ self.project +'/' + 'global' + '/' +"shot"+ '/'+ self.assetNow 
            
    
        fileInfoName = self.lineEdit_currentFileName.text().split('.')[0] +'.txt'  #define the file description Text file name

        if os.path.isdir(fileInfoLocation) == False:
            os.mkdir(fileInfoLocation)
        else:
            pass
            
        self.fullFileInfoName = fileInfoLocation + '/' + fileInfoName
        

        
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
        f = open(self.fullFileInfoName,'r+')
        dataEdit = self.plainTextEdit_BranchFileInfo.toPlainText()
        f.write(dataEdit)
        f.close
        

        



    def getSavingFile(self):
        # print self.workProject
        
        #print self.getFilesInfoFormJson()
        #print self.filesStoreBranchFolder  #, export branch folder
        # print "self.fileInfoDict" ,self.fileInfoDict
        #self.root ="//mcd-server/art_3d_project"
        #self.project = "3d_pipeline_test"
        #self.assetClass ="character"
        #self.assetNow = "shot_02"
        #self.processNow ="lighting" 
       # print self.fileInfoDict.keys()       

        
        currentBranch = self.itemSelect 
        #print currentBranch
        

        #-------------define project initial
        self.projectInitial = ""
        for par in self.project.split('_'):
            self.projectInitial = self.projectInitial + par[0]
            
       
        #-----------finding last version, illegal
        tempVerList= []
        if len(self.fileInfoDict.keys()) >0:

            for verKey in self.fileInfoDict.keys():
               # print verKey , self.fileInfoDict[verKey][0]
                existVerNum = self.fileInfoDict[verKey][0].split('%s'%self.itemSelect)[1].split('_')[1].split('v')[1]
                tempVerList.append(existVerNum)
                
                
            
            tempNextVerNum = int(sorted(tempVerList)[-1])+1
            nextVerNum = 'v'+'%03d'%tempNextVerNum
            
        else:
            
            nextVerNum= 'v001'
            
        
        #------------define savingFileName in branch
        getSavingName = self.projectInitial + '_' + self.assetNow +'_'+ self.processNow[0:3] + '_' + currentBranch +'_'+ nextVerNum +'_'+self.currentUser +'.mb'
        
        self.longSavingName = self.filesStoreBranchFolder + '/' +getSavingName
        
        print self.longSavingName
        
        
        #cmds.file(self.longSavingName,rename=True)

        cmds.file( rename=self.longSavingName )
        cmds.file( save=True, type='mayaBinary' )
        
        #self.initialItemBuild()
        #self.getFilesInfoFormJson()
        self.buildExistFileInfoTree()
        self.createFileTable()
        self.getLinkingFileInfoText()   # create file description file fileName.txt in global folder
        print "reNew file Table"
    

    
    def readFileInof(self):
        
        printText = self.plainTextEdit_BranchFileInfo.toPlainText()
        
        print printText
        
    
    
    

    def getFilesInfoFormJson(self):
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
        
        fileTypeFillet = self.plainTextEdit_optionPage_showFileType.toPlainText().split(',')
        print fileTypeFillet
        print "run getFilesInfoFormJson starting......................."
        print "finding files in the branch"
        #self.itemSelect =  self.treeWidget_branches.currentItem().text(0)
        print self.branchFileStore
        with open(self.branchFileStore, 'r') as f:
            self.branchPreDict = json.load(f)
            

        print "self.branchPreDict.keys()",self.branchPreDict.keys()
        topLevelItemCount = len(self.branchPreDict.keys())    

        self.getExistBranchDict()

        self.getSelectItemLevel()
        
        
        tempTimeFileCompareDict = {}  # temp dictionary , that store file modify datetime and file name
        
        print "self.branchPreDict", self.branchPreDict
       # t = os.path.getmtime(fileName)
        print "self.fullItemIndex",self.fullItemIndex

    # datetime.datetime.fromtimestamp(t)
       
        if len(self.fullItemIndex) == 1:
            

            print self.itemSelect
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
            print "getFilesInfoFormJson check point C"

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
            self.fileInfoDict.update({"%03d"%indexNum:[tempTimeFileCompareDict[serNum].split('/')[-1],self.currentUser,serNum]})




        
        print "run getFilesInfoFormJson End......................."
        print self.fileInfoDict
        print "self.branchFilesInListDict" ,self.branchFilesInListDict
        print tempTimeFileCompareDict
      
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
        print data
        load = ""
        for line in data:
            print line
            load = load + line
            
        print load
        self.plainTextEdit_BranchFileInfo.setPlainText(load)
        
        
    

 #-----------------print out file info in textBrowser function End-------------------------------------------------------------------     

    def getChildIndexCount(self):
        
        itemSelect = self.treeWidget_branches.currentItem()
        print itemSelect.text(0)

       # self.treeWidget_branches.current

    def createBranchDict(self):            #push button
        print "create New Branch"
        #self.newBranch = self.lineEdit_branchName.text()
        self.getNewBranchName()
        print self.newBranch
        
        self.getBranchTopFromTreeList()    # ------------1
   #     print self.treeWidget_branches.currentIndex().row()


    def getBranchTopFromTreeListB(self): #---------1
        print "ggggggggg"
        print self.treeWidget_branches.topLevelItemCount()
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
                            
                            
      #  print self.depth        

        self.findParentTopLevelItem(self.depth)
        
        
        
        
        
    #----------find the topLevelItem, with parent from selected Item, and get the all level index---------------------------------------------------------------------------------
    #----------build all level index into self.fullItemIndex,<list>
    
    def findParentTopLevelItem(self,depth):
        

        
        selectItem = self.treeWidget_branches.currentItem().text(0)
        
        #topLayerItemDict
       # print selectItem

        ##finding top Level Item topLevelItem(topItemLayerIndex)
        if self.depth == 0:
          #  print "top level item"
            topLevelItemIndex = self.topLayerItemDict[selectItem]
            
           # print "selectItem          :",selectItem
           # print "topLevelItem  :",selectItem
          #  print "topLevelItemIndex   :",topLevelItemIndex  
            
            self.fullItemIndex = [topLevelItemIndex]


           
           
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
           # print "thirdLevelItemIndex :",thirdLevelItemIndex
            
            self.fullItemIndex = [topLevelItemIndex,secLevelItemIndex,thirdLevelItemIndex]
            
    

        
    def createNewBranchCombo(self):  # creat New Branch Test  

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
            

                        
                        
        except:
            pass
        self.initialItemBuild()   #reNew treeWidget

                
                
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
        print os.path.isdir(createTopLayerFoder)
        if os.path.isdir(createTopLayerFoder) == True:
            print "already has "+"%s"%createTopLayerFoder + " folder"
            
        else:
            os.mkdir(createTopLayerFoder)
            
                
        print createTopLayerFoder
        
        #   update self.branchDict, the dictionary of all branches   
    
        # topLevelItemCount = len(self.branchDict.keys())
        
        # self.branchDict.update({str(topLevelItemCount):{self.newBranch:{}}})
                          


        

    #   update assetBranchFileInfo.json
  
       # self.getFilesInfoFormJson()           #reNew jsonFile and dirctionary
 
        print "......createNewBranchTopLevel function End............."
        
        
        
        
        
        
        
        
        
    
    # create New Branch on Child Level ----------------------------------------------------------------------------------------------------------------------
    def createNewBranchChildLevel(self): 
     #   print"ggg"
        print len(self.fullItemIndex)    
        print self.fullItemIndex 
       # self.getExistBranchDict()
        itemSelect = self.treeWidget_branches.currentItem().text(0)
        #self.newBranch = self.lineEdit_branchName.text()
        self.getNewBranchName()
        print self.newBranch

        topLevelIndex = int(self.fullItemIndex[0])
        
        try:                     #get second Level index, because,it,may not exist, used try
            secondLevelIndex = int(self.fullItemIndex[1])
        except:
            pass
        


    
        if len(self.fullItemIndex) == 1:     # create 2nd Level Item under select item
            print "Create level 2 branch"

            existLevelCount = len(self.branchDict[str(self.fullItemIndex[0])][itemSelect].keys())   # = child,secLevelIndex
            print existLevelCount
            secItemList = self.branchDict[str(self.fullItemIndex[0])][itemSelect].keys()
            print secItemList

            print "topLevelIndex",topLevelIndex

            if self.newBranch in secItemList:
                print
                print "Change New Branch Name"
                pass
                
                
            else:
                print "build 2nd level item"
                pass
                
         
                try:
                    # addChild sanple:       QtWidgets.QTreeWidgetItem(self.treeWidget_branches.topLevelItem(0)).addChild(0)
                    
                   

                    print 'topLevelIndex, existLevelCount',topLevelIndex, existLevelCount
                    
                    
                    print "create New 2nd Item"
                    QtWidgets.QTreeWidgetItem(self.treeWidget_branches.topLevelItem(topLevelIndex)).setForeground(0,self.brushLevelThree)  #build new item from index

                    self.treeWidget_branches.topLevelItem(topLevelIndex).child(existLevelCount).setFont(0,self.fontLevelThree)
    


                except:
                    #pass
                
                    print "change Name"
                    print topLevelIndex, existLevelCount
                    
            self.treeWidget_branches.topLevelItem(topLevelIndex).child(existLevelCount).setText(0,self.newBranch)   #named the newItem , from typeIn line edit
            # create folder
            createTopLayerFoder = self.workProject + '/' +'scenes'+ '/' + itemSelect +'/' + self.newBranch
            print createTopLayerFoder
            print os.path.isdir(createTopLayerFoder)
            if os.path.isdir(createTopLayerFoder) == True:
                print "already has %s folder"%createTopLayerFoder
            else:
                print "create %s folder"%createTopLayerFoder
                os.mkdir(createTopLayerFoder)
            




        elif len(self.fullItemIndex) == 2: # create 2nd Level Item under select item
            print "Create level 3 branch"
            print self.fullItemIndex
            
            thirdItemList = self.branchDict[str(self.fullItemIndex[0])][self.branchDict[str(self.fullItemIndex[0])].keys()[0]][itemSelect].keys()
            print thirdItemList
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
            print createTopLayerFoder
            print os.path.isdir(createTopLayerFoder)
            if os.path.isdir(createTopLayerFoder) == True:
                print "already has %s folder"%createTopLayerFoder
            else:
                print "create %s folder"%createTopLayerFoder
                os.mkdir(createTopLayerFoder)
            



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
        
        self.newBranch = self.lineEdit_branchName.text()
        
        if self.newBranch == "master":
            print "change other name, not master"
            pass
            
        else:
            pass

        
        
        
        
        
        
        
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
        
        
        
        
##    build tree list , store in dictionary
        
    def getExistBranchDict(self):
        
        
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
        self.exportBranchJsonFile()    #export dictionary to json file
        
       # print self.topLayerItemList
       # print self.topLayerItemDict
       # print self.secLayerItemDict
       # print self.thirdLayerItemDict
        
        
        

        
        
            
    def exportBranchJsonFile(self):  
        
          
        formatedBranchDict = json.dumps(self.branchDict, sort_keys=True , indent =4)  
               
        branchDictFile = "c:/temp/"+"%s"%self.assetName + "_branchDictFile.json"
        
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


 
 