x=50
y=50
g=1
l=0
i=0
p=0
r=0
t=0
def setup():
    size(600,600)
    strokeWeight(5)
def draw():
    global x
    global y
    global g
    global l
    global i
    global p
    global r
    global t
    clear()
    background(255,255,255)
    stroke(p,r,t)
    ellipse(x,y,l,i)
    x=x+g
    y=y+g
    l=l+1
    i=i+1
    p=p+1
    r=r+1
    t=t+1
    if x==550 and y==550:
        g=-1
        x=x+g
        y=y+g
        ellipse(x,y,l,i)
    if x==50 and y==50:
        g=1
        x=x+g
        y=y+g
        ellipse(x,y,l,i)
    if l==50 and i==50:
        l=0
        i=0
        ellipse(x,y,l,i)
    if p==255 and r==255 and t==255:
        p=0
        r=0
        t=0
        stroke(p,r,t)
