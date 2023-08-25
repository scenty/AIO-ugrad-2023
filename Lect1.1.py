import torch
import numpy as np

x = np.random.random(size=[100,100,20])
y = np.random.random(size=[100,100,20])
x.shape
y.shape
print(
    '\nnumpy array:', x,      
    '\nnumpy array:', y,      
)

#切片操作
x[0,1]
x[:,1]
x[::1,0]
x[1::,1]
x[1]
#mean
np.mean(x)
x.mean()
np.average(x)
#weighted mean
weight=np.array([.2,.3,.2])
np.average(x,axis=0,weights=weight)
#moving mean

#geo-mean
np.cumprod(x)
np.cumprod(x)[-1]
pow(np.cumprod(x)[-1],1/6)
#range
x.max()-x.min()
#variable coef
np.std(x)/x.mean()
#median
np.median(x)
#转换成32位浮点
x=x.float()

#与Matlab交互读写
Dataset1 = loadmat('SST1993-2018.mat')
sst = Dataset1['var'][:]#OISST海表温度
xx = Dataset1['xx'][:]            #lon
yy = Dataset1['yy'][:]            #lat
time = np.linspace(1993+1/12,2019,num=312)

#
