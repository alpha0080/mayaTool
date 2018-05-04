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
        self.lineEdit_sf = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sf.setGeometry(QtCore.QRect(40, 80, 61, 20))
        self.lineEdit_sf.setObjectName("lineEdit_sf")
        self.lineEdit_ef = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ef.setGeometry(QtCore.QRect(120, 80, 61, 20))
        self.lineEdit_ef.setObjectName("lineEdit_ef")
        self.label_sf = QtWidgets.QLabel(self.centralwidget)
        self.label_sf.setGeometry(QtCore.QRect(40, 60, 71, 16))
        self.label_sf.setObjectName("label_sf")
        self.label_ef = QtWidgets.QLabel(self.centralwidget)
        self.label_ef.setGeometry(QtCore.QRect(120, 60, 71, 16))
        self.label_ef.setObjectName("label_ef")
        self.label_rt = QtWidgets.QLabel(self.centralwidget)
        self.label_rt.setGeometry(QtCore.QRect(200, 60, 71, 16))
        self.label_rt.setObjectName("label_rt")
        self.lineEdit_rt = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_rt.setGeometry(QtCore.QRect(200, 80, 61, 20))
        self.lineEdit_rt.setObjectName("lineEdit_rt")
        self.pushButton_mc = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mc.setGeometry(QtCore.QRect(290, 80, 75, 23))
        self.pushButton_mc.setObjectName("pushButton_mc")
        self.checkBox_step = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_step.setGeometry(QtCore.QRect(290, 30, 73, 16))
        self.checkBox_step.setObjectName("checkBox_step")
        self.checkBox_allzero = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_allzero.setGeometry(QtCore.QRect(290, 50, 73, 16))
        self.checkBox_allzero.setChecked(True)
        self.checkBox_allzero.setObjectName("checkBox_allzero")
        self.pushButton_addPPF = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_addPPF.setGeometry(QtCore.QRect(40, 150, 201, 23))
        self.pushButton_addPPF.setObjectName("pushButton_addPPF")
        self.pushButton_delPPF = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delPPF.setGeometry(QtCore.QRect(40, 180, 201, 23))
        self.pushButton_delPPF.setObjectName("pushButton_delPPF")
        self.label_rt_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_rt_2.setGeometry(QtCore.QRect(200, 270, 71, 16))
        self.label_rt_2.setObjectName("label_rt_2")
        self.lineEdit_offsetFrame = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_offsetFrame.setGeometry(QtCore.QRect(200, 290, 61, 20))
        self.lineEdit_offsetFrame.setObjectName("lineEdit_offsetFrame")
        self.pushButton_makeOffsetFrame = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_makeOffsetFrame.setGeometry(QtCore.QRect(290, 290, 91, 23))
        self.pushButton_makeOffsetFrame.setObjectName("pushButton_makeOffsetFrame")
        self.lineEdit_offfsetStartFrame = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_offfsetStartFrame.setGeometry(QtCore.QRect(40, 290, 61, 20))
        self.lineEdit_offfsetStartFrame.setObjectName("lineEdit_offfsetStartFrame")
        self.label_sf_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_sf_2.setGeometry(QtCore.QRect(40, 270, 71, 16))
        self.label_sf_2.setObjectName("label_sf_2")
        self.label_ef_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_ef_2.setGeometry(QtCore.QRect(120, 270, 71, 16))
        self.label_ef_2.setObjectName("label_ef_2")
        self.lineEdit_offfsetendFrame = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_offfsetendFrame.setGeometry(QtCore.QRect(120, 290, 61, 20))
        self.lineEdit_offfsetendFrame.setObjectName("lineEdit_offfsetendFrame")
        self.label_sf_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_sf_3.setGeometry(QtCore.QRect(40, 350, 81, 16))
        self.label_sf_3.setObjectName("label_sf_3")
        self.lineEdit_cutkeyFrames = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cutkeyFrames.setGeometry(QtCore.QRect(40, 370, 61, 20))
        self.lineEdit_cutkeyFrames.setObjectName("lineEdit_cutkeyFrames")
        self.pushButton_cutKeys = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cutKeys.setGeometry(QtCore.QRect(120, 370, 91, 23))
        self.pushButton_cutKeys.setObjectName("pushButton_cutKeys")
        self.lineEdit_alignKey = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_alignKey.setGeometry(QtCore.QRect(40, 420, 61, 20))
        self.lineEdit_alignKey.setObjectName("lineEdit_alignKey")
        self.pushButton_alignKey = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_alignKey.setGeometry(QtCore.QRect(120, 420, 91, 23))
        self.pushButton_alignKey.setObjectName("pushButton_alignKey")
        self.label_sf_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_sf_4.setGeometry(QtCore.QRect(40, 400, 81, 16))
        self.label_sf_4.setObjectName("label_sf_4")
        self.checkBox_offsetRandom = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_offsetRandom.setGeometry(QtCore.QRect(290, 270, 73, 16))
        self.checkBox_offsetRandom.setObjectName("checkBox_offsetRandom")
        self.lineEdit_modifyValue = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_modifyValue.setGeometry(QtCore.QRect(40, 610, 61, 20))
        self.lineEdit_modifyValue.setObjectName("lineEdit_modifyValue")
        self.pushButton_makdModify = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_makdModify.setGeometry(QtCore.QRect(290, 610, 91, 23))
        self.pushButton_makdModify.setObjectName("pushButton_makdModify")
        self.label_sf_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_sf_5.setGeometry(QtCore.QRect(40, 590, 81, 16))
        self.label_sf_5.setObjectName("label_sf_5")
        self.label_sf_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_sf_6.setGeometry(QtCore.QRect(120, 590, 111, 16))
        self.label_sf_6.setObjectName("label_sf_6")
        self.lineEdit_modifyFrame = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_modifyFrame.setGeometry(QtCore.QRect(120, 610, 151, 20))
        self.lineEdit_modifyFrame.setObjectName("lineEdit_modifyFrame")
        self.checkBox_translateX = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_translateX.setGeometry(QtCore.QRect(50, 490, 81, 16))
        self.checkBox_translateX.setObjectName("checkBox_translateX")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 460, 411, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.checkBox_translateY = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_translateY.setGeometry(QtCore.QRect(130, 490, 81, 16))
        self.checkBox_translateY.setObjectName("checkBox_translateY")
        self.checkBox_translateZ = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_translateZ.setGeometry(QtCore.QRect(210, 490, 81, 16))
        self.checkBox_translateZ.setObjectName("checkBox_translateZ")
        self.checkBox_rotateX = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_rotateX.setGeometry(QtCore.QRect(50, 520, 81, 16))
        self.checkBox_rotateX.setObjectName("checkBox_rotateX")
        self.checkBox_rotateY = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_rotateY.setGeometry(QtCore.QRect(130, 520, 81, 16))
        self.checkBox_rotateY.setObjectName("checkBox_rotateY")
        self.checkBox_rotateZ = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_rotateZ.setGeometry(QtCore.QRect(210, 520, 81, 16))
        self.checkBox_rotateZ.setObjectName("checkBox_rotateZ")
        self.checkBox_scaleX = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_scaleX.setGeometry(QtCore.QRect(50, 550, 81, 16))
        self.checkBox_scaleX.setObjectName("checkBox_scaleX")
        self.checkBox_scaleZ = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_scaleZ.setGeometry(QtCore.QRect(210, 550, 81, 16))
        self.checkBox_scaleZ.setObjectName("checkBox_scaleZ")
        self.checkBox_scaleY = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_scaleY.setGeometry(QtCore.QRect(130, 550, 81, 16))
        self.checkBox_scaleY.setObjectName("checkBox_scaleY")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label_sf.setText(QtWidgets.QApplication.translate("MainWindow", "start frame", None, -1))
        self.label_ef.setText(QtWidgets.QApplication.translate("MainWindow", "end frame", None, -1))
        self.label_rt.setText(QtWidgets.QApplication.translate("MainWindow", "repeat times", None, -1))
        self.pushButton_mc.setText(QtWidgets.QApplication.translate("MainWindow", "make cycle", None, -1))
        self.checkBox_step.setText(QtWidgets.QApplication.translate("MainWindow", "step", None, -1))
        self.checkBox_allzero.setText(QtWidgets.QApplication.translate("MainWindow", "all in zero", None, -1))
        self.pushButton_addPPF.setText(QtWidgets.QApplication.translate("MainWindow", "add pre and post frame", None, -1))
        self.pushButton_delPPF.setText(QtWidgets.QApplication.translate("MainWindow", "delete pre and post frame", None, -1))
        self.label_rt_2.setText(QtWidgets.QApplication.translate("MainWindow", "offset ", None, -1))
        self.pushButton_makeOffsetFrame.setText(QtWidgets.QApplication.translate("MainWindow", "make offset", None, -1))
        self.label_sf_2.setText(QtWidgets.QApplication.translate("MainWindow", "start frame", None, -1))
        self.label_ef_2.setText(QtWidgets.QApplication.translate("MainWindow", "end frame", None, -1))
        self.label_sf_3.setText(QtWidgets.QApplication.translate("MainWindow", "cutKey Frames", None, -1))
        self.pushButton_cutKeys.setText(QtWidgets.QApplication.translate("MainWindow", "cutKeys", None, -1))
        self.pushButton_alignKey.setText(QtWidgets.QApplication.translate("MainWindow", "align Key", None, -1))
        self.label_sf_4.setText(QtWidgets.QApplication.translate("MainWindow", "align Key", None, -1))
        self.checkBox_offsetRandom.setText(QtWidgets.QApplication.translate("MainWindow", "random", None, -1))
        self.pushButton_makdModify.setText(QtWidgets.QApplication.translate("MainWindow", "modify", None, -1))
        self.label_sf_5.setText(QtWidgets.QApplication.translate("MainWindow", "value", None, -1))
        self.label_sf_6.setText(QtWidgets.QApplication.translate("MainWindow", "frames index [0,1,...]", None, -1))
        self.checkBox_translateX.setText(QtWidgets.QApplication.translate("MainWindow", "translateX", None, -1))
        self.checkBox_translateY.setText(QtWidgets.QApplication.translate("MainWindow", "translateY", None, -1))
        self.checkBox_translateZ.setText(QtWidgets.QApplication.translate("MainWindow", "translateZ", None, -1))
        self.checkBox_rotateX.setText(QtWidgets.QApplication.translate("MainWindow", "rotateX", None, -1))
        self.checkBox_rotateY.setText(QtWidgets.QApplication.translate("MainWindow", "rotateY", None, -1))
        self.checkBox_rotateZ.setText(QtWidgets.QApplication.translate("MainWindow", "rotateZ", None, -1))
        self.checkBox_scaleX.setText(QtWidgets.QApplication.translate("MainWindow", "scaleX", None, -1))
        self.checkBox_scaleZ.setText(QtWidgets.QApplication.translate("MainWindow", "scaleZ", None, -1))
        self.checkBox_scaleY.setText(QtWidgets.QApplication.translate("MainWindow", "scaleY", None, -1))



