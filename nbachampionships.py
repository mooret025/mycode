#!/usr/bin/env python3

most_championships = {"Bill Russell": 11, "Sam Jones": 10,
        "John Havlicek": 8, "Robert Horry": 7,"Kareem Abdul-Jabbar": 6,
        "Michael Jordan": 6, "Scottie Pippen": 6, "Earvin Magic Johnson": 5,
        "Dennis Rodman": 5, "Kobe Bryant": 5, "Tim Duncan": 5, "Shaquille O'Neal": 5,
        "Lebron James": 4, "Tony Parker": 4, "Manu Ginobili": 4,}

message = 'How many championships did your favorite NBA player win?'


while True:
    prompt = input("Who is your favorite NBA player?").strip().title()

    if prompt == 'Bill Russell':
        print("Bill has won: " + str(most_championships.get("Bill Russell")))
    elif prompt == 'Sam Jones':
        print("Sam has won: " + str(most_championships.get("Sam Jones")))
    elif prompt == 'John Havlicek':
        print("John has won: " + str(most_championships.get("John Havlicek")))
    elif prompt == 'Robert Horry':
        print("Robert has won: " + str(most_championships.get("Robert Horry")))
    elif prompt == 'Kobe Bryant':
        print("Kobe has won: " + str(most_championships.get("Kobe Bryant")))
    else:
       print(f"{prompt} is a loser, and any championships you claim he won is probably fake news!")
