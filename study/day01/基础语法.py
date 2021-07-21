import keyword

#输出关键字
print(keyword.kwlist)
print("hello python")

#缩进行代替了大括号
if 1>2:
    print(True)
else:
    print(False)
  #print("aaaa")
#缩进不一致，会导致运行错误

_求和_=3\
     +4\
     +5
print(_求和_)
#python中数字有四种类型：整数、布尔型、浮点数和复数。 int bool float complex

#python中单引号和双引号使用完全相同。
# 使用三引号(''' 或 """)可以指定一个多行字符串。
# 转义符 \
# 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
# 按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
# 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
# Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
# Python中的字符串不能改变。
# Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
# 字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
str1='我是帅哥'
str2="我是美女"
str3="""我是大明星
print
djakldjklsa"""
str4="我是无敌的\n"
str5=r"我是无敌的\n"
str6=str1+str2
str7=str3*2
str8=repr(str4)#变量用repr()
print(str1,str2,str3,str4,str5,str6,str7,str8,end='\n')

_字符串_='123456789'

print(_字符串_[0:1])
print(_字符串_[-1])
print(_字符串_[2:])
print(_字符串_[0:-1:2])# 输出从第一个开始到第最后一个且每隔一个的字符（步长为2）

admin=input("请输入你的年龄\n")
if int(admin)>30:
    print("你可真老，已经"+admin+"岁了。")
else:
    print("你可真年轻，才"+admin+"岁")

print(_字符串_[0:1]);print(_字符串_[-1],end="-");print(_字符串_[2:])#同一行可显示多个语句，用分号分割

if int(admin)>18 and int(admin)<50:
    print("你已成年")
elif int(admin)<18 and int(admin)>0:
    print("你未成年")
else:
    print("你不是人")

#在 python 用 import 或者 from...import 来导入相应的模块。

# 将整个模块(somemodule)导入，格式为： import somemodule
#
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction
#
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
#
# 将某个模块中的全部函数导入，格式为： from somemodule import *

import sys
print(sys.path)
for i in sys.argv:
    print(i)

from sys import  argv,path
print(argv);print(path)
