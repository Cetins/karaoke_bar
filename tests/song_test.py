import unittest

from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Breaking the habit", "Linkin Park")
        
    def test_song_has_name(self):
        self.assertEqual("Breaking the habit", self.song.name)
        
    def test_song_has_artist(self):
        self.assertEqual("Linkin Park", self.song.artist)