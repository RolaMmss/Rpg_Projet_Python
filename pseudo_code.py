 # Preparing a game
player_name = input("Choose a name for your avatar : ")

# Player setup #
rpg_data = {
    "player_hp" : 50 ,
    "enemy_hp" : 50 ,
    "potion_number" : 3 ,
    "turn" :  0 
}

# action = ["attack", "potion"]
    
while player_is_alive() and enemy_is_alive():          # Check hp of both player and enemy  
    # Check if enemy is still alive
    # if enemy_is_alive():
        
        # display the status of player : name, hp, number of potions left      
        afficher_status()    
        # check which turn
        if rpg_data["turn"]%2 == 0 :   # turn is pair
        
        # Demand an action from player: Either to attack or to take a potion
            action = input("Attack or potion")
            if action == "attack":
                player_attack()
            elif action == "potion":
                player_heals()
            #switch_turn
            rpg_data["turn"] += 1
        

        else:
            enemy_tun()
            rpg_data["turn"]+=1


    
    
    
    