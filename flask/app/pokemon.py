from flask import Flask
import os
import requests

app = Flask(__name__)

def collect_together(feature_list):
    res = ""
    for s in feature_list:
        res += s + "\n"
    return res


def get_pokemon_features(data):
    height = "height: "
    weight = "weight: "
    abilities = "abilities: "
    held_items = "held_items: "
    for a in data['abilities']:
        abilities += a['ability']['name'] + " "
    height += str(data['height'])
    weight += str(data['weight'])
    for h_i in data['held_items']:
        held_items += h_i['item']['name'] + " "
    return collect_together([height, weight, abilities, held_items])


@app.route('/pokemon/<name>', methods=['GET'])
def get_info_about_pokemon(name):
    import logging
    logging.basicConfig(filename='error.log', level=logging.DEBUG)
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
    if response.status_code != 200:
        return "Wrong pokemon`s name"
    data = response.json()
    return get_pokemon_features(data)

@app.route('/WhoHasAbility/<name>', methods=['GET'])
def get_info_about_ability(name):
    import logging
    logging.basicConfig(filename='error.log', level=logging.DEBUG)
    response = requests.get(f"https://pokeapi.co/api/v2/ability/{name}")
    if response.status_code != 200:
        return "Wrong ability name"
    data = response.json()
    pokemons = "pokemons: "
    for pokemon in data['pokemon']:
        pokemons += pokemon['pokemon']['name'] + " "
    return pokemons

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)
