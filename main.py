<<<<<<< HEAD

import random as rd
from utils import *
=======
from utils import player_is_alive, enemy_is_alive, display_status, player_attack, player_heals, ennemys_turn
 # Preparing a game
player_name = input("Choose a name for your avatar : ")
rpg_data = {
    "player_hp" : 50 ,
    "enemy_hp" : 50 ,
    "potion_number" : 3 ,
    "turn" :  0, 
    "boss_line_1" : " .-.   ",
    "boss_line_2" : "(o o)  ",
    "boss_line_3" : "| O \  ",
    "boss_line_4" : " \   \ ",
    "boss_line_5" : "  `~~~'",
    "boss_line_6" : "       ",
    "player_line_1" : "     ",
    "player_line_4" : "  o_/",
    "player_line_5" : "  |  ",
    "player_line_6" : " /\  ",
}
print("Welcome "+ player_name +". You will face off against the computer!")
print()
print('''In this battle you and the computer will take turns battling, the first to fall loses!
There are potions laying around for you to grab! You may use up to three potions!
Remember to grab potions BEFORE you attack !''')
>>>>>>> 072be81929ad3839fd61b2f06fe90a0bfc134099

# Player setup #

<<<<<<< HEAD
 # Preparing a game
player_name = input("Choose a name for your avatar : ")
print("Welcome "+ player_name +". You will face off against the computer!")
print()
print('''In this battle you and the computer will take turns battling, the first to fall loses!
There are potions laying around for you to grab! You may use up to three potions!
Remember to grab potions BEFORE you attack !''')



while player_is_alive(rpg_data) and enemy_is_alive(rpg_data):          # Check hp of both player and enemy  
=======

while player_is_alive(rpg_data) and enemy_is_alive(rpg_data):          # Check hp of both player and enemy
>>>>>>> 072be81929ad3839fd61b2f06fe90a0bfc134099
    # Check if enemy is still alive
    # if enemy_is_alive():
        print(rpg_data)
        # display the status of player : name, hp, number of potions left      
<<<<<<< HEAD
        afficher_status(rpg_data)    
=======
        display_status(rpg_data, player_name)    
>>>>>>> 072be81929ad3839fd61b2f06fe90a0bfc134099
        # check which turn
        if rpg_data["turn"]%2 == 0 :   # turn is pair
        # Demand an action from player: Either to attack or to take a potion
<<<<<<< HEAD
            action = input("Attack or potion \n")
            if action == "attack":
                player_attack(rpg_data)
            elif action == "potion":
                player_heals(rpg_data)
            #switch_turn
            rpg_data["turn"] += 1
=======
            action = input("What do you want to do ? (attack/potion) \n")
            if action.lower() == "attack":
                player_attack(rpg_data)
            elif action.lower() == "potion":
                player_heals(rpg_data)
            else:
                print('Veuillez entrer une action valide')
>>>>>>> 072be81929ad3839fd61b2f06fe90a0bfc134099
        
        # Enemy's turn
        else:
<<<<<<< HEAD
            enemy_turn()
            rpg_data["turn"]+=1
=======
            ennemys_turn(rpg_data)

print('Fin du jeu')
if enemy_is_alive(rpg_data):
    print ('GAME OVER')
else:
    print('Felicitations ')
>>>>>>> 072be81929ad3839fd61b2f06fe90a0bfc134099
