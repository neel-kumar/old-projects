import folium
import pandas
import html

data = pandas.read_csv("Volcanoes_USA.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def color(e):
    if e > 4000:
        return 'black'
    elif e > 3000:
        return 'darkred'
    elif e > 2000:
        return 'red'
    else:
        return 'orange'

map = folium.Map(location = [37.323007, -122.073279])

fgv = folium.FeatureGroup(name = 'Volcanoes')

for lt, ln, el, nm in zip(lat, lon, elev, name):
    print(nm, el)
    et = html.escape('%s, elevation %s m' %(nm, el))
    fgv.add_child(folium.CircleMarker(location = (lt, ln), popup = et, radius = 6,
    fill_color = color(el), color = 'black', fill_opacity = 0.6))

fgp = folium.FeatureGroup(name = 'Population')

fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read(),
style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
else 'red' if 1000000000 > x['properties']['POP2005']
else 'black'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
