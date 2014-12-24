from app import app
from flask import render_template

# Index
@app.route("/")
def index():
	return render_template('index.html')