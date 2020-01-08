#logo op het beginscherm
def setup():
    global logo
    logo = loadImage("Images/logo.png")
    logo.resize(200,200)
    frameRate(60)
    
def draw():
    global logo
    image(logo, 272, 60)
