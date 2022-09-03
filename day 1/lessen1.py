from turtle import*

speed(5)


width(5)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(70)
color("green")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(20, 30)
pendown()

color("brown")
begin_fill()
left(120)
forward(30)
left(90)
forward(60)
left(90)
forward(30)
left(90)
forward(60)
end_fill()


penup()
goto(150, 30)
pendown()

color("brown")
begin_fill()
left(90)
forward(30)
left(90)
forward(60)
left(90)
forward(30)
left(90)
forward(60)
end_fill()


exitonclick()