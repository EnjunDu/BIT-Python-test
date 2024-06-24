op=input()
if op[0] in ['R','r']:
    U=float(op[3:])/6.78
    print("USD{:.2f}".format(U))
elif op[0] in ['U','u']:
    R=float(op[3:])*6.78
    print("RMB{:.2f}".format(R))