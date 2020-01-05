
def setup():
    #laad de uitleg van rushhour en de template achtergrond in en resized deze naar het juiste formaat.
    global img, template
    img = loadImage("Images/rushhour.png")
    template = loadImage("Images/template.jpg")
    img.resize(450,650)
    template.resize(750,750)
    frameRate(1)
    
    
def draw():
    global start,timer
    image(template, 0, 0)
    image(img, 150,10)
    
    #tekent een outline (rechthoek) om de uitleg heen
    noFill()
    stroke(0)
    strokeWeight(3)
    rect(149, 9, 452, 652)
    
    
    
    
def draw():
    global start,font, timer
    textFont(font)
    background(230)
    timer = countdown(start)
    fill(0)
    text(str(convert(int(timer))), 500, 70)





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
