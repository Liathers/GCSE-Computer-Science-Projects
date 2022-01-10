from random import randint as genint
from json import dump, load

player_1 = ""
player_2 = ""
player_1_score = 0
player_2_score = 0
dice_sides = 0
dice_result = 0
total_rolls = 1
finished_rolling_dice = False

#dice dependencies
even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
valid_sides = [6, 10, 20]
rounds_to_do = 5

def main():
    global dice_sides
    global total_rolls
    global player_1_score
    global player_2_score
    global finished_rolling_dice
    
    print("=====Input Names=====")
    player_1 = input("Input player 1's name: ")
    player_2 = input("Input player 2's name: ")
    if player_1 == player_2:
        print("Error: player names identical")
        main()
    while dice_sides == 0:
        print("=====How many sides?=====")
        
        print(f"Allowed values are the following: ")
        for x in range(len(valid_sides)):
            print("- " + str(valid_sides[x]))
        print("")
        dice_sides = int(input("How many sides do you want? "))
        if dice_sides not in valid_sides:
            print("That is an invalid input")
            dice_sides = 0
    while finished_rolling_dice == False:
        print(f"=====Dice Roll: Round {total_rolls}=====")
        player_1_score = dice_roll(player_1, player_1_score)
        player_2_score = dice_roll(player_2, player_2_score)
        total_rolls += 1
        if total_rolls > rounds_to_do:
            finished_rolling_dice = True
    if finished_rolling_dice:
        print("All of the die have been rolled!")
        if player_1_score > player_2_score:
            print(f"The player with the highest score is {player_1} with {player_1_score} points!")
            print("")
            handle_scores(True, player_1, player_1_score)
        else:
            print(f"The player with the highest score is {player_2} with {player_2_score} points!")
            print("")
            handle_scores(True, player_2, player_2_score)
        print_top_scores()

def dice_roll(player_name: str, score: int):
    print(f"Rolling dice for {player_name}...")
    dice_result_1 = genint(1,dice_sides)
    dice_result_2 = genint(1,dice_sides)
    total_result = dice_result_1 + dice_result_2
    print(f"The 1st dice rolled a {dice_result_1}!")
    print(f"The 2nd dice rolled a {dice_result_2}!")
    score += total_result
    if total_result in even_numbers:
        score += 10
    else:
        if score >= 0:
            score -= 5
    print(f"{player_name}'s current score is {score}!")
    if dice_result_1 == dice_result_2:
        print("A double was rolled, a dice will be rolled again!")
        print()
        dice_roll(player_name, score)
    print()
    return score

def handle_scores(saving: bool, name: str, score: int):
    def create_save():
        try:
            save = open("./scores.json", "x")
            save.write('{"save": []}')
            save.close
            print("Save created")
        except:
            print("Save located")
    
    def load_data():
        return load(open("./scores.json"))

    def append_score():
        data = load_data()
        data["save"].append(
            {
                "name": name,
                "score": int(score)
            })
        dump(data, open(f"./scores.json", "w"), indent=4, sort_keys=True)
            
    if saving == True:
        create_save()
        append_score()
        #print(load_data())
    if saving == False:
        return load_data()

def print_top_scores():
    data = handle_scores(False, None, None)
    print("=====Top Scores=====")
    data['save'] = sorted(data['save'], key=lambda x : x['score'], reverse=True)
    for x in range(5):
        try:
            name = data["save"][x]["name"]
            score = data["save"][x]["score"]
            suffix = ""
            
            if x == 0: suffix = "st"
            elif x == 1: suffix = "nd"
            elif x == 2: suffix = "rd"
            else: suffix = "th"
              
            print(f"{x+1}{suffix} place is {name} with a score of {score}.")
        except:
            pass

main()
