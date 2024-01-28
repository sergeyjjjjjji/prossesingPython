c=0
r=10
def setup():
    size(600,600)
def draw():
    global c,r
    clear()
    background(255,255,255)
    strokeWeight(r)
    stroke(c,0,0)
    point(300,300)
    if mouseX>200 and mouseY>200 and mouseX<400 and mouseY<400 and mousePressed==True:
        r=r+2
        c=c+1
    if r>600:
        clear()
        noLoop()
        
