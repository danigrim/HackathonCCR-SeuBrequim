import googlemaps
import requests
import geocoding
import upload

API_key = 'AIzaSyDVyd-mpP6ugSDfe0AmRaVusa7BUCp-A5o'


origem = 'rodovia presidente castelo branco km 300'
url = "https://maps.googleapis.com/maps/api/staticmap?"
icon_url ='https://ccr-hack-2020.s3.us-east-2.amazonaws.com/banheiro.png'
lugares  = ['restaurant']



def flow(origem,lugares=[]):

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
    pins_number =''
    names={}
    count=0
    for i in list:
        name     =  i['name']
        lat_long =  i['geometry']['location']
        lati      = str(lat_long['lat'])
        long     = str(lat_long['lng'])
        local    = str(lati+','+long)
        distance = gmaps.distance_matrix((lat, lng), (lati, long), mode="driving")
        if count <= 9:

            pins    += '|'+local
            dest_address = distance['destination_addresses'][0]
            time = distance['rows'][0]['elements'][0]['duration']['text']
            names[str(count)] = [name, dest_address, time]
            pins_number +='&markers=color:red|label:'+str(count)+'|size:mid|'+local
        count+=1


    #Gerando o mapa
    r = requests.get(url+'center='+origem+'&zoom=14&format=jpg&size=600x600&markers=color:blue|label:S|'
    'size:mid|'+str(lat)+','+str(lng)+'|'+'&markers=anchor:bottomright|'
    'icon:'+icon_url+pins+'&key='+API_key+pins_number)

    img_name = 'seubrequin.jpeg'

    f = open(img_name, 'wb')
    f.write(r.content)
    f.close()
    amazon_url = upload.up('seubrequin.jpeg')

    return names,amazon_url

flow(origem,lugares)