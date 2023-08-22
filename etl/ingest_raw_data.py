import os
import duckdb
from tqdm import tqdm
import glob

def create_tables(cursor):
    tables = [
        "dm2019_kepesertaan",
        "dm2020_kepesertaan",
        "dm2021_fkrtldxsekunder",
        "dm2021_fktpnonkapitasi",
        "dm2021_kepesertaan",
        "dm2021_fkrtl",
        "dm2021_fktpkapitasi"
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

    cursor.execute("""
    CREATE TABLE dm2021_fkrtl (
        PSTV01 INTEGER,
        PSTV02 INTEGER,
        PSTV15 FLOAT,
        FKP02 VARCHAR,
        FKL02 VARCHAR,
        FKL03 DATETIME,
        FKL04 DATETIME,
        FKL05 VARCHAR,
        FKL06 VARCHAR,
        FKL07 VARCHAR,
        FKL08 VARCHAR,
        FKL09 VARCHAR,
        FKL10 VARCHAR,
        FKL11 VARCHAR,
        FKL12 VARCHAR,
        FKL13 VARCHAR,
        FKL14 VARCHAR,
        FKL15 VARCHAR,
        FKL15A VARCHAR,
        FKL16 VARCHAR,
        FKL16A VARCHAR,
        FKL17 VARCHAR,
        FKL17A VARCHAR,
        FKL18 VARCHAR,
        FKL18A VARCHAR,
        FKL19 VARCHAR,
        FKL19A VARCHAR,
        FKL20 VARCHAR,
        FKL21 VARCHAR,
        FKL22 INTEGER,
        FKL23 VARCHAR,
        FKL25 VARCHAR,
        FKL26 VARCHAR,
        FKL27 VARCHAR,
        FKL28 VARCHAR,
        FKL29 VARCHAR,
        FKL30 VARCHAR,
        FKL31 VARCHAR,
        FKL32 INTEGER,
        FKL33 VARCHAR,
        FKL34 INTEGER,
        FKL35 VARCHAR,
        FKL36 VARCHAR,
        FKL37 INTEGER,
        FKL38 VARCHAR,
        FKL39 VARCHAR,
        FKL40 INTEGER,
        FKL41 VARCHAR,
        FKL42 VARCHAR,
        FKL43 INTEGER,
        FKL44 VARCHAR,
        FKL45 VARCHAR,
        FKL46 INTEGER,
        FKL47 INTEGER,
        FKL48 INTEGER,
    );
    """)

    cursor.execute("""
    CREATE TABLE dm2021_fktpkapitasi (
        PSTV01 INTEGER,
        PSTV02 INTEGER,
        PSTV15 FLOAT,
        FKP02 VARCHAR,
        FKP03 DATETIME,
        FKP04 DATETIME,
        FKP05 INTEGER,
        FKP06 INTEGER,
        FKP07 INTEGER,
        FKP08 INTEGER,
        FKP09 INTEGER,
        FKP10 INTEGER,
        FKP11 INTEGER,
        FKP12 INTEGER,
        FKP13 INTEGER,
        FKP14 INTEGER,
        FKP14A VARCHAR,
        FKP15 VARCHAR,
        FKP15A VARCHAR,
        FKP16 INTEGER,
        FKP17 INTEGER,
        FKP18 INTEGER,
        FKP19 INTEGER,
        FKP20 INTEGER,
        FKP21 INTEGER,
        FKP22 INTEGER,
    );
    """)

def ingest_parquet_files(conn):
    parquet_paths = glob.glob("raw_data/*.parquet")
    cursor = conn.cursor()
    for path in tqdm(parquet_paths, desc="Ingesting Parquet files"):
        table_name = os.path.basename(path).split('.')[0].lower()
        cursor.execute(f"COPY {table_name} FROM '{path}' (FORMAT 'parquet');")
        conn.commit()
    cursor.close()

def main():
    # Connect to DuckDB
    conn = duckdb.connect('oeroenremboog.db')
    cursor = conn.cursor()

    # Create tables
    create_tables(cursor)

    # Ingest Parquet files into DuckDB
    ingest_parquet_files(conn)

    # Close connection
    cursor.close()

if __name__ == "__main__":
    main()
