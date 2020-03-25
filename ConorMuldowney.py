#####################################################################
#                       Conor Muldowney                             #
#                       Student 109424130                           #
#                   Tkinter Turtle Fractals                         #
#####################################################################

from tkinter import *
#from tkinter.ttk import *
from turtle import RawTurtle, clearscreen
import turtlefigures
import random



#===================== SET UP TK WIN ACCORDING TO SCREENSIZE =====================# 
root = Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.title("Fractal Interface")

#print("Screen width = " + str(screen_width))
#print("Screen height = " + str(screen_height))

if screen_width < 1400:
    root.geometry("1300x800+300+300")
else:
    root.geometry("2000x1500+300+300")

label = Label(root, text = "Conor's Fractal Generator")
label.grid(row = 0, column = 0, columnspan = 4)

root.configure(background="#f08010")



#================ SET UP AND PLACE CANVAS IN FRAME ACCORDING TO SCREENSIZE ================#
if screen_width < 1400:
    cvFrame = LabelFrame(root, text = "Canvas Compact Space", width = 600, height = 600)
    cvFrame.grid(row = 1, column = 0, ipadx = 2, ipady = 2, padx =5, pady =5, columnspan = 4, rowspan = 4)

    cv = Canvas(cvFrame, width = 850, height = 650)
    cv.pack()

else:
    cvFrame = LabelFrame(root, text = "Canvas Extended Space", width = 910, height = 910)
    cvFrame.grid(row = 1, column = 0, ipadx = 2, ipady = 2, padx =5, pady =5, columnspan = 4, rowspan = 4)

    cv = Canvas(cvFrame, width = 1000, height = 1000)
    cv.pack()
    #end canvas



#parameter frame
paramFrame = LabelFrame(root, text = "Parameters")
paramFrame.grid(row = 1, column = 4, columnspan = 2, ipadx = 2, ipady = 2, padx = 5, pady = 5)
#end paramFrame



#text Frame and Widget
txtFrame = LabelFrame(root, text = "Fractal Description", width = 175, height = 300)
txtFrame.grid(row = 3,column = 4, ipadx = 2, ipady = 2, padx = 5, pady = 5)

text = Text(txtFrame, width = 30, height = 15)
text.pack()
#end txtFrame + Widget



#RGB frame
RGBframe = LabelFrame(root, text = "Pen Color")
RGBframe.grid(row = 2 ,column = 4, ipadx = 2, ipady = 2, padx = 5, pady = 5)



#Pen Orientation Frame
orientFrame = LabelFrame(root, text = "Pen Direction")
orientFrame.grid(row = 2 ,column = 6)

#RawTurtle defines obj to draw on TurtleScreen takes (Canvas, ScrolledCanvas or TurtleScreen)
pen = RawTurtle(cv)


#create shape names and index for dropdown menu
shapes = ["Revolver", "Tree", "Circle", "Cross", "Sun", "Biohazard", "Sierpinksi", "More Circles", "Hexes and Circles", "Fern"]
shapesIndex = 0


#create pen speeds and index for dropdown
speed = ["Fastest", "Medium", "Slowest"]
speedIndex = 0


#define initial pen speed and color
pen.speed(0)
pen.color('#0f0f0f')

root.update()

#end win setup



#========================== HANDLERS =============================#

def onChangeColorF():
    #randomizes window background color
    
    r = random.randint(0, 255)
    red = str(hex(int(r)))[2:]  #forces r as a string hex value minus '0x'
    if len(red) < 2:            #hex val needs to be 6 alphanumeric
        return
        red = '0f'
    else:
        red = str(hex(int(r)))[2:]
    #end if else

    
    g = random.randint(0, 255)
    green = str(hex(int(g)))[2:]
    if len(green) < 2:
        return
        green = '0f'
    else:
        green = str(hex(int(g)))[2:]
    #end if else

        
    b = random.randint(0, 255)
    blue = str(hex(int(b)))[2:]
    if len(blue) < 2:
        return
        blue = '0f'
    else:
        blue = str(hex(int(b)))[2:]
    #end if else

        
    root.configure(background='#'+ (red) + (green) + (blue)) #concats rgb values to single hex string

    root.update()
    #end randomized background color


    
