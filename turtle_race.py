import turtle
from turtle import *
from turtle import Turtle
from turtle import Screen, Turtle, mainloop
from random import randint, choice
width,height=550,550
screen = Screen()
screen.setup(width, height)
screen.bgcolor('black')

background = Turtle()
background.penup()
background.setx(-width/2)
background.pendown()

background.color('gray')
background.begin_fill()

for _ in range(2):
    background.forward(width)
    background.right(90)
    background.forward(height/2.5)
    background.right(90)

background.end_fill()

penup()
goto(-10,160)
turtle.color('white')
style = ('Times', 20, 'bold')
turtle.write('Hello! Wellcome to', font=style, align='center')
penup()
goto(-10,115)
turtle.color('white')
style = ('Times', 40, 'bold')
turtle.write('TURTLE RACE ', font=style, align='center')
penup()
goto(-10,90)
style = ('Times', 15, 'bold')
turtle.write('There are 4 turtles select a turtle as u like.',font=style, align='center')
ada = Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-80,70)
dat = Turtle()
dat.color('blue')
dat.shape('turtle')
dat.penup()
dat.goto(-40,70)
cac = Turtle()
cac.color('aqua')
cac.shape('turtle')
cac.penup()
cac.goto(0,70)
adt = Turtle()
adt.color('yellow')
adt.shape('turtle')
adt.penup()
adt.goto(40,70)
penup()
goto(-10,40)
turtle.write('The turtle which comes first to the end line is the WINNER.', font=style, align='center')

pendown()
color('black')
speed(15)
penup()
goto(-150,-25)

for step in range(15):
  right(90)
  for num in range(8):
    penup()
    forward(10)
    pendown()
    color('black')
    forward(10)
  penup()
  backward(160)
  left(90)
  forward(20)
 
penup()
goto(-100,80)  
stamp_size = 5
square_size = 4
finishi_line = 158

  
  
turtle.hideturtle()  

ada = Turtle()
ada.color('red')
ada.shape('turtle')
ada.right(360)
ada.penup()
ada.goto(-180,-55)

dat = Turtle()
dat.color('blue')
dat.shape('turtle')
dat.right(360)
dat.penup()
dat.goto(-180,-93)

cac = Turtle()
cac.color('aqua')
cac.shape('turtle')
cac.right(360)
cac.penup()
cac.goto(-180,-128)

adt = Turtle()
adt.color('yellow')
adt.shape('turtle')
adt.right(360)
adt.penup()
adt.goto(-180,-158)

for turn in range(109):
  ada.forward(randint(1,5))
  dat.forward(randint(1,5))
  cac.forward(randint(1,5))
  adt.forward(randint(1,5))
  
  
if ada.xcor()> dat.xcor() and  ada.xcor() > cac.xcor() and  ada.xcor() >  adt.xcor():
  print(' Red turtle wins! ')
  for i in range(72):
    ada.right(360*5)

elif dat.xcor()> ada.xcor() and  dat.xcor() > ada.xcor() and  dat.xcor() >  adt.xcor():
  print(' Blue turtle wins! ')
  for i in range(72):
    dat.right(360*5)

elif  cac.xcor()> ada.xcor() and  cac.xcor() > dat.xcor() and  cac.xcor() >  adt.xcor():
  print(' Aqua turtle wins! ')
  for i in range(72):
    cac.right(360*5)

elif adt.xcor()>  ada.xcor() and  adt.xcor() > dat.xcor() and  adt.xcor() >  cac.xcor():
  print(' Yellow turtle wins! ')
  for i in range(72):
    adt.right(360*5)


