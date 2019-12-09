import template
from nextPrevious import homeButton


def draw():
    template.draw()
    homeButton()
    button1()
    options()
    header()
    
    
    stroke(0)
    strokeWeight(3)
    line(0, 241, 750, 241)

    
def header():
    textSize(35)
    fill(0)
    text("Kies de gamemode die je wilt spelen", 75, 206)
    
    

def options():
    textSize(21)
    fill(0)
    text("- Rush hour", 295, 306)

    

    
def button1():
    noFill()
    stroke(0,150)
    rect(285,280,170,40)
    mouseHover()

    
def mouseHover():
    if 285 < mouseX < 455 and 280 < mouseY < 320:
        noFill()
        stroke(255,220)
        rect(285,280,170,40)
    else:
        return False
