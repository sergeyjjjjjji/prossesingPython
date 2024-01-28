c=0
r=0
j=0
f=5
n=0
def setup():
    size(600,600)
def draw():
    global r,c,f,n
    stroke(c,c,c)
    frameRate(f)
    rect(0,0,100,100)
    rect(250,0,100,100)
    rect(500,0,100,100)
    strokeWeight(23)
    point(c,f)
    if mousePressed==True:
        
        if mouseX>0 and mouseY>0 and mouseX<100 and mouseY<100 :
            r=0
        if mouseX>250 and mouseY>0 and mouseX<350 and mouseY<350:
            r=1
        if mouseX>500 and mouseY>0 and mouseX<600 and mouseY<600:
            r=2
    if r==0:
        c=c+1
    if r==1:
        f=f+1
    if r==2:
        noLoop()
