import turtle
import math
import random
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help

def setupWindow(wn=None):
  "creates a window for following functions to be drawn in, arg : None, " 
  wn.setworldcoordinates(-360, -1, 361, 1)

def setupAxis(dart=None):
  "creates x and y axes for following functions to be drawn on, arg: None"
  dart.up()
  dart.goto(0,1)  
  dart.down() 
  dart.goto(0,-1) 
  dart.up() 
  dart.goto(-360,0) 
  dart.down()
  dart.goto(360,0)

def drawSineCurve(dart):
  "drawSineCurve function creates a sine curve in terms of radians, arg:dart"
  for i in range(-360,361):
    y = math.sin(math.radians(i))
    dart.goto(i,y)

def drawCosineCurve(dart):
  "drawCosineCurve function creates a cosine curve in terms of radians, arg:dart"
  dart.up()
  dart.color("red")
  dart.goto(-360,1)
  dart.down()
  for i in range(-360,361):
    y = math.cos(math.radians(i))
    dart.goto(i,y)

def drawTangentCurve(dart):
  "drawTangentCurve creates a tangent curve in terms of radians, arg: dart"
  dart.up()
  dart.color("blue")
  dart.goto(-360,1)
  dart.down()
  for i in range(-360,361):
    y = math.tan(math.radians(i))
    dart.goto(i,y)

def age(year=2022):
  "this functions gets the birthday of the user and returns the age of the user, arg:year"
  birthday=int(input("What year were you born? "))
  age = str(year-birthday)
  print("You are "+ age + " years old!" )
  return(age)
age()

def greet(name=input("what's your name?")):
  "this function displays and returns a message with the parameter being a name, arg:name"
  for name in name:
    print("Happy Birthday " + name +", here are some cool curves and a dope star!")
    return greet

greet()

t = turtle.Turtle()
w = turtle.Screen()
t.speed(0)

w.bgcolor(input("enter your favorite color: "))
t.color("white")

def stars():
  "this function creates a star design with 5 sides, each with a length of 50 and turning at an angle of 144 degrees"
  for i in range(0, 5):
    t.fd(50)
    t.right(144)
    
for i in range(100):
  x=random.randint(-320,320)
  y=random.randint(-115,115)

stars()


##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
