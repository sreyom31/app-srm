from datetime import datetime
import sqlite3

# Connect to database
connection = sqlite3.connect('q1.db')

# Create cursor
cursor = connection.cursor()

# Create table
# cursor.execute("""CREATE TABLE recipes (
#     name text,
#     description text,
#     category_id integer,
#     chef_id text,
#     created timestamp
# )""")

# insert data
# time = datetime.now()
# recipes = [
#     ("paneer masala", "p m", 101, "BL00001", time),
#     ("chicken masala", "c m", 102, "BL00002", time),
#     ("butter naan", "chinese", 103, "BL00003", time),
# ]

# cursor.executemany("INSERT INTO recipes VALUES (?, ?, ?, ?, ?)", recipes)

# query to db
cursor.execute("SELECT * FROM recipes WHERE description = 'chinese'")
recipes = cursor.fetchall()
print(len(recipes))
print('-----------------------------------------------------')

cursor.execute("SELECT category_id, name FROM recipes WHERE chef_id = 'BL00002'")
r = cursor.fetchall()
print(r)
print('-----------------------------------------------------')

cursor.execute("SELECT description FROM recipes WHERE name LIKE 'p%'")
d = cursor.fetchall()
print(d)
print('-----------------------------------------------------')

# Commit changes
connection.commit()

# Close connection
connection.close()