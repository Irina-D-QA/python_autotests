import requests

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "22f6891b1f8bdd282427d18028899c03"
HEADER = {"Content-Type": "application/json", "trainer_token": TOKEN}
BODY = {
    "name": "Бульбазавр",
    "photo_id": 112
}

BODY_PUT = {"pokemon_id": "144594",
    "name": "Gin",
    "photo_id": 113}

BODY_POST = {
    "pokemon_id": "144594"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = BODY)
print(response.text)


response_put = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = BODY_PUT)
print(response_put.text)


response_post = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = BODY_POST)
print(response_post.text)

