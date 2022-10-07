from pprint import pprint
from flask_app import app, render_template, redirect, request
from flask_app.models.make_model import Make

# redirect the user to /makes
@app.get('/')
def redirect_user():
    return redirect('/makes')

# display all makes
@app.get('/makes')
def all_makes():
    makes = Make.find_all()
    print(f'**** FOUND - ALL MAKES: ****')
    pprint(makes)
    return render_template('all_makes.html', makes = makes)

# display one make by id
@app.get('/makes/<int:make_id>')
def one_make(make_id):
    print('*'*20 + 'IN THE ONE_MAKE FUNCTION')
    data = {
        'id': make_id
    }
    make = Make.find_by_id_with_models(data)
    print(f'**** FOUND - MAKE ID: {make.id} ****')
    return render_template('one_make.html', make = make)

# display form to create a make
@app.get('/makes/new')
def new_make():
    return render_template('new_make.html')

# process form and create a make
@app.post('/makes')
def create_make():
    make_id = Make.save(request.form)
    print(f'**** CREATED - MAKE ID: {make_id} ****')
    return redirect('/makes')

# display form to edit a make by id
@app.get('/makes/<int:make_id>/edit')
def edit_make(make_id):
    data = {
        'id': make_id
    }
    make = Make.find_by_id(data)
    print(f'**** FOUND - MAKE ID: {make.id} ****')
    return render_template('edit_make.html', make = make)

# process form and update a make by id
@app.post('/makes/<int:make_id>/update')
def update_make(make_id):
    Make.find_by_id_and_update(request.form)
    print(f'**** UPDATED - MAKE ID: {make_id} ****')
    return redirect(f'/makes/{make_id}')

# delete one make by id
@app.get('/makes/<int:make_id>/delete')
def delete_make(make_id):
    data = {
        'id': make_id
    }
    Make.find_by_id_and_delete(data)
    print(f'**** DELETED - MAKE ID: {make_id} ****')
    return redirect('/makes')