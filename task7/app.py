import sqlite3
from sqlite3.dbapi2 import Cursor
from flask import Flask
from flask.templating import render_template
from flask.globals import request
import os


class Base:
    def __init__(self, name):
        self.name = name
        self.tables = []  


class Data:
    def __init__(self, base_names):
        self.bases =  []
        for base_name in base_names:
            self.bases.append(Base(base_name)) 


app = Flask(__name__)
path_to_bases = 'task7/resources/databases/'


def validate_base_name(name):
    if name == '' or name ==' ' or name == '.':
        return False
    else:
        return True


def connect_base(base_name):
    return sqlite3.connect(path_to_bases+base_name+'.sqlite')


@app.route('/index', methods=['POST','GET'])
def index():
    if request.method == "POST":
        base_name = request.form['baseName']
        if validate_base_name(base_name):
            connect_base(base_name)
    data = Data([os.path.splitext(filename)[0] for filename in os.listdir(path_to_bases)])
    return render_template('index.html', data=data)


@app.route('/get_tables', methods=['POST', 'GET'])
def get_tables():
    data = Data([os.path.splitext(filename)[0] for filename in os.listdir(path_to_bases)])
    if request.method == "POST":
        base_name = request.form['btnGetTables']
        cursor = connect_base(base_name).cursor()
        list = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        for i in range(len(data.bases)):
            if data.bases[i].name == base_name:
                data.bases[i].tables = [table[0] for table in list] 
                break
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True) 