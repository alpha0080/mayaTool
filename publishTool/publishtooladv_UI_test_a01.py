# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/alphaOnly/github/mayaTool/publishTool/publishtooladv_07_1.ui'
#
# Created: Wed Oct 18 15:53:16 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

import pablishToolUI01


#Ui_MainWindow.setupUi


class mod_MainWindow(QtWidgets.QMainWindow, pablishToolUI01.Ui_MainWindow):  
    def __init__(self):
        super(mod_MainWindow, self).__init__(self)
       # print 'sdsd'
       # self.ui = Ui_MainWindow()
     #   self.setupUi(self)
        



def main():
    global ui
   # ui = Ui_MainWindow()
    print ui
    app = QtWidgets.QApplication.instance()
    if app == None: app = QtWidgets.QApplication(sys.argv)
    try:
        self.ui.close()
        self.ui.deleteLater()
    except: pass
    ui = mod_MainWindow()
    ui.show()
 
if __name__ == '__main__':
    main()

