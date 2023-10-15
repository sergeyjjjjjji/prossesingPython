
def setup():
    size(600,400)
    frameRate(3)
def draw():
    clear()
    strokeWeight(20)
    ellipse(300,200,400,400)
    line(300,200,random(200 and 400),random(400))
    line(300,200,random(250 and 350),random(150 and 350))
