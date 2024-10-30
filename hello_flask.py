from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
Bootstrap5()  # Initialize Bootstrap5 directly with the app instance

@app.route('/')
def index():
    return render_template('template.html')

if __name__ == '__main__':
    app.run(debug=True)

