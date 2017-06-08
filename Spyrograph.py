#Import the turtle and math libraries
import turtle
import math

#Create the turtle window and a turtle (refer to a previous lab if you don't remember how to do this)
window = turtle.Screen()
bob = turtle.Turtle()


#Prompt for the moving radius, fixed radius, pen offset and color
r = float(input('Please enter the moving radius: '))
R = float(input('Please enter the fixed radius: '))
pen_offset = float(input('Please enter the offset of the pen point: '))
color = raw_input('Please enter the color: ')

#Create a variable to represent the current time, and initialize it to 0.0.
time = 0.0
#Tell your turtle to pick up its pen
bob.penup()
#Tell your turtle to move to the appropriate initial position. In particular, use the equations given above to compute x(0) and y(0)
bob.goto((R + r) * math.cos(time) + pen_offset * math.cos(((R + r) *time)/ r),
    (R + r) * math.sin(time) + pen_offset * math.sin(((R + r) *time)/ r))
    #Tell your turtle to put the pen down
bob.pendown()
#set pen color to the value given by the user.
bob.pencolor(color)

#Write a while loop that continues as long as the time is less than 100
while time < 100:
    #Update the value of time to increase by 0.1
    time += 0.1
    #Tell your turtle to go to the location specified by x and y
    bob.goto((R + r) * math.cos(time) + pen_offset * math.cos(((R+r) *time)/ r),
            (R + r) * math.sin(time) + pen_offset * math.sin(((R+r) *time)/ r))
#exit window when clicked
#window.exitonclick()
#Prompt for the moving radius, fixed radius, pen offset and color
r = float(input('Please enter the moving radius: '))
R = float(input('Please enter the fixed radius: '))
pen_offset = float(input('Please enter the offset of the pen point: '))
color = raw_input('Please enter the color: ')

#Create a variable to represent the current time, and initialize it to 0.0.
time = 0.0
#Tell your turtle to pick up its pen
bob.penup()
#Tell your turtle to move to the appropriate initial position. In particular, use the equations given above to compute x(0) and y(0)
bob.goto((R + r) * math.cos(time) + pen_offset * math.cos(((R + r) *time)/ r),
    (R + r) * math.sin(time) + pen_offset * math.sin(((R + r) *time)/ r))
    #Tell your turtle to put the pen down
bob.pendown()
#set pen color to the value given by the user.
bob.pencolor(color)

#Write a while loop that continues as long as the time is less than 100
while time < 100:
    #Update the value of time to increase by 0.1
    time += 0.1
    #Tell your turtle to go to the location specified by x and y
    bob.goto((R + r) * math.cos(time) + pen_offset * math.cos(((R+r) *time)/ r),
            (R + r) * math.sin(time) + pen_offset * math.sin(((R+r) *time)/ r))
#Prompt for the moving radius, fixed radius, pen offset and color
r = float(input('Please enter the moving radius: '))
R = float(input('Please enter the fixed radius: '))
pen_offset = float(input('Please enter the offset of the pen point: '))
color = raw_input('Please enter the color: ')

#Create a variable to represent the current time, and initialize it to 0.0.
time = 0.0
#Tell your turtle to pick up its pen
bob.penup()
#Tell your turtle to move to the appropriate initial position. In particular, use the equations given above to compute x(0) and y(0)
bob.goto((R + r) * math.cos(time) + pen_offset * math.cos(((R + r) *time)/ r),
    (R + r) * math.sin(time) + pen_offset * math.sin(((R + r) *time)/ r))
    #Tell your turtle to put the pen down
bob.pendown()
#set pen color to the value given by the user.
bob.pencolor(color)

#Write a while loop that continues as long as the time is less than 100
while time < 100:
    #Update the value of time to increase by 0.1
    time += 0.1
    #Tell your turtle to go to the location specified by x and y
    bob.goto((R + r) * math.cos(time) + pen_offset * math.cos(((R+r) *time)/ r),
            (R + r) * math.sin(time) + pen_offset * math.sin(((R+r) *time)/ r))