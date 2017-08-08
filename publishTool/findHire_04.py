
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
          #  print grpLingName
            countList.append(len(grpLingName.split('|')))
            
   # print 'tempBuildDefaultGrpList',tempBuildDefaultGrpList
#
  #  print sorted(countList)
    maxDepth = sorted(countList)[-1]
  #  print maxDepth
   # getItemHierarchy(2)
   # getItemHierarchy(2)
   # getItemHierarchy(2)
    elementEveryLevelCount = {}
    for i in range(1,maxDepth):
        elementEveryLevelCount.update({i:[]})
        
    for i in tempBuildDefaultGrpList:
        chaList =  i.split('|')
       # print 'chaList',chaList
        getItemHierarchy(chaList,maxDepth,elementEveryLevelCount)
    print 'elementEveryLevelCount',elementEveryLevelCount
    
def getItemHierarchy(chaList,maxDepth,elementEveryLevelCount):
    
    #print 'depth',depth
    itemDepth = len(chaList)
   # print itemDepth
 #   tempPerLevelItemList= []
    for i in range( 1,itemDepth):
        print i,chaList[i]
     #   tempPerLevelItemList.append(
        elementEveryLevelCount[i].append(chaList[i])
        #elementEveryLevelCount[i].update({chaList[i]:{}})



        

def getChild(parentObjTransform):
    getChild = pm.listRelatives(parentObjTransform,c=True)
   # print getChild
    
    
#getChild('character')
getAllGrpTransformFromOutliner('character')
    
