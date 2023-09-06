import streamlit as st
import duckdb
import pandas as pd
import plotly.express as px
import json
import geopandas as gpd
from shapely import wkb

class DiabetesMellitusMapPlotter:
    def __call__(self):
        return self.plot_interactive_map()

    def plot_interactive_map(self):
        st.title('Interactive Scatter Plot Map of Indonesia')

        choice = st.selectbox("Choose between Cities and Provinces", ["Cities", "Provinces"])

        conn = duckdb.connect('oeroenremboog.db')
        cursor = conn.cursor()

        if choice == "Cities":
            cursor.execute("SELECT * FROM indonesia_cities;")
        else:
            cursor.execute("SELECT * FROM indonesia_provinces;")

        columns = [desc[0] for desc in cursor.description]
        indonesia_map = pd.DataFrame(cursor.fetchall(), columns=columns)

        if 'geometry' in indonesia_map.columns:
            indonesia_map['geometry'] = indonesia_map['geometry'].apply(wkb.loads, hex=True)
            indonesia_map = gpd.GeoDataFrame(indonesia_map, geometry='geometry')
        else:
            st.warning("No geometry data available for provinces.")

        indonesia_map = gpd.GeoDataFrame(indonesia_map, geometry='geometry')

        # Load the JSON data
        with open('src/data/diff_percentage_dm1_dm2.json') as f:
            diff_data = json.load(f)
        diff_df = pd.DataFrame(diff_data)

        name_column = 'Name' if choice == "Cities" else 'Propinsi'

        diff_df['kabupaten_tinggal'] = diff_df['kabupaten_tinggal'].str.replace('KOTA ', '')

        if name_column in indonesia_map.columns and 'kabupaten_tinggal' in diff_df.columns:
            merged_data = pd.merge(indonesia_map, diff_df, left_on=name_column, right_on='kabupaten_tinggal', how='inner')
        else:
            st.error(f"Missing column {name_column} in either of the DataFrames.")
            return

        merged_data['diff_percentage'] = pd.to_numeric(merged_data['diff_percentage'], errors='coerce') * 100
        merged_data['diff_percentage'].fillna(0, inplace=True)
        merged_data = merged_data[merged_data['kabupaten_tinggal'].notna()]

        indonesia_map.crs = "EPSG:4326"

        # Plotting
        fig = px.scatter_mapbox(merged_data,
                                lat=merged_data.geometry.y,
                                lon=merged_data.geometry.x,
                                color='diff_percentage',
                                color_continuous_scale=["orange", "green"],
                                range_color=(-100, 100),
                                mapbox_style="carto-positron",
                                opacity=0.5,
                                labels={'diff_percentage': 'Difference Percentage'},
                                title='Interactive Map of Indonesia',
                                text=merged_data[name_column])

        fig.update_layout(
            autosize=True,
            margin={"r":0,"t":0,"l":0,"b":0},
            mapbox=dict(
                center=dict(
                    lat=-2.5,
                    lon=118
                ),
                zoom=4.2
            )
        )

        st.plotly_chart(fig, use_container_width=True)

        cursor.close()

        return merged_data

if __name__ == "__main__":
    main = DiabetesMellitusMapPlotter()
    main()