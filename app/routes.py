from app import app
from flask import render_template, request, send_file, url_for
from PIL import Image, ImageDraw, ImageFont
import glob, os

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
        
        position = (10, 10) # Positioned in the top left for now
        
        # Draw the text
        draw.text(position, quote, font=font, fill=(0, 0, 0, 255))
        
        # Bye bye draw instance
        del draw
        
        # Save our image
        image.save('app/static/quote.PNG')
        
        # A return to tell our template to display the image
        display = True
    else:
        # Don't display
        display = False
    
    # Our list of fonts. 
    fonts = []
    
    # Loop over all of the fonts in our fonts folder and add it to our fonts list
    # These fonts have to be TTF!!
    for font in glob.glob('app/static/fonts/*.ttf'):
        # Appends just the name of the file to the list
        # os.path.basename removes the path to the file
        # [:-4] removes the .ttf ext
        fonts.append(os.path.basename(font[:-4]))
        
    
    return render_template('index.html', fonts = fonts, display = display)