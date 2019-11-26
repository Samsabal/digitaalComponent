
import template, logo, buttons, bordspel, homeButton, exitButton

def setup():
    global currentScene
    size(750,750)
    currentScene = "home"
    template.setup()
    logo.setup()
    bordspel.setup()
    homeButton.setup()
    
def draw():
    global currentScene
    #de currentScene laat zien welk scherm het programma moet weergeven
    #de if-statement verteld het programma wat het moet uitvoeren per scene.
    
    if currentScene == "home":
        template.draw()
        logo.draw()
        buttons.draw()
        exitButton.draw()
        hoofdTekst()
        kopjes()
    elif currentScene == "bordspel":
        bordspel.draw()
        homeButton.draw()
        goBack()
    
def hoofdTekst():
    #de tekst op het beginscherm, en de lijn in het midden van het scherm
    textSize(45)
    fill(0)
    text("Battle van Berlijn", 200, 330)
    
    stroke(0)
    strokeWeight(3)
    line(0, 350, 750, 350)
    
    textSize(22)
    fill(0)

    text("Klik op een onderdeel om verder te gaan", 160, 385)
    
def kopjes():
    #de tekst in de verschillende knoppen
    textSize(21)
    fill(0)
    text("- Bordspel", 295, 480)
            
    
def mousePressed():
    #als de muis wordt ingedrukt binnen de verschillende knoppen veranderd de scene
    #en dus veranderd de if in draw() en zo verschijnt een ander scherm
    global currentScene
    if currentScene == "home":
        if 285 < mouseX < 455 and 452 < mouseY < 492:
            currentScene = "bordspel"
            
    if currentScene == "bordspel":
        if 49 < mouseX < 105 and 679 < mouseY < 745:
            currentScene = "home"
            
    if currentScene == "home":
        if 656 < mouseX < 731 and 700 < mouseY < 740:
            exit()
   
def goBack():
    #de tekst op het scherm "bordspel"
    global currentScene    
    if currentScene == "bordspel":
        textSize(21)
        fill(0)
        text("Klik op het logo om terug te gaan naar het hoofdscherm", 130, 717)
