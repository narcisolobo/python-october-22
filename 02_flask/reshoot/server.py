from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/octodex')

@app.route('/octodex')
def octodex():
    data = {
        'person': 'Guest',
        'num': 1,
        'bgcolor': 'black'
    }
    return render_template('index.html', data = data)

@app.route('/octodex/<person>')
def octodex_name(person):
    data = {
        'person': person,
        'num': 3,
        'bgcolor': 'green'
    }
    return render_template('index.html', data = data)

@app.route('/octodex/<person>/<int:num>')
def octodex_name_num(person, num):
    data = {
        'person': person,
        'num': num,
        'bgcolor': 'rebeccapurple'
    }
    return render_template('index.html', data = data)

@app.route('/octodex/<person>/<int:num>/<bgcolor>')
def octodex_name_num_color(person, num, bgcolor):
    data = {
        'person': person,
        'num': num,
        'bgcolor': bgcolor
    }
    return render_template('index.html', data = data)

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5001)