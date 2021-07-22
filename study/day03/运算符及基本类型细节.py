#成员运算符 in  not in
List1=[1,5,8,'hhhh']#列表
set1=set('abcdgfee5sa')#集合
set2={5,"dddd",5}#集合
tup1=(1,8,6,'dasdas',[1,5,8])#元组
dict1={'name':1,'age':2,'sexy':'5'}#字典
print(List1,set1,set2,tup1,dict1)
print(tup1[-1])
if 5 in List1:
    print(str(5)+'在列表中')
else:
    print(str(5)+'不在列表中')

if str(5) in set1:
    print(str(5)+'在集合中')
else:
    print(str(5)+'不在集合中')

if 5 in tup1:
    print(str(5)+'在元组中')
else:
    print(str(5)+'不在元组中')

if str(5) not in dict1.values():
    print(str(5)+'不在字典中')
else:
    print(str(5)+'在字典中')

#身份运算符用于比较两个对象的存储单元 is \  is not
a=20;b=30
if a is b:
    print('相同')
else:
    print('不同')
if a is not b:
    print('不同')
else:
    print('相同')
b=20
if a is b:
    print('相同')
else:
    print('不同')

if a is not b:
    print('不同')
else:
    print('相同')
#is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
x=[1,5,8,9]
y=x
print(id(x))
print(id(y))#id()获取内存地址
if x is y:
    print(True)
else:
    print(False)
if x == y:
    print(True)
else:
    print(False)

y=x[:]
print(id(x))
print(id(y))
if x is y:
    print(True)
else:
    print(False)
if x == y:
    print(True)
else:
    print(False)

x=[1,5,8]
y=[1,5,8]
print(id(x))
print(id(y))
if x is y:
    print(True)
else:
    print(False)
if x == y:
    print(True)
else:
    print(False)

#or and and比or优先级高
#python 中的 and 从左到右计算表达式，若所有值均为真，则返回最后一个值，若存在假，返回第一个假值；
# or 也是从左到有计算表达式，返回第一个为真的值；
# 其中数字 0 是假，其他都是真；
# 字符 "" 是假，其他都是真；
x=True
y=False
z=False
print(x or y);print(x and y);print(z or y and x)

#计算一个整数转为二进制包含的1的个数
def NumberOf1(n):
    # write code here
    cnt = 0
    if n < 0:
        n = n & 0xffffffff
    while n:
        cnt += 1
        n = (n - 1) & n
    return cnt
if __name__=='__main__':
    s=NumberOf1(7)
    print(bin(7))
    print(s)

def hammingWeight(self, n: int) -> int:
    ret = 0
    while n:
        n &= n - 1
        ret += 1
    return ret
print(bin(9))
print(hammingWeight(0,9))
