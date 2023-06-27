from turtle import *
import pandas as pd
import numpy as np
import time
import math

t = Turtle()
s = Screen()
s.tracer(0)
t.shape('square')
t.color('gray2')

prodname = 'Gems Britania Kurkure Thumbs-up Dairymilk Chocos Too-Yumm Oreo'.split()
prodexpdate = [6, 4, 6, 6, 8, 3, 4, 6]
prodweight = [20, 20, 40, 40, 10, 10, 50, 30]
prodprice = [10, 10, 20, 30, 10, 10, 35, 20]
prodcolor = ['yellow', 'red', 'green', 'orange', 'blue', 'pink', 'white', 'brown']

d = {'product': prodname, 'price': prodprice, 'expiry': prodexpdate, 'weight': prodweight}
d1 = pd.DataFrame(d, index=prodcolor)
print(d1)

s.bgcolor('gray2')

r = Turtle()
r.pu()
r.goto(0, 280)
r.color('black')
r.write('click the bubble you want to buy', align="center", font=("Arial", 25, ("bold", "italic")))
r.ht()

prods = []
for i in range(8):
    prods.append(Turtle())

n = 0
g = -280
dis = 80
bis = 80

for prod in prods:
    prod.shape('circle')
    prod.shapesize(1.8, 1.8, 1)
    prod.color(prodcolor[n])
    prod.pu()
    if n <= 3:
        prod.setpos(g + dis, 100)
        dis += 120
    prod.write(prodname[n], align="center", font=("Arial", 15, ("bold", "italic")))
    prod.sety(prod.ycor() - 20)
    if n > 3:
        prod.setpos(g + bis, -100)
        bis += 120
        prod.write(prodname[n], align="center", font=("Arial", 15, ("bold", "italic")))
    prod.sety(prod.ycor() + 20)
    n += 1


def endy():
    t.clear()
    t.speed(1)
    s.tracer(0)
    t.goto(0, 100)
    t.write('please wait', align="center", font=("Arial", 20, ("bold", "italic")))
    t.goto(0, 0)
    t.pensize(1)
    t.pd()
    t.st()
    dd = 50
    t.color('black')

    for i in range(0, 361):
        t.circle(dd)
        t.rt(92)
        if i == 180:
            t.color('white')
        if i == 360:
            t.clear()
            t.pu()
            t.goto(0, 0)
            t.color('black')
            t.write('thank you, purchase successful!!', align="center",
                    font=("Arial", 30, ("bold", "italic")))
            time.sleep(1.5)
            bye()
    update()


def buying(n, l, k):
    s.clear()
    t.home()
    t.sety(t.xcor() + 50)
    t.color('black')
    t.write('price to pay=' + str(n), align="center", font=("Arial", 30, ("bold", "italic")))
    t.sety(t.xcor() - 50)
    t.write('best before (in months)=' + str(l), align="center", font=("Arial", 30, ("bold", "italic")))
    t.sety(t.xcor() - 100)
    t.write('weight of item=' + str(k), align="center", font=("Arial", 30, ("bold", "italic")))
    time.sleep(3)
    endy()


def discal(m, n):
    dist = math.sqrt((m.xcor() - n.xcor()) ** 2 + (m.ycor() - n.ycor()) ** 2)
    return dist


pcolor = ''
t.pu()
h = t.color()
gg = 0

while True:
    for prod in prods:
        s.listen()
        prod.onclick(t.goto, 1)
        if discal(prod, t) <= 30:
            pcolor = prod.color()
            col = pcolor[1]
            gg = d1.at[str(col), 'price']
            pp = d1.at[str(col), 'expiry']
            kk = d1.at[str(col), 'weight']
            buying(gg, pp, kk)
    s.update()  # Update the screen
