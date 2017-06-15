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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1118, 770)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_dynamicIO = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_dynamicIO.setEnabled(True)
        self.groupBox_dynamicIO.setGeometry(QtCore.QRect(960, 50, 150, 150))
        self.groupBox_dynamicIO.setFlat(True)
        self.groupBox_dynamicIO.setCheckable(True)
        self.groupBox_dynamicIO.setObjectName("groupBox_dynamicIO")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_dynamicIO)
        self.checkBox_5.setGeometry(QtCore.QRect(20, 30, 158, 18))
        self.checkBox_5.setChecked(True)
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_dynamicIO)
        self.checkBox_6.setGeometry(QtCore.QRect(20, 60, 158, 18))
        self.checkBox_6.setChecked(True)
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox_dynamicIO)
        self.checkBox_7.setGeometry(QtCore.QRect(20, 90, 158, 18))
        self.checkBox_7.setChecked(True)
        self.checkBox_7.setObjectName("checkBox_7")
        self.groupBox_LookIO = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_LookIO.setGeometry(QtCore.QRect(800, 210, 150, 150))
        self.groupBox_LookIO.setFlat(True)
        self.groupBox_LookIO.setCheckable(True)
        self.groupBox_LookIO.setObjectName("groupBox_LookIO")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_LookIO)
        self.checkBox.setGeometry(QtCore.QRect(20, 30, 158, 18))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox_LookIO)
        self.checkBox_8.setGeometry(QtCore.QRect(20, 60, 158, 18))
        self.checkBox_8.setObjectName("checkBox_8")
        self.groupBox_proxy_IO = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_proxy_IO.setGeometry(QtCore.QRect(960, 210, 150, 150))
        self.groupBox_proxy_IO.setFlat(True)
        self.groupBox_proxy_IO.setCheckable(True)
        self.groupBox_proxy_IO.setObjectName("groupBox_proxy_IO")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_proxy_IO)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 30, 158, 18))
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_proxy_IO)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 60, 158, 18))
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_proxy_IO)
        self.checkBox_4.setGeometry(QtCore.QRect(20, 90, 158, 18))
        self.checkBox_4.setObjectName("checkBox_4")
        self.groupBox_lightIO = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_lightIO.setGeometry(QtCore.QRect(800, 50, 150, 150))
        self.groupBox_lightIO.setFlat(True)
        self.groupBox_lightIO.setCheckable(True)
        self.groupBox_lightIO.setObjectName("groupBox_lightIO")
        self.checkBox_9 = QtWidgets.QCheckBox(self.groupBox_lightIO)
        self.checkBox_9.setGeometry(QtCore.QRect(20, 30, 158, 18))
        self.checkBox_9.setChecked(True)
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.groupBox_lightIO)
        self.checkBox_10.setGeometry(QtCore.QRect(20, 60, 158, 18))
        self.checkBox_10.setChecked(True)
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_13 = QtWidgets.QCheckBox(self.groupBox_lightIO)
        self.checkBox_13.setGeometry(QtCore.QRect(20, 90, 158, 18))
        self.checkBox_13.setChecked(True)
        self.checkBox_13.setObjectName("checkBox_13")
        self.groupBox_renderIO = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_renderIO.setGeometry(QtCore.QRect(800, 370, 150, 150))
        self.groupBox_renderIO.setFlat(True)
        self.groupBox_renderIO.setCheckable(True)
        self.groupBox_renderIO.setObjectName("groupBox_renderIO")
        self.checkBox_renderCam = QtWidgets.QCheckBox(self.groupBox_renderIO)
        self.checkBox_renderCam.setGeometry(QtCore.QRect(20, 30, 158, 18))
        self.checkBox_renderCam.setChecked(True)
        self.checkBox_renderCam.setObjectName("checkBox_renderCam")
        self.checkBox_renderSet = QtWidgets.QCheckBox(self.groupBox_renderIO)
        self.checkBox_renderSet.setGeometry(QtCore.QRect(20, 60, 158, 18))
        self.checkBox_renderSet.setObjectName("checkBox_renderSet")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(50, 40, 701, 401))
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
        self.treeWidget.setPalette(palette)
        self.treeWidget.setAutoScrollMargin(16)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.treeWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.treeWidget.setIndentation(20)
        self.treeWidget.setRootIsDecorated(True)
        self.treeWidget.setUniformRowHeights(False)
        self.treeWidget.setItemsExpandable(True)
        self.treeWidget.setAllColumnsShowFocus(False)
        self.treeWidget.setWordWrap(False)
        self.treeWidget.setExpandsOnDoubleClick(True)
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.header().setVisible(True)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setDefaultSectionSize(300)
        self.treeWidget.header().setHighlightSections(True)
        self.treeWidget.header().setMinimumSectionSize(30)
        self.treeWidget.header().setSortIndicatorShown(False)
        self.pushButton_newWindow = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_newWindow.setGeometry(QtCore.QRect(40, 450, 191, 41))
        self.pushButton_newWindow.setObjectName("pushButton_newWindow")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 500, 701, 241))
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_testA = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_testA.setGeometry(QtCore.QRect(270, 450, 191, 41))
        self.pushButton_testA.setObjectName("pushButton_testA")
        self.pushButton_testB = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_testB.setGeometry(QtCore.QRect(520, 450, 191, 41))
        self.pushButton_testB.setObjectName("pushButton_testB")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.groupBox_dynamicIO.setTitle(QtWidgets.QApplication.translate("MainWindow", "Dynamic IO", None, -1))
        self.checkBox_5.setText(QtWidgets.QApplication.translate("MainWindow", "fluid Cache", None, -1))
        self.checkBox_6.setText(QtWidgets.QApplication.translate("MainWindow", "particle Cache", None, -1))
        self.checkBox_7.setText(QtWidgets.QApplication.translate("MainWindow", "Alembic", None, -1))
        self.groupBox_LookIO.setTitle(QtWidgets.QApplication.translate("MainWindow", "Look IO", None, -1))
        self.checkBox.setText(QtWidgets.QApplication.translate("MainWindow", "texture", None, -1))
        self.checkBox_8.setText(QtWidgets.QApplication.translate("MainWindow", "Shading", None, -1))
        self.groupBox_proxy_IO.setTitle(QtWidgets.QApplication.translate("MainWindow", "Proxy IO", None, -1))
        self.checkBox_3.setText(QtWidgets.QApplication.translate("MainWindow", "GPUCache", None, -1))
        self.checkBox_2.setText(QtWidgets.QApplication.translate("MainWindow", "RibArchive", None, -1))
        self.checkBox_4.setText(QtWidgets.QApplication.translate("MainWindow", "Alembic", None, -1))
        self.groupBox_lightIO.setTitle(QtWidgets.QApplication.translate("MainWindow", "Light IO", None, -1))
        self.checkBox_9.setText(QtWidgets.QApplication.translate("MainWindow", "Env Light", None, -1))
        self.checkBox_10.setText(QtWidgets.QApplication.translate("MainWindow", "Direct Light", None, -1))
        self.checkBox_13.setText(QtWidgets.QApplication.translate("MainWindow", "Mesh Light", None, -1))
        self.groupBox_renderIO.setTitle(QtWidgets.QApplication.translate("MainWindow", "Render IO", None, -1))
        self.checkBox_renderCam.setText(QtWidgets.QApplication.translate("MainWindow", "Render Cam", None, -1))
        self.checkBox_renderSet.setText(QtWidgets.QApplication.translate("MainWindow", "Render Setting", None, -1))
        self.treeWidget.headerItem().setText(0, QtWidgets.QApplication.translate("MainWindow", "items", None, -1))
        self.treeWidget.headerItem().setText(1, QtWidgets.QApplication.translate("MainWindow", "location", None, -1))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "PrmanTextures", None, -1))
        self.treeWidget.topLevelItem(0).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "file", None, -1))
        self.treeWidget.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "mayaTextures", None, -1))
        self.treeWidget.topLevelItem(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "gpuCaches", None, -1))
        self.treeWidget.topLevelItem(3).setText(0, QtWidgets.QApplication.translate("MainWindow", "RibArhives", None, -1))
        self.treeWidget.topLevelItem(4).setText(0, QtWidgets.QApplication.translate("MainWindow", "alembics", None, -1))
        self.treeWidget.topLevelItem(5).setText(0, QtWidgets.QApplication.translate("MainWindow", "cameras", None, -1))
        self.treeWidget.topLevelItem(6).setText(0, QtWidgets.QApplication.translate("MainWindow", "PrmanLights", None, -1))
        self.treeWidget.topLevelItem(7).setText(0, QtWidgets.QApplication.translate("MainWindow", "mayaLights", None, -1))
        self.treeWidget.topLevelItem(8).setText(0, QtWidgets.QApplication.translate("MainWindow", "fluidCaches", None, -1))
        self.treeWidget.topLevelItem(9).setText(0, QtWidgets.QApplication.translate("MainWindow", "particleCaches", None, -1))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_newWindow.setText(QtWidgets.QApplication.translate("MainWindow", "new window", None, -1))
        self.lineEdit.setText(QtWidgets.QApplication.translate("MainWindow", "# total polygons", None, -1))
        self.pushButton_testA.setText(QtWidgets.QApplication.translate("MainWindow", "testA", None, -1))
        self.pushButton_testB.setText(QtWidgets.QApplication.translate("MainWindow", "testB", None, -1))





