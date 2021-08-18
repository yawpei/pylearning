from turtle import *

def drawSun():
    for i in range(8):
        # 开始填充颜色
        begin_fill()
        # 前进80步
        fd(80)
        # 向左120度
        lt(120)
        # 前进80步
        fd(80)
        # 向左120度
        lt(120)
        # 前进80步
        fd(80)
        # 向左143度
        lt(143)
        # 向下画半径为100的弧线 68步
        circle(-100, 68)
        # 结束填充
        end_fill()


def main():
    # 画笔颜色
    pencolor('#EEC211')
    # 画笔抬起
    pu()
    # 定位开始位置
    goto(-20, 100)
    # 画笔落下
    pd()
    # 设置朝向
    seth(0)
    # 设置颜色
    color('#EEC211')
    # 画太阳
    drawSun()
    # 中心部分上色
    begin_fill()
    left(12)
    circle(-145)
    end_fill()
    exitonclick()

main()
