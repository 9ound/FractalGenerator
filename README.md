========================== Conor's Fractal Generator ============================

======== A desktop application to draw fractals using recursive functions =======

		*****turtle_figures.py*****

Turtle figures contains ten recursive functions:

Revolver is comprised of 6 circles and resembles the cylinder of a pistol.

Circles is comprised of 4 tangent circles encased in a larger circle.

Cross is a similar to Sierpinski's triangle except comprised of crosses.

Sun is more complex and is comprised of 11 circles that orbit a larger circle.

Biohazard is comprised of 4 tangent circles encased in a larger circle that resembles a biological hazard sign.

More Circles resembles the cylinder of a pistol except with more circles.

Hexes and Circles is comprised of 6 circles encased in a hexagon.

Tree is a basic binary tree.

Fern is a basic fern fractal.

Sierpinski is Sierpinski's triangle fractal.


		*****ConorMuldowney.py*****

ConorMuldowney.py is an interface where the user can manipulate the functions imported from turtle_figures.
The goal was to provide an interface that integrated the canvas and all associated widgets in one window.
The main issues encountered were preventing the turtle module from opening a new canvas when executing 
certain methods colormode(), pen(), screen(), clearscreen(), resetscreen()

The interface window and canvas automatically resizes depending if the screen width is less than or greater than 1400px. 

The interface provides the ability to:

 - Draw: Draws a selected function from the turtle_figures module. 

The amount of recursions can be increased or decreased by the user.
***For best results the user should not exceed an order number of 9***

The drawing can be scaled in relation to the length of the shapes chosen by the user the length entry field.
***For best results the user should not to exceed a length of 400 on a 1080px screen or 800 on a 2040px screen***

 - Clear: Clears the "order" and "length" fields

 - Wipe: Resets the canvas to white. Issues may occur when drawing the subsequent fractal after cleaning the canvas.
Canvas sometimes doesn't register the initial lines drawn by RawTurtle after wiping.

 - Quit: Quits the app

 - Pen Colour: The pen colour can be adjusted using the R, G and B sliders.
After choosing red, green and blue values the user should click the "Change Pen Color" in order to change the colour.
Pen color can be changed ant any time during the drawing process. 
*Because of issues with colormode() the RGB values had to be passed as a 6 digit alphanumeric hex string.
As a result the sliders range from 16-255. If any slider value was below 16 it would return a 5 digit alphanumeric hex.

 - Window Color: The user has the option to change the color of the interface window by clicking the "Window Color" button. 
The Window is initially orange but randomly generates a new background color each time the button is pressed. 
*Without the use of colormode() background color took a hex string value.

- Description box: The interface displays information about each fractal after draw function has been executed.

- Change Pen Direction: There is an option to change the direction of the pen by using the Change Direction slider. In order to initialise the direction the user has chosen the "Change Direction" button needs to be clicked. 
Direction can be changed at any time during the drawing process however it will affect the fractal if orientation is changed fractal is being drawn.

- Change Pen Speed: The speed of the pen can be chosen via the dropdown menu and initialising the choice with the "Change Speed" button. 
Speed can be changed ant any time during the drawing process.




 


