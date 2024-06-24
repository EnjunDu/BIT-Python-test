fo = open("info.csv","r",encoding='GBK').readlines()
dic={}
for line in fo:
    str=line.strip().split(",")
    dic[str[0]]=str[1:]
a=input()
if a=='A':
    for name,value in dic.items():
        print(name,value[0],value[1])
elif a=='D':
    print(dic)
else:
    print("ERROR")