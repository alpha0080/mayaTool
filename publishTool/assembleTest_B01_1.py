# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha.DESKTOP-1S1STEK/Documents/GitHub/mayaTool/publishTool/assembleTest_B01.ui'
#
# Created: Thu Jul 06 16:28:26 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1041, 895)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(15, 5, 291, 546))
        self.treeWidget.setDragEnabled(True)
        self.treeWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.header().setVisible(False)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setDefaultSectionSize(150)
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setMinimumSectionSize(25)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(350, 15, 321, 531))
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setIconSize(QtCore.QSize(60, 60))
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideNone)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(60)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(60)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(25)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(350, 560, 321, 281))
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.treeWidget.headerItem().setText(0, QtWidgets.QApplication.translate("MainWindow", "assetName", None, -1))
        self.treeWidget.headerItem().setText(1, QtWidgets.QApplication.translate("MainWindow", "assetProcess", None, -1))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "Character", None, -1))
        self.treeWidget.topLevelItem(0).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "anna", None, -1))
        self.treeWidget.topLevelItem(0).child(0).setText(1, QtWidgets.QApplication.translate("MainWindow", "model", None, -1))
        self.treeWidget.topLevelItem(0).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "tiger", None, -1))
        self.treeWidget.topLevelItem(0).child(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "joey", None, -1))
        self.treeWidget.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "Vehicle", None, -1))
        self.treeWidget.topLevelItem(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "Set", None, -1))
        self.treeWidget.topLevelItem(3).setText(0, QtWidgets.QApplication.translate("MainWindow", "Prop", None, -1))
        self.treeWidget.topLevelItem(4).setText(0, QtWidgets.QApplication.translate("MainWindow", "Other", None, -1))
        self.treeWidget.topLevelItem(5).setText(0, QtWidgets.QApplication.translate("MainWindow", "Effect", None, -1))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.tableWidget.verticalHeaderItem(0).setText(QtWidgets.QApplication.translate("MainWindow", "?°å???", None, -1))
        self.tableWidget.verticalHeaderItem(1).setText(QtWidgets.QApplication.translate("MainWindow", "1a", None, -1))
        self.tableWidget.verticalHeaderItem(2).setText(QtWidgets.QApplication.translate("MainWindow", "2a", None, -1))
        self.tableWidget.verticalHeaderItem(3).setText(QtWidgets.QApplication.translate("MainWindow", "3a", None, -1))
        self.tableWidget.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("MainWindow", "ItemName", None, -1))
        self.tableWidget.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("MainWindow", "ItemIcon", None, -1))
        self.tableWidget.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("MainWindow", "MayaPath", None, -1))
        self.tableWidget.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("MainWindow", "RibArchive", None, -1))
        self.tableWidget.horizontalHeaderItem(4).setText(QtWidgets.QApplication.translate("MainWindow", "GpuCache", None, -1))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.item(0, 0).setText(QtWidgets.QApplication.translate("MainWindow", "ItemName", None, -1))
        self.tableWidget.item(0, 1).setText(QtWidgets.QApplication.translate("MainWindow", "ItemIcon", None, -1))
        self.tableWidget.item(0, 2).setText(QtWidgets.QApplication.translate("MainWindow", "FileName", None, -1))
        self.tableWidget.item(1, 0).setText(QtWidgets.QApplication.translate("MainWindow", "ItemName2", None, -1))
        self.tableWidget.setSortingEnabled(__sortingEnabled)



       # self.tableWidget.item(0, 0).setIconSize(QtCore.QSize(60, 60))
       # item.setSizeHint(QtCore.QSize(120,60))
       
        #self.tableWidget.setSizeHint(QtCore.QSize(120,60))
        #self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy(20))

class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #self.QTITEM.ACTION.connect(self.MODDEF)
        self.setupUi(self)
    #def self.MODDEF(self):
        self.tableWidget.setRowCount(9)
       # icon.
       # icon.addPixmap()
        #self.treeWidget_2.setIconSize(QtCore.QSize(60,60))
#tableWidget.setCellWidget(0, 1, ImgWidget1(self))
       # self.tableWidget.setCellWidget(0, 1, icon)
       # self.tableWidget.item.setIcon(0,1,icon)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget.verticalHeader().setDefaultSectionSize(80)
        
        iconFile = QtGui.QIcon("C:/Program Files/Autodesk/Maya2017/icons/publishToolIcon/animation.png")
        
        for row in range(0,3):
            doubleRow = row*2
            for column in range(0,3):
               # dc = column *2
                self.createItem(doubleRow,column,iconFile)
                
        
        
        
    def createItem(self,row,column,iconFile):
       # icon = QtGui.QIcon("C:/Program Files/Autodesk/Maya2017/icons/publishToolIcon/animation.png")

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(row, column, item)
        self.tableWidget.item(row, column).setIcon(iconFile)
        
       # self.tableWidget.item(1, 2).setIconText('aaa')
       # item.
        # add text Item
        item = QtWidgets.QTableWidgetItem()
        textRow = row+1
        self.tableWidget.setRowHeight(textRow , 20) #set text row height
        self.tableWidget.setItem(textRow, column, item)
        self.tableWidget.item(textRow, column).setText(QtWidgets.QApplication.translate("MainWindow", "ItemIcon", None,-1))
        #item.setTextAlignment(-20)
        
      #  self.tableWidget.setRowHeight(1 , 20)  
        



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


 