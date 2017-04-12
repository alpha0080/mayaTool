# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha.DESKTOP-1S1STEK/Documents/GitHub/ribGen/renderManBatchCMD_UI_01.ui'
#
# Created: Tue Feb 14 10:48:29 2017
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
        MainWindow.resize(692, 704)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 30, 101, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_frameStart = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_frameStart.setGeometry(QtCore.QRect(100, 30, 110, 20))
        self.lineEdit_frameStart.setObjectName("lineEdit_frameStart")
        self.lineEdit_frameEnd = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_frameEnd.setGeometry(QtCore.QRect(320, 30, 110, 20))
        self.lineEdit_frameEnd.setObjectName("lineEdit_frameEnd")
        self.lineEdit_Project = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_Project.setGeometry(QtCore.QRect(140, 150, 531, 20))
        self.lineEdit_Project.setObjectName("lineEdit_Project")
        self.lineEdit_filePath = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_filePath.setGeometry(QtCore.QRect(140, 180, 531, 20))
        self.lineEdit_filePath.setObjectName("lineEdit_filePath")
        self.pushButton_createBatchCmd = QtGui.QPushButton(self.centralwidget)
        self.pushButton_createBatchCmd.setGeometry(QtCore.QRect(30, 270, 181, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(90, 112, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 112, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 112, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton_createBatchCmd.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_createBatchCmd.setFont(font)
        self.pushButton_createBatchCmd.setObjectName("pushButton_createBatchCmd")
        self.pushButton_setProject = QtGui.QPushButton(self.centralwidget)
        self.pushButton_setProject.setGeometry(QtCore.QRect(30, 150, 91, 23))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 71, 104))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 71, 104))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 71, 104))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton_setProject.setPalette(palette)
        self.pushButton_setProject.setObjectName("pushButton_setProject")
        self.pushButton_setFilePath = QtGui.QPushButton(self.centralwidget)
        self.pushButton_setFilePath.setGeometry(QtCore.QRect(30, 180, 91, 23))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 71, 104))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 71, 104))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 71, 104))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton_setFilePath.setPalette(palette)
        self.pushButton_setFilePath.setObjectName("pushButton_setFilePath")
        self.lineEdit_filePath_renderCmd = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_filePath_renderCmd.setGeometry(QtCore.QRect(230, 270, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lineEdit_filePath_renderCmd.setFont(font)
        self.lineEdit_filePath_renderCmd.setObjectName("lineEdit_filePath_renderCmd")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 210, 81, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_prmanReleated = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_prmanReleated.setGeometry(QtCore.QRect(140, 210, 531, 20))
        self.lineEdit_prmanReleated.setObjectName("lineEdit_prmanReleated")
        self.lineEdit_resX = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_resX.setEnabled(False)
        self.lineEdit_resX.setGeometry(QtCore.QRect(130, 70, 61, 20))
        self.lineEdit_resX.setObjectName("lineEdit_resX")
        self.lineEdit_resY = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_resY.setEnabled(False)
        self.lineEdit_resY.setGeometry(QtCore.QRect(196, 70, 61, 20))
        self.lineEdit_resY.setObjectName("lineEdit_resY")
        self.lineEdit_modifyMaxSample = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_modifyMaxSample.setEnabled(False)
        self.lineEdit_modifyMaxSample.setGeometry(QtCore.QRect(400, 70, 61, 20))
        self.lineEdit_modifyMaxSample.setObjectName("lineEdit_modifyMaxSample")
        self.checkBox_exportLog = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_exportLog.setGeometry(QtCore.QRect(30, 102, 281, 16))
        self.checkBox_exportLog.setChecked(True)
        self.checkBox_exportLog.setObjectName("checkBox_exportLog")
        self.checkBox_modifyRESXY = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_modifyRESXY.setGeometry(QtCore.QRect(30, 70, 91, 16))
        self.checkBox_modifyRESXY.setObjectName("checkBox_modifyRESXY")
        self.checkBox_modifyMaxSample = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_modifyMaxSample.setGeometry(QtCore.QRect(280, 70, 121, 16))
        self.checkBox_modifyMaxSample.setObjectName("checkBox_modifyMaxSample")
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 120, 681, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 470, 681, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lineEdit_MayaFile = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_MayaFile.setGeometry(QtCore.QRect(190, 548, 471, 31))
        self.lineEdit_MayaFile.setObjectName("lineEdit_MayaFile")
        self.pushButton_setMayaFile = QtGui.QPushButton(self.centralwidget)
        self.pushButton_setMayaFile.setGeometry(QtCore.QRect(20, 548, 151, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 71, 104))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 71, 104))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 71, 104))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton_setMayaFile.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_setMayaFile.setFont(font)
        self.pushButton_setMayaFile.setObjectName("pushButton_setMayaFile")
        self.checkBox_frameStep = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_frameStep.setGeometry(QtCore.QRect(500, 30, 51, 16))
        self.checkBox_frameStep.setObjectName("checkBox_frameStep")
        self.lineEdit_frameStep = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_frameStep.setEnabled(False)
        self.lineEdit_frameStep.setGeometry(QtCore.QRect(560, 30, 61, 20))
        self.lineEdit_frameStep.setObjectName("lineEdit_frameStep")
        self.pushButton_genRenderJob = QtGui.QPushButton(self.centralwidget)
        self.pushButton_genRenderJob.setGeometry(QtCore.QRect(20, 610, 151, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(193, 125, 113))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(193, 125, 113))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(193, 125, 113))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton_genRenderJob.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_genRenderJob.setFont(font)
        self.pushButton_genRenderJob.setObjectName("pushButton_genRenderJob")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 490, 91, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_fileNamePrefix = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_fileNamePrefix.setGeometry(QtCore.QRect(130, 490, 531, 20))
        self.lineEdit_fileNamePrefix.setObjectName("lineEdit_fileNamePrefix")
        self.checkBox_divide = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_divide.setGeometry(QtCore.QRect(500, 70, 71, 16))
        self.checkBox_divide.setObjectName("checkBox_divide")
        self.lineEdit_divide = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_divide.setEnabled(False)
        self.lineEdit_divide.setGeometry(QtCore.QRect(560, 70, 61, 20))
        self.lineEdit_divide.setObjectName("lineEdit_divide")
        self.radioButton_single = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_single.setGeometry(QtCore.QRect(40, 240, 81, 16))
        self.radioButton_single.setChecked(True)
        self.radioButton_single.setObjectName("radioButton_single")
        self.radioButton_multifiles = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_multifiles.setGeometry(QtCore.QRect(130, 240, 91, 16))
        self.radioButton_multifiles.setObjectName("radioButton_multifiles")
        self.pushButton_submitDeadLine = QtGui.QPushButton(self.centralwidget)
        self.pushButton_submitDeadLine.setGeometry(QtCore.QRect(30, 420, 181, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(90, 112, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 112, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 112, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton_submitDeadLine.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_submitDeadLine.setFont(font)
        self.pushButton_submitDeadLine.setObjectName("pushButton_submitDeadLine")
        self.comboBox_deadPool = QtGui.QComboBox(self.centralwidget)
        self.comboBox_deadPool.setGeometry(QtCore.QRect(170, 380, 191, 25))
        self.comboBox_deadPool.setObjectName("comboBox_deadPool")
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 380, 111, 20))
        self.label_5.setObjectName("label_5")
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 310, 681, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 330, 111, 20))
        self.label_6.setObjectName("label_6")
        self.lineEdit_deadLineJobName = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_deadLineJobName.setGeometry(QtCore.QRect(160, 330, 511, 20))
        self.lineEdit_deadLineJobName.setObjectName("lineEdit_deadLineJobName")
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(380, 380, 111, 20))
        self.label_7.setObjectName("label_7")
        self.lineEdit_deadLineJobpriority = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_deadLineJobpriority.setGeometry(QtCore.QRect(480, 380, 51, 20))
        self.lineEdit_deadLineJobpriority.setObjectName("lineEdit_deadLineJobpriority")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 692, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "renderManBatchRender", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Frame Start", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Frame End", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_createBatchCmd.setText(QtGui.QApplication.translate("MainWindow", "Create batchRender file", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_setProject.setText(QtGui.QApplication.translate("MainWindow", "set Project", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_setFilePath.setText(QtGui.QApplication.translate("MainWindow", "set File Path", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_filePath_renderCmd.setText(QtGui.QApplication.translate("MainWindow", "c:/temp/renderManRender.bat", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "PRMAN related", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_prmanReleated.setText(QtGui.QApplication.translate("MainWindow", "prman -t:0 -Progress -recover 0 -logfile c:/temp/render.log -loglevel 4 -checkpoint 5m -cwd ", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_exportLog.setText(QtGui.QApplication.translate("MainWindow", "export LogFile(batchRenderFileName.log)", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_modifyRESXY.setText(QtGui.QApplication.translate("MainWindow", "Modify ResXY", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_modifyMaxSample.setText(QtGui.QApplication.translate("MainWindow", "Modify Max Sample", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_setMayaFile.setText(QtGui.QApplication.translate("MainWindow", "set Maya File", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_frameStep.setText(QtGui.QApplication.translate("MainWindow", "Step", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_frameStep.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_genRenderJob.setText(QtGui.QApplication.translate("MainWindow", "Generate RenderJob", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "file Name Prefix", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_fileNamePrefix.setText(QtGui.QApplication.translate("MainWindow", "<Scene>/<RenderLayer>/<RenderLayer>", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_divide.setText(QtGui.QApplication.translate("MainWindow", "Divide", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_divide.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_single.setText(QtGui.QApplication.translate("MainWindow", "single file", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_multifiles.setText(QtGui.QApplication.translate("MainWindow", "mulit Files", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_submitDeadLine.setText(QtGui.QApplication.translate("MainWindow", "submit to DeadLine", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "select DeadLine Pool", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "DeadLine Job Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "select Job Priority", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_deadLineJobpriority.setText(QtGui.QApplication.translate("MainWindow", "50", None, QtGui.QApplication.UnicodeUTF8))


###------------------------------------------------------QT UI END------------------------------------------------------------------------------------



###------------------------------------------------------custom UI init-------------------------------------------------------------------
        
        self.deadLineRoot = pm.mel.eval("getenv DEADLINE_PATH")+"/deadlinecommand.exe"
        output = subprocess.Popen(["%s"%self.deadLineRoot,"Pools"], stdout=subprocess.PIPE, shell=True).communicate()[0]  #cmd run deadlineCommand -Pools,that get pools from deadline Repo
        poolList = output.split("\r\n")
        poolCount = len(poolList)
        for addNum in range(0,poolCount):
            self.comboBox_deadPool.addItem("")
            comboBoxItemName = poolList[addNum]
            self.comboBox_deadPool.setItemText(addNum, QtGui.QApplication.translate("MainWindow",comboBoxItemName, None, QtGui.QApplication.UnicodeUTF8))




        self.projectPath = pm.mel.eval("rman getvar RMSPROJ")[:-1]
        self.lineEdit_Project.setText(self.projectPath)
        self.lineEdit_deadLineJobName.setText(self.projectPath.split('/')[-4]+"_" + self.projectPath.split('/')[-2])
       # self.renderManRoot = pm.mel.eval("getenv RMANTREE")+"prman.exe"
        

        self.renderCMD = self.projectPath + "/renderCmd/renderManRender.bat "
        self.lineEdit_filePath_renderCmd.setText("renderManRender.bat")
        #prmanCmd = "\""+ self.renderManRoot+"\"" +" -t:0 -Progress -recover 0 -checkpoint 5m -cwd"
        #self.lineEdit_prmanReleated.setText(prmanCmd)
        self.lineEdit_prmanReleated.setText("prman -t:0 -Progress -recover 0 -checkpoint 5m -cwd")

        self.prmanCMD = self.lineEdit_prmanReleated.text()
        print self.prmanCMD
        self.step = self.lineEdit_frameStep.text()
        initResX = cmds.getAttr("renderManRISGlobals.rman__riopt__Format_resolution0")
        initResY = cmds.getAttr("renderManRISGlobals.rman__riopt__Format_resolution1")
        self.lineEdit_resX.setText("%s"%initResX)
        self.lineEdit_resY.setText("%s"%initResY)    
        self.resX = self.lineEdit_resX.text()
        self.resY = self.lineEdit_resY.text()     
        initMaxSample = cmds.getAttr( "renderManRISGlobals.rman__riopt__Hider_maxsamples")
        self.lineEdit_modifyMaxSample.setText("%s"%initMaxSample)
        self.maxSample = self.lineEdit_modifyMaxSample.text()
        self.divide = self.lineEdit_divide.text()
        
        self.cmdRes = "-res"+ " "+ self.resX +" "+self.resY
        print self.cmdRes
        self.cmdMaxSample = "-maxsamples"+" "+self.maxSample
        print self.cmdMaxSample
        self.cmdLog = "-logfile"+" "+"%s"%self.renderCMD[:-3]+"log"+" "+"-loglevel 4"
        print self.cmdLog
        
       # self.resX = self.lineEdit_resX.setText("")
       # self.resY = self.lineEdit_resY.setText("")        
        self.pushButton_setProject.clicked.connect(self.modpushButton_setProject)
        self.pushButton_setFilePath.clicked.connect(self.modpushButton_setFilePath)
        self.pushButton_createBatchCmd.clicked.connect(self.modpushButton_createBatchCmd)
        
        self.pushButton_setMayaFile.clicked.connect(self.modpushButton_setMayaFile)
        self.pushButton_genRenderJob.clicked.connect(self.modpushButton_genRenderJob)
        self.pushButton_submitDeadLine.clicked.connect(self.modpushButton_submitDeadLine)



        self.lineEdit_filePath_renderCmd.textChanged.connect(self.modlineEdit_filePath_renderCmd)

        
     ## checkBox state change   
     
        self.checkBox_frameStep.stateChanged.connect(self.modcheckBox_frameStep)
        self.checkBox_modifyRESXY.stateChanged.connect(self.modcheckBox_modifyRESXY)
        self.checkBox_modifyMaxSample.stateChanged.connect(self.modcheckBox_modifyMaxSample)
        self.checkBox_exportLog.stateChanged.connect(self.modcheckBox_exportLog)
        self.checkBox_divide.stateChanged.connect(self.modcheckBox_divide)


        self.radioButton_single.clicked.connect(self.modradioButton_single)
        self.radioButton_multifiles.clicked.connect(self.modradioButton_multifiles)



        
        
     ## change value if checkbox state is checked  
        self.lineEdit_frameStep.textChanged.connect(self.modlineEdit_frameStep)
        self.lineEdit_resX.textChanged.connect(self.modlineEdit_resX)
        self.lineEdit_resY.textChanged.connect(self.modlineEdit_resY)
        self.lineEdit_modifyMaxSample.textChanged.connect(self.modlineEdit_modifyMaxSample)
        self.lineEdit_divide.textChanged.connect(self.modlineEdit_divide)

   #             
        
        
        
        self.lineEdit_frameStart.textChanged.connect(self.modlineEdit_frameStart)
        self.lineEdit_frameEnd.textChanged.connect(self.modlineEdit_frameEnd)
        self.lineEdit_prmanReleated.textChanged.connect(self.modlineEdit_prmanReleated)
        self.lineEdit_fileNamePrefix.textChanged.connect(self.modlineEdit_fileNamePrefix)
        self.lineEdit_deadLineJobName.textChanged.connect(self.modlineEdit_deadLineJobName)
        self.lineEdit_deadLineJobpriority.textChanged.connect(self.modlineEdit_deadLineJobpriority)





class mod_MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent= QtGui.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        # self.setWindowFlags(QtCore.Qt.Tool)
#-----------------------checkBox-------------------        
        self.setupUi(self)
    def modcheckBox_frameStep(self):
       # print "modcheckBox_frameStep"
        
        if self.checkBox_frameStep.isChecked() == True:  
           # print "frameStep Mod"        
            self.lineEdit_frameStep.setEnabled(True)
        else:
            self.lineEdit_frameStep.setEnabled(False)
            self.lineEdit_frameStep.setText("1")

     

    def modcheckBox_modifyRESXY(self):
      #  print "modcheckBox_modifyRESXY"
        
        if self.checkBox_modifyRESXY.isChecked() == True:  
            print "checkBox_modifyRESXY Mod"  
            self.lineEdit_resX.setEnabled(True)
            self.lineEdit_resY.setEnabled(True)

        else:
            self.lineEdit_resX.setEnabled(False)
            self.lineEdit_resY.setEnabled(False)
        
    def modcheckBox_modifyMaxSample(self):
        if self.checkBox_modifyMaxSample.isChecked() == True:  
            print "checkBox_modifyMaxSample Mod"    
            self.lineEdit_modifyMaxSample.setEnabled(True)
        else:
            self.lineEdit_modifyMaxSample.setEnabled(False)

     
        
    def modcheckBox_exportLog(self):
        if self.checkBox_exportLog.isChecked() == True: 
            self.cmdLog = "-logfile"+" "+"%s"%self.renderCMD[:-3]+"log"+" "+"-loglevel 4"
            print self.cmdLog
            
        else:
            self.cmdLog = ""
            print self.cmdLog

      
            print "checkBox_exportLog Mod"    
            
            
    def modcheckBox_divide(self):
      #  print "modcheckBox_modifyRESXY"
        
        if self.checkBox_divide.isChecked() == True:  
            print "checkBox_divide Mod"  
            self.lineEdit_divide.setEnabled(True)
            
            
        else:
            self.lineEdit_divide.setEnabled(False)
            self.divide = self.lineEdit_divide.setText("1")

            
            
            
            
    def modradioButton_single(self):
        self.lineEdit_filePath_renderCmd.setText("renderManRender.bat")
       # self.singleFileName = self.lineEdit_filePath_renderCmd.setText(self.renderCMD)

        #print "ffff"
            
            
    def modradioButton_multifiles(self):
        multiFileNameList = self.lineEdit_filePath_renderCmd.text().split(".")
        self.multiFileName = multiFileNameList[0]+".$F4.bat"  
        self.lineEdit_filePath_renderCmd.setText(self.multiFileName)      
            
            
    def modlineEdit_divide(self):
       # print "modlineEdit_frameStep"
        self.divide = self.lineEdit_divide.text()
        print self.divide

                    
            
            
            

     
        
#-------------------lineText-------------------------        
    def modlineEdit_frameStep(self):
       # print "modlineEdit_frameStep"
        self.step = self.lineEdit_frameStep.text()
        print self.step

        
    def modlineEdit_resX(self):
        self.resX = self.lineEdit_resX.text()
        print self.resX
        
        
    def modlineEdit_resY(self):
        self.resY = self.lineEdit_resY.text()

        print self.resY
        
    def modlineEdit_modifyMaxSample(self):
        self.maxSample = self.lineEdit_modifyMaxSample.text()

        print  self.maxSample
        
        
    def modlineEdit_prmanReleated(self):
        self.prmanCMD = self.lineEdit_prmanReleated.text ()
        print self.prmanCMD        

        
    def modlineEdit_filePath_renderCmd(self):
        self.renderCMD = self.lineEdit_filePath_renderCmd.text ()
        self.cmdLog = "-logfile"+" "+"%s"%self.renderCMD[:-3]+"log"+" "+"-loglevel 4"

        print self.renderCMD
        
    def modlineEdit_frameStart(self):
        self.frameStart = int( self.lineEdit_frameStart.text () )
        print self.frameStart
    
    
    def modlineEdit_frameEnd(self):
        self.frameEnd = int( self.lineEdit_frameEnd.text () )
        print self.frameEnd
    
                
                                        
    
    def modlineEdit_fileNamePrefix(self):
        self.fileNamePrefix =self.lineEdit_fileNamePrefix.text () 
        print self.fileNamePrefix
    
    def modlineEdit_deadLineJobName(self):
        self.deadLineJobName =self.lineEdit_deadLineJobName.text () 
        self.lineEdit_deadLineJobName.setText(self.deadLineJobName) 
        print  self.deadLineJobName

    def modlineEdit_deadLineJobpriority(self):
        self.deadLineJobpriority =self.lineEdit_deadLineJobpriority.text () 
        self.lineEdit_deadLineJobpriority.setText(self.deadLineJobpriority) 
        print   self.deadLineJobpriority
        
                
                
        
        
        
    def modpushButton_setProject(self):
        self.projectPath = cmds.fileDialog2(fm=3)[0]
       # print projectPath[0]
        self.lineEdit_Project.setText(self.projectPath)
        
    def modpushButton_setFilePath(self):
        self.fileNamePath = cmds.fileDialog2(fm=1)[0]
        
        #print projectPath[0]
        self.lineEdit_filePath.setText(self.fileNamePath)
        
        


        
    def modpushButton_createBatchCmd(self):
        print"write render command batch file"
        #tempForder = "c:/temp"
        self.getFileForder()

        self.jsonFileName = self.cmdFileLocation +"/"+ self.lineEdit_filePath_renderCmd.text()[0:-3]+"json"
        jsonBatFileName = self.cmdFileLocation +"/"+ self.lineEdit_filePath_renderCmd.text()[0:-3]+"batch.json"
        print self.jsonFileName
        self.createRenderCmdJson()
        if self.radioButton_single.isChecked() == True:
            fileName = self.cmdFileLocation  +"/"+ self.lineEdit_filePath_renderCmd.text()
            renderBatchFile = open(fileName,'w')

            for line in self.batchRenderCmdLis:
                renderBatchFile.write(line + "\n")
                

            renderBatchFile.close
        else:

            for frameNum in range(0,(len(self.batchRenderCmdLis))):
                fileName = self.cmdFileLocation  +"/"+ self.lineEdit_filePath_renderCmd.text().split(".")[0] +"."+"%04d"%(frameNum+1)+".bat"
                
                renderBatchFile = open(fileName,'w')
                #renderBatchFile.write("set %path%;%DEADLINE_PATH%bin;%RMANTREE%bin"+"\n")
                renderBatchFile.write(self.batchRenderCmdLis[frameNum])
                renderBatchFile.close
            for frameNum in range(0,(len(self.batchRenderCmdLis))):   # export all bat job to json
                batchJobJsonFile = open(jsonBatFileName,'a')

                fileName = self.cmdFileLocation  +"/"+ self.lineEdit_filePath_renderCmd.text().split(".")[0] +"."+"%04d"%(frameNum+1)+".bat"
                #batchJobJsonFile = open(jsonBatFileName,'a')
                batchJobJsonFile.write(fileName +'\n')
                batchJobJsonFile.close
               # print fileName
               
    def modpushButton_submitDeadLine(self):
        if self.radioButton_single.isChecked() == True:
            print "__________________________________________________________________"
            print "-                                                                -"
            print "-                                                                -"
            print "-                                                                -"
            print "-   do not select single frame                                   -"
            print "-                                                                -"
            print "-                                                                -"
            print "-                                                                -"
            print "__________________________________________________________________"
        else:

            print " sendTo Deadline"
            self.createSubmitDeadLine()
            print self.popCommand
            sendJob = subprocess.Popen(self.popCommand,stdout=subprocess.PIPE,universal_newlines=True, shell=True).communicate()[0]  #cmd run deadlineCommand -Pools,that get pools from deadline Repo
            print sendJob
            
            
            
        
        
        
        

    def createSubmitDeadLine(self):
       # self.getFileForder()
        self.createRenderCmdJson()
       # print self.cmdFileLocation
        poolSelect = self.comboBox_deadPool.currentText() 
        GetCurrentUserFromDeadLine = subprocess.Popen(["%s"%self.deadLineRoot,"GetCurrentUserName"], stdout=subprocess.PIPE, shell=True).communicate()[0]  #cmd run deadlineCommand -Pools,that get pools from deadline Repo
        user = GetCurrentUserFromDeadLine.split("\r\n")[0]
        #print user
        output = self.lineEdit_Project.text()+"/images/"
        #print self.lineEdit_filePath.text().split('/')[-4]
        newDeadLineJobName = self.lineEdit_deadLineJobName.text()
        newDeadLineJobpriority = self.lineEdit_deadLineJobpriority.text()
        totalFrame = str((int(self.frameEnd) - int(self.frameStart)))
        #print self.frameEnd
        #print self.frameStart
        #print self.frameEnd
        
        print newDeadLineJobName 
       # jobinfo = ["Name="+"%s"%newDeadLineJobName,"UserName="+"%s"%user,"Frames="+"%s"%self.frameStart+"-"+"%s"%self.frameEnd,"Pool="+"%s"%poolSelect,"Priority="+"%s"%newDeadLineJobpriority,"Plugin=CommandScript","OutputDirectory0="+"%s"%output]
        jobinfo = ["Name="+"%s"%newDeadLineJobName,"UserName="+"%s"%user,"Frames="+"0"+"-"+"%s"%totalFrame,"Pool="+"%s"%poolSelect,"Priority="+"%s"%newDeadLineJobpriority,"Plugin=CommandScript"]
       # jobinfo = ["Name="+"%s"%newDeadLineJobName,"UserName="+"%s"%user,"Frames="+"%s"%self.frameStart+"-"+"%s"%self.frameEnd,"Pool="+"%s"%poolSelect,"Priority="+"%s"%newDeadLineJobpriority,"Plugin=CommandScript"]

        jobinfoCount= int(len(jobinfo))
        
        #StartupDirectory = self.cmdFileLocation
        print "StartupDirectory="+ self.cmdFileLocation
       
       #print "aaaaaaaaa"
        self.jsonFileName = self.cmdFileLocation +"/"+ self.lineEdit_filePath_renderCmd.text()[0:-3]+"json"
        commandsfileName = self.cmdFileLocation +"/"+"commandsfile.txt "
        jobInfoFileName = self.cmdFileLocation +"/"+"jobInfo.job"
        pluginInfoFileName = self.cmdFileLocation +"/"+"pluginInfo.job"

      #  batchJobJsonFile = open(commandsfileName,'w')

        if self.radioButton_single.isChecked() == True:
            print "Should be select Multi Frame"
            pass
            
            
        else:

            for frameNum in range(0,(len(self.batchRenderCmdLis))):
                fileName = self.cmdFileLocation  +"/"+ self.lineEdit_filePath_renderCmd.text().split(".")[0] +"."+"%04d"%(frameNum+1)+".bat"
                
                renderBatchFile = open(fileName,'w')
                #renderBatchFile.write("set %path%;%DEADLINE_PATH%bin;%RMANTREE%bin"+"\n")
                renderBatchFile.write(self.batchRenderCmdLis[frameNum])
                renderBatchFile.close
                
            if self.frameStart >= 0:
                jobinfo[2] = "Frames="+"%s"%self.frameStart+"-"+"%s"%self.frameEnd
                    
                for echoFrameNum in range(0,self.frameStart):   # export all bat job to json, deadline commandsFile.txt
                    #commandFile = open(commandsfileName,'w')
                    echoCommand = "echo\n"
                    commandFile = open(commandsfileName,'a')
                    commandFile.write(echoCommand)
                    commandFile.close
                    
                    
                    


            for frameNum in range(0,(len(self.batchRenderCmdLis))):   # export all bat job to json, deadline commandsFile.txt
                #commandFile = open(commandsfileName,'w')
                fileName = self.cmdFileLocation  +"/"+ self.lineEdit_filePath_renderCmd.text().split(".")[0] +"."+"%04d"%(frameNum+1)+".bat"
                commandFile = open(commandsfileName,'a')
                commandFile.write('%s'%fileName +'\n')
                commandFile.close

            for lineNum in range(0,jobinfoCount):             # export all render info to deadline commandsFile.txt  
                
                jobInfoFile = open(jobInfoFileName,'a')
                print jobinfo[lineNum]
                jobInfoFile.write('%s'%jobinfo[lineNum]+'\n')
                jobInfoFile.close
            
            pluginInfo = open(pluginInfoFileName,'w')
            pluginInfo.write("StartupDirectory="+ self.cmdFileLocation)
            pluginInfo.close
            
            jobSendToDeadLineBatchFileName = self.cmdFileLocation  +"/"+"sendToDeadLine.bat"
            #jobSendToDeadLineBatchFileName='//MCD-SERVER/art_3d_project/fish_battle_v02_cf/shot/vr_test/layout/renderCmd/0223145242/sendToDeadLine.bat'
            jobSendToDeadLine = open(jobSendToDeadLineBatchFileName,'w')
            jobSendToDeadLine.write("deadlinecommand.exe "+"%s "%jobInfoFileName+"%s "%pluginInfoFileName+"%s "%commandsfileName)
            jobSendToDeadLine.close
            print self.cmdFileLocation
            print jobInfoFileName
            print pluginInfoFileName
            print commandsfileName
            #self.popCommand = jobSendToDeadLineBatchFileName
            self.popCommand=[u'deadlinecommand.exe']
            self.popCommand.append(u'%s'%jobInfoFileName)
            self.popCommand.append(u'%s'%pluginInfoFileName)
            self.popCommand.append(u'%s'%commandsfileName)
            
     

    def getFileForder(self):
        

        dt = datetime.datetime.now()
        newFormatDt = dt.strftime("%m%d%H%M%S")           #("%Y%m%d%H%M%S")  that add year   
        self.cmdFileLocation = self.lineEdit_Project.text()+"/renderCmd/"+newFormatDt
        


        
    def createRenderCmdJson(self):
        self.getFileForder()
        
        pm.sysFile( self.cmdFileLocation, makeDir=True )  # create folder

        self.maxSample = self.lineEdit_modifyMaxSample.text()            
       # fileName = cmdFileLocation +"/"+ self.lineEdit_filePath_renderCmd.text()
        self.jsonFileName = self.cmdFileLocation +"/"+ self.lineEdit_filePath_renderCmd.text()[0:-3]+"json"
        #renderBatchFile = open(fileName,'w')
        renderJsonFile = open(self.jsonFileName,'w')
        parList = self.fileNamePath.split("/")
        #print parList

        count = 0
        self.cmdRes = "-res"+ " "+ self.resX +" "+self.resY
        self.cmdMaxSample = "-maxsamples"+" "+self.maxSample


        self.batchRenderCmdLis = []

        for par in parList:
            #print count 
           # print parList[count]
            
            if par == "renderman" and parList[count+2] == "rib" :
              #  print "go"
                try:
                    #count =8
                    for frameNum in range(int(self.frameStart),int(self.frameEnd)+1):
                      #  print frameNum
                       # renderBatchFile = open(fileName,'a')
                        digiNum = len(parList[count+3])

                        cmd02 = str(frameNum).zfill(digiNum) 
                        cmd01 = parList[count] +"/"+ parList[count+1] +"/" +parList[count+2]
                        fileNameSplit = parList[-1].split(".")
                        cmd03 = fileNameSplit[0]+"."+ cmd02 +"."+"rib"
                        #cmd = self.prmanCMD + self.projectPath+" "+self.cmdLog +" "+ self.cmdRes +" "+self.cmdMaxSample +" " + cmd01 +"/"+ cmd02+"/" +cmd03+"\n"
                       # cmd = self.prmanCMD + self.projectPath +" "+ cmd01 +"/"+ cmd02+"/" + cmd03 +"\n"
                        cmd = "%s"%self.prmanCMD + " "+ "%s"%self.projectPath + " "+ "%s"%self.cmdLog +" "+ "%s"%self.cmdRes+" " +"%s"%self.cmdMaxSample + " "+ cmd01 +"/"+ cmd02+"/" +cmd03+"\n"+"echo Next Frame"+"\n"
                       # print self.cmdLog
                      #  print self.cmdRes
                       # print self.cmdMaxSample
                        #print cmd
                        self.batchRenderCmdLis.append(cmd)
                        #renderBatchFile.write(str(cmd))


                except:
                    print "error path with frame and job number"
              #  print count
            else:
                #pass
                print "unCorrect Command"
             #   print count
             
            count = count +1

            #renderBatchFile.close
       # print self.batchRenderCmdLis


        json.dumps(self.batchRenderCmdLis, sort_keys=True , indent =4)  

        renderJsonFile.write(json.dumps(self.batchRenderCmdLis, sort_keys=True , indent =4))
   
        renderJsonFile.close
            

    def modpushButton_setMayaFile(self):

        self.mayaNamePath = cmds.fileDialog2(fm=1)[0]
        
        #print projectPath[0]
        self.lineEdit_MayaFile.setText(self.mayaNamePath)
        
    def modpushButton_genRenderJob(self):

        self.getFileForder()

        pm.sysFile( self.cmdFileLocation, makeDir=True )  # create folder
        ribGenFIleName= self.lineEdit_MayaFile.text().split("/")[-1].split(".")[0]
        print ribGenFIleName
            
        self.createRibGenCmdJson()
        print self.ribGenCmdList
        for jobNum in range(1,(len(self.ribGenCmdList)+1)):
            print jobNum

            fileName = self.cmdFileLocation  +"/"+ ribGenFIleName +"."+"%04d"%(jobNum)+".bat"
            renderBatchFile = open(fileName,'w')
            renderBatchFile.write(self.ribGenCmdList[(jobNum-1)])
            renderBatchFile.close
            
                
                
                      
    def createRibGenCmdJson(self):
        print "generate export to rib"
        renderCmd = pm.mel.eval("getenv MAYA_LOCATION")
        self.step = self.lineEdit_frameStep.text() 
        self.cmdRes = "-res"+ " "+ self.resX +" "+self.resY
        self.fileNamePrefix =self.lineEdit_fileNamePrefix.text () 
        imagePath = self.lineEdit_Project.text()+"/images"
        self.fileNamePrefix =self.lineEdit_fileNamePrefix.text () 
        self.projectPath = self.lineEdit_Project.text()
        self.mayaNamePath = self.lineEdit_MayaFile.text()
       # print self.cmdRes
        genRibCmd = "\""+"%s"%renderCmd +"/"+"bin/render.exe"+"\""+" -r rib" +" "+"-n 0"+" "+self.cmdRes +" "
      #  genRibCmd = "\""+"%s"%renderCmd +"/"+"bin/render.exe"+"\""+" -r rib" +" "+"%s"%self.mayaNamePath

        #print genRibCmd
        
        self.ribGenCmdList= []
        self.frameDivide()
       # print self.frameNumByDivide
       # print self.frameNumDict
       # print self.frameNumByDivide.keys()

        
        for rangeNum in self.frameNumByDivide.keys():
            self.frameRange = self.frameNumByDivide[rangeNum]
           # print self.frameRange

           # print self.frameRange[0]
           # print self.frameRange[-1]
            self.cmdFrameRange ="-s"+" "+"%s"%self.frameNumDict[self.frameNumByDivide[rangeNum][0]] + " "+"-e" +" "+"%s"%self.frameNumDict[self.frameNumByDivide[rangeNum][-1]]+" "+"-b"+" "+"%s"%self.step
          #  print self.cmdFrameRange
            ribExportCmd = genRibCmd + self.cmdFrameRange +" " + "-rd"+" "+"\""+ imagePath + "\""+" "+"-im"+" "+"\""+ self.fileNamePrefix + "\"" +" "+"-proj"+" "+"\""+ self.projectPath + "\""+" "+"\""+self.mayaNamePath+"\""
            print ribExportCmd
            self.ribGenCmdList.append(ribExportCmd)




#####------------------------------------get divide and frame number ,even though from (- frame)--------

        
    def frameDivide(self):
        print"run frameDivide function"
        self.divide = int(self.lineEdit_divide.text())
        self.frameStart = int( self.lineEdit_frameStart.text () )
        self.frameEnd = int( self.lineEdit_frameEnd.text () )
        self.step = int(self.lineEdit_frameStep.text())

        print "start Frame: " + str(self.frameStart )
        print "End Frame: " + str(self.frameEnd)
        print "frame Divided to: " +str( self.divide)
        print "frame by step: " + str(self.step)
       
        
        
        divide = 8

        start =-10
        end =40
        block = (self.frameEnd-self.frameStart)/self.divide



        self.frameNumDict ={} #reNumber frame job from 1

        for keyNum , frameNum in zip(range(1,(self.frameEnd-self.frameStart+2))  , range(self.frameStart,(self.frameEnd+1))):
            
            self.frameNumDict.update({keyNum:frameNum})
            
            
        count =0
        frameListKey = 1
        self.frameNumByDivide ={}
        self.frameList=[]



        for frameNum in range(1,(self.frameEnd-self.frameStart+2)):
            count = count +1
            self.frameList.append(frameNum)
           # print frameListKey,frameNum 
            self.frameNumByDivide.update({frameListKey:self.frameList})

            if count < (block+1):
          
                pass    
            else: 
                frameListKey = frameListKey +1
                count = 0
                self.frameList=[]









            
#modpushButton_setMayaFile





#def main():
def renderManBatchCMDMain():
    global ui
    app = QtGui.QApplication.instance()
    if app == None: app = QApplication(sys.argv)
    try:
        ui.close()
        ui.deleteLater()
    except: pass
    ui = mod_MainWindow()
    ui.show()
 
#if __name__ == '__main__':
#    main() 
#