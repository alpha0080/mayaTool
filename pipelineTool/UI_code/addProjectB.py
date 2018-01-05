# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/alphaOnly/github/pipelineTool/UI_code/addProjectB.ui'
#
# Created: Thu Dec 28 16:58:35 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

        self.addProject_Frame = QtWidgets.QFrame(self.centralwidget)
        self.addProject_Frame.setGeometry(QtCore.QRect(10, 10, 191, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.addProject_Frame.setPalette(palette)
        self.addProject_Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.addProject_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.addProject_Frame.setObjectName("addProject_Frame")
        self.addProject_buttonLabel = QtWidgets.QPushButton(self.addProject_Frame)
        self.addProject_buttonLabel.setGeometry(QtCore.QRect(30, 0, 150, 30))
        self.addProject_buttonLabel.setMinimumSize(QtCore.QSize(150, 30))
        self.addProject_buttonLabel.setMaximumSize(QtCore.QSize(150, 30))
        self.addProject_buttonLabel.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/alphaOnly/github/pipelineTool/UI/label_G1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addProject_buttonLabel.setIcon(icon)
        self.addProject_buttonLabel.setIconSize(QtCore.QSize(150, 30))
        self.addProject_buttonLabel.setFlat(True)
        self.addProject_buttonLabel.setObjectName("addProject_buttonLabel")
        self.addProject_labelName = QtWidgets.QLabel(self.addProject_Frame)
        self.addProject_labelName.setGeometry(QtCore.QRect(41, 7, 120, 16))
        self.addProject_labelName.setMinimumSize(QtCore.QSize(120, 16))
        self.addProject_labelName.setMaximumSize(QtCore.QSize(120, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.addProject_labelName.setFont(font)
        self.addProject_labelName.setObjectName("addProject_labelName")
        self.addProject_buttonCheck = QtWidgets.QPushButton(self.addProject_Frame)
        self.addProject_buttonCheck.setGeometry(QtCore.QRect(0, 0, 30, 30))
        self.addProject_buttonCheck.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/alphaOnly/github/pipelineTool/UI/label_G2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addProject_buttonCheck.setIcon(icon1)
        self.addProject_buttonCheck.setIconSize(QtCore.QSize(30, 30))
        self.addProject_buttonCheck.setFlat(True)
        self.addProject_buttonCheck.setObjectName("addProject_buttonCheck")


        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.addProject_labelName.setText(QtWidgets.QApplication.translate("MainWindow", "Fishhing Hunter", None, -1))




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


 