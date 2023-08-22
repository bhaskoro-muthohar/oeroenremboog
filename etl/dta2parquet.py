import pandas as pd
import os

def read_raw_data():
    files = {
        "DM2021_fktpkapitasi": "raw_data/DM2021_fktpkapitasi.dta",
    }
    return {name: pd.read_stata(path, convert_categoricals=False) for name, path in files.items()}

def convert_to_parquet(data):
    parquet_paths = {}
    for name, df in data.items():
        parquet_path = f"raw_data/{name}.parquet"
        df.to_parquet(parquet_path)
        parquet_paths[name] = parquet_path
    return parquet_paths

def main():
    # Read raw data
    data = read_raw_data()

    # Convert to Parquet
    convert_to_parquet(data)

if __name__ == "__main__":
    main()