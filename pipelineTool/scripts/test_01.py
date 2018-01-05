import maya.cmds as cmds


    
def getSelectItem():   # got select item and check how many object selected
    selectItemList = cmds.ls(sl=True)
    if len(selectItemList) >1 :
        print 'got more than one object'
    else:
        selectItem = selectItemList[0]
        
    return selectItem
     
  #  print selectItem
  
  
def getAllUVVerticalLine(uvDataDict):
    print uvDataDict
    
    checkStepRange = 0.02  #�H0.02���Z���@���C�Ӱϥ~���d��
    blocks = int(1/checkStepRange)   #�@�@���h�ְ϶�
    startLineUValue = 0
    uvPreLineDict= {}
    
    for i in range(0,blocks):      
        uvPreLineDict.update({i:[]})
        
        
        
    for i in range(0,blocks): #�ˬd���b�C�Ӱ϶���UV
        startLineUValue = startLineUValue +checkStepRange
        lowerValue = float(startLineUValue - checkStepRange/2)    
        higherValue = float(startLineUValue + checkStepRange/2)
        #uvPreLineDict.update({i:[]})
        
        for j in range(0,len(uvDataDict.keys())):
            preUV = uvDataDict.keys()[j]
            preUVuValue = uvDataDict[uvDataDict.keys()[j]][0]
            if preUVuValue < 0.01:           #��U�p�� 0.01 �N��Ƽg�J dict[0]����m
                uvPreLineDict[0].append(preUV)
                
            elif preUVuValue >0.99: #��U�j��0.99 �N��Ƽg�J dict[49]����m
                uvPreLineDict[(blocks-1)].append(preUV)
                
                
            elif preUVuValue > lowerValue and preUVuValue < higherValue:  #���Ƹ���o�ӼƭȰϬq �N��Ƽg�J dict[i]����m
                uvPreLineDict[i].append(preUV)
                
    return uvPreLineDict
    
    
def getUVInfoDict(selectItem):  #got total count of select item
    #print selectItem
    totalUVCount = cmds.polyEvaluate(selectItem,uv=True)
    #return totalUVCount
    uvDataDict ={}
    for i in range(0,totalUVCount):
        preUV = selectItem +'.map[%s]'%i
        #print preUV
        cmds.select(preUV,tgl=True)
        #print cmds.polyEditUV(preUV)
        preUVCord = cmds.polyEditUV(preUV,q=True)
        uvDataDict.update({preUV:preUVCord})  #�x�s�C��UV���y��
    return uvDataDict # �C�@���u�W��UV
    
        
   
def runUVOperate(): #run Test
    selectItem = getSelectItem()
    print 'selectItem',selectItem
    
    uvDataDict= getUVInfoDict(selectItem)
    print 'uvDataDict',uvDataDict
    #getAllUVVerticalLine(uvDataDict)
    uvPreLineDict  = getAllUVVerticalLine(uvDataDict)
    print uvPreLineDict



runUVOperate()

