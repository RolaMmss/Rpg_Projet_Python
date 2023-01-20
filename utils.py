import csv
from random import randint
import csv
from playsound import playsound


def player_is_alive(rpg_data) -> bool:
    """Checks in rpg_data if player_hp is > 0

    Args:
        rpg_data (dict): dict containing all data needed for the game to run and evolve

    Returns:
        bool: True if player's HP >0, else return False
    """
    return rpg_data["player_hp"] > 0

def enemy_is_alive(rpg_data) -> bool:
    """checks in rpg_data if enemy_hp > 0

    Args:
        rpg_data (dict): dict containing all data needed for the game to run and evolve

    Returns:
        bool: True if enemy's HP > 0 else return False
    """
    if rpg_data["enemy_hp"] > 0:
        return True
    else:
        rpg_data["player_score"] += (10*rpg_data["turn"]) - rpg_data["turn"]
        return False
    

def display_status(rpg_data, player_name) -> None:
    """Display characters with names, healths, and potions via rpg_data, lines for ascii charac and data like hp etc...

    Args:
        rpg_data (dict): dict that contains all the data neeed for the game to run adn evolve
        player_name ([type]): var that's not changing during the game, coming from an input at the beginning of the main.py file
    """
    print(" "*24, "SCORE : ", "%04d" % rpg_data["player_score"], "\n",
        "   [", player_name.upper(), " "*(16 - len(player_name)), "]", " "*(11),
        "[", rpg_data["boss_name"].upper(), " "*(16 - len(rpg_data["boss_name"])), "]", "\n",
        "   [ HP :", rpg_data["player_hp"], "/ 50", " "*(6 - len(str(rpg_data["player_hp"]))), "]", " "*11,
        "[ HP : ", rpg_data["enemy_hp"], "/ ",rpg_data["enemy_max_hp"], " "*(6 - len(str(rpg_data["enemy_hp"])) - len(str(rpg_data["enemy_max_hp"]))),"]\n",
        "   [ Potions :",("◊")*rpg_data["potion_number"], " "*(6 - rpg_data["potion_number"]), "]", " "*11 , "[", " "*17, "]\n",
        "       ", rpg_data["player_line_1"], "                  ", rpg_data["boss_line_1"], "\n",
        "       ", rpg_data["player_line_2"], "                  ", rpg_data["boss_line_2"], "\n",
        "       ", rpg_data["player_line_3"], "                  ", rpg_data["boss_line_3"], "\n",
        "       ", rpg_data["player_line_4"], "                  ", rpg_data["boss_line_4"], "\n",
        "       ", rpg_data["player_line_5"], "                  ", rpg_data["boss_line_5"], "\n",
        "       ", rpg_data["player_line_6"], "                  ", rpg_data["boss_line_6"], "\n",
        "       ", rpg_data["player_line_7"], "                  ", rpg_data["boss_line_7"], "\n",
        "       ", rpg_data["player_line_8"], "                  ", rpg_data["boss_line_8"], "\n",
        "       ", rpg_data["player_line_9"], "                  ", rpg_data["boss_line_9"], "\n",
        "       ", rpg_data["player_line_10"], "                  ", rpg_data["boss_line_10"], "\n",
        )

def player_attack(rpg_data, player_name) -> str:
    """if player choosed "attack", enemy_hp decrease randomly by 10-20 HP

    Args:
        rpg_data (dict): dict containing all data from the game
        player_name (str): name that came from the input at the beginning of the main.py file

    Returns:
        str: sentence that must be displayed under the display_status via the phrase var
    """
    random_attack_sound = randint(0,3)
    if random_attack_sound == 0:
        playsound('media/ATTACK.mp3')
    elif random_attack_sound == 1:
        playsound('media/SWORD.mp3')
    elif random_attack_sound == 2:
        playsound('media/SWORD2.mp3')
    elif random_attack_sound == 3:
        playsound('media/KNIFE.mp3')        
    degats = 15 + randint(0,10)
    rpg_data["enemy_hp"] -= degats
    rpg_data["player_score"] += degats
    if rpg_data["enemy_hp"] < 0:
        rpg_data["enemy_hp"] = 0
    rpg_data["turn"] += 1
    return f'{player_name} attacks {rpg_data["boss_name"]}, -{degats} HP'
    

def player_heals(rpg_data, player_name) -> str:
    """if player choosed "potion", player_hp increase randomly by 17-25 HP potion_number decrease by 1

    Args:
        rpg_data (dict): dict containing all data from the game
        player_name (str): name that came from the input at the beginning of the main.py file

    Returns:
        str: returns the sentence that must be displayed une display_status via the phrase var
    """
    playsound('media/potion.mp3')

    soins = 30+randint(0,10)
    if rpg_data["potion_number"] >= 1:
        rpg_data["potion_number"] -= 1
        rpg_data["player_hp"] += soins
        rpg_data["turn"]+=1
        
        if rpg_data["player_hp"] > 50:
            rpg_data["player_hp"] = 50
        return f'{player_name} heals himself, he gains {soins} HP'
    else:
        print("You don't have enough potions !")

