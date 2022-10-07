import queue
from mysqlconnection import connectToMySQL
from pprint import pprint

class Album:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.artist = data['artist']
        self.description = data['description']
        self.is_owned = data['is_owned']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    def __repr__(self):
        return f'<Album: {self.title}>'
    
    # read all albums from db
    @classmethod
    def find_all(cls):
        query = 'SELECT * from albums;'
        results = connectToMySQL('albums_schema').query_db(query)
        albums = []
        for each_result in results:
            albums.append(Album(each_result))
        print('RESULTS LIST OF DICTIONARIES')
        pprint(results)
        print('ALBUMS LIST OF INSTANTIATED OBJECTS OF THE ALBUM CLASS')
        print(albums)
        return albums
    
    # read one album from db
    @classmethod
    def find_one(cls, data):
        query = 'SELECT * from albums WHERE id = %(id)s;'
        results = connectToMySQL('albums_schema').query_db(query, data)
        pprint(results)
        album = Album(results[0])
        return album
    
    # create an album
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO albums (title, artist, description) VALUES (%(title)s, %(artist)s, %(description)s);'
        album_id = connectToMySQL('albums_schema').query_db(query, data)
        return album_id
    
    @classmethod
    def update(cls, data):
        query = 'UPDATE albums SET title = %(title)s, artist = %(artist)s, description = %(description)s;'
        connectToMySQL('albums_schema').query_db(query, data)
        return
    
    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM albums WHERE id = %(id)s;'
        connectToMySQL('albums_schema').query_db(query, data)
        return
