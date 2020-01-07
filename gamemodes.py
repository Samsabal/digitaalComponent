import template
from nextPrevious import homeButton

def draw():
    template.draw()
    homeButton()        
    button1()
    options()
    header()    
    stroke(0)
    strokeWeight(4)
    line(0, 328, 750, 328)
    line(0, 387, 750, 387)
    
def header():
    textSize(35)
    fill(0)
    text("Kies de gamemode die je wilt spelen:", 75, 116)
    text("Of", 370, 370)
    textSize(33)
    text("Kies de spelindeling die je wilt gebruiken:", 47, 456)
    
def options():
    textSize(21)
    fill(0)
    
    #opties van verschillende gamemodes
    text("- Rush Hour", 295, 186)
    text("- Special Sacrifice", 295, 236)
    #opties van verschillende mapindelingen
    text("- Blokkade", 290, 516)
    text("- ", 290, 566)
    

def button1():
    noFill()
    stroke(0,150)
    strokeWeight(3)
    rect(285,160,170,40)
    rect(285,210,170,40)
    rect(280, 490, 180, 40)
    rect(280, 540, 180, 40)
    mouseHover()

def mouseHover():
    if 285 < mouseX < 455 and 160 < mouseY < 200:
        noFill()
        stroke(255,240)
        rect(285,160,170,40)
    elif 285 < mouseX < 455 and 210 < mouseY < 250:
        noFill()
        stroke(255,240)
        rect(285,210,170,40)
    elif 280 < mouseX < 460 and 490 < mouseY < 530:
        noFill()
        stroke(255,240)
        rect(280, 490, 180, 40)
    elif 280 < mouseX < 460 and 540 < mouseY < 580:
        noFill()
        stroke(255,240)
        rect(280, 540, 180, 40)
    else:
        return False
