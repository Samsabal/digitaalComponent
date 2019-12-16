
def draw(bordspelGrid):
    fill(255)
    stroke(0)
    strokeWeight(3)
    rect(100, 75, 550, 300)
    
    fill(255, 0, 0)
    rect(600, 75, 50, 50)
    fill(0)
    textSize(50)
    text("X", 610, 120)

    textSize(21)
    fill(0)
    if bordspelGrid == -1: # West-Berlijn
        textSize(24)
        text("  West-Berlijn Vak", 275, 125)
        textSize(21)
        text("  Alle spionnen van West-Berlijn (blauwe pionnen)\n"+
             "  beginnen in het vak van de thuisbasis van\n" +
             "  West-Berlijn.", 100, 200)
    elif bordspelGrid == -2: # Oost-Berlijn
        textSize(24)
        text("  Oost-Berlijn Vak", 275, 125)
        textSize(21)
        text("  Alle spionnen van Oost-Berlijn (rode pionnen)\n"+
             "  beginnen in het vak van de thuisbasis van\n"+
             "  Oost-Berlijn.", 100, 200)
    elif bordspelGrid == -3: # Ziekenhuis
        textSize(24)
        text("  Ziekenhuis Vak", 275, 125)
        textSize(21)
        text("  Als je op dit vak loopt kun je een gewonde\n"+
             "  spion helen.", 100, 200)
    elif bordspelGrid == -4: # Muur
        textSize(24)
        text("  Muur Vak", 275, 125)
        textSize(21)
        text("  Een pion kan over de muur gaan door 3 te\n"+
             "  gooien. Als je 2 gooit blijf je staan en\n"+
             "  als 1 gooi raak je gewond.", 100, 200)
    elif bordspelGrid == -5: # Speciaal
        textSize(24)
        text("  Speciaal Vak", 275, 125)
        textSize(21)
        text("  Als je op dit vak komt mag je een speciale\n"+
             "  kaart pakken.", 100, 200)
    elif bordspelGrid == -6: # Tunnel
        textSize(24)
        text("  Tunnel Vak", 275, 125)
        textSize(21)
        text("  Je kunt dit gebruiken om aan de andere \n"
             "  kant van de Berlijnse muur te komen zonder\n"+
             "  het risico te lopen gewond te raken.", 100, 200)
    else: # Leeg
        return False
