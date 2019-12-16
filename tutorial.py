import nextPrevious

def setup():
    global tutoPage
    tutoPage = 1
    
def draw():
    tut1()
    #Delete later
    textSize(16)
    fill(0)
    text("Page " + str(tutoPage), 10, 30)
    
def tut1():
    global tutoPage
    if tutoPage == 1:
        nextPrevious.nextButton()
        nextPrevious.homeButton()
    elif tutoPage == 2:
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
    elif tutoPage == 3:
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
    elif tutoPage == 4:
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
    elif tutoPage == 5:
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
    elif tutoPage == 6:
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
    elif tutoPage == 7:
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
    elif tutoPage == 8:
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
    elif tutoPage == 9:
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
    elif tutoPage == 10:
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
    elif tutoPage == 11:
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
    elif tutoPage == 12:
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
    elif tutoPage == 13:
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
    elif tutoPage == 14:
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
    elif tutoPage == 15:
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
    elif tutoPage == 16:
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
    elif tutoPage == 17:
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
    elif tutoPage == 18:
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
    elif tutoPage == 19:
        nextPrevious.previousButton()
        nextPrevious.homeButton()
    else:
        return False
    
def pageIs(x):
    #Zorgt ervoor dat de knoppen in de Snelle Navigatie werken.
    global tutoPage
    tutoPage = x
    
def pageUp():
    #Zorgt ervoor dat de Next knop werkt.
    global tutoPage
    tutoPage = tutoPage + 1
    
def pageDown():
    #Zorgt ervoor dat de Previous knop werkt.
    global tutoPage
    tutoPage = tutoPage - 1
