import sqlite3

db = sqlite3.connect('database_test.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS patient(name TEXT, 
                                                     second_name TEXT, 
                                                     age INT)'''
               )
db.commit()


class Registration:
    pass
