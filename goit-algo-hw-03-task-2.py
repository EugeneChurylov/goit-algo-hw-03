import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def koch_snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("yellow")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-150, 50)
    t.pendown()

    koch_snowflake(t, order, size)

    window.mainloop()

draw_koch_snowflake(3)
