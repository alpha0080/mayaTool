# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha/Documents/GitHub/mayaTool/publishTool/exportTool_UI_a01.ui'
#
# Created: Sat Jun 10 23:03:59 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import maya.cmds as cmds
import os , sys
import pymel.core as pm

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(558, 774)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(380, 100, 171, 651))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox.setGeometry(QtCore.QRect(10, 380, 151, 271))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_convertToTex = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_convertToTex.setGeometry(QtCore.QRect(10, 20, 40, 40))
        self.pushButton_convertToTex.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/alpha.DESKTOP-1S1STEK/Documents/GitHub/mayaTool/publishTool/icons/publishToolIcon/TEX-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_convertToTex.setIcon(icon)
        self.pushButton_convertToTex.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_convertToTex.setFlat(True)
        self.pushButton_convertToTex.setObjectName("pushButton_convertToTex")
        self.pushButton_convertToExr = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_convertToExr.setGeometry(QtCore.QRect(10, 70, 40, 40))
        self.pushButton_convertToExr.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/alpha.DESKTOP-1S1STEK/Documents/GitHub/mayaTool/publishTool/icons/publishToolIcon/EXR-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_convertToExr.setIcon(icon1)
        self.pushButton_convertToExr.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_convertToExr.setFlat(True)
        self.pushButton_convertToExr.setObjectName("pushButton_convertToExr")
        self.pushButton_convertToPng = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_convertToPng.setGeometry(QtCore.QRect(50, 70, 40, 40))
        self.pushButton_convertToPng.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/alpha.DESKTOP-1S1STEK/Documents/GitHub/mayaTool/publishTool/icons/publishToolIcon/PNG-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_convertToPng.setIcon(icon2)
        self.pushButton_convertToPng.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_convertToPng.setFlat(True)
        self.pushButton_convertToPng.setObjectName("pushButton_convertToPng")
        self.pushButton_convertToJpg = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_convertToJpg.setGeometry(QtCore.QRect(90, 70, 40, 40))
        self.pushButton_convertToJpg.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/alpha.DESKTOP-1S1STEK/Documents/GitHub/mayaTool/publishTool/icons/publishToolIcon/jpgs-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_convertToJpg.setIcon(icon3)
        self.pushButton_convertToJpg.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_convertToJpg.setFlat(True)
        self.pushButton_convertToJpg.setObjectName("pushButton_convertToJpg")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 120, 141, 151))
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_Original = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_Original.setGeometry(QtCore.QRect(10, 20, 83, 16))
        self.radioButton_Original.setChecked(True)
        self.radioButton_Original.setObjectName("radioButton_Original")
        self.radioButton_Half = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_Half.setGeometry(QtCore.QRect(10, 40, 83, 16))
        self.radioButton_Half.setChecked(False)
        self.radioButton_Half.setObjectName("radioButton_Half")
        self.radioButton_Quarter = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_Quarter.setGeometry(QtCore.QRect(10, 60, 83, 16))
        self.radioButton_Quarter.setChecked(False)
        self.radioButton_Quarter.setObjectName("radioButton_Quarter")
        self.lineEdit_reduceSizeCustomer = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_reduceSizeCustomer.setEnabled(False)
        self.lineEdit_reduceSizeCustomer.setGeometry(QtCore.QRect(30, 100, 61, 21))
        self.lineEdit_reduceSizeCustomer.setObjectName("lineEdit_reduceSizeCustomer")
        self.radioButton_customer = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_customer.setGeometry(QtCore.QRect(10, 80, 111, 16))
        self.radioButton_customer.setChecked(False)
        self.radioButton_customer.setObjectName("radioButton_customer")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 371, 741))
        self.groupBox_4.setObjectName("groupBox_4")
        self.lineEdit_showFileName = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_showFileName.setGeometry(QtCore.QRect(20, 19, 341, 21))
        self.lineEdit_showFileName.setObjectName("lineEdit_showFileName")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_4)
        self.progressBar.setGeometry(QtCore.QRect(20, 40, 341, 5))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setObjectName("progressBar")
        self.treeWidget_filesList = QtWidgets.QTreeWidget(self.groupBox_4)
        self.treeWidget_filesList.setGeometry(QtCore.QRect(20, 46, 341, 411))
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
        self.treeWidget_filesList.header().setVisible(True)
        self.treeWidget_filesList.header().setCascadingSectionResizes(False)
        self.treeWidget_filesList.header().setDefaultSectionSize(150)
        self.treeWidget_filesList.header().setHighlightSections(True)
        self.treeWidget_filesList.header().setMinimumSectionSize(30)
        self.treeWidget_filesList.header().setSortIndicatorShown(False)
        self.pushButton_refreshList = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_refreshList.setGeometry(QtCore.QRect(20, 470, 40, 40))
        self.pushButton_refreshList.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:/Users/alpha.DESKTOP-1S1STEK/Documents/GitHub/mayaTool/publishTool/icons/publishToolIcon/refreshPublishA.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_refreshList.setIcon(icon4)
        self.pushButton_refreshList.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_refreshList.setFlat(True)
        self.pushButton_refreshList.setObjectName("pushButton_refreshList")
        self.pushButton_delectSelectItems = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_delectSelectItems.setGeometry(QtCore.QRect(310, 470, 40, 40))
        self.pushButton_delectSelectItems.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:/Users/alpha.DESKTOP-1S1STEK/Documents/GitHub/mayaTool/publishTool/icons/publishToolIcon/deletePublishA.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_delectSelectItems.setIcon(icon5)
        self.pushButton_delectSelectItems.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_delectSelectItems.setFlat(True)
        self.pushButton_delectSelectItems.setObjectName("pushButton_delectSelectItems")
        self.lineEdit_metaDataA = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_metaDataA.setGeometry(QtCore.QRect(20, 520, 341, 211))
        self.lineEdit_metaDataA.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_metaDataA.setObjectName("lineEdit_metaDataA")
        self.pushButton_getSelectedNode = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_getSelectedNode.setGeometry(QtCore.QRect(70, 470, 40, 40))
        self.pushButton_getSelectedNode.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("C:/Users/alpha.DESKTOP-1S1STEK/Documents/GitHub/mayaTool/publishTool/icons/publishToolIcon/getSelectItemPublishA.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_getSelectedNode.setIcon(icon6)
        self.pushButton_getSelectedNode.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_getSelectedNode.setFlat(True)
        self.pushButton_getSelectedNode.setObjectName("pushButton_getSelectedNode")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(380, 20, 171, 81))
        self.groupBox_5.setObjectName("groupBox_5")
        self.radioButton_syncMode = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_syncMode.setGeometry(QtCore.QRect(80, 50, 141, 16))
        self.radioButton_syncMode.setObjectName("radioButton_syncMode")
        self.radioButton_publishMode = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_publishMode.setGeometry(QtCore.QRect(80, 20, 83, 16))
        self.radioButton_publishMode.setChecked(True)
        self.radioButton_publishMode.setObjectName("radioButton_publishMode")
        self.pushButton_publishAll = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_publishAll.setGeometry(QtCore.QRect(10, 18, 50, 50))
        self.pushButton_publishAll.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("C:/Users/alpha.DESKTOP-1S1STEK/Documents/GitHub/mayaTool/publishTool/icons/publishToolIcon/uploadPublish.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_publishAll.setIcon(icon7)
        self.pushButton_publishAll.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_publishAll.setFlat(True)
        self.pushButton_publishAll.setObjectName("pushButton_publishAll")
        self.pushButton_newWindow = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_newWindow.setGeometry(QtCore.QRect(670, 580, 51, 41))
        self.pushButton_newWindow.setObjectName("pushButton_newWindow")
        self.treeWidget_FiletOption = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget_FiletOption.setGeometry(QtCore.QRect(400, 120, 141, 341))
        self.treeWidget_FiletOption.setAutoFillBackground(True)
        self.treeWidget_FiletOption.setAutoExpandDelay(-1)
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
        self.treeWidget_FiletOption.header().setVisible(False)
        self.groupBox_CheckAssetUtli = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_CheckAssetUtli.setGeometry(QtCore.QRect(750, 710, 151, 111))
        self.groupBox_CheckAssetUtli.setFlat(True)
        self.groupBox_CheckAssetUtli.setCheckable(True)
        self.groupBox_CheckAssetUtli.setObjectName("groupBox_CheckAssetUtli")
        self.checkBox_CheckBB = QtWidgets.QCheckBox(self.groupBox_CheckAssetUtli)
        self.checkBox_CheckBB.setGeometry(QtCore.QRect(20, 20, 158, 18))
        self.checkBox_CheckBB.setChecked(True)
        self.checkBox_CheckBB.setObjectName("checkBox_CheckBB")
        self.checkBox_CheckPosition = QtWidgets.QCheckBox(self.groupBox_CheckAssetUtli)
        self.checkBox_CheckPosition.setGeometry(QtCore.QRect(20, 40, 158, 18))
        self.checkBox_CheckPosition.setChecked(True)
        self.checkBox_CheckPosition.setObjectName("checkBox_CheckPosition")
        self.checkBox_CheckReNameSG = QtWidgets.QCheckBox(self.groupBox_CheckAssetUtli)
        self.checkBox_CheckReNameSG.setGeometry(QtCore.QRect(20, 60, 158, 18))
        self.checkBox_CheckReNameSG.setChecked(True)
        self.checkBox_CheckReNameSG.setObjectName("checkBox_CheckReNameSG")
        self.checkBox_CheckReNameSG_2 = QtWidgets.QCheckBox(self.groupBox_CheckAssetUtli)
        self.checkBox_CheckReNameSG_2.setGeometry(QtCore.QRect(20, 80, 101, 18))
        self.checkBox_CheckReNameSG_2.setChecked(True)
        self.checkBox_CheckReNameSG_2.setObjectName("checkBox_CheckReNameSG_2")
        self.groupBox_CheckPlugin = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_CheckPlugin.setGeometry(QtCore.QRect(750, 660, 150, 51))
        self.groupBox_CheckPlugin.setFlat(True)
        self.groupBox_CheckPlugin.setCheckable(True)
        self.groupBox_CheckPlugin.setObjectName("groupBox_CheckPlugin")
        self.checkBox_DeleteUnusedPlugin = QtWidgets.QCheckBox(self.groupBox_CheckPlugin)
        self.checkBox_DeleteUnusedPlugin.setGeometry(QtCore.QRect(20, 20, 158, 18))
        self.checkBox_DeleteUnusedPlugin.setChecked(True)
        self.checkBox_DeleteUnusedPlugin.setObjectName("checkBox_DeleteUnusedPlugin")
        self.groupBox_CollectFile = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_CollectFile.setGeometry(QtCore.QRect(750, 470, 150, 181))
        self.groupBox_CollectFile.setFlat(True)
        self.groupBox_CollectFile.setCheckable(True)
        self.groupBox_CollectFile.setObjectName("groupBox_CollectFile")
        self.checkBox_prmanTexture = QtWidgets.QCheckBox(self.groupBox_CollectFile)
        self.checkBox_prmanTexture.setGeometry(QtCore.QRect(20, 20, 158, 18))
        self.checkBox_prmanTexture.setChecked(True)
        self.checkBox_prmanTexture.setObjectName("checkBox_prmanTexture")
        self.checkBox_mayaTexture = QtWidgets.QCheckBox(self.groupBox_CollectFile)
        self.checkBox_mayaTexture.setGeometry(QtCore.QRect(20, 40, 158, 18))
        self.checkBox_mayaTexture.setChecked(True)
        self.checkBox_mayaTexture.setObjectName("checkBox_mayaTexture")
        self.checkBox_gpuCache = QtWidgets.QCheckBox(self.groupBox_CollectFile)
        self.checkBox_gpuCache.setGeometry(QtCore.QRect(20, 60, 158, 18))
        self.checkBox_gpuCache.setChecked(True)
        self.checkBox_gpuCache.setObjectName("checkBox_gpuCache")
        self.checkBox_ribArchive = QtWidgets.QCheckBox(self.groupBox_CollectFile)
        self.checkBox_ribArchive.setGeometry(QtCore.QRect(20, 80, 158, 18))
        self.checkBox_ribArchive.setChecked(True)
        self.checkBox_ribArchive.setObjectName("checkBox_ribArchive")
        self.checkBox_alembicCache = QtWidgets.QCheckBox(self.groupBox_CollectFile)
        self.checkBox_alembicCache.setGeometry(QtCore.QRect(20, 100, 158, 18))
        self.checkBox_alembicCache.setChecked(True)
        self.checkBox_alembicCache.setObjectName("checkBox_alembicCache")
        self.checkBox_prmanLight = QtWidgets.QCheckBox(self.groupBox_CollectFile)
        self.checkBox_prmanLight.setGeometry(QtCore.QRect(20, 120, 158, 18))
        self.checkBox_prmanLight.setCheckable(False)
        self.checkBox_prmanLight.setChecked(False)
        self.checkBox_prmanLight.setObjectName("checkBox_prmanLight")
        self.checkBox_mayaFluidCache = QtWidgets.QCheckBox(self.groupBox_CollectFile)
        self.checkBox_mayaFluidCache.setGeometry(QtCore.QRect(20, 140, 158, 18))
        self.checkBox_mayaFluidCache.setCheckable(False)
        self.checkBox_mayaFluidCache.setChecked(False)
        self.checkBox_mayaFluidCache.setObjectName("checkBox_mayaFluidCache")
        self.checkBox_mayanParticleCache = QtWidgets.QCheckBox(self.groupBox_CollectFile)
        self.checkBox_mayanParticleCache.setGeometry(QtCore.QRect(20, 160, 158, 18))
        self.checkBox_mayanParticleCache.setCheckable(False)
        self.checkBox_mayanParticleCache.setChecked(False)
        self.checkBox_mayanParticleCache.setObjectName("checkBox_mayanParticleCache")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("MainWindow", "Option", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "Convert Texture Format", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "Reduce Texture Size", None, -1))
        self.radioButton_Original.setText(QtWidgets.QApplication.translate("MainWindow", "Original Size", None, -1))
        self.radioButton_Half.setText(QtWidgets.QApplication.translate("MainWindow", "Half Size", None, -1))
        self.radioButton_Quarter.setText(QtWidgets.QApplication.translate("MainWindow", "Quarter Size", None, -1))
        self.radioButton_customer.setText(QtWidgets.QApplication.translate("MainWindow", "Customer Size", None, -1))
        self.groupBox_4.setTitle(QtWidgets.QApplication.translate("MainWindow", "Items", None, -1))
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
        self.lineEdit_metaDataA.setText(QtWidgets.QApplication.translate("MainWindow", "# total polygons", None, -1))
        self.groupBox_5.setTitle(QtWidgets.QApplication.translate("MainWindow", "Publish Mode", None, -1))
        self.radioButton_syncMode.setText(QtWidgets.QApplication.translate("MainWindow", "Synchronous", None, -1))
        self.radioButton_publishMode.setText(QtWidgets.QApplication.translate("MainWindow", "Publish", None, -1))
        self.pushButton_newWindow.setText(QtWidgets.QApplication.translate("MainWindow", "new window", None, -1))
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
        self.treeWidget_FiletOption.setSortingEnabled(__sortingEnabled)
        self.groupBox_CheckAssetUtli.setTitle(QtWidgets.QApplication.translate("MainWindow", "Check AssetUtli", None, -1))
        self.checkBox_CheckBB.setText(QtWidgets.QApplication.translate("MainWindow", "Check BB", None, -1))
        self.checkBox_CheckPosition.setText(QtWidgets.QApplication.translate("MainWindow", "Check Position", None, -1))
        self.checkBox_CheckReNameSG.setText(QtWidgets.QApplication.translate("MainWindow", "ReName SG", None, -1))
        self.checkBox_CheckReNameSG_2.setText(QtWidgets.QApplication.translate("MainWindow", "Check Repeat", None, -1))
        self.groupBox_CheckPlugin.setTitle(QtWidgets.QApplication.translate("MainWindow", "Check Plugin", None, -1))
        self.checkBox_DeleteUnusedPlugin.setText(QtWidgets.QApplication.translate("MainWindow", "Delete Unused Plugin", None, -1))
        self.groupBox_CollectFile.setTitle(QtWidgets.QApplication.translate("MainWindow", "Collect Files", None, -1))
        self.checkBox_prmanTexture.setText(QtWidgets.QApplication.translate("MainWindow", "Prman Textures", None, -1))
        self.checkBox_mayaTexture.setText(QtWidgets.QApplication.translate("MainWindow", "Maya Textures", None, -1))
        self.checkBox_gpuCache.setText(QtWidgets.QApplication.translate("MainWindow", "Gpu Caches", None, -1))
        self.checkBox_ribArchive.setText(QtWidgets.QApplication.translate("MainWindow", "Rib Archives", None, -1))
        self.checkBox_alembicCache.setText(QtWidgets.QApplication.translate("MainWindow", "Alembic Caches", None, -1))
        self.checkBox_prmanLight.setText(QtWidgets.QApplication.translate("MainWindow", "Prman Lights", None, -1))
        self.checkBox_mayaFluidCache.setText(QtWidgets.QApplication.translate("MainWindow", "Maya Fluid Caches", None, -1))
        self.checkBox_mayanParticleCache.setText(QtWidgets.QApplication.translate("MainWindow", "Maya nParticle Caches", None, -1))


