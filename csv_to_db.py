import csv
import sqlite3

# with open('leg_and_foot.csv', 'r', encoding='utf-8') as f:
#     fields = ['name_of_idiom', 'translation', 'definition']
#     reader = csv.DictReader(f, fields, delimiter=';')
#     for row in reader:
#         a = row['name_of_idiom']
#         b = row['translation']
#         c = row['definition']
#         print(a,b,c)
conn = sqlite3.connect("idioms.db")
cursor = conn.cursor()
cursor.execute("""INSERT INTO idioms
                VALUES (5, 4, 3, 2)"""
               )
conn.commit()