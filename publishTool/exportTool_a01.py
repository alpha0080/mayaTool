# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha/Documents/GitHub/mayaTool/publishTool/exportTool_UI_a01.ui'
#
# Created: Sat Jun 10 23:03:59 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

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
        self.treeWidget.setRootIsDecorated(False)
        self.treeWidget.setUniformRowHeights(False)
        self.treeWidget.setItemsExpandable(True)
        self.treeWidget.setAllColumnsShowFocus(False)
        self.treeWidget.setWordWrap(False)
        self.treeWidget.setExpandsOnDoubleClick(True)
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setObjectName("treeWidget")
   

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

        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_newWindow.setText(QtWidgets.QApplication.translate("MainWindow", "new window", None, -1))
        self.lineEdit.setText(QtWidgets.QApplication.translate("MainWindow", "# total polygons", None, -1))




class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #self.QTITEM.ACTION.connect(self.MODDEF)
        self.setupUi(self)
    #def self.MODDEF(self):
    
        self.buildItemTree()
    
    
    
    
            
    def buildItemTree(self):
        
        self.treeWidget.clear()
    
    
    
    
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

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0.setCheckState(0, QtCore.Qt.Checked)

        #item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        #item_0.setCheckState(0, QtCore.Qt.Checked)
        
        countN1 = 0
        countN2 = 0
        countN3 = 0
        countN4 = 0
        countN5 = 0
        countN6 = 0
        countN7 = 0
       # countN8 = 0
        countN9 = 0
        countN10 = 0


        
        self.itemName_prmanTextures = "PrmanTextures"+'__('+'%03d'%countN1+')'
        self.itemName_mayaTextures = "mayaTextures"+'__('+'%03d'%countN2+')'
        self.itemName_gpuCaches = "gpuCaches"+'__('+'%03d'%countN3+')'
        self.itemName_RibArchives = "RibArchives"+'__('+'%03d'%countN4+')'
        self.itemName_alembics = "alembics"+'__('+'%03d'%countN5+')'
        self.itemName_cameras = "cameras"+'__('+'%03d'%countN6+')'
        self.itemName_PrmanLights = "PrmanLights"+'__('+'%03d'%countN7+')'
        #self.itemName_mayaLights = "mayaLights"+'__('+'%03d'%countN8+')'
        self.itemName_fluidCaches = "fluidCaches"+'__('+'%03d'%countN9+')'
        self.itemName_particleCaches = "particleCaches"+'__('+'%03d'%countN10+')'

        

        
        self.treeWidget.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_prmanTextures, None, -1))
        self.treeWidget.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_mayaTextures, None, -1))
        self.treeWidget.topLevelItem(2).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_gpuCaches, None, -1))
        self.treeWidget.topLevelItem(3).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_RibArchives, None, -1))
        self.treeWidget.topLevelItem(4).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_alembics, None, -1))
        self.treeWidget.topLevelItem(5).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_cameras, None, -1))
        self.treeWidget.topLevelItem(6).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_PrmanLights, None, -1))
        self.treeWidget.topLevelItem(7).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_mayaLights, None, -1))
        self.treeWidget.topLevelItem(8).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_fluidCaches, None, -1))
        self.treeWidget.topLevelItem(9).setText(0, QtWidgets.QApplication.translate("MainWindow",self.itemName_particleCaches, None, -1))
        
        '''
         linkingSearchDict = {
                              'PxrTexture':'filename',
                              'file':'fileTextureName',
                              'AlembicNode':'abc_File',
                              'gpuCache':'cacheFileName',
                              'RenderManArchive':'filename'}
                              
        '''   
        
        self.pushButton_newWindow.clicked.connect(self.test)
        
    def test(self):
        self.findPrmanTexture()
        self.findMayaTextures()
        self.findGpuCaches()
        self.findRibArchives()
        self.findAlembics()
        self.findCameras()
        self.findPrmanLights()
        
