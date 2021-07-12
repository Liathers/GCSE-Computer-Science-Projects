from save_handler import create_save, append_save_data, load_save_data, load_story_data
from generate_room_data import generate_room
from os import makedirs, listdir, path, remove, system
from random import randint as randInt

save_dir = ""
user_name = ""
user_health = 0
user_score = 0
user_defeated_enemies = 0
rooms_traversed = 0
max_rooms = 0
user_inventory_items = []
room_data = {}
game_state = 0
save_data = {}
story_data = {}

def load_game():
    system("title Text Based RPG")
    print("=====Game startup=====")
    if path.exists("saves"):
        print("./saves folder located")
    else:
        print("./saves folder not located")
        makedirs("saves")
        print("Created ./saves folder")
    print("=====Save selection=====")
    save_selection()

def save_selection():
    print("1: Load save")
    print("2: Delete save")
    print("3: Create new save")
    option = input("Please select an option: ")
    if option == "1":
        print("=====Load save=====")
        load_existing_save()
    elif option == "2":
        print("=====Delete save=====")
        delete_existing_save()
    elif option == "3":
        print("=====Create save=====")
        create_new_save()
    else:
        print("Invalid option, please try again!")
        print("=====Save selection=====")
        save_selection()

def load_existing_save():
    global save_dir
    saves_directories = listdir("saves/")
    if len(saves_directories) == 0:
        print("There are no saves, create a save!")
        print("=====Create save=====")
        create_new_save()
    else:
        for file in saves_directories:
            print(file.replace("_save.json", ""))
        print()
        option = input("Select save from list: ")
        if option + "_save.json" in saves_directories:
            save_dir = "saves/" + option + "_save.json"
            print("=====Save data loader=====")
            save_data_loader(save_dir)
        else:
            print("Save does not exist, please select another!")
            print("=====Load save=====")
            load_existing_save()

def save_data_loader(save_dir):
    global user_name
    global user_health
    global user_score
    global user_defeated_enemies
    global rooms_traversed
    global max_rooms
    global user_inventory_items
    global room_data
    global game_state

    print("Loading save data...")
    print("Loaded save data")
    print("=====Save data check=====")
    try:
        save_data = load_save_data(save_dir)
        user_name = str(save_data["save"][0]["name"])
        user_health = int(save_data["save"][0]["health"])
        user_score = int(save_data["save"][0]["score"])
        user_defeated_enemies = int(save_data["save"][0]["defeated_enemies"])
        rooms_traversed = int(save_data["save"][0]["rooms_traversed"])
        max_rooms = int(save_data["save"][0]["max_rooms"])
        user_inventory_items = save_data["save"][0]["inventory"]
        room_data = save_data["save"][0]["room_data"]
        game_state = int(save_data["save"][0]["game_state"])
        print("Save data valid!")
    except:
        print("Error, invalid save detected!")
        print("Deleting save...")
        remove(save_dir)
        print("Deleted save, taking you back to the main menu.")
        print("=====Save selection=====")
        save_selection()        
        
    #validate_save_data()
    start_game()

def validate_save_data():
    print("=====Save data check=====")
    try:
        print("name: " + user_name)
        print(user_health + 0)
        print(user_score + 0)
        print(user_defeated_enemies + 0)
        print(rooms_traversed + 0)
        print(max_rooms + 0)
        print(user_inventory_items)
        print(room_data)
        print(game_state + 0)
    except:
        print("Error, invalid save detected!")
        print("Deleting save...")
        remove(save_dir)
        print("Deleted save, taking you back to the main menu.")
        print("=====Save selection=====")
        save_selection()
        

def create_new_save():
    global save_dir
    user_name = input("Input a username: ")
    save_name = f"{user_name}_save.json"
    if path.exists(f"saves/{save_name}"):
        print("Save already exists, please select another username!")
        create_new_save()
    else:
        print("Creating save...")
        save_dir = f"saves/{save_name}"
        create_save(save_dir)
        save_data = load_save_data(save_dir)
        save_data["save"].append(
            {
                "name": user_name,
                "health": 100,
                "score": 0,
                "defeated_enemies": 0,
                "rooms_traversed": 0,
                "max_rooms": 0,
                "inventory": [],
                "room_data": {
                    "generated_room_data": 0 #0=no, 1=yes
                },
                "game_state": 0 #0=alive, 1=dead, 2=won                        
            }
        )
        append_save_data(save_data, save_dir)
        print("Save created")
        start_game()

