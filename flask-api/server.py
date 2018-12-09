# -*- coding: utf-8 -*-
"""
 Using SQLAlchemy and Flask get db record.(GET)
"""

from flask import *
from setupDB.models import WikiContent
from setupDB.models import Scheduledata
from setupDB.models import Userdata
from setupDB.database import db_session
app = Flask(__name__)
app.config['DEBUG'] = True


# 起動されたサーバーの/にアクセスした時の挙動を記述。
# @app.route("/hoge")で記述すれば、http://127.0.0.1:5000/aaでアクセスした時の挙動を記述できる。
@app.route("/")
def index():
    result = {
        "Message": "GET test"
    }
    return jsonify(result=result)

@app.route("/database")
def show():
    #sqlalchemyで Where 演算子 と postのやりかた　自分の環境に対応
    #使われている flask sqlite sqlalchemy
    contents = WikiContent.query.all()
    data = [l.to_dict() for l in contents]
    return jsonify(data),200

@app.route("/userdatabase",methods=['GET','POST'])
def userdata():
    #sqlalchemyで Where 演算子 と postのやりかた　自分の環境に対応
    #使われている flask sqlite sqlalchemy
    if request.method == 'GET':
        contents = Userdata.query.all()
        data = [l.to_dict() for l in contents]
        return jsonify(data),200
    else :
        # ________________________________
        # POSTテスト用コード
        # # result = {
        # #     "Message": "GET test"
        # # }
        # # return jsonify(result=result)
        # ________________________________

        # POSTデータの取得
        data = request.json
        sql = Userdata(data["title"],data["userID"],data["password"])
        db_session.add(sql)
        db_session.commit()

        result = 'OK'
        return jsonify(result),200


@app.route("/scheduledatabase",methods=['GET','POST'])
def scheduledata():
    #sqlalchemyで Where 演算子 と postのやりかた　自分の環境に対応
    #使われている flask sqlite sqlalchemy
    if request.method == 'GET':
        contents = Scheduledata.query.all()
        data = [l.to_dict() for l in contents]
        return jsonify(data),200
    else :
        data = request.json
        sql = Scheduledata(data["title"],data["year"],data["month"],data["day"],data["starthour"],
                            data["startminute"],data["endhour"],data["endminute"])
        db_session.add(sql)
        db_session.commit()

        result = 'OK'
        return jsonify(result),200


# テスト
# @app.route("/register")
# def register():
#     data = WikiContent("aaaaa", "")
#     db_session.add(data)
#     db_session.commit()
#     return '登録'
if __name__ == "__main__":
    # サーバーの起動
    app.run()
