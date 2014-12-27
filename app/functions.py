# Create image function -- pass the entire request form object to it.
def create_image(request):
    from PIL import Image, ImageDraw, ImageFont
    
    
    # Set our font and image sizes
    if request['size'] == "small":
        size = (300, 200)
        attrposition = (10, 150)
        quotemarkposition = (200, 125)
        quotemarksize = 125
        fontsize = 15
    elif request['size'] == "medium":
        size = (600, 400)
        attrposition = (10, 350)
        quotemarkposition = (400, 300)
        quotemarksize = 250
        fontsize = 30
    elif request['size'] == "large":
        size = (1200, 800)
        attrposition = (10, 625)
        quotemarkposition = (1000, 525)
        quotemarksize = 500
        fontsize = 60
    elif request['size'] == "xlarge":
        size = (2400, 1600)
        attrposition = (10, 1425)
        quotemarkposition = (1975, 1300)
        quotemarksize = 1000
        fontsize = 120
        
    # Make our font object for use with the quote and attribution text
    font = ImageFont.truetype('app/static/fonts/'+request['font']+'.ttf', fontsize)
    
    # Create our instance of the image class from Pillow
    image = Image.new('RGB', size, (255, 255, 255, 0))
    
    # Create our draw object
    draw = ImageDraw.Draw(image)
    
    # Positioned in the top left for now
    position = (10, 10)
    
    # Draw the text
    draw.text(position, request['quote'], font=font, fill=(0, 0, 0, 255))
        
    if request['attribution'] != "":
        # Put the quote attribution on the image
        draw.text(attrposition, "- " +request['attribution'], font = font, fill=(0, 0, 0, 255))
    
    if request['quotemarks'] == "True":
        # Just a default position now, can make it do something more advanced later (should appear in bottom right hand corner)
        font = ImageFont.truetype('app/static/fonts/'+request['font']+'.ttf', quotemarksize)
        draw.text(quotemarkposition, '"', font=font, fill=(0, 0, 0, 255))
    
    # Bye bye draw instance
    del draw
    
    # Save our image
    image.save('app/static/quote.PNG')