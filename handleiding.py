#Elke handx moet een nieuwe pagina van de handleiding worden.
def setup():
    global currentPage, template, page1, page2
    currentPage = 1
    template = loadImage("Images/template.jpg")
    page1 = loadImage("Images/page1.png")
    page2 = loadImage("Images/page2.png")
    template.resize(750,750)
    page1.resize(450,650)
    page2.resize(450,650)
    
def draw():
    image(template, 0, 0)
    textSize(16)
    text("Page " + str(currentPage), 10, 30)
    handleiding1()
    noFill()
    strokeWeight(5)
    rect(150,10,450,650)
    strokeWeight(3)
    
def handleiding1():
    global currentPage
    if currentPage == 1:
        image(page1, 150, 10)
    elif currentPage == 2:
        image(page2, 150, 10)
    else:
        return False


def pageUp():
    global currentPage
    currentPage = currentPage + 1
    
def pageDown():
    global currentPage
    currentPage = currentPage - 1

def mousePressed():
    global currentPage
    if currentPage != 20:
        if 656 < mouseX < 731 and 678 < mouseY < 718:
            pageUp()
    if currentPage != 1:
        if 19 < mouseX < 94 and 678 < mouseY < 718:
            pageDown()
        
        
    
    

 
