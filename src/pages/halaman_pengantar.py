import streamlit as st
from database_config import connect_to_db

class HalamanPengantar:
    def __call__(self):
        self.halaman_pengantar()

    def halaman_pengantar(self):
        st.image("https://bpjs-kesehatan.go.id/assets/img/logo/logo-color.svg", width=400)
        
        st.title('Halaman Pengantar')

        st.markdown("""
        ## Selamat Datang!
        Pada laman ini, Anda akan mendapatkan informasi mengenai gambaran umum Diabetes Mellitus, serta informasi pemetaan dan proyeksi kejadian Diabetes Mellitus yang terangkum ke dalam beberapa halaman.
        """)

        with open('src/frontend/style.css', 'r') as f:
            css_content = f.read()

        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

        st.markdown("""
            ## Informasi Halaman yang Tersedia

            <div class="container">
                <div class="wrapper">
                    <div class="card">
                        <a href="your_link_here_1"><h3>1. Gambaran Umum</h3></a>
                        <p>Deskripsi Umum kasus-kasus Diabetes Melitus di Indonesia</p>
                    </div>
                </div>
                <div class="wrapper">
                    <div class="card">
                        <a href="your_link_here_2"><h3>2. Faktor Penting Makanan</h3></a>
                        <p>Hubungan pola konsumsi makanan dengan kasus Diabetes Mellitus</p>
                    </div>
                </div>
                <div class="wrapper">
                    <div class="card">
                        <a href="your_link_here_3"><h3>3. Peta Kasus</h3></a>
                        <p>Pemetaan kasus DM dan pengelompokan Kabupaten/Kota</p>
                    </div>
                </div>
                <div class="wrapper">
                    <div class="card">
                        <a href="your_link_here_4"><h3>4. Proyeksi Kasus</h3></a>
                        <p>Proyeksi Kasus DM per Kabupaten/Kota</p>
                    </div>
                </div>
                <div class="wrapper">
                    <div class="card">
                        <a href="your_link_here_5"><h3>5. Bank Data</h3></a>
                        <p>Informasi data tabular hasil analisa yang bisa digunakan sesuai kebutuhan, seperti operasional</p>
                    </div>
                </div>
                <div class="wrapper">
                    <div class="card">
                        <a href="your_link_here_6"><h3>6. Lampiran (Tentatif)</h3></a>
                        <p>Lampiran penunjang analisa</p>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)


        # st.subheader('Data Preview')
        # data = self.fetch_data()
        # st.write(data)

    def fetch_data(self):
        conn = connect_to_db()
        query = "SELECT * FROM dm2021_kepesertaan"
        result = conn.execute(query).fetch_df()
        conn.close()
        return result
