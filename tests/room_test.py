import unittest

from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.empty_room = Room(0, 0, 0, [])
        self.room1 = Room(3, 5, 15, [])
        self.playlist1 = [
            Song("My Immortal", "Evanescence"),
            Song("I Cant Dance", "Genesis"),
            Song("Icky Thump", "The White Stripes"),
            Song("Howlin For You", "The Black Keys"),
            Song("Galvanize", "Chemical Brothers"),
            Song("Breaking The Habit", "Linkin Park"),
            Song("Legendary", " Welshly Arms"),
            Song("Stone Cold Classics", "AKA George"),
            Song("Back To Black", "Amy Winehouse")
            ]
        self.guests = [
            Guest("Sheldon", 80, "At Last"),
            Guest("Amy", 90, "On The Beach"),
            Guest("Leonard", 90, "Galvanize")
        ]

    def test_room_has_number(self):
        self.assertEqual(3, self.room1.number)
        
    def test_room_has_capacity(self):
        self.assertEqual(5, self.room1.capacity)
        
    def test_room_has_entry_fee(self):
        self.assertEqual(15, self.room1.entry_fee)
        
    def test_open_room(self):
        self.empty_room.open_room(3, 5 , 15, self.playlist1)
        self.assertEqual(self.room1.number, self.empty_room.number)
        self.assertEqual(self.room1.capacity, self.empty_room.capacity)
        self.assertEqual(self.room1.entry_fee, self.empty_room.entry_fee)
        self.assertEqual(self.playlist1, self.empty_room.playlist)
        
    def test_check_availability_true(self):
        self.assertEqual(True, self.room1.check_availability(self.room1, 3))
        
    
    def test_check_availability_false(self):
        self.assertEqual(False, self.empty_room.check_availability(self.empty_room, 3))
        self.assertEqual(False, self.room1.check_availability(self.room1, 6))
        
    def test_check_in(self):
        self.room1.check_in(self.room1 ,self.guests)
        self.assertEqual(2, self.room1.capacity)
        self.assertEqual(65, self.guests[0].wallet)
        self.assertEqual(75, self.guests[2].wallet)
        
    def test_check_out(self):
        self.room1.check_out(self.room1, self.guests)
        self.assertEqual(8, self.room1.capacity)
        
    def test_check_in_and_out(self):
        self.room1.check_in(self.room1, self.guests)
        self.assertEqual(2, self.room1.capacity)
        self.room1.check_out(self.room1, self.guests)
        self.assertEqual(5, self.room1.capacity)
        
    def test_take_payment(self):
        self.room1.take_payment(self.room1, self.guests)
        self.assertEqual(65, self.guests[0].wallet)
        self.assertEqual(75, self.guests[2].wallet)
        
    def test_guest_fav_song(self):
        self.room1.open_room(3, 5 , 15, self.playlist1)
        self.room1.check_in(self.room1 ,self.guests)
        self.assertEqual(True, self.room1.guest_fav_song(self.room1, self.guests))
        self.assertEqual("Whoo!", self.room1.check_in(self.room1, self.guests))
        
        