import sqlite3

# Connect to database
connection = sqlite3.connect('q4.db')

# Create cursor
cursor = connection.cursor()

# Create table
cursor.execute("""CREATE TABLE jobs (
    job_id integer PRIMARY KEY,
    job_title text,
    min_salary integer,
    max_salary integer
)""")

# insert data
jobs = [
    (1, "sde", 4000000, 6000000),
    (2, "waiter", 10000, 20000),
    (3, "electrical engineer", 1000000, 2500000)
]

cursor.executemany("INSERT INTO jobs VALUES (?, ?, ?, ?)", jobs)

# query to db
cursor.execute("SELECT * FROM jobs")
jobs = cursor.fetchall()
print(jobs)
print('-----------------------------------------------------')

# Commit changes
connection.commit()

# Close connection
connection.close()