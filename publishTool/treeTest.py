# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha/Documents/GitHub/mayaTool/publishTool/treeTest.ui'
#
# Created: Tue Jun 13 21:28:12 2017
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
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(110, 30, 241, 451))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item_2.setForeground(0, brush)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.header().setVisible(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.treeWidget.headerItem().setText(0, QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "A1", None, -1))
        self.treeWidget.topLevelItem(0).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "A1_1", None, -1))
        self.treeWidget.topLevelItem(0).child(0).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "A1_1_1", None, -1))
        self.treeWidget.topLevelItem(0).child(0).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "A1_1_2", None, -1))
        self.treeWidget.topLevelItem(0).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "A1_2", None, -1))
        self.treeWidget.topLevelItem(0).child(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "A1_3", None, -1))
        self.treeWidget.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "B1", None, -1))
        self.treeWidget.topLevelItem(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "C1", None, -1))
        self.treeWidget.setSortingEnabled(__sortingEnabled)




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


 