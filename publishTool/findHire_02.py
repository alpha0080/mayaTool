
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
print tempBuildDefaultGrpList[0]
cmds.listRelatives('character',c=True)

for i in tempBuildDefaultGrpList[0].split('|'):
    print i


|character|g1|g2_1|g2_1_1

{'character':{'g1':'g2_1':{'g2_1_1':{}

a= {'character':{'aaa':{'aaasa':{'aaasa3':{}}}}}
buildDefaultGrpDict.update(a)
buildDefaultGrpDict = buildDefaultGrpDict +a