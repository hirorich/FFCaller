# 亀
from turtle import Turtle

import numpy as np
import cv2

# 座標リスト取得
def create_pos_dict(kame, l):
    
    kame.penup()
    
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

# 描写
def create_image(pos_dict, color1='blue', color2='yellow'):
    
    # 出力画像画素データ
    img_data = np.zeros((512, 512, 4), np.uint8)
    
    # ==================================================
    # 左半分を作成
    # y = ((p1y - p0y)x + p1x*p0y - p0x*p1y) / (p1x - p0x)
    # y = (dY*x + XY)/dX
    # ==================================================
    # dY = p1y - p0y
    dY_h = pos_dict['p3'][1] - pos_dict['p2'][1]
    dY_l = pos_dict['p0'][1] - pos_dict['p1'][1]
    
    # XY = p1x*p0y - p0x*p1y
    XY_h = pos_dict['p3'][0] * pos_dict['p2'][1] - pos_dict['p2'][0] * pos_dict['p3'][1]
    XY_l = pos_dict['p0'][0] * pos_dict['p1'][1] - pos_dict['p1'][0] * pos_dict['p0'][1]
    
    # dX =p1x - p0x
    dX_h = pos_dict['p3'][0] - pos_dict['p2'][0]
    dX_l = pos_dict['p0'][0] - pos_dict['p1'][0]
    for x in range(int(np.round(pos_dict['p2'][0])), int(np.round(pos_dict['p3'][0])+1)):
        y_h = int(np.round((dY_h * x + XY_h) / dX_h))
        y_l = int(np.round((dY_l * x + XY_l) / dX_l))
        img_data[y_l:y_h, x, (0, 3)] = 255
    # ==================================================
    # dY = p1y - p0y
    dY_h = pos_dict['p4'][1] - pos_dict['p5'][1]
    dY_l = pos_dict['p10'][1] - pos_dict['p9'][1]
    
    # XY = p1x*p0y - p0x*p1y
    XY_h = pos_dict['p4'][0] * pos_dict['p5'][1] - pos_dict['p5'][0] * pos_dict['p4'][1]
    XY_l = pos_dict['p10'][0] * pos_dict['p9'][1] - pos_dict['p9'][0] * pos_dict['p10'][1]
    
    # dX =p1x - p0x
    dX_h = pos_dict['p4'][0] - pos_dict['p5'][0]
    dX_l = pos_dict['p10'][0] - pos_dict['p9'][0]
    for x in range(int(np.round(pos_dict['p5'][0])+1), int(np.round(pos_dict['p4'][0])+1)):
        y_h = int(np.round((dY_h * x + XY_h) / dX_h)) - 1
        y_l = int(np.round((dY_l * x + XY_l) / dX_l)) + 1
        img_data[y_l:y_h, x, (0, 3)] = 0
    # ==================================================
    # dY = p1y - p0y
    dY_h = pos_dict['p7'][1] - pos_dict['p6'][1]
    dY_l = pos_dict['p8'][1] - pos_dict['p9'][1]
    
    # XY = p1x*p0y - p0x*p1y
    XY_h = pos_dict['p7'][0] * pos_dict['p6'][1] - pos_dict['p6'][0] * pos_dict['p7'][1]
    XY_l = pos_dict['p8'][0] * pos_dict['p9'][1] - pos_dict['p9'][0] * pos_dict['p8'][1]
    
    # dX =p1x - p0x
    dX_h = pos_dict['p7'][0] - pos_dict['p6'][0]
    dX_l = pos_dict['p8'][0] - pos_dict['p9'][0]
    for x in range(int(np.round(pos_dict['p6'][0])), int(np.round(pos_dict['p7'][0])+1)):
        y_h = int(np.round((dY_h * x + XY_h) / dX_h))
        y_l = int(np.round((dY_l * x + XY_l) / dX_l))
        img_data[y_l:y_h, x, (0, 3)] = 255
    # ==================================================
    # Turtle は左下が原点、opencv は左上が原点なので上下反転
    img_data = np.flipud(img_data)
    
    # 上下左右反転したものを右半分に張り付け
    img_data += np.flip(img_data, (0, 1))[:, :, (1, 0, 0, 3)]
    
    # 画像出力
    cv2.imwrite('./icon/icon_512x512.png', img_data)

# main
if __name__ == "__main__":
    
    l = 64
    
    # Turtle設定
    kame = Turtle()
    kame.getscreen().setworldcoordinates(0, 0, 511, 511)
    kame.shapesize(1)
    kame.shape('turtle')
    kame.speed(10)
    
    # 座標取得
    pos_dict = create_pos_dict(kame, l)
    
    # 座標確認
    write_turtle(kame, pos_dict)
    
    # 画像出力
    create_image(pos_dict)
    
    #k=input()

