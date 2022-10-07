from pprint import pprint
from flask_app import app, render_template, redirect, request
from flask_app.models.model_model import Model
from flask_app.models.make_model import Make

# display all models
@app.get('/models')
def all_models():
    models = Model.find_all()
    print(f'**** FOUND - ALL MODELS: ****')
    pprint(models)
    return render_template('all_models.html', models = models)

# display one model by id
@app.get('/models/<int:model_id>')
def one_model(model_id):
    data = {
        'id': model_id
    }
    model = Model.find_by_id(data)
    print(f'**** FOUND - MODEL ID: {model.id} ****')
    return render_template('one_model.html', model = model)

# display form to create a model
@app.get('/models/new')
def new_model():
    makes_from_db = Make.find_all()
    return render_template('new_model.html', makes_for_html = makes_from_db)

# process form and create a model
@app.post('/models')
def create_model():
    model_id = Model.save(request.form)
    print(f'**** CREATED - MODEL ID: {model_id} ****')
    return redirect('/models')

# display form to edit a model by id
@app.get('/models/<int:model_id>/edit')
def edit_model(model_id):
    data = {
        'id': model_id
    }
    model = Model.find_by_id(data)
    print(f'**** FOUND - MODEL ID: {model.id} ****')
    return render_template('edit_model.html', model = model)

# process form and update a model by id
@app.post('/models/<int:model_id>/update')
def update_model(model_id):
    Model.find_by_id_and_update(request.form)
    print(f'**** UPDATED - MODEL ID: {model_id} ****')
    return redirect(f'/models/{model_id}')

# delete one model by id
@app.get('/models/<int:model_id>/delete')
def delete_model(model_id):
    data = {
        'id': model_id
    }
    Model.find_by_id_and_delete(data)
    print(f'**** DELETED - MODEL ID: {model_id} ****')
    return redirect('/models')