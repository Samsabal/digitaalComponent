import nextPrevious, bordspel

def setup():
    global tutoPage, kaart, ziekenhuis, speciaal, muur, westBerlijn, oostBerlijn, tunnel, soldaat, val, richting
    tutoPage = 1
    kaart = loadImage("Images/kaart.png")
    ziekenhuis = loadImage("Images/ziekenhuis.jpg")
    ziekenhuis.resize(60,60)
    speciaal = loadImage("images/speciaal.jpg")
    speciaal.resize(60,60)
    muur = loadImage("images/muur.jpg")
    muur.resize(60,60)
    westBerlijn = loadImage("Images/west-berlijn.jpg")
    westBerlijn.resize(60,60)
    oostBerlijn = loadImage("Images/oost-berlijn.jpg")
    oostBerlijn.resize(60,60)
    tunnel = loadImage("Images/tunnel.jpg")
    tunnel.resize(60,60)
    soldaat = loadImage("Images/soldaat.jpg")
    soldaat.resize(60,60)
    val = loadImage("images/val.jpg")
    val.resize(60,60)
    richting = loadImage("images/richting.jpg")
    richting.resize(60,60)
    
def draw():
    tut1()

def tut1():
    global tutoPage

    if tutoPage == 1:
        stroke(0, 0, 0)
        strokeWeight(2)
        bordspel.draw()
        nextPrevious.backgroundTint()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
        
        textVak()
        
        textSize(21)
        fill(0)
        text("""  Welkom bij BvB
  BvB is een tactisch en competitief bordspel. Dat 
  plaats vindt in Berlijn tijdens de koude oorlog. Het 
  is aan jou om de intel van de tegenstander te stelen 
  en zo de oorlog te winnen.""", 100, 70)
        
    elif tutoPage == 2:
        stroke(0, 0, 0)
        strokeWeight(2)
        bordspel.draw()
        nextPrevious.backgroundTint()
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
        
        #Oplichten vakjes
        image(richting, 375, 390)
        image(westBerlijn, 75, 30)
        image(oostBerlijn, 615, 570)
        
        textVak()
        
        textSize(21)
        fill(0)
        text("""  Er zijn 2 manieren om het spel te winnen:
  1. Door aan de andere kant te komen. 
  2. Door alle vijandige spionnen uit te schakelen.
  
  Je beweegt in BvB door middel van een dobbelsteen 
  die van 1 tot 3 gaat. Je kan alleen horizontaal 
  en verticaal bewegen.""", 100, 70)
    elif tutoPage == 3:
        stroke(0, 0, 0)
        strokeWeight(2)
        bordspel.draw()
        nextPrevious.backgroundTint()
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
        
        textVak()
        
        textSize(21)
        fill(0)
        text("""  In BvB kan je ook met andere spelers vechten door 
  middel van het duel systeem.
  Een duel begint wanneer je met je spion direct 
  tegen de tegenstanders spion aan staat. 
  
  Je gooit dan de normale dobbelsteen en wie het 
  hoogste aantal gooit wint het gevecht. De 
  tegenstanders spion is dan dood en moet in de 
  graveyard worden geplaatst.""", 100, 70)
        
    elif tutoPage == 4:
        stroke(0, 0, 0)
        strokeWeight(2)
        bordspel.draw()
        nextPrevious.backgroundTint()
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
        
        #Oplichten vakjes
        image(ziekenhuis, 435, 510)
         
        textVak()
        
        textSize(21)
        fill(0)
        text("""  In BvB kan je spion ook gewond raken. Hierdoor 
  mag je met elke beurt 1 stap minder zetten. 
  Een gewonde spion kan je helen in het ziekenhuis
  getoond op de pagina hiervoor. Gewonde spionnen 
  moeten ook de tunnels gerbuiken. 
  Wanneer een gewonde spion nog een keer gewond 
  raakt is deze dood. """, 100, 70)
        
    elif tutoPage == 5:
        stroke(0, 0, 0)
        strokeWeight(2)
        bordspel.draw()
        nextPrevious.backgroundTint()
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
        
        #Oplichten vakjes
        image(soldaat, 375, 390)
        image(val, 495, 390)
        
        textVak()
        
        textSize(21)
        fill(0)
        text("""  Er zijn ook kaarten in BvB. 2 hiervan zijn de militair 
  en de val. De militair en de val kunnen geplaatst 
  worden op de kaart en kunnen niet bewegen. 
  De militair start een duel met spionnen en kan de 
  spionnen alleen gewond maken. 
  De val gaat alleen af wanneer er op hetzelfde vakje 
  wordt gestaan en dient dus meer als een blokkade. 
  De val dood spionnen wel.""", 100, 70)
        
    elif tutoPage == 6:
        stroke(0, 0, 0)
        strokeWeight(2)
        bordspel.draw()
        nextPrevious.backgroundTint()
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
        
        #Oplichten vakjes
        image(speciaal, 375, 510)
        image(speciaal, 75, 450)
        image(speciaal, 615, 150)
        
        textVak()
        
        textSize(21)
        fill(0)
        text("""  Er zijn ook speciale kaarten. Dit zijn kaarten die 
  sterker zijn dan gewone kaarten en deze kan je 
  alleen op het aangewezen vak halen.""", 100, 70)
        
    elif tutoPage == 7:
        stroke(0, 0, 0)
        strokeWeight(2)
        bordspel.draw()
        nextPrevious.backgroundTint()
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
        
        #Oplichten vakjes
        image(muur, 615, 30)
        image(muur, 315, 330)
        image(muur, 255, 390)
        image(muur, 195, 450)
        image(muur, 135, 510)
        image(muur, 75, 570)
        image(tunnel, 255, 330)
        
        textVak()
        
        textSize(21)
        fill(0)
        text("""  Er zijn 2 manieren om over de muur te komen: 
  1. Over de muur heen klimmen dit doe je door de 
     dobbelsteen te gooien. 
     1 = spion raakt gewond, 
     2 = spion blijft staan, 
     3 = spion mag over de muur. 
  2. Door de tunnel gaan. Als je de tunnel ingaat ga 
     je naar de andere kan en is je beurt voorbij.""", 100, 70)
        
    elif tutoPage == 8:
        stroke(0, 0, 0)
        strokeWeight(2)
        bordspel.draw()
        nextPrevious.backgroundTint()
        nextPrevious.previousButton()
        nextPrevious.homeButton()
        
        textVak()
        
        textSize(21)
        fill(0)
        text("""  Gefeliciteerd!
  Je bent klaar met de Tutorial en nu helemaal klaar
  om te spelen. Veel plezier!""", 100, 70)
        
    else:
        return False
    
def textVak():
    fill(255)
    stroke(0)
    strokeWeight(3)
    rect(100, 45, 550, 300)
    
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
