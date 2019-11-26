 
def setup():
    global img, img2
    img = loadImage("Images/boardGame.jpg")
    img.resize(600,600)
    img2 = loadImage("Images/template.jpg")
    img2.resize(750,750)
    
def draw():
    #de afbeelding van het spel in het midden van het scherm en de 
    #achtergrond over heel het scherm
    global img, img2
    background(255)
    tint(255, 230)
    image(img2, 0, 0)
    noTint()
    image(img, 75, 30)
    
    noFill()
    stroke(0)
    strokeWeight(3)
    rect(1, 673, 747, 75)
    strokeWeight(5)
    rect(74, 29, 600, 600)

    
    
