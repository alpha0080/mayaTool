
from PySide2 import QtCore, QtGui, QtWidgets


import postgreSQL_db_UI
reload(postgreSQL_db_UI)
import datetime

import json

import postgreSQLCall

reload(postgreSQLCall)
    

Ui_MainWindow = postgreSQL_db_UI.Ui_MainWindow
setupUi = Ui_MainWindow.setupUi

#print Ui_MainWindow
#print QtWidgets.QMainWindow getDataFromTactic




class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #self.QTITEM.ACTION.connect(self.MODDEF)
        self.setupUi(self)
        self.assetsTableName = self.assetDBName_lineEdit.text()
        self.usersTableName = self.userDB_lineEdit.text()
        
        
        #inital running
        # connect to postgreSQL database
        self.getDB = postgreSQLCall.callPostgre('3D_db','postgres','5j/u.42017','192.168.161.47','5432')  
        self.allAssetsData = self.getDataFromTactic()
        
        
        
        
        #all button signal/slot insertAllAssetDataIntoDB ru03
        self.createAssetDB_pushButton.clicked.connect(self.createEmptyAssetsTable) #create userDB
        self.update_AssetDB_pushButton.clicked.connect(self.insertAllAssetDataIntoDB)
        self.testA_pushButton.clicked.connect(self.createEmptyUsersTable)  #create userDB
        self.testB_pushButton.clicked.connect(self.insertAllUserDataIntoDB)
        self.testC_pushButton.clicked.connect(self.reNewUserDBFromTacticIntoDB)
        self.update_AssetDB_pushButton.clicked.connect(self.searchDataFromUserDB)
        
    #def self.MODDEF(self):
    def reNewUserDBFromTacticIntoDB(self):

        try:
            self.deleteUserTable()
        except:
            pass
            
        #self.getDB.close()
        self.createEmptyUsersTable()
        self.insertAllUserDataIntoDB()
            #self.getDB.close()

        self.changeUserNickNameIntoDB()
            

        
    def deleteUserTable(self):
        print 'delete Users Table'
        #self.getDB.deleteSelectTable('assd')
        self.getDB = postgreSQLCall.callPostgre('3D_db','postgres','5j/u.42017','192.168.161.47','5432')  

        self.getDB.deleteSelectTable(self.usersTableName)
        #self.getDB.close()

        
    def getDataFromTactic(self):
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
        usersInTactic = tactic.runTactic('user')
        return(projectsInTactic,assetsInTactic,shotsInTactic,usersInTactic) #return project data in tactic, assets ,shots
        
        
    def createEmptyAssetsTable(self):

        self.getDB = postgreSQLCall.callPostgre('3D_db','postgres','5j/u.42017','192.168.161.47','5432')  

        columnList = ('index text not null,'
                    'code text not null primary key,'
                    'description text not null,'
                    'timestamp text not null,'
                    's_status text not null,'
                    'keywords text not null,'
                    'pipeline_code text not null,'
                    'frames text not null,'
                    'game_code text not null,'
                    'id text not null,'
                    'relative_dir text not null,'
                    'name text not null,'
                    '__search_key__ text not null,'
                    'game_name_chn text not null,'
                    'login text not null,'
                    'asset_type_code text not null'
                    )
        
        self.getDB.createTabeIntoDatabase(self.assetsTableName,columnList)
        
        
        
            
    def createEmptyUsersTable(self): #build users table in DB
        self.getDB = postgreSQLCall.callPostgre('3D_db','postgres','5j/u.42017','192.168.161.47','5432')  
        columnList = ('index text not null,'
                    'code text not null primary key,'
                    'first_name text not null,'
                    'last_name text not null,'
                    'display_name text not null,'
                    'department text not null,'
                    'ext text not null,'
                    'section text not null,'
                    'inProjectA text not null,'
                    'inProjectB text not null,'
                    'inProjectC text not null,'
                    'inProjectD text not null,'
                    'ranking_grade_week1 text not null,'
                    'ranking_grade_week2 text not null,'
                    'ranking_grade_week3 text not null,'
                    'ranking_grade_week4 text not null,'
                    'ranking_grade_week5 text not null,'                    
                    'ranking_description_week1 text not null,'
                    'ranking_description_week2 text not null,'
                    'ranking_description_week3 text not null,'
                    'ranking_description_week4 text not null,'
                    'ranking_description_week5 text not null,'
                    'ranking_grade_all text not null,'
                    'ranking_description_all text not null,'
                    'ranking_all text not null,'
                    'skill text not null,'
                    'skillTraining text not null,'
                    'position text not null,'
                    'salary text not null,'
                    'noteA text not null,'
                    'noteB text not null,'     
                    'noteC text not null,'                    
                    'noteD text not null,'                    
                    'noteE text not null,'                    
                    'noteF text not null'                                   
                    )
        
        self.getDB.createTabeIntoDatabase(self.usersTableName,columnList)
        
    def insertAllUserDataIntoDB(self):
        allUserData = self.allAssetsData[3]
        countUsers = len(allUserData)
        startNum = 0
        endNum = countUsers
         
        for count in range(startNum,endNum):
           # assetColumnData = [(count+1)]
            #assetWriteColumnData = []
            userInfoDict = allUserData[count]
            userWriteColumnData = [str('%04d'%(count+1)),
                                    (userInfoDict['code']).encode('utf-8'),
                                    (userInfoDict['first_name']).encode('utf-8'),
                                    (userInfoDict['last_name']).encode('utf-8'),
                                    (userInfoDict['display_name']).encode('utf-8'),
                                    (userInfoDict['department']).encode('utf-8'),
                                    (userInfoDict['ext']).encode('utf-8'),
                                    (userInfoDict['section']).encode('utf-8'),
                                   'inProject',
                                    'inProjectB',
                                    'inProjectC',
                                    'inProjectD',
                                    'ranking_grade_week1',
                                    'ranking_grade_week2',
                                    'ranking_grade_week3',
                                    'ranking_grade_week4',
                                    'ranking_grade_week5',              
                                    'ranking_description_week1',
                                    'ranking_description_week2',
                                    'ranking_description_week3',
                                    'ranking_description_week4',
                                    'ranking_description_week5',
                                    'ranking_grade_all',
                                    'ranking_description_all',
                                    'ranking_all',
                                    'skill',
                                    'skillTraining',
                                    'position',
                                    'salary',
                                    'noteA',
                                    'noteB',
                                    'noteC',             
                                    'noteD',                  
                                    'noteE',            
                                    'noteF']
            
            
            #print userWriteColumnData
           # for i in userWriteColumnData:
               # print i,type(i)
            try:
                self.getDB.insertAllDataIntoTableColumn(self.usersTableName,userWriteColumnData)
            except:
                pass
             #   print count, ' error'
            #    pass
                #print i['first_name'],i['last_name'],i['display_name'],i['department'],i['ext'],i['section']
               # print i#[count]#, allUserData[count][i]
              #  try:
                #    print type(allAssetsData[0][i])
               # except:
               #     print 'bbb',type(str(allAssetsData[0][i]))
               
            #    assetColumnData.append(allUserData[count][i])
           # wrtieIntoPostgreSQL('assets',assetColumnData)
           # print assetColumnData,len(assetColumnData)
        #self.changeUserNickNameIntoDB()

    def changeUserNickNameIntoDB(self):  
        tableName = self.userDB_lineEdit.text()
        searchKeyWord = 'code'
        userData = self.allAssetsData[3]
        userDataFromDB = self.getDB.getRowSelectDataFromTable(tableName,searchKeyWord)

       # print userData
        show = ''
        whereKey = 'code'
        columnName = 'first_name'
        for codeFromDBData,codeFromTacticData in zip(userDataFromDB,userData):
            whereData = codeFromDBData[0]    #whereData
            columnNameValue = codeFromTacticData['first_name'] #
          #  print whereData, columnNameValue #columnNameValue
            #codeName = code[0]   #get codeValue from DB
            
            
            
           # nickName = ('%s'%i[0]).encode('big5').decode('big5')
            #show = show + nickName +'\n'
           # self.info_plainTextEdit.setPlainText(show)
            
            self.getDB.updateDataToTable(tableName,whereKey,whereData,columnName,columnNameValue)
            
            
        '''    
        for i in userData:
            decodeFirstNameFromTactic = i['first_name'].encode('big5').decode('big5')
            
            nickName = i['first_name'].encode('big5').decode('big5')
            show = show + nickName +'\n'
            self.info_plainTextEdit.setPlainText(show)
        
        '''
    def searchDataFromUserDB(self):
        self.getDB = postgreSQLCall.callPostgre('3D_db','postgres','5j/u.42017','192.168.161.47','5432')  

        tableName = self.userDB_lineEdit.text()
        #searchKeyWord = 'first_name'
        userCode = self.getDB.getRowSelectDataFromTable(tableName,'code')
        userNickName = self.getDB.getRowSelectDataFromTable(tableName,'first_name')
        userDept = self.getDB.getRowSelectDataFromTable(tableName,'department')
        section = self.getDB.getRowSelectDataFromTable(tableName,'section')
        count = len(userNickName)
        for i in range (0,count):
            print userCode[i],userNickName[i],userDept[i],section[i]

       # print userNickName,userDept,section

        
        
        
    def bbbb(self):
        
        userDataFromDB = self.getDB.getRowSelectDataFromTable(tableName,searchKeyWord)
        show = ''

        for i in userDataFromDB:
            nickName = str(i[0]).encode('big5').decode('big5')
            #print i[0],type(i)
            show = show + nickName +'\n'
            self.info_plainTextEdit.setPlainText(show)
           # print userDataFromDB[i]
        
        
        
        
        
    
    def insertAllAssetDataIntoDB(self):
        allAssetsData = self.allAssetsData[1]
    
        countAssets = len(allAssetsData)
        
        #print allAssetsData
        #print countAssets
        #print 'countAssets',countAssets
        # assetWriteColumnData countAssets
        
        #for i in range(0,15):
        startNum = 0
        endNum = countAssets
        for count in range(startNum,endNum):
            assetColumnData = [(count+1)]
            assetWriteColumnData = []
            
            for i in allAssetsData[count].keys():
               # print i
               # print i, allAssetsData[count][i]
              #  try:
                #    print type(allAssetsData[0][i])
               # except:
               #     print 'bbb',type(str(allAssetsData[0][i]))
               
                assetColumnData.append(allAssetsData[count][i])
           # wrtieIntoPostgreSQL('assets',assetColumnData)
           # print assetColumnData,len(assetColumnData)
                

            for i in assetColumnData:
                #print type(i)
                #assetWriteColumnData.append(i)
                if type(i) == int:
                    assetWriteColumnData.append((u'%d'%i).encode('utf-8'))
                   # print '%d'%i
                else:
                    assetWriteColumnData.append(i.encode('utf-8'))
           # print len(assetWriteColumnData)
           # for i in assetWriteColumnData:
             #   print i ,type(i)
            try:
                self.getDB.insertAllDataIntoTableColumn(self.assetsTableName,assetWriteColumnData)
            except:
                pass
                #print 'error'
        '''
                try:
                    #print i#.encode('big5')#.decode('big5')
                    assetWriteColumnData.append(i.decode('utf-8'))
                    #assetWriteColumnData.append(i.encode('big5'))
                except:
                    #print '%d'%i
                    assetWriteColumnData.append(('%d'%i))
                    
            #print assetWriteColumnData    
        
            try:
                self.getDB.insertAllDataIntoTableColumn(self.assetsTableName,assetWriteColumnData)
            except:
                print 'ggg'
                pass
        '''        
                
    def reNewAllAssetInDB(self):#,lastCount):
        '''
        will renew all assets data ,shourced from tactic server. And
        renew  into postgreSQL server databass.
        
        tableName, 'string' , is DB name, it will conect to postgreSQL server.
        lastCount, int , last count number to process, -  option
          
        
        '''
          
        startTime = datetime.datetime.now()

           
        # get data from DB



        codeList =  sorted(self.getDB.getRowSelectDataFromTable(self.assetsTableName,'code'))
        idList = sorted(self.getDB.getRowSelectDataFromTable(self.assetsTableName,'id'))
        
        print 'codeList',codeList
        print 'idList',idList
        
        
        
        
        
    def bbb(self):
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
                    
            
            
            
        
def main():
    global ui
    app = QtWidgets.QApplication.instance()
    if app == None: app = QtWidgets.QApplication(sys.argv)
    try:
        ui.close()
        ui.deleteLater()
    except: pass
    ui = mod_MainWindow()
    ui.show()
 
if __name__ == '__main__':
    main()



 