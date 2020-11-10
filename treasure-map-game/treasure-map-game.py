
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: N10091378
#    Student name: Sasha Le
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  TREASURE MAP
#
#  This assignment tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "follow_path".  You are required to
#  complete this function so that when the program is run it traces
#  a path on the screen, drawing "tokens" to indicate discoveries made
#  along the way, while using data stored in a list to determine the
#  steps to be taken.  See the instruction sheet accompanying this
#  file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must not rely on any non-standard Python
# modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.

from turtle import *
from math import *
from random import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

grid_size = 100 # pixels
num_squares = 7 # to create a 7x7 map grid
margin = 50 # pixels, the size of the margin around the grid
legend_space = 400 # pixels, the space to leave for the legend
window_height = grid_size * num_squares + margin * 2
window_width = grid_size * num_squares + margin +  legend_space
font_size = 18 # size of characters for the coords
starting_points = ['Top left', 'Top right', 'Centre',
                   'Bottom left', 'Bottom right']

#legend x, y for drawing spiral in legend area
legend_x = (num_squares * grid_size) + margin
legend_y = (num_squares * grid_size) // 2
#Token total list
token_0 = []
token_1 = []
token_2 = []
token_3 = []
token_4 = []
total_token = []
#Storing coordinates for spiral used in token
x_coord = []
y_coord = []
#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.  (Very keen students are welcome
# to draw their own background, provided they do not change the map's
# grid or affect the ability to see it.)
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas():
    
    # Set up the drawing window with enough space for the grid and
    # legend
    setup(window_width, window_height)
    setworldcoordinates(-margin, -margin, window_width - margin,
                        window_height - margin)

    # Draw as quickly as possible
    tracer(False)

    # Choose a neutral background colour (if you want to draw your
    # own background put the code here, but do not change any of the
    # following code that draws the grid)
    bgcolor('tan')

    # Get ready to draw the grid
    penup()
    color('brown')
    width(2)

    # Draw the horizontal grid lines
    setheading(0) # face east
    for y_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        penup()
        goto(0, y_coord)
        pendown()
        forward(num_squares * grid_size)
        
    # Draw the vertical grid lines
    setheading(90) # face north
    for x_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        penup()
        goto(x_coord, 0)
        pendown()
        forward(num_squares * grid_size)

    # Draw each of the labels on the x axis
    penup()
    y_offset = -27 # pixels
    for x_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        goto(x_coord, y_offset)
        write(str(x_coord), align = 'center',
              font=('Arial', font_size, 'normal'))

    # Draw each of the labels on the y axis
    penup()
    x_offset, y_offset = -5, -10 # pixels
    for y_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        goto(x_offset, y_coord + y_offset)
        write(str(y_coord), align = 'right',
              font=('Arial', font_size, 'normal'))

    # Mark the space for drawing the legend
    goto((num_squares * grid_size) + margin, (num_squares * grid_size) // 2)

        

    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing still in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the follow_path function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the random_path function appearing below.  Your
# program must work correctly for any data set that can be generated
# by the random_path function.
#
# Each of the data sets is a list of instructions expressed as
# triples.  The instructions have two different forms.  The first
# instruction in the data set is always of the form
#
#     ['Start', location, token_number]
#
# where the location may be 'Top left', 'Top right', 'Centre',
# 'Bottom left' or 'Bottom right', and the token_number is an
# integer from 0 to 4, inclusive.  This instruction tells us where
# to begin our treasure hunt and the token that we find there.
# (Every square we visit will yield a token, including the first.)
#
# The remaining instructions, if any, are all of the form
#
#     [direction, number_of_squares, token_number]
#
# where the direction may be 'North', 'South', 'East' or 'West',
# the number_of_squares is a positive integer, and the token_number
# is an integer from 0 to 4, inclusive.  This instruction tells
# us where to go from our current location in the grid and the
# token that we will find in the target square.  See the instructions
# accompanying this file for examples.
#

# Some starting points - the following fixed paths just start a path
# with each of the five tokens in a different location

fixed_path_0 = [['Start', 'Top left', 0]]
fixed_path_1 = [['Start', 'Top right', 1]]
fixed_path_2 = [['Start', 'Centre', 2]]
fixed_path_3 = [['Start', 'Bottom left', 3]]
fixed_path_4 = [['Start', 'Bottom right', 4]]

# Some miscellaneous paths which encounter all five tokens once

fixed_path_5 = [['Start', 'Top left', 0], ['East', 1, 1], ['East', 1, 2],
                ['East', 1, 3], ['East', 1, 4]]
fixed_path_6 = [['Start', 'Bottom right', 0], ['West', 1, 1], ['West', 1, 2],
                ['West', 1, 3], ['West', 1, 4]]
fixed_path_7 = [['Start', 'Centre', 4], ['North', 2, 3], ['East', 2, 2],
                ['South', 4, 1], ['West', 2, 0]]

# A path which finds each token twice

fixed_path_8 = [['Start', 'Bottom left', 1], ['East', 5, 2],
                ['North', 2, 3], ['North', 4, 0], ['South', 3, 2],
                ['West', 4, 0], ['West', 1, 4],
                ['East', 3, 1], ['South', 3, 4], ['East', 1, 3]]

# Some short paths

fixed_path_9 = [['Start', 'Centre', 0], ['East', 3, 2],
                ['North', 2, 1], ['West', 2, 3],
                ['South', 3, 4], ['West', 4, 1]]

fixed_path_10 = [['Start', 'Top left', 2], ['East', 6, 3], ['South', 1, 0],
                 ['South', 1, 0], ['West', 6, 2], ['South', 4, 3]]

fixed_path_11 = [['Start', 'Top left', 2], ['South', 1, 0], ['East', 2, 4],
                 ['South', 1, 1], ['East', 3, 4], ['West', 1, 3],
                 ['South', 2, 0]]

# Some long paths

fixed_path_12 = [['Start', 'Top right', 2], ['South', 4, 0],
                 ['South', 1, 1], ['North', 3, 4], ['West', 4, 0],
                 ['West', 2, 0], ['South', 3, 4], ['East', 2, 3],
                 ['East', 1, 1], ['North', 3, 2], ['South', 1, 3],
                 ['North', 3, 2], ['West', 1, 2], ['South', 3, 4],
                 ['East', 3, 0], ['South', 1, 1]]

fixed_path_13 = [['Start', 'Top left', 1], ['East', 5, 3], ['West', 4, 2],
                 ['East', 1, 3], ['East', 2, 2], ['South', 5, 1],
                 ['North', 2, 0], ['East', 2, 0], ['West', 1, 1],
                 ['West', 5, 0], ['South', 1, 3], ['East', 3, 0],
                 ['East', 1, 4], ['North', 3, 0], ['West', 1, 4],
                 ['West', 3, 1], ['South', 4, 1], ['East', 5, 1],
                 ['West', 4, 0]]

# "I've been everywhere, man!" - this path visits every square in
# the grid, with randomised choices of tokens

fixed_path_99 = [['Start', 'Top left', randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['West', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['West', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['West', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)]

# If you want to create your own test data sets put them here
 
#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to assess your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a path
# to follow.  Your program must work for any data set that can be
# returned by this function.  The results returned by calling this
# function will be used as the argument to your follow_path function
# during marking.  For convenience during code development and
# marking this function also prints the path to be followed to the
# shell window.
#
# Note: For brevity this function uses some Python features not taught
# in IFB104 (dictionaries and list generators).  You do not need to
# understand this code to complete the assignment.
#
def random_path(print_path = True):
    # Select one of the five starting points, with a random token
    path = [['Start', choice(starting_points), randint(0, 4)]]
    # Determine our location in grid coords (assuming num_squares is odd)
    start_coords = {'Top left': [0, num_squares - 1],
                    'Bottom left': [0, 0],
                    'Top right': [num_squares - 1, num_squares - 1],
                    'Centre': [num_squares // 2, num_squares // 2],
                    'Bottom right': [num_squares - 1, 0]}
    location = start_coords[path[0][1]]
    # Keep track of squares visited
    been_there = [location]
    # Create a path up to 19 steps long (so at most there will be 20 tokens)
    for step in range(randint(0, 19)):
        # Find places to go in each possible direction, calculating both
        # the new grid square and the instruction required to take
        # us there
        go_north = [[[location[0], new_square],
                     ['North', new_square - location[1], token]]
                    for new_square in range(location[1] + 1, num_squares)
                    for token in [0, 1, 2, 3, 4]
                    if not ([location[0], new_square] in been_there)]
        go_south = [[[location[0], new_square],
                     ['South', location[1] - new_square, token]]
                    for new_square in range(0, location[1])
                    for token in [0, 1, 2, 3, 4]
                    if not ([location[0], new_square] in been_there)]
        go_west = [[[new_square, location[1]],
                    ['West', location[0] - new_square, token]]
                    for new_square in range(0, location[0])
                    for token in [0, 1, 2, 3, 4]
                    if not ([new_square, location[1]] in been_there)]
        go_east = [[[new_square, location[1]],
                    ['East', new_square - location[0], token]]
                    for new_square in range(location[0] + 1, num_squares)
                    for token in [0, 1, 2, 3, 4]
                    if not ([new_square, location[1]] in been_there)]
        # Choose a free square to go to, if any exist
        options = go_north + go_south + go_east + go_west
        if options == []: # nowhere left to go, so stop!
            break
        target_coord, instruction = choice(options)
        # Remember being there
        been_there.append(target_coord)
        location = target_coord
        # Add the move to the list of instructions
        path.append(instruction)
    # To assist with debugging and marking, print the list of
    # instructions to be followed to the shell window
    print('Welcome to the Treasure Hunt!')
    print('Here are the steps you must follow...')
    for instruction in path:
        print(instruction)
    # Return the random path
    return path

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "follow_path" function.
#

# Follow the path as per the provided dataset
#

#Starting coordinates
#
#Find starting coordinates on the map and placing allocated token on the spot
#adding half of the pixels onto num_squares * grid_size will give x,y coordinates
#that place cursor in the center ot the squares



# Go to and places icon at starting spot
def follow_path(path_sequence):

    for path in path_sequence:
            if path[0] == 'Start':
                x, y = 0, 0
                goto(x, y)

            if path[1] == 'Top left':
                x = ( 0* grid_size) + (grid_size / 2)                       
                y = ((num_squares - 1) * grid_size) + (grid_size / 2)
                goto(x,y)
                x_coord.append(x)
                y_coord.append(y)

            elif path[1]== 'Bottom left':
                 x = (0 * grid_size) + (grid_size / 2)
                 y = (0 * grid_size) + (grid_size / 2)
                 goto(x,y)
                 x_coord.append(x)
                 y_coord.append(y)

            elif path[1] == 'Top right' :
                x = ((num_squares - 1) * grid_size) + (grid_size / 2)
                y = ((num_squares - 1) * grid_size) + (grid_size / 2)
                goto(x,y)
                x_coord.append(x)
                y_coord.append(y)

            elif path[1] == 'Centre':
                x = (num_squares / 2) * grid_size 
                y = (num_squares / 2) * grid_size
                goto(x,y)
                x_coord.append(x)
                y_coord.append(y)

            elif path[1] == 'Bottom right':
                x = ((num_squares - 1) * grid_size) + (grid_size / 2)
                y = ( 0* grid_size) + (grid_size / 2)
                goto(x,y)
                x_coord.append(x)
                y_coord.append(y)

#Follow the steps after the start and place tokens allocated to certain spots
#along the way
#
            elif path[0] == "North":
                setheading(90)
                distance_to_go = grid_size * path[1]
                forward(distance_to_go)
                y_coord[0] = y_coord[0] + distance_to_go
                
                 
            elif path[0] == "South":
                setheading(270)
                distance_to_go = grid_size * path[1]
                forward(distance_to_go)
                y_coord[0] = y_coord[0] - distance_to_go
                
            elif path[0] == "East":
                setheading(0)
                distance_to_go = grid_size * path[1]
                forward(distance_to_go)
                x_coord[0] = x_coord[0] + distance_to_go

            elif path[0] == "West":
                setheading(180)
                distance_to_go = grid_size * path[1]
                forward(distance_to_go)
                x_coord[0] = x_coord[0] - distance_to_go

#allocating tokens to the token list numbers
            if path[2] == 0:
                uzumaki_clan(x_coord[0],y_coord[0])
                token_0.append(path[2])
                total_token.append(path[2])
                
            elif path[2] == 1:
                uchiha_clan(x_coord[0],y_coord[0])
                total_token.append(path[2])
                token_1.append(path[2])
            elif path[2] == 2:
                fuma_clan(x_coord[0],y_coord[0])
                total_token.append(path[2])
                token_2.append(path[2])
            elif path[2] == 3:
                akimichi_clan(x_coord[0],y_coord[0])
                total_token.append(path[2])
                token_3.append(path[2])
            elif path[2] == 4:
                hatake_clan(x_coord[0],y_coord[0])
                total_token.append(path[2])
                token_4.append(path[2])


#Function that returns x,y coordinates stored in x_coord and y_coord list                
#not sure if need this but will use as an agrument for token
#

def spiral_coord():
    x = x_coord[0]
    y = y_coord[0]
    return x, y


        
#My Tokens
#
def uzumaki_clan (x ,y):
    width(5)  

    goto(x,y)

    setheading(90)
    forward(45)
    pencolor("black")
  

    setheading(180)
    
    
    

    down()
    begin_fill()
    circle(40)
    color("firebrick")
    end_fill()
    up()
    color("black")
    goto(x, y)
    

    

    for i in range(80):
        
        t = i / 20 * pi
        dx = (6.8 + 2.5 * t) * cos(t)
        dy = (6.8 + 2.5 * t) * sin(t)

        goto(x + dx, y + dy)
        down()
    up()
    goto(x,y)







def uchiha_clan (x,y):
    setheading(0)
    up()
    pencolor("black")
    width(3)

    ##top half
    forward(40)
    setheading(90)
    forward(10)
    down()
    begin_fill()
    fillcolor("red")
    circle(40,180)
    setheading(33)
    down()
    circle (-74 , 65)
    end_fill()

    #bottom half
    fillcolor('white')
    begin_fill()
    setheading(270)
    up()
    forward(10)
    setheading(180)
    forward(2)
    down()
    setheading(143)
    circle(64,73)
    setheading(300)
    circle(40 , 60)
    setheading(270)
    forward(20)
    setheading(0)
    forward(10)
    setheading(90)
    forward(20)
    setheading(0)
    circle(40,55)
    end_fill()
    up()
    goto(x , y)

def fuma_clan (x , y):
    setheading(0)
    goto(x,y)
    fillcolor('black')
    width(2)
    up()
    forward(45)
    setheading(155)
    down()
    begin_fill()
    forward(30)
    setheading(120)
    forward(30)
    setheading(240)
    forward(30)
    setheading(205)
    forward(30)
    setheading(330)
    forward(30)
    setheading(300)
    forward(30)
    setheading(55)
    forward(30)
    setheading(30)
    forward(30)
    end_fill()
    up()
    goto(x, y)
    setheading(0)
    forward(4)
    dot(13 , 'white')
def akimichi_clan (x,y):
    goto(x ,y)
    width(7.5)
    dot(94, 'White')
    up()
    fillcolor('White')
    begin_fill()
    setheading(90)
    forward(45)
    down()
    setheading(180)
    circle(45)
    setheading(270)
    forward(90)
    up()
    setheading(0)
    circle(45,50)
    down()
    setheading(90)
    forward(57)
    setheading(219)
    forward(88)
    setheading(90)
    forward(57)
    setheading(319)
    forward(85)
    end_fill()
    up()
    goto(x,y)
    setheading(0)
    


def hatake_clan (x,y):
    width(6)
    up()
    fillcolor('White')
    setheading(90)
    forward(40)
    down()
    begin_fill()
    setheading(225)
    forward(60)
    setheading(315)
    forward(60)
    setheading(45)
    forward(60)
    setheading(135)
    forward(60)
    end_fill()
    setheading(225)
    up()
    forward(20)
    setheading(315)
    down()
    forward(60)
    up()
    setheading(225)
    down()
    forward(20)
    setheading(135)
    down()
    forward(60)
    up()
    setheading(225)
    forward(20)
    setheading(315)
    forward(20)
    setheading(45)
    down()
    forward(60)
    up()
    setheading(315)
    forward(20)
    setheading(225)
    down()
    forward(60)
    up()
    goto(x,y)

#Token LEGEND
def legend():
#legend border
    tracer(False)
    color('brown')
    goto((num_squares * grid_size) + margin, (num_squares * grid_size) // 2)
    
    width(2)
    up()
    setheading(180)
    forward(25)
    down()
    setheading(90)
    forward(350)
    setheading(0)
    forward(350)
    setheading(270)
    forward(700)
    setheading(180)
    forward(350)
    setheading(90)
    forward(350)

#legend title
    up()
    setheading(0)
    forward(200)
    setheading(90)
    forward(300)
    setheading(180)
    forward(180)
    color('Black')
    if str(len(total_token)) == "1":
        write( str(len(total_token))+ " " + 'Shinobi Clan Found!',
               font=('Arial',18, 'bold'))
    else:
        write( str(len(total_token))+ " " + 'Shinobi Clans Found!',
               font=('Arial',18, 'bold'))


#tokens
    
    setheading(270)
    forward(50)
    uzumaki_clan(legend_x + 20,legend_y + 200)
    setheading(0)
    forward(60)
   
    write('Uzumaki Clan'+" " +"["+ str(len(token_0))+ "]", font =('Arial',12,"bold"))
    
    up()
    setheading(180)
    forward(60)
    setheading(270)
    forward(120)
    uchiha_clan(legend_x ,legend_y)
    setheading(0)
    forward(80)
    setheading(90)
    forward(70)

    write('Uchiha Clan'+" " +"["+ str(len(token_1))+ "]",font =('Arial',12,"bold"))

    up()
    fuma_clan(legend_x + 20, legend_y - 30)
    setheading(0)
    forward(60)
   
    write('Fuma Clan'+" " +"["+ str(len(token_2))+ "]", font =('Arial', 12,'bold'))

    up()
    akimichi_clan(legend_x + 27, legend_y - 150)
    setheading(0)
    forward(60)
    write('Akimichi Clan'+" " +"["+ str(len(token_3))+ "]", font=('Arial', 12, 'bold'))
    

    setheading(270)
    forward(110)
    setheading(180)
    forward(60)
    hatake_clan(legend_x + 25,legend_y - 260)
    setheading(0)
    forward(60)
    write('Hatake Clan'+" " +"["+ str(len(token_4))+ "]", font= ('Arial',12, 'bold'))
  
         
        

        

#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your solution.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's theme
# ***** and its tokens
title("Shinobi Clan Emblems in Naruto")

### Call the student's function to follow the path
### ***** While developing your program you can call the follow_path
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_path()" as the
### ***** argument to the follow_path function.  Your program must
### ***** work for any data set that can be returned by the
### ***** random_path function.
#follow_path(fixed_path_0) # <-- used for code development only, not marking
follow_path(random_path()) # <-- used for assessment
legend()
# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
hideturtle()
release_drawing_canvas()

#
#--------------------------------------------------------------------#
