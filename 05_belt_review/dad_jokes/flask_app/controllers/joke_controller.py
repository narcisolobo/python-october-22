from flask_app import app, render_template, redirect, request, session
from flask_app.models.dad_model import Dad
from flask_app.models.joke_model import Joke

# display all jokes
@app.get('/jokes')
def all_jokes():
    if 'dad_id' not in session:
        return redirect('/dads/login_reg')
    data = {
        'id': session['dad_id']
    }
    dad = Dad.find_by_id(data)
    jokes = Joke.find_all()
    return render_template('all_jokes.html', dad = dad, jokes = jokes)

# display form to create joke
@app.get('/jokes/new')
def new_joke():
    if 'dad_id' not in session:
        return redirect('/dads/login_reg')
    return render_template('new_joke.html')

# process form and create joke
@app.post('/jokes')
def create_joke():
    if not Joke.validate_joke(request.form):
        return redirect('/jokes/new')
    Joke.save(request.form)
    return redirect('/jokes')

# display one joke
@app.get('/jokes/<int:joke_id>')
def one_joke(joke_id):
    if 'dad_id' not in session:
        return redirect('/dads/login_reg')
    data = {
        'id': joke_id
    }
    joke = Joke.find_by_id_with_creator(data)
    return render_template('one_joke.html', joke = joke)

# display form to edit joke
@app.get('/jokes/<int:joke_id>/edit')
def edit_joke(joke_id):
    if 'dad_id' not in session:
        return redirect('/dads/login_reg')
    data = {
        'id': joke_id
    }
    joke = Joke.find_by_id_with_creator(data)
    return render_template('edit_joke.html', joke = joke)

@app.post('/jokes/<int:joke_id>/update')
def update_joke(joke_id):
    if not Joke.validate_joke(request.form):
        return redirect(f'/jokes/{joke_id}/edit')
    Joke.find_by_id_and_update(request.form)
    return redirect(f'/jokes/{joke_id}')

@app.get('/jokes/<int:joke_id>/delete')
def delete_joke(joke_id):
    if 'dad_id' not in session:
        return redirect('/dads/login_reg')
    data = {
        'id': joke_id
    }
    Joke.find_by_id_and_delete(data)
    return redirect('/jokes')