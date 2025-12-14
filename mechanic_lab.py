list_a = [1, 2, 3]  # 第一步：创建列表
list_b = list_a  # 第二步：将 list_a 赋值给 list_b
list_a[0] = 999  # 第三步：修改 list_a
print(list_b)  # 第四步：打印 list_b
print(id(list_a))  # 第五步：查看 list_a 的内存地址
print(id(list_b))  # 第五步：查看 list_b 的内存地址
# my_str = "Python"
# my_str[0] = "J"
# try:
#     # 假设你想修改字符串中的某个字符，像这样：
#     s = "Python"
#     s[0] = "J"  # 这会引发 TypeError，因为字符串是不可变的
# except TypeError:
#     # 捕获 TypeError 并输出错误信息
#     print("字符串是不可变的，不能直接修改！")
# 修改后的代码
try:
    my_str = "Python"
    my_str[0] = "J"
except TypeError:
    print("字符串是不可变的，不能直接修改！")

#  - 思考题（写在注释里）：如果我想把 "Python" 变成 "Jython"，正确的代码应该怎么写？
# s = "Python"
# s = "J" + s[1:]  # 通过拼接字符串来创建新的字符串
# print(s)  # 输出 "Jython"
# 修改后的代码
s = "Python"
s = "J" + s[1:]
print(s)


# 定义一个有坑的函数
def bad_append(item, list_argument=[]):
    list_argument.append(item)
    return list_argument
代码解释稍后。。。。。

print(bad_append("Apple"))  # 第一次：往盒子里放 Apple
print(bad_append("Banana"))  # 第二次：还是同一个盒子，再放 Banana
print(bad_append("Cherry"))  # 第三次：还是同一个盒子，再放 Cherry
