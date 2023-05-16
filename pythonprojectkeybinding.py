import turtle

t = turtle.Turtle()

t.setheading(90)
t.speed(0)


def moveup():
  t.fd(10)
  t.setheading(90)


turtle.listen()
turtle.onkey(moveup, 'Up')


def moveleft():
  t.setheading(90)
  t.lt(90)
  t.fd(10)


turtle.listen()
turtle.onkey(moveleft, 'Left')


def moveright():
  t.setheading(90)
  t.rt(90)
  t.fd(10)


turtle.listen()
turtle.onkey(moveright, 'Right')


def movedown():
  t.setheading(90)
  t.bk(10)


turtle.listen()
turtle.onkey(movedown, 'Down')


def RemovePen():
  t.penup()


turtle.listen()
turtle.onkey(RemovePen, 'u')


def PutPen():
  t.pendown()


turtle.listen()
turtle.onkey(PutPen, 'd')


def triangle():
  i = 0
  while i < 3:
    t.fd(50)
    t.lt(120)
    i += 1


turtle.listen()
turtle.onkey(triangle, 't')


def square():
  i = 0
  while i < 4:
    t.fd(50)
    t.lt(90)
    i += 1


turtle.listen()
turtle.onkey(square, 's')


def pentagon():
  i = 0
  while i < 5:
    t.fd(50)
    t.lt(72)
    i += 1


turtle.listen()
turtle.onkey(pentagon, 'p')


def hexagon():
  i = 0
  while i < 6:
    t.fd(50)
    t.lt(60)
    i += 1


turtle.listen()
turtle.onkey(hexagon, 'h')


def heptagon():

  i = 0
  for i in range(7):
    t.forward(50)
    t.left(51.43)


turtle.listen()
turtle.onkey(heptagon, 'H')


def octagon():

  i = 0
  while i < 8:
    t.fd(50)
    t.lt(45)
    i += 1


turtle.listen()
turtle.onkey(octagon, 'o')


def nonagon():

  i = 0
  while i < 9:
    t.fd(50)
    t.lt(40)
    i += 1


turtle.listen()
turtle.onkey(nonagon, 'n')


def decagon():
  i = 0
  while i < 10:
    t.fd(50)
    t.lt(36)
    i += 1


turtle.listen()
turtle.onkey(decagon, 'e')


def dodecagon():
  i = 0
  while i < 12:
    t.fd(50)
    t.lt(30)
    i += 1


turtle.listen()
turtle.onkey(dodecagon, 'D')


def hendecagon():
  i = 0
  for i in range(11):
    t.fd(50)
    t.lt(32.73)


turtle.listen()
turtle.onkey(hendecagon, 'a')


def tridecagon():
  i = 0
  for i in range(13):
    t.fd(50)
    t.lt(27.7)


turtle.listen()
turtle.onkey(tridecagon, 'T')


def tetradecagon():
  i = 0
  for i in range(14):
    t.fd(50)
    t.lt(25.71)


turtle.listen()
turtle.onkey(tetradecagon, 'r')


def pentadecagon():
  i = 0
  for i in range(15):
    t.fd(50)
    t.lt(24)


turtle.listen()
turtle.onkey(pentadecagon, 'P')


def hexadecagon():
  i = 0
  for i in range(16):
    t.fd(50)
    t.lt(22.5)


turtle.listen()
turtle.onkey(hexadecagon, 'x')


def heptadecagon():
  i = 0
  for i in range(17):
    t.fd(50)
    t.lt(21.17)


turtle.listen()
turtle.onkey(heptadecagon, 'E')


def octadecagon():
  i = 0
  for i in range(18):
    t.fd(50)
    t.lt(20)


turtle.listen()
turtle.onkey(octadecagon, 'O')


def enneadecagon():
  i = 0
  for i in range(19):
    t.fd(50)
    t.lt(18.94)


turtle.listen()
turtle.onkey(enneadecagon, 'N')


def icosagon():
  i = 0
  for i in range(20):
    t.fd(50)
    t.lt(18)


turtle.listen()
turtle.onkey(icosagon, 'i')


def roundshape():
  i = 0
  while i < 360:
    t.fd(1)
    t.lt(1)
    i += 1


turtle.listen()
turtle.onkey(roundshape, 'c')


def clear():
  t.clear()


turtle.listen()
turtle.onkey(clear, 'R')


def allpolygons():
  triangle()
  square()
  pentagon()
  hexagon()
  heptagon()
  octagon()
  nonagon()
  decagon()
  hendecagon()
  dodecagon()
  tridecagon()
  tetradecagon()
  pentadecagon()
  hexadecagon()
  heptadecagon()
  octadecagon()
  enneadecagon()
  icosagon()


turtle.listen()
turtle.onkey(allpolygons, 'l')


def thing1():
  turtle.setheading(90)

  def Thing():
    t.forward(100)
    t.rt(90)
    t.fd(100)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(100)
    t.rt(90)
    t.fd(25)
    t.rt(90)
    t.fd(25)
    t.rt(90)
    t.fd(50)

  i = 0
  while i < 15:
    Thing()
    t.rt(10)
    t.fd(50)
    i += 1


turtle.listen()
turtle.onkey(thing1, 'w')
