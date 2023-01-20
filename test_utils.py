import unittest, random
from utils import *

player_name = "TestMan"
rpg_data = {
    "level" : 1,
    "player_hp" : 20 ,
    "enemy_hp" : 40 ,
    "enemy_max_hp" : 50,
    "potion_number" : 3 ,
    "turn" :  4, 
    "player_score" : 87,
    "boss_name" : "Antoine",
}

class TestRPGWithUnittest(unittest.TestCase):
     #  on execute les tests en écrivant la commande suivante dans le terminal (de nombreuses options d'execution sont disponibles)
    """python -m unittest -v"""

    random.seed(42)
    def test_player_is_alive(self):
        self.assertEqual(player_is_alive({"player_hp" : 10 }), True)
        self.assertEqual(player_is_alive({"player_hp" : 0}), False)
        
    def test_enemy_is_alive(self):
        self.assertEqual(enemy_is_alive({"enemy_hp" : 10 }), True)
        self.assertEqual(enemy_is_alive({"enemy_hp" : 0, "player_score" : 10, "turn" : 4 }), False)
    
    def test_player_attack(self):
        player_attack(rpg_data,player_name, False)
        self.assertEqual(rpg_data["enemy_hp"], 21)

    def test_player_heals(self):
        player_heals(rpg_data,player_name, False)
        self.assertEqual(rpg_data["player_hp"], 45)
        self.assertEqual(rpg_data["potion_number"], 2)

    def test_enemys_turn(self):
        enemys_turn(rpg_data,player_name, False)
        self.assertEqual(rpg_data["player_hp"],12)

    def test_all_enemies_dead(self):
        self.assertEqual(all_enemies_dead({"enemy_hp" : 15, "level" : 3}), False)
        self.assertEqual(all_enemies_dead({"enemy_hp" : 0, "level" : 1, "player_score" : 10, "turn" : 4 }), False)
        self.assertEqual(all_enemies_dead({"enemy_hp" : 0, "level" : 3, "player_score" : 10, "turn" : 4}), True)

    def test_ùnext_level(self):  #the ù is used because it will make this test run last (tests run by alphabet order)
        next_level(rpg_data, False)
        self.assertEqual(rpg_data["level"], 2)