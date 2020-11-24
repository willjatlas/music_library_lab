from db.run_sql import run_sql
from modules.album import Album
from modules.artist import Artist 

def save(artist):
    sql = "INSERT INTO artist (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def delete_all():
    sql = "DELETE FROM artist"
    run_sql(sql)

def select_id(id):
    artist = None 
    sql = "SELECT FROM artist WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist = Artist(result['name'], result['id'])
    return artist 
