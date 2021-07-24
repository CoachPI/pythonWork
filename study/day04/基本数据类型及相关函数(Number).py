#Number 数字类型
#数字类型有 int整型  float 浮点型  complex复数  其中bool在python3中为整型的子类型，python3中整型不限制大小
#数字类型不允许改变，可以用del函数删除
import math
import random

int1=3
float1=2.1
complex1=2+4j
#del int1
print(int1,float1,complex1)
#也可以用16进制和8进制代表整型
int16=0xA55
int8=0o777
print(int8,int16)
#复数也可以用complex()表示
complex2=complex(5,6);print(complex2)
#数字的类型转换可以直接用类型当做函数，进行转换
Str1='123';Str2='456'
print(int(Str1));print(float(Str1));print(complex(Str1));print(complex(int(Str1),int(Str2)))

#数字的运算 + - * /
a=6;b=3;c=a+b;d=a*b;e=a/b
print(c,d,e)
#  '/' 一直都是返回一个浮点数，要想返回整型需要用 '//'
f=a//b;print(f)
#这里要注意 ‘//’ 是否返回整型海域分子分母的类型有关
aa=6.0;bb=2;print(aa//bb)
#  '%'  表示取余
g=a%b;print(g)
# '**' 表示幂运算
print(a**b)
# 变量必须定义才能使用，不然会报错，不同类型的数进行运算时，整型会转成浮点型

#数字函数
#abs(x) 返回x的绝对值; math.ceil(x)返回x的向上取整；exp(x)返回常量e的x次幂
inta=-4.3;print(abs(inta))
intb=4.7;print(math.ceil(intb),math.ceil(inta))
intc=2;print(math.exp(intc))
intd=-3
#math.fabs(x) 返回x的绝对值，返回值为浮点型；math.floor(x)返回x的向下取整;math.log(x)返回x的对数；log10(x)返回以10为基数,x的对数
print(math.fabs(intd));print(math.floor(inta));print(math.log(math.e),math.log(100,10));print(math.log10(100))
#max(x1,x2...) 返回给定参数的最大值，min(x1,x2...)返回给定参数的最小值，可以为序列
List1=[5,8,6];List2=[3,8,9]
print(max(List1),min(List2));print(max(Str1,Str2))
#modf(x)返回x的整数部分和小数部分，整数部分和小数部分的符号与x相同，整数部分用浮点型表示
print(math.modf(intb))
#pow(x,y)表示x**y的值
print(math.pow(intd,intc))
#round(x,n)返回x的四舍五入值，如给出n则代表舍入到小数点后的位数，
intaa=5.1236985;print(round(intaa,5))
#sqrt(x)返回x的平方根
intbb=9;print(math.sqrt(intbb))

#随机数函数
#random.choice(),从序列的元素中随机挑选一个元素，例如random.choice(range(10))表示0-9中随机一个整数
Lista=[1,'hhh'];print(random.choice(Lista))
a=10;print(random.choice(range(a)))
# Seta={1,8,7,5};print(random.choice(Seta))

#random.randrange(start,stop,step)方法返回指定递增基数集合中的一个随机数，基数默认值为1。
# start -- 指定范围内的开始值，包含在范围内。
# stop -- 指定范围内的结束值，不包含在范围内。
# step -- 指定递增基数。
#在0-100中选取一个偶数
print(random.randrange(0,100,2))
#在1-100中选取一个奇数
print(random.randrange(1,100,2))
#在0-99中选取一个数
print(random.randrange(100))

#random.random()随机生成下一个实数，他在[0,1)之间
print(random.random())
#seed(x) x可以为任意数字，在调用随机数函数时先调用seed(),会生成同一个随机数
#seed()调用后，之后的random函数都只会生成相同的随机数
random.seed(13)
print(random.random())
#random.shuffle(list)将序列的所有元素随机排序
random.shuffle(List1)
print(List1)
#random.uniform(x,y)随机生成一个实数，它在x与y之间
print(random.uniform(4,9))
