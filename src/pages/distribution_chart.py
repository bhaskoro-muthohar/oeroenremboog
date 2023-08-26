import streamlit as st
import pandas as pd

class DistributionChart:
    def __call__(self):
        self.distribution_chart()

    def distribution_chart(self):
        st.title('Distribution Chart')
        mock_data = pd.DataFrame({'Value': [50, 60, 70, 80, 90]})
        st.bar_chart(mock_data['Value'])