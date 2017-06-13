# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha.DESKTOP-1S1STEK/Documents/GitHub/mayaTool/arnoldBatchCmd/arnoldCmdToolUI.ui'
#
# Created: Tue Jun 06 09:15:27 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import maya.cmds as cmds
import pymel.core as pm
import sys
import os
import json
import datetime
import subprocess  


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 494)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 40, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 70, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_frameStart = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_frameStart.setGeometry(QtCore.QRect(330, 40, 81, 21))
        self.lineEdit_frameStart.setObjectName("lineEdit_frameStart")
        self.lineEdit_frameEnd = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_frameEnd.setGeometry(QtCore.QRect(330, 70, 81, 21))
        self.lineEdit_frameEnd.setObjectName("lineEdit_frameEnd")
        self.pushButton_setProject = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_setProject.setGeometry(QtCore.QRect(30, 110, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.pushButton_setProject.setFont(font)
        self.pushButton_setProject.setObjectName("pushButton_setProject")
        self.lineEdit_Project = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Project.setGeometry(QtCore.QRect(130, 110, 281, 31))
        self.lineEdit_Project.setObjectName("lineEdit_Project")
        self.lineEdit_file = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_file.setGeometry(QtCore.QRect(130, 160, 281, 31))
        self.lineEdit_file.setObjectName("lineEdit_file")
        self.pushButton_setFile = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_setFile.setGeometry(QtCore.QRect(30, 160, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.pushButton_setFile.setFont(font)
        self.pushButton_setFile.setObjectName("pushButton_setFile")
        self.pushButton_submitDeadLine = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_submitDeadLine.setGeometry(QtCore.QRect(30, 410, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.pushButton_submitDeadLine.setFont(font)
        self.pushButton_submitDeadLine.setObjectName("pushButton_submitDeadLine")
        self.pushButton_genRenderJob = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_genRenderJob.setGeometry(QtCore.QRect(230, 410, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.pushButton_genRenderJob.setFont(font)
        self.pushButton_genRenderJob.setObjectName("pushButton_genRenderJob")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 330, 111, 20))
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 290, 111, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit_deadLineJobpriority = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_deadLineJobpriority.setGeometry(QtCore.QRect(170, 330, 51, 20))
        self.lineEdit_deadLineJobpriority.setObjectName("lineEdit_deadLineJobpriority")
        self.comboBox_deadPool = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_deadPool.setGeometry(QtCore.QRect(170, 290, 191, 25))
        self.comboBox_deadPool.setObjectName("comboBox_deadPool")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 370, 111, 20))
        self.label_6.setObjectName("label_6")
        self.lineEdit_deadLineJobName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_deadLineJobName.setGeometry(QtCore.QRect(170, 370, 191, 20))
        self.lineEdit_deadLineJobName.setObjectName("lineEdit_deadLineJobName")
        self.pushButton_setOutPutFolder = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_setOutPutFolder.setGeometry(QtCore.QRect(30, 210, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.pushButton_setOutPutFolder.setFont(font)
        self.pushButton_setOutPutFolder.setObjectName("pushButton_setOutPutFolder")
        self.lineEdit_pushButton_setOutPutFolder = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pushButton_setOutPutFolder.setGeometry(QtCore.QRect(130, 210, 281, 31))
        self.lineEdit_pushButton_setOutPutFolder.setObjectName("lineEdit_pushButton_setOutPutFolder")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "arnoldRender CMD tool ", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Start Frame:", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "End Frame:", None, -1))
        self.pushButton_setProject.setText(QtWidgets.QApplication.translate("MainWindow", "set Project", None, -1))
        self.pushButton_setFile.setText(QtWidgets.QApplication.translate("MainWindow", "set File", None, -1))
        self.pushButton_submitDeadLine.setText(QtWidgets.QApplication.translate("MainWindow", "submit to Deadline", None, -1))
        self.pushButton_genRenderJob.setText(QtWidgets.QApplication.translate("MainWindow", "create bat", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("MainWindow", "select Job Priority", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "select DeadLine Pool", None, -1))
        self.lineEdit_deadLineJobpriority.setText(QtWidgets.QApplication.translate("MainWindow", "50", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "DeadLine Job Name:", None, -1))
        self.pushButton_setOutPutFolder.setText(QtWidgets.QApplication.translate("MainWindow", "outPut", None, -1))



        
        
        
        self.deadLineRoot = pm.mel.eval("getenv DEADLINE_PATH")+"/deadlinecommand.exe"
        output = subprocess.Popen(["%s"%self.deadLineRoot,"Pools"], stdout=subprocess.PIPE, shell=True).communicate()[0]  #cmd run deadlineCommand -Pools,that get pools from deadline Repo
        poolList = output.split("\r\n")
        poolCount = len(poolList)
        for addNum in range(0,poolCount):
            self.comboBox_deadPool.addItem("")
            comboBoxItemName = poolList[addNum]
            self.comboBox_deadPool.setItemText(addNum, QtWidgets.QApplication.translate("MainWindow",comboBoxItemName, None, -1))







class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #self.QTITEM.ACTION.connect(self.MODDEF)
        self.setupUi(self)
    #def self.MODDEF(self):

        #push button
        self.pushButton_setProject.clicked.connect(self.setProject)
        
        self.pushButton_setFile.clicked.connect(self.setFilePath)
        
        self.pushButton_setOutPutFolder.clicked.connect(self.setOutPutFolder)

                
        self.lineEdit_frameStart.textChanged.connect(self.modlineEdit_frameStart)
        self.lineEdit_frameEnd.textChanged.connect(self.modlineEdit_frameEnd)

        self.pushButton_submitDeadLine.clicked.connect(self.submitToDeadline)
        self.pushButton_genRenderJob.clicked.connect(self.createRenderBatchCmdFile)
        self.lineEdit_deadLineJobpriority.textChanged.connect(self.modlineEdit_deadLineJobpriority)

        self.lineEdit_deadLineJobName.textChanged.connect(self.modlineEdit_deadLineJobName)


    def modlineEdit_deadLineJobpriority(self):
        self.deadLineJobpriority =self.lineEdit_deadLineJobpriority.text () 
        self.lineEdit_deadLineJobpriority.setText(self.deadLineJobpriority) 
        print   self.deadLineJobpriority
 
 
    def modlineEdit_deadLineJobName(self):
        self.deadLineJobName =self.lineEdit_deadLineJobName.text () 
        self.lineEdit_deadLineJobName.setText(self.deadLineJobName) 
        print  self.deadLineJobName
    
                
    def setOutPutFolder(self):
        self.outPutPath = cmds.fileDialog2(fm=3)[0]
       # print projectPath[0]
        self.lineEdit_pushButton_setOutPutFolder.setText(self.outPutPath)
        
    def setProject(self):
        self.projectPath = cmds.fileDialog2(fm=3)[0]
       # print projectPath[0]
        self.lineEdit_Project.setText(self.projectPath)
        
    def setFilePath(self):
        self.fileNamePath = cmds.fileDialog2(fm=1)[0]
        
        #print projectPath[0]
        self.lineEdit_file.setText(self.fileNamePath)
        
        
        
        
    def modlineEdit_frameStart(self):
        self.frameStart = int( self.lineEdit_frameStart.text () )
        print self.frameStart
    
    
    def modlineEdit_frameEnd(self):
        self.frameEnd = int( self.lineEdit_frameEnd.text () )
        print self.frameEnd
    
    
    def getFileForder(self):
        
        try:
            os.mkdir('c:/temp')
        except:
            pass
            
        try:
            os.mkdir('c:/temp/renderCmd/')
        except:
            pass
    

        dt = datetime.datetime.now()
        newFormatDt = dt.strftime("%m%d%H%M%S")           #("%Y%m%d%H%M%S")  that add year   
        self.cmdFileLocation = 'c:/temp/renderCmd/'+ newFormatDt
        print self.cmdFileLocation
        try:
            os.mkdir(self.cmdFileLocation)
        except:
            pass
        
       # commandsFileName = 'c:/temp/arnold/commandsfile.txt'
   # jobFileName =  'c:/temp/arnold/jobInfo.job'
  #  plugFileName = 'c:/temp/arnold/pluginInfo.job'

    def createCommandsFile(self):
        print 'createCommandsFile start'
        fileName =  self.cmdFileLocation + '/' + 'commandsfile.txt'
        f=open(fileName,'w')
        for i in range(self.frameStart,(self.frameEnd+1)):
            batFileNameOnly = self.cmdFileLocation +'/'+'arnoldRenderBatch.'+ '%04d'%i + '.bat'
            #print batFileNameOnly    
            f.write(batFileNameOnly + '\n')
        f.close
        


        
        
        
    def createJobInfoFile(self):
        GetCurrentUserFromDeadLine = subprocess.Popen(["%s"%self.deadLineRoot,"GetCurrentUserName"], stdout=subprocess.PIPE, shell=True).communicate()[0]  #cmd run deadlineCommand -Pools,that get pools from deadline Repo
        user = GetCurrentUserFromDeadLine.split("\r\n")[0]
        poolSelect = self.comboBox_deadPool.currentText() 
        self.deadLineJobpriority = self.lineEdit_deadLineJobpriority.text()

        print 'createJobInfoFile start'
        jobinfo = ["Name="+"%s"%self.deadLineJobName,"UserName="+"%s"%user,"Frames="+"%s"%self.frameStart+"-"+"%s"%self.frameEnd,"Pool="+"%s"%poolSelect,"Priority="+"%s"%self.deadLineJobpriority,"Plugin=CommandScript","OutputDirectory0="+"%s"%self.outPutPath]
       # Name=C03_scenes_AO_sirius_tsai
       # UserName=render
       # Frames=250-350
        #Pool=arnold
       # Priority=65
       # Plugin=MayaBatch newDeadLineJobpriority
       # OutputDirectory0=\\mcd-server\art_3d_project\supercar_pk_3\shot\shot03\comp\images\masterLayer\beauty

        fileName =  self.cmdFileLocation + '/' + 'jobInfo.job'
        print jobinfo
       # f=open(fileName,'w')
        #f.write('%s'%jobinfo[lineNum]+'\n')
        #f.close
        jobinfoCount= int(len(jobinfo))
        for lineNum in range(0,jobinfoCount):             # export all render info to deadline commandsFile.txt  
                
            f = open(fileName,'a')
            print jobinfo[lineNum]
            f.write('%s'%jobinfo[lineNum]+'\n')
            f.close

        
    def createPluginInfoFile(self):
        print 'createPluginInfoFile start'
        fileName =  self.cmdFileLocation + '/' + 'pluginInfo.job'
        f=open(fileName,'w')
        f.write('Renderer=arnold'+ '\n' )
        f.close
        
        
    def createSubmitCommand(self):
        print 'createSubmitCommand start'
        fileName =  self.cmdFileLocation + '/' + 'sendToDeadLine.bat'
        jobInfoFileName =  self.cmdFileLocation + '/' + 'jobInfo.job'
        pluginInfoFileName = self.cmdFileLocation + '/' + 'pluginInfo.job'
        commandsfileName = self.cmdFileLocation + '/' + 'commandsfile.txt'
        
 
        f=open(fileName,'w')
        f.write("deadlinecommand.exe "+"%s "%jobInfoFileName+"%s "%pluginInfoFileName+"%s "%commandsfileName)
        f.close
        
        
    def createRenderBatchCmdFile(self):
        for i in range(self.frameStart,(self.frameEnd+1)):
            batFileName = self.cmdFileLocation +'/' + 'arnoldRenderBatch.'+ '%04d'%i + '.bat'
            cmd = "C:/Program Files/Autodesk/Maya2016.5/bin/Render.exe"
           # print batFileName
            f = open(batFileName,'w')
            data = '\"' + cmd + '\"' +' -s ' + str(i) + ' -e ' + str(i) +' '+ '\"' +self.fileNamePath + '\"'# +' -s ' + str(i) + ' -e ' + str(i) +' ' + '\"' +fileName + '\"'
            print cmd
            print data
            f.write(data)
            

            f.close

            

    def submitToDeadline(self):
        self.getFileForder()
        self.createRenderBatchCmdFile()
        self.createCommandsFile()
        self.createJobInfoFile()
        self.createPluginInfoFile()
        self.createSubmitCommand()
        
        
        
        
        
                        
        

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


 