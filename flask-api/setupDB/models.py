# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, Text, DateTime
from setupDB.database import Base
from datetime import datetime


class WikiContent(Base):
    __tablename__ = 'wikicontents'                  # テーブル名
    id = Column(Integer, primary_key=True)          # カラム１(id)データベースの列
    title = Column(String(128), unique=True)        # カラム２(title)　
    body = Column(Text)                             # カラム3(body)
    date = Column(DateTime, default=datetime.now()) # カラム４(date) デフォルト現在日時を設定

    def __init__(self, title=None, body=None, date=None):
        self.title = title
        self.body = body
        self.date = date

    def to_dict(self):
        return dict(
            title = self.title,
            body = self.body,
            date = self.date
        )

    def __repr__(self):
        return '<Title %r>' % (self.title)

#クラスがテーブル
class Userdata(Base):
    __tablename__ = 'Userdata'                      #テーブル名
    id = Column(Integer,primary_key = True)         #カラム(id)
    title = Column(String(128))                     #カラム(title)
    userID = Column(String(20), unique = True)      #カラム(userID)
    password = Column(String(20))                   #カラム(password)

    def __init__(self,title=None,userID=None,password=None):
        self.title = title
        self.userID = userID
        self.password = password

    def to_dict(self):
        return dict(
            title = self.title,
            userID = self.userID,
            password = self.password
        )
    def __repr__(self):
        return '<Title %r>' % (self.title)

class Scheduledata(Base):
    __tablename__ = 'Scheduledata'                   # テーブル名
    id = Column(Integer, primary_key=True)           # カラム１(id)
    title = Column (String(128))                     # カラム2(title)
    year = Column(Integer)                              # カラム3(年)
    month = Column(Integer)                             # カラム4(月)
    day = Column(Integer)                               # カラム5(日)
    starthour = Column(Integer)                         # カラム6(開始時)
    startminute = Column(Integer)                       # カラム7(開始分)
    endhour = Column(Integer)                           # カラム8(終了時)
    endminute = Column(Integer)                          # カラム9(終了分)

    def __init__(self,title=None,year=None, month=None, day=None, starthour=None,
                startminute=None, endhour=None, endminute=None):
        self.title = title
        self.year = year
        self.month = month
        self.day = day
        self.starthour = starthour
        self.startminute = startminute
        self.endhour = endhour
        self.endminute = endminute

    def to_dict(self):
        return dict(
            title = self.title,
            year = self.year,
            month = self.month,
            day = self.day,
            starthour = self.starthour,
            startminute = self.startminute,
            endhour = self.endhour,
            endminute = self.endminute
        )

    def __repr__(self):
        return '<Title %r>' % (self.title)
