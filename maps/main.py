import googlemaps
import pprint
import gmplot
import time

API_key = 'AIzaSyDVyd-mpP6ugSDfe0AmRaVusa7BUCp-A5o'

gmaps = googlemaps.Client(key = API_key)

places_results = gmaps.places_nearby(location =' -23.563114, -46.654554 ',radius = 4000,open_now = False ,
                                     type ='school')

list = places_results['results']

list_lat  = []
list_long = []
for i in list:
    name     =  i['name']
    lat_long =  i['geometry']['location']
    lat      = lat_long['lat']
    list_lat +=[lat]
    long     = lat_long['lng']
    list_long+=[long]


gmap = gmplot.GoogleMapPlotter (-23.562258,-46.655366,15)
gmap.scatter(list_lat, list_long, 'red', size = 10)
gmap.apikey =API_key
gmap.draw('/home/gabriel/gmplot.png')