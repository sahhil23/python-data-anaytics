from turtle import *
speed
pencolor('red')
pensize(5)
for i in range(8,0,-1):
    fd(120)
    rt(45)
    write(f'n={i}',font=("acrilic",16,))

hideturtle()
mainloop()
