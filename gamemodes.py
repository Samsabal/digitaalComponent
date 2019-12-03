import template
from nextPrevious import homeButton


def draw():
    template.draw()
    homeButton()
    button1()
    button2()
    button3()
    button4()
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
    text("- No Buildings", 295, 356)
    textSize(20)
    text("- Wounded only", 295, 406)
    textSize(21)
    text("- Killmode", 295, 456)
    

    
def button1():
    noFill()
    stroke(0,150)
    rect(285,280,170,40)
    mouseHover()
    
def button2():
    noFill()
    stroke(0,150)
    rect(285,330,170,40)
    mouseHover()

def button3():
    noFill()
    stroke(0,150)
    rect(285,380,170,40)
    mouseHover()
    
def button4():
    noFill()
    stroke(0,150)
    rect(285,430,170,40)
    mouseHover()
    
def mouseHover():
    if 285 < mouseX < 455 and 280 < mouseY < 320:
        noFill()
        stroke(255,220)
        rect(285,280,170,40)
    elif 285 < mouseX < 455 and 330 < mouseY < 370:
         noFill()
         stroke(255,220)
         rect(285,330,170,40)
    elif 285 < mouseX < 455 and 380 < mouseY < 420:
        noFill()
        stroke(255,220)
        rect(285,380,170,40)
    elif 285 < mouseX < 455 and 430 < mouseY < 470:
         noFill()
         stroke(255,220)
         rect(285,430,170,40)
    else:
        return False
