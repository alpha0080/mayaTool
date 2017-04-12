# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha/Documents/GitHub/test/QTtest/fileDir_test_02/dirUI_02.ui'
#
# Created: Thu Mar 02 21:57:02 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import os
import maya.cmds as cmds
import pymel.core as pm
import unicodedata

import sys


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
        #self.treeWidgetDir.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "a1", None, -1))
        self.treeWidgetDir.topLevelItem(0).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "a_1_1", None, -1))
        self.treeWidgetDir.topLevelItem(0).child(0).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "a_1_1_1", None, -1))
        self.treeWidgetDir.topLevelItem(0).child(0).child(0).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "a_1_1_1_1", None, -1))
        self.treeWidgetDir.topLevelItem(0).child(0).child(0).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "a_1_1_1_2", None, -1))
        self.treeWidgetDir.topLevelItem(0).child(0).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "a_1_1_2", None, -1))
        self.treeWidgetDir.topLevelItem(0).child(0).child(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "a_1_1_3", None, -1))
        self.treeWidgetDir.topLevelItem(0).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "a_1_2", None, -1))
        self.treeWidgetDir.topLevelItem(0).child(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "a_1_3", None, -1))
        #self.treeWidgetDir.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "a2", None, -1))
        #self.treeWidgetDir.topLevelItem(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "a3", None, -1))
        #self.treeWidgetDir.topLevelItem(3).setText(0, QtWidgets.QApplication.translate("MainWindow", "a4", None, -1))
        self.treeWidgetDir.setSortingEnabled(__sortingEnabled)
        self.pushButton_getProject.setText(QtWidgets.QApplication.translate("MainWindow", "Get Project", None, -1))



        self.pushButton_getProject.clicked.connect(self.modpushButton_test)




class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #self.QTITEM.ACTION.connect(self.MODDEF)
        self.setupUi(self)
    #def self.MODDEF(self):
            
            
    def modpushButton_test(self):
        print "aaaaaaaaaaaaaa"
       # self.num = 3
       ## self.printNum(self.num)
        self.getProjInfo()
        #self.getFileInfor()
        #self.num = self.ObjsCount

        self.dirGive = 'scenes'
        self.treeList(self.dirGive)  
        self.itemCount = self.topLevelItemCount
        self.itemList = self.topLevelItem
        #print self.itemCount, self.itemList
        
        self.TreeTopLeveItemCreate(self.itemCount,self.itemList)  #create topLevelItem form self.TreeTopLeveItemCreate module, self.itemCount 'int',self.itemList = 'list'

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
            topLevelItem.setText(0, QtWidgets.QApplication.translate("MainWindow",tempName))  #topLevelItem named "tempName"
            topLevelItem.setText(0,self.itemList[i])  #change tempName to folder Name , in isDirList
                    
        
        
        
    def temp(self):
        print "create topLevel Items"
        for i in range(0,self.itemCount):
            print i
            print self.isDirList[i]
            topLevelItemName = self.isDirList[i]
            print topLevelItemName
            #name = topLevelItemName
            tempName = "tempName"
           # self.treeWidget.topLevelItem(i).setText(0, QtWidgets.QApplication.translate("MainWindow", name, None, -1))
            topLevelItem = self.treeWidget.topLevelItem(i)
            topLevelItem.setText(0, QtWidgets.QApplication.translate("MainWindow",tempName))  #topLevelItem named "tempName"
            topLevelItem.setText(0,topLevelItemName)  #change tempName to folder Name , in isDirList
                    
        
        
        
    def callTest(self,caller):
        print self.caller
        
    def getProjInfo(self):
        
        
        self.path = cmds.fileDialog2(fm=2)[0]
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
        self.treeInfoDict ={}
        pathTextList = self.path.split('/')
        levelCount = len(pathTextList)   # get the depth  of root, search in self.treeInfoDict

        for root, dirs, files in os.walk(self.path):

            rootRemix = self.path+'/'.join(root.split(self.path)[-1].split('\\'))

            self.rootList.append(rootRemix)

        for item in self.rootList:
            p = self.treeInfoDict
            for x in item.split('/'):
                p = p.setdefault(x, {})
                
        #for i in range (0,len(self.path.split('/')):
                
        #print self.treeInfoDict
        #--------------------get dirTree info from workspace END-------------------------------------------
        
        #--------------------Return dir info from self.treeIndoDict ------------------------------------------
        
        i=0
        #newDict=treeInfoDict.keys()[0]
        while i < levelCount:

            #cmd =['%s'%pathTextList[i]]
            
            #newDict = treeInfoDict['%s'%pathTextList[i]]
            self.treeInfoDict = self.treeInfoDict['%s'%self.treeInfoDict.keys()[0]]

            i=i+1
            
        self.dirUnderSelectPath = self.treeInfoDict                    #return dict under project
        #print self.dirUnderSelectPath['%s'%self.dirGive]                #return dict under select dir under project
        #print self.dirGive

        self.topLevelItem = self.dirUnderSelectPath.keys()             #return keys,topLevelItems under Projects
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


 