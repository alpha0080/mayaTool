import maya.cmds as cmds
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/alphaOnly/github/mayaTool/publishTool/treeTest.ui'
#
# Created: Fri Sep 01 14:22:06 2017
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
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 50, 181, 81))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 170, 181, 81))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 290, 181, 81))
        self.pushButton_3.setObjectName("pushButton_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(390, 390, 371, 121))
        self.plainTextEdit.setObjectName("plainTextEdit")
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
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "A", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "B", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("MainWindow", "A", None, -1))




class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #self.QTITEM.ACTION.connect(self.MODDEF)
        self.setupUi(self)
    #def self.MODDEF(self):
        self.pushButton.clicked.connect(self.storeOutLineStructure)

    def getOutLinerStructure(self,searchAsset):

        #searchAsset = 'character'
        tempBuildDefaultGrpList = []
        tempBuildDefaultGrpList.append(searchAsset)


        countList= []
                    
        allInTransformGrp = cmds.listRelatives(searchAsset, children=True, pa=True,ad=True)

        #print cmds.listRelatives('character|L1_1|L2_1_1|L3_2_1_1', children=True, pa=True,ad=0)
                    #print allInTransformGrp
        if allInTransformGrp == None:
            pass
        else:
            for j in allInTransformGrp:
                grpLingName =  cmds.ls(j,l=True)[0]
                tempBuildDefaultGrpList.append(grpLingName)
              #  print grpLingName
                countList.append(len(grpLingName.split('|')))
                        
        maxDepth = sorted(countList)[-1]-1
        print 'maxDepth',maxDepth
        elementEveryLevelCount = {}
        itemHierarchy = {}
        depthDict = {}

        for i in range(0, maxDepth):
            depthDict.update({i:{}})
            
        #print depthDict
        for i in range(1,maxDepth):
            elementEveryLevelCount.update({i:[]})
          
        allItemReleationShipDist = {}  
          
        #for i in tempBuildDefaultGrpList:
        #    print i 
            
            
        refChildDict = {}
        
            
        for i in tempBuildDefaultGrpList:
           # print i
            #chaList =  i.split('|')
            refChild = cmds.listRelatives(i, children=True, pa=True,ad=0)  
            #print 'refChild',refChild,type(refChild)
            refChildList = []
            try:
                refMaxCount= len(refChild)
               # print 'refMaxCount',refMaxCount
                for j in range(0,refMaxCount):
                    indexOfItem = refChild[j].split('|')[-1]+'.'+str(j)
                    #print j ,refChild[j]
                   # print indexOfItem
                    refChildList.append(indexOfItem)
                    objNodeType = cmds.nodeType(refChild[j])
                    print objNodeType
                    self.itemLevelDict.update({refChild[j].split('|')[-1]:[str(j),objNodeType]})
                refChildDict.update({i.split('|')[-1]:refChildList})
            except:
                refMaxCount = 'none'
                refChildDict.update({i.split('|')[-1]:'None'})
            refParent = cmds.listRelatives(i, children=True, p=True,ad=0) 
         #   for refParent in self.itemLevelDict.keys():
          #      print refParent,  self.itemLevelDict[refParent]
                
           # print 'refParent', refParent
           # print'totalItemCount' , len(refChildDict.keys())
               # print refMaxCount
           # print 'itemLevelDict',itemLevelDict
            refChildSerNum = []
    
    
    def getItemStructure(self):
        print 'getItemStructure start' 
        
        

    def storeOutLineStructure(self):
        print 'aaaa'
        self.itemLevelDict = {}    #create empty itemLevelDict ,item dictionary
        defaultAssetBuildList = ['character','set','prop','vehicle','other','effect']
        for i in defaultAssetBuildList:
            try:
                self.getOutLinerStructure(i)
            #print i
            except:
                pass
        print 'itemLevelDict',self.itemLevelDict
        
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

