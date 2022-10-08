from pprint import pprint
from flask_app import app, render_template, redirect, request, session
from flask_app.models.album_model import Album
from flask_app.models.user_model import User

# display all albums
@app.get('/albums')
def all_albums():
    if not 'user_id' in session:
        return redirect('/users/login_reg')
    albums = Album.find_all_with_creators()
    print(f'**** FOUND - ALL ALBUMS: ****')
    pprint(albums)
    data = {
        'id': session['user_id']
    }
    user = User.find_by_id(data)
    return render_template('all_albums.html', albums = albums, user = user)

# display one album by id
@app.get('/albums/<int:album_id>')
def one_album(album_id):
    if not 'user_id' in session:
        return redirect('/users/login_reg')
    data = {
        'id': album_id
    }
    album = Album.find_by_id_with_creator(data)
    print(f'**** FOUND - ALBUM ID: {album.id} ****')
    return render_template('one_album.html', album = album)

# display form to create an album
@app.get('/albums/new')
def new_album():
    if not 'user_id' in session:
        return redirect('/users/login_reg')
    return render_template('new_album.html')

# process form and create an album
@app.post('/albums')
def create_album():
    if not Album.validate_album_form(request.form):
        return redirect('/albums/new')
    album_id = Album.save(request.form)
    print(f'**** CREATED - ALBUM ID: {album_id} ****')
    return redirect('/albums')

# display form to edit an album by id
@app.get('/albums/<int:album_id>/edit')
def edit_album(album_id):
    if not 'user_id' in session:
        return redirect('/users/login_reg')
    data = {
        'id': album_id
    }
    album = Album.find_by_id(data)
    print(f'**** FOUND - ALBUM ID: {album.id} ****')
    return render_template('edit_album.html', album = album)

# process form and update an album by id
@app.post('/albums/<int:album_id>/update')
def update_album(album_id):
    Album.find_by_id_and_update(request.form)
    print(f'**** UPDATED - ALBUM ID: {album_id} ****')
    return redirect(f'/albums/{album_id}')

# delete one album by id
@app.get('/albums/<int:album_id>/delete')
def delete_album(album_id):
    if not 'user_id' in session:
        return redirect('/users/login_reg')
    data = {
        'id': album_id
    }
    Album.find_by_id_and_delete(data)
    print(f'**** DELETED - ALBUM ID: {album_id} ****')
    return redirect('/albums')