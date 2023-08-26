import streamlit as st
from .interactive_map import InteractiveMap

class TableView:
    def __call__(self):
        self.table_view()

    def table_view(self):
        interactive_map = InteractiveMap()
        indonesia_map = interactive_map()

        st.title('Table Data from Interactive Map')

        if indonesia_map is not None:
            table_data = indonesia_map[['Propinsi', 'Mock Value']]
            table_data.rename(columns={'Propinsi': 'Province', 'Mock Value': 'Value'}, inplace=True)
            st.write(table_data)
        else:
            st.write("No data available")
