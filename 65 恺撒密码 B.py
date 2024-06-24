a = input()
for w in range(0,26):
    x=w
    for i in a:
        if 'a'<=i<='z':
            i = chr(ord('a')+(ord(i)-ord('a')+x)%26)
            print(i,end="")
            continue
        if 'A'<=i<='Z':
            i = chr(ord('A')+(ord(i)-ord('A')+x)%26)
            print(i,end="")
        else:
            print(i,end="")
    print(" ")
