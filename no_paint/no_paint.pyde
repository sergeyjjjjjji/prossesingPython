i=5
def setup():
    size(2000,1000)
def draw():
    global i
    rect(200,200,200,100)
    rect(200,100,200,100)
    rect(200,0,200,100)
    strokeWeight(i)
    line(mouseX,mouseY,pmouseX,pmouseY)
    if key=='s' and keyPressed==True:
        stroke(random(255),random(255),random(255))
    if key=='w' and keyPressed==True:
        i=random(100)
    if key=='a' and keyPressed==True:
        clear()
        background(255,255,255)