def ennemys_turn(rpg_data,player_name) -> str:
    """plays enemy's turn., depending on rpg_data["level"], decrease player's HP and in some came, increase enemy's HP

    Args:
        rpg_data (dict): dict containing all data from the game
        player_name (str): name that came from the input at the beginning of the main.py file

    Returns:
        str: returns the sentence that must be displayed une display_status via the phrase var
    """
    
    if rpg_data["level"] == 1:
        playsound('media/GHOST2.mp3')
        degats = 7+randint(0,8)
        rpg_data["player_hp"] -= (degats)
        rpg_data["turn"]+=1
        if rpg_data["player_hp"] < 0:
            rpg_data["player_hp"]= 0
        return f'{rpg_data["boss_name"]} hit {player_name} ! Ouch ! -{degats} HP'

    elif rpg_data["level"] == 2:
        playsound('media/STRONGHIT.mp3')
        choix = randint(0,3)
        if choix == 2:
            degats = 7 + randint(0,3)
            rpg_data["player_hp"] -= degats
            rpg_data["enemy_hp"] += degats
            rpg_data["turn"] += 1
            if rpg_data["player_hp"] < 0:
                rpg_data["player_hp"]= 0
            if rpg_data["enemy_hp"] > 75:
                rpg_data["enemy"]= 75
            return f'{rpg_data["boss_name"]} steals {degats} HP from {player_name}'
        else:
            degats = 12+randint(0,6)
            rpg_data["player_hp"] -= degats
            rpg_data["turn"]+=1
            if rpg_data["player_hp"] < 0:
                rpg_data["player_hp"]= 0
            return f'{rpg_data["boss_name"]} hit {player_name} with his spear ! -{degats} HP'
        
    elif rpg_data["level"] == 3:
        playsound('media/dragonfire.mp3')
        choix = randint(0,5)
        if choix == 2 or choix ==3:
            degats = 17 + randint(0,3)
            rpg_data["player_hp"] -= degats
            rpg_data["turn"] += 1
            if rpg_data["player_hp"] < 0:
                rpg_data["player_hp"]= 0
            if rpg_data["enemy_hp"] > 100:
                rpg_data["enemy"]= 100
            return f'{rpg_data["boss_name"]} throws fire to {player_name} ! -{degats} HP '
        
        elif choix == 4:
            degats = 0
            rpg_data["player_hp"] -= degats
            rpg_data["turn"] += 1
            if rpg_data["player_hp"] < 0:
                rpg_data["player_hp"]= 0
            if rpg_data["enemy_hp"] > 100:
                rpg_data["enemy"]= 100
            return f'{rpg_data["boss_name"]} missed !'
        
        else:
            degats = 12+randint(0,8)
            rpg_data["player_hp"] -= degats
            rpg_data["turn"]+=1
            if rpg_data["player_hp"] < 0:
                rpg_data["player_hp"]= 0
            return f'{rpg_data["boss_name"]} hit {player_name} with his claws ! -{degats} HP'


    
def all_enemies_dead(rpg_data) -> bool:
    """checks in rpg_data if not enemy_is_alive and if the level is the max level

    Args:
        rpg_data (dict): dict containing all data from the game

    Returns:
        bool: returns True if you defeated the last level, else return False
    """
    max_level = 3
    if rpg_data["level"] == max_level and not enemy_is_alive(rpg_data):     #Test si on est au niveau Max (en l'occurence 2)
        return True
    return False

