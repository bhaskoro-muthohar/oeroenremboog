import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

from src.pages import halaman_pengantar, gambaran_umum, correlation_heatmap, table_view, welcome_page

st.set_page_config(
    page_title="Oeroenremboog Dashboard",
    page_icon="🦈",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
    'Report a bug': "mailto:bhaskoro.jr@gmail.com",
    'About': "# [Click for the secret](https://www.youtube.com/watch?v=dQw4w9WgXcQ)"
    }
)

def html_component():
    components.html(open("src/frontend/index.html").read())

def main():
    if 'indonesia_map' not in st.session_state:
        st.session_state.indonesia_map = None
    pages = {
        # "Welcome Page": welcome_page.WelcomePage(),
        "Pengantar": halaman_pengantar.HalamanPengantar(),
        "1. Gambaran Umum": gambaran_umum.GambaranUmum(),
        "Correlation Heatmap": correlation_heatmap.CorrelationHeatmap(),
        "Table View": table_view.TableView(),
        "HTML Component": html_component
    }

    with st.sidebar:
        selected_page = option_menu("Menu Navigasi", list(pages.keys()))

    page = pages[selected_page]
    page()

    html_string='''
    <script>
    // To break out of iframe and access the parent window
    const streamlitDoc = window.parent.document;

    // Make the replacement
    document.addEventListener("DOMContentLoaded", function(event){
            streamlitDoc.getElementsByTagName("footer")[0].innerHTML = "Made with ♥ and Streamlit";
        });
    </script>
    '''
    components.html(html_string)

if __name__ == "__main__":
    main()
