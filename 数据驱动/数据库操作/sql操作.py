# -*- coding:utf-8 -*-
# Author:D.Gray
import sqlalchemy
from sqlalchemy import Column,String,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = sqlalchemy.create_engine("mysql+pymysql://root:root@localhost/foodscripy?charset=utf8",echo=False)
Base = declarative_base()
class Food(Base):
    __tablename__ = "food"
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    appraise = Column(String(64))
    def __repr__(self):
        return "<id:%s   name:%s  描述：%s>"%(self.id,self.name,self.appraise)
Session_class = sessionmaker(bind=engine)
session = Session_class()
data = session.query(Food).filter(Food.name=="粉皮").all()
print(data[0])