class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #self.QTITEM.ACTION.connect(self.MODDEF)
        self.setupUi(self)
        #self.proj = cmds.workspace(rd=True,q=True)
        #self.workProject
        try:
            pm.mel.eval('rmanLoadPlugin')
            rendermanPath = pm.mel.eval('getenv RMANTREE')
            pythonScriptPath = rendermanPath + 'lib/python2.7/Lib/site-packages'
            sys.path.append(pythonScriptPath)
            import ice

        except:
            print 'pls import prman plugin'
            pass

        
        
        
        ####initial UI#########
       # self.treeWidget_FiletOption.setExpanded   #自動展開 .setCheckState(0, QtCore.Qt.Checked) #設定勾選
        self.treeWidget_FiletOption.topLevelItem(0).setExpanded(1)#自動展開
        self.treeWidget_FiletOption.topLevelItem(1).setExpanded(1)#自動展開
        self.treeWidget_FiletOption.topLevelItem(2).setExpanded(1)#自動展開
        
        self.treeWidget_FiletOption.topLevelItem(0).setCheckState(0, QtCore.Qt.Checked)#設定勾選
        self.treeWidget_FiletOption.topLevelItem(0).child(0).setCheckState(0, QtCore.Qt.Checked)#設定勾選
        self.treeWidget_FiletOption.topLevelItem(0).child(1).setCheckState(0, QtCore.Qt.Checked)#設定勾選
        self.treeWidget_FiletOption.topLevelItem(0).child(2).setCheckState(0, QtCore.Qt.Checked)#設定勾選
        self.treeWidget_FiletOption.topLevelItem(0).child(3).setCheckState(0, QtCore.Qt.Checked)#設定勾選
        self.treeWidget_FiletOption.topLevelItem(0).child(4).setCheckState(0, QtCore.Qt.Checked)#設定勾選
        self.treeWidget_FiletOption.topLevelItem(0).child(5).setCheckState(0, QtCore.Qt.Unchecked)#設定勾選
        self.treeWidget_FiletOption.topLevelItem(0).child(6).setCheckState(0, QtCore.Qt.Unchecked)#設定勾選
        self.treeWidget_FiletOption.topLevelItem(0).child(7).setCheckState(0, QtCore.Qt.Unchecked)#設定勾選
      #  self.treeWidget_FiletOption.topLevelItem(0).child(8).setCheckState(0, QtCore.Qt.Checked)#設定勾選
       # self.treeWidget_FiletOption.topLevelItem(0).child(9).setCheckState(0, QtCore.Qt.Checked)#設定勾選
    
        self.treeWidget_FiletOption.topLevelItem(1).setCheckState(0, QtCore.Qt.Checked)#設定勾選
        self.treeWidget_FiletOption.topLevelItem(1).child(0).setCheckState(0, QtCore.Qt.Checked)#設定勾選
       # self.treeWidget_FiletOption.topLevelItem(1).child(9).setCheckState(0, QtCore.Qt.Checked)#設定勾選
        
        
        
        self.treeWidget_FiletOption.topLevelItem(2).setCheckState(0, QtCore.Qt.Checked)#設定勾選
        self.treeWidget_FiletOption.topLevelItem(2).child(0).setCheckState(0, QtCore.Qt.Checked)#設定勾選
        self.treeWidget_FiletOption.topLevelItem(2).child(1).setCheckState(0, QtCore.Qt.Checked)#設定勾選
        self.treeWidget_FiletOption.topLevelItem(2).child(2).setCheckState(0, QtCore.Qt.Checked)#設定勾選
        self.treeWidget_FiletOption.topLevelItem(2).child(3).setCheckState(0, QtCore.Qt.Checked)#設定勾選
        
        
        
        ###define modify
        

        self.treeWidget_filesList.clicked.connect(self.showFileName)
        self.pushButton_getSelectedNode.clicked.connect(self.getSelectedNode)
        
        
        self.pushButton_refreshList.clicked.connect(self.reflashTree)
        self.pushButton_delectSelectItems.clicked.connect(self.searchIsChecked)
        
        self.treeWidget_filesList.doubleClicked.connect(self.replaceFile)
        
        
        
        
        self.linkingFilePreMoveDict = {}

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

        self.buildItemTree()
         
        #self.createNewItem() 
        
    def replaceFile(self):
        print "replaceFile start"
 
 
 
 
    def copyFilesFromFileTable(self,sourceTable,dest):
        
        
        
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
        
        #cmds.setAttr('PxrTexture9.filename','C:/Users/alpha.DESKTOP-1S1STEK/Pictures/IMG_1483.PNG',typ = "string")
        newFileLocation = cmds.fileDialog2(fm=1,rf=True)[0]
        print newFileLocation
        #C:/Users/alpha.DESKTOP-1S1STEK/Pictures/IMG_1485.PNG
        cmds.setAttr('%s%s'%(self.treeWidget_filesList.currentItem().text(0),self.treeWidget_filesList.currentItem().text(3)),newFileLocation,typ="string")
        #print self.treeWidget.currentItem().text(0) +self.treeWidget.currentItem().text(3),newFileLocation
        self.treeWidget_filesList.topLevelItem(int(self.treeWidget_filesList.currentItem().text(4))).child(int(self.treeWidget_filesList.currentItem().text(5))).setText(1,newFileLocation.split('/')[-1])
        
    def getSelectedNode(self):
        cmds.select(self.treeWidget_filesList.currentItem().text(0))
        
        
        
    def showFileName(self):
        print self.treeWidget_filesList.currentItem().text(2)
        self.lineEdit_showFileName.setText(self.treeWidget_filesList.currentItem().text(2))
        
        
        
    
    def delectChecked(self):
        sefl.searchIsChecked()
        delectList = self.checkNodeDict.keys()
        
       # deleteTable= self.checkNodeDict.keys() treeWidget
        for i in self.checkNodeDict.keys():
            try:
                if len(cmds.listRelatives( i, p=True )) > 0:
                    
                    #print cmds.listRelatives( i, p=True )
                    delectList.append(cmds.listRelatives( i, p=True )[0])

            except:
                pass
        
        print delectList
        cmds.delete(delectList)
        self.checkNodeDict = {}
       # cmds.relationship('PxrTexture2',q=True)
       
       
        
        
    def searchIsChecked(self):
        self.checkNodeDict = {}
        topLayerCounts = self.treeWidget_filesList.topLevelItemCount()
       # print topLayerCounts
        for i in range( 0,topLayerCounts-1):
            for j in range(0,self.treeWidget_filesList.topLevelItem(i).childCount()):


                if self.treeWidget_filesList.topLevelItem(i).child(j).checkState(0) == QtCore.Qt.CheckState.Checked:

                    self.checkNodeDict.update({self.treeWidget_filesList.topLevelItem(i).child(j).text(0):{}})

               # else:
                 #   pass
        print self.checkNodeDict
            
        #self.delectChecked()
        self.reflashTree()




        
    def createNewItem(self,topLayerIndex,index,nodeName,linkingFile,fontColor,attrKey):
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
        
        

        textColor = (int(self.fontColor[0]), int(self.fontColor[1]), int(self.fontColor[2]))
        #        QtWidgets.QTreeWidgetItem(self.treeWidget).setForeground(0,self.brushLevelOne)  #create contain master ,and define font color
      #  QtWidgets.QTreeWidgetItem(self.treeWidget).setForeground(0,QtGui.QBrush(QtGui.QColor(247, 126, 128)))  #create contain master ,and define font color
        
       # #1.default exist , master should exist in top of treeWidget
       # self.treeWidget.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "master", None, -1))
      #  self.treeWidget.topLevelItem(0)#.setFont(0,self.fontLevelOne)#define font size
      
        QtWidgets.QTreeWidgetItem(self.treeWidget_filesList.topLevelItem(topLayerIndex))#.setForeground(0,self.brushLevelThree)  #build new item from index
        
        self.treeWidget_filesList.topLevelItem(topLayerIndex).child(index).setForeground(0,QtGui.QBrush(QtGui.QColor(int(self.fontColor[0]), int(self.fontColor[1]), int(self.fontColor[2]))))#.setFont(0,self.fontLevelThree)
        self.treeWidget_filesList.topLevelItem(topLayerIndex).child(index).setText(0, QtWidgets.QApplication.translate("MainWindow", 'tempName', None, -1))
        self.treeWidget_filesList.topLevelItem(topLayerIndex).child(index).setText(0,nodeName)
        
        if self.checkState == 'Unchecked':
            self.treeWidget_filesList.topLevelItem(topLayerIndex).child(index).setCheckState(0, QtCore.Qt.Unchecked)
        else:
            self.treeWidget_filesList.topLevelItem(topLayerIndex).child(index).setCheckState(0, QtCore.Qt.Checked)
            
        self.treeWidget_filesList.topLevelItem(topLayerIndex).child(index).setForeground(1,QtGui.QBrush(QtGui.QColor(int(self.fontColor[0]), int(self.fontColor[1]), int(self.fontColor[2]))))#.setFont(0,self.fontLevelThree)

       
        self.treeWidget_filesList.topLevelItem(topLayerIndex).child(index).setText(1,linkingFile.split('/')[-1])  #add shot Name into treeWidget in column 2
        self.treeWidget_filesList.topLevelItem(topLayerIndex).child(index).setText(2,linkingFile) #add fullName into treeWidget in column 3
        self.treeWidget_filesList.topLevelItem(topLayerIndex).child(index).setText(3,attrKey) #add nodePath into treeWidget in column 3
        self.treeWidget_filesList.topLevelItem(topLayerIndex).child(index).setText(4,str(topLayerIndex))
        self.treeWidget_filesList.topLevelItem(topLayerIndex).child(index).setText(5,str(index))
  
  
  
  
  
  
  
  
    def checkFileExist(self,linkingFile,checkMode):  #checkMode = pxrTexture,mayaTexture,gpuCache,ribArchive,alembic,pxrLight,mayaFluid,mayanParticle
      #  print 'check file is existed'

        if os.path.isfile(linkingFile) == True:
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
                if linkingFile.split('.')[-1] in ['rib','zip','7z','gz']:
                    self.fontColor = (0,255,0)
                else:
                    self.fontColor =(255,255,0)
                    self.yellowCount = self.yellowCount +1
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
                

           # self.setCheck = 0 
        else:
            self.fontColor =(255,0,0)
            self.setCheck = 1
            self.redCount = self.redCount +1
            self.checkState = 'Checked'


            
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
        


        
    def defineFont(self):
                
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
    
    
    
    
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_filesList)
        item_0.setCheckState(0, QtCore.Qt.Checked)
      #  item1 = QtWidgets.QTreeWidgetItem(self.treeWidget.topLevelItem(0).child(0))

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_filesList)
        item_0.setCheckState(0, QtCore.Qt.Checked)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_filesList)
        item_0.setCheckState(0, QtCore.Qt.Checked)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_filesList)
        item_0.setCheckState(0, QtCore.Qt.Checked)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_filesList)
        item_0.setCheckState(0, QtCore.Qt.Checked)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_filesList)
        item_0.setCheckState(0, QtCore.Qt.Checked)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_filesList)
        item_0.setCheckState(0, QtCore.Qt.Checked)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_filesList)
        item_0.setCheckState(0, QtCore.Qt.Checked)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_filesList)
        item_0.setCheckState(0, QtCore.Qt.Checked)

       # item_1 = QtWidgets.QTreeWidgetItem(item_0)
       # item_0.setCheckState(0, QtCore.Qt.Checked)
                                
       # item1= self.treeWidget.topLevelItem(0).child(0)#.setForeground(0)
       # secLevelItemIndex = self.secLayerItemDict[secLayerItem]

       # self.treeWidget.topLevelItem(0).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "A1_1", None, -1))

        self.itemName_prmanTextures = "PrmanTextures"+'__('+'%03d'%self.countN1+')'
        self.itemName_mayaTextures = "mayaTextures"+'__('+'%03d'%self.countN2+')'
        self.itemName_gpuCaches = "gpuCaches"+'__('+'%03d'%self.countN3+')'
        self.itemName_RibArchives = "RibArchives"+'__('+'%03d'%self.countN4+')'
        self.itemName_alembics = "alembics"+'__('+'%03d'%self.countN5+')'
        self.itemName_cameras = "cameras"+'__('+'%03d'%self.countN6+')'
        self.itemName_PrmanLights = "PrmanLights"+'__('+'%03d'%self.countN7+')'
        #self.itemName_mayaLights = "mayaLights"+'__('+'%03d'%countN8+')'
        self.itemName_fluidCaches = "fluidCaches"+'__('+'%03d'%self.countN9+')'
        self.itemName_nParticleCaches = "particleCaches"+'__('+'%03d'%self.countN10+')'

        

        
        self.treeWidget_filesList.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_prmanTextures, None, -1))
        self.treeWidget_filesList.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_mayaTextures, None, -1))
        self.treeWidget_filesList.topLevelItem(2).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_gpuCaches, None, -1))
        self.treeWidget_filesList.topLevelItem(3).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_RibArchives, None, -1))
        self.treeWidget_filesList.topLevelItem(4).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_alembics, None, -1))
        self.treeWidget_filesList.topLevelItem(5).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_cameras, None, -1))
        self.treeWidget_filesList.topLevelItem(6).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_PrmanLights, None, -1))
        self.treeWidget_filesList.topLevelItem(7).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_fluidCaches, None, -1))
        self.treeWidget_filesList.topLevelItem(8).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_nParticleCaches, None, -1))
       # self.treeWidget.topLevelItem(9).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_fluidCaches, None, -1))
       # self.treeWidget.topLevelItem(0).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "A1_1", None, -1))

        

        
        
        '''
         linkingSearchDict = {
                              'PxrTexture':'filename',
                              'file':'fileTextureName',
                              'AlembicNode':'abc_File',
                              'gpuCache':'cacheFileName',
                              'RenderManArchive':'filename'}
                              
        '''   
        
        
    def reflashTree(self):
        self.buildItemTree()

        self.findPrmanTexture()
        self.findMayaTexture()

        self.findGpuCaches()

        self.findRibArchives()

        self.findAlembics()
      #  self.findCameras()
        self.findPrmanLights()
        self.mayaFluidCache()
        self.mayanParticleCache()
        
        print 'self.linkingFilePreMoveDict',self.linkingFilePreMoveDict
      #  self.buildItemTree()
