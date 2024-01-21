x=300
y=300
def setup():
    size(600,600)
def draw():
    global x,y
    clear()
    background(255,255,255)
    strokeWeight(50)
    point(x,y)
    if mousePressed==True:
        clear()
        background(255,255,255)
        point(mouseX,mouseY)
