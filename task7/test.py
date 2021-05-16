import sqlite3
from sqlite3.dbapi2 import Cursor
from flask import Flask
from flask.templating import render_template
from flask.globals import request
import os


path_to_bases = 'task7/resources/databases/'


def connect_base(base_name):
    return sqlite3.connect(path_to_bases+base_name+'.sqlite')


conn = connect_base('a1')
cursor = conn.cursor()

# cursor.execute("""CREATE TABLE albums
                #   (title text, artist text, release_date text,
                #    publisher text, media_type text)
            #    """)

cursor.execute("""CREATE TABLE x 
                  (title text, release_date text,
                   publisher text, media_type text)
               """)

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cursor.fetchall())