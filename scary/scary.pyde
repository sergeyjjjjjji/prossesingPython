n=0
m=0
k=0
def setup():
    global n,m,k
    size(700,700)
    n=loadImage("scary.jpg")
    m=loadImage("monster.jpg")
    k=loadImage("kloun.jpg")
def draw():
    global n,m,k
    
    if mousePressed==True and mouseButton==LEFT:
        image(n,0,0)
    if mousePressed==True and mouseButton==CENTER:
        image(k,0,0)
    if mousePressed==True and mouseButton==RIGHT:
        image(m,0,0)
    if mousePressed==False:
        clear()
        
