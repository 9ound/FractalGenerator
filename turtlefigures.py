#####################################################################
#                       Conor Muldowney                             #
#                       Student 109424130                           #
#                 turtle_figure Recursive Functions                 #
#####################################################################

'''
This module comprises of 10 recursive functions of which:
5 are circle based (revolver, circle, sun, biohazard, moreCircles)
2 sierpinski based (cross, sierpinski)
1 is a mixture of hexagon and circle (hexCircles)
1 binary tree (tree)
1 fern (fern)
'''
def revolver(n, l, pen):

    if n==0 or l<2 :
        return 0
    pen.left(90)
    pen.up()
    pen.forward(l-l/3)
    pen.right(90)
    pen.down()
    nr1 = revolver(n-1, l/3, pen)

    for i in range (4):
        pen.circle(l/3, 90)
        nr2 = revolver(n-1, -l/7, pen)
        pen.circle(-l/7.3)

    pen.left(90)
    pen.up()
    pen.backward(l-l/3)
    pen.right(90)
    pen.down()
    
    pen.circle(l, 45)
    nr3 = revolver(n-1, l/3, pen)
    pen.circle(l, 90)
    nr4 = revolver(n-1, l/3, pen)
    pen.circle(l, 90)
    nr5 = revolver(n-1, l/3, pen)
    pen.circle(l, 90)
    nr6 = revolver(n-1, l/3, pen)
    pen.circle(l, 45)

    return (nr1 + nr2 + nr3 + nr4 + nr5 + nr6 + 1)
  
def tree(n, l, pen):
     if n==0 or l<2 :
          return 0
     #endif
     pen.forward(l)
     pen.left(45)
     nr1 = tree(n-1, l/2, pen)
     pen.right(90)
     nr2 = tree(n-1, l/2, pen)
     pen.left(45)
     pen.backward(l)
     return (nr1 + nr2 + 1)

def circle(n, l, pen):
     if n==0 or l<2 :
          pen.circle(l)
          return 0
     
     pen.circle(l)
     nr1 = circle(n-1, l/2, pen)
     pen.left(90)
     pen.up()
     pen.forward(l)
     pen.right(90)
     pen.down()
     
     nr2 = circle(n-1, l/2, pen)
     pen.up()
     pen.forward(l)
     pen.left(90)
     pen.down()

     nr3 = circle(n-1, l/3, pen)
     pen.up()
     pen.right(90)
     pen.backward(2*l)
     pen.right(90)
     pen.down()
     
     nr4 = circle(n-1, l/3, pen)
     pen.up()
     pen.left(90)
     pen.forward(l)
     pen.left(90)
     pen.backward(l)
     pen.right(90)

     return (nr1 + nr2 + nr3 + nr4 + 1)

def cross(n, l, pen):
    if n==0:
        pen.forward(l)
        return 0
    nr1 = cross(n-1, l/2, pen)
    pen.left(85)
    nr2 = cross(n-1, l/2, pen)
    pen.right(170)
    nr3 = cross(n-1, l/2, pen)
    pen.left(85)
    nr4 = cross(n-1, l/2, pen)

    return (nr1 + nr2 + nr3 + nr4 + 1) 
        

