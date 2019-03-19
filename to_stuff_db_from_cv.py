from webapp.model import db, Idioms
import csv

def create_db(name_of_idiom,translation,definition):
    idioms_db = Idioms(name_of_idiom=name_of_idiom, translation=translation, definition=definition)
    db.session.add(idioms_db)
    db.session.commit()


# with open('leg_and_foot.csv', 'r', encoding='utf-8') as f:
#     reader = csv.DictReader(f, delimiter=';')
#     for row in reader:
#         print(row)
