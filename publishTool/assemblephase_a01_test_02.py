# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha/Documents/GitHub/mayaTool/publishTool/assemblephase_a01.ui'
#
# Created: Sat Jun 24 20:15:26 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(532, 576)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_testA = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_testA.setGeometry(QtCore.QRect(140, 490, 91, 41))
        self.pushButton_testA.setObjectName("pushButton_testA")
        self.pushButton_testB = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_testB.setGeometry(QtCore.QRect(270, 490, 91, 41))
        self.pushButton_testB.setObjectName("pushButton_testB")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(130, 60, 271, 321))
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setIconSize(QtCore.QSize(100, 100))
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(9)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(9)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/-__check_done_accept_ok-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(50)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget.verticalHeader().setMinimumSectionSize(50)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.pushButton_testA.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.pushButton_testB.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.tableWidget.setSortingEnabled(False)
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.item(0, 1).setText(QtWidgets.QApplication.translate("MainWindow", "12121212121221212122", None, -1))
        self.tableWidget.setSortingEnabled(__sortingEnabled)






class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #self.QTITEM.ACTION.connect(self.MODDEF)
        self.setupUi(self)
    #def self.MODDEF(self):
        self.pushButton_testA.clicked.connect(self.test)
        self.pushButton_testB.clicked.connect(self.createItemInBox)
        
        

        
        
        
    def test(self):
        print 'aaaaa'
        self.getCurrentItemsInScrollBox()
        for i in self.allItemsInBox:
            i.close()
            
        
    def getCurrentItemsInScrollBox(self):
        #allItemsInBox , 在scrollAreaWidgetContents中所有的物件
        self.allItemsInBox = self.scrollAreaWidgetContents.children()  # get all items in scroll area box
        self.currentItemInBoxCount = len(self.allItemsInBox) #get count in scroll

       # for i in allItemsInBox:
       #     print i.text()
        
        #print self.currentItemInBoxCount
        
        #self.pushButton_4.close()
    
    
    def cauItemsToBuild(self):
        itemDict = {'a1':{},
                    'a2':{},
                    'a3':{},
                    'b1':{},
                    'b2':{},
                    'c1':{},
                    'd1':{},
                    'd2':{},
                    }
        


    def createItemInBox(self):
        print 'asdsads'
       # print self.preBuildItemDict
        self.setTableItemSize(20)
        self.setItemCount(10,3)
       
       
       
        
    def setTableItemSize(self,size):
       # self.tableWidget.horizontalHeader().setDefaultSectionSize(size)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(size)
       # self.tableWidget.horizontalHeader()
        self.tableWidget.horizontalHeader().setMinimumSectionSize(size)
        self.tableWidget.verticalHeader().setDefaultSectionSize(size)
        self.tableWidget.verticalHeader().setMinimumSectionSize(size)
        
        
    def setItemCount(self,columnCount,rowCount):
        self.tableWidget.setColumnCount(columnCount)
        self.tableWidget.setRowCount(rowCount)
        #self.pushButton_4.setIconSize(QtCore.QSize(50, 50))
 
        
       # self.pushButton_testC = QtWidgets.QPushButton(self.centralwidget)
       # self.pushButton_testC.setGeometry(QtCore.QRect(0, 100, 100, 100))
       # self.pushButton_testC.setObjectName("pushButton_testC")
       # self.pushButton_testC.setText(QtWidgets.QApplication.translate("MainWindow", "PushButtonAA", None, -1))

        
    def sadsad(self):
        self.pushButton_4A = QtWidgets.QPushButton(self.centralwidget)

        #self.pushButton_4A = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4A.setGeometry(QtCore.QRect(0, 0, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4A.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4A.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_4A.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_4A.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_4A.setAutoFillBackground(False)
        self.pushButton_4A.setText("A")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:/Program Files/Autodesk/Maya2017/icons/16-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4A.setIcon(icon)
        self.pushButton_4A.setIconSize(QtCore.QSize(50, 50))
        #self.pushButton_4.setAutoRepeat(False)
        #self.pushButton_4.setAutoExclusive(False)
        #self.pushButton_4.setFlat(False)
        self.pushButton_4A.setObjectName("pushButton_4A")
        
    def createItemInBoxB(self):
        
        self.pushButton_9 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_9.setGeometry(QtCore.QRect(50, 0, 50, 50))
       # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
       # sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
       # self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_9.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_9.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_9.setObjectName("pushButton_6")
        self.pushButton_9.setText(QtWidgets.QApplication.translate("MainWindow", "B", None, -1))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)


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


 