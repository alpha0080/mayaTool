# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha/Documents/GitHub/mayaTool/publishTool/exportTool_UI_a01.ui'
#
# Created: Tue Jun 13 22:36:24 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1118, 770)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_dynamicIO = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_dynamicIO.setEnabled(True)
        self.groupBox_dynamicIO.setGeometry(QtCore.QRect(960, 50, 150, 150))
        self.groupBox_dynamicIO.setFlat(True)
        self.groupBox_dynamicIO.setCheckable(True)
        self.groupBox_dynamicIO.setObjectName("groupBox_dynamicIO")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_dynamicIO)
        self.checkBox_5.setGeometry(QtCore.QRect(20, 30, 158, 18))
        self.checkBox_5.setChecked(True)
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_dynamicIO)
        self.checkBox_6.setGeometry(QtCore.QRect(20, 60, 158, 18))
        self.checkBox_6.setChecked(True)
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox_dynamicIO)
        self.checkBox_7.setGeometry(QtCore.QRect(20, 90, 158, 18))
        self.checkBox_7.setChecked(True)
        self.checkBox_7.setObjectName("checkBox_7")
        self.groupBox_LookIO = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_LookIO.setGeometry(QtCore.QRect(800, 210, 150, 150))
        self.groupBox_LookIO.setFlat(True)
        self.groupBox_LookIO.setCheckable(True)
        self.groupBox_LookIO.setObjectName("groupBox_LookIO")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_LookIO)
        self.checkBox.setGeometry(QtCore.QRect(20, 30, 158, 18))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox_LookIO)
        self.checkBox_8.setGeometry(QtCore.QRect(20, 60, 158, 18))
        self.checkBox_8.setObjectName("checkBox_8")
        self.groupBox_proxy_IO = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_proxy_IO.setGeometry(QtCore.QRect(960, 210, 150, 150))
        self.groupBox_proxy_IO.setFlat(True)
        self.groupBox_proxy_IO.setCheckable(True)
        self.groupBox_proxy_IO.setObjectName("groupBox_proxy_IO")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_proxy_IO)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 30, 158, 18))
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_proxy_IO)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 60, 158, 18))
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_proxy_IO)
        self.checkBox_4.setGeometry(QtCore.QRect(20, 90, 158, 18))
        self.checkBox_4.setObjectName("checkBox_4")
        self.groupBox_lightIO = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_lightIO.setGeometry(QtCore.QRect(800, 50, 150, 150))
        self.groupBox_lightIO.setFlat(True)
        self.groupBox_lightIO.setCheckable(True)
        self.groupBox_lightIO.setObjectName("groupBox_lightIO")
        self.checkBox_9 = QtWidgets.QCheckBox(self.groupBox_lightIO)
        self.checkBox_9.setGeometry(QtCore.QRect(20, 30, 158, 18))
        self.checkBox_9.setChecked(True)
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.groupBox_lightIO)
        self.checkBox_10.setGeometry(QtCore.QRect(20, 60, 158, 18))
        self.checkBox_10.setChecked(True)
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_13 = QtWidgets.QCheckBox(self.groupBox_lightIO)
        self.checkBox_13.setGeometry(QtCore.QRect(20, 90, 158, 18))
        self.checkBox_13.setChecked(True)
        self.checkBox_13.setObjectName("checkBox_13")
        self.groupBox_renderIO = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_renderIO.setGeometry(QtCore.QRect(800, 370, 150, 150))
        self.groupBox_renderIO.setFlat(True)
        self.groupBox_renderIO.setCheckable(True)
        self.groupBox_renderIO.setObjectName("groupBox_renderIO")
        self.checkBox_renderCam = QtWidgets.QCheckBox(self.groupBox_renderIO)
        self.checkBox_renderCam.setGeometry(QtCore.QRect(20, 30, 158, 18))
        self.checkBox_renderCam.setChecked(True)
        self.checkBox_renderCam.setObjectName("checkBox_renderCam")
        self.checkBox_renderSet = QtWidgets.QCheckBox(self.groupBox_renderIO)
        self.checkBox_renderSet.setGeometry(QtCore.QRect(20, 60, 158, 18))
        self.checkBox_renderSet.setObjectName("checkBox_renderSet")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(50, 40, 701, 401))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 134, 134))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 111, 111))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 59, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 134, 134))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 111, 111))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 59, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 134, 134))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 111, 111))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 59, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.treeWidget.setPalette(palette)
        self.treeWidget.setAutoScrollMargin(16)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.treeWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.treeWidget.setIndentation(20)
        self.treeWidget.setRootIsDecorated(True)
        self.treeWidget.setUniformRowHeights(False)
        self.treeWidget.setItemsExpandable(True)
        self.treeWidget.setAllColumnsShowFocus(False)
        self.treeWidget.setWordWrap(False)
        self.treeWidget.setExpandsOnDoubleClick(True)
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.header().setVisible(True)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setDefaultSectionSize(300)
        self.treeWidget.header().setHighlightSections(True)
        self.treeWidget.header().setMinimumSectionSize(30)
        self.treeWidget.header().setSortIndicatorShown(False)
        self.pushButton_newWindow = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_newWindow.setGeometry(QtCore.QRect(40, 450, 191, 41))
        self.pushButton_newWindow.setObjectName("pushButton_newWindow")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 500, 701, 241))
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_testA = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_testA.setGeometry(QtCore.QRect(270, 450, 191, 41))
        self.pushButton_testA.setObjectName("pushButton_testA")
        self.pushButton_testB = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_testB.setGeometry(QtCore.QRect(520, 450, 191, 41))
        self.pushButton_testB.setObjectName("pushButton_testB")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.groupBox_dynamicIO.setTitle(QtWidgets.QApplication.translate("MainWindow", "Dynamic IO", None, -1))
        self.checkBox_5.setText(QtWidgets.QApplication.translate("MainWindow", "fluid Cache", None, -1))
        self.checkBox_6.setText(QtWidgets.QApplication.translate("MainWindow", "particle Cache", None, -1))
        self.checkBox_7.setText(QtWidgets.QApplication.translate("MainWindow", "Alembic", None, -1))
        self.groupBox_LookIO.setTitle(QtWidgets.QApplication.translate("MainWindow", "Look IO", None, -1))
        self.checkBox.setText(QtWidgets.QApplication.translate("MainWindow", "texture", None, -1))
        self.checkBox_8.setText(QtWidgets.QApplication.translate("MainWindow", "Shading", None, -1))
        self.groupBox_proxy_IO.setTitle(QtWidgets.QApplication.translate("MainWindow", "Proxy IO", None, -1))
        self.checkBox_3.setText(QtWidgets.QApplication.translate("MainWindow", "GPUCache", None, -1))
        self.checkBox_2.setText(QtWidgets.QApplication.translate("MainWindow", "RibArchive", None, -1))
        self.checkBox_4.setText(QtWidgets.QApplication.translate("MainWindow", "Alembic", None, -1))
        self.groupBox_lightIO.setTitle(QtWidgets.QApplication.translate("MainWindow", "Light IO", None, -1))
        self.checkBox_9.setText(QtWidgets.QApplication.translate("MainWindow", "Env Light", None, -1))
        self.checkBox_10.setText(QtWidgets.QApplication.translate("MainWindow", "Direct Light", None, -1))
        self.checkBox_13.setText(QtWidgets.QApplication.translate("MainWindow", "Mesh Light", None, -1))
        self.groupBox_renderIO.setTitle(QtWidgets.QApplication.translate("MainWindow", "Render IO", None, -1))
        self.checkBox_renderCam.setText(QtWidgets.QApplication.translate("MainWindow", "Render Cam", None, -1))
        self.checkBox_renderSet.setText(QtWidgets.QApplication.translate("MainWindow", "Render Setting", None, -1))
        self.treeWidget.headerItem().setText(0, QtWidgets.QApplication.translate("MainWindow", "items", None, -1))
        self.treeWidget.headerItem().setText(1, QtWidgets.QApplication.translate("MainWindow", "location", None, -1))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "PrmanTextures", None, -1))
        self.treeWidget.topLevelItem(0).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "file", None, -1))
        self.treeWidget.topLevelItem(0).child(0).setText(1, QtWidgets.QApplication.translate("MainWindow", "c:\\temp", None, -1))
        self.treeWidget.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "mayaTextures", None, -1))
        self.treeWidget.topLevelItem(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "gpuCaches", None, -1))
        self.treeWidget.topLevelItem(3).setText(0, QtWidgets.QApplication.translate("MainWindow", "RibArhives", None, -1))
        self.treeWidget.topLevelItem(4).setText(0, QtWidgets.QApplication.translate("MainWindow", "alembics", None, -1))
        self.treeWidget.topLevelItem(5).setText(0, QtWidgets.QApplication.translate("MainWindow", "cameras", None, -1))
        self.treeWidget.topLevelItem(6).setText(0, QtWidgets.QApplication.translate("MainWindow", "PrmanLights", None, -1))
        self.treeWidget.topLevelItem(7).setText(0, QtWidgets.QApplication.translate("MainWindow", "mayaLights", None, -1))
        self.treeWidget.topLevelItem(8).setText(0, QtWidgets.QApplication.translate("MainWindow", "fluidCaches", None, -1))
        self.treeWidget.topLevelItem(9).setText(0, QtWidgets.QApplication.translate("MainWindow", "particleCaches", None, -1))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_newWindow.setText(QtWidgets.QApplication.translate("MainWindow", "new window", None, -1))
        self.lineEdit.setText(QtWidgets.QApplication.translate("MainWindow", "# total polygons", None, -1))
        self.pushButton_testA.setText(QtWidgets.QApplication.translate("MainWindow", "testA", None, -1))
        self.pushButton_testB.setText(QtWidgets.QApplication.translate("MainWindow", "testB", None, -1))




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


 