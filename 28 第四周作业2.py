import random
import time
DARTS = eval(input())
hits = 0.0
start = time.perf_counter()
random.seed(123)
for i in range(1,DARTS + 1):
    x,y=random.random(),random.random()
    dists=pow(x**2+y**2,0.5)
    if(dists<=1.0):
        hits+=1
pi = 4*(hits/DARTS)
print("{:.6f}".format(pi))