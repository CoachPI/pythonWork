#斐波那契数列
a,b=0,1
while b<10:
    a,b=b,a+b
    print(a,b)

#第一行包含了一个复合赋值：变量 a 和 b 同时得到新值 0 和 1。最后一行再次使用了同样的方法，可以看到，右边的表达式会在赋值变动之前执行。右边表达式的执行顺序是从左往右的。

def fab(n):
    if n<1:
        print('输入有误！')
        return -1
    if n==1 or n==2:
        return 1
    else:
        return fab(n-1)+fab(n-2)
print(fab(3))