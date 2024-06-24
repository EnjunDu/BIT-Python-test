f = open("latex.log").readlines()
s=set(f)
for i in s:
    f.remove(i)
x=set(f)
print("共{}独特行".format(len(s)-len(x)))