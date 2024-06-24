# CalStatisticsV1.py
def getNum():  # 获取用户不定长度的输入
    input_str = input("")
    input_list = input_str.split(',')
    numbers = [eval(x) for x in input_list]
    return numbers

def mean(numbers):  # 计算平均值
    total = sum(numbers)
    return total / len(numbers)

def dev(numbers, mean):  # 计算标准差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean) ** 2
    return pow(sdev / (len(numbers) - 1), 0.5)

def median(numbers):  # 计算中位数
    numbers.sort()
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1] + numbers[size//2]) / 2
    else:
        med = numbers[size//2]
    return med

n = getNum()  # 主体函数
m = mean(n)
s = dev(n, m)
c = median(n)
print("平均值:{:.2f},标准差:{:.2f},中位数:{}".format(m, s, c))