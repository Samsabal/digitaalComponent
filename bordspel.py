
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
    global template_image, ziekenhuis_masked, muur_masked, speciaal_masked, tunnel_masked, leeg_masked, westBerlijn_masked, oostBerlijn_masked, muur
    muur = loadImage("Images/muur.png")
    muur.resize(600,600)
    
    leeg = loadImage("Images/leeg.jpg")
    leeg.resize(w,w)
    
    westBerlijn = loadImage("Images/west-berlijn.jpg")
    westBerlijn.resize(w,w)
    
    oostBerlijn = loadImage("Images/oost-berlijn.jpg")
    oostBerlijn.resize(w,w)
    
    template_image = loadImage("Images/template.jpg")
    template_image.resize(750,750)
    
    ziekenhuis = loadImage("Images/ziekenhuis.jpg") 
    ziekenhuis.resize(w,w)
    
    speciaal = loadImage("Images/speciaal.jpg")
    speciaal.resize(w,w)
    
    tunnel = loadImage("Images/tunnel.jpg")
    tunnel.resize(w,w)
    
    # Maak mask
    mask_image = createGraphics(ziekenhuis.width,ziekenhuis.height)
    mask_image.beginDraw()
    mask_image.rect(0, 0, w, w)
    mask_image.endDraw()
    
    # Maak kopieen van masks
    ziekenhuis_masked = ziekenhuis.copy()
    ziekenhuis.mask(mask_image)
    
    speciaal_masked = speciaal.copy()
    speciaal.mask(mask_image)
    
    tunnel_masked = tunnel.copy()
    tunnel.mask(mask_image)
    
    leeg_masked = leeg.copy()
    leeg.mask(mask_image)
    
    westBerlijn_masked = westBerlijn.copy()
    westBerlijn.mask(mask_image)
    
    oostBerlijn_masked = oostBerlijn.copy()
    oostBerlijn.mask(mask_image)
    
    leeg_masked = leeg.copy()
    leeg.mask(mask_image)
    
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
    tint(255, 255)
    
    x,y = 75,30 # Waar de grid begint op de X en Y as
    
    fill(0)
    rect(x, y, 599, 599)
    
    for row in grid:
        for col in row:
            if col == -1: # West-Berlijn
                image(westBerlijn_masked, x, y)
            elif col == -2: # Oost-Berlijn
                image(oostBerlijn_masked, x, y)
            elif col == -3: # Ziekenhuis
                image(ziekenhuis_masked, x, y)
            elif col == -5: # Speciaal
                image(speciaal_masked, x, y)
            elif col == -6: # Tunnel
                image(tunnel_masked, x, y)
            else: # Leeg
                image(leeg_masked, x, y)    
            x = x + w
        y = y + w
        x = 75
    
    image(muur, 75, 30)
    
        
