!pip install tinydb

from tinydb import TinyDB, Query

db = TinyDB('db.json')
Ft = Query()

def register_database(a, b, c, d):
  name = a
  age = b
  cel = c
  password = d

  dados = {  'NAME':name,
            'AGE':age,
            'CEL':cel,
            'PASSWORD':password
          }

  db.insert(dados)

a = 1
b = 2
c = 3
d = 4

register_database(a, b, c, d)


from tinydb import TinyDB, Query
from tinydb import where
import pandas as pd

table = pd.read_excel('Dados_Tetes.xlsx')

table

table.fillna(0, inplace=True)

db = TinyDB('db2.json')
Ft = Query()

header = table.columns
header

dados_DB = {}
for a in header:
  print(a)
  for b in table[a]:
    DB = {a:b}
    db.insert(DB)
    print(a,b)

db.all()

result_db = db.search(Ft.Real != 'null')
result_db


db.search(where('LAST_NAME') == 'Eller')