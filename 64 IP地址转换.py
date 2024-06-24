import sys
a=input()
if len(a)!=32:
    print("data error!")
    sys.exit()
for i in  a:
    if i !='0' and i!='1':
        print("data error!")
        sys.exit()
for i in range (3):
    b=int(a[i*8:8*i+8],2)
    print("{}.".format(b),end="")
print("{}".format(int(a[24:32],2)))