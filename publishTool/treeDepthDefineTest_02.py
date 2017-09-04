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
        self.pushButton_2.clicked.connect(self.treeBuildTest)
        self.pushButton_3.clicked.connect(self.treeInfo)
        
    def treeInfoB(self):
        #print self.treeWidget.topLevelItemCount()
        tempMaxDepthContainList = []
        for i in self.allAssetGrpDepthDict:                   #check item maxdepth
            checkMaxDepth =  len(self.allAssetGrpDepthDict[i])
            if checkMaxDepth in tempMaxDepthContainList:
                pass
            else:
                tempMaxDepthContainList.append(checkMaxDepth)
           # print self.allAssetGrpDepthDict[i][0]
        maxItemDepth = sorted(tempMaxDepthContainList)[-1]
        for i in self.allAssetGrpDepthDict.keys():
            print self.allAssetGrpDepthDict[i]#[0]
            
       # for i in range(0,5):
    def treeInfo(self):
       # print 'aaaa'
        print 'aaa',self.treeWidget.topLevelItem(1).text(0)
        item2 =  QtWidgets.QTreeWidgetItem(self.treeWidget.topLevelItem(1))
        item3= QtWidgets.QTreeWidgetItem(item2)
        print item2.parent().childCount()# get child count
     #   print self.treeWidget.topLevelItemCount()
       # item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget.topLevelItem(7))
     #   self.treeWidget.topLevelItem(6).setText(0, QtWidgets.QApplication.translate("MainWindow", "asdasd", None, -1))
      #  self.allAssetGrpDepthDict[  self.allAssetGrpDepthDict         
        
        
    
    def treeBuildTestB(self):
        print 'tree test'
        print 'self.allAssetGrpDepthDict', self.allAssetGrpDepthDict
       # QtWidgets.QTreeWidgetItem
        #QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.clear()
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
       # aa = QtWidgets.QTreeWidget.topLevelItem(1)
       # PySide2.QtWidgets.QTreeWidgetItem(PySide2.QtWidgets.QTreeWidget, PySide2.QtWidgets.QTreeWidgetItem, int = Type)
       
    def treeBuildTest(self):
        print 'testC'
        index = 0
        self.treeWidget.clear()
        #for index in range(0,10):
        print self.allAssetGrpDepthDict[self.allAssetGrpDepthDict.keys()[index]]
        rangeCount = len(self.allAssetGrpDepthDict[self.allAssetGrpDepthDict.keys()[index]])
        topLayerItem = QtWidgets.QTreeWidgetItem(self.treeWidget)
        
        for i in range(0,rangeCount):
            
            maxCurrentLevelCount = int(self.allAssetGrpDepthDict[self.allAssetGrpDepthDict.keys()[index]][i])
            if i == 0:           #create toplevelItem
                for j in range(0,maxCurrentLevelCount):
                    topLayerItem = QtWidgets.QTreeWidgetItem(self.treeWidget)
              #  childItem.setText(0,'aaaa')
            else:
                topLayerItem = QtWidgets.QTreeWidgetItem(topLayerItem)
           # topLayerItem.setText(0,'ttt')
                for j in range(0,maxCurrentLevelCount):
                    childItem = QtWidgets.QTreeWidgetItem(topLayerItem)
              #  childItem.setText(0,'aaaa')

                
        
        
    def treeBuildTestC(self):
        self.treeWidget.clear()
        
        item_1 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_2 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_3 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_4 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_5 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_6 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "character", None, -1))
        self.treeWidget.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "vehicle", None, -1))
        self.treeWidget.topLevelItem(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "set", None, -1))
        self.treeWidget.topLevelItem(3).setText(0, QtWidgets.QApplication.translate("MainWindow", "prop", None, -1))
        self.treeWidget.topLevelItem(4).setText(0, QtWidgets.QApplication.translate("MainWindow", "other", None, -1))
        self.treeWidget.topLevelItem(5).setText(0, QtWidgets.QApplication.translate("MainWindow", "effect", None, -1))
        
        #item >>> PySide2.QtWidgets.QTreeWidgetItem
            #    defaultAssetBuildDict = {'character':'0','vehicle':'1','set':'2','prop':'3','other':'4','effect':'5'}
       # self.treeWidget.
      #  for i in item_1:
       #     self.defaultAssetBuildDict = {'character':'0','vehicle':'1','set':'2','prop':'3','other':'4','effect':'5'}

       #     print i
       # print self.treeWidget.topLevelItem(5)
        #vcheck topLayerItem 
        for i in self.allAssetGrpDepthDict:
            topLevelItem =  i.split('|')[1:]
          #  print 'topLevelItem',topLevelItem
           # self.checkReativesChild(topLevelItem[0])
            topLayerItemIndex = self.defaultAssetBuildDict[topLevelItem[0]]
            print 'topLayerItemIndex',topLayerItemIndex
            
            print  self.allAssetGrpDepthDict[i][0]


            
        #check topLayerItem    
        for i in self.allAssetGrpDepthDict.keys():
            print self.allAssetGrpDepthDict[i]
            for j in range (1,len(self.allAssetGrpDepthDict[i])):
                topLayerItemIndex = int(self.allAssetGrpDepthDict[i][0])
                currentLayerCount = int(self.allAssetGrpDepthDict[i][j])
          #  print self.allAssetGrpDepthDict[i]
            #    print 'topLayerItemIndex',topLayerItemIndex
            #    print 'currentLayerCount',currentLayerCount
                self.buildChildTree(topLayerItemIndex,currentLayerCount,j)
         #   for j in self.allAssetGrpDepthDict[i]:
         
         
    def buildChildTree(self,topLayerItemIndex,currentLayerCount,depth):
        print 'topLayerItemIndex',topLayerItemIndex
        print 'currentLayerCount',currentLayerCount
        print 'depth',depth
        if depth == 1 :
            topLayerChildCount = self.treeWidget.topLevelItem(topLayerItemIndex).childCount()
            delta = currentLayerCount - topLayerChildCount
            print 'delta',delta
            if delta >= 0:
                
                for j in range(0,delta+1):
                        
                    item_1 = QtWidgets.QTreeWidgetItem(self.treeWidget.topLevelItem(topLayerItemIndex))
                    
            else:
                pass
        else:
            print 'depth > 1'
            #itemWidgetIndex = 
            for i in range(0,depth):
                print i
            
                
                      #  item_2 = QtWidgets.QTreeWidgetItem(item_1)
                        
              #  item = QtWidgets.QTreeWidgetItem(self.treeWidget.topLevelItem(topLayerItemIndex))
        #else:
          #  item = QtWidgets.QTreeWidgetItem(self.treeWidget.topLevelItem(topLayerItemIndex))
      
        #print self.treeWidget.topLevelItem(topLayerItemIndex).count()
      #  for i in range(0,currentLayerCount):
       #     print 'cccc',i
      #      if i < currentLayerCount:
        #        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget.topLevelItem(topLayerItemIndex))
