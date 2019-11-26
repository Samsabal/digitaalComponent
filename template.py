#achtergrond van het beginscherm
def setup():
    global img
    img = loadImage("template.jpg")
    img.resize(750,750)
    
def draw():
    global img
    image(img, 0, 0)
    
    
