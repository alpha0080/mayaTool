#coding=utf-8
import postgreSQLCall

reload(postgreSQLCall)

getDB = postgreSQLCall.callPostgre('3D_db','postgres','5j/u.42017','192.168.161.47','5432')
print getDB.cursor

tableName = 'assets'
'''
columnList = ('name text not null primary key,'
            'id text not null,'
            'dept text not null,'
            'position text not null,'
            'salary text not null,'
            'workInProcess text not null,'
            'workSkill text not null,'
            'training text not null,'
            'assessment text not null,'
            'assessmentClass text not null,'
            'note text not null'
            )

print columnList

getDB.createTabeIntoDatabase('mcdUserData',columnList)
'''
#print getDB



# addColumnToTable(self,tableName,columnName,dataType,isNotNull)
#getDB.addColumnToTable('mcduser','fileTT','json','not null')

#print getDB.addColumnToTable.__doc__

#insertDataIntoTableColumn(self,tableName,columnName,value)

#getDB.insertStringDataIntoTableColumn('mcduser','name', '�p��'.decode('big5'))
#print self.cursor
#dataList =['name alpha','id 2013050506','dept 3d','pposition director','salary','work not in work','skill rolling','trainingsleeping','assessement','assessementClass','note']
#len(dataList)
#aa = ['gg'] + dataList[1:]
#getDB.insertAllDataIntoTableColumn('mcdUserData',dataList)
# dropColumnFromTable(self,tableName,columnName)
#getDB.dropColumnFromTable('mcduser','rt')
#whereKey = 'name'
#whereData = 'name alpha'
#columnName = 'workskill'
#columnNameValue = 'jumpping'



#getDB.updateDataToTable(tableName,whereKey,whereData,columnName,columnNameValue)
#getDB.updateDataToDatabase('mcdUserData',

#print getDB.getSelectTableQuery('mcduser')[0]
for i in getDB.getSelectTableQuery('mcdUserData'):
    print i
