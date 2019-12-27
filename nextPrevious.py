#De knoppen die in de handleiding worden gebruikt
import handleiding
def setup():
    global logo
    logo = loadImage("Images/logo.png")
    logo.resize(65,65)
    
def draw():
    nextButton()
    previousButton()
    homeButton()
    handleiding.navButton()

def nextButton():
    noFill()
    stroke(0, 150)
    strokeWeight(5)
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
    else:
        return False
        
        
def previousButton():
    noFill()
    stroke(0, 150)
    strokeWeight(5)
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
        
    else:
        return False
        
def homeButton():
    global logo
    image(logo, 343, 668)
    
# invisible circle for the homebutton indication
    noFill()
    stroke(0)
    strokeWeight(2)
    ellipse(375, 700, 64, 64)
    
    textSize(20)
    fill(0)
    text("Hoofdscherm:", 200, 705)
    
# making the button light up when the mouse hovers over it
    
    if 342 < mouseX < 406 and 667 < mouseY < 735:
        noFill()
        strokeWeight(2.5)
        stroke(255, 220)
        ellipse(375, 700, 66, 66)
        
        textSize(20)
        fill(255)
        text("Hoofdscherm:", 200, 705)
    else: 
        return False

def backgroundTint():
    strokeWeight(0)
    fill(0,0,0,128)
    rect(0, 0, 750, 750)
    
