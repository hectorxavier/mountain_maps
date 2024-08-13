import folium
from IPython.display import display

map_center = [-2.805191, -79.005757]
mymap = folium.Map(location=map_center, zoom_start=12)

folium.Marker(
    [-2.805191, -79.005757],
    popup='Cuenca',
    icon=folium.Icon(color='blue', icon='info-sign')
).add_to(mymap)

display(mymap)
