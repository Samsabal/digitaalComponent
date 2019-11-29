
grid = [ [1]*10 for n in range(10)]
grid[0][0] = -1 # West-Berlijn = Blauw
grid[9][9] = -2 # Oost-Berlijn = Rood

w = 60 # Breedte van de grid cells
 
def setup():
    global template_image
    template_image = loadImage("template.jpg")
    template_image.resize(750,750)
    
def draw():
    #de afbeelding van het spel in het midden van het scherm en de 
    #achtergrond over heel het scherm
    global template_image
    background(255)
    tint(255, 230)
    image(template_image, 0, 0)
    
    noFill()
    stroke(0)
    strokeWeight(3)
    rect(1, 673, 747, 75)
    
    x,y = 75,30 # Waar de grid begint op de X en Y as
    
    for row in grid:
        for col in row:
            if col == -1: # West-Berlijn
                fill(0, 0, 255)
            elif col == -2: # Oost-Berlijn
                fill(255, 0, 0)
            else: # Leeg
                fill(255)
            rect(x, y, w, w)
            x = x + w
        y = y + w
        x = 75
