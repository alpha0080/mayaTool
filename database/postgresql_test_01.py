import sys

sys.path.append('C:/Python27/Lib')
sys.path.append('C:/Python27/Lib/site-packages')

import psycopg2


# connect to postgreSQL server@192.168.161.47
#conn = psycopg2.connect(database='mydb', user='postgres', password='5j/u.42017', host='192.168.161.47', port='5432', sslmode='disable')
conn = psycopg2.connect(database='3D_db', user='postgres', password='5j/u.42017', host='192.168.161.47', port='5432')

cursor = conn.cursor()  #�Ψӫإ߾�Ӹ�Ʈw�ާ@�� tag
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

#���J�@�C
cursor.execute(
        'ALTER TABLE mcduser ADD COLUMN gg integer NOT NULL'
    )
cursor.execute(
        'ADD COLUMN target integer'
    )


#���J��
cursor.execute("INSERT INTO mcduser "
        "VALUES('Gopher', 'China Beijing', 100, '2017-05-27')")

#�d��
cursor.execute("SELECT * FROM mcduser")

rows = cursor.fetchall()
for i in rows:
    print i

for row in rows:
    print('name=' + str(row[0]) + ' address=' + str(row[1]) + 
        ' age=' + str(row[2]) + ' date=' + str(row[3]))
    
#��s�ƾ� 
#cursor.execute("UPDATE Employee SET age = 12 WHERE name ='Gopher'"�^

#�R���ƾ� 
#cursor.execute�] "DELETE FROM Employee WHERE name ='Gopher'"�^   
    
    
#����    
conn.commit()
#����
cursor.close()
conn.close()

cursor.description
cursor.query
#// Result: 'SELECT * FROM Employee' //