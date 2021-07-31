#字典
# 字典是另一种可变容器模型，且可存储任意类型对象。
# 字典的每个键值 key-value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中 ,格式如下所示：
dict1={'name':'hjy','age':22,'sex':'男'}
print(dict1)
#键必须是唯一的，但值则不必。
# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字。
# 一个简单的字典实例：
dict2={'name':'hjy',98:'A'}
print(dict2)
#访问字典里的值，把相应的键放入到方括号中，如下实例:
print(dict2['name'],dict1['age'])
#修改字典，向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例：
dict3={'name':'hjy','age':22,'sex':'男'}
dict3['name']='hhh'
print(dict3)
#删除字典，clear()会清空字典，单字典对象还在，只不过是一个空字典，del会删除字典对象
del dict3['name']#删除name键
print(dict3)

#字典键的特性
#字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。
# 两个重要的点需要记住：
# 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：
dict4={'name':1,"name":2}
print(dict4)
#2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如下实例：
dict5={(1,2,3):'hjy','[1,2,3]':3}
print(dict5)

#字典的迭代
dict6={1:2,2:3,3:4}
for x in dict6.keys():
    print(x)
for y in dict6.values():
    print(y)

#字典的内置函数
#dict.clear() 清空字典内所有元素
dict7={'1':1,'2':2,'3':3}
dict7.clear()
print(dict7)
#dict.copy() 返回一个字典的浅拷贝
dict7={'1':1,'2':2,'3':3}
dict8=dict7.copy()
print('7的内存地址 %s'%id(dict7),'7的内容:',str(dict7))
print('8的内存地址 %s'%id(dict8),'8的内容:',str(dict8))
#dict.fromkeys(seq[, value])创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值。
list1=['name','age','sex']
tup1=(1,2,3)
dict9=dict.fromkeys(tup1,list1)
print(dict9)
#dict.get(key,default=)返回指定键的值，如果不存在则用给定的默认值
testd={'name':1,'age':2,'sex':3}
print(testd.get('age'));print(testd.get('sss','na'))
#key in dict  键在字典中返回True 不在返回false
print('name' in testd);print('sss' in testd)

#dict.items()以列表返回视图对象，是一个可遍历的key/value 对。
#dict.keys()、dict.values() 和 dict.items() 返回的都是视图对象（ view objects），提供了字典实体的动态视图，这就意味着字典改变，视图也会跟着变化。
#视图对象不是列表，不支持索引，可以使用 list() 来转换为列表。
#我们不能对视图对象进行任何的修改，因为字典的视图对象都是只读的。
print(testd.items());print(list(testd.items()))
#dict.items() 遍历
for x,y in testd.items():
    print(' %s'%x,'%s'%y)

#dict.values(),dict.keys() 返回键和值得视图对象

print(testd.keys());print(testd.values())

#遍历
for x in testd.keys():
    print('keys为%s'%x)
for y in testd.values():
    print('values为%s'%y)

del testd['name']
print(testd.items())#dict_items([('age', 2), ('sex', 3)])

#dict.pop(key[,default])删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
testd1={'name':1,'age':2,'sex':3}
print(testd1.pop('name','闪了'));print(testd1)
#dict.popitem()随机返回并删除字典中的最后一对键和值。
#如果字典已经为空，却调用了此方法，就报出KeyError异常。 按照 LIFO（Last In First Out 后进先出法） 顺序规则，即最末尾的键值对。
testd2={'name':1,'age':2,'sex':3}
print(testd2.popitem());print(testd2)

#课后练习
country={}
def add(con):
    if con in country:
        country[con]+=1
    else:
        country[con]=1

add('China')
add('Japan')
add('China')
add('USA')
print(country);print(len(country))