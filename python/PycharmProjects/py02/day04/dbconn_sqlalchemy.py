from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#创建数据库引擎


engine=create_engine(
    #固定格式： 'mysql+pymysql://user:password@ip/database?options'
    'mysql+pymysql://root:123qqq...A@192.168.1.100/sqlalchemyDB?charset=utf8',
    encoding='utf8',
    echo=True  #显示调试信息，生产环境无需设置
)

#创建连接数据库的会话类，用来做之后的增删改查
Session=sessionmaker(bind=engine)




Base = declarative_base()   #生成实体基类

class Departments(Base):
    __tablename__ = 'Departments'  #指定类对应表
    dep_id = Column(Integer,primary_key=True)
    dep_name=Column(String(20),unique=True)

class Employees(Base):
      __tablename__ = 'Employees'
      emp_id=Column(Integer,primary_key=True)
      emp_name=Column(String(30))
      emp_birthday=Column(Date)
      emp_email=Column(String(50))
      dep_id=Column(Integer,ForeignKey('Departments.dep_id'))

class Salary(Base):
    __tablename__='Salary'
    id=Column(Integer,primary_key=True)
    date=Column(Date)
    emp_id=Column(Integer,ForeignKey('Employees.emp_id'))
    basic=Column(Integer)
    award=Column(Integer)



if __name__ == '__main__':
    #如果库中没有表则创建，有的话进行关联，不会再次创建
    Base.metadata.create_all(engine)







