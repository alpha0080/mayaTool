# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha/Documents/GitHub/ribGen/publishTool/publishToolPreVer_02_UI.ui'
#
# Created: Mon Mar 06 22:29:07 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!
from PySide2 import QtCore, QtGui, QtWidgets
import os
import maya.cmds as cmds
import pymel.core as pm


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1141, 789)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 205, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(95, 134, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 101, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(151, 125, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(158, 164, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 205, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 224, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 101, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(151, 125, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(158, 164, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 101, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 205, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 224, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 101, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(151, 125, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 101, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 101, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton_Master = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_Master.setGeometry(QtCore.QRect(210, 30, 48, 16))
        self.radioButton_Master.setObjectName("radioButton_Master")
        self.radioButton_branches = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_branches.setGeometry(QtCore.QRect(270, 30, 65, 16))
        self.radioButton_branches.setObjectName("radioButton_branches")
        self.radioButton_temp = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_temp.setGeometry(QtCore.QRect(340, 30, 69, 16))
        self.radioButton_temp.setObjectName("radioButton_temp")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 30, 141, 41))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, -1, -1, 0)
        self.formLayout.setSpacing(5)
        self.formLayout.setObjectName("formLayout")
        self.radioButton_assets = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton_assets.setObjectName("radioButton_assets")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.radioButton_assets)
        self.radioButton_shots = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton_shots.setObjectName("radioButton_shots")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.radioButton_shots)
        self.radioButton_published = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton_published.setObjectName("radioButton_published")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.radioButton_published)
        self.pushButton_assets = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_assets.setGeometry(QtCore.QRect(40, 100, 131, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        self.pushButton_assets.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton_assets.setFont(font)
        self.pushButton_assets.setAcceptDrops(False)
        self.pushButton_assets.setAutoFillBackground(False)
        self.pushButton_assets.setInputMethodHints(QtCore.Qt.ImhNone)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/number_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_assets.setIcon(icon)
        self.pushButton_assets.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_assets.setObjectName("pushButton_assets")
        self.pushButton_shots = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_shots.setGeometry(QtCore.QRect(40, 140, 131, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        self.pushButton_shots.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton_shots.setFont(font)
        self.pushButton_shots.setAcceptDrops(False)
        self.pushButton_shots.setAutoFillBackground(False)
        self.pushButton_shots.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton_shots.setIcon(icon)
        self.pushButton_shots.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_shots.setObjectName("pushButton_shots")
        self.listWidget_assetProj = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_assetProj.setGeometry(QtCore.QRect(180, 100, 221, 591))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listWidget_assetProj.setFont(font)
        self.listWidget_assetProj.setInputMethodHints(QtCore.Qt.ImhNone)
        self.listWidget_assetProj.setLineWidth(2)
        self.listWidget_assetProj.setMidLineWidth(1)
        self.listWidget_assetProj.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget_assetProj.setObjectName("listWidget_assetProj")
        QtWidgets.QListWidgetItem(self.listWidget_assetProj)
        QtWidgets.QListWidgetItem(self.listWidget_assetProj)
        QtWidgets.QListWidgetItem(self.listWidget_assetProj)
        QtWidgets.QListWidgetItem(self.listWidget_assetProj)
        QtWidgets.QListWidgetItem(self.listWidget_assetProj)
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(870, 110, 61, 341))
        self.listWidget_2.setObjectName("listWidget_2")
        QtWidgets.QListWidgetItem(self.listWidget_2)
        self.listWidget_3 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_3.setGeometry(QtCore.QRect(940, 110, 51, 341))
        self.listWidget_3.setObjectName("listWidget_3")
        QtWidgets.QListWidgetItem(self.listWidget_3)
        self.treeWidget_assetTree = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget_assetTree.setGeometry(QtCore.QRect(420, 100, 401, 591))
        self.treeWidget_assetTree.setObjectName("treeWidget_assetTree")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_assetTree)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_assetTree)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_assetTree)
        self.pushButton_branch = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_branch.setGeometry(QtCore.QRect(420, 56, 30, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(172, 224, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 224, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 224, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton_branch.setPalette(palette)
        self.pushButton_branch.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/branch_01.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_branch.setIcon(icon1)
        self.pushButton_branch.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_branch.setObjectName("pushButton_branch")
        self.pushButton_master = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_master.setGeometry(QtCore.QRect(970, 60, 30, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(172, 224, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 224, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 224, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton_master.setPalette(palette)
        self.pushButton_master.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/master_01.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_master.setIcon(icon2)
        self.pushButton_master.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_master.setObjectName("pushButton_master")
        self.comboBox_branches = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_branches.setGeometry(QtCore.QRect(460, 60, 101, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(117, 157, 151))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 157, 151))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 157, 151))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.comboBox_branches.setPalette(palette)
        self.comboBox_branches.setObjectName("comboBox_branches")
        self.comboBox_branches.addItem("")
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(400, 59, 20, 661))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1141, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.radioButton_Master.setText(QtWidgets.QApplication.translate("MainWindow", "Master", None, -1))
        self.radioButton_branches.setText(QtWidgets.QApplication.translate("MainWindow", "Branches", None, -1))
        self.radioButton_temp.setText(QtWidgets.QApplication.translate("MainWindow", "temp", None, -1))
        self.radioButton_assets.setText(QtWidgets.QApplication.translate("MainWindow", "Assets", None, -1))
        self.radioButton_shots.setText(QtWidgets.QApplication.translate("MainWindow", "Shots", None, -1))
        self.radioButton_published.setText(QtWidgets.QApplication.translate("MainWindow", "Published", None, -1))
        self.pushButton_assets.setText(QtWidgets.QApplication.translate("MainWindow", "  Assets", None, -1))
        self.pushButton_shots.setText(QtWidgets.QApplication.translate("MainWindow", "  Shots", None, -1))
        __sortingEnabled = self.listWidget_assetProj.isSortingEnabled()
        self.listWidget_assetProj.setSortingEnabled(False)
        self.listWidget_assetProj.item(0).setText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.listWidget_assetProj.item(1).setText(QtWidgets.QApplication.translate("MainWindow", "2", None, -1))
        self.listWidget_assetProj.item(2).setText(QtWidgets.QApplication.translate("MainWindow", "3", None, -1))
        self.listWidget_assetProj.item(3).setText(QtWidgets.QApplication.translate("MainWindow", "4", None, -1))
        self.listWidget_assetProj.item(4).setText(QtWidgets.QApplication.translate("MainWindow", "5", None, -1))
        self.listWidget_assetProj.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        self.listWidget_2.item(0).setText(QtWidgets.QApplication.translate("MainWindow", "update", None, -1))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        self.listWidget_3.item(0).setText(QtWidgets.QApplication.translate("MainWindow", "user", None, -1))
        self.listWidget_3.setSortingEnabled(__sortingEnabled)
        self.treeWidget_assetTree.headerItem().setText(0, QtWidgets.QApplication.translate("MainWindow", "anna", None, -1))
        __sortingEnabled = self.treeWidget_assetTree.isSortingEnabled()
        self.treeWidget_assetTree.setSortingEnabled(False)
        self.treeWidget_assetTree.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "master_", None, -1))
        self.treeWidget_assetTree.topLevelItem(0).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "anna_01", None, -1))
        self.treeWidget_assetTree.topLevelItem(0).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "anna_02", None, -1))
        self.treeWidget_assetTree.topLevelItem(0).child(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "anna_03", None, -1))
        self.treeWidget_assetTree.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "branch_01", None, -1))
        self.treeWidget_assetTree.topLevelItem(1).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "branch_01_01", None, -1))
        self.treeWidget_assetTree.topLevelItem(1).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "branch_01_02", None, -1))
        self.treeWidget_assetTree.topLevelItem(1).child(1).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "branch_01_02_01", None, -1))
        self.treeWidget_assetTree.topLevelItem(1).child(1).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "branch_01_02_02", None, -1))
        self.treeWidget_assetTree.topLevelItem(1).child(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "branch_01_03", None, -1))
        self.treeWidget_assetTree.topLevelItem(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "branch_02", None, -1))
        self.treeWidget_assetTree.setSortingEnabled(__sortingEnabled)
        self.comboBox_branches.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "master", None, -1))

      
    ##------------------------------------sign---------------------------------------------
    
