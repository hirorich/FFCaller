# 亀
from turtle import Turtle

# 座標リスト取得
def create_pos_list(kame, l):
    
    kame.getscreen().setworldcoordinates(0, 0, 511, 511)
    
    kame.penup()
    kame.shapesize(1)
    
    kame.setpos(255, 0)
    p0 = (255, 0)
    kame.setheading(150)
    kame.pendown()
    kame.forward(256)
    p1 = (kame.xcor(), kame.ycor())
    kame.penup()
    
    kame.setpos(255, 511)
    p3 = (255, 511)
    kame.setheading(210)
    kame.pendown()
    kame.forward(256)
    p2 = (kame.xcor(), kame.ycor())
    kame.penup()
    
    kame.setpos(255, 511)
    kame.setheading(270)
    kame.pendown()
    kame.forward(l)
    p4 = (kame.xcor(), kame.ycor())
    kame.setheading(210)
    kame.forward(256 - l)
    p5 = (kame.xcor(), kame.ycor())
    kame.penup()
    
    kame.setpos(255, 256)
    p8 = (255, 256)
    kame.setheading(90)
    kame.pendown()
    kame.forward(l)
    p7 = (kame.xcor(), kame.ycor())
    kame.setheading(210)
    kame.forward(256 - l)
    p6 = (kame.xcor(), kame.ycor())
    kame.penup()
    
    kame.setpos(255, 0)
    kame.setheading(90)
    kame.pendown()
    kame.forward(l)
    p10 = (kame.xcor(), kame.ycor())
    kame.setheading(150)
    kame.forward(256 - l)
    p9 = (kame.xcor(), kame.ycor())
    kame.penup()
    
    kame.clear()
    
    list = []
    list.append(p1)
    list.append(p2)
    list.append(p3)
    list.append(p4)
    list.append(p5)
    list.append(p6)
    list.append(p7)
    list.append(p8)
    list.append(p9)
    list.append(p10)
    list.append(p0)
    
    return list

# 描写
def write_list(kame, list, pos_x = 0, pos_y = 0, color1='blue', color2='yellow'):
    
    kame.shapesize(1)
    
    kame.setpos(list[len(list) - 1][0] + pos_x, list[len(list) - 1][1] + pos_y)
    print('x:' + str(list[len(list) - 1][0] + pos_x) + ', y:' + str(list[len(list) - 1][1] + pos_y))
    kame.color(color1, color1)
    kame.pendown()
    kame.begin_fill()
    for pos in list:
        kame.setpos(pos[0] + pos_x, pos[1] + pos_y)
        print('x:' + str(pos[0] + pos_x) + ', y:' + str(pos[1] + pos_y))
    kame.end_fill()
    kame.penup()
    
    kame.setpos(511 - list[len(list) - 1][0] + pos_x, 511 - list[len(list) - 1][1] + pos_y)
    print('x:' + str(511 - list[len(list) - 1][0] + pos_x) + ', y:' + str(511 - list[len(list) - 1][1] + pos_y))
    kame.color(color2, color2)
    kame.pendown()
    kame.begin_fill()
    for pos in list:
        kame.setpos(511 - pos[0] + pos_x, 511 - pos[1] + pos_y)
        print('x:' + str(511 - pos[0] + pos_x) + ', y:' + str(511 - pos[1] + pos_y))
    kame.end_fill()
    kame.penup()

# main
if __name__ == "__main__":
    
    l = 64
    
    kame = Turtle()
    list = create_pos_list(kame, l)
    write_list(kame, list)
    
    kame.getscreen().getcanvas().postscript(file='file_name.ps', colormode='color')
    
    k=input()

