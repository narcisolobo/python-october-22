from pprint import pprint
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'vinyl_one_to_many'


class Song:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # FOREIGN KEY
        self.album_id = data['album_id']
    
    def __repr__(self):
        return f'<Song: {self.title}>'

    # create a song
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO songs (title, album_id) VALUES (%(title)s, %(album_id)s);'
        song_id = connectToMySQL(DATABASE).query_db(query, data)
        return song_id

    # find all songs (no data needed)
    @classmethod
    def find_all(cls):
        query = 'SELECT * from songs;'
        results = connectToMySQL(DATABASE).query_db(query)
        songs = []
        for result in results:
            songs.append(Song(result))
        return songs

    # find one song by id
    @classmethod
    def find_by_id(cls, data):
        query = 'SELECT * from songs WHERE id = %(id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        song = Song(results[0])
        return song

    # update one song by id
    @classmethod
    def find_by_id_and_update(cls, data):
        query = 'UPDATE songs SET title = %(title)s, album_id = %(album_id)s WHERE id = %(id)s;'
        connectToMySQL(DATABASE).query_db(query, data)
        return True

    # delete one song by id
    @classmethod
    def find_by_id_and_delete(cls, data):
        query = 'DELETE FROM songs WHERE id = %(id)s;'
        connectToMySQL(DATABASE).query_db(query, data)
        return True
