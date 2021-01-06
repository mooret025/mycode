#!/usr/bin/env python3

farms = [
        {"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]}, {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
        {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

# farm = farms[0]

# [print(animal) for animal in farm['agriculture']]



options = list(['NE Farm', 'W Farm', 'SE Farm'])
pick = input('Choose a farm - (NE Farm, W Farm, or SE Farm: ')
while pick not in options:
    pick = input('Choose a farm - (NE Farm, W Farm, or SE Farm: ')

for farm in farms:
    if pick == farm['name']:
        for thing in farm['agriculture']:
            print(thing)
