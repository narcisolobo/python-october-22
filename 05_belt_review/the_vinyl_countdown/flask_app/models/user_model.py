from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash
import re # regular expression REGEX

DATABASE = 'vinyl_countdown'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    def __repr__(self):
        return f'<User: {self.username}>'
    
    @staticmethod
    def validate_registration(form):
        is_valid = True
        if len(form['username']) < 2:
            flash('Username must be at least two characters', 'username')
            is_valid = False
        if not EMAIL_REGEX.match(form['email']):
            flash('Please enter a valid email', 'email')
            is_valid = False
        if len(form['password']) < 8:
            flash('Password must be at least eight characters', 'password')
            is_valid = False
        else:
            if form['password'] != form['confirm_password']:
                flash('Passwords must match', 'confirm_password')
                is_valid = False
        return is_valid

    @staticmethod
    def validate_login(form):
        is_valid = True
        if not EMAIL_REGEX.match(form['email']):
            flash('Please enter a valid email', 'log_email')
            is_valid = False
        if len(form['password']) < 8:
            flash('Password must be at least eight characters', 'log_password')
            is_valid = False
        return is_valid
    
    @classmethod
    def find_by_email(cls, data):
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) > 0:
            return User(results[0])
        return None
    
    @classmethod
    def find_by_id(cls, data):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) > 0:
            return User(results[0])
        return None
    
    @classmethod
    def save(cls, data):
        query = 'INSERT into users (username, email, password) VALUES (%(username)s, %(email)s, %(password)s);'
        user_id = connectToMySQL(DATABASE).query_db(query, data)
        return user_id