a = input()
b = float(a)
if a[0]=='R':
    c=b/6.78
    print("USD{:.2f}".format(c))
if a[0]=='U':
    c=b*6.78
    print("RMB{:.2f}".format(c))