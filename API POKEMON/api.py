import requests

def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pokemon_info = {
            "name": data["name"],
            "height": data["height"],
            "weight": data["weight"],
            "abilities": [ability["ability"]["name"] for ability in data["abilities"]],
            "stats": {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]}
        }
        return pokemon_info
    else:
        return None
