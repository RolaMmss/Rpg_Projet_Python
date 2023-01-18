
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
    return False
    

def display_status(rpg_data, player_name) ->None:
    """_summary_
    Display characters with names, healths, and potions
    """
    print(" ",
        player_name, "                           rpg_data["boss1"], "\n",
        " HP : ", rpg_data["player_hp"], "/ 50                      HP : ", rpg_data["enemy_hp"], "/ 50","\n",
        " ",("◊")*rpg_data["potion_number"], "\n",
        "       ", rpg_data["player_line_1"], "                  ", rpg_data["boss_line_1"], "\n",
        "       ", rpg_data["player_line_1"], "                  ", rpg_data["boss_line_2"], "\n",
        "       ", rpg_data["player_line_1"], "                  ", rpg_data["boss_line_1"], "\n",
        "       ", rpg_data["player_line_4"], "                  ", rpg_data["boss_line_4"], "\n",
        "       ", rpg_data["player_line_5"], "                  ", rpg_data["boss_line_5"], "\n",
        "       ", rpg_data["player_line_6"], "                  ", rpg_data["boss_line_6"], "\n",
        )

def player_attack(rpg_data) -> None:
    """if player choosed "attack", enemy_hp decrease randomly by 10-20 HP
    """
    rpg_data["enemy_hp"] -= (10 + randint(0,10))
    if rpg_data["enemy_hp"] < 0:
        rpg_data["enemy_hp"] = 0
    rpg_data["turn"] += 1
    

def player_heals(rpg_data) -> None:
    """if player choosed "potion", player_hp increase randomly by 17-25 HP potion_number decrease by 1
    """
    if rpg_data["potion_number"] >= 1:
        rpg_data["potion_number"] -= 1
        rpg_data["player_hp"] += (22+randint(0,8))
        rpg_data["turn"]+=1
        if rpg_data["player_hp"] > 50:
            rpg_data["player_hp"] = 50
    else:
        print("You don't have enough potions !")

def ennemys_turn(rpg_data) -> None:
    """plays enemy's turn
    player's health should decrease randomly by 5-20 hp
    """
    rpg_data["player_hp"] -= (10+randint(0,15))
    rpg_data["turn"]+=1
    if rpg_data["player_hp"] < 0:
        rpg_data["player_hp"]= 0
    
