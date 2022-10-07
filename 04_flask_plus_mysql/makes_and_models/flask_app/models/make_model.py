from pprint import pprint
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.model_model import Model

DATABASE = 'makes_and_models'


class Make:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.models = []
    
    def __repr__(self):
        return f'<Make: {self.name}>'

    # create a make
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO makes (name) VALUES (%(name)s);'
        make_id = connectToMySQL(DATABASE).query_db(query, data)
        return make_id

    # find all makes (no data needed)
    @classmethod
    def find_all(cls):
        query = 'SELECT * from makes;'
        results = connectToMySQL(DATABASE).query_db(query)
        makes = []
        for result in results:
            makes.append(Make(result))
        return makes

    # find one make by id
    @classmethod
    def find_by_id(cls, data):
        query = 'SELECT * from makes WHERE id = %(id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        make = Make(results[0])
        return make

    # find one make by id with models
    @classmethod
    def find_by_id_with_models(cls, data):
        query = 'SELECT * from makes LEFT JOIN models ON makes.id = models.make_id WHERE makes.id = %(id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        pprint(results)
        make = Make(results[0])
        if results[0]['make_id']:
            for result in results:
                data = {
                    'id': result['models.id'],
                    'name': result['models.name'],
                    'created_at': result['created_at'],
                    'updated_at': result['updated_at'],
                    'make_id': result['make_id']
                }
                make.models.append(Model(data))
        return make

    # update one make by id
    @classmethod
    def find_by_id_and_update(cls, data):
        query = 'UPDATE makes SET name = %(name)s WHERE id = %(id)s;'
        connectToMySQL(DATABASE).query_db(query, data)
        return True

    # delete one make by id
    @classmethod
    def find_by_id_and_delete(cls, data):
        query = 'DELETE FROM makes WHERE id = %(id)s;'
        connectToMySQL(DATABASE).query_db(query, data)
        return True
