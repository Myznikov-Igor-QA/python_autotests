import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '1840164a8c8e17d5d33b4bb6a438228f'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_Creation = {
    "name": "generate",
    "photo_id": -1
}

'''respons_Creation = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_Creation)
print(respons_Creation.text)'''

body_Name = {
    "pokemon_id": "249946",
    "name": "Cloud",
    "photo_id": 1
}

'''respons_Name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_Name)
print(respons_Name.text)'''

body_catch = {
    "pokemon_id": "249950"
}

respons_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(respons_catch.text)



