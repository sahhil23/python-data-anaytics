from turtle import *

def hexagon():
    for _ in range(6):
        fd(100)
        rt(60)
def pentagon():
    for _ in range(5):
        fd(50)
        lt(72)

        #testing
for i in range(6):
    fd(100)
    hexagon()
    pentagon()   
    lt(60)