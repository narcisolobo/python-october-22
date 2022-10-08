from pprint import pprint
from flask_app import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user_model

DATABASE = 'vinyl_countdown'


class Album:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.artist = data['artist']
        self.description = data['description']
        self.is_owned = data['is_owned']
        self.release_date = data['release_date']
        self.creator_id = data['creator_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = data['creator']
    
    def __repr__(self):
        return f'<Album: {self.title}>'
    
    @staticmethod
    def validate_album_form(form):
        is_valid = True
        if len(form['title']) < 2:
            flash('Title must be at least two characters.', 'title')
            is_valid = False
        if len(form['artist']) < 2:
            flash('Artist must be at least two characters.', 'artist')
            is_valid = False
        if len(form['description']) < 10:
            flash('Description must be at least two characters.', 'description')
            is_valid = False
        if not form['is_owned']:
            flash('Please select yes or no.', 'is_owned')
            is_valid = False
        if not form['release_date']:
            flash('Please enter release date.', 'release_date')
            is_valid = False
        return is_valid

    # create an album
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO albums (title, artist, description, is_owned, release_date, creator_id) VALUES (%(title)s, %(artist)s, %(description)s, %(is_owned)s, %(release_date)s, %(creator_id)s);'
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

    # find all albums with creators (no data needed)
    @classmethod
    def find_all_with_creators(cls):
        query = 'SELECT * from albums JOIN users ON albums.creator_id = users.id;'
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        albums = []
        for result in results:
            user_data = {
                'id': result['creator_id']
            }
            creator = user_model.User.find_by_id(user_data)
            album_data = {
                'id': result['id'],
                'title': result['title'],
                'artist': result['artist'],
                'description': result['description'],
                'is_owned': result['is_owned'],
                'release_date': result['release_date'],
                'creator_id': result['creator_id'],
                'created_at': result['created_at'],
                'updated_at': result['updated_at'],
                'creator': creator
            }

            album = Album(album_data)
            albums.append(album)
            
        return albums

    # find one album by id
    @classmethod
    def find_by_id(cls, data):
        query = 'SELECT * from albums WHERE id = %(id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        album = Album(results[0])
        return album

    # find one album by id with creator
    @classmethod
    def find_by_id_with_creator(cls, data):
        query = 'SELECT * from albums JOIN users ON albums.creator_id = users.id WHERE albums.id = %(id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        pprint(results)
        user_data = {
            'id': results[0]['creator_id']
        }
        creator = user_model.User.find_by_id(user_data)
        album_data = {
            'id': results[0]['id'],
            'title': results[0]['title'],
            'artist': results[0]['artist'],
            'description': results[0]['description'],
            'is_owned': results[0]['is_owned'],
            'release_date': results[0]['release_date'],
            'creator_id': results[0]['creator_id'],
            'created_at': results[0]['created_at'],
            'updated_at': results[0]['updated_at'],
            'creator': creator
        }
        album = Album(album_data)
        return album

    # update one album by id
    @classmethod
    def find_by_id_and_update(cls, data):
        query = 'UPDATE albums SET title = %(title)s, artist = %(artist)s, description = %(description)s, is_owned = %(is_owned)s, release_date = %(release_date)s, creator_id = %(creator_id)s WHERE id = %(id)s;'
        connectToMySQL(DATABASE).query_db(query, data)
        return True

    # delete one album by id
    @classmethod
    def find_by_id_and_delete(cls, data):
        query = 'DELETE FROM albums WHERE id = %(id)s;'
        connectToMySQL(DATABASE).query_db(query, data)
        return True
