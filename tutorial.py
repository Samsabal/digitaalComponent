import nextPrevious, bordspel

def setup():
    global tutoPage, kaart, ziekenhuis, speciaal, muurTut
    tutoPage = 1
    kaart = loadImage("Images/kaart.png")
    ziekenhuis = loadImage("Images/ziekenhuis.jpg")
    ziekenhuis.resize(400,400)
    speciaal = loadImage("images/speciaal.jpg")
    speciaal.resize(400,400)
    muurTut = loadImage("images/speciaal.jpg")
    muurTut.resize(400,400)
def draw():
    tut1()

def tut1():
    global tutoPage

    if tutoPage == 1:
        nextPrevious.nextButton()
        nextPrevious.homeButton()
        fill(255)
        stroke(0)
        strokeWeight(3)
        rect(100, 75, 550, 300)
        textSize(21)
        fill(0)
        text("""  Welkom bij BvB
  BvB is een tactisch en competitief bordspel. Dat 
  plaats vindt in Berlijn tijdens de koude oorlog. Het 
  is aan jou om de intel van de tegenstander te stelen 
  en zo de oorlog te winnen.""", 100, 100)
    elif tutoPage == 2:
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
        image(kaart, 70, 30)
    elif tutoPage == 3:
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
        fill(255)
        stroke(0)
        strokeWeight(3)
        rect(100, 75, 550, 300)
        textSize(21)
        fill(0)
        text("""  Er zijn 2 manieren om het spel te winnen:
  1. Door aan de andere kant te komen. 
  2. Door alle vijandige spionnen uit te schakelen.
  
  Je beweegt in BvB door middel van een dobbelsteen 
  die van 1 tot 3 gaat. Je kan alleen horizontaal 
  en verticaal bewegen.""", 100, 100)
    elif tutoPage == 4:
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
        fill(255)
        stroke(0)
        strokeWeight(3)
        rect(100, 75, 550, 300)
        textSize(21)
        fill(0)
        text("""  In BvB kan je ook met andere spelers vechten door 
  middel van het duel systeem.
  Een duel begint wanneer je met je spion direct 
  tegen de tegenstanders spion aan staat. 
  
  Je gooit dan de normale dobbelsteen en wie het 
  hoogste aantal gooit wint het gevecht. De 
  tegenstanders spion is dan dood en moet in de 
  graveyard worden geplaatst.""", 100, 100)
    elif tutoPage == 5:
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
        image(ziekenhuis, 170, 130)
    elif tutoPage == 6:
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
        fill(255)
        stroke(0)
        strokeWeight(3)
        rect(100, 75, 550, 300)
        textSize(21)
        fill(0)
        text("""  In BvB kan je spion ook gewond raken. Hierdoor 
  mag je met elke beurt 1 stap minder zetten. 
  Een gewonde spion kan je helen in het ziekenhuis
  getoond op de pagina hiervoor. Gewonde spionnen 
  moeten ook de tunnels gerbuiken. 
  Wanneer een gewonde spion nog een keer gewond 
  raakt is deze dood. """, 100, 100)
    elif tutoPage == 7:
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
        fill(255)
        stroke(0)
        strokeWeight(3)
        rect(100, 75, 550, 300)
        textSize(21)
        fill(0)
        text("""  Er zijn ook kaarten in BvB. 2 hiervan zijn de militair 
  en de val. De militair en de val kunnen geplaatst 
  worden op de kaart en kunnen niet bewegen. 
  De militair start een duel met spionnen en kan de 
  spionnen alleen gewond maken. 
  De val gaat alleen af wanneer er op hetzelfde vakje 
  wordt gestaan en dient dus meer als een blokkade. 
  De val dood spionnen wel.""", 100, 100)
    elif tutoPage == 8:
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
        image(speciaal, 170, 130)
    elif tutoPage == 9:
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
        fill(255)
        stroke(0)
        strokeWeight(3)
        rect(100, 75, 550, 300)
        textSize(21)
        fill(0)
        text("""  Er zijn ook speciale kaarten. Dit zijn kaarten die 
  sterker zijn dan gewone kaarten en deze kan je 
  alleen op het aangewezen vak halen.""", 100, 100)
    elif tutoPage == 10:
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
        image(muurTut, 170, 130)
    elif tutoPage == 11:
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
        fill(255)
        stroke(0)
        strokeWeight(3)
        rect(100, 75, 550, 300)
        textSize(21)
        fill(0)
        text("""  Er zijn 2 manieren om over de muur te komen: 
  1. Over de muur heen klimmen dit doe je door de 
     dobbelsteen te gooien. 
     1 = spion raakt gewond, 
     2 = spion blijft staan, 
     3 = spion mag over de muur. 
  2. Door de tunnel gaan. Als je de tunnel ingaat ga 
     je naar de andere kan en is je beurt voorbij.""", 100, 100)
    elif tutoPage == 12:
        nextPrevious.previousButton()
        nextPrevious.homeButton()
        fill(255)
        stroke(0)
        strokeWeight(3)
        rect(100, 75, 550, 300)
        textSize(21)
        fill(0)
        text("""  Gefeliciteerd!
  Je bent klaar met de Tutorial en nu helemaal klaar
  om te spelen. Veel plezier!""", 100, 100)
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
