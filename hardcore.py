def setup():
    #laad de uitleg van rushhour en de template achtergrond in en resized deze naar het juiste formaat.
    global img, template
    img = loadImage("Images/hardcore.png")
    template = loadImage("Images/template.jpg")
    img.resize(600,600)
    template.resize(750,750)
    
def draw():
    global img, template
    image(template, 0, 0)
    image(img, 75,30)
    
    #tekent een outline (rechthoek) om de preset heen
    noFill()
    stroke(0)
    strokeWeight(3)
    rect(74,29,602,602)
