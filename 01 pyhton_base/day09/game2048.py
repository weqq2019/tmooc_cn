"""
    2048 核心算法
"""
list_merge = [2, 0, 2, 2]


# 练习1：定义函数,将list_merge中0元素移动到末尾
# 测试：
# [2,0,2,0] -->  [2,2,0,0]
# [2,0,8,4] -->  [2,8,4,0]
def zero_to_end():
    # 思想：从后向前,删除0元素,追加0元素.
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


# 测试
# zero_to_end()
# print(list_merge)

# 练习2：定义函数,将list_merge中相同元素进行合并
# 测试：
# [2,0,2,0] --> [2,2,0,0] -->  [4,0,0,0]
# [2,0,0,2] --> [2,2,0,0] -->  [4,0,0,0]
# [2,2,2,0] -->  [4,2,0,0]
# [2,0,2,2] -->  [2,2,2,0] -->[4,2,0,0]
# [2,2,2,2] -->  [4,4,0,0]
def merge():
    # 思想：相邻相同则合并(后一个元素累加到前一个之上,删除后面元素,追加0)
    zero_to_end()
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]
            list_merge.append(0)


# 测试
# merge()
# print(list_merge)
map = [
    [2, 0, 0, 2],
    [0, 4, 0, 2],
    [0, 4, 2, 0],
    [2, 0, 2, 0],
]


# 练习3：定义函数,将map向左移动
# 思路：将每行数据赋值给list_merge，再调用merge函数进行合并数据.
def move_left():
    global list_merge
    for line in map:
        list_merge = line
        merge()


# move_left()
# print(map)# ？

# 练习4:定义函数,将map向右移动
# 核心思想：将map每行翻转后,
#         赋值给list_merge,再调用merge函数进行合并数据.
#         ...
def move_right():
    global list_merge
    for line in map:
        #  line[::-1] 创建新列表
        list_merge = line[::-1]
        merge()
        line[::-1] = list_merge

move_right()
print(map)
