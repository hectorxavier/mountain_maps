import folium
import json
from IPython.display import display

map_center = [-2.805191, -79.005757]
mymap = folium.Map(location=map_center, zoom_start=20)

folium.Marker(
    [-2.805191, -79.005757],
    popup='Cuenca',
    icon=folium.Icon(color='blue', icon='info-sign')
).add_to(mymap)

geojson_data = open('coordenadas.json')

data = json.load(geojson_data)

folium.GeoJson(data, name="hello world").add_to(mymap)

folium.LayerControl().add_to(mymap)

mymap
