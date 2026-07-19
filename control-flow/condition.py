"""
演示条件语句
"""


def showConditions():
    height = float(input("身高(cm):"))
    weight = float(input("体重(kg):"))
    bmi = weight / (height / 100) ** 2
    print(f"{bmi = :.1f}")
    if bmi < 18.5:
        print("你的体重过轻！")
    elif bmi < 24:
        print("你的身材很棒！")
    elif bmi < 27:
        print("你的体重过重！")
    elif bmi < 30:
        print("你已轻度肥胖！")
    elif bmi < 35:
        print("你已中度肥胖！")
    else:
        print("你已重度肥胖！")

    status_code = int(input("响应状态码: "))
    match status_code:
        case 400:
            description = "Bad Request"
        case 401:
            description = "Unauthorized"
        case 403:
            description = "Forbidden"
        case 404:
            description = "Not Found"
        case 405:
            description = "Method Not Allowed"
        case 418:
            description = "I am a teapot"
        case 429:
            description = "Too many requests"
        case 500 | 501:
            description = "Server error"
        case _:
            description = "Unknown Status Code"
    print("状态码描述:", description)


if __name__ == "__main__":
    showConditions()
