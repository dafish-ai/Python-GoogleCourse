# '''
# 样例1：字符串
# '''
#
# # 字符串
# name = "大鱼AI"
#
# # 1.连接：+
# name1 = "我爱"
# name2 = "大鱼AI"
# # 连接name1 与 name2
# print(name1 + name2)
# '''
# 输出为：我爱大鱼AI
# '''
#
# # 2.重复输出:*
# print(name2 * 3)
# '''
# 输出为：大鱼AI大鱼AI大鱼AI
# '''
#
# # 3.高级操作：replace，spilt
# # str.replace(old, new)
# # 样例：将str1中的 爱 替换成 喜欢
# str1 = "我爱大鱼AI"
# str2 = str1.replace("爱", "喜欢")
# print(str2)
# '''
# 输出为：我喜欢大鱼AI
# '''
#
# # str.split(str, num)
# # str:分隔字符串样式，默认为空格  num:分隔次数，默认为-1,即全部
# # 样例：将字符串str1按空格分隔成为列表
# str1 = "我 爱 大鱼AI"
# list1 = str1.split(" ")
# print(list1)
# '''
# 输出为：['我', '爱', '大鱼AI']
# '''
#
# # 4.索引，替换
# str1 = "我爱大鱼AI"
# # 索引：取字符串第二个元素
# print(str1[1])
# '''
# 输出为：爱
# '''
# # 替换
# # str1[1] = "喜欢"  报错：'str' object does not support item assignment
#
# # 5.字符串格式化
# str1 = "欢迎来到大鱼AI"
# print("字符串格式化使用百分号：%s" % str1)
# print("字符串格式化使用中括号：{}".format(str1))
# '''
# 输出为：字符串格式化使用百分号：欢迎来到大鱼AI
#         字符串格式化使用中括号：欢迎来到大鱼AI
# '''
#
# # 列表
# list1 = ["Python", "Java", "大鱼AI"]
#
# # 1.索引
# print("我爱"+list1[0])
# # 2.添加：append
# list1.append("Html")
# print(list1)
# '''
# 输出为：我爱Python
#         ['Python', 'Java', '大鱼AI', 'Html']
# '''
#
# # 3.删除：remove pop
# list1.pop(2)  # 移除指定位置元素
# print(list1)
# list1.remove("Html")  # 移除指定元素
# print(list1)
#
# '''
# 输出为：['Python', 'Java', 'Html']
#         ['Python', 'Java']
# '''
#
# # 列表元素可修改
# list1[0] = "北京"
# print(list1)
# '''
# 输出为：['北京', 'Java']
# '''

# 元组
tuple1 = (1, 2, 3)

# 1.索引
print(tuple1[0])
'''
输出为：1
'''
# 2.修改（不可修改）
# tuple1[0] = 6
# 报错：'tuple' object does not support item assignment

# 序列转换
string1 = "我爱大鱼AI"
list1 = ["Python", "Java", "C++"]
tuple1 = (1, 2, 3)

# 字符串转变成列表
print(list(string1))
# 元组转变成列表
print(list(tuple1))
'''
输出为：['我', '爱', '大', '鱼', 'A', 'I']
        [1, 2, 3]
'''

# 字符串转变成元组
print(tuple(string1))
# 列表转变成元组
print(tuple(list1))
'''
输出为：('我', '爱', '大', '鱼', 'A', 'I')
        ('Python', 'Java', 'C++')
'''

# 列表转变成字符串
print(str(list1))
# 元组转变成字符串
print(str(tuple1))
'''
输出为：['Python', 'Java', 'C++']
        (1, 2, 3)
注意：这里的输出不是列表、元组，而是字符串
“['Python', 'Java', 'C++']” 和 “(1, 2, 3)”
'''

# 成员运输符：in or not in
string1 = "我爱大鱼AI"
if "大鱼" in string1:
    print("这里有大鱼")

if "Java" not in string1:
    print("我们是学习Python的仔")
'''
输出为：这里有大鱼
        我们是学习Python的仔
'''

# 身份运输符：is or not is
# 注意：is 用于判断两个变量引用对象是否为同一个，== 用于判断引用变量的值是否相等。
str1 = "AI"
str2 = "AI"
if str1 is str2:
    print("str1 与 str2引用的同一个对象")
str1 = "Python"
if str1 is not str2:
    print("str1修改后，str1与str2引用的不是同一个对象")
'''
输出为：str1 与 str2引用的同一个对象
        str1修改后，str1与str2引用的不是同一个对象
'''

