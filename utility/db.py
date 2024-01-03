# Create a sqlite3 database and table for storing the data
# Path: utility/db.py

from sqlalchemy import create_engine

engine = create_engine("sqlite:///database.db", echo=True)
test_engine = create_engine("sqlite:///test_database.db")





