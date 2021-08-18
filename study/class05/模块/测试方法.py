def fib1(n):  # 定义到 n 的斐波那契数列
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b


def fib2(n):  # 返回到 n 的斐波那契数列
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

def fib3(n):
    result=[]
    if n==0:
        print('输入有误')
        return 0;

    if n==1 or n==2:
        return 1
    else:
        return fib3(n-1)+fib3(n-2)

def fib4(n):
    result=[]
    a,b=0,1
    while n>0:
        a,b=b,a+b
        n-=1
        result.append(b)
    return result