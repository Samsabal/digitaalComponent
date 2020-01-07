#achtergrond van het beginscherm
def setup():
    global img
    img = loadImage("Images/template.jpg")
    img.resize(750,750)
    frameRate(60)
    
def draw():
    global img
    image(img, 0, 0)
    
    
