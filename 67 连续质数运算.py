import sys
n = eval(input())
if n%1!=0:
    n = int(n)+1  # 取整数部分
s = 0  # 初始化质数计数器为0
i = n  # 从n开始判断质数
result = []
while s < 5:
    if i < 2:
        i += 1
        continue

    is_prime = True  # 假设i是质数
    for a in range(2, int(i ** 0.5) + 1):
        if i % a == 0:
            is_prime = False
            break
    if is_prime:
        result.append(str(i))
        s += 1
    i += 1
print(",".join(result))
