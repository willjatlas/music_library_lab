import unittest
from modules.artist import Artist

class TestArtist(unittest.TestCase):

    def setUp(self):
        self.artist = Artist("Animals as Leaders")

    def test_artist_has_name(self):
        self.assertEqual("Animals as Leaders", self.artist.name)