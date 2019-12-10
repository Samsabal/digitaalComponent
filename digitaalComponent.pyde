
import template, logo, buttons, bordspel, titleButton, exitButton, nextPrevious, bordspelInfo, gamemodes, handleiding, rushhour
from nextPrevious import homeButton


def setup():
    #wordt 1 keer uitgevoerd. roept alle modules die een setup hebben en voert deze uit aan het begin van het programma.
    global currentScene
    size(750,750)
    currentScene = "home"
    template.setup()
    logo.setup()
    bordspel.setup()
    titleButton.setup()
    nextPrevious.setup()
    handleiding.setup()
    rushhour.setup()
    
def draw():
    global currentScene
    #de currentScene laat zien welk scherm het programma moet weergeven
    #de if-statement verteld het programma wat het moet uitvoeren per scene door per scene de betreffende draw() aan te roepen.
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
        titleButton.draw()
        goBack()
    elif currentScene == "bordspelInfo":
        bordspelInfo.draw(bordspelGrid)
        goBack()
    elif currentScene == "gamemodes":
        gamemodes.draw()
    elif currentScene == "handleiding":
        handleiding.draw()
        nextPrevious.draw()
    elif currentScene == "rushhour":
        rushhour.draw()
        homeButton()
    else:
        return False        
    
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
    text("- Handleiding", 295, 430)
    text("- Bordspel", 295, 480)
    text("- Gamemodes", 295, 530)
    
def mousePressed():
    #als de muis wordt ingedrukt binnen de verschillende knoppen veranderd de scene
    #en dus veranderd de if in draw() en zo verschijnt een ander scherm
    global currentScene, bordspelGrid
    if currentScene == "home":
        if 285 < mouseX < 455 and 402 < mouseY < 442:
            currentScene = "handleiding"
        elif 285 < mouseX < 455 and 452 < mouseY < 492:
            currentScene = "bordspel"
        elif 285 < mouseX < 455 and 502 < mouseY < 542:
            currentScene = "gamemodes"
        elif 656 < mouseX < 731 and 700 < mouseY < 740:
            exit()
            
    if currentScene == "bordspel":
        if 49 < mouseX < 105 and 679 < mouseY < 745:
            currentScene = "home"
        gridX = (mouseX - 75)/bordspel.w
        gridY = (mouseY - 30)/bordspel.w
        if gridY < 10 and gridX < 10:
            if bordspel.grid[gridY][gridX] < 0:
                bordspelGrid = bordspel.grid[gridY][gridX]
                currentScene = "bordspelInfo"
            
    if currentScene == "handleiding" or currentScene == "gamemodes":
        if 342 < mouseX < 406 and 667 < mouseY < 735:
            currentScene = "home"
    
    if currentScene == "bordspelInfo":
        if 600 < mouseX < 648 and 77 < mouseY < 122:
            print(600 < mouseX < 648 and 77 < mouseY < 122)
            currentScene = "bordspel"
            
    if currentScene == "gamemodes" or currentScene == "handleiding" or currentScene == "rushhour":
        if 342 < mouseX < 406 and 667 < mouseY < 735:
            currentScene = "home"
            handleiding.pageIs(1) #Zorgt ervoor dat je niet elke keer helemaal terug hoeft te gaan in de handleiding.
            
            
    if currentScene == "gamemodes":
        if 285 < mouseX < 455 and 280 < mouseY < 320:
            print(285 < mouseX < 455 and 280 < mouseY < 320)
            currentScene = "rushhour"
            
    if currentScene == "handleiding":
        #De Previous en Next knoppen.
        if handleiding.currentPage != 19:
            if 656 < mouseX < 731 and 678 < mouseY < 718:
                handleiding.pageUp()
        if handleiding.currentPage != 0:
            if 19 < mouseX < 94 and 678 < mouseY < 718:
                handleiding.pageDown()
                
        #Snelle Navigatie linker kolom.
        if handleiding.currentPage == 0:
            if 35 < mouseX < 235 and 150 < mouseY < 200:
                handleiding.pageIs(2)
            if 35 < mouseX < 235 and 235 < mouseY < 285:
                handleiding.pageIs(3)
            if 35 < mouseX < 235 and 320 < mouseY < 370:
                handleiding.pageIs(4)
            if 35 < mouseX < 235 and 405 < mouseY < 455:
                handleiding.pageIs(5)
            if 35 < mouseX < 235 and 490 < mouseY < 540:
                handleiding.pageIs(6)
            if 35 < mouseX < 235 and 575 < mouseY < 625:
                handleiding.pageIs(7)
            #Snelle Navigatie middelste kolom.
            if 275 < mouseX < 475 and 150 < mouseY < 200:
                handleiding.pageIs(8)
            if 275 < mouseX < 475 and 235 < mouseY < 285:
                handleiding.pageIs(9)
            if 275 < mouseX < 475 and 320 < mouseY < 370:
                handleiding.pageIs(10)
            if 275 < mouseX < 475 and 405 < mouseY < 455:
                handleiding.pageIs(11)
            if 275 < mouseX < 475 and 490 < mouseY < 540:
                handleiding.pageIs(12)
            if 275 < mouseX < 475 and 575 < mouseY < 625:
                handleiding.pageIs(13)
            #Snelle Navigatie rechter kolom.
            if 515 < mouseX < 715 and 150 < mouseY < 200:
                handleiding.pageIs(14)
            if 515 < mouseX < 715 and 235 < mouseY < 285:
                handleiding.pageIs(15)
            if 515 < mouseX < 715 and 320 < mouseY < 370:
                handleiding.pageIs(16)
            if 515 < mouseX < 715 and 405 < mouseY < 455:
                handleiding.pageIs(17)
            if 515 < mouseX < 715 and 490 < mouseY < 540:
                handleiding.pageIs(18)
            if 515 < mouseX < 715 and 575 < mouseY < 625:
                handleiding.pageIs(19)
            
def goBack():
    #de tekst op het scherm "bordspel"
    global currentScene    
    if currentScene == "bordspel":
        textSize(21)
        fill(0)
        text("Klik op het logo om terug te gaan naar het hoofdscherm", 130, 717)
        
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
    text("- Handleiding", 295, 430)
    text("- Bordspel", 295, 480)
    text("- Gamemodes", 295, 530)
