

import random
user_name = input("Hello, what is your name? ")
print("Welcome "+ user_name +". You will face off against the computer!")
print()
print('''In this battle you and the computer will take turns battling, the first to fall loses!
There are potions laying around for you to grab! You may use up to three potions!
Remember to grab potions BEFORE you attack !''')
# Player setup #

while not player_is_dead:
   
    display_player_name_and_initial_score((name, score) :dict)
    # Start a game
    # Demand an action from player: Either to attack or to take a portion
    choice_attack_or portion()
        if choice == attack:
            pass
        elif choice == portion:
            pass
    switch_turn()