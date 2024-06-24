import random
import time
DARTS = 1000*1000
hits = 0.0
start =time.perf_counter()
for i in range(1,DARTS+1):
    x, y =random.random(),random.random()
    dist = pow(x**2 + y**2,0.5)
    if (dist<=1.0):
       hits+=1
π = 4 * (hits/DARTS)
print("π={}".format(π))
print("运行时间为：{:.5f}s".format(time.perf_counter()-start))