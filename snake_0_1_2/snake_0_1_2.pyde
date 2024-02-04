x=0
y=0
def setup():
    size(600,600)
def draw():
    global x,y
    clear()
    background(255,255,255)
    rect(x,y,100,100)
    if keyPressed:
        if keyCode==UP:
            y=y-1
        if keyCode==LEFT:
            x=x-1
        if keyCode==DOWN:
            y=y+1
        if keyCode==RIGHT:
            x=x+1
    
    
    
    
    
    
    
