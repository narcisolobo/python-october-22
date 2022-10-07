from flask_app import app, render_template, redirect, request
from flask_app.models.song_model import Song

# display one song by id
@app.get('/songs/<int:song_id>')
def one_song(song_id):
    data = {
        'id': song_id
    }
    song = Song.find_by_id(data)
    print(f'**** FOUND - SONG ID: {song.id} ****')
    return render_template('one_song.html', song = song)

# process form and create a song
@app.post('/songs/<int:album_id>')
def create_song(album_id):
    song_id = Song.save(request.form)
    print(f'**** CREATED - SONG ID: {song_id} ****')
    return redirect(f'/albums/{album_id}')

# display form to edit a song by id
@app.get('/songs/<int:song_id>/edit')
def edit_song(song_id):
    data = {
        'id': song_id
    }
    song = Song.find_by_id(data)
    print(f'**** FOUND - SONG ID: {song.id} ****')
    return render_template('edit_song.html', song = song)

# process form and update a song by id
@app.post('/songs/<int:song_id>/update')
def update_song(song_id):
    data = {
        'id': song_id,
        'field1': request.form['field1'],
        'field2': request.form['field2'],
        'field3': request.form['field3']
    }
    Song.find_by_id_and_update(data)
    print(f'**** UPDATED - SONG ID: {song_id} ****')
    return redirect(f'/songs/{song_id}')

# delete one song by id
@app.get('/songs/<int:song_id>/delete')
def delete_song(song_id):
    data = {
        'id': song_id
    }
    Song.find_by_id_and_delete(data)
    print(f'**** DELETED - SONG ID: {song_id} ****')
    return redirect('/songs')