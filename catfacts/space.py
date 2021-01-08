#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get("http://api.open-notify.org/astros.json")

    # the .json() method will dump a JSON string into Pythonic data structures. COOL!
    # This is much easier than using the urllib.request library
    in_space = r.json()
    number = in_space['number']
    inners = in_space['people']
    print(f'People in space: {number}')
    for people in inners:
        print(f'{people["name"]} is on the {people["craft"]}')
main()

