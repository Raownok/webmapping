import folium
import pandas


 


data = pandas.read_csv("volcanoes.txt")
lon = list(data['LON'])
lat = list(data['LAT'])
elev = list(data['ELEV'])
map1 = folium.Map([23.747236, 90.428342], zoom_start = 1, tiles='OpenStreetMap')

def colour_g (elevtion):
    if elevtion < 1000:
        return "green"
    elif 1000 < elevtion < 3000:
        return "blue"
    else : 
        return "red"

fgv = folium.FeatureGroup(name='Volcanoes')

for i,j, el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[i,j], radius=6, color = "gray" , popup = str(el)+'m', fill_color = colour_g(el), fill= True ,fill_opacity = 0.8))
    
fgp = folium.FeatureGroup(name='Population')

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function= lambda c :{ 'fillColor':'blue' if c ['properties']['POP2005'] < 10000000 
else 'yellow' if 10000000 <= c ['properties']['POP2005'] < 20000000 else 'red' } ))

map1.add_child(fgv)
map1.add_child(fgp)
map1.add_child(folium.LayerControl())
map1.save('index.html')