def sun(n, l, pen):
     if n==0 or l<2 :
          pen.circle(l/2)
          return 0

     nr1 = sun(n-1, 2*(l/3), pen)
     pen.up()
     pen.circle(l-l/3, 180)
     pen.right(180)
     pen.down()
     nr2 = sun(n-1, l/3, pen)

     pen.up()
     pen.right(180)
     pen.circle(l-l/3, 360/10)
     pen.down()
     pen.right(180)
     nr3 = sun(n-1, l/3.5, pen)
     
     pen.up()
     pen.right(180)
     pen.circle(l-l/3, 360/12)
     pen.right(180)
     pen.down()
     nr4 = sun(n-1, l/5, pen)

     pen.up()
     pen.right(180)
     pen.circle(l-l/3, 360/16)
     pen.right(180)
     pen.down()
     nr5 = sun(n-1, l/7.5, pen)

     pen.up()
     pen.right(180)
     pen.circle(l-l/3, 360/22)
     pen.right(180)
     pen.down()
     nr6 = sun(n-1, l/11, pen)

     pen.up()
     pen.right(180)
     pen.circle(l-l/3, 360/30)
     pen.right(180)
     pen.down()
     nr7 = sun(n-1, l/15, pen)

     pen.up()
     pen.right(180)
     pen.circle(l-l/3, 360/40)
     pen.right(180)
     pen.down()
     nr8 = sun(n-1, l/20, pen)

     pen.up()
     pen.right(180)
     pen.circle(l-l/3, 360/53)
     pen.right(180)
     pen.down()
     nr9 = sun(n-1, l/27, pen)

     pen.up()
     pen.right(180)
     pen.circle(l-l/3, 360/69)
     pen.right(180)
     pen.down()
     nr10 = sun(n-1, l/34, pen)

     pen.up()
     pen.right(180)
     pen.circle(l-l/3, 360/83)
     pen.right(180)
     pen.down()
     nr11 = sun(n-1, l/43, pen)

     pen.up()
     pen.right(180)
     pen.circle(l-l/3, 70.5-((360/22)+(360/53)+(360/69)+(360/83)))

     return (nr1 + nr2 + nr3 + nr4 + nr5 + nr6 + nr7 + nr8 + nr9 + nr10 + nr11 + 1)

def biohazard(n, l, pen):
     if n==0 or l<2 :
          pen.circle(l)
          return 0
     pen.circle(l)
     pen.up()
     pen.circle(l, 60)
     pen.down()
     nr1 = biohazard(n-1, 7.43*l/16, pen)

     pen.up()
     pen.circle(7.43*l/16, 180)
     pen.right(180)
     pen.down()
     nr2 = biohazard(n-1, 1.14*l/16, pen)
     pen.up()
     pen.right(180)
     pen.circle(7.43*l/16, 180)
     pen.circle(l, 120)
     pen.down()
     nr3 = biohazard(n-1, 7.43*l/16, pen)
     pen.up()
     pen.circle(l, 120)
     pen.down()
     nr4 = biohazard(n-1, 7.43*l/16, pen)
     pen.up()
     pen.circle(l, 60)
     pen.down()

     return (nr1 + nr2 + nr3 + nr4 + 1)

def sierpinski(n, l, pen):
    if n==0 or l<2:
        return 0
    
    nr1 = sierpinski(n-1, l/2, pen)
    pen.forward(l/2)
    nr2 = sierpinski(n-1, l/2, pen)
    pen.forward(l/2)
    pen.left(120)
    pen.forward(l/2)
    nr3 = sierpinski(n-1, l/2, pen)
    pen.forward(l/2)
    pen.left(120)
    pen.forward(l)
    pen.left(120)

    return (nr1 + nr2 + nr3 + 1)

def moreCircles(n, l, pen):
    if n==0 or l<2:
        return 0
    for i in range(8):
        pen.circle(l, 45)
        pen.circle(l/4)
    pen.up()
    pen.left(90)
    pen.forward(l/2)
    pen.right(90)
    pen.down()
    nr1 = moreCircles(n-1, l/2, pen)
    pen.up()
    pen.left(90)
    pen.backward(l/2)
    pen.right(90)
    pen.down()

    return (nr1 + 1)

def hexCircles(n, l, pen):
    if n==0 or l<2:
        return 0
    for i in range(6):
        pen.circle(l/6.9)
        pen.forward(l/4)
        pen.left(60)
        pen.forward(l/4)
    pen.up()
    pen.left(90)
    pen.forward(l/3.45)
    pen.right(90)
    pen.down()

    nr1 = hexCircles(n-1, l/3, pen)

    return (nr1 + 1)

def fern(n,l, pen):
    if n==0 or l<2:
        return 0
    
    pen.forward(0.3*l)
    pen.left(55)
    nr1 = fern(n-1, l/2, pen)
    pen.right(55)
    pen.forward (0.7*l);
    pen.right(40);
    nr2 = fern(n-1, l/2, pen)
    pen.left(40)
    pen.forward(l);
    pen.left(5)
    nr3 = fern(n-1, 0.8*l, pen)
    pen.right(5)
    pen.backward(2*l);

    return nr1 + nr2 + nr3 + 1


