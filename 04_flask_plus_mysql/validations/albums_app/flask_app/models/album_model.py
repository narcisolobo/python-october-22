from flask_app import flash
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
    
    def __repr__(self):
        return f'<Album: {self.title}>'

    # this static method validates the user's form input
    @staticmethod
    def validate_album(form):
        is_valid = True
        if len(form['title']) < 2:
            flash('Title must be at least two characters.', 'title')
            is_valid = False
        if len(form['artist']) < 2:
            flash('Artist must be at least two characters.', 'artist')
            is_valid = False
        if len(form['description']) < 2:
            flash('Description must be at least two characters.', 'description')
            is_valid = False
        return is_valid


    @classmethod
    def save(cls, data):
        query = 'INSERT INTO albums (title, artist, description, is_owned) VALUES (%(title)s, %(artist)s, %(description)s, %(is_owned)s);'
        album_id = connectToMySQL(DATABASE).query_db(query, data)
        print(f'Created: <Album {album_id}>')
        return album_id