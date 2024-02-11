def setup():
    size(600,600)
def draw():
    strokeWeight(25)
    if keyPressed:
        if key=="r":
            rect(random(0,600),random(0,600),50,50)
        if key=="t":
            triangle(random(0,600),random(0,600),random(0,600),random(0,600),random(0,600),random(0,600))
        if key=="p":
            point(random(0,600),random(0,600))
        
