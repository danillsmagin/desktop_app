import sqlite3


def connect():
    db = sqlite3.connect('database_test.db')
    return db


def create_table(db):
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS patient(name TEXT, 
                                                     second_name TEXT, 
                                                     age INT)'''
                   )
    db.commit()


def insert_user(db, username, user_second_name, user_age):
    cursor = db.cursor()
    cursor.execute('INSERT INTO patient values (?, ?, ?)', (username, user_second_name, user_age))
    if username is None or user_second_name is None or user_age is None:
        cursor.execute('DELETE FROM patient WHERE patient.name IS NULL AND patient.second_name IS NULL AND patient.age IS NULL')
    db.commit()


def close_connection(db):
    db.close()
