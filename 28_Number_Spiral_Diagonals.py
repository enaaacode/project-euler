from turtle import *
tracer(0) 
for i in range(10000):
    move = 1 + i*10
    fd(move)
    right(90)

update()
mainloop()