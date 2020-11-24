import pdb
from modules.artist import Artist
from modules.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist('Animals as Leaders')
artist_repository.save(artist_1)

album_1 = Album("Joy of Motion", artist_1, "Prog Metal Jazz Alt")
album_repository.save(album_1)
