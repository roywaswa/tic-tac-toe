import sqlite4
from sqlite4 import SQLite4

sql = SQLite4("tic-tac-toe")

sql.connect(debug=True)
sql.