#cmds.nodeType('nParticleShape1Cache1')


            


        
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



        


        
        
            
    def findPrmanTexture(self):  # store PrmanTextures NodeName and location 

        pxrNodes = cmds.ls( typ ='PxrTexture')
        pxrTexturePath = {}
        for i in pxrNodes:
            path = cmds.getAttr('%s.filename'%i)
            pxrTexturePath.update({i:{'linkingFile':path}})
            self.linkingFilePreMoveDict.update({'pxrTexture':{i:{path:{}}}})
        self.countN1 = len(pxrNodes)
            
      #  print self.countN1
        self.yellowCount = 0
        self.redCount = 0
        attrKey = '.filename'
        for index in range(0,len(pxrTexturePath.keys())):
            nodeName = pxrTexturePath.keys()[index]
            linkingFile = pxrTexturePath[nodeName]['linkingFile']
            
            self.checkFileExist(linkingFile,'pxrTexture')   
            topLayerIndex = 0
            self.createNewItem(topLayerIndex,index,nodeName,linkingFile,self.fontColor,attrKey)
        print pxrTexturePath
        topLayerItemName = "PrmanTextures"+'__('+'%03d'%self.countN1+')'

        self.setTopLayerItemColor(topLayerIndex,topLayerItemName)         
        

        
        
     #cmds.nodeType('file2')       
         #aa= cmds.ls(typ='file') 
        # cmds.select(aa)
    def findMayaTexture(self):  # store mayaNodeName and location 
        
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
       # print self.countN2
        for index in range(0,len(mayaTextureFilePath.keys())):
            nodeName = mayaTextureFilePath.keys()[index]
            linkingFile = mayaTextureFilePath[nodeName]['linkingFile']
            self.checkFileExist(linkingFile,'mayaTexture')   
            #print 'index',index
           # print 'nodeName',nodeName
            #print 'linkingFile',linkingFile
            #print 'self.fontColor',self.fontColor
            topLayerIndex = 1

            self.createNewItem(topLayerIndex,index,nodeName,linkingFile,self.fontColor,attrKey)
            
        topLayerItemName = "mayaTextures"+'__('+'%03d'%self.countN2+')'

        self.setTopLayerItemColor(topLayerIndex,topLayerItemName)         
        
        
            
                        
            
            
            
            
            
            
        



