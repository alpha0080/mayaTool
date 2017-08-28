import maya.cmds as cmds

tempBuildDefaultGrpList = []
countList= []
            
allInTransformGrp = cmds.listRelatives('character', children=True, pa=True,ad=True)

#print cmds.listRelatives('character|L1_1|L2_1_1|L3_2_1_1', children=True, pa=True,ad=0)
            #print allInTransformGrp
if allInTransformGrp == None:
    pass
else:
    for j in allInTransformGrp:
        grpLingName =  cmds.ls(j,l=True)[0]
        tempBuildDefaultGrpList.append(grpLingName)
      #  print grpLingName
        countList.append(len(grpLingName.split('|')))
                
maxDepth = sorted(countList)[-1]-1
print 'maxDepth',maxDepth
elementEveryLevelCount = {}
itemHierarchy = {}
depthDict = {}

for i in range(0, maxDepth):
    depthDict.update({i:{}})
    
#print depthDict
for i in range(1,maxDepth):
    elementEveryLevelCount.update({i:[]})
  
allItemReleationShipDist = {}  
  
#for i in tempBuildDefaultGrpList:
#    print i 
    
    
refChildDict = {}
itemLevelDict = {}
    
for i in tempBuildDefaultGrpList:
   # print i
    #chaList =  i.split('|')
    refChild = cmds.listRelatives(i, children=True, pa=True,ad=0)  
    #print 'refChild',refChild,type(refChild)
    refChildList = []
    try:
        refMaxCount= len(refChild)
       # print 'refMaxCount',refMaxCount
        for j in range(0,refMaxCount):
            indexOfItem = refChild[j].split('|')[-1]+'.'+str(j)
            #print j ,refChild[j]
           # print indexOfItem
            refChildList.append(indexOfItem)
            itemLevelDict.update({refChild[j].split('|')[-1]:str(j)})
        refChildDict.update({i.split('|')[-1]:refChildList})
    except:
        refMaxCount = 'none'
        refChildDict.update({i.split('|')[-1]:'None'})
    refParent = cmds.listRelatives(i, children=True, p=True,ad=0) 
    for refParent in itemLevelDict.keys():
        print refParent,  itemLevelDict[refParent]
        
   # print 'refParent', refParent
   # print'totalItemCount' , len(refChildDict.keys())
       # print refMaxCount
    
    refChildSerNum = []
    
print 'refChildDict',refChildDict

'''

    #for j in range(0,len(refChild)):
    #    try:
      #      print j
    #    except:
   #         pass
    refParent = cmds.listRelatives(i, children=True, p=True,ad=0)  
    allItemReleationShipDist.update({i.split('|')[-1]:{'parent':[],'child':[]}})
    allItemReleationShipDist[i.split('|')[-1]].update({'parent':refParent})
    allItemReleationShipDist[i.split('|')[-1]].update({'child':refChild})
   # print ''.join(
    #print 'chaList',chaList
    
#cmds.select('L1_2')
    
    for j in range(0,maxDepth):   # get data from toplayer to depthLayer
        try: 
            for k in range(0,len(
            print 
            #listAllchild = cmds.listRelatives('character', children=True, pa=True,ad=0)  
           # allItemReleationShipDist.update({chaList[j]:{}})
           # print j                        
           # print 'chaList[j+1]',j+1,chaList[j+1]
           # if chaList[j+1]
           # depthDict[j].update({chaList[j+1]:{}})
        
        except:
            pass
            #depthDict[j].update({'none':{}})
       # print 'chaList[j+1]',chaList[j+1]
       # depthDict[j].update({chaList[j]:{}})
        
  #  print depthDict
    #getItemHierarchy(chaList,maxDepth,elementEveryLevelCount)
  #  getItemHierarchyB(chaList,itemHierarchy)
#cha = tempBuildDefaultGrpList[0]
#  print 'cha',cha
#getItemHierarchyC(cha,itemHierarchy)
#for i in 
'''