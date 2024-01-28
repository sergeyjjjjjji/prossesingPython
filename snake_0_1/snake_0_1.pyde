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
        if key=='w':
            y=y-1
        if key=='a':
            x=x-1
        if key=='s':
            y=y+1
        if key=='d':
            x=x+1
    
    
    
    
    
    
    
