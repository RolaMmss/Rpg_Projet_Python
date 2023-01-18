from utils import * # player_is_alive, enemy_is_alive, afficher_status, player_attack, player_heals, ennemys_turn

 # Preparing a game
player_name = input("Choose a name for your avatar : ")
print("Welcome "+ player_name +". You will face off against the computer!")
print()
print('''In this battle you and the computer will take turns battling, the first to fall loses!
There are potions laying around for you to grab! You may use up to three potions!
Remember to grab potions BEFORE you attack !''')

# Player setup #


while player_is_alive() and enemy_is_alive():          # Check hp of both player and enemy
    # Check if enemy is still alive
    # if enemy_is_alive():
        
        # display the status of player : name, hp, number of potions left      
        afficher_status()    
        # check which turn
        if rpg_data["turn"]%2 == 0 :   # turn is pair
        
        # Demand an action from player: Either to attack or to take a potion
            action = input("What do you want to do ? (attack/potion) \n")
            if action == "attack":
                player_attack()
            elif action == "potion":
                player_heals()
            #switch_turn
            rpg_data["turn"] += 1
        
        # Enemy's turn
        else:
            ennemys_turn()
            rpg_data["turn"]+=1
