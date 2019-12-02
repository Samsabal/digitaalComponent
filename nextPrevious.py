def setup():
    global logo
    logo = loadImage("Images/logo.png")
    logo.resize(65,65)
    
def draw():
    #haal deze 3 functies weg uit de draw() als je de if-statement gaat gebruiken
    homeButton()
    previousButton()
    homeButton()
    
    #if statement om de juiste knoppen te laten zien op de juiste pagina's:
    # if page == "1":
    #     nextButton()
    #     homeButton()
    # elif page == "x":    #x moet de laatste pagina worden
    #     previousButton()
    #     homeButton()
    # else:
    #     nextButton()
    #     previousButton()
    #     homeButton()

def nextButton():
    noFill()
    stroke(0, 150)
    rect(656, 678, 75, 40)
    
    textSize(26)
    fill(0)
    text("NEXT", 660, 707)
    
    #making the button light up when you hover above it
    if 656 < mouseX < 731 and 678 < mouseY < 718:
        noFill()
        stroke(255, 220)
        rect(656, 678, 75, 40)
        fill(255)
        textSize(26)
        text("NEXT", 660, 707)
        
        
def previousButton():
    noFill()
    stroke(0, 150)
    rect(19, 678, 75, 40)
    
    textSize(26)
    fill(0)
    text("PREV", 25, 707)
    
    #making the button light up when you hover above it
    if 19 < mouseX < 94 and 678 < mouseY < 718:
        noFill()
        stroke(255, 220)
        rect(19, 678, 75, 40)
        fill(255)
        textSize(26)
        text("PREV", 25, 707)
        
def homeButton():
    global logo
    image(logo, 343, 668)
    
# invisible circle for the homebutton indication
    noFill()
    stroke(0)
    strokeWeight(2)
    ellipse(375, 700, 64, 64)
    
# making the button light up when the mouse hovers over it
    
    if 342 < mouseX < 406 and 667 < mouseY < 735:
        noFill()
        stroke(255, 220)
        strokeWeight(2.5)
        ellipse(375, 700, 66, 66)
    
