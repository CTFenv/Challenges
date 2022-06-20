# SQL file to sqlite3 database script

# Import statements
import sqlite3, os


# Setting paths
main_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dbinit_file = os.path.join(main_folder, "config", "db_init.sql")
sqlite3_db = os.path.join(main_folder, "app", "database.db")


# Importing file
connection = sqlite3.connect(sqlite3_db)

with open(dbinit_file) as infile:
    print(f"Importing '{dbinit_file}' into '{sqlite3_db}'.")
    connection.executescript(infile.read())

connection.commit()
connection.close()
print("Import done.")
