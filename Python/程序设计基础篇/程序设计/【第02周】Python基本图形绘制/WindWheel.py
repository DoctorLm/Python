#WindWheel.py
import turtle as t
t.pensize(2)
for i in range(4):
    t.seth(90*i)
    t.fd(150)
    t.right(90)
    t.circle(-150, 45)
    t.goto(0,0)
t.done()
#import turtle as t
#t.setup(650, 650, 200, 200)
#t.pensize(2)
#for i in range(4):
#    t.seth(90*i)
#    t.fd(150)
#    t.right(90)
#    t.circle(-150, 45)
#    t.goto(0,0)
#t.done()