def next_level(rpg_data):
    """increses the level by 1 and changes data in rpg_data to reset the player's hp andn the boss name life etc

    Args:
        rpg_data (dict): dict containing all data from the game

    Returns:
        str: returns the sentence that must be displayed une display_status via the phrase var
    """
    playsound('media/goodresult-82807.mp3')
    rpg_data["level"] += 1
    
    if rpg_data["level"] == 2:          #LEVEL 2
        rpg_data["player_hp"] = 50
        rpg_data["enemy_hp"] = 75
        rpg_data["enemy_max_hp"] = 75
        rpg_data["turn"] = 0
        rpg_data["boss_name"] = "Charles" 
        rpg_data["boss_line_1"] = "  <=======]}======" #18 caractères de large
        rpg_data["boss_line_2"] = "    --.   /|      "
        rpg_data["boss_line_3"] = "   _ \"/_.'/       "
        rpg_data["boss_line_4"] = " .'._._,.'        "
        rpg_data["boss_line_5"] = " :/ \{}/          "
        rpg_data["boss_line_6"] = "(L  /--',----._   "
        rpg_data["boss_line_7"] = "    |          \\\ "
        rpg_data["boss_line_8"] = "   : /-\ .'-'\ / |"
        rpg_data["boss_line_9"] = "    \\\ , ||    \|  "
        rpg_data["boss_line_10"] ="     \/ ||    ||  "
        return 'Level 2 - CENTAUR INCOMING !!!'
    
    elif rpg_data["level"] == 3:          #LEVEL 3
        rpg_data["player_hp"] = 50
        rpg_data["enemy_hp"] = 100
        rpg_data["enemy_max_hp"] = 100
        rpg_data["turn"] = 0
        rpg_data["boss_name"] = "Safia" 
        rpg_data["boss_line_1"] = "              \.        `.         `.   " #39 caractères de large
        rpg_data["boss_line_2"] = "      (,,(,    \.         `.   ____,-`.,"
        rpg_data["boss_line_3"] = "   (,'     `/   \.   ,--.___`.'         "
        rpg_data["boss_line_4"] = ",  ,'  ,--.  `,   \.;'         `        "
        rpg_data["boss_line_5"] = " `{D, {    \  :    \;                   "
        rpg_data["boss_line_6"] = "   V,,'    /  /    //                   "
        rpg_data["boss_line_7"] = "   j;;    /  ,' ,-//.    ,---.      ,   "
        rpg_data["boss_line_8"] = "   \;'   /  ,' /  _  \  /  _  \   ,'/   "
        rpg_data["boss_line_9"] = "         \   `'  / \  `'  / \  `.' /    "
        rpg_data["boss_line_10"] ="          `.___,'   `.__,'   `.__,'     "
        return 'DRAGON INCOMING !!!'


def display_victory(rpg_data) -> None:
    """displays congrats message, your score and which level you're going to beat after

    Args:
        rpg_data (dict): dict containing all data from the game
    """
    print(
    "\n\n       ", rpg_data["player_line_1"],
    "\n       ", rpg_data["player_line_2"],
    "\n       ", rpg_data["player_line_3"], f"  Well done, you defeated" 
    "\n       ", rpg_data["player_line_4"], f"         level {rpg_data['level']}."
    "\n       ", rpg_data["player_line_5"], f"    Prepare for level {rpg_data['level']+1}"
    "\n       ", rpg_data["player_line_6"],
    "\n       ", rpg_data["player_line_7"], f"    your score is : {rpg_data['player_score']}", 
    "\n       ", rpg_data["player_line_8"],
    "\n       ", rpg_data["player_line_9"], 
    "\n       ", rpg_data["player_line_10"], )
    # playsound('media/goodresult-82807.mp3')



def save_score(rpg_data, player_name):
    print(f'Your score is {rpg_data["player_score"]}')
    if input('Do you want to save your score ? (Y/N) ').upper() == 'Y' :
        
        with open ('score.csv', 'a') as file:
            writing = csv.writer(file)
            writing.writerow([rpg_data['player_score'], player_name])





def display_final(rpg_data):
    if player_is_alive(rpg_data):
        print(
            " __     ______  _    _  __          _______ _   _    _ \n",
            " \ \   / / __ \| |  | | \ \        / /_   _| \ | |  | |\n",
            "  \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| |  | |\n",
            "   \   /| |  | | |  | |   \ \/  \/ /   | | | . ` |  | |\n",
            "    | | | |__| | |__| |    \  /\  /   _| |_| |\  |  |_|\n",
            "    |_|  \____/ \____/      \/  \/   |_____|_| \_|  (_)\n"
        )
        playsound("media/medieval-fanfare")

    else:
        print(
            "  _____                         ____  \n",
            " / ____|                       / __ \  \n",
            "| |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ \n",
            "| | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|\n",
            "| |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   \n",
            " \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   \n"
        )
        playsound("media/player_dead")
    
    with open ('score.csv', 'r') as file:
        reader=csv.reader(file)
        scores = list(reader)
        sorted_scores = sorted(scores, key = lambda x : x[0], reverse = True)
    
    trophy_l1 = f'  _______  '
    trophy_l2 = f' |  N°1  | '
    trophy_l3 = f'(|{" "*(3-len(sorted_scores[0][1])//2)}{sorted_scores[0][1][:7]}{" "*(int(4-len(sorted_scores[0][1])/2))}|)'
    trophy_l4 = f' |  {sorted_scores[0][0][:5]}  | '
    trophy_l5 = f'  \     /  '
    trophy_l6 = f"   `---'   "
    trophy_l7 = f'   _|_|_   '

    print(
        '\n    Thanks for playing !\n',
        '  //    HIGHSCORES    \\\ ')
    for i in range(7):
        print(str(eval(f'trophy_l{i+1}')+'     '),end='')
        if i!=0:
            try:
                print(f'{i+1}. {" ".join(sorted_scores[i])}')
            except:
                print('')
        else:
            print('')

