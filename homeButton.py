#homebutton op het "bordspel" scherm, als hier op wordt geklikt wordt het beginscherm
#opnieuw weergeven
def setup():
    global logo
    logo = loadImage("logo.png")
    logo.resize(65,65)
    
def draw():
    global logo
    image(logo, 50, 678)
    
# invisible circle for the homebutton indication
    noFill()
    stroke(0)
    strokeWeight(2)
    ellipse(82, 710, 64, 64)
    
    # making the button light up when the mouse hovers over it
    
    if 49 < mouseX < 115 and 679 < mouseY < 745:
        noFill()
        stroke(255, 220)
        strokeWeight(2.5)
        ellipse(82, 710, 66, 66)
