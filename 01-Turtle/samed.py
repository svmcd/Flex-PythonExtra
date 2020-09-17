import turtle             
colors = [ "#e1f7d5","#ffbdbd","#c9c9ff","#ffffff","#f1cbff","#e1f7d5"]
turtle.speed(0)
my_pen = turtle.Pen()
turtle.bgcolor("black")
for x in range(360):
   my_pen.pencolor(colors[x % 6])
   my_pen.width(x/100 + 1)
   my_pen.forward(x)
   my_pen.left(59)
   
turtle.done()