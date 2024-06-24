sb=input()
if sb[0] in ['F','f']:
    C = (float(sb[1:]) - 32) / 1.8
    print("C{:.2f}".format(C))
elif sb[0] in ['C','c']:
    F=1.8*float(sb[1:]) + 32
    print("F{:.2f}".format(F))