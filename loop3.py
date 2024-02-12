from turtle import*
speed('slowest')
pencolor('purple')
bgcolor('lightblue')
for i in range(5):
    fd(100)
    for i in range(5):
        fd(75)
        lt(360/5)
    lt(360/5)
    dot(10)
mainloop()
