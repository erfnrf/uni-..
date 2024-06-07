import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('/mnt/data/test.db')
cursor = conn.cursor()

# Fetch all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Fetch the schema for each table
db_schema = {}
for table in tables:
    table_name = table[0]
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    db_schema[table_name] = columns

# Close the connection
conn.close()

# Print the schema
print(db_schema)
