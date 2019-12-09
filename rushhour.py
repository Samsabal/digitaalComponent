
def setup():
    global img, template
    img = loadImage("Images/rushhour.png")
    template = loadImage("Images/template.jpg")
    img.resize(450,650)
    template.resize(750,750)
    
    
def draw():
    image(template, 0, 0)
    image(img, 150,10)
    
    noFill()
    stroke(0)
    strokeWeight(3)
    rect(149, 9, 452, 652)
    