def onResetCanvasF():
    #creates white rectangle over previous figures on canvas and shows pen afterwards 

    cv.create_rectangle(-1000, -1000, 2000, 2000, fill="white")

    pen.st()
    root.update()


def onClearF():
    #clear entries

    orderEntry.delete(0, 'end')
    lengthEntry.delete(0, 'end')

    root.update()

def penSpeedF():

    #create index for speed in dropdown list
    speedIndex = speed.index(speedDropDownStr.get())

#=================== GET SPEED VALUES FROM speedDropDown ===============#
    
    if speedIndex == 0:

        pen.speed(0)

    elif speedIndex == 1:

        pen.speed(8)

    elif speedIndex == 2:

        pen.speed(3)

        root.update()
    
def onDrawF():
    
    #create index for shapes in dropdown list
    shapesIndex = shapes.index(shapeDropDownStr.get())

    #get the value from orderEntry and make int
    orderValue = int(orderEntry.get())

    #get the value from lengthEntry and make int
    lengthValue = float(lengthEntry.get())

    root.update()
    

    #======================= CALL VALUES FROM turtle_fractals =============================#

    if shapesIndex == 0:

        pen.st()

        pen.up(); pen.left(90); pen.backward(lengthValue); pen.right(90)
        pen.down()
        
        line = turtlefigures.revolver(orderValue, lengthValue, pen)

        pen.up(); pen.home(); pen.down()

        pen.ht()

        text.delete('1.0', END)
        text.insert(INSERT, "Revolver Fractal: \n\nBasic circle based recursive \nfractal resembling the \ncylinder of a revolver\n\nAmount of recursions: " + str(line))
        #print("Revolver Complete")

    elif shapesIndex == 1:

        pen.st()

        pen.up(); pen.backward(lengthValue); pen.down()
        
        line = turtlefigures.tree(orderValue, lengthValue, pen)

        pen.up(); pen.home(); pen.down()
        
        pen.ht()

        text.delete('1.0', END)
        text.insert(INSERT, "Tree Fractal: \n\nBasic tree based \nrecursive fractal.\n\nAmount of recursions: " + str(line))
        #print("Tree Complete")

    elif shapesIndex == 2:

        pen.up(); pen.left(90)
        pen.backward(lengthValue); pen.right(90)
        pen.down()
        
        pen.st()

        line = turtlefigures.circle(orderValue, lengthValue, pen)

        pen.up(); pen.home(); pen.down()
        
        pen.ht()

        text.delete('1.0', END)
        text.insert(INSERT, "Circle Fractal: \n\nBasic circle based \nrecursive fractal.\n\nAmount of recursions: " + str(line))
        #print("Circle Complete")

    elif shapesIndex == 3:

        pen.up(); pen.backward(lengthValue/2); pen.down()
        
        pen.st()
        
        line = turtlefigures.cross(orderValue, lengthValue, pen)

        pen.up(); pen.home(); pen.down()

        pen.ht()

        text.delete('1.0', END)
        text.insert(INSERT, "Sierpinksi Cross: \n\nSierpinksi based recursive \nfractal made of crosses.\n\nAmount of recursions: " + str(line))
        #print("Wheel Complete")

    elif shapesIndex == 4:

        pen.up(); pen.left(90)
        pen.backward(lengthValue); pen.right(90)
        pen.down()

        pen.st()
        
        line = turtlefigures.sun(orderValue, lengthValue, pen)

        pen.up(); pen.home(); pen.down()

        pen.ht()

        text.delete('1.0', END)
        text.insert(INSERT, "Sun Fractal: \n\nCircle based recursive fractal\n\nAmount of recursions: " + str(line))
        #print("Sun Complete")
        
    elif shapesIndex == 5:
        
        pen.up(); pen.left(90)
        pen.backward(lengthValue); pen.right(90)
        pen.down()

        pen.st()
        
        line = turtlefigures.biohazard(orderValue, lengthValue, pen)

        pen.up(); pen.home(); pen.down()

        pen.ht()

        text.delete('1.0', END)
        text.insert(INSERT, "Biohazard Fractal: \n\nCircle based recursive \nfractal.\n\nAmount of recursions: " + str(line))
        #print("Biohazard Complete")
        
    elif shapesIndex == 6:

        pen.up(); pen.backward(lengthValue/2); pen.down()

        pen.st()
        
        line = turtlefigures.sierpinski(orderValue, lengthValue, pen)

        pen.up(); pen.home(); pen.down()

        pen.ht()

        text.delete('1.0', END)
        text.insert(INSERT, "Serpinski Fractal: \n\nTriangle based recursive \nfractal.\n\nAmount of recursions: " + str(line))
        #print("Sierpinski Complete")

    elif shapesIndex == 7:

        pen.st()

        pen.up(); pen.left(90); pen.backward(lengthValue)
        pen.right(90); pen.down()
        
        line = turtlefigures.moreCircles(orderValue, lengthValue, pen)

        pen.up(); pen.home(); pen.down()

        pen.ht()

        text.delete('1.0', END)
        text.insert(INSERT, "More Circles Fractal: \n\nCircle based recursive \nfractal\n\nAmount of recursions: " + str(line))
        #print("More Circles Complete")

    elif shapesIndex == 8:

        pen.st()

        pen.up(); pen.left(90); pen.backward(lengthValue/2.4)
        pen.right(90); pen.down()
        
        line = turtlefigures.hexCircles(orderValue, lengthValue, pen)

        pen.up(); pen.home(); pen.down()
        
        pen.ht()

        text.delete('1.0', END)
        text.insert(INSERT, "Hexes and Circles Fractal: \n\nBasic circle based recursive \nfractal\n\nAmount of recursions: " + str(line))
        #print("hexCircles Complete")

    elif shapesIndex == 9:

        pen.st()

        pen.up(); pen.backward(lengthValue); pen.down()
        
        line = turtlefigures.fern(orderValue, lengthValue/2, pen)

        pen.up(); pen.home(); pen.down()
        
        pen.ht()

        text.delete('1.0', END)
        text.insert(INSERT, "Fern Fractal: \n\nBasic fern based recursive \nfractal\n\nAmount of recursions: " + str(line))
        #print("hexCircles Complete")


        root.update()

