#import libraries
import turtle
import math
#main triangle function
def main_triangle(startx,starty,size,color):
    #create turtle object
    t = turtle.Turtle()
    t.pensize(3)
    t.speed(0)
    t.pendown()
    t.hideturtle
    t.color(color)
    #place turtle at bottom-right vertex
    t.teleport(startx + size/2,starty)
    #repeat three times
    for i in range(3):
        #turn left 120 degrees
        t.left(120)
        #move forward size amount of pixels
        t.forward(size)
    #delete turtle object
    del t
#triangle function
def triangle(startx,starty,size,depth,limit,color):
    #if we are too deep recursively
    if depth > limit:
        #end function
        return
    #create turtle object
    t = turtle.Turtle()
    t.pensize(3)
    t.speed(0)
    t.pendown()
    t.hideturtle()
    t.color(color)
    #move turtle to start coordinates
    t.teleport(startx,starty)
    #draw right side
    t.left(60)
    t.forward(size)
    #draw smaller triangle relative to right side
    triangle(startx + size/2, starty, size/2, depth + 1, limit, color)
    #draw top
    t.left(120)
    t.forward(size)
    #draw smaller triangle relative to top
    triangle(startx, t.ycor(), size/2, depth + 1, limit, color)
    #draw left side
    t.left(120)
    t.forward(size)
    #draw smaller triangle relative to left side
    triangle(startx - size/2, starty, size/2, depth + 1, limit, color)
    #delete turtle
    del t
#koch line function
def koch_line(startx,starty,angle,dir,size,depth,limit,color):
    #create turtle object
    t = turtle.Turtle()
    t.pensize(3)
    t.speed(0)
    t.pendown()
    t.hideturtle()
    t.setheading(angle)
    t.color(color)
    #move turtle to start coordinates
    t.teleport(startx,starty)
    #move forward 1/3 of size
    if depth == 2:
        koch_line(t.xcor(), t.ycor(), t.heading(),dir, size/3, depth + 1, limit, color)
        t.penup()
    t.forward(size/3)
    t.pendown()
    #if our depth is still within range:
    if depth < limit:
        #draw small triangle coming off of line
        koch_triangle(t.xcor(), t.ycor(), t.heading(),dir, size/3, depth + 1, limit, color)
        t.penup()
    t.forward(size/3)
    t.pendown()
    #draw last 1/3 of line
    if depth == 2:
        koch_line(t.xcor(), t.ycor(), t.heading(),dir, size/3, depth + 1, limit, color)
        t.penup()
    t.forward(size/3)
    #delete turtle
    del t
#koch triangle function
def koch_triangle(startx,starty,angle,dir,size,depth,limit,color):
    #if we are too deep recursively
    if depth > limit:
        #end function
        return
    if dir == 'right':
        op_dir = 'left'
    else:
        op_dir = 'right'
    #create turtle object
    t = turtle.Turtle()
    t.pensize(3)
    t.speed(0)
    t.penup()
    t.hideturtle()
    t.setheading(angle)
    t.color(color)
    #move turtle to start coordinates
    t.teleport(startx,starty)
    #move forward size amount
    t.forward(size)
    if depth == 1:
        sides = 3
    else:
        sides = 2
    #loop two times
    for i in range(sides):
        #turn and draw 1/3 of the side using a koch line
        if dir == 'left':
            t.left(120)
        else:
            t.right(120)
        koch_line(t.xcor(), t.ycor(), t.heading(),op_dir, size/3, depth + 1, limit, color)
        t.forward(size/3)
        #draw smaller triangle coming off of side
        koch_triangle(t.xcor(), t.ycor(), t.heading(),op_dir, size/3, depth + 1, limit, color)
        #move forward 1/3 of the side
        if depth == limit:
            t.pendown()
        t.forward(size/3)
        t.penup()
        #draw the last third of the side
        koch_line(t.xcor(), t.ycor(), t.heading(),op_dir, size/3, depth + 1, limit, color)
        t.forward(size/3)
    #delete turtle
    del t
def screen_setup(back):
    screen = turtle.Screen()
    screen.bgcolor(back)
def finish():
    turtle.done()
