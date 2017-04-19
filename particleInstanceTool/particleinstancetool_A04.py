# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha/Documents/GitHub/mayaTool/particleInstanceTool/particleinstancetool_01.ui'
#
# Created: Tue Apr 18 21:39:40 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import pymel.core as pm
import maya.cmds as cmds
import random ,math
import maya.OpenMaya as OpenMaya
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        self.setFontSize=5
        #setPointSize(11) = setPointSize(self.setFontSize +3)
        #setPointSize(10) = setPointSize(self.setFontSize +2)
        #setPointSize(self.setFontSize) = setPointSize(self.setFontSize) 
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(474, 620)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_sourceParticle = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sourceParticle.setGeometry(QtCore.QRect(230, 90, 221, 31))
        self.lineEdit_sourceParticle.setObjectName("lineEdit_sourceParticle")
        self.pushButton_addObbject = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_addObbject.setGeometry(QtCore.QRect(30, 130, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.pushButton_addObbject.setFont(font)
        self.pushButton_addObbject.setObjectName("pushButton_addObbject")
        self.listWidget_objList = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_objList.setGeometry(QtCore.QRect(230, 130, 221, 151))
        self.listWidget_objList.setObjectName("listWidget_objList")
        QtWidgets.QListWidgetItem(self.listWidget_objList)
        QtWidgets.QListWidgetItem(self.listWidget_objList)
        self.pushButton_getParticle = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_getParticle.setGeometry(QtCore.QRect(30, 90, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.pushButton_getParticle.setFont(font)
        self.pushButton_getParticle.setObjectName("pushButton_getParticle")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 10, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit_particleCount = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_particleCount.setGeometry(QtCore.QRect(380, 10, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.lineEdit_particleCount.setFont(font)
        self.lineEdit_particleCount.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_particleCount.setReadOnly(True)
        self.lineEdit_particleCount.setObjectName("lineEdit_particleCount")
        self.comboBox_copyMode = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_copyMode.setGeometry(QtCore.QRect(100, 230, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.comboBox_copyMode.setFont(font)
        self.comboBox_copyMode.setObjectName("comboBox_copyMode")
        self.comboBox_copyMode.addItem("")
        self.comboBox_copyMode.addItem("")
        self.label_copyMode = QtWidgets.QLabel(self.centralwidget)
        self.label_copyMode.setGeometry(QtCore.QRect(-50, 238, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.label_copyMode.setFont(font)
        self.label_copyMode.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_copyMode.setObjectName("label_copyMode")
        self.comboBox_displayMode = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_displayMode.setEnabled(True)
        self.comboBox_displayMode.setGeometry(QtCore.QRect(100, 270, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.comboBox_displayMode.setFont(font)
        self.comboBox_displayMode.setObjectName("comboBox_displayMode")
        self.comboBox_displayMode.addItem("")
        self.comboBox_displayMode.addItem("")
        self.label_copyMode_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_copyMode_2.setGeometry(QtCore.QRect(-50, 278, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.label_copyMode_2.setFont(font)
        self.label_copyMode_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_copyMode_2.setObjectName("label_copyMode_2")
        self.pushButton_create = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create.setGeometry(QtCore.QRect(30, 560, 421, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.pushButton_create.setFont(font)
        self.pushButton_create.setObjectName("pushButton_create")
        self.label_copyMode_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_copyMode_3.setGeometry(QtCore.QRect(-50, 318, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.label_copyMode_3.setFont(font)
        self.label_copyMode_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_copyMode_3.setObjectName("label_copyMode_3")
        self.comboBox_aimMode = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_aimMode.setEnabled(True)
        self.comboBox_aimMode.setGeometry(QtCore.QRect(100, 310, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.comboBox_aimMode.setFont(font)
        self.comboBox_aimMode.setObjectName("comboBox_aimMode")
        self.comboBox_aimMode.addItem("")
        self.comboBox_aimMode.addItem("")
        self.lineEdit_errorMessage = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_errorMessage.setGeometry(QtCore.QRect(230, 290, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.lineEdit_errorMessage.setFont(font)
        self.lineEdit_errorMessage.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_errorMessage.setReadOnly(True)
        self.lineEdit_errorMessage.setObjectName("lineEdit_errorMessage")
        self.label_multiple = QtWidgets.QLabel(self.centralwidget)
        self.label_multiple.setGeometry(QtCore.QRect(140, 358, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.label_multiple.setFont(font)
        self.label_multiple.setAlignment(QtCore.Qt.AlignCenter)
        self.label_multiple.setObjectName("label_multiple")
        self.lineEdit_multiple = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_multiple.setGeometry(QtCore.QRect(400, 368, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.lineEdit_multiple.setFont(font)
        self.lineEdit_multiple.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_multiple.setReadOnly(True)
        self.lineEdit_multiple.setObjectName("lineEdit_multiple")
        self.pushButton_getSurfaceMesh = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_getSurfaceMesh.setGeometry(QtCore.QRect(30, 50, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.pushButton_getSurfaceMesh.setFont(font)
        self.pushButton_getSurfaceMesh.setObjectName("pushButton_getSurfaceMesh")
        self.lineEdit_getSurfaceMesh = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_getSurfaceMesh.setGeometry(QtCore.QRect(230, 50, 221, 31))
        self.lineEdit_getSurfaceMesh.setObjectName("lineEdit_getSurfaceMesh")
        self.pushButton_clearList = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clearList.setGeometry(QtCore.QRect(30, 170, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.pushButton_clearList.setFont(font)
        self.pushButton_clearList.setObjectName("pushButton_clearList")
        self.horizontalSlider_multiPly = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_multiPly.setGeometry(QtCore.QRect(30, 370, 361, 20))
        self.horizontalSlider_multiPly.setMinimum(1)
        self.horizontalSlider_multiPly.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_multiPly.setObjectName("horizontalSlider_multiPly")
        self.lineEdit_multiple_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_multiple_2.setGeometry(QtCore.QRect(400, 490, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.lineEdit_multiple_2.setFont(font)
        self.lineEdit_multiple_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_multiple_2.setReadOnly(True)
        self.lineEdit_multiple_2.setObjectName("lineEdit_multiple_2")
        self.horizontalSlider_randomScale = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_randomScale.setGeometry(QtCore.QRect(30, 492, 361, 20))
        self.horizontalSlider_randomScale.setMinimum(1)
        self.horizontalSlider_randomScale.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_randomScale.setObjectName("horizontalSlider_randomScale")
        self.label_randomScale = QtWidgets.QLabel(self.centralwidget)
        self.label_randomScale.setGeometry(QtCore.QRect(140, 480, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.label_randomScale.setFont(font)
        self.label_randomScale.setAlignment(QtCore.Qt.AlignCenter)
        self.label_randomScale.setObjectName("label_randomScale")
        self.lineEdit_randomPosition = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_randomPosition.setGeometry(QtCore.QRect(400, 400, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.lineEdit_randomPosition.setFont(font)
        self.lineEdit_randomPosition.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_randomPosition.setReadOnly(True)
        self.lineEdit_randomPosition.setObjectName("lineEdit_randomPosition")
        self.horizontalSlider_randomPosition = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_randomPosition.setGeometry(QtCore.QRect(30, 402, 361, 20))
        self.horizontalSlider_randomPosition.setMinimum(0)
        self.horizontalSlider_randomPosition.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_randomPosition.setObjectName("horizontalSlider_randomPosition")
        self.label_randomPosition = QtWidgets.QLabel(self.centralwidget)
        self.label_randomPosition.setGeometry(QtCore.QRect(140, 390, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.label_randomPosition.setFont(font)
        self.label_randomPosition.setAlignment(QtCore.Qt.AlignCenter)
        self.label_randomPosition.setObjectName("label_randomPosition")
        self.lineEdit_randomRotation = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_randomRotation.setGeometry(QtCore.QRect(400, 460, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.lineEdit_randomRotation.setFont(font)
        self.lineEdit_randomRotation.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_randomRotation.setReadOnly(True)
        self.lineEdit_randomRotation.setObjectName("lineEdit_randomRotation")
        self.horizontalSlider_randomRotation = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_randomRotation.setGeometry(QtCore.QRect(30, 462, 361, 20))
        self.horizontalSlider_randomRotation.setMinimum(0)
        self.horizontalSlider_randomRotation.setMaximum(360)
        self.horizontalSlider_randomRotation.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_randomRotation.setObjectName("horizontalSlider_randomRotation")
        self.label_randomRotation = QtWidgets.QLabel(self.centralwidget)
        self.label_randomRotation.setGeometry(QtCore.QRect(140, 450, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.label_randomRotation.setFont(font)
        self.label_randomRotation.setAlignment(QtCore.Qt.AlignCenter)
        self.label_randomRotation.setObjectName("label_randomRotation")
        self.lineEdit_spread = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_spread.setGeometry(QtCore.QRect(400, 430, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.lineEdit_spread.setFont(font)
        self.lineEdit_spread.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_spread.setReadOnly(True)
        self.lineEdit_spread.setObjectName("lineEdit_spread")
        self.horizontalSlider_spread = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_spread.setGeometry(QtCore.QRect(30, 432, 361, 20))
        self.horizontalSlider_spread.setMinimum(0)
        self.horizontalSlider_spread.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_spread.setObjectName("horizontalSlider_spread")
        self.label_spread = QtWidgets.QLabel(self.centralwidget)
        self.label_spread.setGeometry(QtCore.QRect(140, 420, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.label_spread.setFont(font)
        self.label_spread.setAlignment(QtCore.Qt.AlignCenter)
        self.label_spread.setObjectName("label_spread")
        self.label_offset = QtWidgets.QLabel(self.centralwidget)
        self.label_offset.setGeometry(QtCore.QRect(140, 510, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.label_offset.setFont(font)
        self.label_offset.setAlignment(QtCore.Qt.AlignCenter)
        self.label_offset.setObjectName("label_offset")
        self.lineEdit_offset = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_offset.setGeometry(QtCore.QRect(400, 520, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.lineEdit_offset.setFont(font)
        self.lineEdit_offset.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_offset.setReadOnly(True)
        self.lineEdit_offset.setObjectName("lineEdit_offset")
        self.horizontalSlider_offset = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_offset.setGeometry(QtCore.QRect(30, 522, 361, 20))
        self.horizontalSlider_offset.setMinimum(0)
        self.horizontalSlider_offset.setMaximum(5)
        self.horizontalSlider_offset.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_offset.setObjectName("horizontalSlider_offset")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.pushButton_addObbject.setText(QtWidgets.QApplication.translate("MainWindow", "add Object into List", None, -1))
        __sortingEnabled = self.listWidget_objList.isSortingEnabled()
        self.listWidget_objList.setSortingEnabled(False)
        self.listWidget_objList.item(0).setText(QtWidgets.QApplication.translate("MainWindow", "aaa", None, -1))
        self.listWidget_objList.item(1).setText(QtWidgets.QApplication.translate("MainWindow", "bbb", None, -1))
        self.listWidget_objList.setSortingEnabled(__sortingEnabled)
        self.pushButton_getParticle.setText(QtWidgets.QApplication.translate("MainWindow", "get Source Particle", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "total particles Count", None, -1))
        self.lineEdit_particleCount.setText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.comboBox_copyMode.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "duplicate", None, -1))
        self.comboBox_copyMode.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "instance", None, -1))
        self.label_copyMode.setText(QtWidgets.QApplication.translate("MainWindow", "copy Mode", None, -1))
        self.comboBox_displayMode.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Bounding Box", None, -1))
        self.comboBox_displayMode.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "shaded", None, -1))
        self.label_copyMode_2.setText(QtWidgets.QApplication.translate("MainWindow", "display Mode", None, -1))
        self.pushButton_create.setText(QtWidgets.QApplication.translate("MainWindow", "create", None, -1))
        self.label_copyMode_3.setText(QtWidgets.QApplication.translate("MainWindow", "aim Mode", None, -1))
        self.comboBox_aimMode.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "always top", None, -1))
        self.comboBox_aimMode.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "normal", None, -1))
        self.label_multiple.setText(QtWidgets.QApplication.translate("MainWindow", "multiple", None, -1))
        self.lineEdit_multiple.setText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.pushButton_getSurfaceMesh.setText(QtWidgets.QApplication.translate("MainWindow", "get surface Mesh", None, -1))
        self.pushButton_clearList.setText(QtWidgets.QApplication.translate("MainWindow", "clear List", None, -1))
        self.lineEdit_multiple_2.setText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.label_randomScale.setText(QtWidgets.QApplication.translate("MainWindow", "random Scale", None, -1))
        self.lineEdit_randomPosition.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.label_randomPosition.setText(QtWidgets.QApplication.translate("MainWindow", "random Position", None, -1))
        self.lineEdit_randomRotation.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.label_randomRotation.setText(QtWidgets.QApplication.translate("MainWindow", "random Rotation", None, -1))
        self.lineEdit_spread.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.label_spread.setText(QtWidgets.QApplication.translate("MainWindow", "spread", None, -1))
        self.label_offset.setText(QtWidgets.QApplication.translate("MainWindow", "offset", None, -1))
        self.lineEdit_offset.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))





class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #self.QTITEM.ACTION.connect(self.MODDEF)
        self.setupUi(self)
    #def self.MODDEF(self):
        self.listWidget_objList.clear()

        self.pushButton_getParticle.clicked.connect(self.clickButton_getParticle)
        self.pushButton_addObbject.clicked.connect(self.clickButtin_addObjIntoList)
        self.pushButton_create.clicked.connect(self.clickButtin_createInstance)
        self.pushButton_getSurfaceMesh.clicked.connect(self.clickButton_getSurfaceMesh)
        
        self.comboBox_copyMode.currentIndexChanged.connect(self.copyModeSelect)
        self.comboBox_displayMode.currentIndexChanged.connect(self.displayModeSelect)
        self.comboBox_aimMode.currentIndexChanged.connect(self.aimModeSelect)
        self.copyMode = "duplicate"

    def clickButton_getSurfaceMesh(self):
        print" get the surface,that take form other scenes"
        pm.select.
        

    def clickButton_getParticle(self):
        print "get Particle from selected"
        
        getParticle = pm.ls(sl=True)
        self.selectParticleStr = getParticle[0] 
        self.selectParticleShapeStr = pm.ls(sl=True,dag=2)[1].split('(')[0]
        #print self.selectParticleShapeStr
        if pm.nodeType(self.selectParticleShapeStr)  == 'nParticle' :
        
            if len(getParticle) > 1:
                print "make sure select one particle"
            
            else:
                print self.selectParticleStr
                self.lineEdit_sourceParticle.setText("%s"%self.selectParticleStr)
        else:
            print "select particle source"
            pass
        
        self.totalParticleCount = pm.nParticle(getParticle, query=True, ct=True)
        self.lineEdit_particleCount.setText('%s'%self.totalParticleCount)

            
    def clickButtin_addObjIntoList(self):
        print "add object into list"
        self.objList = []   #get objList in listWidger
        self.selectObjList = []   #get list from selected
        objCount =  self.listWidget_objList.count()
        for n in range(0,objCount):
            
            object = self.listWidget_objList.item(n).text()
            self.objList.append(object)
        print self.objList
        
        selectObjs = pm.ls(sl=True)
        selectObjsCount = len(selectObjs)
        
        for i in range(0,selectObjsCount):
            addObj = selectObjs[i].split('(')[0]
            if addObj in self.objList: #check if addObj in list
                pass
            else:
            
                self.selectObjList.append(addObj)
                QtWidgets.QListWidgetItem(self.listWidget_objList)
                itemCount = i + objCount
                itemName = selectObjs[i].split('(')[0]
                self.listWidget_objList.item(itemCount).setText(QtWidgets.QApplication.translate("MainWindow","tempName", None, -1))
                self.listWidget_objList.item(itemCount).setText(itemName)
        print self.selectObjList
        
       # QtWidgets.QListWidgetItem(self.listWidget_objList)

       # self.listWidget_objList.item(0).setText(QtWidgets.QApplication.translate("MainWindow", "aaa", None, -1))
    
    
    
    def copyModeSelect(self):
        self.copyMode = self.comboBox_copyMode.currentText()
        self.lineEdit_errorMessage.setText('copy mode : %s'%self.copyMode)
        
    def displayModeSelect(self):
        self.displayMode = self.comboBox_displayMode.currentText()
        self.lineEdit_errorMessage.setText('display mode : %s'%self.displayMode)

    def aimModeSelect(self):
        self.aimMode = self.comboBox_aimMode.currentText()
        self.lineEdit_errorMessage.setText('aim mode : %s'%self.aimMode)


    def clickButtin_createInstanceB(self):
        totalParticleCount = pm.nParticle('%s'%self.selectParticleStr, query=True, ct=True)

       # print self.selectParticleStr
        particlePositionDict={}

        for n in range(0,totalParticleCount):
            perParticle = self.selectParticleStr.pt[n]

            positionPP = pm.getParticleAttr(perParticle, at='position',a=True)

            particlePositionDict.update({str(n):positionPP})


        emptyGrp = pm.createNode('transform', n='instanceGrp' )
        sourceObjCount = len(self.selectObjList)



    def getVertexNormal(self):
        geo = pm.PyNode('pSphere1')
        pos = self.positionPP

        nodeDagPath = OpenMaya.MObject()
        

        try:
            selectionList = OpenMaya.MSelectionList()
            selectionList.add(geo.name())
            nodeDagPath = OpenMaya.MDagPath()
            selectionList.getDagPath(0, nodeDagPath)
        except:
            warning('OpenMaya.MDagPath() failed on %s' % geo.name())
            

   
        mfnMesh = OpenMaya.MFnMesh(nodeDagPath)

        pointA = OpenMaya.MPoint(pos[0], pos[1], pos[2])
        
        pointB = OpenMaya.MPoint()
        space = OpenMaya.MSpace.kWorld
        util = OpenMaya.MScriptUtil()
        util.createFromInt(0)
        idPointer = util.asIntPtr()

        mfnMesh.getClosestPoint(pointA, pointB, space, idPointer)  
        idx = OpenMaya.MScriptUtil(idPointer).asInt()

        faceVerts = [geo.vtx[i] for i in geo.f[idx].getVertices()]
        closestVertex = None
        minLength = None
        
   # def aaaaaa(self):
        
        for v in faceVerts:
            thisLength = (pos - v.getPosition(space='world')).length()
            if minLength is None or thisLength < minLength:
                minLength = thisLength
                closestVertex = v
        #pm.select('pSphereShape1.vtx[141]')

        closeVertexNormal = pm.polyNormalPerVertex(closestVertex,q=1,xyz=1)
        print closestVertex,closeVertexNormal,len(closeVertexNormal)


        try:
            self.avarageNx =( closeVertexNormal[0] + closeVertexNormal[3] + closeVertexNormal[6]  + closeVertexNormal[9] )/4
            self.avarageNy =( closeVertexNormal[1] + closeVertexNormal[4] + closeVertexNormal[7]  + closeVertexNormal[10] )/4
            self.avarageNz =( closeVertexNormal[2] + closeVertexNormal[5] + closeVertexNormal[8]  + closeVertexNormal[11] )/4
        except:
            pass
            
        print self.avarageNx,self.avarageNy,self.avarageNz







    def clickButtin_createInstance(self):
        sourceObjCount = len(self.selectObjList)
        particlePositionDict={}
        self.allInstanceList=[]
        print "particle",self.selectParticleStr
        bb=cmds.xform('%s'%self.selectParticleStr,bb=True,q=True)
        bbMaxDistance = math.sqrt(((bb[3]-bb[0]) *(bb[3]-bb[0])) + ((bb[4]-bb[1]) *(bb[4]-bb[1])) +((bb[5]-bb[2]) *(bb[5]-bb[2])))
        print bbMaxDistance
        emptyGrp = pm.createNode('transform', n='instanceGrp' )
        totalParticleCount = pm.nParticle('%s'%self.selectParticleStr, query=True, ct=True)
        print 'totalParticleCount',totalParticleCount
        multiplyNum= int(self.lineEdit_multiple.text())
        scaleMultiPly = float(self.lineEdit_randomScale.text())
        randomPosition = float(self.lineEdit_randomPosition.text())
        randomRotation = float(self.lineEdit_Rotation.text())
        print "multiply",self.lineEdit_multiple.text()
        print "spread",self.lineEdit_spread.text()
        print "scale", self.lineEdit_randomScale.text()
        print "position",self.lineEdit_randomPosition.text()
        print "rotation",self.lineEdit_Rotation.text()
        

        
        

        for n in range(0,totalParticleCount):
            
            print n
            

            perParticle = self.selectParticleStr.pt[n]

            self.positionPP = pm.getParticleAttr(perParticle, at='position',a=True)
            
            self.getVertexNormal()
            
            self.positionPP.append(self.avarageNx)
            
            self.positionPP.append(self.avarageNy)
            
            self.positionPP.append(self.avarageNz)
            

            particlePositionDict.update({str(n):self.positionPP})

        print particlePositionDict

        for n in range(0,totalParticleCount):

            for k in range(0,multiplyNum):
                #print n,k
                randMovement = random.uniform((-randomPosition),randomPosition)
                sourceObj = self.selectObjList[random.randint(0,(sourceObjCount-1))] #get random obj index
                newName = 'instanceObj' +'_'+ str(n)+'_'+str(k)
                self.allInstanceList.append(newName)
                #print allInstanceList 
                #print newName


                #randomRotation = random.uniform(-randomRotation,randomRotation)

                randomScale = 1 * (random.uniform( -scaleMultiPly,scaleMultiPly))
                if self.copyMode == "duplicate":
                    newInstanceObj = cmds.duplicate( sourceObj, n=newName )
                else:
                    newInstanceObj = cmds.instance( sourceObj, n=newName )
                #random position
                
                if self.lineEdit_randomPosition.text() == "0":
                    moveX = particlePositionDict[str(n)][0] 
                    moveY = particlePositionDict[str(n)][1] 
                    moveZ = particlePositionDict[str(n)][2] 
                    cmds.setAttr( "%s.translateX"%newName,moveX)
                    cmds.setAttr( "%s.translateY"%newName,moveY)
                    cmds.setAttr( "%s.translateZ"%newName,moveZ)
                   # cmds.setAttr( "%s.rotateY"%newName,randomRotation)

                else:
                    randMoveX = particlePositionDict[str(n)][0] + randMovement/bbMaxDistance
                    randMoveY = particlePositionDict[str(n)][1] 
                    randMoveZ = particlePositionDict[str(n)][2] + randMovement/bbMaxDistance               
                
                    cmds.setAttr( "%s.translateX"%newName,randMoveX)
                    cmds.setAttr( "%s.translateY"%newName,randMoveY)
                    cmds.setAttr( "%s.translateZ"%newName,randMoveZ)
                    
                    #cmds.setAttr( "%s.rotateY"%newName,randomRotation)
                    
                    
                #random scale
                if self.lineEdit_randomScale.text() == "1":
                    pass
                else:
                    cmds.setAttr( "%s.scaleX"%newName,randomScale)
                    cmds.setAttr( "%s.scaleZ"%newName,randomScale)
                    
                    
                #random rotate
                if self.lineEdit_Rotation.text() == "0":
                   # pass
                    rotateNormalx = particlePositionDict[str(n)][3]
                    rotateNormaly = particlePositionDict[str(n)][4]
                    rotateNormalz = particlePositionDict[str(n)][5]  
                    
                    
                    rotX = math.degrees(math.atan2(rotateNormaly,rotateNormalz))
                    rotY = math.degrees(math.atan2(rotateNormalx,rotateNormalz))

                 #   rotZ = math.degrees(math.atan2(rotateNormaly,rotateNormalx))
                    rotZ = math.degrees(math.pi/2-math.asin(rotateNormaly))

                    print n,'rotX',rotX
                    print n,'rotY',rotY
                    print n,'rotZ',rotZ
                    cmds.setAttr( "%s.rotateX"%newName,rotZ) 
                    cmds.setAttr( "%s.rotateY"%newName,rotY) 
                   # cmds.setAttr( "%s.rotateZ"%newName,rotZ) 
                    #pass
                else:     
                    #rotationValue = int(self.lineEdit_Rotation.text())
                    #cmds.setAttr( "%s.rotateY"%newName,random.randint(-rotationValue,rotationValue))
                    pass

                    
              #     rotX =  
                pm.parent(newInstanceObj,emptyGrp)
        #self.randomRotation()
             #   float $rotX = rad_to_deg( atan2( ($normal.z), ($normal.y) ) ); 
                #float $rotZ = rad_to_deg( asin( -($normal.x) ) 
#
            
            #warning
            




def main():
#def particleInstanceToolMain():     
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


 