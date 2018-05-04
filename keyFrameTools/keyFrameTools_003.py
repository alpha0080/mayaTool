# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/alphaOnly/github/mayaTool/keyFrameTools/UI/ui01.ui'
#
# Created: Thu Apr 26 09:29:35 2018
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import maya.cmds as cmds
import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 891)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_numberJoints = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_numberJoints.setGeometry(QtCore.QRect(40, 80, 41, 25))
        self.lineEdit_numberJoints.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_numberJoints.setObjectName("lineEdit_numberJoints")
        self.label_sf = QtWidgets.QLabel(self.centralwidget)
        self.label_sf.setGeometry(QtCore.QRect(20, 20, 111, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_sf.setFont(font)
        self.label_sf.setObjectName("label_sf")
        self.label_ef = QtWidgets.QLabel(self.centralwidget)
        self.label_ef.setGeometry(QtCore.QRect(40, 45, 71, 25))
        self.label_ef.setObjectName("label_ef")
        self.pushButton_createJoint = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_createJoint.setGeometry(QtCore.QRect(350, 80, 75, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton_createJoint.setFont(font)
        self.pushButton_createJoint.setObjectName("pushButton_createJoint")
        self.label_rt_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_rt_2.setGeometry(QtCore.QRect(220, 333, 71, 25))
        self.label_rt_2.setObjectName("label_rt_2")
        self.lineEdit_offsetFrame = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_offsetFrame.setGeometry(QtCore.QRect(220, 360, 61, 25))
        self.lineEdit_offsetFrame.setObjectName("lineEdit_offsetFrame")
        self.pushButton_makeOffsetFrame = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_makeOffsetFrame.setGeometry(QtCore.QRect(317, 360, 91, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton_makeOffsetFrame.setFont(font)
        self.pushButton_makeOffsetFrame.setObjectName("pushButton_makeOffsetFrame")
        self.lineEdit_offfsetStartFrame = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_offfsetStartFrame.setGeometry(QtCore.QRect(47, 360, 61, 25))
        self.lineEdit_offfsetStartFrame.setObjectName("lineEdit_offfsetStartFrame")
        self.label_sf_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_sf_2.setGeometry(QtCore.QRect(47, 333, 71, 25))
        self.label_sf_2.setObjectName("label_sf_2")
        self.label_ef_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_ef_2.setGeometry(QtCore.QRect(127, 333, 71, 25))
        self.label_ef_2.setObjectName("label_ef_2")
        self.lineEdit_offfsetendFrame = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_offfsetendFrame.setGeometry(QtCore.QRect(127, 360, 61, 25))
        self.lineEdit_offfsetendFrame.setObjectName("lineEdit_offfsetendFrame")
        self.label_sf_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_sf_3.setGeometry(QtCore.QRect(47, 159, 81, 25))
        self.label_sf_3.setObjectName("label_sf_3")
        self.lineEdit_cutkeyFrames = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cutkeyFrames.setGeometry(QtCore.QRect(47, 186, 61, 25))
        self.lineEdit_cutkeyFrames.setObjectName("lineEdit_cutkeyFrames")
        self.pushButton_cutKeys = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cutKeys.setGeometry(QtCore.QRect(127, 186, 91, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton_cutKeys.setFont(font)
        self.pushButton_cutKeys.setObjectName("pushButton_cutKeys")
        self.lineEdit_alignKey = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_alignKey.setGeometry(QtCore.QRect(47, 276, 61, 25))
        self.lineEdit_alignKey.setObjectName("lineEdit_alignKey")
        self.pushButton_alignKey = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_alignKey.setGeometry(QtCore.QRect(127, 276, 91, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton_alignKey.setFont(font)
        self.pushButton_alignKey.setObjectName("pushButton_alignKey")
        self.label_sf_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_sf_4.setGeometry(QtCore.QRect(47, 251, 81, 25))
        self.label_sf_4.setObjectName("label_sf_4")
        self.checkBox_offsetRandom = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_offsetRandom.setGeometry(QtCore.QRect(137, 313, 73, 25))
        self.checkBox_offsetRandom.setObjectName("checkBox_offsetRandom")
        self.lineEdit_modifyValue = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_modifyValue.setGeometry(QtCore.QRect(30, 600, 91, 25))
        self.lineEdit_modifyValue.setObjectName("lineEdit_modifyValue")
        self.pushButton_makdModify = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_makdModify.setGeometry(QtCore.QRect(320, 600, 91, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton_makdModify.setFont(font)
        self.pushButton_makdModify.setObjectName("pushButton_makdModify")
        self.label_sf_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_sf_5.setGeometry(QtCore.QRect(30, 580, 101, 16))
        self.label_sf_5.setObjectName("label_sf_5")
        self.label_sf_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_sf_6.setGeometry(QtCore.QRect(150, 580, 111, 16))
        self.label_sf_6.setObjectName("label_sf_6")
        self.lineEdit_modifyFrame = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_modifyFrame.setGeometry(QtCore.QRect(150, 600, 151, 25))
        self.lineEdit_modifyFrame.setObjectName("lineEdit_modifyFrame")
        self.checkBox_translateX = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_translateX.setGeometry(QtCore.QRect(30, 460, 81, 16))
        self.checkBox_translateX.setChecked(False)
        self.checkBox_translateX.setObjectName("checkBox_translateX")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(15, 400, 411, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.checkBox_translateY = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_translateY.setGeometry(QtCore.QRect(110, 460, 81, 16))
        self.checkBox_translateY.setChecked(False)
        self.checkBox_translateY.setObjectName("checkBox_translateY")
        self.checkBox_translateZ = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_translateZ.setGeometry(QtCore.QRect(190, 460, 81, 16))
        self.checkBox_translateZ.setObjectName("checkBox_translateZ")
        self.checkBox_rotateX = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_rotateX.setGeometry(QtCore.QRect(30, 490, 81, 16))
        self.checkBox_rotateX.setObjectName("checkBox_rotateX")
        self.checkBox_rotateY = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_rotateY.setGeometry(QtCore.QRect(110, 490, 81, 16))
        self.checkBox_rotateY.setObjectName("checkBox_rotateY")
        self.checkBox_rotateZ = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_rotateZ.setGeometry(QtCore.QRect(190, 490, 81, 16))
        self.checkBox_rotateZ.setChecked(False)
        self.checkBox_rotateZ.setObjectName("checkBox_rotateZ")
        self.checkBox_scaleX = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_scaleX.setGeometry(QtCore.QRect(30, 520, 81, 16))
        self.checkBox_scaleX.setChecked(False)
        self.checkBox_scaleX.setObjectName("checkBox_scaleX")
        self.checkBox_scaleZ = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_scaleZ.setGeometry(QtCore.QRect(190, 520, 81, 16))
        self.checkBox_scaleZ.setObjectName("checkBox_scaleZ")
        self.checkBox_scaleY = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_scaleY.setGeometry(QtCore.QRect(110, 520, 81, 16))
        self.checkBox_scaleY.setChecked(False)
        self.checkBox_scaleY.setObjectName("checkBox_scaleY")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(15, 120, 420, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_sf_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_sf_7.setGeometry(QtCore.QRect(27, 136, 171, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_sf_7.setFont(font)
        self.label_sf_7.setObjectName("label_sf_7")
        self.horizontalSlider_numberJoints = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_numberJoints.setGeometry(QtCore.QRect(90, 80, 251, 25))
        self.horizontalSlider_numberJoints.setMinimum(1)
        self.horizontalSlider_numberJoints.setMaximum(300)
        self.horizontalSlider_numberJoints.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_numberJoints.setObjectName("horizontalSlider_numberJoints")
        self.checkBox_witImagePlanes = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_witImagePlanes.setGeometry(QtCore.QRect(130, 20, 111, 25))
        self.checkBox_witImagePlanes.setChecked(True)
        self.checkBox_witImagePlanes.setObjectName("checkBox_witImagePlanes")
        self.label_ef_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_ef_3.setGeometry(QtCore.QRect(250, 45, 61, 25))
        self.label_ef_3.setObjectName("label_ef_3")
        self.lineEdit_jointName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_jointName.setGeometry(QtCore.QRect(312, 44, 111, 22))
        self.lineEdit_jointName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_jointName.setObjectName("lineEdit_jointName")
        self.pushButton_modifyName = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_modifyName.setGeometry(QtCore.QRect(40, 680, 181, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton_modifyName.setFont(font)
        self.pushButton_modifyName.setObjectName("pushButton_modifyName")
        self.label_sf_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_sf_8.setGeometry(QtCore.QRect(27, 313, 101, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_sf_8.setFont(font)
        self.label_sf_8.setObjectName("label_sf_8")
        self.label_sf_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_sf_9.setGeometry(QtCore.QRect(27, 226, 231, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_sf_9.setFont(font)
        self.label_sf_9.setObjectName("label_sf_9")
        self.label_sf_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_sf_10.setGeometry(QtCore.QRect(20, 420, 131, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_sf_10.setFont(font)
        self.label_sf_10.setObjectName("label_sf_10")
        self.checkBox_alphaGain = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_alphaGain.setGeometry(QtCore.QRect(250, 136, 73, 25))
        self.checkBox_alphaGain.setObjectName("checkBox_alphaGain")
        self.checkBox_colorGain = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_colorGain.setGeometry(QtCore.QRect(340, 136, 73, 25))
        self.checkBox_colorGain.setObjectName("checkBox_colorGain")
        self.checkBox_modify_alphaGain = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_modify_alphaGain.setGeometry(QtCore.QRect(30, 540, 73, 25))
        self.checkBox_modify_alphaGain.setObjectName("checkBox_modify_alphaGain")
        self.checkBox_modify_colorGain = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_modify_colorGain.setGeometry(QtCore.QRect(110, 540, 73, 25))
        self.checkBox_modify_colorGain.setObjectName("checkBox_modify_colorGain")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(15, 640, 411, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_sf_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_sf_11.setGeometry(QtCore.QRect(20, 650, 131, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_sf_11.setFont(font)
        self.label_sf_11.setObjectName("label_sf_11")
        self.checkBox_modify_all = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_modify_all.setGeometry(QtCore.QRect(340, 460, 81, 16))
        self.checkBox_modify_all.setObjectName("checkBox_modify_all")
        self.radioButton_offsetV = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_offsetV.setGeometry(QtCore.QRect(170, 426, 91, 16))
        self.radioButton_offsetV.setChecked(True)
        self.radioButton_offsetV.setObjectName("radioButton_offsetV")
        self.radioButton_replaceV = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_replaceV.setGeometry(QtCore.QRect(280, 426, 111, 16))
        self.radioButton_replaceV.setObjectName("radioButton_replaceV")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.lineEdit_numberJoints.setText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.label_sf.setText(QtWidgets.QApplication.translate("MainWindow", "create Joints", None, -1))
        self.label_ef.setText(QtWidgets.QApplication.translate("MainWindow", "amount", None, -1))
        self.pushButton_createJoint.setText(QtWidgets.QApplication.translate("MainWindow", "create Joint", None, -1))
        self.label_rt_2.setText(QtWidgets.QApplication.translate("MainWindow", "offset ", None, -1))
        self.pushButton_makeOffsetFrame.setText(QtWidgets.QApplication.translate("MainWindow", "offset Keys", None, -1))
        self.label_sf_2.setText(QtWidgets.QApplication.translate("MainWindow", "start frame", None, -1))
        self.label_ef_2.setText(QtWidgets.QApplication.translate("MainWindow", "end frame", None, -1))
        self.label_sf_3.setText(QtWidgets.QApplication.translate("MainWindow", "cutKey Frames", None, -1))
        self.pushButton_cutKeys.setText(QtWidgets.QApplication.translate("MainWindow", "cut Keys", None, -1))
        self.pushButton_alignKey.setText(QtWidgets.QApplication.translate("MainWindow", "align Keys", None, -1))
        self.label_sf_4.setText(QtWidgets.QApplication.translate("MainWindow", "align frame", None, -1))
        self.checkBox_offsetRandom.setText(QtWidgets.QApplication.translate("MainWindow", "random", None, -1))
        self.lineEdit_modifyValue.setText(QtWidgets.QApplication.translate("MainWindow", "1,1", None, -1))
        self.pushButton_makdModify.setText(QtWidgets.QApplication.translate("MainWindow", "modify Keys", None, -1))
        self.label_sf_5.setText(QtWidgets.QApplication.translate("MainWindow", "value (value,value)", None, -1))
        self.label_sf_6.setText(QtWidgets.QApplication.translate("MainWindow", "frames index [0,1,...]", None, -1))
        self.lineEdit_modifyFrame.setText(QtWidgets.QApplication.translate("MainWindow", "all", None, -1))
        self.checkBox_translateX.setText(QtWidgets.QApplication.translate("MainWindow", "translateX", None, -1))
        self.checkBox_translateY.setText(QtWidgets.QApplication.translate("MainWindow", "translateY", None, -1))
        self.checkBox_translateZ.setText(QtWidgets.QApplication.translate("MainWindow", "translateZ", None, -1))
        self.checkBox_rotateX.setText(QtWidgets.QApplication.translate("MainWindow", "rotateX", None, -1))
        self.checkBox_rotateY.setText(QtWidgets.QApplication.translate("MainWindow", "rotateY", None, -1))
        self.checkBox_rotateZ.setText(QtWidgets.QApplication.translate("MainWindow", "rotateZ", None, -1))
        self.checkBox_scaleX.setText(QtWidgets.QApplication.translate("MainWindow", "scaleX", None, -1))
        self.checkBox_scaleZ.setText(QtWidgets.QApplication.translate("MainWindow", "scaleZ", None, -1))
        self.checkBox_scaleY.setText(QtWidgets.QApplication.translate("MainWindow", "scaleY", None, -1))
        self.label_sf_7.setText(QtWidgets.QApplication.translate("MainWindow", "Cutting All Keys", None, -1))
        self.checkBox_witImagePlanes.setText(QtWidgets.QApplication.translate("MainWindow", "with image plane", None, -1))
        self.label_ef_3.setText(QtWidgets.QApplication.translate("MainWindow", "name proxy:", None, -1))
        self.lineEdit_jointName.setText(QtWidgets.QApplication.translate("MainWindow", "bone_", None, -1))
        self.pushButton_modifyName.setText(QtWidgets.QApplication.translate("MainWindow", "modify Joints and slot  Names", None, -1))
        self.label_sf_8.setText(QtWidgets.QApplication.translate("MainWindow", "Offset All Keys", None, -1))
        self.label_sf_9.setText(QtWidgets.QApplication.translate("MainWindow", "Align All Keys", None, -1))
        self.label_sf_10.setText(QtWidgets.QApplication.translate("MainWindow", "Random All Keys", None, -1))
        self.checkBox_alphaGain.setText(QtWidgets.QApplication.translate("MainWindow", "alpha Gain", None, -1))
        self.checkBox_colorGain.setText(QtWidgets.QApplication.translate("MainWindow", "color Gain", None, -1))
        self.checkBox_modify_alphaGain.setText(QtWidgets.QApplication.translate("MainWindow", "alpha Gain", None, -1))
        self.checkBox_modify_colorGain.setText(QtWidgets.QApplication.translate("MainWindow", "color Gain", None, -1))
        self.label_sf_11.setText(QtWidgets.QApplication.translate("MainWindow", "other tools", None, -1))
        self.checkBox_modify_all.setText(QtWidgets.QApplication.translate("MainWindow", "all", None, -1))
        self.radioButton_offsetV.setText(QtWidgets.QApplication.translate("MainWindow", "offset Value", None, -1))
        self.radioButton_replaceV.setText(QtWidgets.QApplication.translate("MainWindow", "replace Value", None, -1))






class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #self.QTITEM.ACTION.connect(self.MODDEF)
        self.setupUi(self)
    #def self.MODDEF(self):pushButton_modifyName
     #   self.setAttrStateList()
       # self.pushButton_mc.clicked.connect(self.getItems)
        self.pushButton_makeOffsetFrame.clicked.connect(self.offsetKeyFrames)
        self.pushButton_cutKeys.clicked.connect(self.cutKeys)
        self.pushButton_alignKey.clicked.connect(self.alignKeys)
        self.pushButton_makdModify.clicked.connect(self.modifyKeyValue)
       # self.pushButton_modifyName.clicked.connect(self.createJoints)
        self.horizontalSlider_numberJoints.valueChanged.connect(self.modifyJointInputSlider)
        self.lineEdit_numberJoints.textChanged.connect(self.modifyJointInputText)
        self.pushButton_createJoint.clicked.connect(self.createJoints)
        
        
        
        self.checkBox_translateX.stateChanged.connect(self.modifyAttrStateDict)
        self.checkBox_translateY.stateChanged.connect(self.modifyAttrStateDict)
        self.checkBox_translateZ.stateChanged.connect(self.modifyAttrStateDict)
        self.checkBox_rotateX.stateChanged.connect(self.modifyAttrStateDict)
        self.checkBox_rotateY.stateChanged.connect(self.modifyAttrStateDict)
        self.checkBox_rotateZ.stateChanged.connect(self.modifyAttrStateDict)
        self.checkBox_scaleX.stateChanged.connect(self.modifyAttrStateDict)
        self.checkBox_scaleY.stateChanged.connect(self.modifyAttrStateDict)
        self.checkBox_scaleZ.stateChanged.connect(self.modifyAttrStateDict)
        self.checkBox_modify_alphaGain.stateChanged.connect(self.modifyAttrStateDict)
        self.checkBox_modify_colorGain.stateChanged.connect(self.modifyAttrStateDict)
        self.checkBox_modify_all.stateChanged.connect(self.modifyAllAttrStateDict)

    
        self.attrCheckStateDict = {"translateX":0,
                                   "translateY":0,
                                   "translateZ":0,
                                   "rotateX":0,
                                   "rotateY":0,
                                   "rotateZ":0,
                                   "scaleX":0,
                                   "scaleY":0,
                                   "scaleZ":0,
                                   "alphaGain":0,
                                   "colorGain":0
                                   }
                                  
        
    
    
    #create joints with plane(slot) or copy key from other object
    def createJoints(self):
        print "create joints"
        jointAmount = int(self.lineEdit_numberJoints.text())
        
        proxyName =  str(self.lineEdit_jointName.text()) 
        for i in range(0,jointAmount):
            proxyNameSN = proxyName +"%03d"%i
            joint = cmds.createNode("joint",n= proxyNameSN)
            cmds.addAttr( longName='spineAttribute', numberOfChildren=7, attributeType='compound' )
            cmds.addAttr( longName='slotName', dataType="string",parent='spineAttribute')

            cmds.addAttr( longName='alphaGain', attributeType='float',defaultValue=1.0, minValue=0.0, maxValue=1.0,parent='spineAttribute')

            cmds.addAttr(longName='colorGain', usedAsColor=True, attributeType='float3',parent='spineAttribute' )
            cmds.addAttr( longName='redColorGain', attributeType='float', defaultValue=1.0, parent='colorGain' )
            cmds.addAttr( longName='greenColorGain', attributeType='float',defaultValue=1.0, parent='colorGain' )
            cmds.addAttr( longName='blueColorGain', attributeType='float',defaultValue=1.0, parent='colorGain' )
            cmds.addAttr(longName='darkColor', usedAsColor=True, attributeType='float3',parent='spineAttribute' )
            cmds.addAttr( longName='redDarkColor', attributeType='float', defaultValue=0.0, parent='darkColor' )
            cmds.addAttr( longName='greenDarkColor', attributeType='float',defaultValue=0.0, parent='darkColor' )
            cmds.addAttr( longName='blueDarkColor', attributeType='float',defaultValue=0.0, parent='darkColor' )
            cmds.addAttr( longName='slotW', attributeType='long',defaultValue=50, minValue=0, maxValue=2048,parent='spineAttribute')
            cmds.addAttr( longName='slotH', attributeType='long',defaultValue=50, minValue=0, maxValue=2048,parent='spineAttribute')
            cmds.addAttr( longName='blendMode', attributeType='enum',en="normal:additive:multiply:screen",parent='spineAttribute')

            if self.checkBox_witImagePlanes.isChecked() == True:
                slotName = proxyName +"sl_"+"%03d"%i
                cmds.polyPlane(n= slotName,sx=1, sy=1, w=1, h=1)
                cmds.setAttr("%s.scaleX"%slotName,50)
                cmds.setAttr("%s.scaleZ"%slotName,50)
                cmds.setAttr("%s.rotateX"%slotName,90)
                cmds.parent(slotName,proxyNameSN)
            else:
                pass


#print "%04d"%1
    def modifyAllAttrStateDict(self):
      #  print "modify all key"
        if self.checkBox_modify_all.isChecked() == True:
         #   print "all on"
            self.checkBox_translateX.setChecked(True)
            self.checkBox_translateY.setChecked(True)
            self.checkBox_translateZ.setChecked(True)
            self.checkBox_rotateX.setChecked(True)
            self.checkBox_rotateY.setChecked(True)
            self.checkBox_rotateZ.setChecked(True)
            self.checkBox_scaleX.setChecked(True)
            self.checkBox_scaleY.setChecked(True)
            self.checkBox_scaleZ.setChecked(True)
            self.checkBox_modify_alphaGain.setChecked(True)
            self.checkBox_modify_colorGain.setChecked(True)
            

        else:
         #   print "all off"
            self.checkBox_translateX.setChecked(False)
            self.checkBox_translateY.setChecked(False)
            self.checkBox_translateZ.setChecked(False)
            self.checkBox_rotateX.setChecked(False)
            self.checkBox_rotateY.setChecked(False)
            self.checkBox_rotateZ.setChecked(False)
            self.checkBox_scaleX.setChecked(False)
            self.checkBox_scaleY.setChecked(False)
            self.checkBox_scaleZ.setChecked(False)
            self.checkBox_modify_alphaGain.setChecked(False)
            self.checkBox_modify_colorGain.setChecked(False)
                        
            
            
            
            
            
            
    def modifyAttrStateDict(self):
    #    print " modifyAttrStateDict"
        if self.checkBox_translateX.isChecked() == True:
            self.attrCheckStateDict["translateX"] = 1
        else:
            self.attrCheckStateDict["translateX"] = 0
        if self.checkBox_translateY.isChecked() == True:
            self.attrCheckStateDict["translateY"] = 1
        else:
            self.attrCheckStateDict["translateY"] = 0            
            
        if self.checkBox_translateZ.isChecked() == True:
            self.attrCheckStateDict["translateZ"] = 1
        else:
            self.attrCheckStateDict["translateZ"] = 0        
            
            
        
        if self.checkBox_rotateX.isChecked() == True:
            self.attrCheckStateDict["rotateX"] = 1                                   
        else:
            self.attrCheckStateDict["rotateX"] = 0       
                                      
        if self.checkBox_rotateY.isChecked() == True:
            self.attrCheckStateDict["rotateY"] = 1
        else:
            self.attrCheckStateDict["rotateY"] = 0    
                                           
        if self.checkBox_rotateZ.isChecked() == True:
            self.attrCheckStateDict["rotateZ"] = 1
        else:
            self.attrCheckStateDict["rotateZ"] = 0                                   
                                
        if self.checkBox_scaleX.isChecked() == True:
            self.attrCheckStateDict["scaleX"] = 1
        else:
            self.attrCheckStateDict["scaleX"] = 0                                   
                                        
        if self.checkBox_scaleY.isChecked() == True:
            self.attrCheckStateDict["scaleY"] = 1
        else:
            self.attrCheckStateDict["scaleY"] = 0                                   
                                        
        if self.checkBox_scaleZ.isChecked() == True:
            self.attrCheckStateDict["scaleZ"] = 1
        else:
            self.attrCheckStateDict["scaleZ"] = 0                                   

        if self.checkBox_modify_alphaGain.isChecked() == True:
            self.attrCheckStateDict["alphaGain"] = 1
        else:
            self.attrCheckStateDict["alphaGain"] = 0                                   
                                        
        if self.checkBox_modify_colorGain.isChecked() == True:
            self.attrCheckStateDict["colorGain"] = 1
        else:
            self.attrCheckStateDict["colorGain"] = 0                                   
                                        

   #    print self.attrCheckStateDict

    def setAttrStateList(self):
        if self.checkBox_translateX.isChecked() == True:
            print "translate X is selected"
            if "translateX" not in self.attrCheckStateList:
                self.attrCheckStateList.append("translateX")
            else:
                pass
                
        else:
            try:
                self.attrCheckStateList.remove("translateX")
                print "translate X is unselected"
            except:
                pass
        print "self.attrCheckStateList",self.attrCheckStateList
    def modifyJointInputText(self):
    
        print "create Joints"
        
        jointAmount = int(self.lineEdit_numberJoints.text())
        
        print jointAmount
       # self.lineEdit_numberJoints.setText("ffdf")
        
        self.horizontalSlider_numberJoints.setValue(jointAmount)
        
    def modifyJointInputSlider(self):
        
        print "slide change"
        
        jointAmount = int(self.horizontalSlider_numberJoints.value())
        print jointAmount

        self.lineEdit_numberJoints.setText(str(jointAmount))
        
        
        
        
        
    def modifyKeyValue(self):
        print "modify select key Attribute"
       # if self.checkBox_translateX.isChecked() == True:
            
        #if self.checkBox_translateX.isChecked() == True:
        frameList = self.lineEdit_modifyFrame.text().split(",")
        valueList = self.lineEdit_modifyValue.text().split(",")
        objList = cmds.ls(sl=True,l=True)
        
        modifyAttrList=[]
        for attr in self.attrCheckStateDict.keys():
            if self.attrCheckStateDict[attr] == 1:
                modifyAttrList.append(attr)
              #  print attr
        
        print modifyAttrList
        
        print "frameList",frameList
     #   print valueList
     #   print objList
     #   print self.attrCheckStateDict
        for obj in objList:  
            for attr in modifyAttrList:
                keyframeList =  cmds.keyframe( obj,at=attr, query=True) 
                print "keyframeList",obj,attr,keyframeList
                offsetValue =  random.uniform(float(valueList[0]),float(valueList[1]))
              #  print offsetValue
                if frameList[0] == "all":
                    for frame in keyframeList:
                        frameVale = cmds.keyframe(obj,at=attr,t=(frame,frame),q=True,eval=True)[0]
                        print attr,frame,frameVale
                        if self.radioButton_offsetV.isChecked == True:
                            changeValue = offsetValue + frameVale
                          #  print changeValue
                            cmds.setKeyframe(obj, t=[frame,frame], at=attr,v=changeValue )
                        else:
                            cmds.setKeyframe(obj, t=[frame,frame], at=attr,v=offsetValue )

                    
                else:
                    for indexNum in frameList:
                        frame = keyframeList[int(indexNum)]
                        
                        startFrameValue = cmds.keyframe(obj,at=attr,t=(frame,frame),q=True,eval=True)[0]
                        print attr,frame,startFrameValue
                        if self.radioButton_offsetV.isChecked == True:
                            changeValue = offsetValue + frameVale
                            cmds.setKeyframe(obj, t=[frame,frame], at=attr,v=changeValue )
                        else:
                            cmds.setKeyframe(obj, t=[frame,frame], at=attr,v=offsetValue )            
        '''
        for obj in objList:   
            if self.checkBox_scaleX.isChecked() == True:  changeValue
                if frame == "all":
                    keyFrameList = cmds.keyframe( obj,at='sx', query=True) 
                  #  keyFrameList = cmds.keyframe( obj,at='sx', query=True) 
             #   frame = keyFrameList[frameIndex]
                
            print "frame",frame

            randomScaleInt = random.randint(scaleMin,scaleMax)
            print randomScaleInt
            randomScale = float(randomScaleInt)/100.0
            currentValueX = cmds.keyframe(obj,at='sx',t=(frame,frame),q=True,eval=True)[0]
            currentValueY = cmds.keyframe(obj,at='sy',t=(frame,frame),q=True,eval=True)[0]
            currentValueZ = cmds.keyframe(obj,at='sz',t=(frame,frame),q=True,eval=True)[0]

           # print currentValue,type(currentValue)
            vcValueX = float(currentValueX)*float(randomScale)
            vcValueY = float(currentValueY)*float(randomScale)
            vcValueZ = float(currentValueZ)*float(randomScale)

            cmds.keyframe(obj, t=(frame,frame),at='sx',vc =vcValueX)
            cmds.keyframe(obj, t=(frame,frame),at='sy',vc =vcValueY)
            cmds.keyframe(obj, t=(frame,frame),at='sz',vc =vcValueZ)
            
            
      '''  
            
            
            

    def alignKeys(self):
        print "alignKeys"
        objList = self.getObjList()
        alignFrame = float(self.lineEdit_alignKey.text())  
       # print objList
        for obj in objList:
         #   print obj
            keyFrameList= []
            tempKeyFrameList = cmds.keyframe(obj,q=True)
            for key in tempKeyFrameList:
                if key in keyFrameList:
                    pass
                else:
                    keyFrameList.append(key)

            if alignFrame <= keyFrameList[0]:  #align keyframe when align frame <= first keyframe
                for i in range(0,len(keyFrameList)):
                    originalFrame = keyFrameList[i]
                    newKeyFrame = i +alignFrame

                    try:
                        cmds.keyframe(obj,time=(originalFrame,originalFrame),timeChange=(newKeyFrame))
                    except:
                        pass
            else:
                offsetFrame =alignFrame -keyFrameList[0] #align keyframe when align frame > first keyframe
                print keyFrameList
                resveredKeyFrameList = list(reversed(keyFrameList))
                for i in range(0,len(keyFrameList)):
                    originalFrame =  resveredKeyFrameList[i]
                    
                    newKeyFrame = originalFrame +offsetFrame

                    cmds.keyframe(obj,time=(originalFrame,originalFrame),timeChange=(newKeyFrame))
        

    def cutKeys(self):
        print "cutKeys"
        objList = self.getObjList()
        keepRange = int(self.lineEdit_cutkeyFrames.text())
       # cutStartFrame = float(cutFrames.split(",")[0])
        #cutEndFrame = float(cutFrames.split(",")[1])
       # print keepRange
        for obj in objList:
            keyFrameList= []
            tempKeyFrameList = cmds.keyframe(obj,q=True)
            for key in tempKeyFrameList:
                if key in keyFrameList:
                    pass
                else:
                    keyFrameList.append(key)
            totalFrames= len(keyFrameList)
            for i in range(keepRange,totalFrames):
                frame = keyFrameList[i]
              #  print frame
                cmds.cutKey( obj, time=(frame,frame),option="keys" )
                
                
                
        
    
    def offsetKeyFrames(self):
        offsetStartFrame = float(self.lineEdit_offfsetStartFrame.text())
        offsetEndFrame = float(self.lineEdit_offfsetendFrame.text())
       # offsetValue = float(self.lineEdit_offsetFrame.text())

        #divideNextFrame  = divideFrame +1 divideFrame

        keyFrameLength = offsetEndFrame-offsetStartFrame +1.0
        print "offsetKeyFrames"
        
        keyAbleAttList=["translateX","translateY","translateZ","rotateX","rotateY","rotateZ","scaleX","scaleY","scaleZ"] #["translateX","translateY","translateZ","rotateX","rotateY","rotateZ","scaleX","scaleY","scaleZ"]
        objList = self.getObjList()
        
        for obj in objList:
            if self.checkBox_offsetRandom.isChecked() == False:
                offsetValue = int(self.lineEdit_offsetFrame.text())
            else:
                offsetValue = random.randint(0,int(self.lineEdit_offsetFrame.text()))
    
            divideFrame = offsetStartFrame + offsetValue 
            divideStepFrame = divideFrame+0.01


          #  print obj offsetValue
           # if 
            for attr in keyAbleAttList :

              #  print attr,offsetStartFrame,offsetEndFrame,startFrameValue,endFrameValue
                
                try:
                    startFrameValue = cmds.keyframe(obj,at=attr,t=(offsetStartFrame,offsetStartFrame),q=True,eval=True)[0] # get startFrame value
                    endFrameValue = cmds.keyframe(obj,at=attr,t=(offsetEndFrame,offsetEndFrame),q=True,eval=True)[0] # get endFrame value
                    
                    cmds.setKeyframe(obj, t=[offsetStartFrame,offsetStartFrame], at=attr,v=startFrameValue ) #setKey to startFrame
                    cmds.setKeyframe(obj, t=[offsetEndFrame,offsetEndFrame], at=attr,v=endFrameValue ) #setKey to endFrame
                    
                                  
                    keyValueDict = {}
                    offsetKeyFrameDict={}
                    keyFrameList = cmds.keyframe(obj,at=attr,q=True)
                    frameBeNewEndFrame = offsetEndFrame - offsetValue
                    newEndFrameValue =  cmds.keyframe(obj,at=attr,t=(frameBeNewEndFrame,frameBeNewEndFrame),q=True,eval=True)[0]
                    frameBeNewStartFrame = frameBeNewEndFrame +1
                    newStartFrameValue =  cmds.keyframe(obj,at=attr,t=(frameBeNewStartFrame,frameBeNewStartFrame),q=True,eval=True)[0]

                        
               #     divideFrame = offsetEndFrame - offsetValue
                   # modOffsetStepPreKeyFrame = float(offsetEndFrame - offsetValue -0.01)
                  #  modOffsetStepPosteKeyFrame = float(offsetEndFrame - offsetValue+0.01)
                   # divideFrameValue = cmds.keyframe(obj,at=attr,t=(divideFrame,divideFrame),q=True,eval=True)[0]
                 #   postKeyFrameValue = cmds.keyframe(obj,at=attr,t=(divideFrame,divideFrame),q=True,eval=True)[0]
                    #cmds.setKeyframe(obj, t=[modOffsetStepPreKeyFrame,modOffsetStepPreKeyFrame], at=attr,v=divideFrameValue )

                   # cmds.setKeyframe(obj, t=[modOffsetStepPosteKeyFrame,modOffsetStepPosteKeyFrame], at=attr,v=divideFrameValue )
                    
                 #   cmds.setKeyframe(obj, t=[divideFrame,divideFrame], at=attr,v=divideFrameValue )

   
                except:
                    pass


               # print "keyFrameList",keyFrameList
                
                try:
                    keyFrameLength =  float(keyFrameList[-1]-keyFrameList[0]+1.0)
                    startFrame = float(keyFrameList[0])
                   # print "%.2f"%keyFrameLength
                    endFrame = float(keyFrameList[-1])
                    
                    
                #    print startFrame,endFrame
                                    
                    for i in keyFrameList:
                        getValue = float(cmds.keyframe(obj,at= attr,time=(i,i) ,query=True,ev=True)[0])

                        keyValueDict.update({"%.2f"%i:"%.2f"%getValue})
                        
                        

       

                        
                    for i in keyFrameList:
                        totalValue = float(i + offsetValue)
                        
                        if totalValue <= offsetEndFrame:
                            
                            newKey = totalValue
                          #  print "aaa"
                        else:
                            newKey = totalValue -offsetEndFrame + offsetStartFrame -1
                            
                      #  if i == 
                      #  print "newKey",keyFrameLength,i,newKey
                        #newKey = 
                        offsetKeyFrameDict.update({"%.2f"%i:"%.2f"%newKey})
                    
   
                    
                except:
                    keyFrameLength = 0
                    
                    
                try:#clear key in channel
                    print "clear key"
                    cmds.cutKey( obj, time=(keyFrameList[0],keyFrameList[-1]), attribute=attr, option="keys" )
                except:
                    pass
             #   print "offsetKeyFrameDict",offsetKeyFrameDict

               # print keyFrameList[0]

                try:
                    for key in keyFrameList:
                        offsetKey = float(offsetKeyFrameDict["%.2f"%key])
                      #  print key,offsetKey ,type(offsetKey),type("%.2f"%key)
                        setValue = float(keyValueDict["%.2f"%key])
                      #  print key,offsetKey,setValue ,type(setValue),attr,obj
                        cmds.setKeyframe(obj,v=setValue,at=attr,time=(offsetKey,offsetKey))
                     #   print "done"
                    cmds.setKeyframe(obj,v=startFrameValue,at=attr,time=(divideStepFrame,divideStepFrame))
                    cmds.setKeyframe(obj,v=newEndFrameValue,at=attr,time=(offsetEndFrame,offsetEndFrame))
                    cmds.setKeyframe(obj,v=newStartFrameValue,at=attr,time=(offsetStartFrame,offsetStartFrame))

                except:
                    pass
             #   print attr,keyFrameLength,keyFrameList

                    
    def getObjList(self):
        
        objList = cmds.ls(sl=True)
        
        return objList
        

    def getItems(self):
        
       # print self.checkBox_allzero.isChecked()
        objList = cmds.ls(sl=True)
        for obj in objList:
           # print obj
            self.cycleKeys(obj)
        
        
    def cycleKeys(self,obj):
        print obj
        offsetIn = float(self.lineEdit_sf.text())
        offsetOut = float(self.lineEdit_ef.text())
        repeatTimes = int(self.lineEdit_rt.text())
        keyAbleAttList= ["translateX","translateY","translateZ","rotateX","rotateY","rotateZ","scaleX","scaleY","scaleZ"]
        
        if self.checkBox_allzero.isChecked() == True:
            for attr in keyAbleAttList :
                keyFrameList = cmds.keyframe(obj,at=attr,q=True)
                preStartFrame = float(keyFrameList[0]) - 0.01
                postEndFrame = float(keyFrameList[-1]) + 0.01
                cmds.setKeyframe(obj,v=0,at=attr,time=(preStartFrame,preStartFrame))
                cmds.setKeyframe(obj,v=0,at=attr,time=(postEndFrame,postEndFrame))
                #print attr,preStartFrame,postEndFrame
                print attr,keyFrameList
                
            
        
        for attr in keyAbleAttList:
            keyFrameList = cmds.keyframe(obj,at=attr,q=True)
            startKeyFrame = keyFrameList[0]
            endKeyFrame = keyFrameList[-1]
            offsetRange = offsetOut -offsetIn +1
           # print attr,keyFrameList,startKeyFrame,endKeyFrame
            for i in range(0,repeatTimes):
                for j in keyFrameList:
                    frame = i*offsetRange + j
                   # print"attr",attr, i*offsetRange + j
                    getValue = float(cmds.keyframe(obj,at= attr,time=(j,j) ,query=True,ev=True)[0])
                    cmds.setKeyframe(obj,v=getValue,at=attr,time=(frame,frame))
                    print getValue
        
    
        

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


 