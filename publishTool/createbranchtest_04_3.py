# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha.DESKTOP-1S1STEK/Documents/GitHub/ribGen/publishTool/createbranchtest_04_1.ui'
#
# Created: Wed Mar 29 10:18:29 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(558, 577)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_createNewBranch = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_createNewBranch.setGeometry(QtCore.QRect(310, 450, 231, 41))
        self.pushButton_createNewBranch.setObjectName("pushButton_createNewBranch")
        self.lineEdit_branchName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_branchName.setGeometry(QtCore.QRect(10, 450, 261, 41))
        self.lineEdit_branchName.setText("")
        self.lineEdit_branchName.setObjectName("lineEdit_branchName")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 420, 161, 21))
        self.label.setObjectName("label")
        self.treeWidget_branches = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget_branches.setGeometry(QtCore.QRect(10, 10, 171, 311))
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
        self.pushButton_reNewBranchDict = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reNewBranchDict.setGeometry(QtCore.QRect(10, 510, 261, 41))
        self.pushButton_reNewBranchDict.setObjectName("pushButton_reNewBranchDict")
        self.pushButton_mergeToMaster = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mergeToMaster.setGeometry(QtCore.QRect(310, 510, 231, 41))
        self.pushButton_mergeToMaster.setObjectName("pushButton_mergeToMaster")
        self.tableWidget_FileList = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_FileList.setGeometry(QtCore.QRect(190, 10, 351, 151))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableWidget_FileList.setFont(font)
        self.tableWidget_FileList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget_FileList.setAutoScrollMargin(16)
        self.tableWidget_FileList.setAlternatingRowColors(True)
        self.tableWidget_FileList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
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
        self.textBrowser_BranchFileInfo = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_BranchFileInfo.setGeometry(QtCore.QRect(190, 170, 351, 151))
        self.textBrowser_BranchFileInfo.setMidLineWidth(1)
        self.textBrowser_BranchFileInfo.setTabChangesFocus(False)
        self.textBrowser_BranchFileInfo.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textBrowser_BranchFileInfo.setOpenExternalLinks(True)
        self.textBrowser_BranchFileInfo.setObjectName("textBrowser_BranchFileInfo")
        self.pushButton_editFileInfo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_editFileInfo.setGeometry(QtCore.QRect(450, 330, 31, 31))
        self.pushButton_editFileInfo.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Program Files/Autodesk/Maya2017/icons/editY.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_editFileInfo.setIcon(icon)
        self.pushButton_editFileInfo.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_editFileInfo.setAutoDefault(False)
        self.pushButton_editFileInfo.setDefault(False)
        self.pushButton_editFileInfo.setFlat(True)
        self.pushButton_editFileInfo.setObjectName("pushButton_editFileInfo")
        self.pushButton_submitFileImfo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_submitFileImfo.setGeometry(QtCore.QRect(490, 330, 31, 31))
        self.pushButton_submitFileImfo.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Program Files/Autodesk/Maya2017/icons/submitB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_submitFileImfo.setIcon(icon1)
        self.pushButton_submitFileImfo.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_submitFileImfo.setDefault(False)
        self.pushButton_submitFileImfo.setFlat(True)
        self.pushButton_submitFileImfo.setObjectName("pushButton_submitFileImfo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.pushButton_createNewBranch.setText(QtWidgets.QApplication.translate("MainWindow", "new Branch", None, -1))
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
        self.pushButton_reNewBranchDict.setText(QtWidgets.QApplication.translate("MainWindow", "ReNew Branch Dict", None, -1))
        self.pushButton_mergeToMaster.setText(QtWidgets.QApplication.translate("MainWindow", "merge", None, -1))
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




class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #self.QTITEM.ACTION.connect(self.MODDEF)
        self.setupUi(self)
    #def self.MODDEF(self):



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


 