x=1
y=1
g=1
def setup():
    size(600,600)
    strokeWeight(10)
def draw():
    global x
    global y
    global g
    clear()
    background(255,255,255)
    rect(200,200,x,y)
    x=x+g
    y=y+g
    if x>100 and y>100:
        g=-1
        x=x+g
        y=y+g
        rect(200,200,x,y)
    if x==1 and y==1:
        g=1
        x=x+g
        y=y+g
        rect(200,200,x,y)
