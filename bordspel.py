
grid = [ [1]*10 for n in range(10)]
grid[0][0] = -1 # West-Berlijn = Blauw
grid[9][9] = -2 # Oost-Berlijn = Rood
grid[1][3] = -3
grid[8][6] = -3 # Ziekenhuis

w = 60 # Breedte van de grid cells

def setup():
    global template_image, ziekenhuis_masked
    ziekenhuis = loadImage("images/ziekenhuis.jpg")
    ziekenhuis.resize(w,w)
    
    # Maak mask
    mask_image = createGraphics(ziekenhuis.width,ziekenhuis.height)
    mask_image.beginDraw()
    mask_image.rect(0, 0, w, w)
    mask_image.endDraw()
    
    # Maak copie van mask
    ziekenhuis_masked = ziekenhuis.copy();
    ziekenhuis.mask(mask_image);
    
    template_image = loadImage("template.jpg")
    template_image.resize(750,750)
    
def draw():
    #de afbeelding van het spel in het midden van het scherm en de 
    #achtergrond over heel het scherm
    global template_image, ziekenhuis_masked
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
                rect(x,y,w,w)
            elif col == -2: # Oost-Berlijn
                fill(255, 0, 0)
                rect(x,y,w,w)
            elif col == -3: # Ziekenhuis
                image(ziekenhuis_masked, x, y)
            else: # Leeg
                fill(255)
                rect(x,y,w,w)
            x = x + w
        y = y + w
        x = 75