class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #self.QTITEM.ACTION.connect(self.MODDEF)
    #def self.MODDEF(self):
        
        
        # self.setWindowFlags(QtCore.Qt.Tool)
        self.setupUi(self)
        
        self.pushButton_assets.clicked.connect(self.modpushButton_assets)
        
        self.pushButton_shots.clicked.connect(self.modpushButton_shots)

        self.pushButton_branch.clicked.connect(self.modpushButton_branch)
        
        self.pushButton_master.clicked.connect(self.modpushButton_master)

    def popUpwindow(self):
        window = cmds.window(t="input window",h=100,w=400,s=0)
        cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 0), columnWidth=[(1, 100), (2, 250)] )
        cmds.text( label='Name' )
        name = cmds.textField()
        cmds.text( label='Address' )
        address = cmds.textField()
        cmds.text( label='Phone Number' )
        phoneNumber = cmds.textField()
        cmds.text( label='Email' )
        email = cmds.textField()

        #    Attach commands to pass focus to the next field if the Enter
        #    key is pressed. Hitting just the Return key will keep focus
        #    in the current field.
        #
        cmds.textField( name, edit=True, enterCommand=('cmds.setFocus(\"' + address + '\")') )
        cmds.textField( address, edit=True, enterCommand=('cmds.setFocus(\"' + phoneNumber + '\")') )
        cmds.textField( phoneNumber, edit=True, enterCommand=('cmds.setFocus(\"' + email + '\")') )
        cmds.textField( email, edit=True, enterCommand=('cmds.setFocus(\"' + name + '\")') )

        cmds.showWindow( window )
        
        
        
        
    def modpushButton_master(self):
        #cmds.workspaceLayoutManager( listLayouts=True )
        
        try:
            cmds.deleteUI( self.branchCreateWindow, control=True )
        except:
            pass
            
                  




        branchDict = {'1':{'master':[]},
                      '2':{'branch_01':[]},
                      '3':{'branch_02':[]},
                      '4':{'branch_03':[]}
                      }

        for i in branchDict.keys():
            print i
                      
        self.branchCreateWindow = cmds.window(t="branchCreateWindow",h=100,w=400,s=0)
        cmds.rowColumnLayout( numberOfColumns=2 , columnAttach=(1, 'right', 5), columnWidth=[(1, 100), (2, 250)],rs=(5,5),cs=(5,5))
        cmds.text(' ')
        cmds.text(' ')
        cmds.text( label='Name' )
        name = cmds.textField()

        cmds.text( label='From Branch' )
        cmds.optionMenu()#, changeCommand=printNewMenuItem )
        cmds.menuItem( label='Master' )
      #  cmds.menuItem( label='Branch_01' )
      #  cmds.menuItem( label='Branch_02' )
        #address = cmds.textField()
        ##cmds.text( label='Phone Number' )
        #phoneNumber = cmds.textField()
        #cmds.text( label='Email' )
        #email = cmds.textField()

        #    Attach commands to pass focus to the next field if the Enter
        #    key is pressed. Hitting just the Return key will keep focusrowSpacing
        #    in the current field.
        #
       # cmds.textField( name, edit=True, enterCommand=('cmds.setFocus(\"' + address + '\")') )

        cmds.showWindow( self.branchCreateWindow )

        
    
    def modpushButton_branch(self):
        self.popUpwindow()
        print "aaaaaaaaaaaaaaaaa"


        
        

            
            
    def modpushButton_assets(self):
        print "get info from asset dir"

        self.getProjInfo()

        self.dirGive = 'assets'   # set self.dirGive ,in self.treeList module
        self.treeList(self.dirGive)  
        print self.topLevelItem    #return keys,topLevelItems under Projects

        self.itemCount = self.topLevelItemCount
        self.itemList = self.topLevelItem
        #print self.itemCount, self.itemList
        
        self.assetItemListCreate(self.itemCount,self.itemList)  #create topLevelItem form self.TreeTopLeveItemCreate module, self.itemCount 'int',self.itemList = 'list'
        
        
        
    def modpushButton_shots(self):
        print "get info from shot dir"

        self.getProjInfo()
        
        self.dirGive = 'shots'
        self.treeList(self.dirGive)  
        
        self.itemCount = self.topLevelItemCount
        self.itemList = self.topLevelItem
        print self.topLevelItem    #return keys,topLevelItems under Projects

        #print self.itemCount, self.itemList
        
        self.assetItemListCreate(self.itemCount,self.itemList) 
        
        

    #------------------------- create TopLevelItem Start -------------------------------------------------------------------------
    def TreeTopLeveItemCreate(self,itemCount,itemList):
        print self.itemCount
        print self.itemList
        print "create topLevel Items"
        num_item_0 =1
        while num_item_0 < self.itemCount:
            item_0 = QtWidgets.QTreeWidgetItem(self.treeWidgetDir)
            num_item_0 = num_item_0 +1

        for i in range(0,self.itemCount):
            topLevelItem = self.treeWidgetDir.topLevelItem(i)
            tempName = "tempName"
            topLevelItem.setText(QtWidgets.QApplication.translate("MainWindow",tempName))  #topLevelItem named "tempName"
            #topLevelItem.setText(self.itemList[i])  #change tempName to folder Name , in isDirList
            
            
            
    #-------------------------create Item List, projectBase ,from assets,shots, publish,global 
    def assetItemListCreate(self,itemCount,itemList):
        self.listWidget_assetProj.clear()
        
        num_item_0 =0
        while num_item_0 < self.itemCount:
            # create number of itemCount items in List
            QtWidgets.QListWidgetItem(self.listWidget_assetProj)

            num_item_0 = num_item_0 +1        
        


        for i in range(0,self.itemCount):

            tempName = "tempName"
            #try:
            listItem = self.listWidget_assetProj.item(i)
            listItem.setText(QtWidgets.QApplication.translate("MainWindow",tempName))
            listItem.setText(self.itemList[i])
           # except:
               # pass

        
        
    def temp(self):
        print "create topLevel Items"
        for i in range(0,self.itemCount):

            topLevelItemName = self.isDirList[i]

            #name = topLevelItemName
            tempName = "tempName"
           # self.treeWidget.topLevelItem(i).setText(0, QtWidgets.QApplication.translate("MainWindow", name, None, -1))
            topLevelItem = self.treeWidget.topLevelItem(i)
            topLevelItem.setText(0, QtWidgets.QApplication.translate("MainWindow",tempName))  #topLevelItem named "tempName"
            topLevelItem.setText(0,topLevelItemName)  #change tempName to folder Name , in isDirList
                    
        
        
        
    def callTest(self,caller):
        print self.caller
        
    #-------------------get current project--------------------------------------------------------
        
    def getProjInfo(self):
        
        
       # self.path = cmds.fileDialog2(fm=2)[0]
        self.path = "C:/mayaProjs/projectPP"   

        print self.path
        
    def getFileInfor(self):

        self.dirObjs = os.listdir(self.path)
        self.ObjsCount = len(self.dirObjs)
        #collect files that as the file filter
        self.isDirList = []
        self.isFileList = []
        self.fileFilter = ['.ma','.mb','.rib','.abc']
        for obj in self.dirObjs:
            pathObj = self.path + '/'+u'%s'%obj
            print pathObj
            if os.path.splitext(pathObj)[1] in self.fileFilter:                 
                self.isFileList.append(obj)
            elif os.path.splitext(pathObj)[1] == "":
                self.isDirList.append(obj)
                
        print self.path
        print self.dirObjs
        print self.ObjsCount
        print "isDirList:    ", self.isDirList
        print "isFileList:    ", self.isFileList
        
        
        

    def treeList(self,dirGive):
        #this module, will return dirTree, self.treeInfoDict,
        #self.path = "C:/mayaProjs/vdbDevelop"

        #--------------------get dirTree info from workspace Start-------------------------------------------
        self.rootList = []
        self.allFileNameList = []
        self.treeInfoDict ={}
        pathTextList = self.path.split('/')
        levelCount = len(pathTextList)   # get the depth  of root, search in self.treeInfoDict
            
        for root, dirs, files in os.walk(self.path):

            rootRemix = self.path+'/'.join(root.split(self.path)[-1].split('\\'))
        #    print rootRemix
            ## find all files 
            for singleFileName in files:

                        
                filePath = os.path.join(root, singleFileName)
                #rename filePath to newFilePathName, '\\' to '/'
                newFilePathName = ''    
                for cha in filePath:
                    if cha != '\\':
                        newFilePathName += cha
                    else:
                        newFilePathName += '/'
                
                filePath = os.path.join(root, newFilePathName)
                self.rootList.append(filePath)

            self.rootList.append(rootRemix)       
            


        for item in self.rootList:
            p = self.treeInfoDict
            for x in item.split('/'):
                p = p.setdefault(x, {})
                

        #--------------------get dirTree info from workspace END-------------------------------------------
        
        #--------------------Return dir info from self.treeIndoDict ------------------------------------------
        
        i=0
        #newDict=treeInfoDict.keys()[0]
        while i < levelCount:

            self.treeInfoDict = self.treeInfoDict['%s'%self.treeInfoDict.keys()[0]]

            i=i+1
            
        self.dirUnderSelectPath = self.treeInfoDict                    #return dict under project
        print self.dirUnderSelectPath
       # print self.treeInfoDict     
        #print self.dirUnderSelectPath['%s'%self.dirGive]                #return dict under select dir under project
        #print self.dirGive

        self.topLevelItem = self.dirUnderSelectPath[self.dirGive].keys()           #return keys,topLevelItems under Projects
        #print self.topLevelItem                
        self.topLevelItemCount = len(self.topLevelItem)                #return counts of topLevelItems
        #print self.topLevelItemCount



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


 
 