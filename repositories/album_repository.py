from db.run_sql import run_sql
from modules.album import Album
from modules.artist import Artist 
import repositories.artist_repository as artist_repository

def save(album):
    sql = ("INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *")
    values = [album.title, album.genre, album.artist_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album


