from random import choice
from json import dumps

options_north = ["Walk north", "Head north", "Hike north", "Parade north"]
options_east = ["Stagger east", "Run towards the rising sun", "Parade east"]
options_west = ["Trudge west", "Head left", "Sprint west", "Run towards the western sea"]
enemies = ["Goblin", "Ogre", "Evil Rat", "Giant Slime", "Demonic Ant", "null"] #null=no enemy
items = ["Sword", "Shield", "Apple", "Banana", "Tinned beans", "Dagger"] #null=no item

def generate_enemy_health(enemy):
    if enemy == "Goblin":
        return 25
    elif enemy == "Ogre":
        return 30
    elif enemy == "Evil Rat":
        return 10
    elif enemy == "Giant Slime":
        return 25
    elif enemy == "Demonic Ant":
        return 5
    elif enemy == "null":
        return 0
    else:
        print("Error: Fake enemy found, this isn't supposed to happen, please tell Harley :(")
        quit()

def generate_room():
    print("Generating room data...")
    option_one = choice(options_north)
    option_two = choice(options_east)
    option_three = choice(options_west)
    enemy = choice(enemies)
    enemy_health = generate_enemy_health(enemy)
    item = choice(items)
    print("Generated room data")
    return {"generated_room_data": 1, "option_one": option_one, "option_two": option_two, "option_three": option_three, "enemy": enemy, "enemy_health": enemy_health, "item": item}
