from PIL import Image, ImageDraw, ImageFont

class Visualise(object): 
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self, weather_statements):
        message = ""
        for statement in weather_statements: 
            message = message + " \n " + str(statement)

        font = ImageFont.truetype("/Library/fonts/Arial.ttf", size=20)

        img = Image.new('RGB', (self.width, self.height), color='white')
        
        imgDraw = ImageDraw.Draw(img)

        textWidth, textHeight = imgDraw.textsize(message, font=font)
        xText = (self.width - textWidth) / 2
        yText = (self.height - textHeight) / 2

        imgDraw.text((xText, yText), message, font=font, fill=(0, 0, 0))

        img.save('weather.png')
    
    def display(self):

        # convert image 
        img = Image.open("/home/pi/weather.png")

        pal_img = Image.new("P", (1, 1))
        pal_img.putpalette((255, 255, 255, 0, 0, 0, 255, 0, 0) + (0, 0, 0) * 252)

        img = img.convert("RGB").quantize(palette=pal_img)

        # display image
        inky_display.set_image(img)
        inky_display.show()
        

        