
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
            
    print 'tempBuildDefaultGrpList',tempBuildDefaultGrpList
#
  #  print sorted(countList)
    maxDepth = sorted(countList)[-1]
  #  print maxDepth
   # getItemHierarchy(2)
   # getItemHierarchy(2)
   # getItemHierarchy(2)
    elementEveryLevelCount = {}
    itemHierarchy = {}
    for i in range(1,maxDepth):
        elementEveryLevelCount.update({i:[]})
        
    for i in tempBuildDefaultGrpList:
        chaList =  i.split('|')
       # print 'chaList',chaList
        #getItemHierarchy(chaList,maxDepth,elementEveryLevelCount)
        getItemHierarchyB(chaList,itemHierarchy)
  #  print 'elementEveryLevelCount',elementEveryLevelCount
   # print 'itemHierarchy',itemHierarchy
    
def getItemHierarchyB(chaList,itemHierarchy):
    itemDepth = len(chaList)
   # print chaList
    for i in range( itemDepth-1,0,-1):
       # print chaList[i]
       # print i
    #print range( itemDepth,0,-1)
        print chaList[i]
        #itemHierarchy.update({chaList[i]:{}})
        parentItem = chaList[i-1]
        print 'parentItem',parentItem
        #itemHierarchy
        
def getItemHierarchy(chaList,maxDepth,elementEveryLevelCount):
    
    #print 'depth',depth
    itemDepth = len(chaList)
   # print itemDepth
 #   tempPerLevelItemList= []
    for i in range( 1,itemDepth):
       # print i,chaList[i]
      #  print elementEveryLevelCount[i]
        if chaList[i] in elementEveryLevelCount[i]:
            pass
     #   tempPerLevelItemList.append(
        else:
            elementEveryLevelCount[i].append(chaList[i])
        #elementEveryLevelCount[i].update({chaList[i]:{}})

#cmds.listRelatives('L5_g2',f=True,p=True)
#print cmds.listConnections('L5_g2',c=True)
        

def getChild(parentObjTransform):
    getChild = pm.listRelatives(parentObjTransform,c=True)
   # print getChild
    
    
#getChild('character')
getAllGrpTransformFromOutliner('character')
    