class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #self.QTITEM.ACTION.connect(self.MODDEF)
        self.setupUi(self)
        self.proj = cmds.workspace(rd=True,q=True)

    #def self.MODDEF(self):
        self.defineFont()
        self.pushButton_newWindow.clicked.connect(self.test)
        self.pushButton_testA.clicked.connect(self.findGpuCaches)
        
        self.treeWidget.doubleClicked.connect(self.replaceFile)

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
        
        
        
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
        
        
        
    def createNewItem(self,topLayerIndex,index,nodeName,linkingFile,fontColor):
        #fontColor = self.fontColor
        #print index,nodeName,linkingFile,self.fontColor
        if len(linkingFile) > 0:
            pass
        else:
            linkingFile = 'N/A'
        print 'topLayerIndex',topLayerIndex
        print 'index',index
        print 'nodeName',nodeName
        print 'linkingFile',linkingFile
        print 'self.fontColor',self.fontColor
        
        

        textColor = (int(self.fontColor[0]), int(self.fontColor[1]), int(self.fontColor[2]))
        
        #        QtWidgets.QTreeWidgetItem(self.treeWidget).setForeground(0,self.brushLevelOne)  #create contain master ,and define font color
      #  QtWidgets.QTreeWidgetItem(self.treeWidget).setForeground(0,QtGui.QBrush(QtGui.QColor(247, 126, 128)))  #create contain master ,and define font color
        
       # #1.default exist , master should exist in top of treeWidget
       # self.treeWidget.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "master", None, -1))
      #  self.treeWidget.topLevelItem(0)#.setFont(0,self.fontLevelOne)#define font size
      
        QtWidgets.QTreeWidgetItem(self.treeWidget.topLevelItem(topLayerIndex))#.setForeground(0,self.brushLevelThree)  #build new item from index
        self.treeWidget.topLevelItem(topLayerIndex).child(index).setForeground(0,QtGui.QBrush(QtGui.QColor(int(self.fontColor[0]), int(self.fontColor[1]), int(self.fontColor[2]))))#.setFont(0,self.fontLevelThree)
        self.treeWidget.topLevelItem(topLayerIndex).child(index).setText(0, QtWidgets.QApplication.translate("MainWindow", 'tempName', None, -1))
        self.treeWidget.topLevelItem(topLayerIndex).child(index).setText(0,nodeName)
        self.treeWidget.topLevelItem(topLayerIndex).child(index).setCheckState(0, QtCore.Qt.Checked)
        self.treeWidget.topLevelItem(topLayerIndex).child(index).setForeground(1,QtGui.QBrush(QtGui.QColor(int(self.fontColor[0]), int(self.fontColor[1]), int(self.fontColor[2]))))#.setFont(0,self.fontLevelThree)

        self.treeWidget.topLevelItem(topLayerIndex).child(index).setText(1, QtWidgets.QApplication.translate("MainWindow", 'linkingFileLocation', None, -1))
        self.treeWidget.topLevelItem(topLayerIndex).child(index).setText(1,linkingFile)
  
  
  
  
  
  
  
  
    def checkFileExist(self,linkingFile,checkMode):  #checkMode = pxrTexture,mayaTexture,gpuCache,ribArchive,alembic,pxrLight,mayaFluid,mayanParticle
        print 'check file is existed'

        if os.path.isfile(linkingFile) == True:
            if checkMode == 'pxrTexture':
                print 'check the file is pxr texture'
                if linkingFile.split('.')[-1] == 'tex':
                    self.fontColor = (0,255,0)

                else:
                    self.fontColor =(255,255,0)
                    self.yellowCount = self.yellowCount +1
                    
            elif checkMode == 'mayaTexture':
                print 'check the file is surport maya image format'
                if linkingFile.split('.')[-1] in ['jpg','tif','png','exr','tga','iff','bmp','psd','dds','hdr']:
                    self.fontColor = (0,255,0)
                else:
                    self.fontColor =(255,255,0)
                    self.yellowCount = self.yellowCount +1
                    
            elif checkMode == 'gpuCache':
                print 'check the file is surport gpuCache format'
                if linkingFile.split('.')[-1] in ['abc']:
                    self.fontColor = (0,255,0)
                else:
                    self.fontColor =(255,255,0)
                    self.yellowCount = self.yellowCount +1
                                 
            elif checkMode == 'ribArchive':
                print 'check the file is surport ribArchive format'
                if linkingFile.split('.')[-1] in ['rib','zip','7z','gz']:
                    self.fontColor = (0,255,0)
                else:
                    self.fontColor =(255,255,0)
                    self.yellowCount = self.yellowCount +1
                                 
            elif checkMode == 'alembic':
                print 'check the file is surport alembic format'
                if linkingFile.split('.')[-1] in ['abc']:
                    self.fontColor = (0,255,0)
                else:
                    self.fontColor =(255,255,0)
                    self.yellowCount = self.yellowCount +1
                                 
            elif checkMode == 'pxrLight':
                print 'check the file is surport pxrLight format'
                if linkingFile.split('.')[-1] in ['tex','exr','tex']:
                    self.fontColor = (0,255,0)
                else:
                    self.fontColor =(255,255,0)
                    self.yellowCount = self.yellowCount +1
                                 
                                                                                                                                      
            elif checkMode == 'mayaFluid':
                print 'check the file is surport mayaFluid format'
                if linkingFile.split('.')[-1] in ['xml']:
                    self.fontColor = (0,255,0)
                else:
                    self.fontColor =(255,255,0)
                    self.yellowCount = self.yellowCount +1
                                                     
                    
                                                                                                                                      
            elif checkMode == 'mayanParticle':
                print 'check the file is surport mayanParticle format'
                if linkingFile.split('.')[-1] in ['xml']:
                    self.fontColor = (0,255,0)
                else:
                    self.fontColor =(255,255,0)
                    self.yellowCount = self.yellowCount +1
                                                     
                                        
                    
                    
             
            else:
                pass
                
           # self.setCheck = 0 
        else:
            self.fontColor =(255,0,0)
            self.setCheck = 1
            self.redCount = self.redCount +1
        

            
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
        
        self.treeWidget.clear()
    
    
    
    
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0.setCheckState(0, QtCore.Qt.Checked)
      #  item1 = QtWidgets.QTreeWidgetItem(self.treeWidget.topLevelItem(0).child(0))

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0.setCheckState(0, QtCore.Qt.Checked)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0.setCheckState(0, QtCore.Qt.Checked)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0.setCheckState(0, QtCore.Qt.Checked)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0.setCheckState(0, QtCore.Qt.Checked)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0.setCheckState(0, QtCore.Qt.Checked)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0.setCheckState(0, QtCore.Qt.Checked)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0.setCheckState(0, QtCore.Qt.Checked)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
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

        

        
        self.treeWidget.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_prmanTextures, None, -1))
        self.treeWidget.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_mayaTextures, None, -1))
        self.treeWidget.topLevelItem(2).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_gpuCaches, None, -1))
        self.treeWidget.topLevelItem(3).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_RibArchives, None, -1))
        self.treeWidget.topLevelItem(4).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_alembics, None, -1))
        self.treeWidget.topLevelItem(5).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_cameras, None, -1))
        self.treeWidget.topLevelItem(6).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_PrmanLights, None, -1))
        self.treeWidget.topLevelItem(7).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_fluidCaches, None, -1))
        self.treeWidget.topLevelItem(8).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_nParticleCaches, None, -1))
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
        
        
    def test(self):
        self.findPrmanTexture()
        self.findMayaTexture()

        self.findGpuCaches()

        self.findRibArchives()

        self.findAlembics()
      #  self.findCameras()
        self.findPrmanLights()
        self.mayaFluidCache()
        self.mayanParticleCache()
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
            
        print camerasInfo
        print self.countN6



        


        
        
            
    def findPrmanTexture(self):  # store PrmanTextures NodeName and location 
        
        pxrNodes = cmds.ls( typ ='PxrTexture')
        pxrTexturePath = {}
        for i in pxrNodes:
            path = cmds.getAttr('%s.filename'%i)
            pxrTexturePath.update({i:{'linkingFile':path}})
           
        self.countN1 = len(pxrNodes)
            
        print self.countN1
        self.yellowCount = 0
        self.redCount = 0
        for index in range(0,len(pxrTexturePath.keys())):
            nodeName = pxrTexturePath.keys()[index]
            linkingFile = pxrTexturePath[nodeName]['linkingFile']
            
            self.checkFileExist(linkingFile,'pxrTexture')   
            topLayerIndex = 0
            self.createNewItem(topLayerIndex,index,nodeName,linkingFile,self.fontColor)
        print pxrTexturePath
        self.setTopLayerItemColor(topLayerIndex)         
        
        
        
        
     #cmds.nodeType('file2')       
         #aa= cmds.ls(typ='file') 
        # cmds.select(aa)
    def findMayaTexture(self):  # store mayaNodeName and location 
        
        mayaTextureFileNode = cmds.ls( typ ='file')
        mayaTextureFilePath = {}
        for i in mayaTextureFileNode:
            path = cmds.getAttr('%s.fileTextureName'%i)
            mayaTextureFilePath.update({i:{'linkingFile':path}})
           
        self.countN2 = len(mayaTextureFileNode)
        self.yellowCount = 0
        self.redCount = 0            
        print self.countN2
        for index in range(0,len(mayaTextureFilePath.keys())):
            nodeName = mayaTextureFilePath.keys()[index]
            linkingFile = mayaTextureFilePath[nodeName]['linkingFile']
            self.checkFileExist(linkingFile,'mayaTexture')   
            #print 'index',index
           # print 'nodeName',nodeName
            #print 'linkingFile',linkingFile
            #print 'self.fontColor',self.fontColor
            topLayerIndex = 1

            self.createNewItem(topLayerIndex,index,nodeName,linkingFile,self.fontColor)
            
        self.setTopLayerItemColor(topLayerIndex)         
            
            
            
                        
            
            
            
            
            
            
        



