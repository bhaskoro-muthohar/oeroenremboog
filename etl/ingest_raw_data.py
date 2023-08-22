import duckdb
import pandas as pd
from tqdm import tqdm
import os

def read_raw_data():
    files = {
        "DM2019_kepesertaan": "raw_data/DM2019_kepesertaan.dta",
        "DM2020_kepesertaan": "raw_data/DM2020_kepesertaan.dta",
        "DM2021_fkrtldxsekunder": "raw_data/DM2021_fkrtldxsekunder.dta",
        "DM2021_fktpnonkapitasi": "raw_data/DM2021_fktpnonkapitasi.dta",
        "DM2021_kepesertaan": "raw_data/DM2021_kepesertaan.dta",
    }
    return {name: pd.read_stata(path) for name, path in files.items()}

def convert_to_parquet(data):
    parquet_paths = {}
    for name, df in data.items():
        for col in df.select_dtypes(['category']):
            df[col] = df[col].astype(str)
        parquet_path = f"raw_data/{name}.parquet"
        df.to_parquet(parquet_path)
        parquet_paths[name] = parquet_path
    return parquet_paths

def create_tables(cursor):
    tables = [
        "dm2019_kepesertaan",
        "dm2020_kepesertaan",
        "dm2021_fkrtldxsekunder",
        "dm2021_fktpnonkapitasi",
        "dm2021_kepesertaan",
    ]
    for table in tables:
        cursor.execute(f"DROP TABLE IF EXISTS {table};")

    cursor.execute("""
    CREATE TABLE dm2019_kepesertaan (
        PSTV01 VARCHAR,
        PSTV02 VARCHAR,
        PSTV03 DATE,
        PSTV04 VARCHAR,
        PSTV05 VARCHAR,
        PSTV06 VARCHAR,
        PSTV07 VARCHAR,
        PSTV08 VARCHAR,
        PSTV09 VARCHAR,
        PSTV10 VARCHAR,
        PSTV11 VARCHAR,
        PSTV12 VARCHAR,
        PSTV13 VARCHAR,
        PSTV14 VARCHAR,
        PSTV15 FLOAT,
        PSTV16 VARCHAR,
        PSTV17 VARCHAR,
        PSTV18 FLOAT
    );
    """)

    cursor.execute("""
    CREATE TABLE dm2020_kepesertaan (
        PSTV01 VARCHAR,
        PSTV02 VARCHAR,
        PSTV03 DATE,
        PSTV04 VARCHAR,
        PSTV05 VARCHAR,
        PSTV06 VARCHAR,
        PSTV07 VARCHAR,
        PSTV08 VARCHAR,
        PSTV09 VARCHAR,
        PSTV10 VARCHAR,
        PSTV11 VARCHAR,
        PSTV12 VARCHAR,
        PSTV13 VARCHAR,
        PSTV14 VARCHAR,
        PSTV15 FLOAT,
        PSTV16 VARCHAR,
        PSTV17 VARCHAR,
        PSTV18 FLOAT
    );
    """)

    cursor.execute("""
    CREATE TABLE dm2021_fkrtldxsekunder (
        FKL02 VARCHAR,
        FKL24 VARCHAR,
        FKL24A VARCHAR,
        FKL24B VARCHAR
    );
    """)

    cursor.execute("""
    CREATE TABLE dm2021_fktpnonkapitasi (
        PSTV01 INTEGER,
        PSTV02 INTEGER,
        PSTV15 FLOAT,
        PNK02 VARCHAR,
        PNK03 DATETIME,
        PNK04 DATETIME,
        PNK05 DATETIME,
        PNK06 VARCHAR,
        PNK07 VARCHAR,
        PNK08 VARCHAR,
        PNK09 VARCHAR,
        PNK10 VARCHAR,
        PNK11 VARCHAR,
        PNK12 VARCHAR,
        PNK13 VARCHAR,
        PNK13A VARCHAR,
        PNK14 VARCHAR,
        PNK15 VARCHAR,
        PNK16 VARCHAR,
        PNK17 VARCHAR,
        PNK18 VARCHAR,
        PNK19 FLOAT,
        PNK20 FLOAT
    );
    """)

    cursor.execute("""
    CREATE TABLE dm2021_kepesertaan (
        PSTV01 VARCHAR,
        PSTV02 VARCHAR,
        PSTV03 DATE,
        PSTV04 VARCHAR,
        PSTV05 VARCHAR,
        PSTV06 VARCHAR,
        PSTV07 VARCHAR,
        PSTV08 VARCHAR,
        PSTV09 VARCHAR,
        PSTV10 VARCHAR,
        PSTV11 VARCHAR,
        PSTV12 VARCHAR,
        PSTV13 VARCHAR,
        PSTV14 VARCHAR,
        PSTV15 FLOAT,
        PSTV16 VARCHAR,
        PSTV17 VARCHAR,
        PSTV18 FLOAT
    );
    """)

def ingest_parquet_files(conn, parquet_paths):
    cursor = conn.cursor()
    for name, path in tqdm(parquet_paths.items(), desc="Ingesting Parquet files"):
        table_name = name.lower()
        cursor.execute(f"COPY {table_name} FROM '{path}' (FORMAT 'parquet');")
        conn.commit()
    cursor.close()

def main():
    # Read raw data
    data = read_raw_data()

    # Convert to Parquet
    parquet_paths = convert_to_parquet(data)

    # Connect to DuckDB
    conn = duckdb.connect('oeroenremboog.db')
    cursor = conn.cursor()

    # Create tables
    create_tables(cursor)

    # Ingest Parquet files into DuckDB
    ingest_parquet_files(conn, parquet_paths)

    # Close connection
    cursor.close()

if __name__ == "__main__":
    main()
