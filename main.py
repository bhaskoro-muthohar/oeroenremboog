from database_config import connect_to_db

conn = connect_to_db()
result = conn.execute("SELECT * FROM system.information_schema.tables").fetchall()
print(result)
conn.close()