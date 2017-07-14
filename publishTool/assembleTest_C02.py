# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha.DESKTOP-1S1STEK/Documents/GitHub/mayaTool/publishTool/assembleTest_B01.ui'
#
# Created: Thu Jul 06 16:28:26 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


import json
import os
from pprint import pprint


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 895)
        MainWindow.setMinimumSize(QtCore.QSize(650, 0))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_P3_largeIcon = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_P3_largeIcon.setGeometry(QtCore.QRect(320, 30, 61, 36))
        self.pushButton_P3_largeIcon.setCheckable(True)
        self.pushButton_P3_largeIcon.setObjectName("pushButton_P3_largeIcon")
        self.pushButton_P3_MidIcon = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_P3_MidIcon.setGeometry(QtCore.QRect(400, 30, 61, 36))
        self.pushButton_P3_MidIcon.setCheckable(True)
        self.pushButton_P3_MidIcon.setObjectName("pushButton_P3_MidIcon")
        self.pushButton_P3_smallIcon = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_P3_smallIcon.setGeometry(QtCore.QRect(480, 30, 61, 36))
        self.pushButton_P3_smallIcon.setCheckable(True)
        self.pushButton_P3_smallIcon.setObjectName("pushButton_P3_smallIcon")
        self.pushButton_P3_text = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_P3_text.setGeometry(QtCore.QRect(560, 30, 61, 36))
        self.pushButton_P3_text.setCheckable(True)
        self.pushButton_P3_text.setObjectName("pushButton_P3_text")
        self.frame_15 = QtWidgets.QFrame(self.centralwidget)
        self.frame_15.setGeometry(QtCore.QRect(5, 110, 636, 746))
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
        self.treeWidget_sceneAssembleTree = QtWidgets.QTreeWidget(self.frame_15)
        self.treeWidget_sceneAssembleTree.setGeometry(QtCore.QRect(5, 50, 201, 466))
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
        self.tableWidget_AssetItemList = QtWidgets.QTableWidget(self.frame_15)
        self.tableWidget_AssetItemList.setGeometry(QtCore.QRect(210, 50, 261, 466))
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
        self.treeWidget_inputOption = QtWidgets.QTreeWidget(self.frame_15)
        self.treeWidget_inputOption.setGeometry(QtCore.QRect(475, 50, 156, 246))
        self.treeWidget_inputOption.setRootIsDecorated(True)
        self.treeWidget_inputOption.setObjectName("treeWidget_inputOption")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_inputOption)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_inputOption)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_inputOption)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_inputOption)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_inputOption)
        self.treeWidget_inputOption.header().setVisible(False)
        self.treeWidget_inputOption.header().setMinimumSectionSize(25)
        self.plainTextEdit_assetMetaData = QtWidgets.QPlainTextEdit(self.frame_15)
        self.plainTextEdit_assetMetaData.setGeometry(QtCore.QRect(210, 525, 261, 216))
        self.plainTextEdit_assetMetaData.setObjectName("plainTextEdit_assetMetaData")
        self.frame_7 = QtWidgets.QFrame(self.frame_15)
        self.frame_7.setGeometry(QtCore.QRect(5, 525, 200, 214))
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
        self.label_showImage_2.setGeometry(QtCore.QRect(5, 7, 196, 185))
        self.label_showImage_2.setText("")
        self.label_showImage_2.setPixmap(QtGui.QPixmap("icons/publishToolIcon/picture-01-150.png"))
        self.label_showImage_2.setObjectName("label_showImage_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.pushButton_P3_largeIcon.setText(QtWidgets.QApplication.translate("MainWindow", "Large", None, -1))
        self.pushButton_P3_MidIcon.setText(QtWidgets.QApplication.translate("MainWindow", "mid", None, -1))
        self.pushButton_P3_smallIcon.setText(QtWidgets.QApplication.translate("MainWindow", "Small", None, -1))
        self.pushButton_P3_text.setText(QtWidgets.QApplication.translate("MainWindow", "Text", None, -1))
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
        self.treeWidget_inputOption.headerItem().setText(0, QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        __sortingEnabled = self.treeWidget_inputOption.isSortingEnabled()
        self.treeWidget_inputOption.setSortingEnabled(False)
        self.treeWidget_inputOption.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "Maya File", None, -1))
        self.treeWidget_inputOption.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "RibArchive", None, -1))
        self.treeWidget_inputOption.topLevelItem(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "GpuArchive", None, -1))
        self.treeWidget_inputOption.topLevelItem(3).setText(0, QtWidgets.QApplication.translate("MainWindow", "Shader", None, -1))
        self.treeWidget_inputOption.topLevelItem(4).setText(0, QtWidgets.QApplication.translate("MainWindow", "Texture", None, -1))
        self.treeWidget_inputOption.setSortingEnabled(__sortingEnabled)
            







