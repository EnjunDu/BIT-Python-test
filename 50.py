str = input()
count = 0
for i in str:
    if i == 'a':
        count+=1
    else:
        continue
print("{}".format(count))