import requests
import json
import webbrowser

API_KEY='xFA1MowhaIc1praSSqUiFM5ejrjGJvh041EwNcgT'

url='https://api.nasa.gov/planetary/apod'

#parametros
params ={
    'api_key':API_KEY,
    'hd':'True',
    'date':'2022-04-25'
}

response = requests.get(url,params=params)
json_data = json.loads(response.text)
image_url = json_data['hdurl']
webbrowser.open(image_url)
