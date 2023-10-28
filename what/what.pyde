y=50
g=1
x=50
def setup():
    size(600,600)
def draw():
    global y
    global g
    global x
    strokeWeight(random(100))
    stroke(random(255),random(255),random(255))
    point(x,y)
    y=y+g
    x=x+g
    if y==550:
        g=-1
        y=y+g
        point(x,y)
    if y==50:
        g=1
        y=y+g
        point(x,y)
    if x==550:
        g=-1
        x=x+g
        point(x,y)
    if x==50:
        g=1
        y=y+g
        point(x,y)
    
