#函数  组织好的，可重复使用的
#len是统计长度   py官方内置函数
#函数的使用
#在重复使用某一功能时，可以使用函数


#函数的定义
'''
def 函数名(传入参数):
    函数体
    return 返回值
'''


#函数的参数
def add(a,b):
    result = a + b
    print(result)
    return result
add(1,2)


#函数返回值，将函数的结果返回给函数的调用者
#调用函数时，加一个变量来表示
e = add(3,4)
print(e)


#None类型
#用于判断中None等同于False  ！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
def check_age(age):
    if age > 18:
        return "sucess"
    else:
        return None
resurt = check_age(16)
if not resurt:
    print("您是未成年！")


#函数的说明文档
#用多行注释进行说明，必须写在函数体之前
'''
def func(x,y)
    \'''
    :param x:形参x的说明
    :param y:形参y的说明
    :return:返回值的说明
    \'''
    函数体
    return 返回值
'''


#函数的嵌套调用


#函数中变量的作用域
#局部变量（即在函数中别定义的变量）和全局变量（函数外被定义的变量）
#在函数中修改全局变量，只有函数内部才能使用。但使用global关键字即可修改全局变量
num = 200
def test():
    global num
    num = 100
    print(num)
test()
print(num)

#函数的综合案例
name = None                                     #先定义一个全局变量
money = 5000000
name = input("请输入您的名字？\n")
def check(show_header):
    if show_header:
        print("-------------查询-------------")   #方便其他函数查询余额时直接调用且不输出这句话
    print(f"{name},您好，您的余额剩余：{money}元")
def in_(num_1):
    print("-------------存款-------------")
    global money
    money += num_1
    print(f"{name},您好，您存款{num_1}元成功")
    check(False)                                  #调用查询函数
def out(num_2):
    print("-------------取款-------------")
    global money
    money -= num_2
    print(f"{name},您好，您取款{num_2}元成功")
    check(False)
def menu():
    print("-------------菜单-------------")
    print(f"{name},您好欢迎来到xx银行ATM，请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择：\n")
while True:
    keyboard_input = menu()
    if keyboard_input == "1":
        check(True)
        continue         #通过continue进行下一次循环
    elif keyboard_input == "2":
        num_1 = int(input("您想存多少钱？\n"))
        in_(num_1)
        continue
    elif keyboard_input == "3":
        num_2 = int(input("您想取多少钱？\n"))
        out(num_2)
        continue
    else:
        print("程序已经退出！")
        break