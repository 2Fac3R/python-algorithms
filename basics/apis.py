import requests
import json

api_url = 'https://rickandmortyapi.com/api'

response = requests.get(f"{api_url}/character")
data = json.loads(response.text)

# print(data['info'])
# print(data['results'])
# print(data['results'][0]['name'])
# print(data['results'][0]['url'])
# print(data['results'][0]['image'])

characters = data['results']

for character in characters:
    print(f"{character['name']} from {character['origin']['name']}")
