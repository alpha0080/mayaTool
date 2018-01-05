# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/alphaOnly/github/pipelineTool/UI_code/addTable.ui'
#
# Created: Thu Dec 28 17:53:43 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 50, 256, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)

        self.tableWidget.verticalHeaderItem(0).setText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.tableWidget.verticalHeaderItem(1).setText(QtWidgets.QApplication.translate("MainWindow", "2", None, -1))
        self.tableWidget.verticalHeaderItem(2).setText(QtWidgets.QApplication.translate("MainWindow", "3", None, -1))
        self.tableWidget.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("MainWindow", "a", None, -1))
        self.tableWidget.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("MainWindow", "b", None, -1))
        self.tableWidget.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("MainWindow", "c", None, -1))




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


 