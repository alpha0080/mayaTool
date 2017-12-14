#coding=utf-8


from pprint import pprint

import datetime

import json

def getDataFromTactic():
    print "run getDataFromTactic start"
    publishConfigFile = '//mcd-one/database/assets/scripts/maya_scripts/publishToolConfig.json'
    
    with open(publishConfigFile, 'r') as f:
        publishToolSettingData = json.load(f)

    scripts_path = "//mcd-one/database/assets"
    sys.path.append(scripts_path +  "/client")
    sys.path.append(scripts_path + "/scripts/tactic_scripts/ui")
    
    
    tacticHostName = publishToolSettingData['tacticHostName']
    tacticHostIP = publishToolSettingData['tacticHostIP']
    loginID = publishToolSettingData['tacticID']
    loginPW = publishToolSettingData['tacticPW']
    root = publishToolSettingData['root']
    fileTypeFillet = publishToolSettingData['fileTypeFillet']

    import getTacticDataB
    reload(getTacticDataB)


    tactic = getTacticDataB.connectToTactic(tacticHostName,tacticHostIP,loginID,loginPW)  # login tactic 
   # print tactic
    assetsInTactic = tactic.runTactic('asset')   #get all asset data
    projectsInTactic = tactic.runTactic('project') #get all project data
    shotsInTactic = tactic.runTactic('shot') #get all shots data

    return(projectsInTactic,assetsInTactic,shotsInTactic) #return project data in tactic, assets ,shots
    

    
    
    
def reNewAllAssetInDBB():
    allAssetsData = getDataFromTactic()[1]
    
    countAssets = len(allAssetsData)
    #print 'countAssets',countAssets
    
    
    
    #for i in range(0,15):
    startNum = 0
    endNum =countAssets
    for count in range(startNum,endNum):
        assetColumnData = []
        assetWriteColumnData = []
        for i in allAssetsData[count].keys():
          #  print i, allAssetsData[count][i]
          #  try:
            #    print type(allAssetsData[0][i])
           # except:
           #     print 'bbb',type(str(allAssetsData[0][i]))
            assetColumnData.append(allAssetsData[count][i])
       # wrtieIntoPostgreSQL('assets',assetColumnData)
       # print assetColumnData,len(assetColumnData)
        for i in assetColumnData:
            try:
                #print i#.encode('big5')#.decode('big5')
                assetWriteColumnData.append(i.encode('utf-8'))
                #assetWriteColumnData.append(i.encode('big5'))
            except:
                #print '%d'%i
                assetWriteColumnData.append(('%d'%i))
                
        print assetWriteColumnData
        wrtieIntoPostgreSQL('assets',assetWriteColumnData)
            #pass

