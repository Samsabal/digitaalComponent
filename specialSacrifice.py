def setup():
    #laad de uitleg van rushhour en de template achtergrond in en resized deze naar het juiste formaat.
    global img, template
    img = loadImage("Images/specialSacrifice.png")
    template = loadImage("Images/template.jpg")
    img.resize(450,650)
    template.resize(750,750)
    
def draw():
    global img, template
    image(template, 0, 0)
    image(img, 150,10)
    
    #tekent een outline (rechthoek) om de uitleg heen
    noFill()
    stroke(0)
    strokeWeight(3)
    rect(149, 9, 452, 652)
