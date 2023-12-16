y=450
t=350
g=250
j=150
c=-10
def setup():
    size(600,600)
def draw():
    global y,t,g,j,c
    clear()
    background(255,255,255)
    stroke(142,103,20)
    fill(142,103,20)
    rect(275,y,50,100)
    stroke(20,142,43)
    fill(20,142,43)
    triangle(200,y,300,t,400,y)
    triangle(200,t,300,g,400,t)
    triangle(200,g,300,j,400,g)
    stroke(255,0,0)
    strokeWeight(15)
    line(340,475,390,475)
    line(340,490,390,490)
    line(340,505,390,505)
    stroke(255,235,3)
    strokeWeight(20)
    point(365,490)
    stroke(247,217,217)
    strokeWeight(65)
    point(75,250)
    stroke(255,0,0)
    strokeWeight(5)
    line(50,250,75,275)
    line(75,275,100,250)
    stroke(0,0,0)
    point(60,235)
    point(90,235)
    stroke(19,229,234)
    fill(19,229,234)
    strokeWeight(15)
    rect(45,282,65,150)
    triangle(45,218,77,186,110,218)
    line(30,282,30,382)
    line(125,282,125,382)
    strokeWeight(25)
    line(45,442,45,542)
    line(110,442,110,542)
    line(110,542,130,542)
    line(45,542,25,542)
def mouseClicked():
    global y,t,g,j,c
    y=y+c
    t=t+c
    g=g+c
    j=j+c
    stroke(255,255,255)
    rect(340,475,50,50)
