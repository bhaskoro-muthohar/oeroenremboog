import streamlit as st
import geopandas as gpd
import plotly.graph_objects as go
import random

class InteractiveMap:
    def __call__(self):
        return self.interactive_map()

    def interactive_map(self):
        st.title('Interactive Map of Indonesia Provinces')

        indonesia_map = gpd.read_file('raw_data/indonesia-prov.geojson')
        indonesia_map = indonesia_map.to_crs("EPSG:3395")
        indonesia_map['geometry'] = indonesia_map['geometry'].centroid
        indonesia_map = indonesia_map.to_crs("EPSG:4326")
        indonesia_map['latitude'] = indonesia_map['geometry'].y
        indonesia_map['longitude'] = indonesia_map['geometry'].x
        indonesia_map['Mock Value'] = [random.randint(100, 1000) for _ in range(len(indonesia_map))]

        if 'indonesia_map' not in st.session_state:
            st.session_state.indonesia_map = None
        st.session_state.indonesia_map = indonesia_map

        fig = go.Figure(go.Scattermapbox(
            lon=indonesia_map['longitude'],
            lat=indonesia_map['latitude'],
            text=indonesia_map['Propinsi'] + ': ' + indonesia_map['Mock Value'].astype(str),
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=12,
                color=indonesia_map['Mock Value'],
                colorscale='Viridis'
            )
        ))

        fig.update_layout(
            mapbox=dict(
                center=dict(lat=-2, lon=118),
                zoom=3.4,
                style='carto-positron'
            ),
            margin={"r": 0, "t": 0, "l": 0, "b": 0}
        )

        st.plotly_chart(fig)

        return indonesia_map
