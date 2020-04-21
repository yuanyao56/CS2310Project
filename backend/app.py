import json
import math
from datetime import datetime
import re
from flask import Flask, redirect, url_for, request
from flask import jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
cors = CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databse/temp.db'
db = SQLAlchemy(app)

start = False
type = -1
tempSet = -1
knobSet = -1
bestTemp = 72
cur = 1
curTemp = -1
lastchange = -10


class Temp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.TIMESTAMP, unique=False, nullable=False)
    read = db.Column(db.FLOAT, unique=False, nullable=False)

    def __init__(self, i, t, r):
        self.id = i
        self.time = t
        self.read = r


@app.cli.command('initdb')
def initdb_command():
    db.drop_all()
    db.create_all()
    db.session.commit()
    print('Initialized the database.')
    with open("tempRead/tempReading.txt", 'r') as temp:
        temp.readline()
        line = temp.readline()
        while line:
            line = temp.readline()
            if line != '':
                parts = re.split("\s[\s]+", line)
                date = datetime.strptime(parts[1], '%Y/%m/%d %H:%M:%S')
                r = 32 + float(parts[2][:-1]) * 9 / 5
                db.session.add(Temp(parts[0], date, r))
        db.session.flush()
        db.session.commit()


@app.route('/')
def hello_world():
    if not start:
        return redirect(url_for('start'))
    else:
        return redirect(url_for('home'))


@app.route('/start', methods=['GET', 'POST'])
def start():
    if request.method == 'POST':
        data = request.get_json()
        global type
        type = data['type']
        print("get type " + type)
        return ""


@app.route('/setTemp', methods=['GET', 'POST'])
def set():
    if request.method == 'POST':
        data = request.get_json()
        global tempSet
        tempSet = float(data['temp'])
        print("get temp setting " + data['temp'])
        return json.dumps({'type': type})


@app.route('/setKnob', methods=['GET', 'POST'])
def setKnob():
    if request.method == 'POST':
        data = request.get_json()
        global knobSet
        knobSet = float(data['temp'])
        print("get knob setting " + str(data['temp']))
        return json.dumps({'type': type})


@app.route('/change', methods=['GET', 'POST'])
def change():
    if request.method == 'POST':
        global lastchange
        if lastchange >= 0:
            print("change: return Please wait for few minutes for air conditioner to work")
            return json.dumps({'message': "Please wait for few minutes for air conditioner to work", 'change': '0'})
        lastchange = 10
        data = request.get_json()
        feeling = data['type']
        message = ""
        global tempSet
        if type == '0':
            # digital
            diff = -1
            if abs(curTemp - bestTemp) > 0.75:
                diff = math.log(abs(curTemp - bestTemp), 5) + 0.75
            else:
                diff = 0.5
            tempSet = round(tempSet + diff if feeling == 0 else tempSet - diff, 2)
            print("return " + "Set temperature to " + str(tempSet))
            return json.dumps({'message': "Set temperature to " + str(tempSet), 'change': '1'})

        else:
            # knob
            global knobSet
            if abs(curTemp - bestTemp) > 2:
                diff = math.log(abs(curTemp - bestTemp)) + 2
            else:
                diff = 1
            diff = diff / 0.8
            newangle = round(knobSet + diff if feeling == 0 else tempSet - diff, 2)
            if newangle > 50:
                newangle = 49
            if newangle < 0:
                newangle = 1
            # request 0 cold, 1 hot
            message = "Set Knob to " + str(newangle)
            print("change:return " + str(newangle))
            return json.dumps({'message': message, 'angle': newangle, 'change': '1'})


@app.route('/curTemp')
def read():
    global cur
    global curTemp
    global lastchange
    global tempSet
    cur += 1
    lastchange -= 1

    curTemp = Temp.query.filter_by(id=cur).first().read
    if lastchange <= -20:
        tempSet = curTemp
    print("send " + str(cur) + " " + str(curTemp))
    return str(curTemp)


import threading

# 启动运行
if __name__ == '__main__':
    app.run()
