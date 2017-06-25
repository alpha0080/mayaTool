import maya.cmds as cmds
import pymel.core as pm
import json, os



def createAssetTopLayerGrp(mode):  #check code H001
    print ' createAssetTopLayerGrp '
    print 'error code H001, create character,vehicle,set,prop and other'
    
    print mode
    
    assetTopLayerTransformNodeList = ['character','vehicle','set','prop','other']
    print assetTopLayerTransformNodeList
    
    for nodeName in assetTopLayerTransformNodeList:
        cmds.createNode('transform', n = nodeName )
        
        
 
    
def run(mode):
    createAssetTopLayerGrp(mode)
    
    
createAssetTopLayerGrp('check')
    

run('check')