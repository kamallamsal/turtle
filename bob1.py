import turtle

bob = turtle.Turtle()

bob.pencolor("blue")

for i in range(50):
	bob.forward(50)
	bob.left(123)

bob.pencolor("red")
for i in range(50):
	bob.forward(100)
	bob.left(123)
	
turtle.done()		