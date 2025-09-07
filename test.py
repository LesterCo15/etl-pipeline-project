import pandas as pd
import requests
import json
import time
import csv

url = "https://pokeapi.co/api/v2/pokemon?limit="

def extract(url: str, limit: int):
  data = requests.get(f"{url}{limit}").json()
  raw_data_list = []
  for p in data['results']:
    raw_data = requests.get(p['url']).json()
    raw_data_list.append(raw_data)
    time.sleep(0.6)
  return raw_data_list

def transform(data_list: list):
  pokemon_list = []
  for data in data_list:
    species = requests.get(data['species']['url']).json()
  
    # Abilities
    abilities = [a['ability']['name'] for a in data['abilities']]
    ability_1 = abilities[0] if len(abilities) > 0 else None
    ability_2 = abilities[1] if len(abilities) > 1 else None

    # Stats
    stats = {s['stat']['name']: s['base_stat'] for s in data['stats']}

    # Types
    types = [t['type']['name'] for t in data['types']]
    type_1 = types[0] if len(types) > 0 else None
    type_2 = types[1] if len(types) > 1 else None

    pokemon_info = {
      "name": data['name'],
      "ability_1": ability_1,
      "ability_2": ability_2,
      "base_experience": data['base_experience'],
      "height": data['height'],
      "weight": data['weight'],
      "generation": species['generation']['name'],
      "poke_hp": stats.get('hp'),
      "poke_atk": stats.get('attack'),
      "poke_def": stats.get('defense'),
      "poke_spl_atk": stats.get('special-attack'),
      "poke_spl_def": stats.get('special-defense'),
      "poke_spd": stats.get('speed'),
      "type_1": type_1,
      "type_2":type_2
    }

    pokemon_list.append(pokemon_info)
    print(f"Fetched {pokemon_info['name']}")

  print("\n Done! Collected", len(pokemon_list), "Pokemon.")
  return pokemon_list

def load(data: list, csv_file: str):
  with open(csv_file, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

def main():
  raw_data = extract(url, 100)
  cleaned_data = transform(raw_data)
  load(cleaned_data, "pokemon.csv")

if __name__ == '__main__':
  main()
