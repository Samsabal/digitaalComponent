import time

def setup():
    global start,font
    start = time.time()
    font = createFont("Arial", 40)
    frameRate(1)
    
    
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

    
