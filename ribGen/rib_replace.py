# -*- coding: utf-8 -*-
import PySide.QtCore as qc
import PySide.QtGui as qg
import pymel.core as pm
import os
import maya.cmds as cmds
global ui

dialog=None

#---------------------------------------------------------------------------------------------------#

class Black_UI(qg.QDialog):
    def __init__(self):
        qg.QDialog.__init__(self)
        self.setWindowTitle('rib replace'+' v0.7'+u' by 小黑')
        self.setWindowFlags(qc.Qt.WindowStaysOnTopHint)
        self.setModal(False)
        self.resize(600,480)
        self.setLayout(qg.QVBoxLayout())
        self.layout().setAlignment(qc.Qt.AlignTop)


        pxr_shaders=['PxrSurface','PxrLayerSurface']
        #定義路徑替換UI
        substitueLabel=qg.QLabel('Substitute path root')
        self.layout().addWidget(substitueLabel)
        replacePathFormLayout=qg.QFormLayout()
        self.oldRoot=qg.QLineEdit()
        self.newRoot=qg.QLineEdit()
        replacePathFormLayout.addRow('Old Root',self.oldRoot)
        replacePathFormLayout.addRow('New Root',self.newRoot)
        self.layout().addLayout(replacePathFormLayout)



        self.under_but_layout = qg.QHBoxLayout()
        substitute_rib_but = qg.QPushButton('substitute Rib')
        substitute_rib_but.clicked.connect(self.rib_replace)
        substitute_gpu_but = qg.QPushButton('substitute gpuCache')
        substitute_gpu_but.clicked.connect(self.gpu_replace)
        set_matteID_but = qg.QPushButton('set matteID')
        set_matteID_but.clicked.connect(self.set_matteID)
        self.under_but_layout.addWidget(substitute_rib_but)
        self.under_but_layout.addWidget(substitute_gpu_but)
        self.under_but_layout.addWidget(set_matteID_but)
        self.layout().addLayout(self.under_but_layout)


#---------------------------------------------------------------------------------------------------#
    def rib_replace(self):
		rib_list=pm.ls(type='RenderManArchive',dag=True)
		for i in rib_list:
			path=pm.getAttr(i+'.filename')
			new_path=self.go_replace(path)
			pm.setAttr( i+'.filename', new_path )


    def gpu_replace(self):
		rib_list=pm.ls(type='gpuCache',dag=True)
		for i in rib_list:
			path=pm.getAttr(i+'.cacheFileName')
			new_path=self.go_replace(path)
			pm.setAttr( i+'.cacheFileName', new_path )


    def go_replace(self,path):
		old_path=self.oldRoot.text()
		new_path=self.newRoot.text()
		new_path=new_path.replace('\\','/')
		pathChanged=path.replace(old_path,new_path)
		return pathChanged

    def set_matteID(self):
        if pm.objExists('global_matteID'):
            print 'global_matteID already exists '
        else:
            pm.shadingNode('PxrMatteID', at=True,n='global_matteID')
        PxrSurface_shaders=pm.ls(type='PxrSurface')
        PxrLayerSurface_shaders=pm.ls(type='PxrLayerSurface')
        PxrDisney_shaders=pm.ls(type='PxrDisney')

        for i in PxrSurface_shaders:
            pm.connectAttr( 'global_matteID.resultAOV', i+'.utilityPattern[0]' ,f=True)

        for i in PxrLayerSurface_shaders:
            pm.connectAttr( 'global_matteID.resultAOV', i+'.utilityPattern[0]' ,f=True)

        for i in PxrDisney_shaders:
            pm.connectAttr( 'global_matteID.resultAOV', i+'.inputAOV' ,f=True)




#---------------------------------------------------------------------------------------------------#
def create():
    global dialog
    if dialog is None:
        dialog =Black_UI()
    dialog.show()

def delete():
    global dialog
    if dialog is None:
        return
    dialog.deleteLater()
    dialog =None


def rib_replaceMain():
    global dialog
    if dialog is None:
        dialog =Black_UI()
    dialog.show()