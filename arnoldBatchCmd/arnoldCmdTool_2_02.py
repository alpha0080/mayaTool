# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha.DESKTOP-1S1STEK/Documents/GitHub/mayaTool/arnoldBatchCmd/arnoldCmdToolUI.ui'
#
# Created: Thu Jun 08 13:35:44 2017
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

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
        MainWindow.resize(506, 839)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-50, 30, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-50, 60, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_frameStart = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_frameStart.setGeometry(QtCore.QRect(130, 30, 81, 21))
        self.lineEdit_frameStart.setObjectName("lineEdit_frameStart")
        self.lineEdit_frameEnd = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_frameEnd.setGeometry(QtCore.QRect(130, 60, 81, 21))
        self.lineEdit_frameEnd.setObjectName("lineEdit_frameEnd")
        self.pushButton_setProject = QtGui.QPushButton(self.centralwidget)
        self.pushButton_setProject.setGeometry(QtCore.QRect(30, 180, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.pushButton_setProject.setFont(font)
        self.pushButton_setProject.setObjectName("pushButton_setProject")
        self.lineEdit_Project = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_Project.setGeometry(QtCore.QRect(200, 180, 281, 31))
        self.lineEdit_Project.setObjectName("lineEdit_Project")
        self.lineEdit_assFile = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_assFile.setGeometry(QtCore.QRect(200, 300, 281, 31))
        self.lineEdit_assFile.setObjectName("lineEdit_assFile")
        self.pushButton_setAssFile = QtGui.QPushButton(self.centralwidget)
        self.pushButton_setAssFile.setGeometry(QtCore.QRect(30, 300, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.pushButton_setAssFile.setFont(font)
        self.pushButton_setAssFile.setObjectName("pushButton_setAssFile")
        self.pushButton_submitDeadLine = QtGui.QPushButton(self.centralwidget)
        self.pushButton_submitDeadLine.setGeometry(QtCore.QRect(40, 780, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.pushButton_submitDeadLine.setFont(font)
        self.pushButton_submitDeadLine.setObjectName("pushButton_submitDeadLine")
        self.pushButton_convertToAss = QtGui.QPushButton(self.centralwidget)
        self.pushButton_convertToAss.setGeometry(QtCore.QRect(30, 430, 451, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.pushButton_convertToAss.setFont(font)
        self.pushButton_convertToAss.setObjectName("pushButton_convertToAss")
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 740, 111, 20))
        self.label_7.setObjectName("label_7")
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 700, 111, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit_deadLineJobpriority = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_deadLineJobpriority.setGeometry(QtCore.QRect(190, 740, 51, 20))
        self.lineEdit_deadLineJobpriority.setObjectName("lineEdit_deadLineJobpriority")
        self.comboBox_deadPool = QtGui.QComboBox(self.centralwidget)
        self.comboBox_deadPool.setGeometry(QtCore.QRect(190, 700, 191, 25))
        self.comboBox_deadPool.setObjectName("comboBox_deadPool")
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 130, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_deadLineJobName = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_deadLineJobName.setGeometry(QtCore.QRect(200, 119, 281, 31))
        self.lineEdit_deadLineJobName.setObjectName("lineEdit_deadLineJobName")
        self.pushButton_setAssOutPutFolder = QtGui.QPushButton(self.centralwidget)
        self.pushButton_setAssOutPutFolder.setGeometry(QtCore.QRect(30, 240, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.pushButton_setAssOutPutFolder.setFont(font)
        self.pushButton_setAssOutPutFolder.setObjectName("pushButton_setAssOutPutFolder")
        self.lineEdit_pushButton_setAssOutPutFolder = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_pushButton_setAssOutPutFolder.setGeometry(QtCore.QRect(200, 240, 281, 31))
        self.lineEdit_pushButton_setAssOutPutFolder.setObjectName("lineEdit_pushButton_setAssOutPutFolder")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 160, 221, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 280, 221, 16))
        self.label_4.setObjectName("label_4")
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(200, 220, 221, 16))
        self.label_8.setObjectName("label_8")
        self.lineEdit_pushButton_setImageOutputFolder = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_pushButton_setImageOutputFolder.setGeometry(QtCore.QRect(200, 370, 281, 31))
        self.lineEdit_pushButton_setImageOutputFolder.setObjectName("lineEdit_pushButton_setImageOutputFolder")
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(200, 350, 221, 16))
        self.label_9.setObjectName("label_9")
        self.pushButton_setImageOutputFolder = QtGui.QPushButton(self.centralwidget)
        self.pushButton_setImageOutputFolder.setGeometry(QtCore.QRect(30, 370, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.pushButton_setImageOutputFolder.setFont(font)
        self.pushButton_setImageOutputFolder.setObjectName("pushButton_setImageOutputFolder")
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 480, 451, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(40, 510, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.lineEdit_yRes = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_yRes.setGeometry(QtCore.QRect(200, 510, 41, 21))
        self.lineEdit_yRes.setObjectName("lineEdit_yRes")
        self.lineEdit_xRes = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_xRes.setGeometry(QtCore.QRect(100, 510, 41, 21))
        self.lineEdit_xRes.setObjectName("lineEdit_xRes")
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(140, 510, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.lineEdit_gamma = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_gamma.setGeometry(QtCore.QRect(200, 570, 41, 21))
        self.lineEdit_gamma.setObjectName("lineEdit_gamma")
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(40, 570, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.checkBox_ignoreTexture = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_ignoreTexture.setEnabled(False)
        self.checkBox_ignoreTexture.setGeometry(QtCore.QRect(300, 500, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.checkBox_ignoreTexture.setFont(font)
        self.checkBox_ignoreTexture.setObjectName("checkBox_ignoreTexture")
        self.checkBox_ignoreLight = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_ignoreLight.setEnabled(False)
        self.checkBox_ignoreLight.setGeometry(QtCore.QRect(300, 530, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.checkBox_ignoreLight.setFont(font)
        self.checkBox_ignoreLight.setObjectName("checkBox_ignoreLight")
        self.checkBox_ignoreShadow = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_ignoreShadow.setEnabled(False)
        self.checkBox_ignoreShadow.setGeometry(QtCore.QRect(300, 560, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.checkBox_ignoreShadow.setFont(font)
        self.checkBox_ignoreShadow.setObjectName("checkBox_ignoreShadow")
        self.checkBox_ignoreDisplacement = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_ignoreDisplacement.setEnabled(False)
        self.checkBox_ignoreDisplacement.setGeometry(QtCore.QRect(300, 590, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.checkBox_ignoreDisplacement.setFont(font)
        self.checkBox_ignoreDisplacement.setObjectName("checkBox_ignoreDisplacement")
        self.checkBox_ignoreDisplacement_2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_ignoreDisplacement_2.setEnabled(False)
        self.checkBox_ignoreDisplacement_2.setGeometry(QtCore.QRect(300, 620, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.checkBox_ignoreDisplacement_2.setFont(font)
        self.checkBox_ignoreDisplacement_2.setObjectName("checkBox_ignoreDisplacement_2")
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(40, 600, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.lineEdit_thread = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_thread.setGeometry(QtCore.QRect(200, 600, 41, 21))
        self.lineEdit_thread.setObjectName("lineEdit_thread")
        self.lineEdit_AA = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_AA.setGeometry(QtCore.QRect(200, 540, 41, 21))
        self.lineEdit_AA.setObjectName("lineEdit_AA")
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(60, 540, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "arnoldRender CMD tool ", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Start Frame:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "End Frame:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_setProject.setText(QtGui.QApplication.translate("MainWindow", "set Project", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_setAssFile.setText(QtGui.QApplication.translate("MainWindow", "set ass File", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_submitDeadLine.setText(QtGui.QApplication.translate("MainWindow", "submit to Deadline", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_convertToAss.setText(QtGui.QApplication.translate("MainWindow", "convert To Ass", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "select Job Priority", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "select DeadLine Pool", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_deadLineJobpriority.setText(QtGui.QApplication.translate("MainWindow", "50", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "DeadLine Job Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_setAssOutPutFolder.setText(QtGui.QApplication.translate("MainWindow", "select ass folder", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "select workspace, project in progress", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "select maya file, that will be convert to .ass", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "select ass folder, that be placed ass file", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "select images , output folder", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_setImageOutputFolder.setText(QtGui.QApplication.translate("MainWindow", "select image folder", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "X Res:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Y Res:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_gamma.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "output Gamma:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_ignoreTexture.setText(QtGui.QApplication.translate("MainWindow", "Ignore texture maps", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_ignoreLight.setText(QtGui.QApplication.translate("MainWindow", "Ignore lights", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_ignoreShadow.setText(QtGui.QApplication.translate("MainWindow", "Ignore shadow", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_ignoreDisplacement.setText(QtGui.QApplication.translate("MainWindow", "Ignore displacement", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_ignoreDisplacement_2.setText(QtGui.QApplication.translate("MainWindow", "Ignore displacement", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "thread", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_thread.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "AA sample:", None, QtGui.QApplication.UnicodeUTF8))


        
        
        self.deadLineRoot = pm.mel.eval("getenv DEADLINE_PATH")+"/deadlinecommand.exe"
        output = subprocess.Popen(["%s"%self.deadLineRoot,"Pools"], stdout=subprocess.PIPE, shell=True).communicate()[0]  #cmd run deadlineCommand -Pools,that get pools from deadline Repo
        poolList = output.split("\r\n")
        poolCount = len(poolList)
        for addNum in range(0,poolCount):
            self.comboBox_deadPool.addItem("")
            comboBoxItemName = poolList[addNum]
            self.comboBox_deadPool.setItemText(addNum, QtGui.QApplication.translate("MainWindow",comboBoxItemName, None, QtGui.QApplication.UnicodeUTF8))


        self.startFrame = int(cmds.getAttr('defaultRenderGlobals.startFrame'))
        self.endFrame = int(cmds.getAttr('defaultRenderGlobals.endFrame'))

        self.lineEdit_frameStart.setText(str(self.startFrame))
        self.lineEdit_frameEnd.setText(str(self.endFrame))
        
        
        self.xRes = int(cmds.getAttr('defaultResolution.width'))
        self.yRes = int(cmds.getAttr('defaultResolution.height'))
        
        self.lineEdit_xRes.setText(str(self.xRes))
        self.lineEdit_yRes.setText(str(self.yRes))
        self.gamma = str(self.lineEdit_gamma.text())
       # self.aaSample = int(cmds.getAttr('defaultArnoldRenderOptions.AASamples'))
      #  self.lineEdit_AA.setText(str(self.aaSample))
        #self.deadLineJobName =self.lineEdit_deadLineJobName.text () 
        try:
            self.lineEdit_deadLineJobName.setText(cmds.file(q=True,sn=True).split('/')[-1].split('.')[-2])
            self.deadLineJobName = self.lineEdit_deadLineJobName.text () 
        except:
            pass
        



class mod_MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent= QtGui.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        # self.setWindowFlags(QtCore.Qt.Tool) pushButton_setAssFile lineEdit_pushButton_setAssOutPutFolder pushButton_setProject
        
        self.setupUi(self)

        #push button pushButton_setAssOutPutFolder pushButton_setImageOutputFolder
        self.pushButton_setProject.clicked.connect(self.setProject)
        
        #self.pushButton_setFile.clicked.connect(self.setFilePath)
        #self.pushButton_setFile.clicked.connect(self.setFilePath)

        self.pushButton_setImageOutputFolder.clicked.connect(self.setImageOutputFolder)
        #self.pushButton_setAssOutPutFolder.clicked.connect(self.exportAssFile)

                
        self.lineEdit_frameStart.textChanged.connect(self.modlineEdit_frameStart)
        self.lineEdit_frameEnd.textChanged.connect(self.modlineEdit_frameEnd)
        
        
        self.lineEdit_deadLineJobName.textChanged.connect(self.modlineEdit_deadLineJobName)
       # self.pushButton_submitDeadLine.clicked.connect(self.submitToDeadline)
        self.pushButton_setAssOutPutFolder.clicked.connect(self.setAssOutPutFolder)
        self.pushButton_setAssFile.clicked.connect(self.modPushButton_setAssFile)
        self.lineEdit_deadLineJobpriority.textChanged.connect(self.modlineEdit_deadLineJobpriority)

        self.lineEdit_deadLineJobName.textChanged.connect(self.modlineEdit_deadLineJobName)
        self.lineEdit_gamma.textChanged.connect(self.modlineEdit_gamma)
        
        self.pushButton_convertToAss.clicked.connect(self.exportAssFile)
        self.pushButton_submitDeadLine.clicked.connect(self.submitToDeadline)
        
        
        

    def modlineEdit_gamma(self):
        self.gamma =self.lineEdit_gamma.text () 
        self.lineEdit_gamma.setText(self.gamma) 
        print   self.gamma
 
        


        
    def modlineEdit_deadLineJobpriority(self):
        self.deadLineJobpriority =self.lineEdit_deadLineJobpriority.text () 
        self.lineEdit_deadLineJobpriority.setText(self.deadLineJobpriority) 
        print   self.deadLineJobpriority
 
 
    def modlineEdit_deadLineJobName(self):
        self.deadLineJobName =self.lineEdit_deadLineJobName.text () 
        self.lineEdit_deadLineJobName.setText(self.deadLineJobName) 
        print  self.deadLineJobName
    
    
    
    
                    
    def setAssOutPutFolder(self):
        self.outAssPutPath = cmds.fileDialog2(fm=2)[0]
       # print projectPath[0]
        self.lineEdit_pushButton_setAssOutPutFolder.setText(self.outAssPutPath)
        
        
        
                
    def setImageOutputFolder(self):
        self.ImageOutputFolder = cmds.fileDialog2(fm=2)[0]
       # print projectPath[0]
        self.lineEdit_pushButton_setImageOutputFolder.setText(self.ImageOutputFolder)
        
        
    def modPushButton_setAssFile(self):
        self.setAssFile = cmds.fileDialog2(fm=1)[0]
       # print projectPath[0]
        self.lineEdit_assFile.setText(self.setAssFile)
        
        
    def setProject(self):
        self.projectPath = cmds.fileDialog2(fm=2)[0]
       # print projectPath[0]
        self.lineEdit_Project.setText(self.projectPath)
        
        self.projectFolder = self.projectPath +'/'+ 'renderCMD'

        
        
        
    def modlineEdit_frameStart(self):
        self.frameStart = int( self.lineEdit_frameStart.text () )
        cmds.setAttr('defaultRenderGlobals.startFrame',self.frameStart)
        print self.frameStart
    
    
    def modlineEdit_frameEnd(self):
        self.endFrame = int( self.lineEdit_frameEnd.text () )
        cmds.setAttr('defaultRenderGlobals.endFrame',self.endFrame)
        print self.endFrame
    
    
    def submitToDeadline(self):
        self.getFileForder()
        print self.cmdFileLocation
        self.createRenderBatchCmdFile()
        self.createCommandsFile()
        self.createJobInfoFile()
        self.createPluginInfoFile()
        self.createSubmitCommand()
        
        
    def getFileForder(self):
         
        
        if os.path.isdir(self.projectFolder ) == True:
            pass
        else:
            os.mkdir(self.projectFolder )
            

        dt = datetime.datetime.now()
        newFormatDt = dt.strftime("%m%d%H%M%S")           #("%Y%m%d%H%M%S")  that add year   
        self.cmdFileLocation = self.projectFolder +'/'+ newFormatDt
        print self.cmdFileLocation
        try:
            os.mkdir(self.cmdFileLocation)
        except:
            pass
            
            
            
    def createRenderBatchCmdFile(self):
        tempFileName = self.setAssFile.split('/')[-1].split('.')[0]
        print tempFileName
        sourceFileName =  self.setAssFile.split('.')[0]
                

        for i in range(self.startFrame,(self.endFrame+1)):
            # kick -i teapot.ass -r 640 480 -g 2.2 -o teapot.tif
            batFileName = self.cmdFileLocation +'/' + 'arnoldRenderBatch.'+ '%04d'%i + '.bat'
            cmd = "C:/solidangle/mtoadeploy/2016.5/bin/kick.exe"
            print batFileName
            f = open(batFileName,'w')
            
            data  = '\"' + cmd + '\"' +' -g '+ self.gamma +' -i '+'\"' +sourceFileName +'.'+ '%04d'%i +'.ass' + '\"'+' -o ' + '\"' + self.ImageOutputFolder +'/'+ tempFileName +'.'+ '%04d'%i +'.exr' + '\"'
            #data = '\"' + cmd + '\"' +' -s ' + str(i) + ' -e ' + str(i) +' '+ '\"' +self.fileNamePath + '\"'# +' -s ' + str(i) + ' -e ' + str(i) +' ' + '\"' +fileName + '\"'
            print cmd
            print data
            f.write(data)
            

            f.close




            
            
            
            
        
       # commandsFileName = 'c:/temp/arnold/commandsfile.txt'
   # jobFileName =  'c:/temp/arnold/jobInfo.job'
  #  plugFileName = 'c:/temp/arnold/pluginInfo.job'

    def createCommandsFile(self):

        print 'createCommandsFile start'
        fileName =  self.cmdFileLocation + '/' + 'commandsfile.txt'
        f=open(fileName,'w')
        for i in range(self.startFrame,(self.endFrame+1)):
            batFileNameOnly = self.cmdFileLocation +'/'+'arnoldRenderBatch.'+ '%04d'%i + '.bat'
            #print batFileNameOnly    
            f.write(batFileNameOnly + '\n')
        f.close
        
        
       # kick -i teapot.ass -r 640 480 -g 2.2 -o teapot.tif
        

    def exportAssFile(self):
        
        

        assStore = self.outAssPutPath
        fileName = self.deadLineJobName      #ass ÀÉ®×¦WºÙ 

        print assStore
        for i in range(self.startFrame,self.endFrame +1):
            
            cmds.currentTime(i,e=True)
            
            currentFrame = int(cmds.currentTime(q=True))

            framePanding = '%04d'%currentFrame
            cmd = 'arnoldExportAss -f ' + '\"' + assStore +'/' + fileName +'.'+ framePanding +'.ass' +'\"'
            print cmd
            pm.mel.eval('%s'%cmd)


                #     self.startFrame
        #self.endFrame    outPutPath
        
        
    def createJobInfoFile(self):
        GetCurrentUserFromDeadLine = subprocess.Popen(["%s"%self.deadLineRoot,"GetCurrentUserName"], stdout=subprocess.PIPE, shell=True).communicate()[0]  #cmd run deadlineCommand -Pools,that get pools from deadline Repo
        user = GetCurrentUserFromDeadLine.split("\r\n")[0]
        poolSelect = self.comboBox_deadPool.currentText() 
        self.deadLineJobpriority = self.lineEdit_deadLineJobpriority.text()

        print 'createJobInfoFile start'
        jobinfo = ["Name="+"%s"%self.deadLineJobName,"UserName="+"%s"%user,"Frames="+"%s"%self.startFrame+"-"+"%s"%self.endFrame,"Pool="+"%s"%poolSelect,"Priority="+"%s"%self.deadLineJobpriority,"Plugin=CommandScript","OutputDirectory0="+"%s"% self.ImageOutputFolder]
       # Name=C03_scenes_AO_sirius_tsai
       # UserName=render
       # Frames=250-350
        #Pool=arnold
       # Priority=65
       # Plugin=MayaBatch newDeadLineJobpriorityomp\images\masterLayer\beauty

        fileName =  self.cmdFileLocation + '/' + 'jobInfo.job'
       # OutputDirectory0=\\mcd-server\art_3d_project\supercar_pk_3\shot\shot03\c
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
        f.write('StartupDirectory='+'%s'%self.cmdFileLocation + '\n' )
        f.close
        #StartupDirectory=\\mcd-server\art_3d_project\supercar_pk_3\shot\shot01\ass\renderCMD\0608161915

        
    def createSubmitCommand(self):
        print 'createSubmitCommand start'
        fileName =  self.cmdFileLocation + '/' + 'sendToDeadLine.bat'
        jobInfoFileName =  self.cmdFileLocation + '/' + 'jobInfo.job'
        pluginInfoFileName = self.cmdFileLocation + '/' + 'pluginInfo.job'
        commandsfileName = self.cmdFileLocation + '/' + 'commandsfile.txt'
        
 
        f=open(fileName,'w')
        f.write("deadlinecommand.exe "+"%s "%jobInfoFileName+"%s "%pluginInfoFileName+"%s "%commandsfileName)
        f.close
        
        

 #arnoldToDeadline
#def arnoldToDeadlineMain():
def main():
    global ui
    app = QtGui.QApplication.instance()
    if app == None: app = QApplication(sys.argv)
    try:
        ui.close()
        ui.deleteLater()
    except: pass
    ui = mod_MainWindow()
    ui.show()
 
if __name__ == '__main__':
    main() 