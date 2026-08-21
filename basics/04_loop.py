"""
讲解循环的语法和用法
"""

import time


def showLoop():
    for i in range(1, 6):
        print("hi, +", i)
        time.sleep(1)

    total = 0
    for j in range(10):
        if j % 2 == 0:
            total += j
    print("sum of even numbers:", total)

    j = 0
    while j < 5:
        print("while loop: ", j)
        j += 1


if __name__ == "__main__":
    showLoop()
