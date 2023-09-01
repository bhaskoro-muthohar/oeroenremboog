import streamlit as st
import pandas as pd

class GambaranUmum:
    def __call__(self):
        self.gambaran_umum()

    def gambaran_umum(self):
        st.image("https://bpjs-kesehatan.go.id/assets/img/logo/logo-color.svg", width=400)
        st.title('Halaman 01: Gambaran Umum Kasus DM Tipe I & II')
        mock_data = pd.DataFrame({'Value': [50, 60, 70, 80, 90]})
        st.bar_chart(mock_data['Value'])