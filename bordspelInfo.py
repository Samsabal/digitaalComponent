
infoPage = 0

def setup():
    global infoPage
    infoPage = 0
    
def draw(bordspelGrid):
    fill(255)
    stroke(0)
    strokeWeight(1)
    rect(100, 75, 550, 300, 5)
    
    line(120, 275, 620, 275)
    
    closeButton()
    readMoreButton()
    if bordspelGrid == -1: # West-Berlijn
        infoPage = 7
        textSize(28)
        text("West-Berlijn Vak", 120, 125)
        textSize(21)
        text("Alle spionnen van West-Berlijn (blauwe pionnen)\n"+
             "beginnen in het vak van de thuisbasis van\n" +
             "West-Berlijn.", 120, 180)
    elif bordspelGrid == -2: # Oost-Berlijn
        infoPage = 7
        textSize(28)
        text("Oost-Berlijn Vak", 120, 125)
        textSize(21)
        text("Alle spionnen van Oost-Berlijn (rode pionnen)\n"+
             "beginnen in het vak van de thuisbasis van\n"+
             "Oost-Berlijn.", 120, 180)
    elif bordspelGrid == -3: # Ziekenhuis
        infoPage = 9
        textSize(28)
        text("Ziekenhuis Vak", 120, 125)
        textSize(21)
        text("Als je op dit vak loopt kun je een gewonde\n"+
             "spion helen.", 120, 180)
    elif bordspelGrid == -4: # Muur
        infoPage = 10
        textSize(28)
        text("Muur Vak", 120, 125)
        textSize(21)
        text("Een pion kan over de muur gaan door 3 te\n"+
             "gooien. Als je 2 gooit blijf je staan en\n"+
             "als 1 gooi raak je gewond.", 120, 180)
    elif bordspelGrid == -5: # Speciaal
        infoPage = 8
        textSize(28)
        text("Speciaal Vak", 120, 125)
        textSize(21)
        text("Als je op dit vak komt mag je een speciale\n"+
             "kaart pakken.", 120, 180)
    elif bordspelGrid == -6: # Tunnel
        infoPage = 12
        textSize(28)
        text("Tunnel Vak", 120, 125)
        textSize(21)
        text("Je kunt dit gebruiken om aan de andere \n"
             "kant van de Berlijnse muur te komen zonder\n"+
             "het risico te lopen gewond te raken.", 120, 180)
    else: # Leeg
        return False
    
def closeButton():
    noFill()
    stroke(0,255)
    strokeWeight(1)
    rect(175,300,170,40)
    fill(0)
    textSize(20)
    text("Sluiten", 225, 327)
    mouseHover()
    
def readMoreButton():
    noFill()
    stroke(0,255)
    strokeWeight(1)
    rect(405,300,170,40)
    fill(0)
    textSize(20)
    text("Lees meer...", 428, 327)
    mouseHover()
    
def mouseHover():
    if 175 < mouseX < 345 and 300 < mouseY < 340:
        noFill()
        stroke(0,150)
        strokeWeight(2)
        rect(175,300,170,40)
        cursor(HAND)
    elif 405 < mouseX < 575 and 300 < mouseY < 340:
        noFill()
        stroke(0,150)
        strokeWeight(2)
        rect(405,300,170,40)
        cursor(HAND)
    else:
        cursor(ARROW)
        
