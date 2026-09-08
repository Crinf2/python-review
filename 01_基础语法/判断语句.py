#布尔类型的字面量True和False，True本质上是数字1，False是数字0
#比较运算符相等“==”，左侧大于右侧“>=”,左侧小于右侧“<=”


#判断语句  if  else
age_1 = int(input("你的年龄是：\n"))
age_2 = int(input("你同桌的年龄是：\n"))#input默认按照字符串，如果需要计算需要转化为整数
if age_1 < age_2:
    print(f"你同桌比你大{age_2 - age_1}岁")
else:
    print("你比你同桌大 %d岁" % (age_1 - age_2))


#if elif else多条件判断


#判断语句的嵌套   关键点在于空格的缩进
#必须年龄大于等于18岁且小于30岁，同时入职时间需满足2年，或者级别大于3才能领取
age = int(input("你的年龄是？\n"))
time_1 = int(input("你的入职时间是？\n"))
time_2 = int(input("你的级别是？\n"))
if age >= 18 and age < 30:
    print(f"你的年龄已经达标！")
    if time_1 > 2 or time_2 > 3:
        print("符合条件！")
    else:
        print("不符合条件！")
else:
    print("不符合条件！")


#猜数字    随机数字 import random
#                 num = random.randint(n,m)
import random
num = random.randint(1, 100)
