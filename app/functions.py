# Create image function -- pass the entire request form object to it.
class TextLengthError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
        
class NoTextError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def create_image(request):
    
    from PIL import Image, ImageDraw, ImageFont
    
    if len(request['quote']) > 255:
        raise TextLengthError("The length of a quote cannot exceed 255 characters.")
    
    if not request['quote']:
        raise NoTextError("Your quote cannot be empty.")
    
    # Set our font and image sizes
    if request['size'] == "small":
        size = (300, 200)
        attrposition = (10, 180)
        quotemarkposition = (250, 120)
        quotemarksize = 125
        fontsize = 15
    elif request['size'] == "medium":
        size = (600, 400)
        attrposition = (10, 350)
        quotemarkposition = (400, 275)
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
        quotemarkposition = (1975, 1100)
        quotemarksize = 1000
        fontsize = 120
    
    # Add new lines so that text doesn't overflow. Ugly for now.
    import textwrap
    quote = textwrap.wrap(request['quote'], 24)
    
    # Make our font object for use with the quote and attribution text
    font = ImageFont.truetype('app/static/fonts/'+request['font']+'.ttf', fontsize)
    
    # Create our instance of the image class from Pillow
    image = Image.new('RGB', size, (255, 255, 255, 0))
    
    # Create our draw object
    draw = ImageDraw.Draw(image)
    
    # Positioned in the top left for now
    position = [10, 10]
    
    for line in quote:
        # Draw the text
        draw.text(position, line, font=font, fill=(0, 0, 0, 255))
        position[1] += fontsize
        
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
    
    return quote