# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/alphaOnly/github/pipelineTool/UI_code/addButtonC.ui'
#
# Created: Fri Dec 29 16:37:50 2017
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
        self.projectButtonA = QtWidgets.QPushButton(self.centralwidget)
        self.projectButtonA.setGeometry(QtCore.QRect(10, 10, 30, 30))
        self.projectButtonA.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../UI/label_G2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("../UI/label_G2_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("../UI/label_G2_2.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.projectButtonA.setIcon(icon)
        self.projectButtonA.setIconSize(QtCore.QSize(30, 30))
        self.projectButtonA.setCheckable(True)
        self.projectButtonA.setFlat(True)
        self.projectButtonA.setObjectName("projectButtonA")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))




class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #self.QTITEM.ACTION.connect(self.MODDEF)
        self.setupUi(self)
    #def self.MODDEF(self):



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


 