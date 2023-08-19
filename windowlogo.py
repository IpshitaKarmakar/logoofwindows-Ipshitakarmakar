import turtle as t
t.speed(1)    #speed defines as movement of the object in graphics
t.bgcolor("black")    #defining the background color in graphics
t.penup()          #penup function make sure the moving object doenot draw anything on the window to not create any wrong drawing on graphics

t.goto(-50,60)      #goto is used to move the turtle in absolute position. It can change along x axis and y axis.
t.pendown()         #is used to draw anything in the window. It is the default settings in turtle.It is used when penup function is used in the code to stop the graphics.
t.color('#00adef')   #windows color setting in the graphics
t.begin_fill()         #begin_fill is used to call just before drawing a shape to be filled
t.goto(100,100)         #fill the #00adef color along first quadrant
t.goto(100,-100)        #fill the #00adef color along fourth quadrant
t.goto(-50,-60)         #fill the #00adef color along third quadrant
t.goto(-50,60)          #fill the #00adef color along second quadrant

t.end_fill()      #fill the shape after the call begin of begin_fill() function

t.color('black')    #defining color of animated along x axis 
t.goto(15,100)           #fill the black color along  +ve x axis and +ve y axis (first quadrant)
t.color('black')       #defining color of animated along y axis 
t.width(10) #defining the animated width of the black color line in the window logo
t.goto(15,-100)        #fill the black color along  +ve x axis and +ve y axis (fourth quadrant)
t.penup()           #stop the animated black color for not showing any error in output

t.goto(100,0)        #moving the absolute position of logo along +ve x axis 
t.pendown()          #Draw the entire windows logo on the graphics which is written in above code 

t.goto(-100,0)      #moving the absolute position of logo along -ve x axis 
t.mainloop()    #it is a infinite loop that blocks the execution of the code
