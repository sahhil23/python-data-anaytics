from turtle import*
speed(0)

def polygon(side,size,color):
    fillcolor(color)
    begin_fill()
    for _ in range(side):
        fd(size)
        lt(360/side)

        #testing
for i in range(6):
    polygon(15,50,'green')    # required arguements
    polygon(6,100,'yellow')
    polygon(4,100,'red')
    lt(60)
hideturtle()
mainloop()