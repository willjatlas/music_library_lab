from db.run_sql import run_sql
from modules.album import Album
from modules.artist import Artist 
import repositories.artist_repository as artist_repository

def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def delete_all():
    sql = "DELETE FROM album"
    run_sql(sql)

def select_id(id):
    album = None 
    sql = "SELECT FROM album WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        album = Album(result['title'], result['artist'], result["genre"], result['id'])
    return album