#cmds.nodeType('nParticleShape1Cache1')

    def findPrmanLights(self): # store PrmanLights NodeName and location 
        
        prmanLightType =['PxrRectLight','PxrDiskLight','PxrDistantLight','PxrSphereLight','PxrDomeLight','PxrEnvDayLight','PxrMeshLight']
        prmanLightNodes = []
        prmanLightInfo = {}
        for prmanNodeType in prmanLightType:
            prmanLightNodes = prmanLightNodes + cmds.ls( typ =prmanNodeType)
            
        print prmanLightNodes 
       
        for i in prmanLightNodes:
            intensity = cmds.getAttr('%s.intensity'%i)
            exposure = cmds.getAttr('%s.exposure'%i)
            if cmds.nodeType(i) == 'PxrEnvDayLight' :  
                lightColor = 'none'
            else :
                lightColor = cmds.getAttr('%s.lightColor'%i)  
                
                                     
            if cmds.nodeType(i) == 'PxrRectLight' :           
                lightColorMap = cmds.getAttr('%s.lightColorMap'%i)
            else:
                lightColorMap = 'none'
                
            if cmds.nodeType(i) == 'PxrDomeLight' :           
                lightColorMap = cmds.getAttr('%s.lightColorMap'%i)
            else:
                lightColorMap = 'none'
                
                             
            if cmds.nodeType(i) == 'PxrMeshLight' :           
                textureColor = cmds.getAttr('%s.textureColor'%i)
            else:
                textureColor = 'none' 
                
                
            if cmds.nodeType(i) == 'PxrDistantLight' :           
                angleExtent = cmds.getAttr('%s.angleExtent'%i)
            else:
                angleExtent = 'none'
            
            prmanLightInfo.update({i:{'intensity':intensity,
                                      'exposure':exposure,
                                      'lightColor':lightColor,
                                      'lightColorMap':lightColorMap,
                                      'angleExtent':angleExtent,
                                      'textureColor':textureColor,
                                      
                                      }})

        self.countN7 = len(prmanLightInfo.keys())
        print prmanLightInfo
        print self.countN7
       
            
        '''
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
        
    '''

        
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

        
        
    def findAlembics(self): # store alembics NodeName and location 
        
        alembicNodes = cmds.ls( typ ='AlembicNode')
        alembicPath = {}
        for i in alembicNodes:
            path = cmds.getAttr('%s.abc_File'%i)
            alembicPath.update({i:path})
            
        self.countN5 = len(alembicNodes)
            
        print alembicPath
        print self.countN5
        
        
    def findNParticleCache(self): # store nParticles NodeName and location 
#cmds.listConnections('nParticleShape1Cache1',t='playFromCache')
        nParticleNode = cmds.ls( typ ='cacheFile')
        nParticleCachePath = {}
        for i in alembicNodes:
            baseDirectory = cmds.getAttr('%s.cachePath'%i)
            baseName = cmds.getAttr('%s.cacheName'%i)
            isEnable = cmds.getAttr('%s.isEnable'%i)
            startFrame = cmds.getAttr('%s.startFrame'%i)
            scale = cmds.getAttr('%s.scale'%i)
            hold = cmds.getAttr('%s.hold'%i)
            preCycle = cmds.getAttr('%s.preCycle'%i)
            postCycle = cmds.getAttr('%s.postCycle'%i)
            sourceStart = cmds.getAttr('%s.sourceStart'%i)
            sourceEnd = cmds.getAttr('%s.sourceEnd'%i)
            originalStart = cmds.getAttr('%s.originalStart'%i)
            originalEnd= cmds.getAttr('%s.originalEnd'%i)
            
            
            

            
            alembicPath.update({i:path})
            
        self.countN5 = len(alembicNodes)
            
        print alembicPath
        print self.countN5
    
    def findRibArchives(self): # store RibArchives NodeName and location 
        
        RibArchivesNodes = cmds.ls( typ ='RenderManArchive')
        RibArchivesPath = {}
        for i in RibArchivesNodes:
            path = cmds.getAttr('%s.filename'%i)
            RibArchivesPath.update({i:path})
            
        self.countN4 = len(RibArchivesNodes)
            
        print RibArchivesPath
        print self.countN4
                
        
            
    def findPrmanTexture(self):  # store PrmanTextures NodeName and location 
        #pxrFilePath = 'PxrTexture.filename' 
        
        pxrNodes = cmds.ls( typ ='PxrTexture')
        pxrTexturePath = {}
        for i in pxrNodes:
            path = cmds.getAttr('%s.filename'%i)
            pxrTexturePath.update({i:path})
            
        self.countN1 = len(pxrNodes)
            
        print pxrTexturePath
        print self.countN1
        
        
    def findMayaTextures(self): # store mayaTextures NodeName and location 
      #  pxrFilePath = 'file.fileTextureName'
        
        mayaFileNodes = cmds.ls( typ ='file')
        mayaFilePath = {}
        for i in mayaFileNodes:
            path = cmds.getAttr('%s.fileTextureName'%i)
            mayaFilePath.update({i:path})
            
        self.countN2 = len(mayaFileNodes)
            
        print mayaFilePath
        print self.countN2
        
        

    def findGpuCaches(self): # store mayaTextures NodeName and location 
      #  pxrFilePath = 'file.fileTextureName'
        
        gpuCacheNodes = cmds.ls( typ ='gpuCache')
        gpuCachePath = {}
        for i in gpuCacheNodes:
            path = cmds.getAttr('%s.cacheFileName'%i)
            gpuCachePath.update({i:path})
            
        self.countN3 = len(gpuCacheNodes)
            
        print gpuCachePath
        print self.countN3
                
        
        
        
        
        
        
        
        
        
        

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


 