#用numpy创建随机值，测试，与数据项目无关
import numpy as np
from matplotlib import pyplot as plt

n,m,s=40,160,10
data=np.random.random(n)*s+m
#print(data)
c,x,_=plt.hist(data,10)
print(c)
print(x)
plt.show()
