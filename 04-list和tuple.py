# list
# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。

list = [1,2,3,4,5,'a','b','c']
print(len(list))

for item in range(8):
    # comment: 
    print(list[item])
# end for

# 用索引来访问list中每一个位置的元素，索引是从0开始的,也可以从-1开始，直接获取最后一个元素。
print(list[-1])

# 可以使用append添加元素，使用insert插入元素，使用pop删除元素
list.append(6)
print(list)
# insert后为索引号
list.insert(3,33)
print(list)
list.pop()
print(list)
# pop后为索引号
list.pop(3)
print(list)

# tuple
# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改。
# tuple没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来。