# de verschillende knoppen op het beginscherm
def draw():
    button1()
    button2()
    button3()
    button4()

        
def button1():
    #handleiding
    noFill()
    stroke(0,150)
    strokeWeight(3)
    rect(285,402,170,40)
    mouseHover()
    
def button2():
    #bordspel
    noFill()
    stroke(0,150)
    strokeWeight(3)
    rect(285,452,170,40)
    mouseHover()
    
def button3():
    #gamemodes
    noFill()
    stroke(0,150)
    strokeWeight(3)
    rect(285,502,170,40)
    mouseHover()
    
def button4():
    #tutorial
    noFill()
    stroke(0,150)
    strokeWeight(3)
    rect(285,552,170,40)
    mouseHover()
    
def mouseHover():
    if 285 < mouseX < 455 and 402 < mouseY < 442:
         noFill()
         stroke(255,220)
         rect(285,402,170,40)
    elif 285 < mouseX < 455 and 452 < mouseY < 492:
        noFill()
        stroke(255,220)
        rect(285,452,170,40)
    elif 285 < mouseX < 455 and 502 < mouseY < 542:
         noFill()
         stroke(255,220)
         rect(285,502,170,40)
    elif 285 < mouseX < 455 and 552 < mouseY < 592:
         noFill()
         stroke(255,220)
         rect(285,552,170,40)
    else:
        return False
