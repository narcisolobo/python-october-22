from flask_app import app

# remember to import your controllers
from flask_app.controllers import dad_controller, joke_controller

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5001)