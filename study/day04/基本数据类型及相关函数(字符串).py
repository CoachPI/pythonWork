#字符串的创建可以用'' 或者""
import random

str='我真的是太帅了';str1="但是没有我帅"
print('甲：'+str+"\n乙："+str1)
#python不支持单字符类型，单字符也是按字符串来使用
#py中字符串按方括号[]来截取语法如下：str[x:y]截取x到y下标之间的字符串，不包括y下标，
#字符串截取正序从0开始，倒序从-1开始
str2='abcdefgh'
print(str2[0:])#从第一位截取到最后一位
print(str2[:])#截取整个字符串
print(str2[:-1])#截取到最后一个字符串之前
print(str2[1:6])#截取下标1到下标5之间的字符串
print(str2[-1:])#从后面截取最后一个字符串
print(str2[::-1])#倒序字符串
#字符串更新，因为字符串是不可变的，所以要改变只能是截取拼接
print(str2[0:7]+str)

#py转义字符
#  \在末尾时表示续行符
print('djksaljd\
ajsdlkjsal\
djasldlk')

# \\反斜杠  \'单引号  \"双引号  \a响铃执行后电脑有铃声  \b退格  \000 空  \n换行
print('\\');print('\'');print('\"');print('\a');print('ssss \bdddd');print('\000');print('aa\ndd')
#\v 纵向制表符  \t 横向制表符  \f换页
print('aaa \v bbb');print('aaa \t bbb');print('aaa \f bbb')
# \r 回车，将 \r 后面的内容移到字符串开头，并逐一替换开头部分的字符，直至将 \r 后面的内容完全替换完成。
print('aaaa\rbb')
#\yyy 八进制数，y 代表 0~7 的字符，例如：\012 代表换行。
print("\110\145\154\154\157\40\127\157\162\154\144\41")
# \xyy 十六进制数，以 \x 开头，y 代表的字符，例如：\x0a 代表换行
print("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21")

#py字符串运算符
str2='abcdefgh'
print('aaa'+'bbb')#+拼接
print(str2*2)# *代表重复 数字代表重复的次数
print(str2[4]) #通过索引获取下标的字符串
print(str2[1:4])# 截取 遵循左闭右开原则
#in  not in 判断指定字符串是否在字符串中
print('a' in str2);print('z' not in str2)
# r/R 输出原石字符串。转义字符也原样输出
print(r'stradasda\n')

#字符串格式化  %s
print('我叫%s,今年%s岁'%('hjy','16'))
#%c 格式化字符及其ASCII码
print('今年%c岁'%('a'))
#%d 格式化整数
print('今年%d岁'%(-16.0))
#%u格式化无符号整型
print('今年%u岁'%(16.0))
# %f 格式化浮点型
print('今年%.1f岁'%(16.2))
# %e %E 用科学技术法格式化
print('今年%e岁'%(16.0));print('今年%E岁'%(16.0))
# %g %f和%e简写 %G %f和%E简写
print('今年%g岁'%(16.0))
#格式化辅助操作符
print('今年%.2f岁'%(16.2))#.定义宽度和精度
print('%+f岁'%(16.59845))# + 正数前显示+号
print('%#o'%16);print('%#x'%16)#  # 在八进制数前显示0 在十六进制数前显示0x

#三引号
str5='''
这是一个多行字符串
制表符tab（\t）
换行符（\n）
'''
print(str5)

# f-string python3.6 之后版本添加的，称之为字面量格式化字符串，是新的格式化字符串的语法。
#可以替代%用法
#f-string 格式化字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去，实例如下：
name='hjy';age=18;List=[1,5,8,9];dict1={1:'dsdsd',2:'adads'}
print(f'名字:{name},年龄{age},爱好的数字{random.choice(List)},喜欢的字母{dict1[1]}')
#在 Python 3.8 的版本中可以使用 = 符号来拼接运算表达式与结果：
a=1
print(f'{a+1=}')
#python的字符串内建函数
#str.capitalize()将字符串的第一个字符转为大写
print('abc'.capitalize())
#str.center(width,fillchar)方法返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
#如果字符串宽度小于width 则用fillchar去填充
print('分割线'.center(60,'-'))

#str.ljust(width,fillchar);str.rjust(width,fillchar) 左对齐和右对齐，指定宽度并用指定字符填充
print('左对齐'.ljust(50,'*'));print('右对齐'.rjust(50,'*'))

#str.count(sub,start=,end=) 统计字符串sub在字符串中出现的次数，start和end代表范围
print('aaaaccccaadddd'.count('a',0,2))
# 编码str.encode(’utf-8‘),解码str.encode(’utf-8‘).decode(’utf-8‘,'strict')
str555='我真帅'
str555=str555.encode('utf-8')
str666=str555.decode('utf-8','strict')
print(f'UTF-8编码:{str555 },UTF-8解码{str666}')

