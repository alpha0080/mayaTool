# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha.DESKTOP-1S1STEK/Documents/GitHub/ribGen/publish/publish_01.ui'
#
# Created: Wed Mar 01 16:03:09 2017
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import maya.cmds as cmds
import pymel.core as pm
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 1144)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 40, 221, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.radioButton_selectAsset = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_selectAsset.setObjectName("radioButton_selectAsset")
        self.horizontalLayout.addWidget(self.radioButton_selectAsset)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.radioButton_selectShot = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_selectShot.setObjectName("radioButton_selectShot")
        self.horizontalLayout.addWidget(self.radioButton_selectShot)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_selectProject = QtGui.QPushButton(self.centralwidget)
        self.pushButton_selectProject.setGeometry(QtCore.QRect(30, 10, 711, 23))
        self.pushButton_selectProject.setObjectName("pushButton_selectProject")
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 420, 331, 331))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 420, 331, 331))
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_selectAsset.setText(QtGui.QApplication.translate("MainWindow", "asset", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_selectShot.setText(QtGui.QApplication.translate("MainWindow", "shot", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_selectProject.setText(QtGui.QApplication.translate("MainWindow", "select Project", None, QtGui.QApplication.UnicodeUTF8))
        
        
        self.pushButton_selectProject.clicked.connect(self.modpushButton_selectProject)
                

        self.radioButton_selectAsset.clicked.connect(self.selectAssetOrShot)
        self.radioButton_selectShot.clicked.connect(self.selectAssetOrShot)




class mod_MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent= QtGui.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)     
        self.setupUi(self)
        

        
        
#    def projectInfo(self):
#        self.plainTextEditA.setPlainText("ssss")

    def selectAssetOrShot(self):
        #self.lineEditA1.setText("%s"%currentStartFrame)
        if self.radioButton_selectAsset.isChecked() == True:
            print "select Asset"
            
        else:
            print "select Shot"
            
            
    def modpushButton_selectProject(self):
        globalProjectName = cmds.fileDialog2(fm=2)[0]
        underList =  os.listdir(globalProjectName)
        print globalProjectName
        dirTree = {}
        for i in underList:    
            if os.path.isdir(globalProjectName + "/"+i) == True:
                print i
                treeDir.update({i:""})
            else:
                pass
               # print i
               
        self.pushButton_selectProject.setText(globalProjectName)
                
        self.lineEdit.

 
def main():
#def publishMain():
    global ui
    app = QtGui.QApplication.instance()
    if app == None: app = QApplication(sys.argv)
    try:
        ui.close()
        ui.deleteLater()
    except: pass
    ui = mod_MainWindow()
    ui.show()
 
if __name__ == '__main__':
    main() 