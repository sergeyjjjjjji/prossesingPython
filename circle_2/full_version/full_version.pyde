y=50
g=1
def setup():
    size(600,400)
    strokeWeight(50)
def draw():
    global y
    global g
    clear()
    background(255,255,255)
    point(50,y)
    y=y+g
    if y==350:
        g=-1
        y=y+g
        point(50,y)
    if y==50:
        g=1
        y=y+g
        point(50,y)
