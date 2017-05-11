# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha.DESKTOP-1S1STEK/Documents/GitHub/mayaTool/renderman/rendermanGeoSet/rendermanGeoSet_UI_A01.ui'
#
# Created: Wed May 10 13:52:24 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 475)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_attach = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_attach.setGeometry(QtCore.QRect(180, 70, 91, 23))
        self.pushButton_attach.setObjectName("pushButton_attach")
        self.pushButton_detach = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_detach.setGeometry(QtCore.QRect(180, 110, 91, 23))
        self.pushButton_detach.setObjectName("pushButton_detach")
        self.pushButton_select = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_select.setGeometry(QtCore.QRect(180, 150, 91, 23))
        self.pushButton_select.setObjectName("pushButton_select")
        self.listWidget_gemSetting = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_gemSetting.setGeometry(QtCore.QRect(10, 30, 161, 421))
        self.listWidget_gemSetting.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.listWidget_gemSetting.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget_gemSetting.setObjectName("listWidget_gemSetting")
        QtWidgets.QListWidgetItem(self.listWidget_gemSetting)
        QtWidgets.QListWidgetItem(self.listWidget_gemSetting)
        self.pushButton_create = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create.setGeometry(QtCore.QRect(180, 30, 91, 23))
        self.pushButton_create.setObjectName("pushButton_create")
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(180, 230, 91, 23))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.listWidget_optionalAttr = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_optionalAttr.setGeometry(QtCore.QRect(470, 30, 171, 221))
        self.listWidget_optionalAttr.setObjectName("listWidget_optionalAttr")
        QtWidgets.QListWidgetItem(self.listWidget_optionalAttr)
        QtWidgets.QListWidgetItem(self.listWidget_optionalAttr)
        QtWidgets.QListWidgetItem(self.listWidget_optionalAttr)
        QtWidgets.QListWidgetItem(self.listWidget_optionalAttr)
        QtWidgets.QListWidgetItem(self.listWidget_optionalAttr)
        QtWidgets.QListWidgetItem(self.listWidget_optionalAttr)
        QtWidgets.QListWidgetItem(self.listWidget_optionalAttr)
        QtWidgets.QListWidgetItem(self.listWidget_optionalAttr)
        QtWidgets.QListWidgetItem(self.listWidget_optionalAttr)
        self.listWidget_addedAttr = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_addedAttr.setGeometry(QtCore.QRect(680, 30, 171, 221))
        self.listWidget_addedAttr.setObjectName("listWidget_addedAttr")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(650, 100, 21, 23))
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_remove = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_remove.setGeometry(QtCore.QRect(650, 130, 21, 23))
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.tabWidget_setting = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_setting.setGeometry(QtCore.QRect(470, 260, 381, 191))
        self.tabWidget_setting.setObjectName("tabWidget_setting")
        self.tab_setting = QtWidgets.QWidget()
        self.tab_setting.setObjectName("tab_setting")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_setting)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 361, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget_setting.addTab(self.tab_setting, "")
        self.pushButton_rename = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_rename.setGeometry(QtCore.QRect(180, 300, 91, 23))
        self.pushButton_rename.setObjectName("pushButton_rename")
        self.lineEdit_newName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_newName.setGeometry(QtCore.QRect(180, 340, 91, 20))
        self.lineEdit_newName.setObjectName("lineEdit_newName")
        self.listWidget_geoSelected = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_geoSelected.setGeometry(QtCore.QRect(280, 30, 171, 421))
        self.listWidget_geoSelected.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.listWidget_geoSelected.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget_geoSelected.setObjectName("listWidget_geoSelected")
        QtWidgets.QListWidgetItem(self.listWidget_geoSelected)
        QtWidgets.QListWidgetItem(self.listWidget_geoSelected)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget_setting.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Renderman Geo Set", None, -1))
        self.pushButton_attach.setText(QtWidgets.QApplication.translate("MainWindow", "attach", None, -1))
        self.pushButton_detach.setText(QtWidgets.QApplication.translate("MainWindow", "detach", None, -1))
        self.pushButton_select.setText(QtWidgets.QApplication.translate("MainWindow", "select", None, -1))
        self.listWidget_gemSetting.setSortingEnabled(True)
        __sortingEnabled = self.listWidget_gemSetting.isSortingEnabled()
        self.listWidget_gemSetting.setSortingEnabled(False)
        self.listWidget_gemSetting.item(0).setText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.listWidget_gemSetting.item(1).setText(QtWidgets.QApplication.translate("MainWindow", "2", None, -1))
        self.listWidget_gemSetting.setSortingEnabled(__sortingEnabled)
        self.pushButton_create.setText(QtWidgets.QApplication.translate("MainWindow", "create", None, -1))
        self.pushButton_delete.setText(QtWidgets.QApplication.translate("MainWindow", "delete", None, -1))
        __sortingEnabled = self.listWidget_optionalAttr.isSortingEnabled()
        self.listWidget_optionalAttr.setSortingEnabled(False)
        self.listWidget_optionalAttr.item(0).setText(QtWidgets.QApplication.translate("MainWindow", "Subdiv Facevarying Interp", None, -1))
        self.listWidget_optionalAttr.item(1).setText(QtWidgets.QApplication.translate("MainWindow", "Subdiv Interp", None, -1))
        self.listWidget_optionalAttr.item(2).setText(QtWidgets.QApplication.translate("MainWindow", "Subdiv Scheme", None, -1))
        self.listWidget_optionalAttr.item(3).setText(QtWidgets.QApplication.translate("MainWindow", "Matte Object", None, -1))
        self.listWidget_optionalAttr.item(4).setText(QtWidgets.QApplication.translate("MainWindow", "Micropolygon Length", None, -1))
        self.listWidget_optionalAttr.item(5).setText(QtWidgets.QApplication.translate("MainWindow", "Hold Out", None, -1))
        self.listWidget_optionalAttr.item(6).setText(QtWidgets.QApplication.translate("MainWindow", "Camera Visibility", None, -1))
        self.listWidget_optionalAttr.item(7).setText(QtWidgets.QApplication.translate("MainWindow", "Indirect Visibility", None, -1))
        self.listWidget_optionalAttr.item(8).setText(QtWidgets.QApplication.translate("MainWindow", "Transmission Visibility", None, -1))
        self.listWidget_optionalAttr.setSortingEnabled(__sortingEnabled)
        self.pushButton_add.setText(QtWidgets.QApplication.translate("MainWindow", ">", None, -1))
        self.pushButton_remove.setText(QtWidgets.QApplication.translate("MainWindow", "<", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.tabWidget_setting.setTabText(self.tabWidget_setting.indexOf(self.tab_setting), QtWidgets.QApplication.translate("MainWindow", "setting", None, -1))
        self.pushButton_rename.setText(QtWidgets.QApplication.translate("MainWindow", "rename", None, -1))
        self.listWidget_geoSelected.setSortingEnabled(True)
        __sortingEnabled = self.listWidget_geoSelected.isSortingEnabled()
        self.listWidget_geoSelected.setSortingEnabled(False)
        self.listWidget_geoSelected.item(0).setText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.listWidget_geoSelected.item(1).setText(QtWidgets.QApplication.translate("MainWindow", "2", None, -1))
        self.listWidget_geoSelected.setSortingEnabled(__sortingEnabled)




class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #self.QTITEM.ACTION.connect(self.MODDEF)
        self.setupUi(self)
    #def self.MODDEF(self):
    
    
    
        #button click
        self.pushButton_create.clicked.connect(self.click_button_Create)
        
        
        
        
        
        
        
        
        
#-----------------------------call module-------------------------        
    def click_button_Create(self):
        print "click button Create"
        
        



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


 