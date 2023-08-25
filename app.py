import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import geopandas as gpd
import plotly.express as px
import plotly.graph_objects as go
import random
from database_config import connect_to_db

def fetch_data():
    conn = connect_to_db()
    query = "SELECT * FROM dm2021_kepesertaan"
    result = conn.execute(query).fetch_df()
    conn.close()
    return result

def data_view():
    st.title('DuckDB Data Viewer')
    st.subheader('Data from dm2021_kepesertaan table')
    data = fetch_data()
    st.write(data)

def distribution_chart():
    st.title('Distribution Chart')
    mock_data = pd.DataFrame({'Value': [50, 60, 70, 80, 90]})
    st.bar_chart(mock_data['Value'])

def correlation_heatmap():
    st.title('Correlation Heatmap')
    mock_data = pd.DataFrame({'A': [1, 2, 3], 'B': [2, 3, 4], 'C': [3, 4, 5]})
    corr = mock_data.corr()

    fig, ax = plt.subplots()

    sns.heatmap(corr, annot=True, ax=ax)

    st.pyplot(fig)

def interactive_map():
    st.title('Interactive Map of Indonesia Provinces')

    indonesia_map = gpd.read_file('raw_data/indonesia-prov.geojson')

    indonesia_map = indonesia_map.to_crs("EPSG:3395")

    indonesia_map['geometry'] = indonesia_map['geometry'].centroid

    indonesia_map = indonesia_map.to_crs("EPSG:4326")

    indonesia_map['latitude'] = indonesia_map['geometry'].y
    indonesia_map['longitude'] = indonesia_map['geometry'].x

    indonesia_map['Mock Value'] = [random.randint(100, 1000) for _ in range(len(indonesia_map))]

    fig = go.Figure(data=go.Scattergeo(
        lon=indonesia_map['longitude'],
        lat=indonesia_map['latitude'],
        text=indonesia_map['Propinsi'] + ': ' + indonesia_map['Mock Value'].astype(str),
        mode='markers',
        marker=dict(size=12, color=indonesia_map['Mock Value'], colorscale='Viridis')
    ))

    fig.update_layout(
        geo=dict(
            scope='asia',
            projection_type='mercator',
            showland=True,
            landcolor='rgb(243, 243, 243)',
            countrycolor='rgb(204, 204, 204)',
        ),
        margin={"r": 0, "t": 0, "l": 0, "b": 0}
    )

    st.plotly_chart(fig)

    return indonesia_map

def table_view(indonesia_map=None):
    st.title('Table Data from Interactive Map')

    if indonesia_map is not None:
        table_data = indonesia_map[['Propinsi', 'Mock Value']]
        table_data.rename(columns={'Propinsi': 'Province', 'Mock Value': 'Value'}, inplace=True)
        st.write(table_data)
    else:
        st.write("No data available")

def main():
    st.title("Navigation")
    pages = ["Data View", "Distribution Chart", "Correlation Heatmap", "Interactive Map", "Table View"]
    selected_page = st.session_state.selected_page if 'selected_page' in st.session_state else pages[0]

    cols = st.columns(len(pages))
    for idx, page in enumerate(pages):
        if cols[idx].button(page):
            selected_page = page
            st.session_state.selected_page = selected_page

    if selected_page == "Data View":
        data_view()
    elif selected_page == "Distribution Chart":
        distribution_chart()
    elif selected_page == "Correlation Heatmap":
        correlation_heatmap()
    elif selected_page == "Interactive Map":
        interactive_map()
    elif selected_page == "Table View":
        indonesia_map = interactive_map()
        table_view(indonesia_map)

if __name__ == "__main__":
    main()
