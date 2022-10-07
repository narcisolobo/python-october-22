from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'makes_and_models'


class Model:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    def __repr__(self):
        return f'<Model: {self.name}>'

    # create a model
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO models (name, make_id) VALUES (%(name)s, %(make_id)s);'
        model_id = connectToMySQL(DATABASE).query_db(query, data)
        return model_id

    # find all models (no data needed)
    @classmethod
    def find_all(cls):
        query = 'SELECT * from models;'
        results = connectToMySQL(DATABASE).query_db(query)
        models = []
        for result in results:
            models.append(Model(result))
        return models

    # find one model by id
    @classmethod
    def find_by_id(cls, data):
        query = 'SELECT * from models WHERE id = %(id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        model = Model(results[0])
        return model

    # update one model by id
    @classmethod
    def find_by_id_and_update(cls, data):
        query = 'UPDATE models SET name = %(name)s WHERE id = %(id)s;'
        connectToMySQL(DATABASE).query_db(query, data)
        return True

    # delete one model by id
    @classmethod
    def find_by_id_and_delete(cls, data):
        query = 'DELETE FROM models WHERE id = %(id)s;'
        connectToMySQL(DATABASE).query_db(query, data)
        return True
