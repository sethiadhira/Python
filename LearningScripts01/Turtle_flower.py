import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(some_turtle):
        some_turtle.forward(100)
        some_turtle.right(30)
        some_turtle.forward(100)
        some_turtle.right(150)
        

def draw_art():
       
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(20)
    fx=brad.xcor()
    fy=brad.ycor()

    for i in range(1,37):
        #draw_square(brad)
        draw_triangle(brad)
        brad.right(10)

    brad.setx(fx)
    brad.sety(fy)
    brad.forward(100)     
    brad.color("blue")
    brad.right(90)
    brad.forward(200)
    brad.left(90)
    brad.circle(100,180,100)
    window.exitonclick()    
'''
#this is multiline comment
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(10)

    draw_square(brad)
    
    angie =turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
'''



draw_art()
