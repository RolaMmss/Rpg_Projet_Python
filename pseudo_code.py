 # Preparing a game
player_name = input("Choose a name for your avatar : ")

rpg_data = {
    "player_hp" : 50 ,
    "enemy_hp" : 50 ,
    "potion_number" : 3 ,
    "turn" :  0 
}
    
while player_is_alive:        # Check hp of both player and enemy  
    check enemy_is_alive() 
    display_status() 
    player_name_and_initial_score((name, score) :dict)
    # Start a game
    # Demand an action from player: Either to attack or to take a portion
        input("Attack or potion")
        if choice == attack:
            pass
        elif choice == potion:
            pass
    switch_turn()
    



    
    
    
    