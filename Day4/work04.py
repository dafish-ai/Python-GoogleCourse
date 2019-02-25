'''
函数作业讲解
'''

'''
作业一：
自己定义函数，实现与random.sample方法相同的功能
'''
"""
讲解：首先我们要了解random.sample函数的功能
random.py文件中是这样解释的：Chooses k unique random elements from a population sequence or set.
（从原序列或者集合中选择k个唯一的随机元素）
random.sample(population, k)
参数：
        population：原序列或集合
        k：选取随机数个数
返回数据类型：列表
"""
import random
def my_sample(population, k):
    # 第一步：数据转换，方便统一操作
    temp_population = list(population)
    # 第二步：判断溢出
    if not 0 < k < len(temp_population):    # 也可以写出  k<0 or k>len(temp_population)
        print("随机数个数输入错误，参数k数值错误！")
    # 第三步：生成随机数
    r_list = []   # 存储返回元素列表
    temp_list = []    # 存储返回元素下标列表
    for i in range(k):
        a0 = random.randint(0, k)  # 用random.randint生成随机整数下标
        if i == 0:
            temp_list.append(a0)
        while a0 in temp_list:   # 去除重复下标
            a0 = random.randint(0,k)
        temp_list.append(a0)
        r_list.append(temp_population[a0])
    return r_list


# 测试题一
my_list = my_sample([1,2,3,4,5,7,9,10,22],4)
print(my_list)
'''
输出：
[5, 3, 1, 2]
'''


'''
作业二：
自己定义函数，求取任意个整数中(即要求函数参数为可选参数)，最大的值
'''
"""
讲解：
这里我们要理解Python里函数的可变参数
可变参数：就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个
在参数前面加上*就是可变参数。在函数内部，可变参数接收得到的是一个tuple（元组）
"""
# 注意:这里的int_number实际是一个元组，不信你可以print(type(int_number))试试
def max_int(*int_number):
    # 最简单：调用max()函数
    # return max(int_number)

    # 自己比较大小
    temp = int_number[0]
    for i in range(1, len(int_number)):
        if int_number[i] > temp:
            temp = int_number[i]
    return temp

# 测试题二
a0 = max_int(5,2,3,4)
print(a0)
'''
运行结果：
5
'''

