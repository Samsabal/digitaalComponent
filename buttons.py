# de verschillende knoppen op het beginscherm
def draw():
    button2()
    
def button2():
    noFill()
    stroke(0,150)
    rect(285,452,170,40)
    mouseHover()
    
def mouseHover():
    if 285 < mouseX < 455 and 452 < mouseY < 492:
        noFill()
        stroke(255,220)
        rect(285,452,170,40)
