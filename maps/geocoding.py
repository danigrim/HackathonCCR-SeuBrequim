import requests

API_key = 'AIzaSyDVyd-mpP6ugSDfe0AmRaVusa7BUCp-A5o'
url     = 'https://maps.googleapis.com/maps/api/geocode/json'

class convert():

    def logradouro_para_coordenadas(self,logradouro):

        lat, lng = None, None
        api_key = API_key
        url_base_static_maps = url
        endpoint = f"{url_base_static_maps}?address={logradouro}&key={api_key}"
        r = requests.get(endpoint)
        if r.status_code not in range(200, 299):
            return None, None
        try:

            results = r.json()['results'][0]
            lat = results['geometry']['location']['lat']
            lng = results['geometry']['location']['lng']
        except:
            pass
        return lat, lng