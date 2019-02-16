# 作业1 ： 打印Hello World
# 直接打印
print("Hello World")
# % 格式化打印
print("%s" % "Hello World")
# format函数格式化打印
print("{}".format("Hello World"))
"""
输出：  Hello World
        Hello World
        Hello World
"""

# 作业2 ：
"""
定义一个列表，包含自己的家庭成员名字，
定义完成后在你名字前加入"大鱼AI"，再
将"大鱼AI"这一名字删除，此时判断"
大鱼AI"是否在列表中。
"""
# 定义列表
my_family = ["爸爸", "妈妈", "我"]
# 插入"大鱼AI"在"我"前面
my_family.insert(2, "大鱼AI")
print(my_family)

# 删除"大鱼AI"
my_family.remove("大鱼AI")
print(my_family)

# 判断"大鱼AI"是否在列表中
if "大鱼AI" in my_family:
    print("大鱼AI在我家")
else:
    print("大鱼AI不在我家")
"""
输出为：
    ['爸爸', '妈妈', '大鱼AI', '我']
    ['爸爸', '妈妈', '我']
    大鱼AI不在我家
"""
