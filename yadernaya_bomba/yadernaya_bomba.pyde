t=1
g=10
def setup():
    size(600,600)
    frameRate(2)
def draw():
    global t
    global g
    strokeWeight(t)
    point(300,300)
    t=t+g
    if t==650:
        noLoop()
