from pprint import pprint
from flask_app import app, render_template, redirect, request
from flask_app.models.album_model import Album

# redirect user from root route to /albums
@app.get('/')
def redirect_user():
    return redirect('/albums')

# display all albums
@app.get('/albums')
def all_albums():
    albums = Album.find_all()
    print(f'**** FOUND - ALL ALBUMS: ****')
    pprint(albums)
    return render_template('all_albums.html', albums = albums)

# display one album by id
@app.get('/albums/<int:album_id>')
def one_album(album_id):
    data = {
        'id': album_id
    }
    album = Album.find_by_id_with_songs(data)
    print(f'**** FOUND - ALBUM ID: {album.id} ****')
    return render_template('one_album.html', album = album)

# display form to create a album
@app.get('/albums/new')
def new_album():
    return render_template('new_album.html')

# process form and create an album
@app.post('/albums')
def create_album():
    album_id = Album.save(request.form)
    print(f'**** CREATED - ALBUM ID: {album_id} ****')
    return redirect('/albums')

# display form to edit an album by id
@app.get('/albums/<int:album_id>/edit')
def edit_album(album_id):
    data = {
        'id': album_id
    }
    album = Album.find_by_id(data)
    print(f'**** FOUND - ALBUM ID: {album.id} ****')
    return render_template('edit_album.html', album = album)

# process form and update a album by id
@app.post('/albums/<int:album_id>/update')
def update_album(album_id):
    data = {
        'id': album_id,
        'title': request.form['title'],
        'artist': request.form['artist'],
        'description': request.form['description'],
        'is_owned': request.form['is_owned']
    }
    Album.find_by_id_and_update(data)
    print(f'**** UPDATED - ALBUM ID: {album_id} ****')
    return redirect(f'/albums/{album_id}')

# delete one album by id
@app.get('/albums/<int:album_id>/delete')
def delete_album(album_id):
    data = {
        'id': album_id
    }
    Album.find_by_id_and_delete(data)
    print(f'**** DELETED - ALBUM ID: {album_id} ****')
    return redirect('/albums')