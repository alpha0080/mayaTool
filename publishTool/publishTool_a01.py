# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha/Documents/GitHub/ribGen/publishTool/publishTool_A01.ui'
#
# Created: Sat Mar 04 16:04:19 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidgetDir = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidgetDir.setGeometry(QtCore.QRect(30, 50, 311, 351))
        self.treeWidgetDir.setObjectName("treeWidgetDir")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidgetDir)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidgetDir)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidgetDir)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidgetDir)
        self.pushButton_getProject = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_getProject.setGeometry(QtCore.QRect(30, 10, 80, 31))
        self.pushButton_getProject.setObjectName("pushButton_getProject")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.treeWidgetDir.headerItem().setText(0, QtWidgets.QApplication.translate("MainWindow", "A", None, -1))
        __sortingEnabled = self.treeWidgetDir.isSortingEnabled()
        self.treeWidgetDir.setSortingEnabled(False)
        self.treeWidgetDir.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "a1", None, -1))
        self.treeWidgetDir.topLevelItem(0).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "a_1_1", None, -1))
        self.treeWidgetDir.topLevelItem(0).child(0).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "a_1_1_1", None, -1))
        self.treeWidgetDir.topLevelItem(0).child(0).child(0).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "a_1_1_1_1", None, -1))
        self.treeWidgetDir.topLevelItem(0).child(0).child(0).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "a_1_1_1_2", None, -1))
        self.treeWidgetDir.topLevelItem(0).child(0).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "a_1_1_2", None, -1))
        self.treeWidgetDir.topLevelItem(0).child(0).child(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "a_1_1_3", None, -1))
        self.treeWidgetDir.topLevelItem(0).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "a_1_2", None, -1))
        self.treeWidgetDir.topLevelItem(0).child(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "a_1_3", None, -1))
        self.treeWidgetDir.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "a2", None, -1))
        self.treeWidgetDir.topLevelItem(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "a3", None, -1))
        self.treeWidgetDir.topLevelItem(3).setText(0, QtWidgets.QApplication.translate("MainWindow", "a4", None, -1))
        self.treeWidgetDir.setSortingEnabled(__sortingEnabled)
        self.pushButton_getProject.setText(QtWidgets.QApplication.translate("MainWindow", "Get Project", None, -1))




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


 