# import pip._vendor.requests as requests
import requests
import json

endpoint = 'https://rickandmortyapi.com/api/character'

response = requests.get(endpoint)
data = json.loads(response.text)

# print(data['info'])
# print(data['results'])
# print(data['results'][0]['name'])
# print(data['results'][0]['url'])
# print(data['results'][0]['image'])

characters = data['results']

for character in characters:
    print(character['name'])
