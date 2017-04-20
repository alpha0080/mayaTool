# -*- coding: utf-8 -*-
#
# Form implementation generated from reading ui file 'C:/Users/alpha/Documents/GitHub/mayaTool/particleInstanceTool/particleinstancetool_01.ui'
#
# by alpha
#
# particleInstanceTool V0.9
#avarageNx
#



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
        MainWindow.resize(476, 668)
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
        self.label_copyMode = QtWidgets.QLabel(self.centralwidget)
        self.label_copyMode.setGeometry(QtCore.QRect(10, 210, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        font.setItalic(True)
        self.label_copyMode.setFont(font)
        self.label_copyMode.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_copyMode.setObjectName("label_copyMode")
        self.pushButton_create = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create.setGeometry(QtCore.QRect(30, 590, 421, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.pushButton_create.setFont(font)
        self.pushButton_create.setObjectName("pushButton_create")
        self.label_copyMode_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_copyMode_3.setGeometry(QtCore.QRect(0, 260, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        font.setItalic(True)
        self.label_copyMode_3.setFont(font)
        self.label_copyMode_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_copyMode_3.setObjectName("label_copyMode_3")
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
        self.label_multiple.setGeometry(QtCore.QRect(140, 388, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.label_multiple.setFont(font)
        self.label_multiple.setAlignment(QtCore.Qt.AlignCenter)
        self.label_multiple.setObjectName("label_multiple")
        self.lineEdit_multiple = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_multiple.setGeometry(QtCore.QRect(400, 398, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.lineEdit_multiple.setFont(font)
        self.lineEdit_multiple.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_multiple.setReadOnly(False)
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
        self.horizontalSlider_multiPly.setGeometry(QtCore.QRect(30, 400, 361, 20))
        self.horizontalSlider_multiPly.setMinimum(1)
        self.horizontalSlider_multiPly.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_multiPly.setObjectName("horizontalSlider_multiPly")
        self.lineEdit_randomScale = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_randomScale.setGeometry(QtCore.QRect(400, 520, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.lineEdit_randomScale.setFont(font)
        self.lineEdit_randomScale.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_randomScale.setReadOnly(False)
        self.lineEdit_randomScale.setObjectName("lineEdit_randomScale")
        self.horizontalSlider_randomScale = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_randomScale.setEnabled(True)
        self.horizontalSlider_randomScale.setGeometry(QtCore.QRect(30, 522, 361, 20))
        self.horizontalSlider_randomScale.setMinimum(0)
        self.horizontalSlider_randomScale.setMaximum(1000)
        self.horizontalSlider_randomScale.setSingleStep(1)
        self.horizontalSlider_randomScale.setPageStep(10)
        self.horizontalSlider_randomScale.setSliderPosition(1)
        self.horizontalSlider_randomScale.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_randomScale.setObjectName("horizontalSlider_randomScale")
        self.label_randomScale = QtWidgets.QLabel(self.centralwidget)
        self.label_randomScale.setGeometry(QtCore.QRect(140, 510, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.label_randomScale.setFont(font)
        self.label_randomScale.setAlignment(QtCore.Qt.AlignCenter)
        self.label_randomScale.setObjectName("label_randomScale")
        self.lineEdit_randomPosition = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_randomPosition.setGeometry(QtCore.QRect(400, 430, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.lineEdit_randomPosition.setFont(font)
        self.lineEdit_randomPosition.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_randomPosition.setReadOnly(False)
        self.lineEdit_randomPosition.setObjectName("lineEdit_randomPosition")
        self.horizontalSlider_randomPosition = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_randomPosition.setGeometry(QtCore.QRect(30, 432, 361, 20))
        self.horizontalSlider_randomPosition.setMinimum(-1000)
        self.horizontalSlider_randomPosition.setMaximum(1000)
        self.horizontalSlider_randomPosition.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_randomPosition.setObjectName("horizontalSlider_randomPosition")
        self.label_randomPosition = QtWidgets.QLabel(self.centralwidget)
        self.label_randomPosition.setGeometry(QtCore.QRect(140, 420, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.label_randomPosition.setFont(font)
        self.label_randomPosition.setAlignment(QtCore.Qt.AlignCenter)
        self.label_randomPosition.setObjectName("label_randomPosition")
        self.lineEdit_randomRotation = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_randomRotation.setGeometry(QtCore.QRect(400, 490, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.lineEdit_randomRotation.setFont(font)
        self.lineEdit_randomRotation.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_randomRotation.setReadOnly(False)
        self.lineEdit_randomRotation.setObjectName("lineEdit_randomRotation")
        self.horizontalSlider_randomRotation = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_randomRotation.setGeometry(QtCore.QRect(30, 492, 361, 20))
        self.horizontalSlider_randomRotation.setMinimum(0)
        self.horizontalSlider_randomRotation.setMaximum(360)
        self.horizontalSlider_randomRotation.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_randomRotation.setObjectName("horizontalSlider_randomRotation")
        self.label_randomRotation = QtWidgets.QLabel(self.centralwidget)
        self.label_randomRotation.setGeometry(QtCore.QRect(140, 480, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.label_randomRotation.setFont(font)
        self.label_randomRotation.setAlignment(QtCore.Qt.AlignCenter)
        self.label_randomRotation.setObjectName("label_randomRotation")
        self.lineEdit_spread = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_spread.setEnabled(False)
        self.lineEdit_spread.setGeometry(QtCore.QRect(400, 460, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.lineEdit_spread.setFont(font)
        self.lineEdit_spread.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_spread.setReadOnly(True)
        self.lineEdit_spread.setObjectName("lineEdit_spread")
        self.horizontalSlider_spread = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_spread.setEnabled(False)
        self.horizontalSlider_spread.setGeometry(QtCore.QRect(30, 462, 361, 20))
        self.horizontalSlider_spread.setMinimum(0)
        self.horizontalSlider_spread.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_spread.setObjectName("horizontalSlider_spread")
        self.label_spread = QtWidgets.QLabel(self.centralwidget)
        self.label_spread.setEnabled(False)
        self.label_spread.setGeometry(QtCore.QRect(140, 450, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.label_spread.setFont(font)
        self.label_spread.setAlignment(QtCore.Qt.AlignCenter)
        self.label_spread.setObjectName("label_spread")
        self.label_offset = QtWidgets.QLabel(self.centralwidget)
        self.label_offset.setEnabled(True)
        self.label_offset.setGeometry(QtCore.QRect(140, 540, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.label_offset.setFont(font)
        self.label_offset.setAlignment(QtCore.Qt.AlignCenter)
        self.label_offset.setObjectName("label_offset")
        self.lineEdit_offset = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_offset.setEnabled(True)
        self.lineEdit_offset.setGeometry(QtCore.QRect(400, 550, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.lineEdit_offset.setFont(font)
        self.lineEdit_offset.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_offset.setReadOnly(True)
        self.lineEdit_offset.setObjectName("lineEdit_offset")
        self.horizontalSlider_offset = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_offset.setEnabled(True)
        self.horizontalSlider_offset.setGeometry(QtCore.QRect(30, 552, 361, 20))
        self.horizontalSlider_offset.setMinimum(-1000)
        self.horizontalSlider_offset.setMaximum(1000)
        self.horizontalSlider_offset.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_offset.setObjectName("horizontalSlider_offset")
        self.checkBox_exportJson = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_exportJson.setEnabled(False)
        self.checkBox_exportJson.setGeometry(QtCore.QRect(30, 330, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.checkBox_exportJson.setFont(font)
        self.checkBox_exportJson.setObjectName("checkBox_exportJson")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 230, 189, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_duplicate = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.radioButton_duplicate.setFont(font)
        self.radioButton_duplicate.setChecked(True)
        self.radioButton_duplicate.setObjectName("radioButton_duplicate")
        self.horizontalLayout.addWidget(self.radioButton_duplicate)
        self.radioButton_instance = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.radioButton_instance.setFont(font)
        self.radioButton_instance.setObjectName("radioButton_instance")
        self.horizontalLayout.addWidget(self.radioButton_instance)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 280, 191, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_alwaysTop = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.radioButton_alwaysTop.setFont(font)
        self.radioButton_alwaysTop.setObjectName("radioButton_alwaysTop")
        self.horizontalLayout_2.addWidget(self.radioButton_alwaysTop)
        self.radioButton_normal = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.radioButton_normal.setFont(font)
        self.radioButton_normal.setChecked(True)
        self.radioButton_normal.setObjectName("radioButton_normal")
        self.horizontalLayout_2.addWidget(self.radioButton_normal)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 350, 441, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(401, 369, 51, 21))
        self.toolButton.setObjectName("toolButton")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(32, 374, 360, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize-2)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
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
        self.label_copyMode.setText(QtWidgets.QApplication.translate("MainWindow", "copy Mode", None, -1))
        self.pushButton_create.setText(QtWidgets.QApplication.translate("MainWindow", "create", None, -1))
        self.label_copyMode_3.setText(QtWidgets.QApplication.translate("MainWindow", "aim Mode", None, -1))
        self.label_multiple.setText(QtWidgets.QApplication.translate("MainWindow", "multiply", None, -1))
        self.lineEdit_multiple.setText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.pushButton_getSurfaceMesh.setText(QtWidgets.QApplication.translate("MainWindow", "get surface Mesh", None, -1))
        self.pushButton_clearList.setText(QtWidgets.QApplication.translate("MainWindow", "clear List", None, -1))
        self.lineEdit_randomScale.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.label_randomScale.setText(QtWidgets.QApplication.translate("MainWindow", "random Scale", None, -1))
        self.lineEdit_randomPosition.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.label_randomPosition.setText(QtWidgets.QApplication.translate("MainWindow", "random Position", None, -1))
        self.lineEdit_randomRotation.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.label_randomRotation.setText(QtWidgets.QApplication.translate("MainWindow", "random Rotation", None, -1))
        self.lineEdit_spread.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.label_spread.setText(QtWidgets.QApplication.translate("MainWindow", "spread", None, -1))
        self.label_offset.setText(QtWidgets.QApplication.translate("MainWindow", "offset", None, -1))
        self.lineEdit_offset.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.checkBox_exportJson.setText(QtWidgets.QApplication.translate("MainWindow", "export data to .json", None, -1))
        self.radioButton_duplicate.setText(QtWidgets.QApplication.translate("MainWindow", "duplicate", None, -1))
        self.radioButton_instance.setText(QtWidgets.QApplication.translate("MainWindow", "instance", None, -1))
        self.radioButton_alwaysTop.setText(QtWidgets.QApplication.translate("MainWindow", "always Top", None, -1))
        self.radioButton_normal.setText(QtWidgets.QApplication.translate("MainWindow", "normal", None, -1))
        self.toolButton.setText(QtWidgets.QApplication.translate("MainWindow", "reset", None, -1))





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
        self.pushButton_clearList.clicked.connect(self.clickButton_clearList)
        
        self.toolButton.clicked.connect(self.clickButton_reset)
        
        #slide_1
        self.horizontalSlider_multiPly.valueChanged.connect(self.change_Multiply)
        self.lineEdit_multiple.textChanged.connect(self.change_MultiplyText)
        #slide_2
        self.horizontalSlider_randomPosition.valueChanged.connect(self.change_randomPosition)
        self.lineEdit_randomPosition.textChanged.connect(self.change_randomPositionText)
        #slide_3
        self.horizontalSlider_spread.valueChanged.connect(self.change_spread)
        #slide_4
        self.horizontalSlider_randomRotation.valueChanged.connect(self.change_randomRotation)
        self.lineEdit_randomRotation.textChanged.connect(self.change_randomRotationText)

        #slide_5
        self.horizontalSlider_randomScale.valueChanged.connect(self.change_randomScale)
        self.lineEdit_randomScale.textChanged.connect(self.change_randomScaleText)

        #slide_6
        self.horizontalSlider_offset.valueChanged.connect(self.change_offset)
        self.lineEdit_offset.textChanged.connect(self.change_offsetText)


        self.radioButton_duplicate.setChecked(True)
        self.radioButton_normal.setChecked(True)
        
    def clickButton_reset(self):
        
        self.radioButton_duplicate.setChecked(True)
        self.radioButton_normal.setChecked(True)
        self.horizontalSlider_multiPly.setValue(1)
        self.horizontalSlider_randomPosition.setValue(0)
        self.horizontalSlider_spread.setValue(0)
        self.horizontalSlider_randomRotation.setValue(0)
        self.horizontalSlider_randomScale.setValue(0)
        self.horizontalSlider_offset.setValue(0)
        
        
    #slide_1    
    def change_Multiply(self):
        getMultiplyValue = self.horizontalSlider_multiPly.value()
        self.lineEdit_multiple.setText(str(getMultiplyValue))
        
    def change_MultiplyText(self):
        getMultiplyValue = int(self.lineEdit_multiple.text())
        self.horizontalSlider_multiPly.setValue(getMultiplyValue)
        
        
        
    #slide_2
    def change_randomPosition(self):
        getrandomPositionValue = float(self.horizontalSlider_randomPosition.value())/(100.0)
        self.lineEdit_randomPosition.setText(str(getrandomPositionValue))
        
    def change_randomPositionText(self):
        getrandomPositionValue = float(self.lineEdit_randomPosition.text())*(100.0)
        self.horizontalSlider_randomPosition.setValue(int(getrandomPositionValue))
        
    #slide_3

    def change_spread(self):
        getspreadValue = self.horizontalSlider_spread.value()
        self.lineEdit_spread.setText(str(getspreadValue))
    #slide_4
    def change_randomRotation(self):
        getrandomRotationValue = self.horizontalSlider_randomRotation.value()
        self.lineEdit_randomRotation.setText(str(getrandomRotationValue))
        
        
    def change_randomRotationText(self):
        getrandomRotationValue = float(self.lineEdit_randomRotation.text())
        self.horizontalSlider_randomRotation.setValue(getrandomRotationValue)
                
        
        
    #slide_5
    def change_randomScale(self):
        getrandomScaleValue = float(self.horizontalSlider_randomScale.value())/(100.0)
        print getrandomScaleValue
        self.lineEdit_randomScale.setText(str(getrandomScaleValue))
    
    def change_randomScaleText(self):
        getrandomScaleValue = int(float(self.lineEdit_randomScale.text())*(100.0))
        self.horizontalSlider_randomScale.setValue(getrandomScaleValue)
            
        
               
        
        
        
        
    #slide_6
    def change_offset(self):
        getoffsetValue = float(self.horizontalSlider_offset.value()/(100.0))
        self.lineEdit_offset.setText(str(getoffsetValue))
    
    def change_offsetText(self):
        getoffsetValue = int(float(self.lineEdit_offset.text())*(100.0))
        self.horizontalSlider_offset.setValue(getoffsetValue)
            



        
    def clickButton_getSurfaceMesh(self):
        print" get the surface,that take form other scenes"
        self.selectMesh = pm.ls(sl=True)[0].split('(')[0]
        self.lineEdit_getSurfaceMesh.setText(self.selectMesh)
        

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
           # if addObj in self.objList: #check if addObj in list
          #      pass
           # else:
            
            self.selectObjList.append(addObj)
            QtWidgets.QListWidgetItem(self.listWidget_objList)
            itemCount = i + objCount
            itemName = selectObjs[i].split('(')[0]
            self.listWidget_objList.item(itemCount).setText(QtWidgets.QApplication.translate("MainWindow","tempName", None, -1))
            self.listWidget_objList.item(itemCount).setText(itemName)
        print self.selectObjList
        
       # QtWidgets.QListWidgetItem(self.listWidget_objList)

       # self.listWidget_objList.item(0).setText(QtWidgets.QApplication.translate("MainWindow", "aaa", None, -1))
    
    def clickButton_clearList(self):
        self.listWidget_objList.clear()
        self.objList = []
        self.selectObjList = []
        

    def getVertexNormal(self):
        geo = pm.PyNode(self.selectMesh)
       # print geo
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
       # print closestVertex,closeVertexNormal,len(closeVertexNormal)


        try:
            self.avarageNx =( closeVertexNormal[0] + closeVertexNormal[3] + closeVertexNormal[6]  + closeVertexNormal[9] )/4
            self.avarageNy =( closeVertexNormal[1] + closeVertexNormal[4] + closeVertexNormal[7]  + closeVertexNormal[10] )/4
            self.avarageNz =( closeVertexNormal[2] + closeVertexNormal[5] + closeVertexNormal[8]  + closeVertexNormal[11] )/4
        except:
            pass
            
        #print self.avarageNx,self.avarageNy,self.avarageNz







    def clickButtin_createInstance(self):
        sourceObjCount = len(self.selectObjList)
        particlePositionDict={}
        self.allInstanceList=[]
        #print "particle",self.selectParticleStr
        bb=cmds.xform('%s'%self.selectParticleStr,bb=True,q=True)
        bbMaxDistance = math.sqrt(((bb[3]-bb[0]) *(bb[3]-bb[0])) + ((bb[4]-bb[1]) *(bb[4]-bb[1])) +((bb[5]-bb[2]) *(bb[5]-bb[2])))
        #print bbMaxDistance
        emptyGrp = pm.createNode('transform', n='%s_instanceGrp'%self.selectParticleStr )
        self.totalParticleCount = pm.nParticle('%s'%self.selectParticleStr, query=True, ct=True)
        #print 'totalParticleCount',totalParticleCount
        multiplyNum= int(self.lineEdit_multiple.text())
        
        
        scaleMultiPly = (float(self.lineEdit_randomScale.text())/(1.0))
        randomPosition = float(self.lineEdit_randomPosition.text())
        randomRotation = float(self.lineEdit_randomRotation.text())
        offsetValue = float(self.lineEdit_offset.text())
        print "multiply",multiplyNum
        print "spread",self.lineEdit_spread.text()
        print "scale", self.lineEdit_randomScale.text()
        print "position",self.lineEdit_randomPosition.text()
        print "rotation",self.lineEdit_randomRotation.text()
        print "offset",self.lineEdit_offset.text()
        

        countGetValue = 0
        for n in range(0,self.totalParticleCount):
            

            perParticle = self.selectParticleStr.pt[n]  
            #print perParticle


            self.positionPP = pm.getParticleAttr(perParticle, at='position',a=True)
            
            self.getVertexNormal()  

            self.positionPP.append(self.avarageNx)
            
            self.positionPP.append(self.avarageNy)
            
            self.positionPP.append(self.avarageNz)
            

            particlePositionDict.update({str(n):self.positionPP})
            countGetValue = countGetValue +1
            processPresentValue = int(((float(countGetValue)/float(self.totalParticleCount))/2.0)*100.0)
           # print processPresentValue
            self.progressBar.setValue(processPresentValue)
        print "get all data from particle"
            
       # print particlePositionDict
        countSetObj =0
        for n in range(0,self.totalParticleCount):
            countSetObj = countSetObj +1
            processPresentValue = int(((float(countSetObj)/float(self.totalParticleCount))/(2.0) + 0.5)*100.0)
           # print processPresentValue
           # self.progressBar.value(processPresentValue)
            self.progressBar.setValue(processPresentValue)

            for k in range(0,multiplyNum):
                #print n,k
                randMovement = random.uniform((-randomPosition),randomPosition)
                sourceObj = self.selectObjList[random.randint(0,(sourceObjCount-1))] #get random obj index
                newName = self.selectParticleStr+'_instanceObj' +'_'+ str(n)+'_'+str(k)
                self.allInstanceList.append(newName)
                #print allInstanceList 
                #print newName
                #self.totalParticleCount
                #randomRotation = random.uniform(-randomRotation,randomRotation)

                randomScale = 1 * (random.uniform( (1.0-scaleMultiPly),(1.0+scaleMultiPly)))
                if self.radioButton_duplicate.isChecked() == True:

                    newInstanceObj = cmds.duplicate( sourceObj, n=newName,rc=True,rr=True )
                else:

                    newInstanceObj = cmds.instance( sourceObj, n=newName )
                #random position
                pm.parent(newInstanceObj,emptyGrp)



                if self.lineEdit_randomPosition.text() == "0":
                    moveX = particlePositionDict[str(n)][0]                
                    moveY = particlePositionDict[str(n)][1]                 
                    moveZ = particlePositionDict[str(n)][2] 
                    cmds.setAttr( "%s.translateX"%newName,moveX)
                    cmds.setAttr( "%s.translateY"%newName,moveY)
                    cmds.setAttr( "%s.translateZ"%newName,moveZ)
                   # cmds.setAttr( "%s.rotateY"%newName,randomRotation)
                    #print moveX,moveY,moveZ
                else:
                    #randMoveX = particlePositionDict[str(n)][0] + randMovement/bbMaxDistance
                                        
                    #if self.lineEdit_offset.text() == "0":
                       # randMoveY = particlePositionDict[str(n)][1] 
                    #else:                      
                       # randMoveY = particlePositionDict[str(n)][1] + float(self.lineEdit_offset.text())
                    moveY = particlePositionDict[str(n)][1]
                    #randMoveY = particlePositionDict[str(n)][1] 
                    #randMoveZ = particlePositionDict[str(n)][2] + randMovement/bbMaxDistance               
                    #print randMoveX,randMoveY,randMoveZ
                    cmds.setAttr( "%s.translateX"%newName,(particlePositionDict[str(n)][0] +random.uniform(-float(self.lineEdit_randomPosition.text()),float(self.lineEdit_randomPosition.text()))))

                    cmds.setAttr( "%s.translateY"%newName,moveY)
                    cmds.setAttr( "%s.translateZ"%newName,(particlePositionDict[str(n)][2] +random.uniform(-float(self.lineEdit_randomPosition.text()),float(self.lineEdit_randomPosition.text()))))
                    
                    #cmds.setAttr( "%s.rotateY"%newName,randomRotation)

                    #(particlePositionDict[str(n)][0] +random.uniform(float(self.lineEdit_randomPosition.text())))

                if self.lineEdit_randomScale.text() == "0":
                    pass
                else:
                    cmds.setAttr( "%s.scaleX"%newName,randomScale)
                    cmds.setAttr( "%s.scaleZ"%newName,randomScale)
                    
                    
                #random rotate

                if self.radioButton_normal.isChecked() == True: 

                    rotateNormalx = particlePositionDict[str(n)][3]
                    rotateNormaly = particlePositionDict[str(n)][4]
                    rotateNormalz = particlePositionDict[str(n)][5]  
                    
                    
                    rotX = math.degrees(math.atan2(rotateNormaly,rotateNormalz))
                    rotY = math.degrees(math.atan2(rotateNormalx,rotateNormalz))

                    rotZ = math.degrees(math.pi/2-math.asin(rotateNormaly))

                    #print n,'rotX',rotX
                    #print n,'rotY',rotY
                    #print n,'rotZ',rotZ
                    randRotValue = float(self.lineEdit_randomRotation.text())

 
                    cmds.setAttr( "%s.rotateX"%newName,(rotZ+random.uniform(-randRotValue,randRotValue)))
                    cmds.setAttr( "%s.rotateY"%newName,(rotY+random.uniform(-randRotValue,randRotValue)))

                   # cmds.setAttr( "%s.rotateY"%newName,randRotValue) 
                    #self.returnProcessPersent()
                else:
                    pass
                if self.lineEdit_offset.text() == "0":
                    pass
                else:
                    originalTranslateY = cmds.getAttr("%s.translateY"%newName)
                    moveY = originalTranslateY + offsetValue
                    cmds.setAttr( "%s.translateY"%newName,moveY)


                    

    def returnProcessPersent(self):
        self.processUnitValue = self.processUnitValue + self.processUnitValue

        
        self.progressBar.value(int(self.processUnitValue))
                

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


 