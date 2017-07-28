
import maya.cmds as cmds

sel = cmds.ls(sl=True)
#sel = cmds.ls(tr =True)
#print sel
defaultRequestGroupList = ['character','vehicle','set','prop','other','effect']
buildDefaultGrpDict ={}
tempBuildDefaultGrpList = []
for i in defaultRequestGroupList:
    buildDefaultGrpDict.update({i:{}})
    
    allInTransformGrp = cmds.listRelatives(i, children=True, pa=True,ad=True)
    #print allInTransformGrp
    if allInTransformGrp == None:
        pass
    else:
        for j in allInTransformGrp:
            grpLingName =  cmds.ls(j,l=True)[0]
            tempBuildDefaultGrpList.append(grpLingName)
            #print grpLingName.split('|')
            #print grpLingName.split('|')
            #print grpLingName 
    
print buildDefaultGrpDict
print tempBuildDefaultGrpList

a= {'character':{'aaa':{'aaasa':{'aaasa3':{}}}}}
buildDefaultGrpDict.update(a)
buildDefaultGrpDict = buildDefaultGrpDict +a