# Drawing a Heart <3 Using turtle

from turtle import *
import turtle

color("red")
begin_fill()
pensize(3)
left(50)
forward(133)
circle(50,200)
right(140)
circle(50,200)
forward(133)
end_fill()

turtle.color('white')
style = ('Courier', 30, 'normal')
turtle.write('Eli', font=style, align="center")

done()


