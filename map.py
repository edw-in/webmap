import folium
import pandas

data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location = [42.103989, -110.689801], zoom_start = 6, tiles = "Stamen Terrain")

fgv = folium.FeatureGroup(name = "Volcanoes!")

def rise(height):
    if height < 1000:
        color='green'
    elif 1000<= height < 3000:
        color='orange'
    else:
        color='red'
    return color

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location = [lt, ln], popup = str(el)+"m",radius = 6, fill_color = rise(el), color = 'grey', fill_opacity=0.7 ))

fgp = folium.FeatureGroup(name = 'Population!')

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else "orange" if 10000000 <= x['properties'] ['POP2005'] < 50000000 else 'red'
if 20000000 <= x['properties'] ['POP2005'] < 250000000 else 'black'}))

map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())

map.save("map.html")
