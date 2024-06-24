# 请在...补充一行或多行代码

def cmul(a,*b):
    sum=a
    for i in b:
        sum*=i
    return sum

print(eval("cmul({})".format(input())))