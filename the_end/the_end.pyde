a=5
b=1
def setup():
    size(600,600)
def draw():
    global a,b
    clear()
    background(255,255,255)
    strokeWeight(a)
    point(300,300)
    if key=='b':
        b=1
        a=a+b
    if key=='m':
        b=-1
        a=a+b