def reNewAllAssetInDB(tableName,lastCount):
    '''will renew all assets data ,shourced from tactic server. And
    renew  into postgreSQL server databass.
    
    tableName, 'string' , is DB name, it will conect to postgreSQL server.
    lastCount, int , last count number to process, -  option
      
    
    '''
      
    startTime = datetime.datetime.now()

       
    # get data from DB
    
    import postgreSQLCall

    reload(postgreSQLCall)
    
    getDB = postgreSQLCall.callPostgre('3D_db','postgres','5j/u.42017','192.168.161.47','5432')
    
    codeList =  sorted(getDB.getRowSelectDataFromTable(tableName,'code'))
    idList = sorted(getDB.getRowSelectDataFromTable(tableName,'id'))
    
    
    
    
    
    
    #get data from tactic
    allAssetsData = getDataFromTactic()[1]   # all assets data from tactic
    allAssetsDataKeyList =  allAssetsData[0].keys()#.keys
    #print allAssetsDataKeyList
    
    countAssetsTactic = len(allAssetsData) # all assets count from tactic
    countAssetsDB = len(codeList)  # all assets count from tactic
    print 'countAssetsTactic',countAssetsTactic
    print 'countAssetsDB',countAssetsDB
    #print idList
    if lastCount == 0 :
    
        startColumnNum = 0
        endColumnNum = countAssetsTactic
        

    else: 
        startColumnNum = countAssetsTactic-lastCount
        endColumnNum = countAssetsTactic
        
        
    for count in range(startColumnNum,endColumnNum):  #relace select assets data in DB from tactic
        assetColumnData = []
        assetWriteColumnData = []
        for i in allAssetsData[count].keys():

            assetColumnData.append(allAssetsData[count][i])

        whereKey = 'code'    #get searchKey
        whereData = codeList[count][0]
        #countNum = idList
        print 'indexNum',count+1
        #print whereData
        
        for i,j in zip(allAssetsDataKeyList,assetColumnData):
            try:

                newDataInColumn =  j #.decode('big5')

            except:
                #print '%d'%i
                #assetWriteColumnData.append(('%d'%i))
                newDataInColumn = '%d'%j
            #print allAssetsDataKeyList[i]
            columnName = str(i)
            columnNameValue = newDataInColumn 
            #update DB
            
            #print tableName,whereKey,whereData,columnName,columnNameValue
            
    
            try:
                getDB.updateDataToTable(tableName,whereKey,whereData,columnName,columnNameValue)  
            except:
                 
                print 'error at' , tableName,whereKey,whereData,columnName,columnNameValue
            
    '''        
    for count in range(countAssetsTactic,countAssetsDB+1):   
        whereKey = 'code'    #get searchKey
        whereData = codeList[count][0]
        for i in allAssetsDataKeyList:
            columnName = i
            columnNameValue = ''
            print 'count',count
            print 'columnName',columnName
            print 'columnNameValue',columnNameValue
        #countNum = idList
            try:
                getDB.updateDataToTable(tableName,whereKey,whereData,columnName,columnNameValue) 
            except:
                pass    
    '''    
    #timestamp = time.mktime(now.timetuple())
    endTime = datetime.datetime.now()
    #print startTime
    #print endTime
    print (endTime - startTime)
 
        
    
def checkColumnDataInDB(tableName):
    
    import postgreSQLCall

    reload(postgreSQLCall)
    
    getDB = postgreSQLCall.callPostgre('3D_db','postgres','5j/u.42017','192.168.161.47','5432')
    
    codeList =  getDB.getRowSelectDataFromTable(tableName,'code')
    idList = getDB.getRowSelectDataFromTable(tableName,'id')
    
    
    #getDB.updateDataToTable(tableName,whereKey,whereData,columnName,columnNameValue)
    #print idList[-1]
    #for i in idList:
       # print i
    
    #rows = getDB.getRowDataFromTable(tableName)
    
    #totalColumnCount = len(rows)


    
def wrtieIntoPostgreSQL(tableName,dataList):

    import postgreSQLCall

    reload(postgreSQLCall)
    
    getDB = postgreSQLCall.callPostgre('3D_db','postgres','5j/u.42017','192.168.161.47','5432')
    #print getDB.cursor

    #tableName = 'assets'
    
   # print tableName
    #print  dataList  
   # print getDB.getRowDataFromTable(tableName)
    #print ", ".join(dataList),len(dataList)
    #dataList = ['code xxxxx','description xxxxx','timestamp xxxxx','s_status xxxxx','keywords xxxxx','pipeline_code xxxxx',
    #            'frames xxxxx','game_code xxxx','id xxxxx','relative_dir xxxxx','name xxxxx',
    #            '__search_key__ xxxxx','game_name_chn xxxxx','login xxxxx','asset_type_code xxxxx']
    
    try:
        getDB.insertAllDataIntoTableColumn(tableName,dataList)
    except:
        pass
        #getDB.updateDataToTable(tableName,whereKey,whereData,columnName,columnNameValue)
    
#checkColumnDataInDB('assets')
reNewAllAssetInDB('assets',10)
#getDataFromTactic()[0]
#wrtieIntoPostgreSQL()