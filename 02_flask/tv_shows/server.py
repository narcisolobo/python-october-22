# import Flask and necessary functions and objects
from flask import Flask, render_template, redirect, request
# instantiate flask app
app = Flask(__name__)
# import our Show class
from show import Show

# let's create an empty list to hold our shows
shows = []

# this route just redirects the user
# from the root route to the form
@app.get('/')
def redirect_user():
    return redirect('/shows/new')

# this route displays a form for the user
# to add a new show
@app.get('/shows/new')
def new_show():
    return render_template('new_show.html')

# this route processes the form and
# instantiates a new Show object
# using the form's values
@app.post('/shows')
def create_show():
    # our show's id is the length of the shows list + 1
    id = len(shows) + 1

    # let's grab all the form values out of the
    # post request and create variables
    title = request.form['title']
    genre = request.form['genre']
    description = request.form['description']
    # convert rating from string to int
    rating = int(request.form['rating'])
    release_date = request.form['release_date']

    # instantiate a new Show object using
    # above variables
    new_show = Show(id, title, genre, description, rating, release_date)

    # add the new_show to the shows list
    shows.append(new_show)

    # redirect on a post request!
    # we'll send the user to the /shows
    # get route
    return redirect('/shows')

# this route displays all the shows
# it looks like the same route as above,
# but this one uses get, not post
@app.get('/shows')
def all_shows():
    # send our shows list as a template variable
    return render_template('all_shows.html', shows = shows)

@app.get('/shows/<int:show_id>')
def display_show(show_id):
    # get the correct show from the shows list
    # based off the id in the route
    show = shows[show_id - 1]
    # send the show as a template variable
    return render_template('display_show.html', show = show)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5001)