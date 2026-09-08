#循环语句  基于条件的判断  条件是判断或者布尔类型
#while循环
#像喜欢的人表白，每天表白一次，持续100天
time = 0
day = 1
while time < 100:
    print("今天是第%d天，你好，我真的很喜欢你！" % day)
    day += 1
    time += 1


#求1--100的和
a = 1
sum = 0#!!!!!!!!!!!!!!!!!!!!!
while a <= 100:
    sum += a
    a += 1
print(sum)


#while循环的基础案例
#1--100随机数，循环猜数字

import random
num = random.randint(1, 100)
count = 0
while True:
    guess_num = int(input("请输入你猜测的数字：\n"))
    count += 1
    if guess_num == num:
        print("猜中了！")
        break
    else:
        if guess_num > num:
            print("猜大了！")
        else:
            print("猜小了！")
print("你一共猜了%d次" % count)


#while循环的嵌套           #换行\n,不换行end=''   !!!!!!!!!!!!!!!!!!!!!!!!!!!
#打印九九乘法表
#制表符  \t
a = 1
while a <= 9:
    b = 1
    while b <= a:
        print(f"{b} * {a} = {b * a}\t", end='')
        b += 1
    a += 1
    print()