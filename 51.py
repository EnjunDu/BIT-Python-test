import sys
s = input()
counts={}
for i in s:
    counts[i] = counts.get(i,0)+1
for i in s:
    if counts[i] ==1:
        print("{}".format(s.index(i)))
        sys.exit()
    else:
        print("-1")