# Rpg_Projet_Python
Brief 1 -  SAS Tech IA

### About this game: ###

In this game, you and the computer (enemies) will take turns battling, the first to fall loses! Each starts with a 50 health points (HP). There are potions laying around for you to grab! The enemy has no potions. These potions help you to recover randomly by 30-40 HP. You may use up to five potions! Remember to grab potions BEFORE you attack ! The game consists of three levels with different enemies to beat.

### Run the game: ### 

The game runs via main.py.

### Start of the game: ### 
1- The player is requested to supply a pseudo name.
2- Names of player and enemy, hps, score and potions are displayed. In addition, images of both is generated using letters and special characters .

### Functionalities of the game: ### 
1- As long as the player and all enemies are alive, the game continues. 
2- If it is player's turn, two actions are suggested, either to attack or to  take a potion : "What do you want to do ? (attack/potion) "
    - If the player chooses to attack, enemy's health decreases randomly. Python generates this random amount.
    - If the player chooses to take a potion, his health increases randomly and number of potions decreases by 1.
    - If the player supplies an invalid action, a message is displayed : "Please enter a valid action".
<!-- 2- If it is enemy's turn, depending on what monster you're facing a choice is generated: either to attack (75%) and the player randomly looses HP (7-15 HP) or to recover (25%) and in this case the enemy randomly gains HP (7-10 HP) and the player randomly looses HP (7-10 HP). -->

### End of game: ### 
    1- Once the enemy's HP becomes zero, the player wins first level and a new level starts with a different enemy.
        - When all enemies are dead, the player wins and the game ends.
    2- When the player's HP becomes zero then the game ends and a "GAME OVER" message is displayed.

### Requirements: ### 
    Visual Studio Code - code editor
    Python - Interpreted programming language.
    Pysound module - "pip install pysound" (pip3 if unknown command) in the terminal then follow the instructions, you may need to update to PyObjC if you get errors for missing audio files


### Version : 1.0

### Authors: ### 
    Rola Sadek
    David Breau
    Maxime Rowell





