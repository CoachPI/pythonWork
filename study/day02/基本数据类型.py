#python允许为多个变量复制
a=b=c=d=5
print(a,b,c,d)
a,b,c=1,3.0,"hhh"
print(a,b,c)
# Python3 中有六个标准的数据类型：
#
# Number（数字）
# String（字符串）       不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# List（列表）             可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
# Tuple（元组）
# Set（集合）
# Dictionary（字典）
#Number
a,b,c,d=1,True,2.0,2+4j
print(type(a),type(b),type(c),type(d))#type()函数显示类型
print(isinstance(a,int))#isinstance判断类型
# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。
#当你指定一个值时，Number 对象就会被创建：您也可以使用del语句删除一些对象引用。
del a;del b
#print(a,b,c,d)#NameError: name 'a' is not defined
class A:
    print(1)

class B(A):
    print(2)
print(isinstance(A(),A))
print(type(A())==A)
print(isinstance(B(),A))
print(type(B())==A)

#Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加 True==1，False==0 是会返回 Ture，但可以通过 is 来判断类型
if 1 == True:
    print(1==True)
else:
    print(1==False)
#数值运算
print(1*2,end="-");print(4/2,end="-");print(4//2,end="-");print(2**3)
#1、Python可以同时为多个变量赋值，如a, b = 1, 2。
# 2、一个变量可以通过赋值指向不同类型的对象。
# 3、数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
# 4、在混合计算时，Python会把整型转换成为浮点数。 Python还支持复数，复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型

#String 字符串
str1="Lucy-animal"

print(str1[0:-4])
print(str1[:5])
print(str1*2)
print(str1[0:9:2])
#与 C 字符串不同的是，Python 字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误。
#python字符串不可变
print(str1[5])

#List 索引值与String字符串一样，正序0开始，倒序-1开始
List=[1,2,3.0,"LUCY"]
print(List);print(List[0:3])
#加号 + 是列表连接运算符，星号 * 是重复操作
List2=[6.0,5,4,"HAPPY"]
print(List+List2);print(List*2)
#与Python字符串不一样的是，列表中的元素是可以改变的：
List[0]=4
List[1:4]=[9,6,"hjy"]
print(List);print(List[-1::-1])
#1、List写在方括号之间，元素用逗号隔开。
# 2、和字符串一样，list可以被索引和切片。
# 3、List可以使用+操作符进行拼接。
# 4、List中的元素是可以改变的。

#拓展 翻转字符串
def revertString(abc):
    _翻转字符串_=abc[::-1]
    return _翻转字符串_

if __name__ == "__main__":
    abc='abcde'
    rw=revertString(abc)
    print(rw)

#Tuple 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
#元组中的元素类型也可以不相同：
tup=(1.5,4+5j,'jjdjdjdj')
print(tup);print(tup[:]);print(tup[0:3]);print(tup[::-1])
#tup[0]=2 修改元组内数据会报错 TypeError:'tuple' object does not support item assignment
#print(tup)
#虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
#构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
tup1=()#空元组
tup2=(20,)#一个元素的元组
print(tup1+tup2)
#ps1、与字符串一样，元组的元素不能修改。
# 2、元组也可以被索引和切片，方法一样。
# 3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
# 4、元组也可以使用+操作符进行拼接。

#set（集合）
#集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
# 基本功能是进行成员关系测试和删除重复元素。
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
# 创建格式：
set1={9,6,"jdjdj"}
set2=set("ddd")
print(set1);print(set2)
#set可自动去重
set3={"123",123,"123",5,8,123,"321"}
print(set3)
#判断元素是否在set中
a=6#input('请输入：')
if int(a) in set3:
    print(str(a)+"在set中")
else:
    print(str(a)+"不在set中")

#set可以进行集合运算
_集合1_=set('asdsacvxzcz')
_集合2_=set('gjlasjdioscz')
print(_集合2_);print(_集合1_)
print(_集合2_-_集合1_)#差集
print(_集合2_|_集合1_)#并集
print(_集合2_&_集合1_)#交集
print(_集合2_^_集合1_)#两个集合中不同时存在的元素

#Dictionary 字典
#字典（dictionary）是Python中另一个非常有用的内置数据类型。
# 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
# 键(key)必须使用不可变类型。
# 在同一个字典中，键(key)必须是唯一的。
dict={'name':'hhh',2:12,'sexy':'男'}
print(dict);print(dict[2]);print('姓名：'+dict['name']+'-年龄：'+str(dict[2])+'-性别：'+dict['sexy'])

