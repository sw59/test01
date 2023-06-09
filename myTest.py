def fibonacci(n):
    if n <= 0:
        return "输入错误，请输入一个正整数"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n):
            a, b = b, a + b
        return b


assert fibonacci(1) == 0, "Error: fibonacci(1) should return 0"
assert fibonacci(2) == 1, "Error: fibonacci(2) should return 1"
assert fibonacci(3) == 1, "Error: fibonacci(3) should return 1"
assert fibonacci(4) == 2, "Error: fibonacci(4) should return 2"
assert fibonacci(5) == 3, "Error: fibonacci(5) should return 3"
assert fibonacci(6) == 4, "Error: fibonacci(6) should return 5"

print("学习时一种")
print("尊重时一种")
print("按时交")
print(3+3)
print(5%2)
print(3*3)
print(6/3)
print("这是第一次提交")
print("这是第二次提交")
print("这是第三次提交")
print("creating a new branch is quick and simple")
print("这个bug需要明天修复")
print("又一次创建dev分支")
print("这一次要学会在终端push/pull")