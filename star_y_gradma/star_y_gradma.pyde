t=1
g=1
def setup():
    size(600,600)
    frameRate(10)
    stroke(251,255,0)
def draw():
    global t
    global g
    clear()
    background(255,255,255)
    strokeWeight(t)
    line(300,215,325,450)
    line(325,450,200,300)
    line(200,300,400,300)
    line(400,300,275,450)
    line(275,450,300,215)
    t=t+g
