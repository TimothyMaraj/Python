import sqlite3 as dB
import os
from datetime import datetime
import random
from flask import Flask, render_template, request, Response
app = Flask(__name__)


con = dB.connect('webserver_dataBase.db')
print 
with con:
    con.execute(
        '''CREATE TABLE IF NOT EXISTS USER(
        ID INT PRIMARY KEY NOT NULL,
        WORD TEXT,
        FLOAT INTEGER
        );
        ''')

sql = 'INSERT INTO USER (ID, WORD, FLOAT) values(?,?,?)'
data = [
     (1,"temp",77),
     (2,"Air Quality", 90)
]
with con: 
    con.executemany(sql,data)

with con: 
    data = con.execute("SELECT * FROM USER WHERE float <= 5")
    for row in data: 
        print(row)