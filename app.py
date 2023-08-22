import streamlit as st
import pandas as pd
from database_config import connect_to_db

def fetch_data():
    conn = connect_to_db()
    query = "SELECT * FROM dm2021_kepesertaan"
    result = conn.execute(query).fetch_df()
    conn.close()
    return result

def main():
    st.title('DuckDB Data Viewer')
    st.subheader('Data from dm2021_kepesertaan table')

    data = fetch_data()
    st.write(data)

if __name__ == "__main__":
    main()
