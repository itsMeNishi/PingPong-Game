# -*- coding: utf-8 -*-
"""
Created on Sat May 23 15:44 :41 2020

@author: Nishi
"""

import turtle
import os

wn = turtle.Screen()
wn.title("PONG Game by Nishi :)")
wn.bgcolor("black")
wn.setup(width= 800, height = 600)
wn.tracer(0)  #stops the window from updating and speeds up the game

score_a = 0
score_b = 0


#Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)   # TO improve the speed of game, not the paddle on the screen
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.color("white")
paddle_a.penup()   # To avoid paddle draw a line on screen
paddle_a.goto(-350,0)

#Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)   # TO improve the speed of game, not the paddle on the screen
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.color("white")
paddle_b.penup()   # To avoid paddle draw a line on screen
paddle_b.goto(350,0)


#Ball

ball = turtle.Turtle()
ball.speed(0)   # TO improve the speed of game, not the paddle on the screen
ball.shape("circle")
ball.color("white")
ball.penup()   # To avoid paddle draw a line on screen
ball.goto(0,0)
ball.dx = 0.1
ball.dy = -0.1

#Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A : 0   Player B : 0", align = "Center", font = ("Courier", 24, "normal"))


#Function

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
 
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
 
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)    
  
 
 
#Keyboard binding

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

   


# Main game loop

while True:
    wn.update()
          #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
 
         #Check the borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("aplay water.wav&")
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay water.wav&")

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A : {}   Player B : {}".format(score_a,score_b), align = "Center", font = ("Courier", 24, "normal"))

        
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A : {}   Player B : {}".format(score_a,score_b), align = "Center", font = ("Courier", 24, "normal"))

       
    #Paddle and ball collisions
    if(ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
         ball.setx(340)
         ball.dx *= -1
         os.system("aplay bounce.wav&")


    if(ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
         ball.setx(-340)
         ball.dx *= -1
         os.system("aplay bounce.wav&")








   
