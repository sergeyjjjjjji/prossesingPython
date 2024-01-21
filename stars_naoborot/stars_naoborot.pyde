
def setup():
    size(600,400)
    background(0,0,0)
def draw():
    stroke(random(106),random(27),random(99))
    strokeWeight(random(5))
    point(random(650),random(640))
    if mousePressed==True:
        stroke(random(106),random(27),random(99))
        strokeWeight(random(5))
        point(random(650),random(640))
    else:
        clear()

    
