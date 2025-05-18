# database.py
import pymysql
from pymysql.cursors import DictCursor

def get_connection():
    connection = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='@Gauravpatil123',  # replace this
        database='edupath_db',              # replace with your DB name
        cursorclass=DictCursor
    )
    return connection