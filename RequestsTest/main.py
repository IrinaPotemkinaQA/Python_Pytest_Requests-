import requests


URL = 'https://pokemonbattle.ru/v2'
TOKEN = '41f444b969c1989ab84c73465b7dd4e7'
HEADER = {'Conten-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "generate",
    "photo": "generate"
}
body_change_name = {
    "pokemon_id": "ID",
    "name": "generate",
    "photo": "generate"
}
body_pokeball = {
    "pokemon_id": "id"
}
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

pokemon_id = response_create.json()['id']
print(pokemon_id)


response_change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(response_change_name.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)


