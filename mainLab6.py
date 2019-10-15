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
    
def etchASketch():
    keyboard = getchar()
    while running == True :
        lcd.set_pixel(x=64, y=31, 1)
        displayText("Etch a Sketch",lcd,10,10)
        lcd.show()
        if keyboard == '\x1b[A':
           if (y == 0) and (x >= 0) and (x <= 127):
                lcd.set_pixel(x, y=63, 1)
                lcd.show()
           else :
                lcd.set_pixel(x, y-1, 1)
                lcd.show()
        elif keyboard == '\x1b[B':
            if (y == 63) and (x >= 0) and (x <= 127): 
                y = 0
                lcd.set_pixel(x, y, 1)
                lcd.show()
            else :
                y+ = 1
                lcd.set_pixel(x, y, 1)
                lcd.show()                
        elif keyboard == '\x1b[C':
            if (x == 127) and (y >= 0) and (y <= 63): 
                x=0 
                lcd.set_pixel(x, y, 1)
                lcd.show()
            else :
                x+ = 1
                lcd.set_pixel(x, y, 1)
                lcd.show()
        elif keyboard == '\x1b[D':
            if (x == 0) and (y >= 0) and (y <= 63): 
                x = 127
                lcd.set_pixel(x, y, 1)
                lcd.show()
            else :
                x- = 1
                lcd.set_pixel(x, y, 1)
                lcd.show()
        elif keyboard == "s":
            clearScreen(lcd)
            displayText("Etch a Sketch",lcd,10,10)
            x = 64
            y = 31
            lcd.set_pixel(x, y, 1)
            lcd.show()
        elif keyboard == 'q':
            running = False
        else:
            displayText("PLease use only the following keys: *1.Arrow keys to change direction. *2. s to start again a new drawing. *3. q to quit. Thanks.",lcd,2,2)
            lcd.show()
  
def displayObject(obj,x,y):
    objLength=0
    while objLength <= len(obj) -1:
        tupleLength=0
        while tupleLength <= len(obj[objLength]) -1 :
            displ = obj[objlength] [tuplelength]
            lcd.set_pixel(x,y,displ)
            x +=1
            tuplelength +=1
        y +=1
        objlength +=1