#cmds.nodeType('pCone1RibArchiveGPUCacheShape')
    def findGpuCaches(self): # store mayaTextures NodeName and location  
      #  pxrFilePath = 'file.fileTextureName'
        
        gpuCacheNodes = cmds.ls( typ ='gpuCache')
        gpuCachePath = {}
        for i in gpuCacheNodes:
            path = cmds.getAttr('%s.cacheFileName'%i)
            gpuCachePath.update({i:{'linkingFile':path}})
           # self.linkingFilePreMoveDict.update({'gpuCache':{i:{path:{}}}})
            self.linkingFilePreMoveDict.update({'gpuCache':{i:{path:{}}}})

        self.countN3 = len(gpuCacheNodes)
        self.yellowCount = 0
        self.redCount = 0              

        attrKey = '.cacheFileName'
        
        for index in range(0,len(gpuCachePath.keys())):
            nodeName = gpuCachePath.keys()[index]
            linkingFile = gpuCachePath[nodeName]['linkingFile']
            self.checkFileExist(linkingFile,'gpuCache')   
            #print 'index',index
           # print 'nodeName',nodeName
            #print 'linkingFile',linkingFile
            #print 'self.fontColor',self.fontColor
            topLayerIndex = 2
            self.createNewItem(topLayerIndex,index,nodeName,linkingFile,self.fontColor,attrKey)

        topLayerItemName = "gpuCaches"+'__('+'%03d'%self.countN3+')'

        self.setTopLayerItemColor(topLayerIndex,topLayerItemName)         
        
        
            
                        
            
            

            
    def findRibArchives(self): # store RibArchives NodeName and location 
        
        RibArchivesNodes = cmds.ls( typ ='RenderManArchive')
        RibArchivesPath = {}
        for i in RibArchivesNodes:
            path = self.workProject +cmds.getAttr('%s.filename'%i)
            RibArchivesPath.update({i:{'linkingFile':path}})
            self.linkingFilePreMoveDict.update({'ribArchive':{i:{path:{}}}})
  
        self.countN4 = len(RibArchivesNodes)
        self.yellowCount = 0
        self.redCount = 0   

        attrKey = '.filename'
                    
        for index in range(0,len(RibArchivesPath.keys())):
            nodeName = RibArchivesPath.keys()[index]
            linkingFile = RibArchivesPath[nodeName]['linkingFile']
            self.checkFileExist(linkingFile,'ribArchive')   
            topLayerIndex = 3
            self.createNewItem(topLayerIndex,index,nodeName,linkingFile,self.fontColor,attrKey)
        topLayerItemName =  "RibArchives"+'__('+'%03d'%self.countN4+')'

        self.setTopLayerItemColor(topLayerIndex,topLayerItemName)         
        
        
    def findAlembics(self): # store alembics NodeName and location 
        
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
    
        for index in range(0,len(alembicPath.keys())):
            nodeName = alembicPath.keys()[index]
            linkingFile = alembicPath[nodeName]['linkingFile']
            self.checkFileExist(linkingFile,'alembic')   
            topLayerIndex = 4
            self.createNewItem(topLayerIndex,index,nodeName,linkingFile,self.fontColor,attrKey)
            
        topLayerItemName = "alembics"+'__('+'%03d'%self.countN5+')'

        self.setTopLayerItemColor(topLayerIndex,topLayerItemName)  
        
        
        
        
    def findPrmanLights(self): # store PrmanLights NodeName and location 
        
        prmanLightType =['PxrRectLight','PxrDiskLight','PxrDistantLight','PxrSphereLight','PxrDomeLight','PxrEnvDayLight','PxrMeshLight']
        prmanLightNodes = []
        prmanLightInfo = {}
        for prmanNodeType in prmanLightType:
            prmanLightNodes = prmanLightNodes + cmds.ls( typ =prmanNodeType)
  
       # print prmanLightNodes 
        self.yellowCount = 0
        self.redCount = 0      
        attrKey = '.lightColorMap'
   
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
            topLayerIndex = 6
            self.createNewItem(topLayerIndex,index,nodeName,linkingFile,self.fontColor,attrKey)
            
        topLayerItemName = "PrmanLights"+'__('+'%03d'%self.countN7+')'

        self.setTopLayerItemColor(topLayerIndex,topLayerItemName)  
        
        
        
