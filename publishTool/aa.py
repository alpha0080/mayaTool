# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha/Documents/GitHub/mayaTool/publishTool/aa.ui'
#
# Created: Sat Jun 24 22:34:17 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets



        
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(465, 407)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
       # self.pushButton_testB = QtWidgets.QPushButton(self.centralwidget)
       # self.pushButton_testB.setGeometry(QtCore.QRect(270, 300, 91, 41))
       # self.pushButton_testB.setObjectName("pushButton_testB")
        self.pushButton_testA = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_testA.setGeometry(QtCore.QRect(140, 300, 91, 41))
        self.pushButton_testA.setObjectName("pushButton_testA")
        
        #self.pushButton_testC = QtWidgets.QPushButton(self.centralwidget)
        #self.pushButton_testC.setGeometry(QtCore.QRect(0, 300, 91, 41))
        #self.pushButton_testC.setObjectName("pushButton_testA")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
       # self.pushButton_testB.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.pushButton_testA.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))




class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #self.QTITEM.ACTION.connect(self.MODDEF)
        self.setupUi(self)
    #def self.MODDEF(self):
     #   MainWindow.setObjectName("MainWindow")
      #  MainWindow.resize(465, 407)
       # self.centralwidget = QtWidgets.QWidget(MainWindow)
       # self.centralwidget.setObjectName("centralwidget")


        self.pushButton_testA.clicked.connect(self.createItemInBox)




    def createItemInBox(self):
        print 'asdsads'
        #print self.centralwidget
        
        self.pushButton_testC = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_testC.setGeometry(QtCore.QRect(0, 300, 91, 41))
        self.pushButton_testC.setObjectName("pushButton_testA")
        

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


 