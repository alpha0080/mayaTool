# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha/Documents/maya/2017/scripts/buttonA_UI.ui'
#
# Created: Tue Dec 12 18:56:35 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(731, 549)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 90, 656, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(60, 60))
        self.label_3.setMaximumSize(QtCore.QSize(60, 60))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../prefs/icons/UI/cat-alt-256.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(60, 60))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(200, 60))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.pushButtonB = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonB.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButtonB.setMaximumSize(QtCore.QSize(60, 60))
        self.pushButtonB.setObjectName("pushButtonB")
        self.horizontalLayout.addWidget(self.pushButtonB)
        self.pushButtonC = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonC.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButtonC.setMaximumSize(QtCore.QSize(60, 60))
        self.pushButtonC.setObjectName("pushButtonC")
        self.horizontalLayout.addWidget(self.pushButtonC)
        self.pushButtonD = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonD.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButtonD.setMaximumSize(QtCore.QSize(60, 60))
        self.pushButtonD.setObjectName("pushButtonD")
        self.horizontalLayout.addWidget(self.pushButtonD)
        self.pushButtonE = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonE.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButtonE.setMaximumSize(QtCore.QSize(60, 60))
        self.pushButtonE.setObjectName("pushButtonE")
        self.horizontalLayout.addWidget(self.pushButtonE)
        self.pushButtonA_2 = QtWidgets.QPushButton(Form)
        self.pushButtonA_2.setEnabled(True)
        self.pushButtonA_2.setGeometry(QtCore.QRect(330, 400, 60, 60))
        self.pushButtonA_2.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButtonA_2.setMaximumSize(QtCore.QSize(60, 60))
        self.pushButtonA_2.setAutoFillBackground(False)
        self.pushButtonA_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../prefs/icons/UI/cat-alt-256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonA_2.setIcon(icon)
        self.pushButtonA_2.setIconSize(QtCore.QSize(60, 60))
        self.pushButtonA_2.setFlat(True)
        self.pushButtonA_2.setObjectName("pushButtonA_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "User Name:", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "AAAAAAAAAA", None, -1))
        self.pushButtonB.setText(QtWidgets.QApplication.translate("Form", "ButtonB", None, -1))
        self.pushButtonC.setText(QtWidgets.QApplication.translate("Form", "ButtonC", None, -1))
        self.pushButtonD.setText(QtWidgets.QApplication.translate("Form", "ButtonD", None, -1))
        self.pushButtonE.setText(QtWidgets.QApplication.translate("Form", "ButtonE", None, -1))




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


 