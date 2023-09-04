import streamlit as st
import pandas as pd
import numpy as np
import json
import plotly.express as px
import plotly.graph_objs as go

class GambaranUmum:
    def __call__(self):
        self.gambaran_umum()

    def gambaran_umum(self):
        st.image("https://bpjs-kesehatan.go.id/assets/img/logo/logo-color.svg", width=400)
        st.title('Gambaran Umum Kasus DM Tipe I & II')
        st.subheader('Distribusi Jumlah Kasus per Jenis Diagnosis (Kasus DM Ditandai Merah Jingga) #ff4500')

        data_json = '''
            [{
            "keluhan": "Lainnya",
            "jumlah_kunjungan": "422474"
            }, {
            "keluhan": "DM Tipe I",
            "jumlah_kunjungan": "99523"
            }, {
            "keluhan": "DM Tipe II",
            "jumlah_kunjungan": "575232"
            }, {
            "keluhan": "DM Lainnya",
            "jumlah_kunjungan": "63253"
            }, {
            "keluhan": "Penyakit Hipertensi",
            "jumlah_kunjungan": "156768"
            }, {
            "keluhan": "Penyakit pada Esofagus, Perut, Usus Dua Belas Jari",
            "jumlah_kunjungan": "33819"
            }, {
            "keluhan": "ISPA",
            "jumlah_kunjungan": "36287"
            }, {
            "keluhan": "Penyakit Jantung",
            "jumlah_kunjungan": "96216"
            }, {
            "keluhan": "Stroke",
            "jumlah_kunjungan": "17863"
            }, {
            "keluhan": "Penyakit Ginjal Kronis",
            "jumlah_kunjungan": "97638"
            }, {
            "keluhan": "Penanganan Tindak Lanjut",
            "jumlah_kunjungan": "80575"
            }, {
            "keluhan": "Penyakit pada Muskuloskeletal dan Jaringan Ikat",
            "jumlah_kunjungan": "104316"
            }, {
            "keluhan": "Kunjungan Sehat",
            "jumlah_kunjungan": "232704"
            }]
        '''

        data_list = json.loads(data_json)
        for item in data_list:
            item['jumlah_kunjungan'] = int(item['jumlah_kunjungan'])
        data_df = pd.DataFrame(data_list)

        data_df = data_df.sort_values(by='jumlah_kunjungan', ascending=False)

        highlight_conditions = data_df['keluhan'].isin(["DM Tipe I", "DM Tipe II", "DM Lainnya"])
        data_df['color'] = ['#ff4500' if condition else '#d3d3d3' for condition in highlight_conditions]

        fig = px.bar(
            data_df, 
            x='jumlah_kunjungan', 
            y='keluhan', 
            orientation='h', 
            text='jumlah_kunjungan', 
            color='color', 
            color_discrete_map='identity',
            category_orders={"keluhan": list(data_df['keluhan'])}
        )
        fig.update_layout(showlegend=False)
        
        col1, col2 = st.columns([3, 1])
        with col1:
            fig.update_layout(
                autosize=False,
                width=1400,
                showlegend=False,
            )
            st.plotly_chart(fig)
        with col2:
            st.markdown("&nbsp;", unsafe_allow_html=True)
            st.markdown("&nbsp;", unsafe_allow_html=True)
            st.markdown("""
            **Jumlah Kunjungan dengan diagnosis DM tipe II** menempati posisi paling atas.
            
            Hal tersebut mengindikasikan penderita DM pada tahun 2019 masih banyak yang mengalami keluhan DM pada tahun 2021. 
            
            Oleh karena itu, menarik untuk ditelusuri bagaimana lifetime cost para penderita DM.
            """)

        st.subheader('Distribusi Jumlah Kasus DM per Jenjang Usia')

        with open('src/data/pyramid.json', 'r') as f:
            data_list_pyramid = json.load(f)
        
        for item in data_list_pyramid:
            item['jumlah_kunjungan'] = int(item['jumlah_kunjungan'])
        df_pyramid = pd.DataFrame(data_list_pyramid)

        df_pyramid_tipe1 = df_pyramid[df_pyramid['keluhan'] == 'DM Tipe I'].sort_values(by='kategori_umur')
        df_pyramid_tipe2 = df_pyramid[df_pyramid['keluhan'] == 'DM Tipe II'].sort_values(by='kategori_umur')

        df_pyramid_tipe1['jumlah_kunjungan'] = -df_pyramid_tipe1['jumlah_kunjungan']

        y = list(df_pyramid_tipe1['kategori_umur'])
        men_bins = list(df_pyramid_tipe2['jumlah_kunjungan'])
        women_bins = list(df_pyramid_tipe1['jumlah_kunjungan'])

        layout = go.Layout(
            yaxis=go.layout.YAxis(title='Kategori Umur'),
            xaxis=go.layout.XAxis(title='Jumlah Kunjungan'),
            barmode='relative',
            bargap=0.1,
            autosize=False,
            width=1400,
            margin=dict(l=50, r=50, b=100, t=100, pad=4)
        )

        data = [
            go.Bar(y=y, x=men_bins, orientation='h', name='DM Tipe II', hoverinfo='x', marker=dict(color='powderblue')),
            go.Bar(y=y, x=women_bins, orientation='h', name='DM Tipe I', text=-1 * np.array(women_bins).astype('int'), hoverinfo='text', marker=dict(color='seagreen'))
        ]

        fig = go.Figure(data=data, layout=layout)
        st.plotly_chart(fig)

        st.subheader('Persebaran Jumlah Kasus DM per Kabupaten/Kota')