import sqlite3

connect = sqlite3.connect('db.sqlite3')
cursor = connect.cursor()

sql = '''
    SELECT * FROM cars_cars;
'''

data = cursor.execute(sql)
print(data.fetchall())