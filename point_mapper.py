import folium
import pandas as pd
from geolib import geohash
from folium.plugins import MiniMap

# This is a sample geohash. Potentially, future iterations will include tables of geohashes and other classifiers
geo_hash = "9q3vmuqxq4hg"

coordinates = geohash.decode(geo_hash)

mapper = {'Latitude': [coordinates[0]],
          'Longitude': [coordinates[1]]}

# Convert dictionary into a dataframe
df = pd.DataFrame(mapper)
#%%

# Specify points to zoom in on
lat, lon = df.iloc[0]['Latitude'],df.iloc[0]['Longitude']

# This is the main map with the most zoom
main_map = folium.Map(location=[lat,lon], zoom_start=18, tiles='Esri.WorldImagery')

# This will add the baselayer for the main map
folium.TileLayer(
    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Boundaries_and_Places/MapServer/tile/{z}/{x}/{y}',
    attr='ESRI World Boundaries and Places', name='Roads and Labels', overlay=True
).add_to(main_map)

# Adding the point to the map
folium.Marker([lat,lon], popup=f'Point at ({lat}), {lon})').add_to(main_map)

# Create and add the smaller map to give context
minimap = MiniMap(tile_layer='OpenStreetMap', 
                  toggle_display=True, 
                  zoom_level_fixed=14,
                  width=400, height=500)
main_map.add_child(minimap)

# Prevent sticky fingers from playing with layers
folium.LayerControl().add_to(main_map)
#%%
main_map.save('test_map.html')

main_map
#%%
