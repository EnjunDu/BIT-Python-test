sum = 0
for i in range(1,967):
    if i%2!=0:
        sum+=i
    else:
        sum-=i
print("{}".format(sum))