def delete_existing_save():
    global save_dir
    saves_directories = listdir("saves/")
    if len(saves_directories) == 0:
        print("There are no saves, create a save!")
        print("=====Create save=====")
        create_new_save()
    else:
        for file in saves_directories:
            print(file.replace("_save.json", ""))
        print()
        option = input("Select save from list: ")
        if option + "_save.json" in saves_directories:
            save_dir = "saves/" + option + "_save.json"
            print("Deleting save...")
            remove(save_dir)
            print("Save deleted")
            print("=====Save selection=====")
            save_selection()
        else:
            print("Save does not exist, please select another!")
            print("=====Delete save=====")
            delete_existing_save()

def generate_room_data():
    global room_data
    room_data = generate_room()
    save_data["save"][0]["room_data"] = room_data
    append_save_data(save_data, save_dir)
    #print(room_data)

def start_game():
    global save_data
    save_data = load_save_data(save_dir)
    print("=====Game=====")
    if game_state == 0:
        if save_data["save"][0]["room_data"]["generated_room_data"] != 1:
            generate_room_data()
            print()
        else:
            print("Room data found")
            print()

        start_game_story()
    elif game_state == 1:
        print("You have died!")
        option = input("Do you want to return to the main menu (y/n)? ").lower()
        if option != "n":
            print("=====Save selection=====")
            save_selection()
        else:
            quit()
    elif game_state == 2:
        print("You have completed the game! Congrats!")
        option = input("Do you want to return to the main menu (y/n)? ").lower()
        if option != "n":
            print("=====Save selection=====")
            save_selection()
        else:
            quit()

def start_game_story():
    global story_data
    print("Loading story data...")
    story_data = load_story_data()
    print("Loaded story data")
    
    print(story_data["story"][0]["title"])
    print(story_data["story"][0]["text"])
    print(story_data["story"][1]["text"])
    print(story_data["story"][2]["title"])
    print(story_data["story"][2]["text"].replace("{ITEM_NAME}", room_data["item"]).replace("{ENEMY_NAME}", room_data["enemy"]))
    #generate_room_data()
    print("=====Make your choice!=====")
    game_option_selection(3, True)

def game_option_selection(options_length: int, enemy_present: bool):
    attack_enemy = False
    
    if options_length == 2:
        print("1: " + room_data["option_one"])
        print("2: " + room_data["option_two"])

        if enemy_present:
            print("3: Attack the " + room_data["enemy"])

        selected = input("What do you wish to do? ")
        if selected == "1":
            selected_option = room_data["option_one"]
        elif selected == "2":
            selected_option = room_data["option_two"]
        elif selected == "3" and enemy_present:
            selected_option = "attack the " + room_data["enemy"]
            attack_enemy = True
        else:
            print("Invalid option, please select another!")
            print("=====Make your choice!=====")
            game_option_selection(options_length, enemy_present)
            
    elif options_length == 3:
        print("1: " + room_data["option_one"])
        print("2: " + room_data["option_two"])
        print("3: " + room_data["option_three"])

        if enemy_present:
            print("4: Attack the " + room_data["enemy"])

        selected = input("What do you wish to do? ")
        if selected == "1":
            selected_option = room_data["option_one"]
        elif selected == "2":
            selected_option = room_data["option_two"]
        elif selected == "3":
            selected_option = room_data["option_three"]
        elif selected == "4" and enemy_present:
            selected_option = "attack the " + room_data["enemy"]
            attack_enemy = True
        else:
            print("Invalid option, please select another!")
            print("=====Make your choice!=====")
            game_option_selection(options_length, enemy_present)
    else:
        print("Error: Invalid options detected, this isn't supposed to happen, please tell Harley :(")
        exit()

    if attack_enemy:
        print("=====Attacking enemy=====")
        game_option_attack_enemy(room_data["enemy"], room_data["enemy_health"])
    else:
        print(f"You decided to {selected_option.lower()}.")

def game_option_attack_enemy(enemy: str, enemy_health: int):
    print(f"Placeholder, attacking enemy. Enemy: {enemy}, Enemy Health: {enemy_health}")
    if enemy_health > 5:
        attackInt = randInt(0, enemy_health - 5)
        damageInt = randInt(0, 1)
        if damageInt == 0:
            if attackInt == 0:
                print("Oh no, you missed!")
            else:
                print(f"Woohoo! You dealt {attackInt} damage to the {enemy}")
                enemy_health -= attackInt
        else:
            print("Placeholder")
            damage = 0 #placeholder value
            print(f"The {enemy} dodged your attack and dealt {damages} damage to you!")

load_game()
