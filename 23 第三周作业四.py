op = input()
yp = int(op)
n = (yp+1)//2
if n ==0:
    n=1
for i in range (n):
    print(' '*(n-1-i),end="")
    print('*'*((i+1)*2-1))
