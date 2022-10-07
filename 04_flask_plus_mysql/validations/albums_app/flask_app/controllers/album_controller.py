from flask_app import app, render_template, redirect, request
from flask_app.models.album_model import Album

# redirect the user to the form
@app.get('/')
def redirect_to_form():
    return redirect('/albums/new')

# display form to create an album
@app.get('/albums/new')
def new_album():
    return render_template('new_album.html')

@app.post('/albums')
def create_album():
    if not Album.validate_album(request.form):
        return redirect('/albums/new')