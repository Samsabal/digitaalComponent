
def draw():
    fill(255)
    stroke(0)
    strokeWeight(1)
    rect(100, 75, 550, 300, 5)
    
    line(120, 275, 620, 275)
    
    sluiten()
    kleurverandering()
    
    textSize(28)
    text("Blokkade", 120, 125)
    textSize(16)
    text("Je tegenstander via 1 weg naar je basis dwingen?\n" +
             "Dat kan! Deze preset blokkeert bijna alle wegen naar je\n" +
             "thuisbasis. Zo wordt het voor je tegenstander\n" +
             "een stuk moeilijker om je te verslaan!" , 120, 180)
    




def sluiten():
    noFill()
    stroke(0,255)
    strokeWeight(1)
    rect(175,300,170,40)
    fill(0)
    textSize(20)
    text("Sluiten", 225, 327)
    
def kleurverandering():
    if 175 < mouseX < 345 and 300 < mouseY < 340:
        noFill()
        stroke(0,150)
        strokeWeight(2)
        rect(175,300,170,40)
    
