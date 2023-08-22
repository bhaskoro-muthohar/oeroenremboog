from database_config import connect_to_db

conn = connect_to_db()
result = conn.execute("SELECT * FROM dm2021_kepesertaan LIMIT 10").fetchall()
print(result)
conn.close()