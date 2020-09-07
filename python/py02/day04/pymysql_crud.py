import pymysql

#创建mysql连接
conn=pymysql.connect(
    host='192.168.1.100',
    port=3306,
    user='root',
    passwd='123qqq...A',
    db='nsd1911',
    charset='utf8')

#创建游标
cur=conn.cursor()

#编写sql语句
# select1='select * from departments'

#执行sql语句
# cur.execute(select1)
# cur.scroll(2,mode='absolute')
# result1=cur.fetchall()
# result1=cur.fetchone()
update1='update departments set dep_name=%s WHERE dep_name=%s'
cur.execute(update1,('human resource','hr'))


conn.commit()
#关闭游标以及连接
cur.close()
conn.close()