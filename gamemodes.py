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
    text("- Rush Hour", 110, 196)
    textSize(18)
    text("- Special Sacrifice", 480, 196)
    textSize(21)
    #opties van verschillende mapindelingen
    text("- Blokkade", 110, 546)
    text("- Hardcore", 480, 546)
    

def button1():
    noFill()
    stroke(0,150)
    rect(100,170,170,40)
    rect(470,170,170,40)
    rect(100, 520, 170, 40)
    rect(470, 520, 170, 40)
    mouseHover()

def mouseHover():
    if 100 < mouseX < 280 and 170 < mouseY < 210:
        noFill()
        stroke(255,240)
        rect(100,170,170,40)
    elif 470 < mouseX < 650 and 170 < mouseY < 210:
        noFill()
        stroke(255,240)
        rect(470,170,170,40)
    elif 100 < mouseX < 280 and 520 < mouseY < 560:
        noFill()
        stroke(255,240)
        rect(100, 520, 170, 40)
    elif 470 < mouseX < 650 and 520 < mouseY < 560:
        noFill()
        stroke(255,240)
        rect(470, 520, 170, 40)
    else:
        return False
