import unittest

from utils import *

# player_name = "TestMan"
# rpg_data = {
#     "level" : 1,
#     "player_hp" : 50 ,
#     "enemy_hp" : 50 ,
#     "enemy_max_hp" : 50,
#     "potion_number" : 5 ,
#     "turn" :  0, 
#     "player_score" : 0,
#     "boss_name" : "Antoine",
# }

class TestAddWithUnittest(unittest.TestCase):
     #  on execute les tests en écrivant la commande suivante dans le terminal (de nombreuses options d'execution sont disponibles)
    """python -m unittest -v"""

    def test_player_is_alive(self):
        self.assertEqual(player_is_alive({"player_hp" : 10 }), True)
        self.assertEqual(player_is_alive({"player_hp" : 0 }), False)
        self.assertEqual(player_is_alive({"player_hp" : -5 }), False)
        
    def test_enemy_is_alive(self):
        self.assertEqual(enemy_is_alive({"enemy_hp" : 10 }), True)
        self.assertEqual(enemy_is_alive({"enemy_hp" : 0 }), False)
        self.assertEqual(enemy_is_alive({"enemy_hp" : -5 }), False)
    
    # def test_player_attack(self):
    #     self.assertEqual(player_attack(rpg_data, player_name), rpg_data["player_hp"])


        

        