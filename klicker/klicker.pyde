y=0
def setup():
    size(600,400)
def draw():
    global y
    clear()
    rect(200,200,200,100)
    text(y,200,100)
    if mouseX>200 and mouseX<400 and mouseY>200 and mouseY<300 and mousePressed==True:
        y=y+9888888888888
    
