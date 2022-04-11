import sqlite3

# Connect to database
connection = sqlite3.connect('q5.db')

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

# Create job_history table
cursor.execute("""CREATE TABLE jobs_history (
    employee_id integer,
    start_date text,
    end_date text,
    department_id integer,
    job_id integer,
    FOREIGN KEY (job_id) REFERENCES jobs (job_id)
)""")

# insert data
jobs_history = [
    (1, "2019-01-01", "2019-12-31", 101, 1),
    (2, "2019-01-01", "2019-12-31", 102, 2),
    (3, "2019-01-01", "2019-12-31", 103, 3)
]

cursor.executemany("INSERT INTO jobs_history VALUES (?, ?, ?, ?, ?)", jobs_history)

# query to db
cursor.execute("SELECT * FROM jobs")
jobs = cursor.fetchall()
print(jobs)
print('-----------------------------------------------------')
cursor.execute("SELECT * FROM jobs_history")
jobs_history = cursor.fetchall()
print(jobs_history)

# Commit changes
connection.commit()

# Close connection
connection.close()