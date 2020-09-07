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

# #编写sql语句
# create_dep='''create table departments(
# dep_id char(10),dep_name varchar(20),
# PRIMARY KEY (dep_id)
# )
# '''
# create_emp='''create table employees(
# emp_id char(10),emp_name VARCHAR (20),birth_date DATE ,email VARCHAR(50),
# dep_id char(10),
# PRIMARY KEY(emp_id),
# FOREIGN KEY(dep_id) REFERENCES departments(dep_id)
# )
# '''
# create_salary='''create table salary(
# id char(10),date DATE,emp_id char(10),basic INT ,
# awards int,
# PRIMARY KEY (id),
# FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
# )
# '''
insert1='insert into departments VALUES (%s,%s)'
deps=[(1,'hr'),(2,'ops'),(3,'dev'),(4,'market'),(5,'qa'),(6,'sales')]

#执行sql语句
# cur.execute(create_dep)
# cur.execute(create_emp)
# cur.execute(create_salary)
cur.executemany(insert1,deps)

#对数据库改动，需要commit确认提交
conn.commit()

#关闭游标以及连接
cur.close()
conn.close()


