y=50
g=1
x=50
h=550
d=50
j=550
w=550
s=50
c=550
i=-1
def setup():
    size(600,600)
def draw():
    global y
    global g
    global x
    global h
    global d
    global i
    global j
    global w
    global s
    global c
    clear()
    background(255,255,255)
    strokeWeight(random(100))
    stroke(random(255),random(255),random(255))
    ellipse(h,d,random(100),random(100))
    ellipse(j,w,random(100),random(100))
    ellipse(x,y,random(100),random(100))
    ellipse(s,c,random(100),random(100))
    y=y+g
    x=x+g
    h=h+i
    d=d+g
    j=j+i
    w=w+i
    s=s+g
    c=c+i
    if y==250:
        g=-1
        y=y+g
        ellipse(x,y,random(100),random(100))
    if y==50:
        g=1
        y=y+g
        ellipse(x,y,random(100),random(100))
    if x==250:
        g=-1
        x=x+g
        ellipse(x,y,random(100),random(100))
    if x==50:
        g=1
        y=y+g
        ellipse(x,y,random(100),random(100))
    if h==350:
        i=1
        h=h+i
        ellipse(h,d,random(100),random(100))
    if h==550:
        i=-1
        h=h+i
        ellipse(h,d,random(100),random(100))
    if d==350:
        g=-1
        d=d+g
        ellipse(h,d,random(100),random(100))
    if d==50:
        g=1
        d=d+g
        ellipse(h,d,random(100),random(100))
    if j==350:
        i=1
        j=j+i
        ellipse(j,w,random(100),random(100))
    if j==550:
        i=-1
        j=j+i
        ellipse(j,w,random(100),random(100))
    if w==350:
        i=1
        w=w+i
        ellipse(j,w,random(100),random(100))
    if w==550:
        i=-1
        w=w+i
        ellipse(j,w,random(100),random(100))
    if c==250:
        i=1
        c=c+i
        ellipse(s,c,random(100),random(100))
    if c==550:
        i=-1
        c=c+i
        ellipse(s,c,random(100),random(100))
    if s==250:
        g=-1
        s=s+g
        ellipse(s,c,random(100),random(100))
    if s==50:
        g=1
        s=s+g
        ellipse(s,c,random(100),random(100))
    
