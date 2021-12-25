import random;
from classes import Player;
from enemies import Goblin;
player_class = None


def select_class():
    print(f"""\nWelecome to Arteria. Please select a class:
1) Warrior (WIP)
2) Archer (WIP)""")
    option = input(f"""\n""")
    return option


while player_class == None:
    option = select_class()
    if option == "1" or option.capitalize() == "Warrior":
        player_health = 100
        player_class = "Warrior"
        break
    elif option == "2" or option.capitalize() == "Archer":
        player_health = 100
        player_class = "Archer"
        break
    else:
        print(f"""\nPlease select a valid class from the list.""")

player1 = Player(player_class)

print(f"""\nYou have selected {player1.player_class}.""")
