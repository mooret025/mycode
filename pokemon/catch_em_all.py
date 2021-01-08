#!/usr/bin/env python3

# imports always go at the top of your code
import requests

def main():
    pokemon = input("Type in a pokemon >> ").strip()
    pokeapi = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}").json()
    url = pokeapi['sprites']['front_default']
    
    with open("/home/student/static/output.txt", 'w') as file_obj:
        print(f"URL to sprite: {url}\n", file=file_obj)
        print(f"{pokemon.capitalize()} has been in {len(pokeapi['game_indices'])} Pokemon games.\n", file=file_obj)
        move_list = []
        for move in pokeapi['moves']:
            move_list.append(move['move']['name'])
        print(f"{pokemon.capitalize()} has {len(move_list)} moves.\n", file=file_obj)
        print(move_list, file=file_obj)
main()
