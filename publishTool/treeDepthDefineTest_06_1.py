
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/alphaOnly/github/mayaTool/publishTool/treeTest.ui'
#
# Created: Fri Sep 01 14:22:06 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import maya.cmds as cmds



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
        self.pushButton_2.clicked.connect(self.runBuildItemLevelTree)
        self.pushButton_3.clicked.connect(self.setItemName)
        
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




##------------------------------------------------------------------------------------------------------------------------------------------        
       
    def runBuildItemLevelTree(self):
        print 'start to build itemTree'
        self.treeWidget.clear()
        self.buildDefaultTopLayerItem()


        print 'build tree'
        totalIteCount = len(self.allAssetGrpDepthDict.keys())   # get how many items in self.allAssetGrpDepthDict  �A��ooutline���Ҧ��h�Ū��W���`�ƶq
        for i in range(0,totalIteCount):
           # print i
            eachItemFullName =  self.allAssetGrpDepthDict.keys()[i]        #��o�C�Ӽh��group�W��,fullName ����W��
            eachItemShortName = eachItemFullName.split('|')[-1]
            eachItemDepthList = self.allAssetGrpDepthDict[self.allAssetGrpDepthDict.keys()[i]] #��o�C�Ӽh��group �ҹ������h��List
            eachItemFullDepth = len(eachItemDepthList) #��o����Ҧb�h�šA �C�Ӫ����`�h��

            topLayerItemIndex = int(eachItemDepthList[0])
            topLayerItemSelect = self.treeWidget.topLevelItem(topLayerItemIndex)
            parentItem = topLayerItemSelect


            for depth in range(1,eachItemFullDepth):
               # print 'depth',depth
                currentCount = parentItem.childCount()

                maxCount = int(eachItemDepthList[depth])+1

                placeIndex = int(eachItemDepthList[depth])

                delta = maxCount - currentCount

                if delta <= 0:

                    parentItem = parentItem.child(placeIndex)

                else:
                    self.createChildItem(delta,currentCount,parentItem,eachItemShortName)
                
                #try:
                    parentItem = self.childItem.parent().child(placeIndex)   #�^�Ǧb�ĴX�Ӥ���
            self.defineItemAddress(parentItem,eachItemDepthList,eachItemShortName)
            
    def defineItemAddress(self,parentItem,eachItemDepthList,eachItemShortName):
        depthLength = len(eachItemDepthList)
       # print depthLength
        itemSelect = parentItem
      #  print parentItem.text(0),parentItem.child(2).text(0)
        for childIndex in range(1,depthLength):
           # print listIndex[childIndex]
        
            itemSelect = itemSelect.child(int(eachItemDepthList[childIndex]))
            #print listIndex[childIndex]
       # print itemSelect.text(0)
        itemSelect.setText(0,eachItemShortName)
        
      #  itemSelect.setText('0',itemName)            
            
            

    def buildDefaultTopLayerItem(self):

        defaultTopLayerItem = ['character','vehicle','set','prop','other','effect']
        for i in defaultTopLayerItem:
            #itemName = defaultTopLayerItem[i]
            topLayerItem = QtWidgets.QTreeWidgetItem(self.treeWidget) 
            topLayerItem.setText(0,'%s'%i)
    


        
    def createChildItem(self,delta,currentCount,parentItem,eachItemShortName):   # maxCount ���Ӽh�Żݭn�ЫشX�Ӫ���
        print 'eachItemShortName',eachItemShortName


        #self.checkItemInPosition()
        for i in range(0,delta):

            self.childItem =  QtWidgets.QTreeWidgetItem(parentItem)
            self.childItem.setText(0,eachItemShortName)

    
##-----------------------------------------------------------------------------------------------------------------------------------   
        
    def setItemName(self):
        
       # print self.treeWidget.topLevelItem(0).child(2).child(0).child(2).child(1).setText(0,'adadsadad')
        listIndex = ['0', '0', '0', '2', '1']
        itemName = 'L5_hh2'
        parentItem = self.treeWidget.topLevelItem(0)
        totalItemCounts = len(self.allAssetGrpDepthDict.keys())
        for i in range(0, totalItemCounts):
            itemName =  self.allAssetGrpDepthDict.keys()[i].split('|')[-1]
            listIndex = self.allAssetGrpDepthDict[self.allAssetGrpDepthDict.keys()[i]]
            parentItem = self.treeWidget.topLevelItem(int(listIndex[0]))

            self.defineItemAddress(parentItem,listIndex,itemName)
        
    
    


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
              #  print 'tempItemLevelList',tempItemLevelList
                
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

