import math
import pickle
import pprint


#repr()： 产生一个解释器易读的表达形式。
for x in range(1,11):
    print(repr(x*x*x))

s='aaa\nbbb'
print(s)
#repr()会自动转义字符中的转义字符
print(repr(s))#输出 aaa/nbbb
print(str(s))# 输出 aaa
             #     bbb
#repr()的参数可以使python中的任一类型
list1=[1,3,'f']
dict1={1:'1',2:'2',3:'3'}
str1='sssmmdd\n'
number1=6
print('list1:',repr(list1),'\ndict1:',repr(dict1),'\nstr1:',repr(str1),'\nnumber1:',repr(number1))

print('数'.rjust(2),'平方'.rjust(3),'立方'.rjust(4))
for x in range(1,11):
    print(repr(x).rjust(2),' ',repr(x*x).rjust(3),' ',repr(x*x*x).rjust(4))
    # print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # 注意前一行 'end' 的使用
    # print(repr(x*x*x).rjust(4))

#format()的使用
print('{}{}'.format('我是','你爹'))
#可以通过给定序号确定format输出的值
print('{1}{0}'.format('你爹','我是'))
#如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数。
print('姓名：{name},年龄：{age}{1}{0}'.format('ggg','hhh',name='你爹',age=18))
#!a (使用 ascii()), !s (使用 str()) 和 !r (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
print('{!s}'.format('nnn\nbbb'));print('{!r}'.format('nnn\nbbb'))

#可选项 : 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后三位：
print('π保留三位小数{0:.3f}'.format(math.pi))
#在 : 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
table={'小红':15,'小明':16,'小林':14}
for name,age in table.items():
    print('{0}==>{1:10}'.format(name,age))

#input()从键盘输入一个值
# a=input('请输入一个值：')
# print('输入的是：',a)

#open() 将会返回一个 file 对象，基本语法格式如下:  open(filename, mode)
#filename：包含了你要访问的文件名称的字符串值。
#mode：决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
#f=open('新建文本文档.html','a+')
#f.write('新增文本文字jsjsjsjjsj')
#f.close()
f=open('测试文档.txt','r+',encoding='utf-8')
sss=f.write('str((\'dddd\',123) \nsjsjsjsjs' )
f.close()
print(sss)

f1=open('新建文本文档.html','r',encoding='utf-8')
f2=open('测试文档.txt','r+',encoding='utf-8')
str=f1.read()
#f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
str1=f2.readline()
print(str);print(str1)
#f.readlines() 将返回该文件中包含的所有行。
#如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。
str2=f2.readlines()
print(str2)
f1.close();f2.close()

#文件对象也可以迭代
f3=open('测试文档.txt','r+',encoding='utf-8')
for line in f3:
    print(line,end='-\n')
f3.close()
#如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。
# from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：
# seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
# seek(x,1) ： 表示从当前位置往后移动x个字符
# seek(-x,2)：表示从文件的结尾往前移动x个字符

f4=open('测试文档.txt','r+',encoding='utf-8')
str4=f4.seek(5,0)
print('输出',str4)

#python的pickle模块实现了基本的数据序列和反序列化。
# 通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
# 通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
# 基本接口：pickle.dump(obj, file, [,protocol])  x = pickle.load(file)

dict2={'a':[1,5,6,'4']
       ,'b':('s',1,'ddd')
       ,'c':15}
list2=[1,'55',22,3]
output=open('测试文档2.pkl','wb')
pickle.dump(dict2,output)
pickle.dump(list2,output,-1)
output.close()

pkl_file = open('测试文档2.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()



