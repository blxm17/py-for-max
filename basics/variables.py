"""
展示变量的使用方法和基本类型。
"""

def showBasics():
    # 变量示例
    age = 10  # 整数变量
    name = "Alice"  # 字符串变量
    height = 5.7  # 浮点数变量

    # 常量示例
    PI = 3.14159  # 数学常量
    MAX_VALUE = 100  # 最大值常量

    print("My name is", name)
    print("I am", age, "years old")
    print("My height is", height, "feet")
    print("PI is approximately", PI)
    print("The maximum value is", MAX_VALUE)

    # 不同进制
    print(0b100)  # 二进制整数
    print(0o100)  # 八进制整数
    print(100)    # 十进制整数
    print(0x100)  # 十六进制整数

    print(123.456)    # 数学写法
    print(1.23456e2)  # 科学计数法

    # 判定变量类型
    a = 100
    b = 123.45
    c = 'hello, world'
    d = True
    print(type(a))  # <class 'int'>
    print(type(b))  # <class 'float'>
    print(type(c))  # <class 'str'>
    print(type(d))  # <class 'bool'>

    # 类型转换
    a = 100
    b = 123.45
    c = '123'
    d = '100'
    e = '123.45'
    f = 'hello, world'
    g = True
    print(float(a))         # int类型的100转成float，输出100.0
    print(int(b))           # float类型的123.45转成int，输出123
    print(int(c))           # str类型的'123'转成int，输出123
    print(int(c, base=16))  # str类型的'123'按十六进制转成int，输出291
    print(int(d, base=2))   # str类型的'100'按二进制转成int，输出4
    print(float(e))         # str类型的'123.45'转成float，输出123.45
    print(bool(f))          # str类型的'hello, world'转成bool，输出True
    print(int(g))           # bool类型的True转成int，输出1
    print(chr(a))           # int类型的100转成str，输出'd'
    print(ord('d'))         # str类型的'd'转成int，输出100

if __name__ == "__main__":
    # 这里可以添加一些测试代码
    showBasics()  # 测试输出
