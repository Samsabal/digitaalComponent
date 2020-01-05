#De handleiding en bijbehorende Snelle Navigatie.
import nextPrevious
def setup():
    global currentPage, template, page1, page2, page3, page4, page5, page6, page7, page8, page9, page10, page11, page12, page13, page14, page15, page16, page17, page18, page19
    currentPage = 1
    template = loadImage("Images/template.jpg")
    page1 = loadImage("Images/page1.png")
    page2 = loadImage("Images/page2.png")
    page3 = loadImage("Images/page3.png")
    page4 = loadImage("Images/page4.png")
    page5 = loadImage("Images/page5.png")
    page6 = loadImage("Images/page6.png")
    page7 = loadImage("Images/page7.png")
    page8 = loadImage("Images/page8.png")
    page9 = loadImage("Images/page9.png")
    page10 = loadImage("Images/page10.png")
    page11 = loadImage("Images/page11.png")
    page12 = loadImage("Images/page12.png")
    page13 = loadImage("Images/page13.png")
    page14 = loadImage("Images/page14.png")
    page15 = loadImage("Images/page15.png")
    page16 = loadImage("Images/page16.png")
    page17 = loadImage("Images/page17.png")
    page18 = loadImage("Images/page18.png")
    page19 = loadImage("Images/page19.png")
    
    template.resize(750,750)
    page1.resize(450,650)
    page2.resize(450,650)
    page3.resize(450,650)
    page4.resize(450,650)
    page5.resize(450,650)
    page6.resize(450,650)
    page7.resize(450,650)
    page8.resize(450,650)
    page9.resize(450,650)
    page10.resize(450,650)
    page11.resize(450,650)
    page12.resize(450,650)
    page13.resize(450,650)
    page14.resize(450,650)
    page15.resize(450,650)
    page16.resize(450,650)
    page17.resize(450,650)
    page18.resize(450,650)
    page19.resize(450,650)
    frameRate(60)
        
def draw():
    #Dit is de page indicator in de handleiding.
    image(template, 0, 0)
    textSize(16)
    fill(0)
    text("Page " + str(currentPage), 10, 30)
    handleiding1()
    noFill()
    strokeWeight(5)
    stroke(0)
    if currentPage > 0:
        rect(150,10,450,650)
    
def handleiding1():
    #Hiermee wordt de afbeelding in handleiding veranderd.
    global currentPage
    if currentPage == 0:
        snelNav()
        backButton()
        nextPrevious.homeButton()
    elif currentPage == 1:
        image(page1, 150, 10)
        nextPrevious.nextButton()
        navHoofdButton()
        nextPrevious.homeButton()
    elif currentPage == 2:
        image(page2, 150, 10)
        nextPrevious.draw()
    elif currentPage == 3:
        image(page3, 150, 10)
        nextPrevious.draw()
    elif currentPage == 4:
        image(page4, 150, 10)
        nextPrevious.draw()
    elif currentPage == 5:
        image(page5, 150, 10)
        nextPrevious.draw()
    elif currentPage == 6:
        image(page6, 150, 10)
        nextPrevious.draw()
    elif currentPage == 7:
        image(page7, 150, 10)
        nextPrevious.draw()
    elif currentPage == 8:
        image(page8, 150, 10)
        nextPrevious.draw()
    elif currentPage == 9:
        image(page9, 150, 10)
        nextPrevious.draw()
    elif currentPage == 10:
        image(page10, 150, 10)
        nextPrevious.draw()
    elif currentPage == 11:
        image(page11, 150, 10)
        nextPrevious.draw()
    elif currentPage == 12:
        image(page12, 150, 10)
        nextPrevious.draw()
    elif currentPage == 13:
        image(page13, 150, 10)
        nextPrevious.draw()
    elif currentPage == 14:
        image(page14, 150, 10)
        nextPrevious.draw()
    elif currentPage == 15:
        image(page15, 150, 10)
        nextPrevious.draw()
    elif currentPage == 16:
        image(page16, 150, 10)
        nextPrevious.draw()
    elif currentPage == 17:
        image(page17, 150, 10)
        nextPrevious.draw()
    elif currentPage == 18:
        image(page18, 150, 10)
        nextPrevious.draw()
    elif currentPage == 19:
        image(page19, 150, 10)
        nextPrevious.previousButton()
        nextPrevious.homeButton()
        navButton()
    else:
        return False

