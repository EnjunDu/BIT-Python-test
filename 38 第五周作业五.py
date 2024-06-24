def hanoi(n, source, auxiliary, target):#初始化"源"、"辅助"和 "目标"
    if n == 1:
        print("[STEP {:>3}] {}->{}".format(hanoi.step, source, target))
        hanoi.step += 1
    else:
        hanoi(n-1, source, target, auxiliary)
        print("[STEP {:>3}] {}->{}".format(hanoi.step, source, target))
        hanoi.step += 1
        hanoi(n-1, auxiliary, source, target)
hanoi.step = 1  # 初始化步骤计数
n = int(input())  # 输入汉诺塔的盘数
hanoi(n, 'A', 'B', 'C')  # 调用汉诺塔函数
