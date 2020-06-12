import googlemaps
import pprint
import time

API_key = 'AIzaSyDVyd-mpP6ugSDfe0AmRaVusa7BUCp-A5o'

gmaps = googlemaps.Client(key = API_key)

places_results = gmaps.places_nearby(location ='-33.8670522,151.1957362',radius = 400000,open_now = False ,
                                     type ='café')

print(places_results)