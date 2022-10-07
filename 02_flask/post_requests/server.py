from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'dfe8b056414fa496019f1b98878e8a1dd6f774f3b1a187692c0c6c08281578eb'

@app.route('/')
def redirect_user():
    return redirect('/users/register')

@app.route('/users/register')
def index():
    return render_template('index.html')

@app.post('/users')
def insert_user():
    session['username'] = request.form['username']
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    session['muppet'] = request.form['muppet']
    return redirect('/users')

@app.get('/users')
def results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5001)