def onShowTurtleF():
    #shows pen

    pen.st()
    root.update()


def onHideTurtleF():
    #hides pen

    pen.ht()
    root.update()

def changeDirF():
    
    pen.setheading(changeDir.get())
    root.update()

def resetOrientation():

    pen.setheading(0)
    root.update()

def onPenColorF():
    '''
    Get color values from sliders in range 16.0-255.0 and force as valid input for pen.color()
    pen.color takes "colorstring" or "#ffffff" as arg. 
    Unable to use turtle.colormode() as it would create new canvas outside of tkinter win
    '''

    #RED VALUE
    redValue = str(hex(int(redSlider.get())))[2:] #force hex str value and remove first 2 chars '0x'
    if len(redValue) < 2:
        return
        redValue = _  #returns previous value
    else:
        redValue = str(hex(int(redSlider.get())))[2:]

    #GREEN VALUE
    greenValue = str(hex(int(greenSlider.get())))[2:]
    if len(greenValue) < 2:
        return
        greenValue = _
    else:
        greenValue = str(hex(int(greenSlider.get())))[2:]
    
    #BLUE VALUE
    blueValue = str(hex(int(blueSlider.get())))[2:]
    if len(blueValue) < 2:
        return
        blueValue = _
    else:
        blueValue = str(hex(int(blueSlider.get())))[2:]

    pen.color('#' + (redValue) + (greenValue) + (blueValue))
    

    #================== PRINT COLOR VALUES FOR TEST ====================#
    #print('Red = ' + (redValue))
    #print('Blue = ' + (blueValue))
    #print('Green = ' + (greenValue))

    
def onQuitF():
    #quits app
    
    root.destroy()
    root.quit()

    
#========================= MAKE INTERFACE =========================#
orderLabel = Label(paramFrame, width = 10, text = "Order")
orderLabel.grid(row = 1, column =0)

