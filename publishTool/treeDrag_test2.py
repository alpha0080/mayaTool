# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/alphaOnly/github/mayaTool/publishTool/treeDrag_test.ui'
#
# Created: Tue Sep 26 10:42:52 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMouseTracking(True)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)

        self.treeWidget.setGeometry(QtCore.QRect(90, 10, 256, 471))
        self.treeWidget.setDragEnabled(False)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        
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


    def mousePressEvent(self, event):
        self.treeWidget.mousePressEvent(event)
        print 'asd'

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.treeWidget.headerItem().setText(0, QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "a", None, -1))
        self.treeWidget.topLevelItem(0).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "a1", None, -1))
        self.treeWidget.topLevelItem(0).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "a2", None, -1))
        self.treeWidget.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "b", None, -1))
        self.treeWidget.topLevelItem(1).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "b1", None, -1))
        self.treeWidget.topLevelItem(1).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "b2", None, -1))
        self.treeWidget.topLevelItem(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "c", None, -1))
        self.treeWidget.topLevelItem(3).setText(0, QtWidgets.QApplication.translate("MainWindow", "d", None, -1))
        self.treeWidget.setSortingEnabled(__sortingEnabled)

#class MyTreeView(QtWidgets.QTreeView):

   # def __init__(self, parent=None):
   #     super(MyTreeView, self).__init__(parent)
   #     self.dropIndicatorRect = QtCore.QRect()
class MyTreeWidget(QtWidgets.QTreeWidget,Ui_MainWindow):

    def __init__(self):
      #  super(MyTreeWidget, self).setupUi(self)
        #self.treeWidget = QtWidgets.QTreeWidget(QtWidgets.QWidget(MainWindow))
       # print parent.objectName()
        print '11111'#,MyTreeWidget.objectName()
       # self.itemDoubleClicked.connect(self.addHere)
    def test(self):
        print 'test'
            

    '''
    def delButtonPressed(self):
        self.setDragEnabled(True)
        print'ggaa',self.currentItem()
        for item in self.selectedItems():
            if item.deletable:
                item.parent.removeChild(item)
                MyTreeItemClass.child_list.remove(item)
        
    def addHere(self, clickeditem, column):
        global listbox
        
        for x in listbox.selectedItems():
            if clickeditem.can_add_here == True:
                print('Adding item(s) here', clickeditem.treetext)
                itemtext = x.text()
                newtreeitem = MyTreeItemClass(itemtext, parent=clickeditem)
                clickeditem.setExpanded(False)  # need to use false to counter-act the double-clicking action?
            else:
               print('cannot add to this item') 
    '''

class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #super(tree,self).__init__()
       # super(mod_MainWindow, self).__init__(parent)
        #self.centralwidget = QtWidgets.QWidget(MainWindow)
        
    #    super(MyTreeView, self).__init__()
        #self.QTITEM.ACTION.connect(self.MODDEF)
       # print QtWidgets.QTreeWidget(self.centralwidget)
        self.setupUi(self)
     #   tree = QtWidgets.treeWidget()
        print self.treeWidget

       # MyTreeWidget()
       # print self.objectName()
      #  print self.treeWidget.objectName()
        #tree = self.treeWidget
      #  self.tree = MyTreeWidget(self.treeWidget)
      #  self.tree.hello()
        #print self.tree.objectName()
    #def self.MODDEF(self):
      #  aa = self.treeWidget
        self.treeWidget.setDragEnabled(True)
       # print tree
        self.treeWidget.setDragDropOverwriteMode(True)
        self.treeWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.treeWidget.setDefaultDropAction(QtCore.Qt.LinkAction)
        self.treeWidget.setMouseTracking(True)
     #   self.tree = MyTreeWidget()
       # self.treeWidget.pressed.connect(self.test)
        #self.treeWidget.itemCollapsed.connect(self.testB)
        
    def testB(self):
        print 'change'
        #selectItem = self.treeWidget.currentItem()
        #print 'item',selectItem.text(0)
        #print 'parent',selectItem.parent().text(0)

        #print 'bbb'
        
    def test(self):
        item = self.treeWidget.currentItem()
        print dir(self.treeWidget.DragSelectingState)
        print self.treeWidget
        self.dropEvent()
       # print 'press'
        #selectItem = self.treeWidget.currentItem()
      #  selectItem = self.treeWidget.currentItem()
       # print self.treeWidget.selectedItems(0)
       # print 'parent',selectItem.parent().text(0)
       # selectItem.pressed.connect(self.testB)
      #  print self.treeWidget.itemCollapsed

        #self.treeWidget.itemEntered.connect(self.testB)
    def keyPressEvent(self, e):     
        print 'press'   
        if e.key() == QtCore.Qt.Key_Delete:
            #print('pressed delete key')
            self.delButtonPressed()

    def delButtonPressed(self):
       # self.treeWidget.setDragEnabled(True)
        print'ggaa',self.treeWidget.currentItem().text(0)
       # for item in self.selectedItems():
       #     if item.deletable:
      #          item.parent.removeChild(item)
     #           MyTreeItemClass.child_list.remove(item)
       # 

                

        #print 'press'
        
        #print self.treeWidget
       # l2 = QtWidgets.QTreeWidgetItem(["c"])
        #print QtWidgets.QTreeWidget.pos(QtWidgets.QWidget(l2))
       # print l2.pos()
    
    def dropEvent(self, e):
        item=self.itemAt(e.pos())
        if item: self.addHere(item)
        e.accept()
        
        
        #print MyTreeView
        
    def mousePressEvent(self, e):
        print self.treeWidget
        self.treeWidget.mousePressEvent(e)
        print self.treeWidget.dragEnterEvent(e)
       # print aa
        print 'asd'

    def dragEnterEvent(self, event):
        print 'dfdffdfdfd'
        if event.mimeData().hasFormat("application/x-ltreedata"):
            event.accept()
        else:
            event.ignore()
        print 'cd'
        
        
        


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


 