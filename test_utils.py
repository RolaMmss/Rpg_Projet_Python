import unittest, random

from utils import *

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
    

        