from turtle import*

speed('fast')

s=0
while s < 1000:
    fd(50+s)
    lt(60)
    write(s)
    dot(20)
    s += 10
mainLoop()