# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha/Documents/GitHub/ribGen/convertUI/convert_UI_to_PY_QT5.uI'
#
# Created: Tue Feb 28 22:40:45 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets
import maya.cmds as cmds
import pymel.core as pm
import os

global ui
from PySide2 import QtCore, QtGui, QtWidgets
from pyside2uic import compileUi


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 433)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(75, 114, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 44, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 114, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 44, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 114, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 44, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 180, 741, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_03 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_03.setGeometry(QtCore.QRect(20, 350, 741, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.pushButton_03.setFont(font)
        self.pushButton_03.setObjectName("pushButton_03")
        self.pushButton_01 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_01.setGeometry(QtCore.QRect(20, 20, 741, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.pushButton_01.setFont(font)
        self.pushButton_01.setObjectName("pushButton_01")
        self.pushButton_02 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_02.setGeometry(QtCore.QRect(20, 110, 741, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.pushButton_02.setFont(font)
        self.pushButton_02.setObjectName("pushButton_02")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 230, 61, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(250, 249, 206))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 249, 206))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label.setPalette(palette)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 220, 651, 50))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Python Tool", None, -1))
        self.pushButton_03.setText(QtWidgets.QApplication.translate("MainWindow", "Convert", None, -1))
        self.pushButton_01.setText(QtWidgets.QApplication.translate("MainWindow", "get the original UI file", None, -1))
        self.pushButton_02.setText(QtWidgets.QApplication.translate("MainWindow", "Test UI", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "FileName:", None, -1))





class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #self.QTITEM.ACTION.connect(self.MODDEF)
    #def self.MODDEF(self):
        
        
        # self.setWindowFlags(QtCore.Qt.Tool)
        self.setupUi(self)
        #self.pushButton.clicked.connect(self.buttonPushCommand(happy=2))
        self.pushButton_01.clicked.connect(self.modpushButton_01)
        self.pushButton_02.clicked.connect(self.modpushButton_02)
        self.pushButton_03.clicked.connect(self.modpushButton_03)

        self.lineEdit.textChanged.connect(self.modlineEdit)
        
        
        
        
    def modpushButton_01(self):
        
        self.uiFileLongName = cmds.fileDialog2(fm=1)[0]
        print self.uiFileLongName
        
        self.pushButton_01.setText(self.uiFileLongName)
        self.workPath = os.path.split(self.uiFileLongName)[0]
        self.UiFileName = os.path.split(self.uiFileLongName)[1].split('.')[0]+'.py'

        
        #newUiToPyName = self.uiFile.split('/')[-1].split('.')[0]+'.py'
        self.lineEdit.setText(self.UiFileName)
        
        
    def modpushButton_02(self):
        
        dialog1 = cmds.loadUI(f=self.uiFileLongName)
        cmds.showWindow(dialog1)

        print"test UI,%s"%self.uiFileLongName
  
    def modpushButton_03(self):
        self.modlineEdit()
        
        

        
        pyfile = open(self.uiToPyFileLongName, 'w')
        #pyfileTemp = open(self.uiToPyFileLongName+'.temp','w')
        compileUi(self.uiFileLongName, pyfile, False, 4,False)
        defActionConnectText="\n\n\nclass mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):\n   \n    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):\n        super(mod_MainWindow, self).__init__(parent)\n        #self.QTITEM.ACTION.connect(self.MODDEF)\n        self.setupUi(self)\n    #def self.MODDEF(self):\n\n\n\n"
        defMainText="def main():\n    global ui\n    app = QtWidgets.QApplication.instance()\n    if app == None: app = QtWidgets.QApplication(sys.argv)\n    try:\n        ui.close()\n        ui.deleteLater()\n    except: pass\n    ui = mod_MainWindow()\n    ui.show()\n \nif __name__ == '__main__':\n    main()\n\n\n "           
                                   
        #pyfileTemp.write(titleText)
        pyfile.write(defActionConnectText)
        
        pyfile.write(defMainText)
        #pyfileTemp.close()
        
        pyfile.close()
        
        print"convert %s to file %s"%(self.uiFileLongName,self.uiToPyFileLongName)
        
    def modlineEdit(self):
        self.UiFileName = self.lineEdit.text()
        self.uiToPyFileLongName = self.workPath + '/'+self.UiFileName
        print self.UiFileName
        print self.uiToPyFileLongName
        
        
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
    