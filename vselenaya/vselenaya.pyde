x=650
y=650
g=-10
def setup():
    size(600,600)
    frameRate(2)
def draw():
    global x
    global y
    global g
    clear()
    background(255,255,255)
    strokeWeight(10)
    stroke(random(255),random(255),random(255))
    ellipse(300,300,x,y)
    y=y+g
    x=x+g
