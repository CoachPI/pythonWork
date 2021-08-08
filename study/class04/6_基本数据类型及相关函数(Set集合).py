# 集合（set）是一个无序的不重复元素序列。
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
set1={'1',5,5,6,'1'}
print(set1)
#集合的运算
set2={6,8,4,9,1,'2'}
print(set1-set2)#集合a中包含而集合b中不包含的元素
print(set1|set2)#集合a中包含或者集合b中包含的所有元素
print(set1&set2)#两个集合都包含的元素
print(set1^set2)#两个集合不同时存在的元素
print(5 in set1)#判断元素是否在集合中
#集合推导式
a={x for x in 'abcdefg' if x not in 'efg'}
b=set(x for x in 'abcdefg' if x not in 'abc')
print(a);print(b)
#集合的基本操作
#添加元素 set.add(x)将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作。
set1.add(9)
print(set1)
#还有一种方法 set.update(x) 参数可以是列表，元组，字典
#新增列表和元组时会将列表中的元素都拿出来放入集合，有存在的元素不新增
#新增字典时会将字典的键值对分别拿出放入集合中，有存在的元素不新增
set1.update([1,5,6])
#set1.update(['s'],('a'))
print(set1)
# set1.update((1,5,6))
set1.update({('j','h','g')})#这种方法是新增一个元组集合到集合中
print(set1)
set1.update({'name':1,'age':2})
print(set1)

#移除元素 set.remove(x)将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误。
set1.remove('name')
# set1.remove('a') 会报错
print(set1)
#此外还有一个方法也是移除集合中的元素，s.discard( x )且如果元素不存在，不会发生错误。
set1.discard('a')#不会报错
print(set1)

#也可以设置随机删除元素，set.pop()
set1.pop()
print(set1)#set 集合的 pop 方法会对集合进行无序的排列，然后将这个无序排列集合的左面第一个元素进行删除。

#计算集合元素个数 len(set)
print(len(set1))

#清空集合 set.clear(0
set2.clear()
print(set2)

#拷贝集合 这里是创建了一个新集合 与原集合无关了
set3=set1.copy()
set3.update('a')#{'1', 5, 6, ('j', 'h', 'g'), 'a', 9, 'age'}
print(set3);print(set1);print('set1内存地址%s'%id(set1),'set3内存地址%s'%id(set3))

#set.difference(set) 返回多个集合的差集
set2={6,8,4,9,1,'2'}
b=set3.difference(set1)#这里表示set3有set1没有的元素
c=set2.difference(set3)#这里表示set2有set3没有的元素
print(b);print(c)

#set.difference_update(set)用于移除两个集合中都存在的元素。
#difference_update() 方法与 difference() 方法的区别在于 difference() 方法返回一个移除相同元素的新集合，
# 而 difference_update() 方法是直接在原来的集合中移除元素，没有返回值。
set3.difference_update(set2)
print(set3)

#set.intersection(set1, set2 ... etc) 返回两个或更多集合中都包含的元素，即交集。
set3=set1.copy()
b=set3.intersection(set2,set1)
print(b)

#set.intersection_update(set)用于获取两个或更多集合中都重叠的元素，即计算交集。
#intersection_update() 方法不同于 intersection() 方法，因为 intersection() 方法是返回一个新的集合，
# 而 intersection_update() 方法是在原始的集合上移除不重叠的元素。
set3.intersection_update(set2,set1)
print(set3)

#set.isdisjoint(set)用于判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。。
set1={1,3,5,8}
set2={8,6,5,4,1,2}
print(set1.isdisjoint(set2))

#set.issubset(set)判断集合的所有元素是否都包含在指定集合中，如果是则返回 True，否则返回 False。
print(set1.issubset(set2))

#set.issuperset(set)判断指定集合的所有元素是否都包含在原始的集合中，如果是则返回 True，否则返回 False。
a={2,1,3,6,9,5,4,8}
b={1,2,3}
print(a.issuperset(b))

#set.symmetric_difference()方法返回两个集合中不重复的元素集合，即会移除两个集合中都存在的元素。
a={1,5,3,6}
b={1,2,3,5}
c=a.symmetric_difference(b)
print(c);print(a);print(b)

#set.symmetric_difference_update(set)与上面的方法等效只是在原集合中操作，而不是返回一个新集合
a.symmetric_difference_update(b)
print(a)

#set.union(set1,set2,set3) 返回并集
c=a.union(b)
print(c)