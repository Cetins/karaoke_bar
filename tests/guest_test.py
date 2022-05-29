import unittest

from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("John Brown", 150, "Run the world")
        
    def test_guest_has_name(self):
        self.assertEqual("John Brown", self.guest.name)
        
    def test_guest_has_wallet(self):
        self.assertEqual(150, self.guest.wallet)
        
    def test_guest_has_fav_song(self):
        self.assertEqual("Run the world", self.guest.fav_song)