#str.endswith(__suffix=,__start=,__end=) 判断字符串是否以某个字符串结尾，可选参数start end代表字符串的范围,如果是返回True否返回False
#suffix可以是元素
str='abcdksleoioaaa'
list1=['aaa','bbb','5']
print(str.endswith('aaa'));print(str.endswith(list1[2]));print(str.endswith('aaa',11,14))
#str.expandtabs(x) 将字符串中\t用空格表示不传参则加上前面的字符串默认8个位置
str='shsh\thshs\thshs'
print(str.expandtabs());print(str.expandtabs(2))
#str.find(str, beg=0, end=len(string)) 判断字符串中是否包含子字符串，包含返回第一个索引下标，不包含返回-1，可以圈定范围
#同理还有str.rfind()从右边开始找
str='aajdjdjdlkaalsl'
print(str.find('aa'));print(str.find('aa',7,10));print(str.rfind('aa'))
#index(str, beg=0, end=len(string)) 与find一样只不过不包含会返回异常
#同理还有str.rindex()从右边开始找
print(str.index('aa'));print(str.rindex('aa'))
#str.isalnum()判断字符串是否由数字和字母组成 str.isalpha()判断字符串是否只由字母和文字组成
str='assd111-'
str1='aaasss111'
str2='sss哈哈哈'
str3='ss哈哈1'
print(str.isalnum());print(str1.isalnum())
print(str3.isalpha());print(str2.isalpha())
#str.isdigit() 判断是否只由数字组成  str.islower()判断是否只由小写字母构成
#str.isspace()判断是否只由空格 str.isupper判断是否只由大写字母构成

#str.istitle()判断字符串是否是标题
#如果字符串中所有的单词拼写首字母是否为大写，且其他字母为小写则返回 True，否则返回 False.
str = "This Is String Example...Wow!!!"
print(str.istitle())

str = "This is string example....wow!!!"
print(str.istitle())

#join() 将指定序列用指定分隔符连接起来
list1=['1','8','5','6']
set1={'1','5','8','sss'}
tup1=('1','5','6')
print('-'.join(list1));print('+'.join(set1));print('0'.join(tup1))
#len()返回字符串长度
print(len(str))

#str.lower()将字符串中的字母转为小写  str.upper()将字符串中的字转为大写
str='aaaBBB111'
print(str.lower());print(str.upper())

#str.lstrip()截掉字符串左边的空格 str.rstrip()截掉字符串右边的空格
str='   sssss';str1='sss   '
print(str.lstrip());print(str1.rstrip())

#str.maketrans(intab,outtab) 建立字符串的映射表。intab为输入，outtab为输出
str='asd';str1='123'
str3='asssddda'
trans=str3.maketrans(str,str1)
print(trans)
print(str3.translate(trans))

#max(str)返回字符串中最大的字母，min(str)返回字符串中最小的字母 比较的是ASCII码大小
str='abcdefG'
print(max(str),ord('f'));print(min(str))

#str.replace(__old=,__new=,max) 用指定字符串替换原字符串，如果有max则替换不超过max次
str='abccccaaaa'
print(str.replace('a',' ',2))

#str.split('',num) 指定某个字符进行分割，如果有num则分割成num+1个字符
#返回的是个序列
str='1,5,6,6,8,4,89,8'
print(str.split(','));print(str.split(',',2))

#str.startswith(sub,__start=,__end=) 检查字符串是否以指定字符串开头，是则True 否则False，start和end则是指定范围
str='abcffgdd'
print(str.startswith('abc'));print(str.startswith('abc',1,5));print(str.startswith('abc',0))

#str.strip('s')移除字符串首尾的指定字符串只能移除首尾不能移除中间的
str='----ad-asd-asd-as-da-sd-as-das-----'
print(str.strip('-'))
#str.swapcase()  将字符串中大小写互转
str='aaabbbcccAAAASSSDD'
print(str.swapcase())
#str.title()  返回标题化字符串即首字母大写
#非字母的第一个字母转为大写
str='sss2aa2a8ggg'
print(str.title())

#str.translate() 翻译str.maketrans()制作的映射表
str1='abcd';str2='1234'
str3='aabbccddeeffgg'
transtab=str3.maketrans(str1,str2)
str3=str3.translate(transtab)
print(str3)
#str.zfill(width) 返回指定宽的字符串，不够右对齐前面填0
str='abc'
print(str.zfill(10))

#str.isdecimal() 检查字符串是否只汗十进制数字 返回true false
str='165480xAA'
print(str.isdecimal())

