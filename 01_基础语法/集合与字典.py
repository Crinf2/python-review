#集合
#不支持元素的重复，即自带去重功能，且内容无序
#集合使用大括号
set_1 = {1, 2, 2, 3}
print(set)#即使事先将集合中的元素写重复，打印出来仍然是去重的
#空的集合定义         变量名称 = set()
my_set = {"三国演义", "红楼梦", "西游记", "水浒传", "三国演义", "红楼梦", "西游记", "水浒传"}#内容无序
my_set_empty = set()
print(my_set)
print(my_set_empty)


#集合不支持下标索引访问，允许修改
#添加新元素 add
my_set.add("蜡笔小新")
print(my_set)
#移除元素 remove
my_set.remove("蜡笔小新")
print(my_set)
#随机取出一个元素 pop  随机取出
element = my_set.pop()#每次取出都随机
print(element, my_set)
#清空集合 clear
my_set.clear()
print(my_set)
#取两个集合的差集，得到一个新集合，原来两个集合不变，差集  集合1.diffrence(集合2)，即集合1有而集合2没有的
set_3 = {1, 2, 2, 3, 5}
set_4 = {1, 2, 3, 4}
set_5 = set_3.difference(set_4)
print(set_5)
#消除两个集合的差集         集合1.diffrence_update(集合2)    在集合1中删除和集合2相同的元素
set_3.difference_update(set_4)
print(set_3)
#两个集合合并成一个   union     集合1.union(集合2)
set_6 = set_3.union(set_4)
print(set_6)#自动去重
#统计集合的元素量     len
#集合的遍历         while循环不可以，因为不支持下标索引


#信息去重   有一列表对象my_list=['黑马程序员','传智播客','黑马程序员','传智播客','itheima','itcast','itheima','itcast','best']
#定义一个空集合   通过for循环遍历列表,在for循环中将列表 的元素添加至集合，最终得到元素去重的集合对象，并打印输出
my_list=['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast', 'best']
my_sett = set()
for i in my_list:
    my_sett.add(i)
print(my_sett)


#字典
#按照key找到value
my_dict = {"张继科": "最速大满贯", "马龙": "超级全满贯"}
#空字典 dict = {}   或者 dict = dict()
print(my_dict["张继科"])
#嵌套字典
#key不可为字典