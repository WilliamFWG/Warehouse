from dbconn_sqlalchemy import Session,Employees,Departments

#创建到数据库会话类
session=Session()

#对数据库进行增删改查
###################################################################################
#增加部门
# hr = Departments(dep_id=1,dep_name='人事部')
# ops = Departments(dep_id=2,dep_name='运维部')
# dev = Departments(dep_id=3,dep_name='开发部')
#qa = Departments(dep_id=4,dep_name='测试部')
# market = Departments(dep_id=5,dep_name='市场部')
# sales = Departments(dep_id=6,dep_name='销售部')
# session.add_all([hr,ops,dev,market,qa,sales])
####################################################################################
# #创建员工记录
# William = Employees(emp_id=1,emp_name='William',emp_birthday='1980-04-09',
#                     emp_email='william@qq.com',dep_id=2)
# Minnie = Employees(emp_id=2,emp_name='Minnie',emp_birthday='1983-07-14',
#                     emp_email='minnie@qq.com',dep_id=5)
# Joe = Employees(emp_id=3,emp_name='Joe',emp_birthday='2011-06-03',
#                     emp_email='Joe@qq.com',dep_id=3)
# Dachui = Employees(emp_id=4,emp_name='Dachui',emp_birthday='1980-12-11',
#                     emp_email='dachui@qq.com',dep_id=1)
# Xiaochui = Employees(emp_id=5,emp_name='Xiaochui',emp_birthday='1981-1-19',
#                     emp_email='Xiaochui@qq.com',dep_id=4)
# session.add_all([William,Minnie,Joe,Dachui,Xiaochui])
####################################################################################
#查询的参数是类（表），返回的是实例列表（即表里的每行记录）
# qset1=session.query(Departments)   #部门表内的所有select * from Department;  该指令仅是一条sql语句
# qset1.all()   #返回表内所有行的列表  【行1，行2，行3.。。。】
# for line in qset1:
#     print(line.dep_id,line.dep_name)     #循环取出每一行的相关字段
##########################################################################################
#查询的参数是变量，返回的是由变量组成的元组列表
# qset2=session.query(Employees.emp_name,Employees.emp_email)
# print(qset2.all())
##########################################################################################
#实现排序
# qset3=session.query(Employees).order_by(Employees.emp_id)
# for line in qset3:
#     print(line.emp_id,line.emp_name,line.emp_email)
###########################################################################################
#取切片
# qset4=session.query(Employees).order_by(Employees.emp_id)[2:4]
# for line in qset4:
#     print(line.emp_id,line.emp_name,line.emp_email
##########################################################################################
#过滤和二次过滤
# qset5=session.query(Employees).filter(Employees.emp_id>2)
# qset5=qset5.filter(Employees.emp_birthday=='2011-06-03')
# for line in qset5:
#     print(line.emp_id,line.emp_name,line.emp_email)
##########################################################################################
# #模糊查询
# qset6=session.query(Employees).filter(Employees.emp_email.like('%qq.com'))
# for line in qset6:
#     print(line.emp_id, line.emp_name, line.emp_email)
##########################################################################################
# #in 和 not in
# qset7=session.query(Employees).filter(~Employees.emp_id.in_((2,3)))
# for line in qset7:
#     print(line.emp_id, line.emp_name, line.emp_email)
##########################################################################################
#多表查询
#两张表有主外建约束关系,所以查询时,他们自动匹配
#查询时,要先写Employees,join时就写Departments
# qset8=session.query(Employees.emp_name,Departments.dep_name).join(Departments)
# for line in qset8:
#     print(line.emp_name,line.dep_name)

##########################################################################################
# #更新:
# qset9=session.query(Employees).filter(Employees.emp_id==2)
# tgt=qset9.first()
# tgt.emp_name="Minnie Niu"
##########################################################################################
#删除
qset10=session.query(Employees).filter(Employees.emp_id==5)
tgt=qset10.first()
session.delete(tgt)


##########################################################################################

#如果对数据库有改动，需要确认，提交crud语句
session.commit()


#关闭会话
session.close()
