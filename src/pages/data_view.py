import streamlit as st
from database_config import connect_to_db

class DataView:
    def __call__(self):
        self.data_view()

    def data_view(self):
        st.title('Oeroenremboog Data Visualization')

        # Introduction or Context about the data
        st.markdown("""
        ## Context
        The data we're exploring comes from the `dm2021_kepesertaan` table, blablabla
        """)

        # Important Features of the Data
        st.markdown("""
        ## Key Features
        - **ID**: Unique identifier for each participant blablabla
        - ... (add any other important columns here)
        """)

        # Why this data is important
        st.markdown("""
        ## Importance
        Analyzing this data allows us to:
        1. Understand participation patterns.
        """)

        st.subheader('Data Preview')
        data = self.fetch_data()
        st.write(data)

    def fetch_data(self):
        conn = connect_to_db()
        query = "SELECT * FROM dm2021_kepesertaan"
        result = conn.execute(query).fetch_df()
        conn.close()
        return result
