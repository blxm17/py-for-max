"""
展示运算符，优先级等知识。
"""


def showOperators():
    print(321 + 12)  # 加法运算，输出333
    print(321 - 12)  # 减法运算，输出309
    print(321 * 12)  # 乘法运算，输出3852
    print(321 / 12)  # 除法运算，输出26.75
    print(321 // 12)  # 整除运算，输出26
    print(321 % 12)  # 求模运算，输出9
    print(321**12)  # 求幂运算，输出1196906950228928915420617322241

    # 优先级
    print(2 + 3 * 5)  # 17
    print((2 + 3) * 5)  # 25
    print((2 + 3) * 5**2)  # 125
    print(((2 + 3) * 5) ** 2)  # 625

    # 赋值运算符
    a = 10
    b = 3
    a += b  # 相当于：a = a + b
    a *= a + 2  # 相当于：a = a * (a + 2)
    print("a =", a)  # 大家算一下这里会输出什么
    # 赋值运算构成的表达式本身不产生任何值，所以下面注释掉的代码是错误的
    # print(a=10)
    # 为了解决这个问题，引入了海象运算符 :=
    print((a := 10))  # 10

    # 比较运算符和逻辑运算符
    flag0 = 1 == 1
    flag1 = 3 > 2
    flag2 = 2 < 1
    flag3 = flag1 and flag2
    flag4 = flag1 or flag2
    flag5 = not flag0
    print("flag0 =", flag0)  # flag0 = True
    print("flag1 =", flag1)  # flag1 = True
    print("flag2 =", flag2)  # flag2 = False
    print("flag3 =", flag3)  # flag3 = False
    print("flag4 =", flag4)  # flag4 = True
    print("flag5 =", flag5)  # flag5 = False
    print(flag1 and not flag2)  # True
    print(1 > 2 or 2 == 3)  # False

    # 格式化输出
    x = 1.236
    print("The value of x is %.1f" % x)  # 方法1
    print(f"The value of x is {x:.2f}")  # 方法2
    print(f"The value {x = :.2f}")  # 方法3


if __name__ == "__main__":
    showOperators()
