
import random as rd
from utils import *

# Player setup #
rpg_data = {
    "player_hp" : 50 ,
    "enemy_hp" : 50 ,
    "potion_number" : 3 ,
    "turn" :  0 
}

 # Preparing a game
player_name = input("Choose a name for your avatar : ")
print("Welcome "+ player_name +". You will face off against the computer!")
print()
print('''In this battle you and the computer will take turns battling, the first to fall loses!
There are potions laying around for you to grab! You may use up to three potions!
Remember to grab potions BEFORE you attack !''')



while player_is_alive(rpg_data) and enemy_is_alive(rpg_data):          # Check hp of both player and enemy  
    # Check if enemy is still alive
    # if enemy_is_alive():
        
        # display the status of player : name, hp, number of potions left      
        afficher_status(rpg_data)    
        # check which turn
        if rpg_data["turn"]%2 == 0 :   # turn is pair
        
        # Demand an action from player: Either to attack or to take a potion
            action = input("Attack or potion \n")
            if action == "attack":
                player_attack(rpg_data)
            elif action == "potion":
                player_heals(rpg_data)
            #switch_turn
            rpg_data["turn"] += 1
        

        else:
            enemy_turn()
            rpg_data["turn"]+=1
