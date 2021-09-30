import random, turtle, time

def drawGap():  # 绘制单段数码管间隔
    turtle.penup()
    turtle.fd(5)

def drawLine(draw):  # 绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.speed(10)
    turtle.fd(40)
    turtle.right(90)

def drawDigit(d):  # 根据数字绘制七段数码管
    drawLine(True) if d in ['-','2', '3', '4', '5', '6', '8', '9'] else drawLine(False)
    drawLine(True) if d in ['1', '3', '4', '5', '6', '7', '8', '9', '0'] else drawLine(False)
    drawLine(True) if d in ['2', '3', '5', '6', '8', '9', '0'] else drawLine(False)
    drawLine(True) if d in ['2', '6', '8', '0'] else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in ['0', '4', '5', '6', '8', '9'] else drawLine(False)
    drawLine(True) if d in ['2', '3', '5', '6', '7', '8', '9', '0'] else drawLine(False)
    drawLine(True) if d in ['1', '2', '3', '4', '7', '8', '9', '0'] else drawLine(False)
    turtle.right(180)
    turtle.penup()
    turtle.fd(20)

def drawNum(floor):  # 获得要输出的数字
    turtle.pencolor('black')
    for i in floor:
        drawDigit(i)
    turtle.write('F', font = ('Arial', 25, 'normal'))
    time.sleep(0.5)
    turtle.clear()
    turtle.goto(-50,0)

def drawNotice(n_floor,k):
    turtle.pencolor("black")
    turtle.goto(-100, 0)
    turtle.write('{}F Arrived, Door Open.'.format(n_floor), font=('Times New Roman', 25, 'normal'))
    time.sleep(3)
    turtle.clear()
    turtle.goto(-100, 0)
    turtle.write('Door Close, Start Off {}'.format(k), font=('Times New Roman', 25, 'normal'))
    time.sleep(3)
    turtle.clear()
    turtle.goto(-50,0)

def drawfloor(floor):
    turtle.write("当前在第{}层".format(floor), font=('Times New Roman', 18, 'normal'))
    time.sleep(1)
    turtle.clear()
    turtle.goto(-50, 0)

def trans(now_floor, list, ex_list):
    if list[0] == now_floor:
        list.remove(now_floor)
    if list[0] < now_floor:
        mid = min(list)
        fin = max(list)
        for j in range(now_floor, mid - 1, -1):
            if j in ex_list:
                continue
            else:
                drawNum(str(j))
            if j in list:
                list.remove(j)
                k = ''
                drawNotice(j, k)
        now_floor = mid
        if list != []:
            for k in range(now_floor, fin + 1, 1):
                if k in ex_list:
                    continue
                else:
                    drawNum(str(k))
                if k in list:
                    list.remove(k)
                    drawNotice(k,'')
            now_floor = fin
    else:
        mid = max(list)
        fin = min(list)
        for j in range(now_floor, mid + 1, 1):
            if j in ex_list:
                continue
            else:
                drawNum(str(j))
            if j in list:
                list.remove(j)
                k = ''
                drawNotice(j, k)
            now_floor = j
        now_floor = mid
        if list != []:
            for k in range(now_floor, fin - 1, -1):
                if k in ex_list:
                    continue
                else:
                    drawNum(str(k))
                if k in list:
                    list.remove(k)
                    drawNotice(k,'')
            now_floor = fin

"""
本程序模拟电梯运行：假设随机某楼层地下3层，地上22层(无0层，14层，18层)，随机产生电梯当前楼层与用户所在楼层，用户键入运送请求(通过回车多值键入)，电梯先到达产生请求
所在楼层，再先按第一位用户的请求楼层方向运行，该方向运行完毕后再运行逆方向的请求。其中，idle交互框为电梯控制台界面，turtle图框为乘客显示界面。
"""
def main():
    exclude_list = [0, 14, 18]
    key = True
    while key:
        now_floor = random.randint(-3, 22)                 #随机生成电梯当前所在楼层
        guests_floor=random.randint(-3, 22)                #随机生成乘客所在楼层
        if now_floor not in exclude_list and guests_floor not in exclude_list:
            key = False
    list = []
    print("当前电梯在第{}层，您在第{}层".format(now_floor, guests_floor))
    floor = input("请输入您要到达楼层'数字'(-3F至22F,无14F和18F)：")                       #乘客键入需要到达的楼层
    key = True
    while key:                                                                       #输入异常处理
        try:
            if floor != '' and isinstance(eval(floor), int) and eval(floor) >= -3 and \
                    eval(floor) <= 22 and (int(floor) not in exclude_list):
                list.append(floor)
                floor = input("输入成功，请继续输入：")
                if floor == '':
                    key = False
                    break
            else:
                if list[-1] == '':
                    key = False
                    break
                elif eval(floor) in exclude_list:
                    floor = input("本楼无0F, 14F和18F,请重新输入：")
                elif eval(floor) < -3:
                    floor = input("请重新输入-3F以上楼层:")
                elif eval(floor) > 22:
                    floor = input("请重新输入22F以下楼层:")
                else:
                    floor = input("输入错误，请重新输入:")
                    if floor == '':
                        break
        except:
            if floor == '':
                break
            floor = input("输入错误，请重新输入:")
            if floor == '':
                key = False
    print("名义楼层：",list)

    list2=[]                                                                    #实际楼层确认
    for i in list:
        if eval(i) >=19:
            list2.append(str(eval(i) - 2))
        elif 14 <eval(i) <18:
            list2.append(str(eval(i) - 1))
        else:
            if i in list2:
                continue
            else:
                list2.append(i)
    print("实际楼层：" ,list2)

    #乘客界面模拟电梯运行
    list3 = []
    for i in list:
        if eval(i) in list3:
            continue                                #数据去重
        else:
            list3.append(eval(i))
    list = list3

    turtle.setup(450,225)                           #用户界面框
    turtle.screensize(300, 400, "lightblue")
    turtle.penup()
    turtle.goto(-50,0)
    turtle.pensize(5)
    turtle.pencolor('black')
    if guests_floor > now_floor and len(list) != 0:             #电梯到达用户所在楼层
        drawfloor(str(now_floor))
        for i in range(now_floor,guests_floor + 1, 1):
            if i in exclude_list:
                continue
            else:
                drawNum(str(i))
        drawNotice(guests_floor, '')
        now_floor = guests_floor
        trans(now_floor, list, exclude_list)                   #送至目标楼层

    elif guests_floor < now_floor and len(list) != 0:
        drawfloor(str(now_floor))
        for i in range(now_floor, guests_floor - 1, -1):
            if i in exclude_list:
                continue
            else:
                drawNum(str(i))
        drawNotice(guests_floor, '')
        now_floor = guests_floor
        trans(now_floor, list, exclude_list)

    else:
        if len(list) == 0:
            pass
        else:
            drawfloor(str(now_floor))
            trans(now_floor, list, exclude_list)
    print("运行结束。")
main()
