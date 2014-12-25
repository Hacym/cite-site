from app import app
from flask import render_template, request, url_for
from PIL import Image, ImageDraw, ImageFont
import os, base64

# Index
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Create our variables from our form
        font = ImageFont.truetype('app/static/fonts/'+request.form['font']+'.ttf', 15)
        
        # Breaking out our colors into RGB to use in Pillow --
        # this is done with Javascript on the template side
        fontcolor_r = request.form["font-r"]
        fontcolor_g = request.form["font-g"]
        fontcolor_b = request.form["font-b"]
        
        bgcolor_r = request.form["bg-r"]
        bgcolor_g = request.form["bg-g"]
        bgcolor_b = request.form["bg-b"]
        
        quote = request.form['quote']
        quotemarks = request.form['quotemarks']
        
        # For now, our size is gonna be nice and simple: 300px wide, 200px tall
        # Eventually we can make it do more advanced stuff, like custom image sizes
        size = (300, 200)
        image = Image.new('RGB', size, (255, 255, 255, 0)) # Create our instance of the image class from Pillow
        
        # Create our draw object
        draw = ImageDraw.Draw(image)
        
        # Positioned in the top left for now
        position = (10, 10)
        
        # Draw the text
        draw.text(position, quote, font=font, fill=(0, 0, 0, 255))
        
        # Bye bye draw instance
        del draw
        
        # Save our image
        image.save('app/static/quote.PNG')
        
        # Open it back up...
        imgfile = open('app/static/quote.PNG')
        
        # Encode it as base64 for use in the template (cache issue resolved)
        imagesrc = base64.b64encode(imgfile.read())
        
        # A return to tell our template to display the image
        display = True
    else:
        # Don't display
        display = False
        imagesrc = False
    
    # Our list of fonts. 
    # These fonts have to be TTF!!
    fonts = [font.rstrip('.ttf') for font in os.listdir('app/static/fonts') if font.endswith('.ttf')]
        
    
    return render_template('index.html', fonts = fonts, display = display, imagesrc = imagesrc)