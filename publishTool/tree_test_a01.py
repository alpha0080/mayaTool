# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha/Documents/GitHub/test/QTtest/fileDir_test_02/tree_test_UI_a01.ui'
#
# Created: Thu Aug 10 22:41:45 2017
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
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))




class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #self.QTITEM.ACTION.connect(self.MODDEF)
        self.setupUi(self)
    #def self.MODDEF(self):
    
        self.pushButton.clicked.connect(self.runTest)
        
    def runTest(self):
        
        self.getAllGrpTransformFromOutliner('character')
        
 
    def getAllGrpTransformFromOutliner(self,topLayerItemInOutlinear):

        tempBuildDefaultGrpList = []
        countList= []
            
        allInTransformGrp = cmds.listRelatives(topLayerItemInOutlinear, children=True, pa=True,ad=True)
            #print allInTransformGrp
        if allInTransformGrp == None:
            pass
        else:
            for j in allInTransformGrp:
                grpLingName =  cmds.ls(j,l=True)[0]
                tempBuildDefaultGrpList.append(grpLingName)
              #  print grpLingName
                countList.append(len(grpLingName.split('|')))
                
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
        getItemHierarchyC(cha,itemHierarchy)
        
    def getItemHierarchyC(cha, itemHierarchy):
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


 