orderStr = StringVar()
orderEntry = Entry(paramFrame, width = 10, textvariable = orderStr)
orderEntry.grid(row = 1, column = 1)

lengthLabel = Label(paramFrame, width = 10, text = "Length")
lengthLabel.grid(row = 2, column =0)

lengthStr = StringVar()
lengthEntry = Entry(paramFrame, width = 10, textvariable = lengthStr)
lengthEntry.grid(row = 2, column = 1)


#shape selection menu
shapeLabel = Label(paramFrame, width = 10, text= "Shapes")
shapeLabel.grid(row = 3, column =0)

shapeDropDownStr = StringVar()
shapeDropDown = OptionMenu(paramFrame, shapeDropDownStr, *shapes)
shapeDropDown.grid(row = 3, column = 1)


#canvas and window buttons: CLEAR, DRAW, WIPE, QUIT
clearButton = Button(paramFrame, text = "Clear", command = onClearF)
clearButton.grid(row = 4, column = 0, rowspan=2)

drawButton = Button(paramFrame, text = "Draw", command = onDrawF, fg="green")
drawButton.grid(row = 4, column = 1, rowspan=2)

wipeButton = Button(paramFrame, text = "Wipe", command = onResetCanvasF)
wipeButton.grid(row = 6, column = 0)

quitButton = Button(paramFrame, text = "Quit", command=onQuitF, fg="red")
quitButton.grid(row = 6, column = 1)


#random background color for the window button
winColorButton = Button(paramFrame, text = "Window Color", command = onChangeColorF)
winColorButton.grid(row = 20, column = 0, columnspan = 3, rowspan=2)


#hide and show pen buttons
showTurtleButton = Button(paramFrame, text = "Show Pen",command = onShowTurtleF)
showTurtleButton.grid(row = 16, column = 0, rowspan=2)

hideTurtleButton = Button(paramFrame, text = "Hide Pen",command = onHideTurtleF)
hideTurtleButton.grid(row = 16, column = 1, rowspan=2)


#============================ onChangeColor value sliders =============================#
redLabel = Label(RGBframe, width = 10, text= "R. Value")
redLabel.grid(row = 1, column = 0)

redSlider = Scale(RGBframe, from_=16, to=255, orient=HORIZONTAL, fg="red")
redSlider.grid(row = 1, column = 1, columnspan=2)

greenLabel = Label(RGBframe, width = 10, text= "G. Value")
greenLabel.grid(row = 2, column = 0)

greenSlider = Scale(RGBframe, from_=16, to=255, orient=HORIZONTAL, fg="green")
greenSlider.grid(row = 2, column = 1, columnspan=2)

blueLabel = Label(RGBframe, width = 10, text= "B. Value")
blueLabel.grid(row = 3, column = 0)

blueSlider = Scale(RGBframe, from_=16, to=255, orient=HORIZONTAL, fg="blue")
blueSlider.grid(row = 3, column = 1, columnspan=2)

#pen color label + button
penColorButton = Button(RGBframe, text ="Change Pen Color", command = onPenColorF)
penColorButton.grid(row = 5, column = 0, columnspan = 3)

#pen direction
changeDir = Scale(orientFrame, from_=0, to=360, orient=HORIZONTAL)
changeDir.grid(row = 0, column = 0, columnspan=2)

changeDirButton = Button(orientFrame, text = "Change Direction",command = changeDirF)
changeDirButton.grid(row = 4, column = 0)

changeDirFooter = Label(orientFrame, text= "")
changeDirFooter.grid(row = 5, column = 0)

#pen speed dropdown + button
speedLabel = Label(orientFrame, width = 10, text= "Pen Speed")
speedLabel.grid(row = 6, column =0)

speedDropDownStr = StringVar()
speedDropDown = OptionMenu(orientFrame, speedDropDownStr, *speed)
speedDropDown.grid(row = 7, column = 0)

changeSpeedButton = Button(orientFrame, text ="Change Speed", command = penSpeedF)
changeSpeedButton.grid(row = 8, column = 0)
root.update()

root.mainloop()

#======================== END ========================# 

