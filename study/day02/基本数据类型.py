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



