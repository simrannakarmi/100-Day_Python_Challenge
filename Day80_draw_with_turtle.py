import turtle
t = turtle.Turtle()

t.color("red", "green")
t.begin_fill()

for i in range(4):    
    t.forward(200)
    t.left(90)
    
t.end_fill()

c = ["blue", "pink", "yellow", "orange"]
k = 0
for i in range(100, 0, -20):    
    t.color(c[k])
    k += 1
    t.begin_fill()
    t.circle(i)
    t.end_fill()
    
turtle.done()