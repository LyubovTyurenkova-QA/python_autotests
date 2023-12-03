import requests

host = "https://api.pokemonbattle.me:9104"
token = "f97e538cb3c5fca37ca513deca5b2612"

response = requests.post(url= f'{host}/pokemons',
                         headers={'Content-Type': 'application/json', 'trainer_token': f'{token}'},
                         json={"name": "Кот", "photo": "https://dolnikov.ru/pokemons/albums/509.png"})
print (f'Code: {response.status_code}  - {response.reason}. Message: {response.text}')

response = requests.put(url= f'{host}/pokemons',
                         headers={'Content-Type': 'application/json', 'trainer_token': f'{token}'},
                         json= {"pokemon_id": "21099", "name": "Котик", "photo": "https://dolnikov.ru/pokemons/albums/509.png"})
print (f'Code: {response.status_code}  - {response.reason}. Message: {response.text}')

response = requests.post(url= f'{host}/trainers/add_pokeball',
                         headers={'Content-Type': 'application/json', 'trainer_token': f'{token}'},
                         json={ "pokemon_id": "21099"})
print (f'Code: {response.status_code}  - {response.reason}. Message: {response.text}')