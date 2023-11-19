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
    if mouseX>200 and mouseX<400 and mouseY>200 and mouseY<300 and mousePressed==True:
        stroke(random(255),random(255),random(255))
    if mouseX>200 and mouseX<400 and mouseY>100 and mouseY<200 and mousePressed==True:
        i=random(100)
    if mouseX>200 and mouseX<400 and mouseY>0 and mouseY<100 and mousePressed==True:
        clear()
        background(255,255,255)
