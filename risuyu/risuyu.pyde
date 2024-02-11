x=300
y=300
g=1
def setup():
    size(600,600)
def draw():
    global x,y,g
    strokeWeight(25)
    point(x,y)
    x=x+g
    if x==600:
        g=-1
        x=x+g
    if x==0:
        g=1
        x=x+g
    if keyCode==UP:
        g=-1
        y=y+g
    if keyCode==DOWN:
        g=1
        y=y+g
