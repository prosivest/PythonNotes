# 变量

# 变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头，但不能以数字打头，例如，可将变量命名为message_1，但不能将其命名为1_message。
# 变量名不能包含空格，但可使用下划线来分隔其中的单词。例如，变量名greeting_message可行，但变量名greeting message会引发错误。
# 不要将Python关键字和函数名用作变量名，即不要使用Python保留用于特殊用途的单词，如print。
# 变量名应既简短又具有描述性。例如，name比n好，student_name比s_n好，name_length比length_of_persons_name好。
# 慎用小写字母l和大写字母O，因为它们可能被人错看成数字1和0。

a = 1
b = "123"
c = True
print(c)
c = 'yhm'
print(c)

# 这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。
# 例如Java是静态语言。


# 常量
# 所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量：
PI = 3.1415926
print(PI)
print(10/3)

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\'\n'
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Bob!'''

print(n,f,s1,s2,s3,s4)