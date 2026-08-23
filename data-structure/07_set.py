def showSetUsage():
    """
    展示Python集合(set)常用操作示例 (含集合推导式与集合操作)
    返回: None(用于演示输出)
    """

    # ================== 1. 创建不同方式集合 ==================
    print("【1. 创建集合】")
    set1 = set()  # 空集合
    set2 = {1, 2, 3}  # 数字集合
    set3 = {"apple", "banana"}  # 字符串集合
    set4 = {1, 2, 2, 3}  # 去重后的集合
    set5 = set("Python")  # 字符串转集合

    # 【新增】集合推导式：最强大的集合创建方式
    even_numbers = {x for x in range(10) if x % 2 == 0}  # 基础推导

    print(f"空集合:          {set1}")
    print(f"数字集合:        {set2}")
    print(f"字符串集合:      {set3}")
    print(f"去重集合:      {set4}")
    print(f"字符集合:        {set5}")
    print(f"偶数推导：{even_numbers}")

    # ================== 2. 添加与修改元素 ==================
    print("\n【2. 添加与修改元素】")
    set1.add(4)  # 添加单个元素
    set1.update([5, 6])  # 添加多个元素
    set1.add("inserted")  # 指定位置插入

    print(f"合并后集合: {set1}")
    set1.remove("inserted")  # 删除元素
    print(f"删除后集合: {set1}")

    # ================== 3. 删除元素 ==================
    print("\n【3. 删除元素】")
    removed = set1.pop()  # 移除并返回任意元素
    print(f"弹出任意元素: {removed}")

    set1.discard(2)  # 按值删除，不报错
    print(f"discard后集合: {set1}")

    # ================== 4. 合并与拼接 ==================
    print("\n【4. 合并与拼接】")
    a = {1, 2}
    b = {3, 4}
    result_union = a.union(b)  # 返回新集合
    a.update(b)  # 原地合并

    print(f"union合并: {result_union}")
    print(f"update合并: {a}")

    # ================== 5. 遍历集合 ==================
    print("\n【5. 遍历集合】")
    for item in set1:
        print(item, end=" ")

    print("\n集合元素:")
    for item in set1:
        print(item)

    # ================== 6. 常用方法 ==================
    print("\n【6. 常用方法】")

    # add() - 添加单个元素
    e = set1.copy()
    e.add(8)
    print(f"add后: {e}")

    # update() - 合并多个子集合
    f = {9, 10}
    g = {1, 2}
    result_union = f.union(g)
    print(f"union合并: {result_union}")

    # clear() - 清空集合
    set1.clear()
    print(f"clear后: {set1}")

    # ================== 7. 排序与翻转 ==================
    print("\n【7. 排序与翻转】")
    nums = {6, 3, 8, 2}
    sorted_nums = sorted(nums)  # 返回新集合
    nums = sorted(nums, reverse=True)  # 原地排序并反向

    print(f"sort后: {nums}")

    # set本身没有reverse方法，但可以转换为列表再翻转
    nums_list = list(nums)
    nums_list.reverse()
    nums = set(nums_list)
    print(f"reverse后：{nums}")

    # ================== 8. 删除与替换 ==================
    print("\n【8. 删除与替换】")
    items = {1, 2, 3}
    items.remove(2)  # 按值删除
    print(f"remove后:{items}")

    items.add(999)  # 替换索引元素
    print(f"replace后:{items}")

    # ================== 9. 常用方法速查 ==================
    print("\n【9. 常用集合方法总结】")
    methods = {
        "add": "添加单个元素",
        "update": "合并多个子集合",
        "remove": "删除指定值",
        "discard": "删除指定值，不报错",
        "clear": "清空集合",
        "union": "并集（返回新集合）",
        "intersection": "交集（返回新集合）",
        "difference": "差集（返回新集合）",
        "symmetric_difference": "对称差集（返回新集合）",
    }

    print(f"{'方法名':12} | {'功能描述':15}")
    for method, desc in methods.items():
        print(f"{method:12} | {desc:15}")

    # ================== 10. 综合操作示例 ==================
    print("\n【10. 综合集合操作】")
    final_set = {10, 20, 30, 40, 50}

    # 显式演示集合操作：交集、并集、差集等
    set2 = {20, 30, 40}
    set3 = {10, 30, 50}

    intersection = final_set.intersection(set2)
    union = final_set.union(set3)
    difference = final_set.difference(set2)
    symmetric_difference = final_set.symmetric_difference(set3)

    print(f"原集合: {final_set}")
    print(f"交集: {intersection}")
    print(f"并集: {union}")
    print(f"差集: {difference}")
    print(f"对称差集: {symmetric_difference}")


# ================== 主程序演示 ==================
if __name__ == "__main__":
    showSetUsage()