#
            
                
                
        '''
            if self.treeWidget.topLevelItemCount() < self.allAssetGrpDepthDict[i][0]:
                delta =  int(self.allAssetGrpDepthDict[i][0])-self.treeWidget.topLevelItemCount()
                print 'topLayerItem',self.treeWidget.topLevelItemCount()
                print 'needTopLayerItem',int(self.allAssetGrpDepthDict[i][0])
                print delta
                if delta >= 0:
                    for j in range(0,delta+1):
                        
                        item_1 = QtWidgets.QTreeWidgetItem(self.treeWidget)
                        item_2 = QtWidgets.QTreeWidgetItem(item_1)
                        
                else:
                    pass
                
            else:
                pass
                
        '''
            
        
            
            
            

    def checkReativesChild(self,item):
      #  print item
        childItem = cmds.listRelatives(item,c=True)
        print childItem
        
        

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
                  #  print objNodeType
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
    
    
    def getItemStructure(self,searchAsset,assetIndex):
       # print 'getItemStructure start' 
        allItemInTopLayerItem = cmds.listRelatives(searchAsset, children=True, pa=True,ad=True,f=True)
       # print allItemInTopLayerItem
        for i in allItemInTopLayerItem:
        #    print i
            tempItemLevelList = [assetIndex]
            for j in i.split('|'):
                #print j
                try:
                   # print j,self.itemLevelDict[j]
                    getPartDepthLevel = self.itemLevelDict[j][0]  #get index of each depth level
                   # print j,getPartDepthLevel
                    tempItemLevelList.append(str(getPartDepthLevel))
                    #self.allAssetGrpDepthDict.update({j:self.itemLevelDict[j]})

                except:
                    pass
                print 'tempItemLevelList',tempItemLevelList
                
            self.allAssetGrpDepthDict.update({i:tempItemLevelList})
        
        
        

    def storeOutLineStructure(self):
       # print 'aaaa'
        self.itemLevelDict = {}    #create empty itemLevelDict ,item dictionary
        self.allAssetGrpDepthDict = {}    #create empty dict, that reference group depth and index to each item and grp
        
        self.defaultAssetBuildDict = {'character':'0','vehicle':'1','set':'2','prop':'3','other':'4','effect':'5'}
        for i in self.defaultAssetBuildDict:
            try:
                self.getOutLinerStructure(i)
            #print i
            except:
                pass
        print 'itemLevelDict',self.itemLevelDict
        
        for i in self.defaultAssetBuildDict.keys():
            try:
                self.getItemStructure(i,self.defaultAssetBuildDict[i])
            except:
                pass
        print 'self.allAssetGrpDepthDict', self.allAssetGrpDepthDict
                
            
        
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