def snelNav():
    #Hier worden alle knoppen in de Snelle Navigatie getekend.
    image(template, 0, 0)
    textSize(45)
    tint(255)
    text("Snelle Navigatie", 210, 60)
    textSize(21)
    text("Klik op een knop om naar de pagina te gaan", 155, 120)
    stroke(0)
    strokeWeight(3)
    line(0, 80, 750, 80)
    
    noFill()
    stroke(0, 150)
    strokeWeight(3)
    rect(35, 150, 200, 50) #1 Eerste 6 vakjes aan de linker kant.
    rect(35, 235, 200, 50) #2
    rect(35, 320, 200, 50) #3
    rect(35, 405, 200, 50) #4
    rect(35, 490, 200, 50) #5
    rect(35, 575, 200, 50) #6
    rect(275, 150, 200, 50) #7 De 6 vakjes daarna in het midden.
    rect(275, 235, 200, 50) #8
    rect(275, 320, 200, 50) #9
    rect(275, 405, 200, 50) #10
    rect(275, 490, 200, 50) #11
    rect(275, 575, 200, 50) #12
    rect(515, 150, 200, 50) #13 De laatste 6 vakjes aan de rechter kant.
    rect(515, 235, 200, 50) #14
    rect(515, 320, 200, 50) #15
    rect(515, 405, 200, 50) #16
    rect(515, 490, 200, 50) #17
    rect(515, 575, 200, 50) #18
    
    textSize(21)
    tint(255)
    text("- Korte Uitleg", 45, 185)#1       /Links/ De tekst die in de kopjes staat
    text("- In De Doos", 45, 270)#2
    text("- No Place Zones", 45, 355)#3
    text("- Voorbereiding", 45, 440)#4
    text("- Spelverloop", 45, 525)#5
    text("- Thuisfronten", 45, 610)#6
    text("- Speciale Kaarten", 285, 185)#7  /Midden/
    text("- Ziekenhuis", 285, 270)#8
    text("- Muur #1", 285, 355)#9
    text("- Muur #2", 285, 440)#10
    text("- Tunnels", 285, 525)#11
    text("- Pion Beweging", 285, 610)#12
    text("- Dueleren", 525, 185)#13         /Rechts/
    text("- Militair En Val", 525, 270)#14
    text("- Vallen Plaatsen", 525, 355)#15
    text("- Gewond Raken", 525, 440)#16
    text("- Kaarten #1", 525, 525)#17
    text("- Kaarten #2", 525, 610)#18
    
    #Ervoor zorgen dat de knoppen oplichten.
    if 35 < mouseX < 235 and 150 < mouseY < 200:#1    /Links/
        noFill()
        stroke(255)
        rect(35, 150, 200, 50)
    elif 35 < mouseX < 235 and 235 < mouseY < 285:#2 
        noFill()
        stroke(255)
        rect(35, 235, 200, 50)
    elif 35 < mouseX < 235 and 320 < mouseY < 370:#3
        noFill()
        stroke(255)
        rect(35, 320, 200, 50)
    elif 35 < mouseX < 235 and 405 < mouseY < 455:#4
        noFill()
        stroke(255)
        rect(35, 405, 200, 50)
    elif 35 < mouseX < 235 and 490 < mouseY < 540:#5
        noFill()
        stroke(255)
        rect(35, 490, 200, 50)
    elif 35 < mouseX < 235 and 575 < mouseY < 625:#6
        noFill()
        stroke(255)
        rect(35, 575, 200, 50)
    elif 275 < mouseX < 475 and 150 < mouseY < 200:#7  /Midden/
        noFill()
        stroke(255)
        rect(275, 150, 200, 50)
    elif 275 < mouseX < 475 and 235 < mouseY < 285:#8 
        noFill()
        stroke(255)
        rect(275, 235, 200, 50)
    elif 275 < mouseX < 475 and 320 < mouseY < 370:#9
        noFill()
        stroke(255)
        rect(275, 320, 200, 50)
    elif 275 < mouseX < 475 and 405 < mouseY < 455:#10
        noFill()
        stroke(255)
        rect(275, 405, 200, 50)
    elif 275 < mouseX < 475 and 490 < mouseY < 540:#11
        noFill()
        stroke(255)
        rect(275, 490, 200, 50)
    elif 275 < mouseX < 475 and 575 < mouseY < 625:#12
        noFill()
        stroke(255)
        rect(275, 575, 200, 50)
    elif 515 < mouseX < 715 and 150 < mouseY < 200:#13 /Rechts/
        noFill()
        stroke(255)
        rect(515, 150, 200, 50)
    elif 515 < mouseX < 715 and 235 < mouseY < 285:#14
        noFill()
        stroke(255)
        rect(515, 235, 200, 50)
    elif 515 < mouseX < 715 and 320 < mouseY < 370:#15
        noFill()
        stroke(255)
        rect(515, 320, 200, 50)
    elif 515 < mouseX < 715 and 405 < mouseY < 455:#16
        noFill()
        stroke(255)
        rect(515, 405, 200, 50)
    elif 515 < mouseX < 715 and 490 < mouseY < 540:#17
        noFill()
        stroke(255)
        rect(515, 490, 200, 50)
    elif 515 < mouseX < 715 and 575 < mouseY < 625:#18
        noFill()
        stroke(255)
        rect(515, 575, 200, 50)
    
