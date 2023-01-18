
from random import randint

def player_is_alive(rpg_data) -> bool:
    """Checks if the player's HP is > 0

    Returns:
        bool: True if player's HP >0, else return False
    """
    if rpg_data["player_hp"] > 0:
        return True
    return False

def enemy_is_alive(rpg_data) -> bool:
    """checks if the enemy's HP is > 0

    Returns:
        bool: True if enemy's HP >0 else return False
    """
    if rpg_data["enemy_hp"] > 0:
        return True
    else:
        rpg_data["player_score"] += (10*rpg_data["turn"]) - rpg_data["turn"]
        return False
    

def display_status(rpg_data, player_name) ->None:
    """_summary_
    Display characters with names, healths, and potions
    """
    print(" ",
        player_name, "                              ", rpg_data["boss1"], "       ", "SCORE : ", rpg_data["player_score"],"\n"
        " HP : ", rpg_data["player_hp"], "/ 50                      HP : ", rpg_data["enemy_hp"], "/ 50","\n",
        " ",("◊")*rpg_data["potion_number"], "\n",
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

def player_attack(rpg_data, player_name) -> None:
    """if player choosed "attack", enemy_hp decrease randomly by 10-20 HP
    """
    degats = 15 + randint(0,10)
    rpg_data["enemy_hp"] -= degats
    rpg_data["player_score"] += degats
    if rpg_data["enemy_hp"] < 0:
        rpg_data["enemy_hp"] = 0
    rpg_data["turn"] += 1
    return f'{player_name} attacks GHOST, -{degats} HP'
    

def player_heals(rpg_data, player_name) -> None:
    """if player choosed "potion", player_hp increase randomly by 17-25 HP potion_number decrease by 1
    """
    soins = 22+randint(0,8)
    if rpg_data["potion_number"] >= 1:
        rpg_data["potion_number"] -= 1
        rpg_data["player_hp"] += soins
        rpg_data["turn"]+=1
        
        if rpg_data["player_hp"] > 50:
            rpg_data["player_hp"] = 50
        return f'{player_name} heals himself, he gains {soins} HP'
    else:
        print("You don't have enough potions !")

def ennemys_turn(rpg_data,player_name) -> None:
    """plays enemy's turn
    player's health should decrease randomly by 5-20 hp
    """
    degats = 7+randint(0,8)
    rpg_data["player_score"] += 1
    rpg_data["player_hp"] -= (degats)
    rpg_data["turn"]+=1
    if rpg_data["player_hp"] < 0:
        rpg_data["player_hp"]= 0
    return f'Ghost hit {player_name} ! Ouch ! -{degats} HP'
    
def all_enemies_dead(rpg_data):
    max_level = 2
    if rpg_data["level"] == max_level and not enemy_is_alive(rpg_data): #Test si on est au niveau Max (en l'occurence 2)
        return True
    return False

def next_level(rpg_data):
    rpg_data["level"] += 1
    
    if rpg_data["level"] == 2:          #LEVEL 2
        rpg_data["player_hp"] = 50
        rpg_data["enemy_hp"] = 75
        rpg_data["turn"] = 0
        rpg_data["boss_name"] = "" 
        rpg_data["boss_line_1"] = "  <=======]}======" #18 caractères de large
        rpg_data["boss_line_2"] = "    --.   /|      "
        rpg_data["boss_line_3"] = "   _\"/_.'/       "
        rpg_data["boss_line_4"] = " .'._._,.'        "
        rpg_data["boss_line_5"] = " :/ \{}/          "
        rpg_data["boss_line_6"] = "(L  /--',----._   "
        rpg_data["boss_line_7"] = "    |          \\ "
        rpg_data["boss_line_8"] = "   : /-\ .'-'\ / |"
        rpg_data["boss_line_9"] = "    \\, ||    \|  "
        rpg_data["boss_line_10"] ="     \/ ||    ||  "
        return 'CENTAUR INCOMING !!!'
