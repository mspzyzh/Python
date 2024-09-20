"""
数据类型

1. int     整数  （10，-10，0）
2. float   浮点  （13.14，5.20，-1.11）
3. complex 复数  （1+2j,以j结尾表示复数）
4. bool    布尔  （用于逻辑判断，true表示真记作1，false表示假记作0）
5. String  字符串 （字符串由任意数量字符组成，用作描述文本）
6. List    列表  （有序的可变序列，可有序记录一堆可变的python数据集合）
7. Tuple   元组  （有序的不可变序列，可有序记录一堆不可变的python数据集合）
8. Set     集合  （无序的不重复集合，可无序记录一堆不重复的python数据集合）
9. Dictionary  字典  （无序的Key-Value集合，可无序记录一堆Key-Value的python数据集合）
"""
# 为变量赋值
a1 = "牛马"
a2 = 18
a3 = 1.234

# 打印变量类型和变量值
print(type(a1),a1)
print(type(a2),a2)
print(type(a3),a3)

#数据类型转换
#整数浮点数转字符串
b2 = str(a2)
b3 = str(a3)
print(type(b2),b2)
print(type(b3),b3)

#字符串转整数
c2 = int(b2)
print(type(c2),c2)

#字符串转浮点数
c3 = float(b3)
print(type(c3),c3)

#整数浮点数互转
d2 = float(a2)
d3 = int(a3)
print(type(d2),d2)
print(type(d3),d3)