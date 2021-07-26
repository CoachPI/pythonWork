# 序列是 Python 中最基本的数据结构。
# 序列中的每个值都有对应的位置值，称之为索引，第一个索引是 0，第二个索引是 1，依此类推。
# Python 有 6 个序列的内置类型，但最常见的是列表和元组。
# 列表都可以进行的操作包括索引，切片，加，乘，检查成员。
# 此外，Python 已经内置确定序列的长度以及确定最大和最小的元素的方法。
# 列表是最常用的 Python 数据类型，它可以作为一个方括号内的逗号分隔值出现。
# 列表的数据项不需要具有相同的类型
# 创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。如下所示：
List1=[1,8,9,7,5]
List2=['1','6','7','8']
List3=['1',8,'hjhyj',9]
print(List1,'\n',List2,'\n',List3)

#与字符串的索引一样，列表索引从 0 开始，第二个索引是 1，依此类推。
#通过索引列表可以进行截取、组合等操作。倒序访问从-1开始
print(List1[-1]);print(List2[2]);print(List3[3])
#同样也可以和字符串一样使用方括号截取列表 截取原则左闭右开
print(List1[1:3]);print(List2[:]);print(List3[:-1])

#可以通过获取列表的值来对列表进行修改，也可以用append（）方法新增
List1[2]=10
List2[3]=1
List3[0]='8'
print(List1);print(List2);print(List3)
List1.append(List2)
print(List1)
#也可以使用del方法删除列表中的元素
del List1[-1]
print(List1)
#列表的操作符
#+代表组合两个列表
print(List1+List2)
#len()返回列表长度
print(len(List1))
#*代表列表重复
print(List1*2)
# in \not in  判断元素是否在列表中
print(1 in List1);print(1 not in List1)
#for x in List :迭代
for i in List1:
    print(i)

#列表的拼接和截取
List4=List1+List3
List5=List1[0:2]+List2[1:3]
List5 +=List1
print(List4);print(List5)

#列表的嵌套，可以在列表中传入其他列表
List6=[List1,List2]
print(List6);print(List6[0]);print(List6[0][3])

#max()返回列表中的最大值，min（）返回列表中的最小值，len（）返回列表长度，list（）将元组转换为列表
print(max(List1));print(min(List1));print(len(List3))
#list.count(x)统计某个元素在列表中出现的次数
list1=[1,8,4,6,3,2,3,3];list2=['1','6','6','3']
print(list1.count(2));print(list2.count('6'))

#list.extend(seq)在列表末尾一次性增加一个序列中的多个值
list3=list(range(5))
list1.extend(list3)
print(list1)
#list.index(x,start,end)找出列表中某个元素第一次出现的索引
print(list1.index(8));print(list2.index('6',1,3))
#list.insert(index,obj)在列表的指定索引插入元素
list1.insert(1,'1')
print(list1)
#list.pop(index)移除列表中的元素 默认最后一个
print(list1.pop())
print(list1)
print(list1.pop(2))
print(list1)

#list.remove(obj) 移除某个值得第一个匹配项
list7=['dsada','dad','aaa','bbb','bbb']
list7.remove('aaa')
list7.remove('bbb')
print(list7)
#list.reverse()反向列表
list7.reverse()
print(list7)
#list.sort(key=None, reverse=False)对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
#排序规则，reverse = True 降序， reverse = False 升序（默认）。
#字母按
list7.sort()
print(list7)
list7.sort(reverse=True)
print(list7)
#拓展将原列表中的字母转为大写，并降序
list8 = []
for i in list7:
    i=i.upper()
    list8.append(i)
    list8.sort(reverse=True)
print(list8)


list8=['一','二','三','死']
list8.sort(reverse=False)
print(list8)

#list.clear()清空列表
list8.clear()
print(list8)
#list.copy() 复制列表
list9=list7.copy()
print(list9)

#拓展 给定一个数字列表 输出由列表里的数字构成所有的三维坐标
listAA=[1,2,3,4]
listBB=[(x,y,z) for x in listAA for y in listAA for z in listAA ]
print(listBB)

#拓展 给定一个字符串列表 输出由列表里的字符串构建的语句
listC=['小明','小红','男','女',13,14]
listD=[('姓名：'+x+'性别：'+y+'年龄'+str(z)) for x in listC if x=='小明' for y in listC if y=='男' for z in listC if z==14]
listE=[('姓名：'+x+'性别：'+y+'年龄'+str(z)) for x in listC if x=='小红' for y in listC if y=='女' for z in listC if z==13]
print(listD);print(listE)
