template = '零一二三四五六七八九'
s = input()
for i in s:
    print(template[eval(i)],end="")