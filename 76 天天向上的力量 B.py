a=eval(input())
up=pow(1+a/1000,364)
down=pow(1-a/1000,364)
print("{:.2f}, {:.2f}, {}".format(up,down,int(up/down)))