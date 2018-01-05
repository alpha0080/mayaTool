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
    
    checkStepRange = 0.02  #以0.02的距離作為每個區外的範圍
    blocks = int(1/checkStepRange)   #一共有多少區塊
    startLineUValue = 0
    uvPreLineDict= {}
    
    for i in range(0,blocks):      
        uvPreLineDict.update({i:[]})
        
        
        
    for i in range(0,blocks): #檢查落在每個區塊的UV
        startLineUValue = startLineUValue +checkStepRange
        lowerValue = float(startLineUValue - checkStepRange/2)    
        higherValue = float(startLineUValue + checkStepRange/2)
        #uvPreLineDict.update({i:[]})
        
        for j in range(0,len(uvDataDict.keys())):
            preUV = uvDataDict.keys()[j]
            preUVuValue = uvDataDict[uvDataDict.keys()[j]][0]
            if preUVuValue < 0.01:           #當U小於 0.01 將資料寫入 dict[0]的位置
                uvPreLineDict[0].append(preUV)
                
            elif preUVuValue >0.99: #當U大於0.99 將資料寫入 dict[49]的位置
                uvPreLineDict[(blocks-1)].append(preUV)
                
                
            elif preUVuValue > lowerValue and preUVuValue < higherValue:  #當資料落於這個數值區段 將資料寫入 dict[i]的位置
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
        uvDataDict.update({preUV:preUVCord})  #儲存每個UV的座標
    return uvDataDict # 每一條線上的UV
    
        
   
def runUVOperate(): #run Test
    selectItem = getSelectItem()
    print 'selectItem',selectItem
    
    uvDataDict= getUVInfoDict(selectItem)
    print 'uvDataDict',uvDataDict
    #getAllUVVerticalLine(uvDataDict)
    uvPreLineDict  = getAllUVVerticalLine(uvDataDict)
    print uvPreLineDict



runUVOperate()

