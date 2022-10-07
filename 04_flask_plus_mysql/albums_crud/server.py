from pprint import pprint
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
from album_model import Album

# find all albums
@app.get('/albums')
def index():
    albums = Album.find_all()
    print('ALBUMS IN SERVER.PY')
    pprint(albums)
    return render_template('index.html', albums = albums)

# find one album by id
@app.get('/albums/<int:album_id>')
def find_by_id(album_id):
    data = {
        'id': album_id
    }

    album = Album.find_one(data)
    return render_template('display_album.html', album = album)

# display form to create album
@app.get('/albums/new')
def new_album():
    return render_template('new_album.html')

# create an album
@app.post('/albums')
def create_album():
    data = {
        'title': request.form['title'],
        'artist': request.form['artist'],
        'description': request.form['description']
    }
    album_id = Album.save(data)
    print(f'CREATED ALBUM WITH ID: {album_id}')
    return redirect('/albums')

# display form to edit album
@app.get('/albums/<int:album_id>/edit')
def edit_album(album_id):
    data = {
        'id': album_id
    }

    album = Album.find_one(data)
    return render_template('edit_album.html', album = album)

@app.post('/albums/<int:album_id>/update')
def update_album(album_id):
    data = {
        'title': request.form['title'],
        'artist': request.form['artist'],
        'description': request.form['description']
    }
    Album.update(data)
    return redirect(f'/albums/{album_id}')

# delete route
@app.get('/albums/<int:album_id>/delete')
def delete_album(album_id):
    data = {
        'id': album_id
    }
    Album.delete(data)
    return redirect('/albums')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5001)