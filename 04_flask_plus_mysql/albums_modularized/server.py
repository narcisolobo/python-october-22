from flask_app import app

# Remember to import controllers
from flask_app.controllers import album_controller

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5001)