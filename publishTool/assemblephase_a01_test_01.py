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
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_testA = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_testA.setGeometry(QtCore.QRect(140, 490, 91, 41))
        self.pushButton_testA.setObjectName("pushButton_testA")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(140, 40, 120, 80))
        self.widget.setObjectName("widget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(220, 40, 201, 361))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 199, 359))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 0, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_4.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setText("A")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:/Program Files/Autodesk/Maya2017/icons/16-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_4.setAutoRepeat(False)
        self.pushButton_4.setAutoExclusive(False)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton_testB = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_testB.setGeometry(QtCore.QRect(270, 490, 91, 41))
        self.pushButton_testB.setObjectName("pushButton_testB")
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
        
        self.pushButton_testC = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_testC.setGeometry(QtCore.QRect(0, 100, 100, 100))
        self.pushButton_testC.setObjectName("pushButton_testC")
        self.pushButton_testC.setText(QtWidgets.QApplication.translate("MainWindow", "PushButtonAA", None, -1))

        
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


 