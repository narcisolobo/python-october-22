from pprint import pprint
from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap5
import requests
app = Flask(__name__)
app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'superhero'
bstrap = Bootstrap5(app)

# variables
resources = ['people', 'planets']
BASE_URL = 'https://swapi.dev/api/'

@app.get('/')
def redirect_user():
    return redirect('/swapi')

@app.get('/swapi')
def swapi():
    return render_template('swapi.html', resources = resources)

@app.post('/swapi/go')
def swapi_go():
    resource = request.form['resource']
    res_id = request.form['res_id']
    return redirect(f'/swapi/{resource}/{res_id}')

@app.get('/swapi/people/<int:res_id>')
def swapi_people(res_id):
    response = requests.get(f'{BASE_URL}/people/{res_id}')
    person = response.json()
    pprint(person)
    return render_template('people.html', resources = resources, person = person)

@app.get('/swapi/planets/<int:res_id>')
def swapi_planets(res_id):
    return render_template('planets.html', resources = resources)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5001)