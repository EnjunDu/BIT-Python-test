s = input()
d = eval(s)
e = {}
try:
    for k in d:
        e[d[k]] =k
    print(e)
except:
    print("输入错误")