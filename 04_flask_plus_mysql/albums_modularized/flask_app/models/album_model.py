from pprint import pprint
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'albums_schema'


class Album:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.artist = data['artist']
        self.description = data['description']
        self.is_owned = data['is_owned']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # create
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO albums (title, artist, description) VALUES (%(title)s, %(artist)s, %(description)s);'
        album_id = connectToMySQL(DATABASE).query_db(query, data)
        print(f'Created: <Album {album_id}>')
        return album_id

    # find all (no data needed)
    @classmethod
    def find_all(cls):
        query = 'SELECT * from albums;'
        results = connectToMySQL(DATABASE).query_db(query)
        albums = []
        for result in results:
            albums.append(Album(result))
        print(f'Found all albums:')
        pprint(albums)
        return albums

    # find one by id
    @classmethod
    def find_by_id(cls, data):
        query = 'SELECT * from albums WHERE id = %(id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        album = Album(results[0])
        print(f'Found: <Album {data["id"]}>')
        return album

    # update one by id
    @classmethod
    def find_by_id_and_update(cls, data):
        query = 'UPDATE albums SET title = %(title)s, artist = %(artist)s, description = %(description)s WHERE id = %(id)s;'
        connectToMySQL(DATABASE).query_db(query, data)
        print(f'Updated: <Album {data["id"]}>')
        return True

    # delete one by id
    @classmethod
    def find_by_id_and_delete(cls, data):
        query = 'DELETE FROM albums WHERE id = %(id)s;'
        connectToMySQL(DATABASE).query_db(query, data)
        print(f'Deleted: <Album {data["id"]}>')
        return True
