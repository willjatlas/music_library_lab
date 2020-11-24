import unittest
from modules.album import Album

class TestAlbum(unittest.TestCase):

    def setUp(self):
        self.album = Album("The Joy of Motion", "Animals as Leaders", "Alt Prog Metal Jazz")

    def test_album_has_title(self):
        self.assertEqual("The Joy of Motion", self.album.title)
    
    def test_album_has_artist(self):
        self.assertEqual("Animals as Leaders", self.album.artist)

    def test_album_had_genre(self):
        self.assertEqual("Alt Prog Metal Jazz", self.album.genre)