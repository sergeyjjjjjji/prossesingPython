import time
y=0
i=second()
def setup():
    size(600,600)
def draw():
    global i
    stroke(255,3,3)
    text(i,200,500)
    rect(200,200,100,100)
    text(y,200,100)
def mouseClicked():
    global y,i
    text(i,200,500)
    if mouseX>200 and mouseX<300 and mouseY>200 and mouseY<300:
        y=y+1
        clear()
    if y>30:
        text('You won',200,600)
    if i>30:
        text('You are loser',200,600)
        
    
