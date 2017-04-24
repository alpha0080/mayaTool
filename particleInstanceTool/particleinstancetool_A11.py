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
import random ,math, os,json
import maya.OpenMaya as OpenMaya
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        self.setFontSize=5
        #setPointSize(11) = setPointSize(self.setFontSize +3)
        #setPointSize(10) = setPointSize(self.setFontSize +2)
        #setPointSize(self.setFontSize) = setPointSize(self.setFontSize) 

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(457, 811)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 10, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit_particleCount = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_particleCount.setGeometry(QtCore.QRect(310, 10, 61, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        self.lineEdit_particleCount.setFont(font)
        self.lineEdit_particleCount.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_particleCount.setReadOnly(True)
        self.lineEdit_particleCount.setObjectName("lineEdit_particleCount")
        self.pushButton_create = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create.setGeometry(QtCore.QRect(30, 748, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        self.pushButton_create.setFont(font)
        self.pushButton_create.setObjectName("pushButton_create")
        self.label_multiple = QtWidgets.QLabel(self.centralwidget)
        self.label_multiple.setGeometry(QtCore.QRect(140, 546, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        self.label_multiple.setFont(font)
        self.label_multiple.setAlignment(QtCore.Qt.AlignCenter)
        self.label_multiple.setObjectName("label_multiple")
        self.lineEdit_multiple = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_multiple.setGeometry(QtCore.QRect(381, 559, 51, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.lineEdit_multiple.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        self.lineEdit_multiple.setFont(font)
        self.lineEdit_multiple.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_multiple.setReadOnly(False)
        self.lineEdit_multiple.setObjectName("lineEdit_multiple")
        self.horizontalSlider_multiPly = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_multiPly.setGeometry(QtCore.QRect(30, 558, 341, 20))
        self.horizontalSlider_multiPly.setMinimum(1)
        self.horizontalSlider_multiPly.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_multiPly.setObjectName("horizontalSlider_multiPly")
        self.lineEdit_randomScale = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_randomScale.setGeometry(QtCore.QRect(381, 679, 51, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.lineEdit_randomScale.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        self.lineEdit_randomScale.setFont(font)
        self.lineEdit_randomScale.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_randomScale.setReadOnly(False)
        self.lineEdit_randomScale.setObjectName("lineEdit_randomScale")
        self.horizontalSlider_randomScale = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_randomScale.setEnabled(True)
        self.horizontalSlider_randomScale.setGeometry(QtCore.QRect(30, 680, 341, 20))
        self.horizontalSlider_randomScale.setMinimum(-100)
        self.horizontalSlider_randomScale.setMaximum(100)
        self.horizontalSlider_randomScale.setSingleStep(0)
        self.horizontalSlider_randomScale.setPageStep(10)
        self.horizontalSlider_randomScale.setSliderPosition(1)
        self.horizontalSlider_randomScale.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_randomScale.setObjectName("horizontalSlider_randomScale")
        self.label_randomScale = QtWidgets.QLabel(self.centralwidget)
        self.label_randomScale.setGeometry(QtCore.QRect(140, 668, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        self.label_randomScale.setFont(font)
        self.label_randomScale.setAlignment(QtCore.Qt.AlignCenter)
        self.label_randomScale.setObjectName("label_randomScale")
        self.lineEdit_randomPosition = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_randomPosition.setGeometry(QtCore.QRect(381, 589, 51, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.lineEdit_randomPosition.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        self.lineEdit_randomPosition.setFont(font)
        self.lineEdit_randomPosition.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_randomPosition.setReadOnly(False)
        self.lineEdit_randomPosition.setObjectName("lineEdit_randomPosition")
        self.horizontalSlider_randomPosition = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_randomPosition.setGeometry(QtCore.QRect(30, 590, 341, 20))
        self.horizontalSlider_randomPosition.setMinimum(0)
        self.horizontalSlider_randomPosition.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_randomPosition.setObjectName("horizontalSlider_randomPosition")
        self.label_randomPosition = QtWidgets.QLabel(self.centralwidget)
        self.label_randomPosition.setGeometry(QtCore.QRect(140, 578, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        self.label_randomPosition.setFont(font)
        self.label_randomPosition.setAlignment(QtCore.Qt.AlignCenter)
        self.label_randomPosition.setObjectName("label_randomPosition")
        self.lineEdit_randomRotation = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_randomRotation.setGeometry(QtCore.QRect(381, 649, 51, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.lineEdit_randomRotation.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        self.lineEdit_randomRotation.setFont(font)
        self.lineEdit_randomRotation.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_randomRotation.setReadOnly(False)
        self.lineEdit_randomRotation.setObjectName("lineEdit_randomRotation")
        self.horizontalSlider_randomRotation = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_randomRotation.setGeometry(QtCore.QRect(30, 650, 341, 20))
        self.horizontalSlider_randomRotation.setMinimum(0)
        self.horizontalSlider_randomRotation.setMaximum(360)
        self.horizontalSlider_randomRotation.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_randomRotation.setObjectName("horizontalSlider_randomRotation")
        self.label_randomRotation = QtWidgets.QLabel(self.centralwidget)
        self.label_randomRotation.setGeometry(QtCore.QRect(140, 638, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        self.label_randomRotation.setFont(font)
        self.label_randomRotation.setAlignment(QtCore.Qt.AlignCenter)
        self.label_randomRotation.setObjectName("label_randomRotation")
        self.lineEdit_spread = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_spread.setEnabled(False)
        self.lineEdit_spread.setGeometry(QtCore.QRect(381, 619, 51, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.lineEdit_spread.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        self.lineEdit_spread.setFont(font)
        self.lineEdit_spread.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_spread.setReadOnly(True)
        self.lineEdit_spread.setObjectName("lineEdit_spread")
        self.horizontalSlider_spread = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_spread.setEnabled(False)
        self.horizontalSlider_spread.setGeometry(QtCore.QRect(30, 620, 341, 20))
        self.horizontalSlider_spread.setMinimum(0)
        self.horizontalSlider_spread.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_spread.setObjectName("horizontalSlider_spread")
        self.label_spread = QtWidgets.QLabel(self.centralwidget)
        self.label_spread.setEnabled(False)
        self.label_spread.setGeometry(QtCore.QRect(140, 608, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        self.label_spread.setFont(font)
        self.label_spread.setAlignment(QtCore.Qt.AlignCenter)
        self.label_spread.setObjectName("label_spread")
        self.label_offset = QtWidgets.QLabel(self.centralwidget)
        self.label_offset.setEnabled(True)
        self.label_offset.setGeometry(QtCore.QRect(140, 698, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        self.label_offset.setFont(font)
        self.label_offset.setAlignment(QtCore.Qt.AlignCenter)
        self.label_offset.setObjectName("label_offset")
        self.lineEdit_offset = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_offset.setEnabled(True)
        self.lineEdit_offset.setGeometry(QtCore.QRect(381, 709, 51, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.lineEdit_offset.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        self.lineEdit_offset.setFont(font)
        self.lineEdit_offset.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_offset.setReadOnly(False)
        self.lineEdit_offset.setObjectName("lineEdit_offset")
        self.horizontalSlider_offset = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_offset.setEnabled(True)
        self.horizontalSlider_offset.setGeometry(QtCore.QRect(30, 710, 341, 20))
        self.horizontalSlider_offset.setMinimum(0)
        self.horizontalSlider_offset.setMaximum(5)
        self.horizontalSlider_offset.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_offset.setObjectName("horizontalSlider_offset")
        self.checkBox_exportToFile = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_exportToFile.setEnabled(True)
        self.checkBox_exportToFile.setGeometry(QtCore.QRect(30, 370, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        self.checkBox_exportToFile.setFont(font)
        self.checkBox_exportToFile.setObjectName("checkBox_exportToFile")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 506, 411, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(380, 520, 51, 21))
        self.toolButton.setObjectName("toolButton")
        self.lineEdit_errorMessage = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_errorMessage.setGeometry(QtCore.QRect(30, 314, 401, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.lineEdit_errorMessage.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        self.lineEdit_errorMessage.setFont(font)
        self.lineEdit_errorMessage.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_errorMessage.setReadOnly(True)
        self.lineEdit_errorMessage.setObjectName("lineEdit_errorMessage")
        self.pushButton_clearList = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clearList.setGeometry(QtCore.QRect(30, 141, 161, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        self.pushButton_clearList.setFont(font)
        self.pushButton_clearList.setObjectName("pushButton_clearList")
        self.listWidget_objList = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_objList.setGeometry(QtCore.QRect(200, 111, 231, 192))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.listWidget_objList.setPalette(palette)
        self.listWidget_objList.setObjectName("listWidget_objList")
        QtWidgets.QListWidgetItem(self.listWidget_objList)
        QtWidgets.QListWidgetItem(self.listWidget_objList)
        self.pushButton_addObbject = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_addObbject.setGeometry(QtCore.QRect(30, 111, 161, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_addObbject.sizePolicy().hasHeightForWidth())
        self.pushButton_addObbject.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        self.pushButton_addObbject.setFont(font)
        self.pushButton_addObbject.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_addObbject.setObjectName("pushButton_addObbject")
        self.pushButton_getSurfaceMesh = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_getSurfaceMesh.setGeometry(QtCore.QRect(30, 41, 161, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_getSurfaceMesh.sizePolicy().hasHeightForWidth())
        self.pushButton_getSurfaceMesh.setSizePolicy(sizePolicy)
        self.pushButton_getSurfaceMesh.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        self.pushButton_getSurfaceMesh.setFont(font)
        self.pushButton_getSurfaceMesh.setObjectName("pushButton_getSurfaceMesh")
        self.pushButton_getParticle = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_getParticle.setGeometry(QtCore.QRect(30, 71, 161, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        self.pushButton_getParticle.setFont(font)
        self.pushButton_getParticle.setObjectName("pushButton_getParticle")
        self.lineEdit_getSurfaceMesh = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_getSurfaceMesh.setGeometry(QtCore.QRect(200, 41, 231, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.lineEdit_getSurfaceMesh.setPalette(palette)
        self.lineEdit_getSurfaceMesh.setObjectName("lineEdit_getSurfaceMesh")
        self.lineEdit_sourceParticle = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sourceParticle.setGeometry(QtCore.QRect(200, 71, 231, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.lineEdit_sourceParticle.setPalette(palette)
        self.lineEdit_sourceParticle.setObjectName("lineEdit_sourceParticle")
        self.checkBox_inputFromFile = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_inputFromFile.setEnabled(True)
        self.checkBox_inputFromFile.setGeometry(QtCore.QRect(30, 390, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        self.checkBox_inputFromFile.setFont(font)
        self.checkBox_inputFromFile.setObjectName("checkBox_inputFromFile")
        self.lineEdit_exportFolder = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_exportFolder.setGeometry(QtCore.QRect(200, 370, 211, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.lineEdit_exportFolder.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        self.lineEdit_exportFolder.setFont(font)
        self.lineEdit_exportFolder.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_exportFolder.setReadOnly(True)
        self.lineEdit_exportFolder.setObjectName("lineEdit_exportFolder")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 303, 411, 15))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(20, 360, 411, 15))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.pushButton_addObbject_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_addObbject_2.setGeometry(QtCore.QRect(410, 370, 21, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_addObbject_2.sizePolicy().hasHeightForWidth())
        self.pushButton_addObbject_2.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(88, 130, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(88, 130, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(88, 130, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.pushButton_addObbject_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        self.pushButton_addObbject_2.setFont(font)
        self.pushButton_addObbject_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_addObbject_2.setObjectName("pushButton_addObbject_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 20, 47, 12))
        self.label.setObjectName("label")
        self.listWidget_fileList = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_fileList.setGeometry(QtCore.QRect(200, 390, 231, 121))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 62, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 62, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 62, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 62, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 62, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.listWidget_fileList.setPalette(palette)
        font = QtGui.QFont()
        font. setPointSize(self.setFontSize)
        self.listWidget_fileList.setFont(font)
        self.listWidget_fileList.setAlternatingRowColors(True)
        self.listWidget_fileList.setObjectName("listWidget_fileList")
        QtWidgets.QListWidgetItem(self.listWidget_fileList)
        QtWidgets.QListWidgetItem(self.listWidget_fileList)
        QtWidgets.QListWidgetItem(self.listWidget_fileList)
        QtWidgets.QListWidgetItem(self.listWidget_fileList)
        QtWidgets.QListWidgetItem(self.listWidget_fileList)
        self.pushButton_writeCache = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_writeCache.setGeometry(QtCore.QRect(30, 450, 161, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        self.pushButton_writeCache.setFont(font)
        self.pushButton_writeCache.setObjectName("pushButton_writeCache")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 524, 360, 12))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.progressBar.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_aimMode = QtWidgets.QLabel(self.centralwidget)
        self.label_aimMode.setGeometry(QtCore.QRect(30, 240, 154, 14))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        font.setItalic(True)
        self.label_aimMode.setFont(font)
        self.label_aimMode.setAlignment(QtCore.Qt.AlignCenter)
        self.label_aimMode.setObjectName("label_aimMode")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 259, 154, 29))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_normal = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        self.radioButton_normal.setFont(font)
        self.radioButton_normal.setChecked(True)
        self.radioButton_normal.setObjectName("radioButton_normal")
        self.horizontalLayout_2.addWidget(self.radioButton_normal)
        self.radioButton_alwaysTop = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        self.radioButton_alwaysTop.setFont(font)
        self.radioButton_alwaysTop.setObjectName("radioButton_alwaysTop")
        self.horizontalLayout_2.addWidget(self.radioButton_alwaysTop)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(30, 206, 154, 29))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_duplicate = QtWidgets.QRadioButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        self.radioButton_duplicate.setFont(font)
        self.radioButton_duplicate.setChecked(True)
        self.radioButton_duplicate.setObjectName("radioButton_duplicate")
        self.horizontalLayout.addWidget(self.radioButton_duplicate)
        self.radioButton_instance = QtWidgets.QRadioButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        self.radioButton_instance.setFont(font)
        self.radioButton_instance.setObjectName("radioButton_instance")
        self.horizontalLayout.addWidget(self.radioButton_instance)
        self.label_copyMode = QtWidgets.QLabel(self.centralwidget)
        self.label_copyMode.setGeometry(QtCore.QRect(30, 186, 154, 15))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        font.setItalic(True)
        self.label_copyMode.setFont(font)
        self.label_copyMode.setAlignment(QtCore.Qt.AlignCenter)
        self.label_copyMode.setObjectName("label_copyMode")
        self.pushButton_placeItemFromCache = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_placeItemFromCache.setGeometry(QtCore.QRect(30, 480, 161, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font. setPointSize(self.setFontSize)
        self.pushButton_placeItemFromCache.setFont(font)
        self.pushButton_placeItemFromCache.setObjectName("pushButton_placeItemFromCache")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "ParticleInstanceTool", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "total particles Count", None, -1))
        self.lineEdit_particleCount.setText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.pushButton_create.setText(QtWidgets.QApplication.translate("MainWindow", "create", None, -1))
        self.label_multiple.setText(QtWidgets.QApplication.translate("MainWindow", "multiply", None, -1))
        self.lineEdit_multiple.setText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
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
        self.checkBox_exportToFile.setText(QtWidgets.QApplication.translate("MainWindow", "export data to File", None, -1))
        self.toolButton.setText(QtWidgets.QApplication.translate("MainWindow", "reset", None, -1))
        self.pushButton_clearList.setText(QtWidgets.QApplication.translate("MainWindow", "clear List", None, -1))
        __sortingEnabled = self.listWidget_objList.isSortingEnabled()
        self.listWidget_objList.setSortingEnabled(False)
        self.listWidget_objList.item(0).setText(QtWidgets.QApplication.translate("MainWindow", "aaa", None, -1))
        self.listWidget_objList.item(1).setText(QtWidgets.QApplication.translate("MainWindow", "bbb", None, -1))
        self.listWidget_objList.setSortingEnabled(__sortingEnabled)
        self.pushButton_addObbject.setText(QtWidgets.QApplication.translate("MainWindow", "add Object into List", None, -1))
        self.pushButton_getSurfaceMesh.setText(QtWidgets.QApplication.translate("MainWindow", "get surface Mesh", None, -1))
        self.pushButton_getParticle.setText(QtWidgets.QApplication.translate("MainWindow", "get Source Partic ", None, -1))
        self.checkBox_inputFromFile.setText(QtWidgets.QApplication.translate("MainWindow", "input From File", None, -1))
        self.pushButton_addObbject_2.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Ver. 0.92", None, -1))
        __sortingEnabled = self.listWidget_fileList.isSortingEnabled()
        self.listWidget_fileList.setSortingEnabled(False)
        self.listWidget_fileList.item(0).setText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.listWidget_fileList.item(1).setText(QtWidgets.QApplication.translate("MainWindow", "2", None, -1))
        self.listWidget_fileList.item(2).setText(QtWidgets.QApplication.translate("MainWindow", "3", None, -1))
        self.listWidget_fileList.item(3).setText(QtWidgets.QApplication.translate("MainWindow", "4", None, -1))
        self.listWidget_fileList.item(4).setText(QtWidgets.QApplication.translate("MainWindow", "5", None, -1))
        self.listWidget_fileList.setSortingEnabled(__sortingEnabled)
        self.pushButton_writeCache.setText(QtWidgets.QApplication.translate("MainWindow", "write Cache", None, -1))
        self.label_aimMode.setText(QtWidgets.QApplication.translate("MainWindow", "aim Mode", None, -1))
        self.radioButton_normal.setText(QtWidgets.QApplication.translate("MainWindow", "normal", None, -1))
        self.radioButton_alwaysTop.setText(QtWidgets.QApplication.translate("MainWindow", "always Top", None, -1))
        self.radioButton_duplicate.setText(QtWidgets.QApplication.translate("MainWindow", "duplicate", None, -1))
        self.radioButton_instance.setText(QtWidgets.QApplication.translate("MainWindow", "instance", None, -1))
        self.label_copyMode.setText(QtWidgets.QApplication.translate("MainWindow", "copy Mode", None, -1))
        self.pushButton_placeItemFromCache.setText(QtWidgets.QApplication.translate("MainWindow", "place Item from Cache", None, -1))




class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #self.QTITEM.ACTION.connect(self.MODDEF)
        self.setupUi(self)
    #def self.MODDEF(self):
        #self.check_ExportToFile()
        
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

        # export ,input from file
        
        self.checkBox_exportToFile.stateChanged.connect(self.check_ExportToFile)
        self.checkBox_inputFromFile.stateChanged.connect(self.check_importFromFile)
        
        self.pushButton_writeCache.clicked.connect(self.clickButton_writeCache)
        self.listWidget_fileList.clicked.connect(self.clickListWidget_fileList)
        self.pushButton_placeItemFromCache.clicked.connect(self.placeItemFromCache)


        self.radioButton_duplicate.setChecked(True)
        self.radioButton_normal.setChecked(True)
        self.errorInstanceObj= []
        
    def clickListWidget_fileList(self):
        openFileName = self.listWidget_fileList.currentItem().text()
        self.oprnFileFullName =  self.exportFolder +'/' +openFileName
        
    def placeItemFromCache(self):
        
        dataName = open(oprnFileFullName,'r')
        self.particlePositionDict = json.load(dataName)   
        self.clickButtin_createInstanceFromCache()
        
    def check_ExportToFile(self):

        print"export to file"
        self.exportFolder = cmds.fileDialog2(fm=3)[0]
        self.lineEdit_exportFolder.setText(self.exportFolder)
        
        self.searchParticleJsonFolder()

        jsonFilesCount = len(self.fileList)
        self.listWidget_fileList.clear()
        fileReverseStored = sorted(self.fileList, reverse = True )
        for i in range(0,jsonFilesCount):
     
            QtWidgets.QListWidgetItem(self.listWidget_fileList)

            itemName = fileReverseStored[i].split('(')[0]
            self.listWidget_fileList.item(i).setText(QtWidgets.QApplication.translate("MainWindow","tempName", None, -1))
            self.listWidget_fileList.item(i).setText(itemName)
        
    def searchParticleJsonFolder(self):
        self.fileList = []
        self.verNumCountList = []
        print self.exportFolder
        allFileInDir = os.listdir(self.exportFolder)
        for file in allFileInDir:
            if file.split('.')[-1] == "json":
                self.fileList.append(file)
                self.verNumCountList.append(file.split('.')[-2].split('_')[-1].split('v')[1])
                #print file.split('.')[-2].split('_')[-1].split('v')[1]
        print self.fileList
        self.verNumSortList = sorted(self.verNumCountList)
       # jsonFilesCount
        
        
    def clickButton_writeCache(self):
        data = json.dumps(self.particlePositionDict, sort_keys=True , indent =4)

        self.searchParticleJsonFolder()
        if len(self.fileList) == 0:
            frameNum = 'v001'
            newJsonFileName = self.selectParticleStr +'_'+ frameNum+'.json'
            self.exportDataFile = self.exportFolder + '/' + newJsonFileName
            #data = "self.particlePositionDict"
            exportParticleDate = open(self.exportDataFile,'w')
            exportParticleDate.write(data)
            exportParticleDate.close
            QtWidgets.QListWidgetItem(self.listWidget_fileList)
            self.listWidget_fileList.item(0).setText(QtWidgets.QApplication.translate("MainWindow","tempName", None, -1))
            self.listWidget_fileList.item(0).setText(newJsonFileName)
            self.searchParticleJsonFolder()
        else:
            print self.verNumSortList
            lastVerNum = int(self.verNumSortList[-1])
            newVer = lastVerNum +1
            frameNum = 'v'+'%03d'%newVer
            #print frameNum
            newJsonFileName = self.selectParticleStr +'_'+ frameNum+'.json'
            self.exportDataFile = self.exportFolder + '/' + newJsonFileName
            print self.exportDataFile
            #print dataB
            exportParticleDate = open(self.exportDataFile,'w')
            exportParticleDate.write(data)
            exportParticleDate.close
            self.fileList
            itemIndexAdd = int(len(self.fileList)+1)
            print itemIndexAdd
            #jsonFilesCount = len(self.fileList)
            self.listWidget_fileList.clear()
            #print jsonFilesCount
            self.fileList.append(newJsonFileName)
            fileReverseStored = sorted(self.fileList, reverse = True )   
            #print fileReverseStored
            for i in range(0,itemIndexAdd):

                QtWidgets.QListWidgetItem(self.listWidget_fileList)

             #   itemName = fileList[i].split('(')[0]
                self.listWidget_fileList.item(i).setText(QtWidgets.QApplication.translate("MainWindow","tempName", None, -1))
                self.listWidget_fileList.item(i).setText(fileReverseStored[i])

           # json.dumps(dataName, sort_keys=True , indent =4)
        
    def check_importFromFile(self):
        print"import from file"
        
 
 
    
        
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
        #pm.select('pPlaneShape1.vtx[1785]')
            #aa=pm.ls(sl=True,fl=True)[0].split('(')[0]
            #print cmds.polyListComponentConversion(aa,fv=True, tf=True)
            #print len(cmds.polyListComponentConversion(aa,fv=True, tf=True))
        closeVertexNormal = pm.polyNormalPerVertex(closestVertex,q=1,xyz=1)
        #print closestVertex,len(closeVertexNormal),closeVertexNormal


        if len(closeVertexNormal) == 12:
            self.avarageNx =( closeVertexNormal[0] + closeVertexNormal[3] + closeVertexNormal[6]  + closeVertexNormal[9] )/4.0
            self.avarageNy =( closeVertexNormal[1] + closeVertexNormal[4] + closeVertexNormal[7]  + closeVertexNormal[10] )/4.0
            self.avarageNz =( closeVertexNormal[2] + closeVertexNormal[5] + closeVertexNormal[8]  + closeVertexNormal[11] )/4.0
        elif len(closeVertexNormal) == 6:
            self.avarageNx =( closeVertexNormal[0] + closeVertexNormal[3] )/2.0
            self.avarageNy =( closeVertexNormal[1] + closeVertexNormal[4] )/2.0
            self.avarageNz =( closeVertexNormal[2] + closeVertexNormal[5] )/2.0
        elif len(closeVertexNormal) == 3:
            self.avarageNx =( closeVertexNormal[0] )
            self.avarageNy =( closeVertexNormal[1] )
            self.avarageNz =( closeVertexNormal[2] )
        elif len(closeVertexNormal) == 12:
            self.avarageNx =( closeVertexNormal[0] + closeVertexNormal[3] + closeVertexNormal[6]  + closeVertexNormal[9] + closeVertexNormal[12] )/5.0
            self.avarageNy =( closeVertexNormal[1] + closeVertexNormal[4] + closeVertexNormal[7]  + closeVertexNormal[10] + closeVertexNormal[13] )/5.0
            self.avarageNz =( closeVertexNormal[2] + closeVertexNormal[5] + closeVertexNormal[8]  + closeVertexNormal[11] + closeVertexNormal[14] )/5.0
        else:
            pass  
          
            
        #print self.avarageNx,self.avarageNy,self.avarageNz allInstanceList

    def clickButtin_createInstanceFromCache(self):
        sourceObjCount = len(self.selectObjList)
        #self.particlePositionDict={}
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
                    moveX = self.particlePositionDict[str(n)][0]                
                    moveY = self.particlePositionDict[str(n)][1]                 
                    moveZ = self.particlePositionDict[str(n)][2] 
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
                    moveY = self.particlePositionDict[str(n)][1]
                    #randMoveY = particlePositionDict[str(n)][1] 
                    #randMoveZ = particlePositionDict[str(n)][2] + randMovement/bbMaxDistance               
                    #print randMoveX,randMoveY,randMoveZ
                    cmds.setAttr( "%s.translateX"%newName,(self.particlePositionDict[str(n)][0] +random.uniform(-float(self.lineEdit_randomPosition.text()),float(self.lineEdit_randomPosition.text()))))

                    cmds.setAttr( "%s.translateY"%newName,moveY)
                    cmds.setAttr( "%s.translateZ"%newName,(self.particlePositionDict[str(n)][2] +random.uniform(-float(self.lineEdit_randomPosition.text()),float(self.lineEdit_randomPosition.text()))))
                    
                    #cmds.setAttr( "%s.rotateY"%newName,randomRotation)

                    #(particlePositionDict[str(n)][0] +random.uniform(float(self.lineEdit_randomPosition.text())))

                if self.lineEdit_randomScale.text() == "0":
                    pass
                else:
                    cmds.setAttr( "%s.scaleX"%newName,randomScale)
                    cmds.setAttr( "%s.scaleZ"%newName,randomScale)
                    
                    
                #random rotate

                if self.radioButton_normal.isChecked() == True: 

                    rotateNormalx = self.particlePositionDict[str(n)][3]
                    rotateNormaly = self.particlePositionDict[str(n)][4]
                    rotateNormalz = self.particlePositionDict[str(n)][5]  
                    
                    
                    rotX = math.degrees(math.atan2(rotateNormaly,rotateNormalz))
                   # rotX = numpy.deg2rad(numpy.arctan2(rotateNormaly,rotateNormalz))
                    rotY = math.degrees(math.atan2(rotateNormalx,rotateNormalz))
                   # rotY = numpy.deg2rad(numpy.arctan2(rotateNormalx,rotateNormalz))

                    #rotZ = math.degrees((math.pi/(2.0))-math.asin(rotateNormaly))
                    try:
                        rotZ = math.degrees(1.57-math.asin(rotateNormaly))
                        #print "correct",rotateNormaly
                    except:
                        #print "error",rotateNormaly
                       # print math.asin(rotateNormaly)
                        rotZ = math.degrees(1.57-abs(math.asin(1.0)))
                        #print "%s"%newName + "   rotZ error"
                        self.errorInstanceObj.append(newName)
                        pass
                    #print n,'rotX',rotX
                    #print n,'rotY',rotY
                    #print n,'rotZ',rotZ
                    math.asin(-0.5)
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
        print self.errorInstanceObj
        #self.lineEdit_errorMessage.setText(self.errorInstanceObj)






    def clickButtin_createInstance(self):
        sourceObjCount = len(self.selectObjList)
        self.particlePositionDict={}
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
            
          #  try:
            self.getVertexNormal()  

            self.positionPP.append(self.avarageNx)
                
            self.positionPP.append(self.avarageNy)
            
            self.positionPP.append(self.avarageNz)
           # except:
             #   self.positionPP.append(0.0)
             #   self.positionPP.append(0.0)
             #   self.positionPP.append(0.0)
            

            self.particlePositionDict.update({str(n):self.positionPP})
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
                    moveX = self.particlePositionDict[str(n)][0]                
                    moveY = self.particlePositionDict[str(n)][1]                 
                    moveZ = self.particlePositionDict[str(n)][2] 
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
                    moveY = self.particlePositionDict[str(n)][1]
                    #randMoveY = particlePositionDict[str(n)][1] 
                    #randMoveZ = particlePositionDict[str(n)][2] + randMovement/bbMaxDistance               
                    #print randMoveX,randMoveY,randMoveZ
                    cmds.setAttr( "%s.translateX"%newName,(self.particlePositionDict[str(n)][0] +random.uniform(-float(self.lineEdit_randomPosition.text()),float(self.lineEdit_randomPosition.text()))))

                    cmds.setAttr( "%s.translateY"%newName,moveY)
                    cmds.setAttr( "%s.translateZ"%newName,(self.particlePositionDict[str(n)][2] +random.uniform(-float(self.lineEdit_randomPosition.text()),float(self.lineEdit_randomPosition.text()))))
                    
                    #cmds.setAttr( "%s.rotateY"%newName,randomRotation)

                    #(particlePositionDict[str(n)][0] +random.uniform(float(self.lineEdit_randomPosition.text())))

                if self.lineEdit_randomScale.text() == "0":
                    pass
                else:
                    cmds.setAttr( "%s.scaleX"%newName,randomScale)
                    cmds.setAttr( "%s.scaleZ"%newName,randomScale)
                    
                    
                #random rotate

                if self.radioButton_normal.isChecked() == True: 

                    rotateNormalx = self.particlePositionDict[str(n)][3]
                    rotateNormaly = self.particlePositionDict[str(n)][4]
                    rotateNormalz = self.particlePositionDict[str(n)][5]  
                    
                    
                    rotX = math.degrees(math.atan2(rotateNormaly,rotateNormalz))
                    rotY = math.degrees(math.atan2(rotateNormalx,rotateNormalz))

                    #rotZ = math.degrees((math.pi/(2.0))-math.asin(rotateNormaly))
                    try:
                        rotZ = math.degrees(1.57-math.asin(rotateNormaly))
                        #print "correct",rotateNormaly
                    except:
                        #print "error",rotateNormaly
                       # print math.asin(rotateNormaly)
                        rotZ = math.degrees(1.57-abs(math.asin(1.0)))
                        #print "%s"%newName + "   rotZ error"
                        self.errorInstanceObj.append(newName)
                        pass
                    #print n,'rotX',rotX
                    #print n,'rotY',rotY
                    #print n,'rotZ',rotZ
                    math.asin(-0.5)
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
        print self.errorInstanceObj
        #self.lineEdit_errorMessage.setText(self.errorInstanceObj)


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


 