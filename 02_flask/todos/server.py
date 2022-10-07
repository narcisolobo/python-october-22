from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = '74e46f7d7643cccbee4f37092f23c35178acea6e37995c89c1c3141ec9f6f931'
from uuid import uuid4

# display form to set username
@app.get('/')
def index():
    return render_template('index.html')

# handle the username form
@app.post('/users')
def set_username():
    session['username'] = request.form['username']
    return redirect('/todos/new')

# display a form to create a todo
@app.get('/todos/new')
def new_todo():
    return render_template('new_todo.html')

# handle the new todo form
# and create a todo
@app.post('/todos')
def create_todo():
    new_todo = {
        'id': str(uuid4()),
        'title': request.form['title'],
        'description': request.form['description'],
        'is_complete': False
    }
    if 'todos' not in session:
        session['todos'] = []
    todos = list(session['todos'])
    todos.append(new_todo)
    session['todos'] = todos
    return redirect('/todos')

# display all todos
@app.get('/todos')
def all_todos():
    return render_template('all_todos.html')

@app.get('/todos/<todo_id>')
def display_todo(todo_id):
    found_todo = None
    for todo in session['todos']:
        if todo['id'] == todo_id:
            found_todo = todo
    return render_template('display_todo.html', todo = found_todo)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5001)