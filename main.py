from gfxhat import lcd,  fonts
from PIL import Image, ImageFont, ImageDraw
from click import getchar

def clearScreen(lcd):
    lcd.clear()
    lcd.show()

def displayText(text,lcd,x,y):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show() 

keyboard = getchar ()
while running == True :
    if keyboard = '\x1b[A':
        lcd.set_pixel(x, y, 1)
    
    elif keyboard = '\x1b[B':
        lcd.set_pixel(x, y, 1)
    
    elif keyboard = '\x1b[C':
        lcd.set_pixel(x, y, 1)

    elif keyboard = '\x1b[D':
        lcd.set_pixel(x, y, 1)

    elif keyboard = "s":
        lcd.set_pixel(x, y, 1)

    else keyboard = 'q':
        running == False