def pageIs(x):
    #Zorgt ervoor dat de knoppen in de Snelle Navigatie werken.
    global currentPage
    currentPage = x

def pageUp():
    #Zorgt ervoor dat de Next knop werkt.
    global currentPage
    currentPage = currentPage + 1
    
def pageDown():
    #Zorgt ervoor dat de Previous knop werkt.
    global currentPage
    currentPage = currentPage - 1

def navHoofdButton():
    #De button die leidt naar de Snelle Navigatie op de eerste pagina van de handleiding.
    noFill()
    stroke(0, 150)
    strokeWeight(5)
    rect(19, 678, 75, 40)
    
    textSize(26)
    fill(0)
    text("NAVI", 25, 707)
    
    #Zorgt ervoor dat de knop oplicht.
    if 19 < mouseX < 94 and 678 < mouseY < 718:
        noFill()
        stroke(255, 220)
        rect(19, 678, 75, 40)
        fill(255)
        textSize(26)
        text("NAVI", 25, 707)
        
    else:
        return False

def navButton():
    #De button die naar de Snelle Navigatie leidt.
    noFill()
    stroke(0, 150)
    strokeWeight(5)
    rect(19, 618, 75, 40)
    
    textSize(26)
    fill(0)
    text("NAVI", 25, 647)
    
    #Zorgt ervoor dat de knop oplicht.
    if 19 < mouseX < 94 and 618 < mouseY < 658:
        noFill()
        stroke(255, 220)
        rect(19, 618, 75, 40)
        fill(255)
        textSize(26)
        text("NAVI", 25, 647)
        
    else:
        return False    
    
def backButton():
    #De back button in de Snelle Navigatie.
    noFill()
    stroke(0, 150)
    strokeWeight(5)
    rect(656, 678, 75, 40)
    
    textSize(26)
    fill(0)
    text("BACK", 660, 707)
    
    #Zorgt ervoor dat de knop oplicht.
    if 656 < mouseX < 731 and 678 < mouseY < 718:
        noFill()
        stroke(255, 220)
        rect(656, 678, 75, 40)
        fill(255)
        textSize(26)
        text("BACK", 660, 707)
    else:
        return False
