
from random import randint

def player_is_alive(rpg_data) -> bool:
    """Checks in rpg_data if player_hp is > 0

    Args:
        rpg_data (dict): dict containing all data needed for the game to run and evolve

    Returns:
        bool: True if player's HP >0, else return False
    """
    if rpg_data["player_hp"] > 0:
        return True# Player setup #
    return False

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
    print(" "*24, "SCORE : ", rpg_data["player_score"], "\n",
        "   [", player_name.upper(), " "*(15 - len(player_name)), "]", " "*(11),
        "[", rpg_data["boss_name"].upper(), " "*(15 - len(rpg_data["boss_name"])), "]", "\n",
        "   [ HP :", rpg_data["player_hp"], "/ 50     ]", " "*11, "[ HP : ", rpg_data["enemy_hp"], "/ ",rpg_data["enemy_max_hp"],"  ]\n",
        "   [ Potions :",("◊")*rpg_data["potion_number"], " "*(5 - rpg_data["potion_number"]), "]", " "*11 , "[", " "*16, "]\n",
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
        degats = 7+randint(0,8)
        rpg_data["player_hp"] -= (degats)
        rpg_data["turn"]+=1
        if rpg_data["player_hp"] < 0:
            rpg_data["player_hp"]= 0
        return f'{rpg_data["boss_name"]} hit {player_name} ! Ouch ! -{degats} HP'

    elif rpg_data["level"] == 2:
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

    
def all_enemies_dead(rpg_data) -> bool:
    """checks in rpg_data if not enemy_is_alive and if the level is the max level

    Args:
        rpg_data (dict): dict containing all data from the game

    Returns:
        bool: returns True if you defeated the last level, else return False
    """
    max_level = 2
    if rpg_data["level"] == max_level and not enemy_is_alive(rpg_data): #Test si on est au niveau Max (en l'occurence 2)
        return True
    return False

def next_level(rpg_data):
    """increses the level by 1 and changes data in rpg_data to reset the player's hp andn the boss name life etc

    Args:
        rpg_data (dict): dict containing all data from the game

    Returns:
        str: returns the sentence that must be displayed une display_status via the phrase var
    """
    
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

def display_final(rpg_data, player_name):
    pass
