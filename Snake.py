import turtle
import time
import random

#Game Speed
delay=0.2

#Setup Screen
wn=turtle.Screen()
wn.title("Snake by Gerd Harlander")
wn.bgcolor("Green")
wn.setup(width=600, height=600)
wn.tracer(0)

#Score
score=0
highscore=0

#Setup Segments
segments=[]

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score 0 Highscore 0", align="center", font=("Courier",24,"normal"))

#Snake Head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"

#Food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(-50,-50)

#Function
def go_up():
    if head.direction!="down":
        head.direction="up"
def go_down():
    if head.direction!="up":
        head.direction="down"
def go_left():
    if head.direction!="right":
        head.direction="left"
def go_right():
    if head.direction!="left":
        head.direction="right"

#Keyboard Bindings
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")

#Moving function
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)



#Main Loop
while True:
    wn.update()
   

    #Collision betwenn Head and Food
    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.setx(x)
        food.sety(y)
        
        segment=turtle.Turtle()
        segment.speed(0)
        segment.penup()
        segment.shape("square")
        segment.color("gray")
        segments.append(segment)

        score+=10

        if score>highscore:
            highscore=score

        pen.clear()
        pen.write("Score {} Highscore {}".format(score, highscore), align="center", font=("Courier",24,"normal"))

    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    
    #Collision between Boarders
    if(head.ycor()>290 or head.ycor()<-290 or head.xcor()>290 or head.xcor()<-290):
        time.sleep(1)
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        head.goto(0,0)
        head.direction="stop"
        if score>highscore:
           highscore=score
        pen.clear()
        score=0
        pen.write("Score {} Highscore {}".format(score, highscore), align="center", font=("Courier",24,"normal"))

    move()

    #Collision between Head and segment
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            head.goto(0,0)
            head.direction="stop"
            if score>highscore:
                highscore=score
            pen.clear()
            score=0
            pen.write("Score {} Highscore {}".format(score, highscore), align="center", font=("Courier",24,"normal"))

    time.sleep(delay)