#Elke handx moet een nieuwe pagina van de handleiding worden.
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
    
def draw():
    image(template, 0, 0)
    textSize(16)
    text("Page " + str(currentPage), 10, 30)
    handleiding1()
    noFill()
    strokeWeight(5)
    rect(150,10,450,650)
    
def handleiding1():
    global currentPage
    if currentPage == 1:
        image(page1, 150, 10)
    elif currentPage == 2:
        image(page2, 150, 10)
    elif currentPage == 3:
        image(page3, 150, 10)
    elif currentPage == 4:
        image(page4, 150, 10)
    elif currentPage == 5:
        image(page5, 150, 10)
    elif currentPage == 6:
        image(page6, 150, 10)
    elif currentPage == 7:
        image(page7, 150, 10)
    elif currentPage == 8:
        image(page8, 150, 10)
    elif currentPage == 9:
        image(page9, 150, 10)
    elif currentPage == 10:
        image(page10, 150, 10)
    elif currentPage == 11:
        image(page11, 150, 10)
    elif currentPage == 12:
        image(page12, 150, 10)
    elif currentPage == 13:
        image(page13, 150, 10)
    elif currentPage == 14:
        image(page14, 150, 10)
    elif currentPage == 15:
        image(page15, 150, 10)
    elif currentPage == 16:
        image(page16, 150, 10)
    elif currentPage == 17:
        image(page17, 150, 10)
    elif currentPage == 18:
        image(page18, 150, 10)
    elif currentPage == 19:
        image(page19, 150, 10)
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
        
        
    
    

 