#cmds.nodeType('pCone1RibArchiveGPUCacheShape')
    def findGpuCaches(self): # store mayaTextures NodeName and location  
      #  pxrFilePath = 'file.fileTextureName'
        
        gpuCacheNodes = cmds.ls( typ ='gpuCache')
        gpuCachePath = {}
        for i in gpuCacheNodes:
            path = cmds.getAttr('%s.cacheFileName'%i)
            gpuCachePath.update({i:{'linkingFile':path}})
            
        self.countN3 = len(gpuCacheNodes)
        self.yellowCount = 0
        self.redCount = 0              

        for index in range(0,len(gpuCachePath.keys())):
            nodeName = gpuCachePath.keys()[index]
            linkingFile = gpuCachePath[nodeName]['linkingFile']
            self.checkFileExist(linkingFile,'gpuCache')   
            #print 'index',index
           # print 'nodeName',nodeName
            #print 'linkingFile',linkingFile
            #print 'self.fontColor',self.fontColor
            topLayerIndex = 2

            self.createNewItem(topLayerIndex,index,nodeName,linkingFile,self.fontColor)
        self.setTopLayerItemColor(topLayerIndex)         




            
    def findRibArchives(self): # store RibArchives NodeName and location 
        
        RibArchivesNodes = cmds.ls( typ ='RenderManArchive')
        RibArchivesPath = {}
        for i in RibArchivesNodes:
            path = self.proj +cmds.getAttr('%s.filename'%i)
            RibArchivesPath.update({i:{'linkingFile':path}})
            
        self.countN4 = len(RibArchivesNodes)
        self.yellowCount = 0
        self.redCount = 0              
        for index in range(0,len(RibArchivesPath.keys())):
            nodeName = RibArchivesPath.keys()[index]
            linkingFile = RibArchivesPath[nodeName]['linkingFile']
            self.checkFileExist(linkingFile,'ribArchive')   
            topLayerIndex = 3
            self.createNewItem(topLayerIndex,index,nodeName,linkingFile,self.fontColor)
        self.setTopLayerItemColor(topLayerIndex)         
        
        
    def findAlembics(self): # store alembics NodeName and location 
        
        alembicNodes = cmds.ls( typ ='AlembicNode')
        alembicPath = {}
        for i in alembicNodes:
            path = cmds.getAttr('%s.abc_File'%i)
            alembicPath.update({i:{'linkingFile':path}})
            
        self.countN5 = len(alembicNodes)
        self.yellowCount = 0
        self.redCount = 0              
        for index in range(0,len(alembicPath.keys())):
            nodeName = alembicPath.keys()[index]
            linkingFile = alembicPath[nodeName]['linkingFile']
            self.checkFileExist(linkingFile,'alembic')   
            topLayerIndex = 4
            self.createNewItem(topLayerIndex,index,nodeName,linkingFile,self.fontColor)
            
        self.setTopLayerItemColor(topLayerIndex)         
            
            
        
    def findPrmanLights(self): # store PrmanLights NodeName and location 
        
        prmanLightType =['PxrRectLight','PxrDiskLight','PxrDistantLight','PxrSphereLight','PxrDomeLight','PxrEnvDayLight','PxrMeshLight']
        prmanLightNodes = []
        prmanLightInfo = {}
        for prmanNodeType in prmanLightType:
            prmanLightNodes = prmanLightNodes + cmds.ls( typ =prmanNodeType)
            
        print prmanLightNodes 
        self.yellowCount = 0
        self.redCount = 0         
        for i in prmanLightNodes:
            intensity = cmds.getAttr('%s.intensity'%i)
            exposure = cmds.getAttr('%s.exposure'%i)
            if cmds.nodeType(i) == 'PxrEnvDayLight' :  
                lightColor = 'N/A'
            else :
                lightColor = cmds.getAttr('%s.lightColor'%i)  
                
                                     
            if cmds.nodeType(i) == 'PxrRectLight' :           
                lightColorMap = cmds.getAttr('%s.lightColorMap'%i)
            else:
                lightColorMap = 'N/A'
                
            if cmds.nodeType(i) == 'PxrDomeLight' :           
                lightColorMap = cmds.getAttr('%s.lightColorMap'%i)
            else:
                lightColorMap = 'N/A'
                
                             
            if cmds.nodeType(i) == 'PxrMeshLight' :           
                textureColor = cmds.getAttr('%s.textureColor'%i)
            else:
                textureColor = 'N/A' 
                
                
            if cmds.nodeType(i) == 'PxrDistantLight' :           
                angleExtent = cmds.getAttr('%s.angleExtent'%i)
            else:
                angleExtent = 'N/A'
            
            prmanLightInfo.update({i:{'intensity':intensity,
                                      'exposure':exposure,
                                      'lightColor':lightColor,
                                      'linkingFile':lightColorMap, #lightColorMap
                                      'angleExtent':angleExtent,
                                      'textureColor':textureColor,
                                      
                                      }})

        self.countN7 = len(prmanLightInfo.keys())
        
        for index in range(0,len(prmanLightInfo.keys())):
            nodeName = prmanLightInfo.keys()[index]
            linkingFile = prmanLightInfo[nodeName]['linkingFile']
            self.checkFileExist(linkingFile,'pxrLight')   
            topLayerIndex = 6
            self.createNewItem(topLayerIndex,index,nodeName,linkingFile,self.fontColor)
        self.setTopLayerItemColor(topLayerIndex)         