class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)

        self.setupUi(self)

        self.pushButton_P3_largeIcon.clicked.connect(self.setLargeAssetIcon)
        self.pushButton_P3_MidIcon.clicked.connect(self.setMidAssetIcon)
        self.pushButton_P3_smallIcon.clicked.connect(self.setSmallAssetIcon)
        self.pushButton_P3_text.clicked.connect(self.setTextAsset)
        self.tableWidget_AssetItemList.itemClicked.connect(self.showAssetMetaDataFromSelect)
        self.itemDict ={}

        self.loadPublishedData()#('character','texture')
       # self.itemDict = {'item01':'a1','item02':'b1','item03':'c1','item04':'D1','item05':'E1','item06':'f1','item07':'g1','item08':'h1','item09':'i9'}
        
        self.totalItemCount = len(self.itemDict)
        #self.initialTableWidgetAssetList()
        #print self.itemDict.keys()
    def showAssetMetaDataFromSelect(self):
        print 'showAssetMetaDataFromSelect start'
        print self.tableWidget_AssetItemList.currentItem().text()
        
        
        
    def loadPublishedDataB(self,assetClass,processType):
        
        allAssetClass = ['character','vehicle','set','prop','other']
        allProcesType = ['layout','animation','lighting','effect','simulation']
       # file = '//mcd-server/art_3d_project/ani_pop_v01_cf/publish/global/ani_pop_v01_cf_publishAnnonce.json'
        
        file = '//mcd-server/art_3d_project/ocean_world_2016_cf/publish/global/ocean_world_2016_cf_publishAnnonce.json'
        with open(file) as data_file:    
            data = json.load(data_file)
            
        for i in data['assets'][assetClass].keys():
            self.itemDict.update({i.split('.')[0]:{}})

            try:
                linkingData = data['assets'][assetClass][i][processType]['state']
                self.itemDict[i.split('.')[0]].update(linkingData)

            except:
                pass
                
    def loadPublishedData(self):
        
        file = '//mcd-server/art_3d_project/ocean_world_2016_cf/publish/global/ocean_world_2016_cf_publishAnnonce.json'
        with open(file) as data_file:    
            data = json.load(data_file)
            
        allAssetClass = ['character','vehicle','set','prop','other']
        allProcesType = ['layout','animation','lighting','effects','simulation']



        allItemDict = {}
        assetTempDict ={}
        shotTempDict = {}

        for i in allAssetClass:
            for j in data['assets'][i].keys():
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
        allItemDict.update(shotTempDict)

        self.itemDict = allItemDict
        print self.itemDict

     
    def setLargeAssetIcon(self):
        
        
        print 'setLargeAssetIcon'
        self.tableWidget_AssetItemList.clear()
        
        self.pushButton_P3_largeIcon.setChecked(True) 
        self.pushButton_P3_MidIcon.setChecked(False) 
        self.pushButton_P3_smallIcon.setChecked(False) 
        self.pushButton_P3_text.setChecked(False) 
        
        if self.totalItemCount%2 == 0:
            setRow = ((self.totalItemCount / 2) *2) +1
        else: 
            setRow = ((self.totalItemCount / 2) *2) +2
            
        print setRow
        
        #setRow = self.totalItemCount / 2 *2 +2
        
        
        self.tableWidget_AssetItemList.setColumnCount(2)
        self.tableWidget_AssetItemList.setRowCount(setRow)
              
        self.tableWidget_AssetItemList.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget_AssetItemList.verticalHeader().setDefaultSectionSize(120)
        iconFile = QtGui.QIcon("C:/Program Files/Autodesk/Maya2017/icons/publishToolIcon/animation.png")
        tableItemIndex={}
        
        for column in range(0,2): #set icon 
            for row in range(0,setRow,2):

                self.createTableItem(column,row,iconFile,120)

                
        for column in range(0,2):
            for row in range(1,setRow,2):
                self.setTableItemText(column,row)
      
        self.storeItemDateInDict (2)  # create Item Dict

                
    def storeItemDateInDict(self,cloumnCount):
        infoSearchList = ['fileName','fileIcon','gpuCache','ribArchive','user','publishTime','metaData']
        rowCount = 0
        self.tableItemListInfoDict= {}
        for i in range(0,self.totalItemCount ):
            self.tempInfoDictPreItem = {}

            if cloumnCount == 1:
                column = 0
                row = i
                
            else:
                column = i % cloumnCount
            
                row = i/cloumnCount *2
            
            tempKey = str(column) +'_._'+ str(row)
            item = self.itemDict.keys()[i]
            tempItemList = {}
            for j in infoSearchList:
                try:
                    secondItem = self.itemDict[self.itemDict.keys()[i]][j]
                except:
                    secondItem = {}
                tempItemList.update({j:secondItem})
                
            self.tableItemListInfoDict.update({tempKey:{item:tempItemList}})



        print self.tableItemListInfoDict
        
        self.setItemText(cloumnCount)
        self.setItemIcon()
        
    def setMidAssetIcon(self):
        print 'setMidAssetIcon'
        self.pushButton_P3_largeIcon.setChecked(False) 
        self.pushButton_P3_MidIcon.setChecked(True) 
        self.pushButton_P3_smallIcon.setChecked(False) 
        self.pushButton_P3_text.setChecked(False) 
        
        if self.totalItemCount%3 == 0:
            setRow = ((self.totalItemCount / 3) *2) +1
        else: 
            setRow = ((self.totalItemCount / 3) *2) +2
            
        print setRow
        
        
        self.tableWidget_AssetItemList.setColumnCount(3)
        self.tableWidget_AssetItemList.setRowCount(setRow)
              
        self.tableWidget_AssetItemList.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget_AssetItemList.verticalHeader().setDefaultSectionSize(80)
        iconFile = QtGui.QIcon("C:/Program Files/Autodesk/Maya2017/icons/publishToolIcon/animation.png")
        
        for column in range(0,3): #set icon setItemText
            for row in range(0,setRow,2):
                print row
                self.createTableItem(column,row,iconFile,80)
                
        for column in range(0,3):
            for row in range(1,setRow,2):
             #   print row
                self.setTableItemText(column,row)
                
        self.storeItemDateInDict (3)
    def setSmallAssetIcon(self):
        print 'setSmallAssetIcon'
        self.pushButton_P3_largeIcon.setChecked(False) 
        self.pushButton_P3_MidIcon.setChecked(False) 
        self.pushButton_P3_smallIcon.setChecked(True) 
        self.pushButton_P3_text.setChecked(False)  
        if self.totalItemCount%4 == 0:
            setRow = ((self.totalItemCount / 4) *2) +1
        else: 
            setRow = ((self.totalItemCount / 4) *2) +2
            
        print setRow
        
        
        self.tableWidget_AssetItemList.setColumnCount(4)
        self.tableWidget_AssetItemList.setRowCount(setRow)
              
        self.tableWidget_AssetItemList.horizontalHeader().setDefaultSectionSize(60)
        self.tableWidget_AssetItemList.verticalHeader().setDefaultSectionSize(60)
        iconFile = QtGui.QIcon("C:/Program Files/Autodesk/Maya2017/icons/publishToolIcon/animation.png")
        
        for column in range(0,4): #set icon 
            for row in range(0,setRow,2):
                print row
                self.createTableItem(column,row,iconFile,60)
                
        for column in range(0,4):
            for row in range(1,setRow,2):
             #   print row
                self.setTableItemText(column,row)
        self.storeItemDateInDict (4)
        
    def setTextAsset(self):
        print 'setTextAsset~~'
        self.pushButton_P3_largeIcon.setChecked(False) 
        self.pushButton_P3_MidIcon.setChecked(False) 
        self.pushButton_P3_smallIcon.setChecked(False) 
        self.pushButton_P3_text.setChecked(True) 
        setRow = self.totalItemCount #+ 1
        self.tableWidget_AssetItemList.setColumnCount(1)
        self.tableWidget_AssetItemList.setRowCount(setRow)  
       # iconFile = QtGui.QIcon("C:/Program Files/Autodesk/Maya2017/icons/publishToolIcon/animation.png")

        self.tableWidget_AssetItemList.horizontalHeader().setDefaultSectionSize(300)

        for row in range(0, setRow):
            print row
            self.setTableItemText(0,row)
        self.storeItemDateInDict (1)

        
                
        
        
        
        
        
        
        
    
    def setItemText(self,cloumnCount):
        #print self.tableItemListInfoDict.keys()
        #print 'cloumnCount',cloumnCount
        for i in self.tableItemListInfoDict.keys():
            if cloumnCount == 1:
                row = int(i.split('_._')[1])
                column = 0
            else:
                row = int(i.split('_._')[1])+1
                column = int(i.split('_._')[0])
            itemName = str(self.tableItemListInfoDict[i].keys()[0])
            print itemName
            print row ,column

            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_AssetItemList.setItem(row, column, item)
            self.tableWidget_AssetItemList.item(row, column).setText(QtWidgets.QApplication.translate("MainWindow",'aaa', None,-1))
            self.tableWidget_AssetItemList.item(row, column).setText(QtWidgets.QApplication.translate("MainWindow",itemName, None,-1))
            
    
        
        
        
        
                                    
        
    def initialTableWidgetAssetList(self):
        self.tableWidget_AssetItemList.clear()
        #self.tableWidget_AssetItemList.setRowCount(2)
        #self.tableWidget_AssetItemList.setColumnCount(2)

        self.tableWidget_AssetItemList.setColumnCount(3)
        self.tableWidget_AssetItemList.setRowCount(4)
      
        self.tableWidget_AssetItemList.horizontalHeader().setDefaultSectionSize(60)
        self.tableWidget_AssetItemList.verticalHeader().setDefaultSectionSize(60)


    def createTableItem(self,column,row,iconFile,iconSize):

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_AssetItemList.setItem(row, column, item)
        self.tableWidget_AssetItemList.item(row, column).setText(QtWidgets.QApplication.translate("MainWindow", "ItemIconHere", None,-1))

        self.tableWidget_AssetItemList.item(row, column).setIcon(iconFile)
        self.tableWidget_AssetItemList.setIconSize(QtCore.QSize(iconSize,iconSize))

        
    def createItemB(self,column,row,iconFile):
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
        item = QtWidgets.QTableWidgetItem()
       # textRow = row+1
        self.tableWidget_AssetItemList.setRowHeight(row , 20) #set text row height
        self.tableWidget_AssetItemList.setItem(row, column, item)
        self.tableWidget_AssetItemList.item(row, column).setText(QtWidgets.QApplication.translate("MainWindow", "ItemName", None,-1))
        #item.setTextAlignment(-20)

      #  self.tableWidget.setRowHeight(1 , 20)  
      
      
    def setItemIcon(self):
        print 'setItemIcon start'
        for i in self.tableItemListInfoDict.keys():
            row = int(i.split('_._')[1])
            column = int(i.split('_._')[0])
           # print i
            if len(self.tableItemListInfoDict[i][self.tableItemListInfoDict[i].keys()[0]]['fileIcon']) >0:
                iconFile = QtGui.QIcon(self.tableItemListInfoDict[i][self.tableItemListInfoDict[i].keys()[0]]['fileIcon'])#.keys()
            else:
                iconFile =QtGui.QIcon('//Art-1405260002/D/assets/scripts/maya_scripts/icons/publishToolIcon/emoji-32-512.png')
                #iconFile = QtGui.QIcon("C:/Program Files/Autodesk/Maya2017/icons/publishToolIcon/animation.png")
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_AssetItemList.setItem(row, column, item)
            #self.tableWidget_AssetItemList.item(row, column).setText(QtWidgets.QApplication.translate("MainWindow", "ItemIcon", None,-1))
            self.tableWidget_AssetItemList.item(row, column).setIcon(iconFile)
       # self.tableWidget_AssetItemList.setIconSize(QtCore.QSize(60,60))



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


 