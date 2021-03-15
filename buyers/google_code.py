import geocoder
import json

with open('./config.json', 'r') as file:
    config = json.load(file)

def addressToLatLng(addres):
    try:
        API_KEY = config['API_KEY_GOOGLE']
        geo = geocoder.google(addres, key=API_KEY)
        return geo
    except Exception as e:
        return 'Ocurrio un error ' + e
