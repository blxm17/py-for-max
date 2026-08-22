def demonstrate_tuple_comprehensive():
    """
    综合展示 Python 中元组 (tuple) 的核心特性：
    1. 与列表的区别（可变性）
    2. 切片操作（支持，返回新元组）
    3. 生成式的使用（作为输入源，需配合 tuple() 转换为元组）
    """
    
    print("=" * 50)
    print("Python 元组综合演示程序")
    print("=" * 50)

    # --- 1. 元组与列表的区别 (可变性) ---
    print("\n【特性一】不可变性对比")
    my_list = [1, 2, 3]
    my_tuple = (4, 5, 6)
    
    print(f"原始列表: {my_list} (类型: {type(my_list).__name__})")
    print(f"原始元组: {my_tuple} (类型: {type(my_tuple).__name__})")
    
    # 修改列表
    my_list[0] = 100
    print(f"修改后列表: {my_list}")
    
    # 尝试修改元组（会报错）
    try:
        my_tuple[0] = 100
    except TypeError as e:
        print(f"尝试修改元组失败: {e}")

    # --- 2. 切片操作 (支持，返回新元组) ---
    print("\n【特性二】切片操作")
    data_tuple = ('a', 'b', 'c', 'd', 'e')
    
    # 正向切片
    sub1 = data_tuple[1:4]
    print(f"切片 [1:4]: {sub1} (类型: {type(sub1).__name__})")
    
    # 反向切片
    sub2 = data_tuple[-2:]
    print(f"切片 [-2:]: {sub2}")
    
    # 注意：切片结果仍是元组，不可直接修改内容
    try:
        sub1[0] = 'X'
    except TypeError as e:
        print(f"尝试修改切片结果失败: {e}")

    # --- 3. 生成式的使用 (需配合 tuple()) ---
    print("\n【特性三】生成式与元组转换")
    
    # 错误示范：(x for x in ...) 是生成器，不是元组
    gen_obj = (x for x in range(5))
    print(f"生成器对象: {gen_obj} (类型: {type(gen_obj).__name__})")
    
    # 正确做法：使用 tuple() 将生成式转换为元组
    my_tuple_from_gen = tuple(x for x in range(5))
    print(f"转换后的元组: {my_tuple_from_gen} (类型: {type(my_tuple_from_gen).__name__})")
    
    # 也可以直接使用列表推导式配合 tuple()
    my_tuple_from_list = tuple([x * 2 for x in range(3)])
    print(f"从列表推导式转换的元组: {my_tuple_from_list}")

    # --- 4. 其他常见用法 ---
    print("\n【特性四】其他常用场景")
    
    # 作为字典键（必须是不可变类型）
    person = {"name": "Alice", "id": (1001, 2001)}
    print(f"元组作为字典键: {person['id']}")
    
    # 解包 (Unpacking)
    a, b, c = my_tuple_from_gen
    print(f"解包赋值: a={a}, b={b}, c={c}")
    
    # 默认参数值（推荐用元组避免修改）
    def greet(name, *args):
        return f"Hello {name}! Args: {args}"
    
    result = greet("World", "Python", "is", "great")
    print(f"函数解包调用: {result}")

if __name__ == "__main__":
    demonstrate_tuple_comprehensive()