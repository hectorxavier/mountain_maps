import folium
import json
from IPython.display import display

map_center = [-2.805191, -79.005757]
mymap = folium.Map(location=map_center, zoom_start=12)

folium.Marker(
    [-2.805191, -79.005757],
    popup='Cuenca',
    icon=folium.Icon(color='blue', icon='info-sign')
).add_to(mymap)

geojson_data = '''{
    "type": "FeatureCollection",
    "features": [
      {
        "type": "Feature",
        "properties": {},
        "geometry": {
          "coordinates": [
            [
              [
                -79.00885203732139,
                -2.7992277033995805
              ],
              [
                -79.00886789712413,
                -2.7990275298472227
              ],
              [
                -79.00899189316257,
                -2.798735189897215
              ],
              [
                -79.00915163580206,
                -2.798519368228284
              ],
              [
                -79.00898997620786,
                -2.7983248146208552
              ],
              [
                -79.00884487976336,
                -2.7979522507132657
              ],
              [
                -79.00878432293649,
                -2.797443895773256
              ],
              [
                -79.00933485096984,
                -2.797293352159116
              ],
              [
                -79.00971540333649,
                -2.7977361121029247
              ],
              [
                -79.00995840298887,
                -2.798393991103538
              ],
              [
                -79.00986433369042,
                -2.798929426640683
              ],
              [
                -79.00972518119617,
                -2.799444103504058
              ],
              [
                -79.00885203732139,
                -2.7992277033995805
              ]
            ]
          ],
          "type": "Polygon"
        }
      }
    ]
  }'''

folium.GeoJson(geojson_data, name="hello world").add_to(mymap)

folium.LayerControl().add_to(mymap)

mymap

#display(mymap)
