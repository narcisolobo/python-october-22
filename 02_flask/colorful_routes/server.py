from flask import Flask, render_template
app = Flask(__name__)

# Root Route
@app.route('/')
def index():
    return 'Hello world!'

@app.route('/home')
def home():
    return '<h1>Home Page</h1>'

@app.route('/name/<person>')
def say_hello(person):
    return f'<h1>Hello, {person}!</h1>'

@app.route('/name/<person>/<int:num>')
def repeat_name(person, num):
    return f'<h1>Hello, {person}!</h1>' * num

@app.route('/octodex')
def octodex():
    data = {
        'person': 'Guest',
        'num': 1,
        'bgcolor': 'black'
    }
    return render_template('index.html', data = data)

@app.route('/octodex/<person>')
def octodex_person(person):
    data = {
        'person': person,
        'num': 3,
        'bgcolor': 'green'
    }
    return render_template('index.html', data = data)

@app.route('/octodex/<person>/<int:num>')
def octodex_person_repeat(person, num):
    data = {
        'person': person,
        'num': num,
        'bgcolor': 'dodgerblue'
    }
    return render_template('index.html', data = data)

@app.route('/octodex/<person>/<int:num>/<bgcolor>')
def octodex_person_repeat_color(person, num, bgcolor):
    data = {
        'person': person,
        'num': num,
        'bgcolor': bgcolor
    }
    return render_template('index.html', data = data)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5001)