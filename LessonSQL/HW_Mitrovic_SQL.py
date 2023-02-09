import sqlite3

conn = sqlite3.connect('hw.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT,col_1 TEXT)''')
conn.commit()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT,col_1 INTEGER)''')
conn.commit()
my_list = [1, 'Minsk', 2, 'Moscow', 3, 'Basel']
for i in my_list:
    if type(i) is str:
        len_i = len(i)
        cursor.execute('''INSERT INTO tab_1(col_1) VALUES(?)''', (i,))
        cursor.execute('''INSERT INTO tab_2(col_1) VALUES(?)''', (len_i,))
        conn.commit()

    elif type(i) is int:
        if i % 2 == 0:
            cursor.execute('''INSERT INTO tab_2(col_1) VALUES (?)''', (i,))
        elif i % 2 != 0:
            odd = 'odd nnumber'
            cursor.execute('''INSERT INTO tab_1(col_1) VALUES (?)''', (odd,))
            conn.commit()
cursor.execute('''SELECT * FROM tab_1''')
k = cursor.fetchall()
cursor.execute('''SELECT*FROM tab_2''')
l = cursor.fetchall()
print(k)
print(l)
if len(l) > 5:
    cursor.execute('''DELETE FROM tab_1 WHERE id=1''')
else:
    cursor.execute('''UPDATE tab_1 SET col_1="HELLO" FROM id=1''')
conn.commit()

cursor.execute('''SELECT*FROM tab_1''')
cursor.execute('''SELECT*FROM tab_2''')
l = cursor.fetchall()
k = cursor.fetchall()
print(l)
print(k)
