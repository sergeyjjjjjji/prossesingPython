x=300
y=300
g=10
n=0
def setup():
    size(600,600)
def draw():
    global x,y,g
    clear()
    background(255,255,255)
    strokeWeight(40)
    stroke(0,0,0)
    point(x,y)
    x=x+g
    y=y+g
    if x==600 and y==600:
        g=-10
        x=x+g
        y=y+g
        point(x,y)
    if x==0 and y==0:
        g=10
        x=x+g
        y=y+g
        point(x,y)
    if mousePressed==True:
        background(50,40,200)
    else:
        background(255,255,255)
