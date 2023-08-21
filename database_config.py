import duckdb

def connect_to_db():
    conn = duckdb.connect('my_database.duckdb')
    # Additional configuration here
    return conn