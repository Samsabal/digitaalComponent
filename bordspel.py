
grid = [ [1]*10 for n in range(10)]
grid[0][0] = -1 # West-Berlijn = Blauw
grid[9][9] = -2 # Oost-Berlijn = Rood
grid[1][3] = grid[8][6] = -3 # Ziekenhuis
grid[1][4] = grid[8][5] = grid[7][0] = grid[2][9] = -5 # Speciaal
grid[4][6] = grid[5][3] = -6 # Tunnel

grid_x = 9
for grid_y in range(10): # Muur
    grid[grid_y][grid_x] = -4
    grid_x -= 1

w = 60 # Breedte van de grid cells

def setup():
    global template_image, ziekenhuis_masked, muur_masked, speciaal_masked, tunnel_masked
    template_image = loadImage("Images/template.jpg")
    template_image.resize(750,750)
    
    ziekenhuis = loadImage("images/ziekenhuis.jpg")
    ziekenhuis.resize(w,w)
    
    muur = loadImage("images/muur.jpg")
    muur.resize(w,w)
    
    speciaal = loadImage("images/speciaal.jpg")
    speciaal.resize(w,w)
    
    tunnel = loadImage("images/tunnel.jpg")
    tunnel.resize(w,w)
    
    # Maak mask
    mask_image = createGraphics(ziekenhuis.width,ziekenhuis.height)
    mask_image.beginDraw()
    mask_image.rect(0, 0, w, w)
    mask_image.endDraw()
    
    # Maak kopieen van masks
    ziekenhuis_masked = ziekenhuis.copy()
    ziekenhuis.mask(mask_image)
    
    muur_masked = muur.copy()
    muur.mask(mask_image)
    
    speciaal_masked = speciaal.copy()
    speciaal.mask(mask_image)
    
    tunnel_masked = tunnel.copy()
    tunnel.mask(mask_image)
    
def draw():
    #de afbeelding van het spel in het midden van het scherm en de 
    #achtergrond over heel het scherm
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
            elif col == -4: # Muur
                image(muur_masked, x, y)
            elif col == -5: # Speciaal
                image(speciaal_masked, x, y)
            elif col == -6: # Tunnel
                image(tunnel_masked, x, y)
            else: # Leeg
                fill(255)
                rect(x,y,w,w)
            x = x + w
        y = y + w
        x = 75
