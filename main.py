from random import randint as genint
from json import dump, load
player_1 = ""
player_2 = ""
player_1_score = 0
player_2_score = 0
dice_result = 0
total_rolls = 1
finished_rolling_dice = False
# "save": []

def main():
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
    while finished_rolling_dice == False:
        print(f"=====Dice Roll: Round {total_rolls}=====")
        player_1_score = dice_roll(player_1, player_1_score)
        player_2_score = dice_roll(player_2, player_2_score)
        total_rolls += 1
        if total_rolls > 5:
            finished_rolling_dice = True
    if finished_rolling_dice:
        print("All of the die have been rolled!")
        if player_1_score > player_2_score:
            print(f"The player with the highest score is {player_1} with {player_1_score} points!")
            handle_scores(True, player_1, player_1_score)
        else:
            print(f"The player with the highest score is {player_2} with {player_2_score} points!")
            handle_scores(True, player_2, player_2_score)
        print_top_scores()

def dice_roll(player_name: str, score: int):
    print(f"Rolling dice for {player_name}...")
    dice_result_1 = genint(1,6)
    dice_result_2 = genint(1,6)
    total_result = dice_result_1 + dice_result_2
    print(f"The 1st dice rolled a {dice_result_1}!")
    print(f"The 2nd dice rolled a {dice_result_2}!")
    score += total_result
    if total_result == 2 or total_result == 4 or total_result == 6 or total_result == 8 or total_result == 10 or total_result == 12:
        score += 10
    else:
        if score >= 0:
            score -= 5
    print(f"{player_name}'s current score is {score}!")
    print()
    return score
    
    if dice_result_1 == dice_result_2:
        print("A double was rolled, the dice will be rolled again!")
        dice_roll(player_name, score)

def handle_scores(saving: bool, name: str, score: int):
    def create_save():
        try:
            save = open("./scores.json", "x")
            save.write('{"save": []}')
            save.close
        except:
            print("Save located")
    
    def load_data():
        return load(open("./scores.json"))

    def append_score():
        data = load_data()
        data["save"].append(
            {
                "name": name,
                "score": score
            })
        dump(data, open(f"./scores.json", "w"), indent=4)
            
    if saving == True:
        create_save()
        append_score()
        print(load_data())
    if saving == False:
        return load_data()

def print_top_scores():
    print("=====Top Scores=====")
    data = handle_scores(False, None, None)
    try:
        name_1 = data["save"][0]['name']
        score_1 = data["save"][0]['score']
        name_2 = data["save"][1]['name']
        score_2 = data["save"][1]['score']
        name_3 = data["save"][2]['name']
        score_3 = data["save"][2]['score']
        name_4 = data["save"][3]['name']
        score_4 = data["save"][3]['score']
        name_5 = data["save"][4]['name']
        score_5 = data["save"][4]['score']
        
        print(f"1st place is {name_1} with a score of {score_1}.")
        print(f"2nd place is {name_2} with a score of {score_2}.")
        print(f"3rd place is {name_3} with a score of {score_3}.")
        print(f"4th place is {name_4} with a score of {score_4}.")
        print(f"5th place is {name_5} with a score of {score_5}.")
    except:
        print("!!Temporary error catch!!")
        print(f"Data: {data}")
    

main()
