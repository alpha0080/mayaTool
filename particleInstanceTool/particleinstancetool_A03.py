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
        
        self.setFontSize=8
        #setPointSize(11) = setPointSize(self.setFontSize +3)
        #setPointSize(10) = setPointSize(self.setFontSize +2)
        #setPointSize(self.setFontSize)    = setPointSize(self.setFontSize) 
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(484, 505)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_sourceParticle = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sourceParticle.setGeometry(QtCore.QRect(230, 40, 231, 31))
        self.lineEdit_sourceParticle.setObjectName("lineEdit_sourceParticle")
        self.pushButton_addObbject = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_addObbject.setGeometry(QtCore.QRect(30, 80, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize) 
        self.pushButton_addObbject.setFont(font)
        self.pushButton_addObbject.setObjectName("pushButton_addObbject")
        self.listWidget_objList = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_objList.setGeometry(QtCore.QRect(230, 80, 231, 161))
        self.listWidget_objList.setObjectName("listWidget_objList")
        QtWidgets.QListWidgetItem(self.listWidget_objList)
        QtWidgets.QListWidgetItem(self.listWidget_objList)
        self.pushButton_getParticle = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_getParticle.setGeometry(QtCore.QRect(30, 40, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize) 
        self.pushButton_getParticle.setFont(font)
        self.pushButton_getParticle.setObjectName("pushButton_getParticle")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 272, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize) 
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.lineEdit_randomScale = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_randomScale.setGeometry(QtCore.QRect(150, 270, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize) 
        self.lineEdit_randomScale.setFont(font)
        self.lineEdit_randomScale.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_randomScale.setObjectName("lineEdit_randomScale")
        self.lineEdit_randomPosition = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_randomPosition.setGeometry(QtCore.QRect(150, 290, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize) 
        self.lineEdit_randomPosition.setFont(font)
        self.lineEdit_randomPosition.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_randomPosition.setObjectName("lineEdit_randomPosition")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 292, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize) 
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_Rotation = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Rotation.setGeometry(QtCore.QRect(150, 310, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize) 
        self.lineEdit_Rotation.setFont(font)
        self.lineEdit_Rotation.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_Rotation.setObjectName("lineEdit_Rotation")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 312, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize) 
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 10, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize) 
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit_particleCount = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_particleCount.setGeometry(QtCore.QRect(390, 10, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize) 
        self.lineEdit_particleCount.setFont(font)
        self.lineEdit_particleCount.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_particleCount.setReadOnly(True)
        self.lineEdit_particleCount.setObjectName("lineEdit_particleCount")
        self.comboBox_copyMode = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_copyMode.setGeometry(QtCore.QRect(100, 130, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize) 
        self.comboBox_copyMode.setFont(font)
        self.comboBox_copyMode.setObjectName("comboBox_copyMode")
        self.comboBox_copyMode.addItem("")
        self.comboBox_copyMode.addItem("")
        self.label_copyMode = QtWidgets.QLabel(self.centralwidget)
        self.label_copyMode.setGeometry(QtCore.QRect(-50, 138, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize) 
        self.label_copyMode.setFont(font)
        self.label_copyMode.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_copyMode.setObjectName("label_copyMode")
        self.comboBox_displayMode = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_displayMode.setGeometry(QtCore.QRect(100, 170, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize) 
        self.comboBox_displayMode.setFont(font)
        self.comboBox_displayMode.setObjectName("comboBox_displayMode")
        self.comboBox_displayMode.addItem("")
        self.comboBox_displayMode.addItem("")
        self.label_copyMode_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_copyMode_2.setGeometry(QtCore.QRect(-50, 178, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize) 
        self.label_copyMode_2.setFont(font)
        self.label_copyMode_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_copyMode_2.setObjectName("label_copyMode_2")
        self.pushButton_create = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create.setGeometry(QtCore.QRect(30, 420, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize) 
        self.pushButton_create.setFont(font)
        self.pushButton_create.setObjectName("pushButton_create")
        self.label_copyMode_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_copyMode_3.setGeometry(QtCore.QRect(-50, 218, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize) 
        self.label_copyMode_3.setFont(font)
        self.label_copyMode_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_copyMode_3.setObjectName("label_copyMode_3")
        self.comboBox_aimMode = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_aimMode.setGeometry(QtCore.QRect(100, 210, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize) 
        self.comboBox_aimMode.setFont(font)
        self.comboBox_aimMode.setObjectName("comboBox_aimMode")
        self.comboBox_aimMode.addItem("")
        self.comboBox_aimMode.addItem("")
        self.lineEdit_errorMessage = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_errorMessage.setGeometry(QtCore.QRect(230, 270, 231, 121))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize) 
        self.lineEdit_errorMessage.setFont(font)
        self.lineEdit_errorMessage.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_errorMessage.setObjectName("lineEdit_errorMessage")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 250, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize) 
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_spread = QtWidgets.QLabel(self.centralwidget)
        self.label_spread.setGeometry(QtCore.QRect(0, 342, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize) 
        self.label_spread.setFont(font)
        self.label_spread.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_spread.setObjectName("label_spread")
        self.lineEdit_spread = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_spread.setGeometry(QtCore.QRect(150, 340, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize) 
        self.lineEdit_spread.setFont(font)
        self.lineEdit_spread.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_spread.setObjectName("lineEdit_spread")
        self.label_multiple = QtWidgets.QLabel(self.centralwidget)
        self.label_multiple.setGeometry(QtCore.QRect(0, 372, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize) 
        self.label_multiple.setFont(font)
        self.label_multiple.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_multiple.setObjectName("label_multiple")
        self.lineEdit_multiple = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_multiple.setGeometry(QtCore.QRect(150, 370, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize) 
        self.lineEdit_multiple.setFont(font)
        self.lineEdit_multiple.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_multiple.setObjectName("lineEdit_multiple")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.pushButton_addObbject.setText(QtWidgets.QApplication.translate("MainWindow", "add Object into list", None, -1))
        __sortingEnabled = self.listWidget_objList.isSortingEnabled()
        self.listWidget_objList.setSortingEnabled(False)
        self.listWidget_objList.item(0).setText(QtWidgets.QApplication.translate("MainWindow", "aaa", None, -1))
        self.listWidget_objList.item(1).setText(QtWidgets.QApplication.translate("MainWindow", "bbb", None, -1))
        self.listWidget_objList.setSortingEnabled(__sortingEnabled)
        self.pushButton_getParticle.setText(QtWidgets.QApplication.translate("MainWindow", "get Source Particle", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "random Scale", None, -1))
        self.lineEdit_randomScale.setText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.lineEdit_randomPosition.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "random Position", None, -1))
        self.lineEdit_Rotation.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "random Rotation", None, -1))
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
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "error message", None, -1))
        self.label_spread.setText(QtWidgets.QApplication.translate("MainWindow", "spread", None, -1))
        self.lineEdit_spread.setText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.label_multiple.setText(QtWidgets.QApplication.translate("MainWindow", "multiple", None, -1))
        self.lineEdit_multiple.setText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))




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

        
        self.comboBox_copyMode.currentIndexChanged.connect(self.copyModeSelect)
        self.comboBox_displayMode.currentIndexChanged.connect(self.displayModeSelect)
        self.comboBox_aimMode.currentIndexChanged.connect(self.aimModeSelect)
        self.copyMode = "duplicate"



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
                    rotX = math.degrees(math.atan2(rotateNormalx,rotateNormaly))
                    rotZ = math.degrees(math.asin(-rotateNormalx))
                    print n,'rotX',rotX
                    print n,'rotZ',rotZ
                    cmds.setAttr( "%s.rotateX"%newName,rotZ) 
                    #cmds.setAttr( "%s.rotateY"%newName,rotX) 
                    cmds.setAttr( "%s.rotateZ"%newName,-rotX) 
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


 