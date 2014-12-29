from app import app
from flask import render_template, request, url_for
import os, os.path, base64

# Index
@app.route("/", methods=['GET', 'POST'])
def index():        
    
    # Our list of fonts. 
    # These fonts have to be TTF!!
    if len([font.rstrip('.ttf') for font in os.listdir('app/static/fonts') if font.endswith('.ttf')]) > 0:
        fonts = [font.rstrip('.ttf') for font in os.listdir('app/static/fonts') if font.endswith('.ttf')]
    else:
        return "FATAL ERROR: NO FONTS FOUND."
    
    # Check to see if there are any logo files.
    # Logo files must be stored as .png files in app/static/logos
    if len([file for file in os.listdir('app/static/logos/') if os.path.isfile(name)]) > 0:
        logos = [logos.rstrip('.png') for file in os.listdir('app/static/logos') if font.endswith('.png')]
    else: 
        logos = False
    
    return render_template('index.html', fonts = fonts, logos = logos)
    
@app.route("/create_image", methods=['POST', 'GET'])
def create_image():
    from functions import create_image, TextLengthError, NoTextError
    try:
        # create_image function from functions.py, pass it the entire request form object.
        # This function creates our image for us
        create_image(request.form)
    
        # We need to open the image back up so that it can be encoded
        imgfile = open('app/static/quote.PNG')
    
        # Encode it as base64 for use in the template (cache issue resolved)
        imagesrc = "data:image/png;base64, " + base64.b64encode(imgfile.read())
        
        return imagesrc
    except TextLengthError as e:
        return e.value, 406
    except NoTextError as e:
        return e.value, 406