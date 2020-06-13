import googlemaps
import requests
import geocoding

API_key = 'AIzaSyDVyd-mpP6ugSDfe0AmRaVusa7BUCp-A5o'
origem = 'rodovia presidente castelo branco km 300'
url = "https://maps.googleapis.com/maps/api/staticmap?"
icon_url ='https://www.muygle.com/node-red/muygle/api/language?name=police'
lugares  = 'police'

# Google client
gmaps = googlemaps.Client(key = API_key)

# Geocoding convert
a =geocoding.convert()
lat,lng  = a.logradouro_para_coordenadas(origem)

# Encontrando Lugares próximos
places_results = gmaps.places_nearby(location = (lat,lng),radius = 2000,open_now = False ,
                                     type =lugares)

list = places_results['results']
pins =''
for i in list:
    name     =  i['name']
    lat_long =  i['geometry']['location']
    lat      = str(lat_long['lat'])
    long     = str(lat_long['lng'])
    local    = str(lat+','+long)
    pins    += '|'+local

#Gerando o mapa
r = requests.get(url+'center='+origem+'&zoom=15&format=jpg&size=600x600&markers=anchor:bottomright|'
                                      'icon:'+icon_url+pins+'&key='+API_key)


f = open('seubrequin.jpg', 'wb')
f.write(r.content)
f.close()