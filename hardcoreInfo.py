

def draw():
    fill(255)
    stroke(0)
    strokeWeight(1)
    rect(100, 75, 550, 300, 5)
    
    line(120, 275, 620, 275)

    sluiten()
    kleurverandering()
    
    textSize(28)
    text("Hardcore", 120, 125)
    textSize(16)
    text("Je tegenstander niet de mogelijkheid van speciale kaarten geven?\n" +
             "Dat kan! Deze preset blokkeert de Speciale kaarten\n" +
             "voor de meeste manieren van het vak bereiken.\n" +
             "Zo wordt het voor je tegenstander een stuk moeilijker." , 120, 180)
    
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
