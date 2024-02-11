x=300
y=300
g=1
def setup():
    size(600,600)
def draw():
    rect(random(0,600),random(0,600),50,50)
    if key=="1":
        fill(255,0,0)
        rect(random(0,600),random(0,600),50,50)
    if key=="2":
        fill(0,255,0)
        rect(random(0,600),random(0,600),50,50)
    if key=="3":
        fill(0,0,255)
        rect(random(0,600),random(0,600),50,50)
    if key=="4":
        fill(255,0,255)
        rect(random(0,600),random(0,600),50,50)
    if key=="5":
        fill(0,255,255)
        rect(random(0,600),random(0,600),50,50)
    if key=="6":
        fill(255,255,0)
        rect(random(0,600),random(0,600),50,50)
    if key=="7":
        fill(255,122,0)
        rect(random(0,600),random(0,600),50,50)
    if key=="8":
        fill(122,0,255)
        rect(random(0,600),random(0,600),50,50)
        
