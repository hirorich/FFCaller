# 亀
from turtle import Turtle

import numpy as np
import cv2

# 座標リスト取得
def create_pos_dict(kame, l):
    
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
    
    pos_dict = dict()
    pos_dict['p0'] = p0
    print('p0:' + str(p0[0]) + ', ' + str(p0[1]))
    pos_dict['p1'] = p1
    print('p1:' + str(p1[0]) + ', ' + str(p1[1]))
    pos_dict['p2'] = p2
    print('p2:' + str(p2[0]) + ', ' + str(p2[1]))
    pos_dict['p3'] = p3
    print('p3:' + str(p3[0]) + ', ' + str(p3[1]))
    pos_dict['p4'] = p4
    print('p4:' + str(p4[0]) + ', ' + str(p4[1]))
    pos_dict['p5'] = p5
    print('p5:' + str(p5[0]) + ', ' + str(p5[1]))
    pos_dict['p6'] = p6
    print('p6:' + str(p6[0]) + ', ' + str(p6[1]))
    pos_dict['p7'] = p7
    print('p7:' + str(p7[0]) + ', ' + str(p7[1]))
    pos_dict['p8'] = p8
    print('p8:' + str(p8[0]) + ', ' + str(p8[1]))
    pos_dict['p9'] = p9
    print('p9:' + str(p9[0]) + ', ' + str(p9[1]))
    pos_dict['p10'] = p10
    print('p10:' + str(p10[0]) + ', ' + str(p10[1]))
    
    return pos_dict

# 描写
def write_turtle(kame, pos_dict, color1='blue', color2='yellow'):
    
    kame.shapesize(1)
    
    point = pos_dict['p' + str(len(pos_dict) - 1)]
    kame.setpos(point[0], point[1])
    kame.color(color1, color1)
    kame.pendown()
    kame.begin_fill()
    for pos in range(len(pos_dict)):
        point = pos_dict['p' + str(pos)]
        kame.setpos(point[0], point[1])
    kame.end_fill()
    kame.penup()
    
    kame.setpos(511 - pos_dict['p' + str(len(pos_dict) - 1)][0], 511 - pos_dict['p' + str(len(pos_dict) - 1)][1])
    kame.color(color2, color2)
    kame.pendown()
    kame.begin_fill()
    for pos in range(len(pos_dict)):
        point = pos_dict['p' + str(pos)]
        kame.setpos(511 - point[0], 511 - point[1])
    kame.end_fill()
    kame.penup()

# main
if __name__ == "__main__":
    
    l = 64
    
    kame = Turtle()
    pos_dict = create_pos_dict(kame, l)
    write_turtle(kame, pos_dict)
    
    
    
    
    
    k=input()

