import nextPrevious, bordspel

def setup():
    global tutoPage, kaart, ziekenhuis, speciaal, muur, westBerlijn, oostBerlijn, tunnel, soldaat, spion_rood, spion_blauw, spion_gewond, val, arrow_ver, arrow_hor
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
    soldaat = loadImage("Images/soldaat.png")
    soldaat.resize(60,60)
    spion_blauw = loadImage("Images/spion_blauw.png")
    spion_blauw.resize(60,60)
    spion_rood = loadImage("Images/spion_rood.png")
    spion_rood.resize(60,60)
    spion_gewond = loadImage("Images/spion_gewond.png")
    spion_gewond.resize(60,60)
    val = loadImage("images/val.jpg")
    val.resize(60,60)
    arrow_ver = loadImage("Images/arrow_ver.png")
    arrow_ver.resize(60,120)
    arrow_hor = loadImage("Images/arrow_hor.png")
    arrow_hor.resize(120,60)
    
def draw():
    tut1()
    textSize(16)
    fill(0)
    #Dit is de page indicator in de handleiding.
    text("Page " + str(tutoPage), 10, 30)
    
def tut1():
    globl tutoPage
    
    if tutoPage == 1:
        #Het bordspel dat op de achtergrond staat.
        stroke(0, 0, 0)
        strokeWeight(2)
        bordspel.draw()
        
        #Knoppen en de getinte achtergrond
        nextPrevious.backgroundTint()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
        
        #Het vak waar de tekst in staat
        textVak()
        
        #De tekst die in het vak staat
        textSize(21)
        fill(0)
        text("""  Welkom bij BvB
  BvB is een tactisch en competitief bordspel. Dat 
  plaats vindt n Berlijn tijdens de koude oorlog. Het 
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
        
        image(arrow_ver, 555, 330)
        image(arrow_hor, 435, 450)
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
        
        image(spion_rood, 435, 390)
        image(spion_blauw, 495, 390)
        
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
        
        image(spion_gewond, 435, 390)
        image(ziekenhuis, 435, 510)
         
        textVak()
        
        textSize(21)
        fill(0)
        text("""  In BvB kan je spion ook gewond raken. Hierdoor 
  mag je met elke beurt 1 stap minder zetten.
  Een gewonde spion kan je helen in het ziekenhuis
  getoond op het bord hieronder.
  Gewonde spionnen moeten ook de tunnels 
  gebruiken.
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
        
        image(speciaal, 375, 510)
        image(speciaal, 75, 450)
        image(speciaal, 615, 150)
        
        textVak()
        
        textSize(21)
        fill(0)
        text("""  Er zijn ook speciale kaarten. Dit zijn kaarten die 
  sterker zijn dan gewone kaarten en deze kan je 
  alleen op het aangewezen vak halen.
  Je mag in totaal 7 kaarten in je hand hebben
  waarvan 3 special en 4 standaard.
  Elke beurt heb je de kans om een standaard kaart 
  om te ruilen je kan deze beurt dan geen kaart 
  meer spelen.""", 100, 70)
        
    elif tutoPage == 7:
        stroke(0, 0, 0)
        strokeWeight(2)
        bordspel.draw()
        
        nextPrevious.backgroundTint()
        nextPrevious.previousButton()
        nextPrevious.nextButton()
        nextPrevious.homeButton()
        
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
  om te spelen. Als er iets nog onduidelijk is raad ik 
  aan de handleiding door te nemen. 
  Veel plezier!""", 100, 70)
        
    else:
        return False
    
def textVak():
    #Het vak waar de tekst in staat.
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
