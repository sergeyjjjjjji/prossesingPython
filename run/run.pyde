def setup():
    size(600,600)
    frameRate(1)
def draw():
    clear()
    background(255,255,255)
    if key=="r":
        rotate(radians(30))
    line(300,300,400,300)
    line(300,300,300,400)
    line(300,300,400,400)
    line(400,400,400,300)
    line(400,400,300,400)
