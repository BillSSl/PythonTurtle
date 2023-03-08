import turtle

t = turtle.Turtle()

t.color('red')
t.begin_fill()

t.penup()
t.fd(50)
t.pendown()

def side():
  t.fd(100)
  t.rt(90)
  t.fd(100)
  t.rt(90)
  t.fd(100)
  t.rt(-90)
for i in range(4):
  side()
  
t.end_fill()



