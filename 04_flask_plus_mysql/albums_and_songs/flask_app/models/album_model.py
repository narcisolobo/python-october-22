from pprint import pprint
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.song_model import Song
DATABASE = 'vinyl_one_to_many'


class Album:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.artist = data['artist']
        self.description = data['description']
        self.is_owned = data['is_owned']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.songs = []
    
    def __repr__(self):
        return f'<Album: {self.title}>'

    # create a album
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO albums (title, artist, description) VALUES (%(title)s, %(artist)s, %(description)s);'
        album_id = connectToMySQL(DATABASE).query_db(query, data)
        return album_id

    # find all albums (no data needed)
    @classmethod
    def find_all(cls):
        query = 'SELECT * from albums;'
        results = connectToMySQL(DATABASE).query_db(query)
        albums = []
        for result in results:
            albums.append(Album(result))
        return albums

    # find one album by id
    @classmethod
    def find_by_id(cls, data):
        query = 'SELECT * from albums WHERE id = %(id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        album = Album(results[0])
        return album
    
    @classmethod
    def find_by_id_with_songs(cls, data):
        query = 'SELECT * from albums LEFT JOIN songs ON albums.id = songs.album_id WHERE albums.id = %(id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        pprint(results)
        album = Album(results[0])
        if results[0]['album_id']:
            for result in results:
                song_data = {
                    'id': result['songs.id'],
                    'title': result['songs.title'],
                    'created_at': result['songs.created_at'],
                    'updated_at': result['songs.updated_at'],
                    'album_id': result['album_id']
                }
                song = Song(song_data)
                album.songs.append(song)
        return album

    # update one album by id
    @classmethod
    def find_by_id_and_update(cls, data):
        query = 'UPDATE albums SET title = %(title)s, artist = %(artist)s, description = %(description)s, is_owned = %(is_owned)s WHERE id = %(id)s;'
        connectToMySQL(DATABASE).query_db(query, data)
        return True

    # delete one album by id
    @classmethod
    def find_by_id_and_delete(cls, data):
        query = 'DELETE FROM albums WHERE id = %(id)s;'
        connectToMySQL(DATABASE).query_db(query, data)
        return True
