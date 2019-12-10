
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
        text("  West-Berlijn Vak", 100, 100)
        text("""  Hier komt uitgebreide informatie over het vak.""", 100, 125)
    elif bordspelGrid == -2: # Oost-Berlijn
        text("  Oost-Berlijn Vak", 100, 100)
        text("""  Hier komt uitgebreide informatie over het vak.""", 100, 125)
    elif bordspelGrid == -3: # Ziekenhuis
        text("  Ziekenhuis Vak", 100, 100)
        text("""  Hier komt uitgebreide informatie over het vak.""", 100, 125)
    elif bordspelGrid == -4: # Muur
        text("  Muur Vak", 100, 100)
        text("""  Hier komt uitgebreide informatie over het vak.""", 100, 125)
    elif bordspelGrid == -5: # Speciaal
        text("  Speciaal Vak", 100, 100)
        text("""  Hier komt uitgebreide informatie over het vak.""", 100, 125)
    elif bordspelGrid == -6: # Tunnel
        text("  Tunnel Vak", 100, 100)
        text("""  Hier komt uitgebreide informatie over het vak.""", 100, 125)
    else: # Leeg
        text("  Leeg Vak", 100, 100)
        text("""  Hier komt uitgebreide informatie over het vak.""", 100, 125)
