#python中的循环语句有 for 和while
#while循环实例
a=10
while a>0:
    print(a)
    a-=1
#计算1到100的和
n=100
sum=0
count=1
while count<=n:
    sum+=count
    count+=1
print(sum)
#可以通过设置表达式不为false来实现无限循环,可以用ctrl+c来退出无限循环
var=0
while var:
    a=int(input('请输入一个数:\n'))
    print('你输入的数是:%d'%a)
    if a==0:
        var=a
print('end')

#while循环使用else条件
a=10
while a>0:
    print(a)
    a-=1
else:
    print('a小于0了')

#for循环
#Python for 循环可以遍历任何可迭代对象，如一个列表或者一个字符串。
for i in [1,5,6,8,7,9,5]:
    print(i)
#break语句可用于跳出当前循环提
for i in [1,5,6,8,4,2,3]:
    print(i)
    if i==5:
        break
else:
    print('无循环数据')
print('循环已结束')
#range() 如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列
for i in range(6):#同样的遵循左闭右开原则，从开始
    print(i)
#也可以指定范围
for i in range(2,4):
    print(i)
#也可以指定增数
for i in range(0,10,2):
    print(i)
#增数也可以是负数
for i in range(0,-10,-2):
    print(i)

#可以把range()和序列结合起来使用
list1=['小明','小红','张三','李四']
for i in range(len(list1)):
    print('学号:%d'%i,'姓名:%s'%list1[i])

#break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
#continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。

for i in list1:
    if i=='张三':
        print('%s你是犯人你被捕了'%i)
        break
    print('%s你是好人你可以走'%i)

a=10
while a>0:
    a-=1
    if a==2:
        continue
    print(a)
else:
    print('结束了')
a=10
while a>0:
    a-=1
    if a==2:
        break
    print(a)
else:
    print('结束了')

#冒泡排序
list2=[6,8,9,4,2,1,7,4,5]
for i in range(len(list2)):
    for j in range(i+1,len(list2)):
        if list2[j]<list2[i]:
            a=list2[i]
            list2[i]=list2[j]
            list2[j]=a
print(list2)