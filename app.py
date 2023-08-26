import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

from src.pages import data_view, distribution_chart, correlation_heatmap, interactive_map, table_view, welcome_page

st.set_page_config(
    page_title="Oeroenremboog Dashboard",
    page_icon="🦈",
    layout="centered",
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
        "Data View": data_view.DataView(),
        "Distribution Chart": distribution_chart.DistributionChart(),
        "Correlation Heatmap": correlation_heatmap.CorrelationHeatmap(),
        "Interactive Map": interactive_map.InteractiveMap(),
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
