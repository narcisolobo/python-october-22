from flask import Flask, render_template
from python_cohort import cohort
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', students = cohort)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5001)