from app import app
from flask import render_template

# Index
@app.route("/")
def index():
    fonts = ('Arial', 'Courier New', 'Verdana', 'Times New Roman')
    return render_template('index.html', fonts = fonts)