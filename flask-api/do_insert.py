from setupDB.database import init_db
from setupDB.database import db_session
from setupDB.models import WikiContent
from setupDB.models import Scheduledata
from setupDB.models import Userdata

# idには連番。title、textを指定。dateは日時が勝手に入る(model.pyのデフォルト設定により)
c1 = WikiContent("Flask", "micro framework")  # カラム1:'Flask' カラム2:'micro framework'を指定してインスタンス作成
db_session.add(c1)                            # insert実行
db_session.commit()                           # commit実行


d1 = Userdata("userdata","Test","pass")
db_session.add (d1)

d2 = Scheduledata("date",2018,12,6,16,53,17,53)
db_session.add(d2)

db_session.commit()
