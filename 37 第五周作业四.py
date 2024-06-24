def fbi(n):
    if n==1:
        return 1
    if n==2:
        return 1
    if n>2:
        return fbi(n-1) +fbi(n-2)
n = eval(input())
print(fbi(n))