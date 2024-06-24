f=open("latex.log","r",encoding="utf-8")
w=f.readlines()
s=0
sum=0
for line in w:
    line=line.strip('\n')
    if len(line)==0:
        continue
    s+=1
    sum+=len(line)
print("{}".format(sum/s))