#cmds.listConnections('nParticleShape1')        
    def mayaFluidCache(self): # store mayaTextures NodeName and location 
      #  pxrFilePath = 'file.fileTextureName'
      
        mayaFluidCacheInfo = {}
        
        mayaFileNodes = cmds.ls( typ ='fluidShape')
        
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
          
        self.countN9 = len(mayaFluidCacheInfo.keys())
        self.yellowCount = 0
        self.redCount = 0              
        for index in range(0,len(mayaFluidCacheInfo.keys())):
            nodeName = mayaFluidCacheInfo.keys()[index]
            linkingFile = mayaFluidCacheInfo[nodeName]['linkingFile']
            self.checkFileExist(linkingFile,'mayaFluid')   
            topLayerIndex = 7
            self.createNewItem(topLayerIndex,index,nodeName,linkingFile,self.fontColor)
        self.setTopLayerItemColor(topLayerIndex)         

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
        self.yellowCount = 0
        self.redCount = 0                      
        for index in range(0,len(mayanParticleCacheInfo.keys())):
            nodeName = mayanParticleCacheInfo.keys()[index]
            linkingFile = mayanParticleCacheInfo[nodeName]['linkingFile']
            self.checkFileExist(linkingFile,'mayanParticle')   
            topLayerIndex = 8
            self.createNewItem(topLayerIndex,index,nodeName,linkingFile,self.fontColor)
        
        
        self.setTopLayerItemColor(topLayerIndex)         
          
        self.countN10 = len(mayanParticleCacheInfo.keys())
            
        print mayanParticleCacheInfo
        print self.countN10
            
        
    def setTopLayerItemColor(self,topLayerIndex):
        if self.redCount > 0:

            self.topLayerColor = (255,0,0)
        
        else:
            
            if self.yellowCount >0 :
                self.topLayerColor = (255,255,0)
                
            else:
                self.topLayerColor = (255,255,255)
                
        self.treeWidget.topLevelItem(topLayerIndex).setForeground(0,QtGui.QBrush(QtGui.QColor(int(self.topLayerColor[0]), int(self.topLayerColor[1]), int(self.topLayerColor[2]))))

        
        

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


 