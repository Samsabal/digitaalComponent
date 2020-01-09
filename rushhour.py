import time, timer as t

def setup():
    #laad de uitleg van rushhour en de template achtergrond in en resized deze naar het juiste formaat.
    global img, template, timer, start
    img = loadImage("Images/rushhour.png")
    template = loadImage("Images/template.jpg")
    img.resize(450,650)
    template.resize(750,750)
    frameRate(1)
    
    
def draw():
    global img, template, timer, start
    image(template, 0, 0)
    image(img, 150,10)
    
    #tekent een outline (rechthoek) om de uitleg heen
    noFill()
    stroke(0)
    strokeWeight(3)
    rect(149, 9, 452, 652)
    
    #timergerelateerde text + rectangles
    timer = countdown(t.start)
    fill(0)
    textSize(30)
    text(str(convert(int(timer))), 30, 375)
    text(str(convert(int(timer))), 630, 375)
    noFill()
    stroke(0)
    strokeWeight(3)
    rect(27, 344, 100, 40)
    rect(627, 344, 100, 40)
    
    #overige tekst/instructies
    textSize(20)
    text("Tijd over:", 29, 336)
    text("Tijd over:", 629, 336)
    textSize(14)
    text("Wanneer de tijd om is is het spel afgelopen!", 159, 570)


def countdown(start):
    snap = time.time()
    return (start + 600) - snap


def convert(sec):
  #functie die de tijd convert naar leesbare text
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60

  return str(hours) + ":" + str(mins) + ":" + str(sec)
