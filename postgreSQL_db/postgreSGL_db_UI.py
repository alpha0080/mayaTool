# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/alphaOnly/github/mayaTool/postgreSQL_db/postgreSGL_db_UI.ui'
#
# Created: Fri Dec 08 16:36:18 2017
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
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(350, 20, 411, 114))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.createProjectDB_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.createProjectDB_pushButton.setObjectName("createProjectDB_pushButton")
        self.verticalLayout_5.addWidget(self.createProjectDB_pushButton)
        self.createAssetDB_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.createAssetDB_pushButton.setObjectName("createAssetDB_pushButton")
        self.verticalLayout_5.addWidget(self.createAssetDB_pushButton)
        self.createShotDB_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.createShotDB_pushButton.setObjectName("createShotDB_pushButton")
        self.verticalLayout_5.addWidget(self.createShotDB_pushButton)
        self.createUserDB_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.createUserDB_pushButton.setObjectName("createUserDB_pushButton")
        self.verticalLayout_5.addWidget(self.createUserDB_pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.projectDBName_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.projectDBName_label.setAlignment(QtCore.Qt.AlignCenter)
        self.projectDBName_label.setObjectName("projectDBName_label")
        self.verticalLayout_3.addWidget(self.projectDBName_label)
        self.assetDBName_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.assetDBName_label.setAlignment(QtCore.Qt.AlignCenter)
        self.assetDBName_label.setObjectName("assetDBName_label")
        self.verticalLayout_3.addWidget(self.assetDBName_label)
        self.shotDBName_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.shotDBName_label.setAlignment(QtCore.Qt.AlignCenter)
        self.shotDBName_label.setObjectName("shotDBName_label")
        self.verticalLayout_3.addWidget(self.shotDBName_label)
        self.user_DBName_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.user_DBName_label.setAlignment(QtCore.Qt.AlignCenter)
        self.user_DBName_label.setObjectName("user_DBName_label")
        self.verticalLayout_3.addWidget(self.user_DBName_label)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.projectDBName_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.projectDBName_lineEdit.setEnabled(False)
        self.projectDBName_lineEdit.setObjectName("projectDBName_lineEdit")
        self.verticalLayout_4.addWidget(self.projectDBName_lineEdit)
        self.assetDBName_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.assetDBName_lineEdit.setEnabled(False)
        self.assetDBName_lineEdit.setObjectName("assetDBName_lineEdit")
        self.verticalLayout_4.addWidget(self.assetDBName_lineEdit)
        self.shotDB_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.shotDB_lineEdit.setEnabled(False)
        self.shotDB_lineEdit.setObjectName("shotDB_lineEdit")
        self.verticalLayout_4.addWidget(self.shotDB_lineEdit)
        self.userDB_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.userDB_lineEdit.setEnabled(False)
        self.userDB_lineEdit.setObjectName("userDB_lineEdit")
        self.verticalLayout_4.addWidget(self.userDB_lineEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.projectDBCount_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.projectDBCount_label.setAlignment(QtCore.Qt.AlignCenter)
        self.projectDBCount_label.setObjectName("projectDBCount_label")
        self.verticalLayout_2.addWidget(self.projectDBCount_label)
        self.assetDBCount_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.assetDBCount_label.setAlignment(QtCore.Qt.AlignCenter)
        self.assetDBCount_label.setObjectName("assetDBCount_label")
        self.verticalLayout_2.addWidget(self.assetDBCount_label)
        self.shotDBCount_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.shotDBCount_label.setAlignment(QtCore.Qt.AlignCenter)
        self.shotDBCount_label.setObjectName("shotDBCount_label")
        self.verticalLayout_2.addWidget(self.shotDBCount_label)
        self.userDBCount_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.userDBCount_label.setAlignment(QtCore.Qt.AlignCenter)
        self.userDBCount_label.setObjectName("userDBCount_label")
        self.verticalLayout_2.addWidget(self.userDBCount_label)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.update_AssetDB_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.update_AssetDB_pushButton.setGeometry(QtCore.QRect(340, 270, 111, 23))
        self.update_AssetDB_pushButton.setObjectName("update_AssetDB_pushButton")
        self.testA_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.testA_pushButton.setGeometry(QtCore.QRect(340, 160, 111, 23))
        self.testA_pushButton.setObjectName("testA_pushButton")
        self.testB_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.testB_pushButton.setGeometry(QtCore.QRect(470, 160, 111, 23))
        self.testB_pushButton.setObjectName("testB_pushButton")
        self.testC_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.testC_pushButton.setGeometry(QtCore.QRect(610, 160, 111, 23))
        self.testC_pushButton.setObjectName("testC_pushButton")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(20, 30, 281, 231))
        self.treeWidget.setObjectName("treeWidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 300, 281, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.info_plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.info_plainTextEdit.setGeometry(QtCore.QRect(340, 300, 441, 251))
        self.info_plainTextEdit.setObjectName("info_plainTextEdit")
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
        self.createProjectDB_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "create project DB", None, -1))
        self.createAssetDB_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "create asset DB", None, -1))
        self.createShotDB_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "create shot DB", None, -1))
        self.createUserDB_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "create user DB", None, -1))
        self.projectDBName_label.setText(QtWidgets.QApplication.translate("MainWindow", "projects DB:", None, -1))
        self.assetDBName_label.setText(QtWidgets.QApplication.translate("MainWindow", "assets DB:", None, -1))
        self.shotDBName_label.setText(QtWidgets.QApplication.translate("MainWindow", "shots DB:", None, -1))
        self.user_DBName_label.setText(QtWidgets.QApplication.translate("MainWindow", "users DB:", None, -1))
        self.projectDBName_lineEdit.setText(QtWidgets.QApplication.translate("MainWindow", "projsDB", None, -1))
        self.assetDBName_lineEdit.setText(QtWidgets.QApplication.translate("MainWindow", "assetsDB", None, -1))
        self.shotDB_lineEdit.setText(QtWidgets.QApplication.translate("MainWindow", "shotsDB", None, -1))
        self.userDB_lineEdit.setText(QtWidgets.QApplication.translate("MainWindow", "usersDB", None, -1))
        self.projectDBCount_label.setText(QtWidgets.QApplication.translate("MainWindow", "projsCountNum", None, -1))
        self.assetDBCount_label.setText(QtWidgets.QApplication.translate("MainWindow", "assetsCountNum", None, -1))
        self.shotDBCount_label.setText(QtWidgets.QApplication.translate("MainWindow", "shotsCountNum", None, -1))
        self.userDBCount_label.setText(QtWidgets.QApplication.translate("MainWindow", "usersCountNum", None, -1))
        self.update_AssetDB_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "update assets DB", None, -1))
        self.testA_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "test_A", None, -1))
        self.testB_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "test_B", None, -1))
        self.testC_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "test_C", None, -1))
        self.treeWidget.headerItem().setText(0, QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.treeWidget.headerItem().setText(1, QtWidgets.QApplication.translate("MainWindow", "2", None, -1))
        self.treeWidget.headerItem().setText(2, QtWidgets.QApplication.translate("MainWindow", "3", None, -1))
        self.treeWidget.headerItem().setText(3, QtWidgets.QApplication.translate("MainWindow", "4", None, -1))
        self.treeWidget.headerItem().setText(4, QtWidgets.QApplication.translate("MainWindow", "5", None, -1))
        self.tableWidget.verticalHeaderItem(0).setText(QtWidgets.QApplication.translate("MainWindow", "a", None, -1))
        self.tableWidget.verticalHeaderItem(1).setText(QtWidgets.QApplication.translate("MainWindow", "b", None, -1))
        self.tableWidget.verticalHeaderItem(2).setText(QtWidgets.QApplication.translate("MainWindow", "c", None, -1))
        self.tableWidget.verticalHeaderItem(3).setText(QtWidgets.QApplication.translate("MainWindow", "d", None, -1))
        self.tableWidget.verticalHeaderItem(4).setText(QtWidgets.QApplication.translate("MainWindow", "e", None, -1))
        self.tableWidget.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.tableWidget.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("MainWindow", "2", None, -1))
        self.tableWidget.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("MainWindow", "3", None, -1))
        self.tableWidget.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("MainWindow", "4", None, -1))
        self.tableWidget.horizontalHeaderItem(4).setText(QtWidgets.QApplication.translate("MainWindow", "5", None, -1))




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


 