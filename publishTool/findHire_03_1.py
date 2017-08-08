
import pymel.core as pm
import maya.cmds as cmds

def getAllGrpTransformFromOutliner(topLayerItemInOutlinear):

    tempBuildDefaultGrpList = []
    countList= []
        
    allInTransformGrp = cmds.listRelatives(topLayerItemInOutlinear, children=True, pa=True,ad=True)
        #print allInTransformGrp
    if allInTransformGrp == None:
        pass
    else:
        for j in allInTransformGrp:
            grpLingName =  cmds.ls(j,l=True)[0]
            tempBuildDefaultGrpList.append(grpLingName)
            print grpLingName
            countList.append(len(grpLingName.split('|')))
            
    print tempBuildDefaultGrpList

    print sorted(countList)
    maxDepth = sorted(countList)[-1]
  #  print maxDepth
    getItemHierarchy(2)
    for i in tempBuildDefaultGrpList:
        print i.split('|')
        

def getItemHierarchy(depth):
    print 'depth',depth
    
print 214280*0.27
    

def getChild(parentObjTransform):
    getChild = pm.listRelatives(parentObjTransform,c=True)
    print getChild
    
    
#getChild('character')
getAllGrpTransformFromOutliner('character')
    
