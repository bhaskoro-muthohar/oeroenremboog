import duckdb

def connect_to_db():
    conn = duckdb.connect('oeroenremboog.db')
    # Additional configuration here
    return conn