# if else
#请输入两个数判断大小
a=int(input('请输入第一个数:\n'))
b=int(input('请输入第二个数:\n'))
if a>b:
    print('第一个数比较大')
elif a<b:
    print('第二个数比较大')
else :
    print('两个数一样大')

#输入两个数并输出其中的偶数
a1=int(input('请输入第一个数:\n'))
b1=int(input('请输入第二个数:\n'))
if a1%2==0:
    for i in range(a1,b1,2):
        print(i)
elif a1%2!=0:
    for i in range(a1+1,b1,2):
        print(i)