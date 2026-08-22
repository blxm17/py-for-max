def showListUsage():
    """
    展示Python列表常用操作示例 (含列表推导式与切片)
    返回: None（用于演示输出）
    """
    
    # ================== 1. 创建不同方式列表 ==================
    print("【1. 创建列表】")
    list1 = []                      # 空列表
    list2 = [1, 2, 3]              # 数字列表
    list3 = ["apple", "banana"]    # 字符串列表
    list4 = list(range(5))         # range()生成列表
    list5 = list("Python")         # 字符串转列表

    # 【新增】列表推导式：最强大的列表创建方式
    squares = [x**2 for x in range(1, 6)]          # 基础推导
    evens = [x for x in range(10) if x % 2 == 0]  # 带条件过滤
    
    print(f"空列表:          {list1}")
    print(f"数字列表:        {list2}")
    print(f"字符串列表:      {list3}")
    print(f"范围列表:        {list4}")
    print(f"字符列表:        {list5}")
    print(f"平方推导：{squares}")
    print(f"偶数过滤：{evens}")


    # ================== 2. 添加与修改元素 ==================
    print("\n【2. 添加与修改元素】")
    list1.append(4)                # 添加单元素到末尾
    list1.extend([5, 6])           # 添加多个元素
    list1.insert(2, "inserted")    # 指定位置插入

    print(f"合并后列表: {list1}")
    list1[3] = "updated"           # 修改索引元素
    print(f"修改后列表: {list1}")


    # ================== 3. 删除元素 ==================
    print("\n【3. 删除元素】")
    removed = list1.pop()          # 移除并返回末尾元素
    print(f"弹出最后元素: {removed}")

    del list1[1]                   # 按索引删除
    print(f"删除后列表: {list1}")


    # ================== 4. 合并与拼接 ==================
    print("\n【4. 合并与拼接】")
    a = [1, 2]
    b = [3, 4]
    result_add = a + b            # 连接生成新列表
    
    c = [5, 6, 7]
    d = []
    d.extend([10])
    d.extend(a)
    
    print(f"使用+合并: {result_add}")
    print(f"extend合并: {d}")


    # ================== 5. 遍历列表 ==================
    print("\n【5. 遍历列表】")
    for i in list1:
        print(i, end=" ")

    print("\n索引遍历:")
    for idx, val in enumerate(list1):
        print(f"{idx}: {val}")


    # ================== 6. 常用方法 ==================
    print("\n【6. 常用方法】")
    
    # append() - 追加单个元素
    e = list1.copy()
    e.append(8)
    print(f"append后: {e}")
    
    # extend() - 添加多个元素
    f = [9, 10]
    g = [1, 2]
    result_extend = f + g
    print(f"extend合并: {result_extend}")
    
    # clear() - 清空列表
    list1.clear()
    print(f"clear后: {list1}")


    # ================== 7. 排序与翻转 ==================
    print("\n【7. 排序与翻转】")
    nums = [6, 3, 8, 2]
    sorted_nums = sorted(nums)     # 返回新列表
    nums.sort(reverse=True)        # 原地排序并反向
    
    print(f"sort后: {nums}")

    list4.reverse()
    print(f"reverse后：{list4}")


    # ================== 8. 删除与替换 ==================
    print("\n【8. 删除与替换】")
    items = [1, 2, 3]
    items.remove(2)                # 按值删除
    print(f"remove后：{items}")

    items[0] = 999                # 替换索引元素
    print(f"replace后：{items}")


    # ================== 9. 常用方法速查 ==================
    print("\n【9. 常用列表方法总结】")
    methods = {
        'append': '添加单个元素',
        'extend': '合并多个子列表',
        'insert': '指定位置插入',
        'pop': '弹出末尾或索引元素',
        'remove': '删除指定值',
        'clear': '清空列表',
        'sort': '排序（原地修改）',
        'reverse': '翻转顺序',
    }

    print(f"{'方法名':12} | {'功能描述':15}")
    for method, desc in methods.items():
        print(f"{method:12} | {desc:15}")


    # ================== 10. 综合操作示例 (含切片) ==================
    print("\n【10. 综合列表操作 & 切片】")
    final_list = [10, 20, 30, 40, 50]
    
    # 显式演示切片：start:end:step
    sub1 = final_list[1:4]      # 取中间部分
    sub2 = final_list[::-1]     # 完全反转 (等同于 reverse)
    sub3 = final_list[::2]      # 每隔一个取一个
    
    print(f"原列表：{final_list}")
    print(f"切片 [1:4]: {sub1}")
    print(f"切片 [::-1] (反转): {sub2}")
    print(f"切片 [::2] (隔项): {sub3}")


# ================== 主程序演示 ==================
if __name__ == "__main__":
    showListUsage()