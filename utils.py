
def player_is_alive() -> bool:
    """Checks if the player's HP is > 0

    Returns:
        bool: True if player's HP >0, else return False
    """
    if rpg_data["player_hp"] > 0:
        return True
    return False

def enemy_is_alive() -> bool:
    """checks if the enemy's HP is > 0

    Returns:
        bool: True if enemy's HP >0 else return False
    """
    if rpg_data["enemy_hp"] > 0:
        return True
    return False
    

def afficher_status() ->None:
    pass

def player_attack() -> None:
    rpg_data["enemy_hp"] -= (10 + randint(10))
    if rpg_data["enemy_hp"] < 0:
        rpg_data["enemy_hp"] = 0
    

def player_heals() -> None:
    if rpg_data["potion_number"] >= 1:
        rpg_data["potion_number"] -= 1
        rpg_data["player_hp"] += (17+randint(8))
        if rpg_data["player_hp"] > 50:
            rpg_data["player_hp"] = 50
    else:
        print("You don't have enough potions !")

def ennemys_turn() -> None:
    """plays enemy's turn
    player's health should decrease randomly of 5-20 hp
    """
    rpg_data["player_hp"] -= (5+randint(15))
    if rpg_data["player_hp"] < 0:
        rpg_data["player_hp"]= 0