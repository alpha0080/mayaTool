# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha/Documents/GitHub/ribGen/publishTool/createbranchtest_01.ui'
#
# Created: Fri Mar 17 00:34:42 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import json , os , getpass,socket
import datetime


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.setFontSize=5

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(582, 712)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget_branch = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_branch.setGeometry(QtCore.QRect(0, 0, 591, 701))
        self.tabWidget_branch.setObjectName("tabWidget_branch")
        self.tab_branch = QtWidgets.QWidget()
        self.tab_branch.setObjectName("tab_branch")
        self.lineEdit_branchName = QtWidgets.QLineEdit(self.tab_branch)
        self.lineEdit_branchName.setGeometry(QtCore.QRect(10, 440, 261, 41))
        self.lineEdit_branchName.setText("")
        self.lineEdit_branchName.setObjectName("lineEdit_branchName")
        self.pushButton_editFileInfo = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_editFileInfo.setGeometry(QtCore.QRect(450, 320, 31, 31))
        self.pushButton_editFileInfo.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/editY.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_editFileInfo.setIcon(icon)
        self.pushButton_editFileInfo.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_editFileInfo.setAutoDefault(False)
        self.pushButton_editFileInfo.setDefault(False)
        self.pushButton_editFileInfo.setFlat(True)
        self.pushButton_editFileInfo.setObjectName("pushButton_editFileInfo")
        self.pushButton_mergeToMaster = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_mergeToMaster.setGeometry(QtCore.QRect(310, 500, 231, 41))
        self.pushButton_mergeToMaster.setObjectName("pushButton_mergeToMaster")
        self.pushButton_createNewBranch = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_createNewBranch.setGeometry(QtCore.QRect(310, 440, 231, 41))
        self.pushButton_createNewBranch.setObjectName("pushButton_createNewBranch")
        self.textBrowser_BranchFileInfo = QtWidgets.QTextBrowser(self.tab_branch)
        self.textBrowser_BranchFileInfo.setGeometry(QtCore.QRect(190, 160, 351, 151))
        self.textBrowser_BranchFileInfo.setMidLineWidth(1)
        self.textBrowser_BranchFileInfo.setTabChangesFocus(False)
        self.textBrowser_BranchFileInfo.setReadOnly(False)
        self.textBrowser_BranchFileInfo.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.textBrowser_BranchFileInfo.setOpenExternalLinks(True)
        self.textBrowser_BranchFileInfo.setObjectName("textBrowser_BranchFileInfo")
        self.label = QtWidgets.QLabel(self.tab_branch)
        self.label.setGeometry(QtCore.QRect(10, 410, 161, 21))
        self.label.setObjectName("label")
        self.treeWidget_branches = QtWidgets.QTreeWidget(self.tab_branch)
        self.treeWidget_branches.setGeometry(QtCore.QRect(10, 0, 171, 311))
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
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_branches)
        font = QtGui.QFont()
        font.setUnderline(True)
        brush = QtGui.QBrush(QtGui.QColor(215, 255, 208))
        brush.setStyle(QtCore.Qt.NoBrush)
        item_0.setForeground(0, brush)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setItalic(True)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setItalic(True)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_branches)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_branches)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_branches)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_branches)
        self.treeWidget_branches.header().setVisible(False)
        self.treeWidget_branches.header().setCascadingSectionResizes(False)
        self.treeWidget_branches.header().setDefaultSectionSize(311)
        self.treeWidget_branches.header().setMinimumSectionSize(4)
        self.treeWidget_branches.header().setSortIndicatorShown(False)
        self.treeWidget_branches.header().setStretchLastSection(False)
        self.pushButton_submitFileImfo = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_submitFileImfo.setGeometry(QtCore.QRect(490, 320, 31, 31))
        self.pushButton_submitFileImfo.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/submitB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_submitFileImfo.setIcon(icon1)
        self.pushButton_submitFileImfo.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_submitFileImfo.setDefault(False)
        self.pushButton_submitFileImfo.setFlat(True)
        self.pushButton_submitFileImfo.setObjectName("pushButton_submitFileImfo")
        self.tableWidget_FileList = QtWidgets.QTableWidget(self.tab_branch)
        self.tableWidget_FileList.setGeometry(QtCore.QRect(190, 0, 351, 131))
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
        self.pushButton_reNewBranchDict = QtWidgets.QPushButton(self.tab_branch)
        self.pushButton_reNewBranchDict.setGeometry(QtCore.QRect(10, 500, 261, 41))
        self.pushButton_reNewBranchDict.setObjectName("pushButton_reNewBranchDict")
        self.lineEdit_currentFileName = QtWidgets.QLineEdit(self.tab_branch)
        self.lineEdit_currentFileName.setGeometry(QtCore.QRect(190, 132, 351, 27))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 44, 34))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 44, 34))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.lineEdit_currentFileName.setPalette(palette)
        self.lineEdit_currentFileName.setObjectName("lineEdit_currentFileName")
        self.tabWidget_branch.addTab(self.tab_branch, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_optionPage_projDescription = QtWidgets.QLabel(self.tab_2)
        self.label_optionPage_projDescription.setGeometry(QtCore.QRect(30, 40, 130, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.label_optionPage_projDescription.setFont(font)
        self.label_optionPage_projDescription.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_optionPage_projDescription.setObjectName("label_optionPage_projDescription")
        self.label_optionPage_showFileType = QtWidgets.QLabel(self.tab_2)
        self.label_optionPage_showFileType.setGeometry(QtCore.QRect(30, 340, 130, 16))
        font = QtGui.QFont()
        font.setPointSize(self.setFontSize)
        self.label_optionPage_showFileType.setFont(font)
        self.label_optionPage_showFileType.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_optionPage_showFileType.setObjectName("label_optionPage_showFileType")
        self.label_optionPage_tempB = QtWidgets.QLabel(self.tab_2)
        self.label_optionPage_tempB.setGeometry(QtCore.QRect(30, 390, 130, 16))
        font = QtGui.QFont()
        font.setPointSize(self.setFontSize)
        self.label_optionPage_tempB.setFont(font)
        self.label_optionPage_tempB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_optionPage_tempB.setObjectName("label_optionPage_tempB")
        self.label_optionPage_userPref = QtWidgets.QLabel(self.tab_2)
        self.label_optionPage_userPref.setGeometry(QtCore.QRect(30, 280, 130, 16))
        font = QtGui.QFont()
        font.setPointSize(self.setFontSize)
        self.label_optionPage_userPref.setFont(font)
        self.label_optionPage_userPref.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_optionPage_userPref.setObjectName("label_optionPage_userPref")
        self.label_optionPage_User = QtWidgets.QLabel(self.tab_2)
        self.label_optionPage_User.setGeometry(QtCore.QRect(30, 230, 130, 16))
        font = QtGui.QFont()
        font.setPointSize(self.setFontSize)
        self.label_optionPage_User.setFont(font)
        self.label_optionPage_User.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_optionPage_User.setObjectName("label_optionPage_User")
        self.label_optionPage_workProj = QtWidgets.QLabel(self.tab_2)
        self.label_optionPage_workProj.setGeometry(QtCore.QRect(30, 100, 130, 16))
        font = QtGui.QFont()
        font.setPointSize(self.setFontSize)
        self.label_optionPage_workProj.setFont(font)
        self.label_optionPage_workProj.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_optionPage_workProj.setObjectName("label_optionPage_workProj")
        self.label_optionPage_branchFileInfo = QtWidgets.QLabel(self.tab_2)
        self.label_optionPage_branchFileInfo.setGeometry(QtCore.QRect(30, 160, 130, 16))
        font = QtGui.QFont()
        font.setPointSize(self.setFontSize)
        self.label_optionPage_branchFileInfo.setFont(font)
        self.label_optionPage_branchFileInfo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_optionPage_branchFileInfo.setObjectName("label_optionPage_branchFileInfo")
        self.plainTextEdit_optionPage_projDescription = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_optionPage_projDescription.setGeometry(QtCore.QRect(170, 40, 351, 50))
        font = QtGui.QFont()
        font.setPointSize(self.setFontSize)
        self.plainTextEdit_optionPage_projDescription.setFont(font)
        self.plainTextEdit_optionPage_projDescription.setReadOnly(True)
        self.plainTextEdit_optionPage_projDescription.setPlainText("")
        self.plainTextEdit_optionPage_projDescription.setObjectName("plainTextEdit_optionPage_projDescription")
        self.plainTextEdit_optionPage_workProj = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_optionPage_workProj.setGeometry(QtCore.QRect(170, 100, 351, 50))
        font = QtGui.QFont()
        font.setPointSize(self.setFontSize)
        self.plainTextEdit_optionPage_workProj.setFont(font)
        self.plainTextEdit_optionPage_workProj.setReadOnly(True)
        self.plainTextEdit_optionPage_workProj.setObjectName("plainTextEdit_optionPage_workProj")
        self.plainTextEdit_optionPage_branchInfoPos = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_optionPage_branchInfoPos.setGeometry(QtCore.QRect(170, 160, 351, 50))
        font = QtGui.QFont()
        font.setPointSize(self.setFontSize)
        self.plainTextEdit_optionPage_branchInfoPos.setFont(font)
        self.plainTextEdit_optionPage_branchInfoPos.setReadOnly(True)
        self.plainTextEdit_optionPage_branchInfoPos.setObjectName("plainTextEdit_optionPage_branchInfoPos")
        self.plainTextEdit_optionPage_currentUser = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_optionPage_currentUser.setGeometry(QtCore.QRect(170, 230, 351, 40))
        font = QtGui.QFont()
        font.setPointSize(self.setFontSize)
        self.plainTextEdit_optionPage_currentUser.setFont(font)
        self.plainTextEdit_optionPage_currentUser.setReadOnly(True)
        self.plainTextEdit_optionPage_currentUser.setObjectName("plainTextEdit_optionPage_currentUser")
        self.plainTextEdit_optionPage_userPref = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_optionPage_userPref.setGeometry(QtCore.QRect(170, 280, 351, 50))
        font = QtGui.QFont()
        font.setPointSize(self.setFontSize)
        self.plainTextEdit_optionPage_userPref.setFont(font)
        self.plainTextEdit_optionPage_userPref.setReadOnly(True)
        self.plainTextEdit_optionPage_userPref.setObjectName("plainTextEdit_optionPage_userPref")
        self.plainTextEdit_optionPage_showFileType = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_optionPage_showFileType.setGeometry(QtCore.QRect(170, 340, 351, 40))
        font = QtGui.QFont()
        font.setPointSize(self.setFontSize)
        self.plainTextEdit_optionPage_showFileType.setFont(font)
        self.plainTextEdit_optionPage_showFileType.setReadOnly(False)
        self.plainTextEdit_optionPage_showFileType.setObjectName("plainTextEdit_optionPage_showFileType")
        self.plainTextEdit_optionPage_tempB = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_optionPage_tempB.setGeometry(QtCore.QRect(170, 390, 351, 40))
        font = QtGui.QFont()
        font.setPointSize(self.setFontSize)
        self.plainTextEdit_optionPage_tempB.setFont(font)
        self.plainTextEdit_optionPage_tempB.setReadOnly(True)
        self.plainTextEdit_optionPage_tempB.setObjectName("plainTextEdit_optionPage_tempB")
        self.tabWidget_branch.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget_branch.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.pushButton_mergeToMaster.setText(QtWidgets.QApplication.translate("MainWindow", "merge", None, -1))
        self.pushButton_createNewBranch.setText(QtWidgets.QApplication.translate("MainWindow", "new Branch", None, -1))
        self.textBrowser_BranchFileInfo.setHtml(QtWidgets.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'PMingLiU\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">fileIno:</p></body></html>", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Branch Name", None, -1))
        self.treeWidget_branches.headerItem().setText(0, QtWidgets.QApplication.translate("MainWindow", "branch Info", None, -1))
        __sortingEnabled = self.treeWidget_branches.isSortingEnabled()
        self.treeWidget_branches.setSortingEnabled(False)
        self.treeWidget_branches.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "master", None, -1))
        self.treeWidget_branches.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "branch_01", None, -1))
        self.treeWidget_branches.topLevelItem(1).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "branch_01_a", None, -1))
        self.treeWidget_branches.topLevelItem(1).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "branch_01_b", None, -1))
        self.treeWidget_branches.topLevelItem(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "branch_02", None, -1))
        self.treeWidget_branches.topLevelItem(3).setText(0, QtWidgets.QApplication.translate("MainWindow", "test", None, -1))
        self.treeWidget_branches.topLevelItem(3).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "test_a01", None, -1))
        self.treeWidget_branches.topLevelItem(3).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "test_a02", None, -1))
        self.treeWidget_branches.topLevelItem(3).child(1).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "test_a02_1", None, -1))
        self.treeWidget_branches.topLevelItem(4).setText(0, QtWidgets.QApplication.translate("MainWindow", "temp", None, -1))
        self.treeWidget_branches.topLevelItem(5).setText(0, QtWidgets.QApplication.translate("MainWindow", "extra", None, -1))
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
        self.pushButton_reNewBranchDict.setText(QtWidgets.QApplication.translate("MainWindow", "ReNew Branch Dict", None, -1))
        self.lineEdit_currentFileName.setText(QtWidgets.QApplication.translate("MainWindow", "SelectFile:", None, -1))
        self.tabWidget_branch.setTabText(self.tabWidget_branch.indexOf(self.tab_branch), QtWidgets.QApplication.translate("MainWindow", "branch Edit", None, -1))
        self.label_optionPage_projDescription.setText(QtWidgets.QApplication.translate("MainWindow", "project Description:", None, -1))
        self.label_optionPage_showFileType.setText(QtWidgets.QApplication.translate("MainWindow", "show File Type:", None, -1))
        self.label_optionPage_tempB.setText(QtWidgets.QApplication.translate("MainWindow", "temp_B:", None, -1))
        self.label_optionPage_userPref.setText(QtWidgets.QApplication.translate("MainWindow", "User Pref:", None, -1))
        self.label_optionPage_User.setText(QtWidgets.QApplication.translate("MainWindow", "current User:", None, -1))
        self.label_optionPage_workProj.setText(QtWidgets.QApplication.translate("MainWindow", "working Projsct :", None, -1))
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
        
        
        #clear treeWidger_branches, all Clear
        self.treeWidget_branches.clear()
        self.tableWidget_FileList.clear()
        self.defineFont()
        self.printOutProjectInfo()
        
        self.branch_index = 0
        
        self.assetName  = "anna"
        self.branchDict={"0":{"master":{}}} 
        self.pushButton_reNewBranchDict.clicked.connect(self.getExistBranchDict)
        
        self.pushButton_createNewBranch.clicked.connect(self.createNewBranchCombo)


        self.pushButton_mergeToMaster.clicked.connect(self.getSavingFile)
        
        self.treeWidget_branches.itemClicked.connect(self.createFileTable)
        
        self.tableWidget_FileList.itemClicked.connect(self.printOutFileInfo)
        
        self.pushButton_editFileInfo.clicked.connect(self.printOutProjectInfo)

        self.getCurrentLevelList = []
        self.initialItemBuild()

        
  #-----------------------------------upper are load startUp-------------------------------------------------------------------------------------------------------      
        
    def clear(self):
        
        self.tableWidget_FileList.clear()
        
        
    def printOutProjectInfo(self):
        # input project infomation, project root, name,asset name, shot name, isAsset Value
        print "get input info"
        self.root = "C:/mayaProjs"
        #self.root ="//mcd-server/art_3d_project"
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
      #  with open(self.branchFileStore, 'r') as f:
     #       json_data = json.load(f)
    

        
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
        
        self.branchDict={"0":{"master":{}}}    #default Master Item
        
        self.buildExistFileInfoTree()
        self.buildTreeFromExistFileData()
        
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
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
        
        self.getFilesInfoFormJson()
        self.tableWidget_FileList.clear()
        

  
         # self.fileInfoDict = {'01':["projectName_assetClass_assetName_process_v001_alpha.mb","alpha","2017/03/28    10:28","info xxxxxxxxxxxxxxxxxxxxxx"],
                         #    '02':["projectName_assetClass_assetName_process_v002_alpha.mb","alpha","2017/03/28    10:29"],
                          #   '03':["projectName_assetClass_assetName_process_v003_alpha.mb","alpha","2017/03/28    10:30"],
                          #   '04':["projectName_assetClass_assetName_process_v004_alpha.mb","alpha","2017/03/28    10:31"],
                             
                             
        tableIndex = sorted(self.fileInfoDict.keys())  #string
        
        verIndex = sorted(self.fileInfoDict.keys(), reverse = True )        


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
        print" run createFileTable function End..................."





    def getSavingFile(self):
        
        #self.project = "3d_pipeline_test"
        #self.assetClass ="character"
        #self.assetNow = "shot_02"
        #self.processNow ="lighting"
        #self.currentBranchName  get Selected Branch Name
        
        #--------------------get project initial--------------------
        self.projInitial = ""
       
        for par in self.project.split('_'):
            self.projInitial = self.projInitial + par[0]
        print self.projInitial
        
        
        #print self.currentBranchName
            
       # print projInitial
        #self.getFilesInfoFormJson()
        #print self.filesStoreBranchFolder
      #  print self.currentBranchFileDict
        #savingFileName =
       # self.assetProcess = ['concept','model','texture','rigging']
        #self.shotProcess = ['concept','layout','animation','lighting','effects','simulation','comp']
        #processTypeShortNameList = ["con","mod","tex","rig","lay","ani","lig","eff","sim","com","master","publish"]
        

        #-----------------get last version in branch folder
       # for file in os.listdir(self.filesStoreBranchFolder):
           # print file.split('%s'%self.currentBranchName)#[1].split('_')
               
               #     print file, par
               
        #--------------- get files in branch folder,and file type in fileTypeList  
        tempVerList =[]     
        for key in self.fileInfoDict.keys():
            try:
                verNum = self.fileInfoDict[key][0].split('%s'%self.currentBranchName)[1].split('_')[1]
                tempVerList.append(verNum)
            except:
                pass
        
        
        tempVerListSorted = sorted(tempVerList)

  
         # self.fileInfoDict =
        
                    

    def getFilesInfoFormJson(self):  # export files to list_widget ,build from branchInfoFile as json ,ex. globals/shot/shot_02/shot02/shot_02_lighting.json
        # check the select tree item depth, 
        # export file dict, self.branchFilesInListDict
        #

        
        fileTypeFillet = self.plainTextEdit_optionPage_showFileType.toPlainText().split(',')
        print fileTypeFillet
        print "run getFilesInfoFormJson starting......................."
        print "finding files in the branch"
        itemSelect =  self.treeWidget_branches.currentItem().text(0)
        
        with open(self.branchFileStore, 'r') as f:
            self.branchPreDict = json.load(f)
            

        topLevelItemCount = len(self.branchPreDict.keys())    

        self.getExistBranchDict()

        self.getSelectItemLevel()
        
        tempTimeFileCompareDict = {}  # temp dictionary , that store file modify datetime and file name
        

        if len(self.fullItemIndex) == 1:
            

            
            self.branchFilesInListDict = self.branchPreDict[str(self.fullItemIndex[0])][itemSelect]['file']
            
            fileCount = len(self.branchPreDict[str(self.fullItemIndex[0])][itemSelect]['file'].keys())

            self.filesStoreBranchFolder = self.workProject + '/' +'scenes' + '/' + itemSelect
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
            
            secLevelItem = self.branchPreDict[str(self.fullItemIndex[0])][self.branchPreDict[str(self.fullItemIndex[0])].keys()[0]]['folder'][itemSelect]

          #  print "secLevelItem['file'].keys()",secLevelItem['folder']
            self.branchFilesInListDict = secLevelItem['file']
            secLevelFolder = self.branchPreDict[str(self.fullItemIndex[0])].keys()[0]

            self.filesStoreBranchFolder = self.workProject + '/' +'scenes' + '/' + secLevelFolder + '/' + itemSelect


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
            topLayerItem = self.branchPreDict[str(self.fullItemIndex[0])].keys()[0]

            secLevelItem = self.branchPreDict[str(self.fullItemIndex[0])][self.branchPreDict[str(self.fullItemIndex[0])].keys()[0]]['folder']#[self.fullItemIndex[0]]]#]['folder'][itemSelect]['folder'].keys()[0]
            parSecLevelItem = secLevelItem.keys()[self.fullItemIndex[1]]
            thirdLevelItem = secLevelItem[parSecLevelItem]
            
            fourLevelItem = thirdLevelItem['folder'][itemSelect]['file']
            #print fourLevelItem
            self.branchFilesInListDict = fourLevelItem
            
            self.filesStoreBranchFolder = self.workProject + '/' +'scenes' + '/'+ topLayerItem + '/' + parSecLevelItem +'/'+itemSelect
            
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



        self.currentBranchName = itemSelect

        self.currentBranchFileDict = tempTimeFileCompareDict
        print "run getFilesInfoFormJson End......................."
       # print self.fileInfoDict
        print "self.branchFilesInListDict" ,self.branchFilesInListDict
      #  print tempTimeFileCompareDict
      
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

        
        #update assetBranchFileInfo.json
    ##-------------------------creader folder---------------------------------------------------------  

        createTopLayerFoder = self.workProject + '/' +'scenes'+ '/'+ self.newBranch 
        print os.path.isdir(createTopLayerFoder)
        if os.path.isdir(createTopLayerFoder) == True:
            print "already has "+"%s"%createTopLayerFoder + " folder"
            
        else:
            os.mkdir(createTopLayerFoder)
            
        
       # print createTopLayerFoder
        
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


 
 