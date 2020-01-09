#de exit-knop op het beginscherm, als de gebruiker hier op klikt sluit het programma
def draw():
    noFill()
    stroke(0, 150)
    strokeWeight(3)
    rect(656, 700, 75, 40)
    
    textSize(26)
    text("EXIT", 667, 729)
    
    if 656 < mouseX < 731 and 700 < mouseY < 740:
        noFill()
        stroke(255, 220)
        rect(656, 700, 75, 40)
        fill(255)
        text("EXIT", 667, 729)
        
