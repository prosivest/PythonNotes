# 字符串及编码
#
# ASCII编码利用8bit也就是一个字节存储大小写英文字母、数字和一些符号。
# Unicode编码使用两个字节表示一个字符（如果要用到非常偏僻的字符，就需要4个字节）
# UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。
# 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。
# 用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件。
# 浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器。
#
# 最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言。
print("包含中文的str")

# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
# -*- coding: utf-8 -*-

print(ord("Y"))
print(chr(88))
print(ord("饕"))

""" 
Python的字符串类型是str,在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
Unicode表示的str可以通过encode方法编码为指定的bytes。
纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。
含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。
"""
print("YHM".encode("ascii"))
print("余浩淼".encode("UTF-8"))

# 如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：

print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))


# 字符串格式化
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数
print('Hi, %s, you have $%d.' % ('Michael', 1000000))
print('%4d-%04d' % (3, 1))
print('%.2f' % 3.1415926)
# 另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多：
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
s1 = 72
s2 = 85
r = (s2-s1)/s1*100
print('小明的成绩提升了%.1f%%' % r)
print('小明的成绩提升了{0:.2f}%'.format(r))
print(f"小明的成绩提升了{r:.2f}%")


# f-string 的用法
name = 'Alice'
age = 30

# 嵌入变量
print(f"用户 {name} 今年 {age} 岁。")
print(f"用户 {name=} 今年 {age=} 岁。")

# 嵌入表达式（计算）
print(f"十年后，她将是 {age + 10} 岁。")

# 嵌入函数调用
print(f"她的名字大写是：{name.upper()}")

# 格式化数字（例如，保留两位小数）
price = 49.99
print(f"价格是：${price:.2f}") 
