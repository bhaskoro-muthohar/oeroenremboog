import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class CorrelationHeatmap:
    def __call__(self):
        self.correlation_heatmap()

    def correlation_heatmap(self):
        st.title('Correlation Heatmap')
        mock_data = pd.DataFrame({'A': [1, 2, 3], 'B': [2, 3, 4], 'C': [3, 4, 5]})
        corr = mock_data.corr()

        fig, ax = plt.subplots()

        sns.heatmap(corr, annot=True, ax=ax)

        st.pyplot(fig)