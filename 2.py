Tempstr = input()
if Tempstr [-1] in ['F','f']:
    C=(float(Tempstr[0:-1])-32)/1.8
    print("{:.2f}C".format(C))
elif Tempstr [-1] in ['C','c']:
    F = 1.8 * float(Tempstr[0:-1]) +32
    print("{:.2f}F".format(F))
else :
    print("输入格式错误")