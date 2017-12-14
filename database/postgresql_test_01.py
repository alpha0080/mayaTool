import sys

sys.path.append('C:/Python27/Lib')
sys.path.append('C:/Python27/Lib/site-packages')

import psycopg2


# connect to postgreSQL server@192.168.161.47
#conn = psycopg2.connect(database='mydb', user='postgres', password='5j/u.42017', host='192.168.161.47', port='5432', sslmode='disable')
conn = psycopg2.connect(database='3D_db', user='postgres', password='5j/u.42017', host='192.168.161.47', port='5432')

cursor = conn.cursor()  #用來建立整個資料庫操作的 tag
#command ='"CREATE TABLE public.trtrt("yyy int");"'
#cursor.execute("CREATE TABLE public.sdsd(uer int);")
#cursor.execute("CREATE TABLE Cars(Id INTEGER PRIMARY KEY, Name VARCHAR(20), Price INT)")
#cursor.close
#print cursor.name


for i in dir(cursor):
    print i
    
cursor.execute(
        'CREATE TABLE mcduser ('
        'name varchar(80),'
        'id int,'
        'dept int,'
        'skill text,'
        'update date'
        ')'
    )

#插入一列
cursor.execute(
        'ALTER TABLE mcduser ADD COLUMN gg integer NOT NULL'
    )
cursor.execute(
        'ADD COLUMN target integer'
    )


#插入值
cursor.execute("INSERT INTO mcduser "
        "VALUES('Gopher', 'China Beijing', 100, '2017-05-27')")

#查詢
cursor.execute("SELECT * FROM mcduser")

rows = cursor.fetchall()
for i in rows:
    print i

for row in rows:
    print('name=' + str(row[0]) + ' address=' + str(row[1]) + 
        ' age=' + str(row[2]) + ' date=' + str(row[3]))
    
#更新數據 
#cursor.execute("UPDATE Employee SET age = 12 WHERE name ='Gopher'"）

#刪除數據 
#cursor.execute（ "DELETE FROM Employee WHERE name ='Gopher'"）   
    
    
#提交    
conn.commit()
#關閉
cursor.close()
conn.close()

cursor.description
cursor.query
#// Result: 'SELECT * FROM Employee' //