#cmds.listConnections('nParticleShape1')        
    def mayaFluidCache(self): # store mayaTextures NodeName and location 
      #  pxrFilePath = 'file.fileTextureName'
      
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
        for index in range(0,len(mayaFluidCacheInfo.keys())):
            nodeName = mayaFluidCacheInfo.keys()[index]
            linkingFile = mayaFluidCacheInfo[nodeName]['linkingFile']
            self.checkFileExist(linkingFile,'mayaFluid')   
            topLayerIndex = 7
            self.createNewItem(topLayerIndex,index,nodeName,linkingFile,self.fontColor,attrKey)
        topLayerItemName = "fluidCaches"+'__('+'%03d'%self.countN9+')'
        self.setTopLayerItemColor(topLayerIndex,topLayerItemName)      

       # print 'mayaFluidCacheInfo',mayaFluidCacheInfo
    def mayanParticleCache(self): # store mayanParticle NodeName and location fluidCache
      
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
        for index in range(0,len(mayanParticleCacheInfo.keys())):
            nodeName = mayanParticleCacheInfo.keys()[index]
            linkingFile = mayanParticleCacheInfo[nodeName]['linkingFile']
            self.checkFileExist(linkingFile,'mayanParticle')   
            topLayerIndex = 8
            self.createNewItem(topLayerIndex,index,nodeName,linkingFile,self.fontColor,attrKey)
        
        
        topLayerItemName ="particleCaches"+'__('+'%03d'%self.countN10+')'

        self.setTopLayerItemColor(topLayerIndex,topLayerItemName)      

            
       # print mayanParticleCacheInfo
       # print self.countN10
            
        
    def setTopLayerItemColor(self,topLayerIndex,topLayerItemName):
        if self.redCount > 0:

            self.topLayerColor = (255,0,0)
        
        else:
            
            if self.yellowCount >0 :
                self.topLayerColor = (255,255,0)
                
            else:
                self.topLayerColor = (255,255,255)
        self.treeWidget_filesList.topLevelItem(topLayerIndex).setText(0, QtWidgets.QApplication.translate("MainWindow",topLayerItemName, None, -1))
       
        self.treeWidget_filesList.topLevelItem(topLayerIndex).setForeground(0,QtGui.QBrush(QtGui.QColor(int(self.topLayerColor[0]), int(self.topLayerColor[1]), int(self.topLayerColor[2]))))
        
        

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


 