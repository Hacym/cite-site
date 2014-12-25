from app import app
from flask import render_template, request

# Index
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Create our variables from our form
        font = request.form['font']
        fontcolor = request.form['fontcolor']
        bgcolor = request.form['bgcolor']
        quote = request.form['quote']
        squotemarks = request.form['quotemarks']
        
        # A return to tell our template to display the image
        display = True
    else:
        display = False
    
    fonts = ('Arial', 'Courier New', 'Verdana', 'Times New Roman')
    return render_template('index.html', fonts = fonts, display = display)