#for循环的基础语法
#while循环有条件，且可以自行控制        for循环是对一批内容进行逐一处理  所以也叫做遍历循环，无法定义循环条件
name = "nihaoya"
for x in name:
    print(x)
#无法构建无限循环


#内容为“ithejma is a brand of itcast"
#通过for循环遍历，统计有几个英文字母a
count = 0
name = "ithejma is a brand of itcast"
for x in name:
    if x == "a":
        count += 1
print(count)


#range语句    获得数字序列  发再被for循环使用
#for循环中的待处理数据集是序列类型，指的是内容可以逐次取出的一种类型，包括字符串列表元组
#range（num）,从0到num结束的数字序列，不包含num
#比如range（5）数据是【0，1，2，3，4】
#range（num1,num2）数据是从num1开始到num2结束的数字序列，不包含num2
#range(num1,num2,step)数据是从num1开始到num2结束的数字序列，不包含num2，数字之间的步长以step为准


#变量具有作用域


#for循环的嵌套
#用for循环输出九九乘法表
for x in range(1, 10):
    for y in range(1, x + 1):
        print(f"{y} * {x} = {y * x}\t", end='')
    print()


#循环的控制中断break和continue
#continue可用于for和while循环
for x in range(1, 10):
    #语句1
    continue
    #语句2
#这样子语句2就不会被执行  也是有作用域


#break   Continue是跳过，可以继续执行除了被跳过的，但是break是直接全部终止   依然是具有作用域


#综合案例
#完成发工资案例
#某公司账户余额有1w元，给20名员工发工资。员工编号从1--20，从编号1开始，依次领取工资，每人可以领取1000元。
#领取工资时财务会判断员工的绩效分（1--10）（随机生成）。如果低于5，不发工资，换下一位
#如果工资发完了，则结束发工资
import random
money = 10000
for y in range(1, 21):
    random_score = random.randint(1, 10)
    if random_score < 5:
        print(f"该员工{y}绩效分小于5分，不满足发工资要求，下一位！")
        continue
    if money >= 1000:
        money -= 1000
        print(f"该员工{y}绩效分大于5分，满足发工资要求！工资账户余额还剩下{money}元")
    else:
        print(f"余额不足，当前余额为{money}元，请下个月再来！")
        break