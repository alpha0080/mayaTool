# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha/Documents/GitHub/mayaTool/publishTool/tree_test_UI_a02.ui'
#
# Created: Mon Aug 14 22:42:38 2017
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
        self.treeWidget.setGeometry(QtCore.QRect(130, 30, 256, 461))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 40, 80, 111))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 180, 80, 111))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 350, 80, 111))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
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
        self.treeWidget.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "a", None, -1))
        self.treeWidget.topLevelItem(0).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "a1", None, -1))
        self.treeWidget.topLevelItem(0).child(0).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "a11", None, -1))
        self.treeWidget.topLevelItem(0).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "a2", None, -1))
        self.treeWidget.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "b", None, -1))
        self.treeWidget.topLevelItem(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "c", None, -1))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "A", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "B", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("MainWindow", "C", None, -1))




class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #self.QTITEM.ACTION.connect(self.MODDEF)
        self.setupUi(self)
    #def self.MODDEF(self):
        self.pushButton.clicked.connect(self.runTest)
        
        self.pushButton_2.clicked.connect(self.runTestB)
        
        #self.pushButton_3.clicked.connect(self.runTestC)
        
        
    def runTestB(self):
        print "asdasdsad"
        '''
        parentItemName = self.treeWidget.currentItem().text(0)
        print self.treeWidget.indexOfTopLevelItem(self.treeWidget.currentItem())
        print parentItemName
        getParent =  QtWidgets.QTreeWidgetItem(parentItemName)
       # childItem = QtWidgets.QTreeWidgetItem(getParent)
       # getParent.addChild(childItem)
        print 'getParent',getParent.text(0)
        '''
        parentItem = self.treeWidget.topLevelItem(0).child(0)
        childItem = QtWidgets.QTreeWidgetItem(parentItem)
        parentItem.addChild(childItem)
        
        
    def runTest(self):
        
        self.getAllGrpTransformFromOutliner('character')
        
 
    def getAllGrpTransformFromOutliner(self,topLayerItemInOutlinear):

        tempBuildDefaultGrpList = []
        countList= []
            
        allInTransformGrp = cmds.listRelatives(topLayerItemInOutlinear, children=True, pa=True,ad=True)
        print 'allInTransformGrp',allInTransformGrp
        
        
        
   # def aaa(self):
        if allInTransformGrp == None:
            pass
        else:
            for j in allInTransformGrp:
                grpLingName =  cmds.ls(j,l=True)[0]
                #grpTempList = grpLingName.split('|') 
                tempBuildDefaultGrpList.append(grpLingName.split('|') [1:])
               # print grpLingName.split('|')
                countList.append(len(grpLingName.split('|')))
        print 'countList',countList   
        print 'tempBuildDefaultGrpList',tempBuildDefaultGrpList
        self.treeRefList= []
        self.treeRefDict ={}
        self.allItemDepthList = []
        treeDepth=  sorted(countList)[-1]
        for i in range(0,treeDepth):
            self.treeRefDict.update({str(i):[]})
            #print i
            
        for i in tempBuildDefaultGrpList:
            self.recordItemLevelDict(i)
      #  print self.treeRefList
        print self.treeRefDict
        print 'allItemDepthList',self.allItemDepthList
        
        #self.buildGrpTree(tempBuildDefaultGrpList[0])
    def recordItemLevelDict(self,itemRef):
        
        print 'itemRef',itemRef
        
        for i in range(0,len(itemRef)):
           # self.treeRefDict[str(i)]+(itemRef[i])
            #print itemRef[i]
            tempList = self.treeRefDict[str(i)]#.append(itemRef[i])
            print 'tempList',tempList
            if itemRef[i] in tempList:
                pass
            else:
                tempList.append(itemRef[i])
            depthAddress = ''
            if i ==0  :
                tempList.append(itemRef[i])
                self.allItemDepthList.append({itemRef[i]:depthAddress})
            else :
                    #depthAddress = '0'
                tempList.append(itemRef[i])
            
           # print 'tempList',tempList
           # self.treeRefDict.update({str(i):tempList})

        
        
        
    def buildGrpTree(self,itemFullNameList):
        print 'itemFullNameList',itemFullNameList
        self.treeWidget.clear()
        for i in itemFullNameList:
            item = QtWidgets.QTreeWidgetItem(self.treeWidget)
            item.setText(0,QtWidgets.QApplication.translate("MainWindow", str(i), None, -1))
       # print QtWidgets.QTreeWidgetItem(self.treeWidget)
        #item = QtWidgets.QTreeWidgetItem(self.treeWidget)
       # item.setText(0,QtWidgets.QApplication.translate("MainWindow", "ccc", None, -1))
      #  item2 =QtWidgets.QTreeWidgetItem(item)
       # item.addChild(item)
       # PySide2.QtWidgets.QTreeWidgetItem.addChild(PySide2.QtWidgets.QTreeWidgetItem)
        #item.setText(0,QtWidgets.QApplication.translate("MainWindow", "ccc", None, -1))
      #  print item
        
            
    
    def test(self):   
        maxDepth = sorted(countList)[-1]

        elementEveryLevelCount = {}
        itemHierarchy = {}
        for i in range(1,maxDepth):
            elementEveryLevelCount.update({i:[]})
        for i in tempBuildDefaultGrpList:
            chaList =  i.split('|')
           # print 'chaList',chaList
            #getItemHierarchy(chaList,maxDepth,elementEveryLevelCount)
          #  getItemHierarchyB(chaList,itemHierarchy)
        cha = tempBuildDefaultGrpList[0]
      #  print 'cha',cha
        self.getItemHierarchyC(cha,itemHierarchy)
        
    def getItemHierarchyC(self,cha, itemHierarchy):
        print cha   

        
      #  print 'elementEveryLevelCount',elementEveryLevelCount
       # print 'itemHierarchy',itemHierarchy
        
        
    def createTree(self):
        print 'aaaaa'
        
        self.treeWidget.clear()
        
      #  item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item.setText(0,QtWidgets.QApplication.translate("MainWindow", "ccc", None, -1))
        item2 =QtWidgets.QTreeWidgetItem(item)



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


 