class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #self.QTITEM.ACTION.connect(self.MODDEF)
        self.setupUi(self)
    #def self.MODDEF(self):

        self.pushButton_mc.clicked.connect(self.getItems)
        self.pushButton_makeOffsetFrame.clicked.connect(self.offsetKeyFrames)
        self.pushButton_cutKeys.clicked.connect(self.cutKeys)
        self.pushButton_alignKey.clicked.connect(self.alignKeys)
        self.pushButton_makdModify.clicked.connect(self.modifyKeyValue)
        
        
    def modifyKeyValue(self):
        print "modify select key Attribute"
       # if self.checkBox_translateX.isChecked() == True:
            
        #if self.checkBox_translateX.isChecked() == True:
        frame = self.lineEdit_modifyFrame.text()
        value = float(self.lineEdit_modifyValue.text())
        objList = self.getObjList() 
        for obj in objList:   
            if self.checkBox_scaleX.isChecked() == True:
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

    def alignKeys(self):
        print "alignKeys"
        objList = self.getObjList()
        alignFrame = float(self.lineEdit_alignKey.text())  
        print objList
      #  print alignFrame     
        for obj in objList:
            print obj
            keyFrameList= []
            tempKeyFrameList = cmds.keyframe(obj,q=True)
            for key in tempKeyFrameList:
                if key in keyFrameList:
                    pass
                else:
                    keyFrameList.append(key)

     #   print keyFrameList
        
            for i in range(0,len(keyFrameList)):
                originalFrame = keyFrameList[i]
                newKeyFrame = i +alignFrame
              #  print  originalFrame,newKeyFrame
                try:
                    cmds.keyframe(obj,time=(originalFrame,originalFrame),timeChange=(newKeyFrame))
                except:
                    pass




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
        offsetValue = float(self.lineEdit_offsetFrame.text())
        

        keyFrameLength = offsetEndFrame-offsetStartFrame +1.0
        print "offsetKeyFrames"
        
        keyAbleAttList=["translateX","translateY","translateZ","rotateX","rotateY","rotateZ","scaleX","scaleY","scaleZ"] #["translateX","translateY","translateZ","rotateX","rotateY","rotateZ","scaleX","scaleY","scaleZ"]
        objList = self.getObjList()
        
        for obj in objList:
            if self.checkBox_offsetRandom.isChecked() == False:
                offsetValue = int(self.lineEdit_offsetFrame.text())
            else:
                offsetValue = random.randint(0,int(self.lineEdit_offsetFrame.text()))
                
            
          #  print obj
           # if 
            for attr in keyAbleAttList :
                try:
                    divideFrame = offsetEndFrame - offsetValue
                    modOffsetStepPreKeyFrame = float(offsetEndFrame - offsetValue -0.01)
                    modOffsetStepPosteKeyFrame = float(offsetEndFrame - offsetValue+0.01)
                    divideFrameValue = cmds.keyframe(obj,at=attr,t=(divideFrame,divideFrame),q=True,eval=True)[0]
                 #   postKeyFrameValue = cmds.keyframe(obj,at=attr,t=(divideFrame,divideFrame),q=True,eval=True)[0]
                    cmds.setKeyframe(obj, t=[modOffsetStepPreKeyFrame,modOffsetStepPreKeyFrame], at=attr,v=divideFrameValue )
                    cmds.setKeyframe(obj, t=[divideFrame,divideFrame], at=attr,v=divideFrameValue )

                    cmds.setKeyframe(obj, t=[modOffsetStepPosteKeyFrame,modOffsetStepPosteKeyFrame], at=attr,v=divideFrameValue )

                  #  print attr,modOffsetStepPreKeyFrame,divideFrameValue
                  #  print attr,modOffsetStepPosteKeyFrame,divideFrameValue
   
                except:
                    pass
               # cmds.keyframe(obj, t=(modOffsetStepPreKeyFrame,modOffsetStepPreKeyFrame),at=attr,vc =preKeyFrameValue)
               # cmds.keyframe(obj, t=(postKeyFrameValue,postKeyFrameValue),at=attr,vc =postKeyFrameValue)
# cmds.setKeyframe("pSphere6", t=[99.01,99.01], at="translateX",v=30 )                
 #cmds.keyframe("pSphere6",at="translateX",q=True)               
                  #  cmds.setKeyframe(obj, t=[modOffsetStepPosteKeyFrame,modOffsetStepPosteKeyFrame], at=attr,v=divideFrameValue )
              
                keyValueDict = {}
                offsetKeyFrameDict={}
                keyFrameList = cmds.keyframe(obj,at=attr,q=True)
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


 