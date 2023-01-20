from utils import player_is_alive, enemy_is_alive, display_status, player_attack, player_heals, enemys_turn ,next_level, all_enemies_dead, display_victory, save_score, display_final
from playsound import playsound

 # Preparing a game
while True:
    player_name = input("Choose a name for your avatar : ")

    if len(player_name) > 16:
        print('Enter a maximum of 16 characters.')
        continue
    else:
        break
phrase = ('')
rpg_data = {
    "level" : 1,
    "player_hp" : 50 ,
    "enemy_hp" : 50 ,
    "enemy_max_hp" : 50,
    "potion_number" : 5 ,
    "turn" :  0, 
    "player_score" : 0,
    "boss_name" : "Antoine",
    "boss_line_1" : "       ",
    "boss_line_2" : "       ",
    "boss_line_3" : "       ",
    "boss_line_4" : "       ",
    "boss_line_5" : " .-.   ",
    "boss_line_6" : "(o o)  ",
    "boss_line_7" : "| O \  ",
    "boss_line_8" : " \   \ ",
    "boss_line_9" : "  `~~~'",
    "boss_line_10" : "       ",
    "player_line_1" : "            ",
    "player_line_2" : "            ",
    "player_line_3" : "\           ",
    "player_line_4" : " \   ~~,    ",
    "player_line_5" : " _\_  (=> _ ",
    "player_line_6" : "  <}.==\"./I\\",
    "player_line_7" : "   '-\T/-\I/",
    "player_line_8" : "     /_\    ",
    "player_line_9" : "   _// \\\   ",
    "player_line_10" : "   \    I_  "
}

print("Welcome "+ player_name +" in Escape from Simplon")
print()
print('''You're going to face MONSTERS coming to teach you IA things !
Be careful, it could be really hurtful sometimes, Good luck !''')
playsound('media/goodresult-82807.mp3')

while player_is_alive(rpg_data) and not all_enemies_dead(rpg_data):          # Check hp of both player and enemy
    # Check if enemy is still alive
    if enemy_is_alive(rpg_data):
        # display the status of player : name, hp, number of potions left        
        display_status(rpg_data, player_name)  
        if phrase !=None and phrase != '' :
            print(phrase)
            input()
        # check which turnpip install pygobject
        if rpg_data["turn"]%2 == 0 :   # turn is pair
        # Demand an action from player: Either to attack or to take a potion
            action = input("What do you want to do ? (Attack [A]/ Potion [P]) \n")
            if action.lower() == "attack" or action.lower() == "a":
                phrase = player_attack(rpg_data,player_name)
            elif action.lower() == "potion" or action.lower() == "p":
                phrase = player_heals(rpg_data,player_name)
            else:
                print('Please enter a valid action ')
        
        # Enemy's turn
        else:
            phrase = enemys_turn(rpg_data, player_name)
    
    else:
        display_victory(rpg_data)
        input()
        phrase = next_level(rpg_data)

display_final(rpg_data)
save_score(rpg_data,player_name)

