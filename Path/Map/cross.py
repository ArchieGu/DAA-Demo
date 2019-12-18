import numpy as np
import matplotlib.pyplot as plt
from provinces import *
from InSide import millerToXY

x1 = ShangHai_Lon
y1 = ShangHai_Lat
x1,y1 = millerToXY(x1,y1)

x_start = 33547259
x_end = 33121518
y_start = 7606963
y_end = 6789409

k = (y_end - y_start)/(x_end-x_start)
x_line =np.arange(x_start, x_end, -1000)
b = y_start-x_start*k
y_line = x_line * k +b

y=y1-y_line
nLen=len(x1)
xzero=np.zeros((nLen,))
yzero=np.zeros((nLen,))
for i in range(nLen-1):
    if np.dot(y[i], y[i+1]) == 0:#   %等于0的情况
        if y[i]==0:
            xzero[i]=i
            yzero[i]=0
        if y[i+1] == 0:
            xzero[i+1]=i+1
            yzero[i+1]=0
    elif np.dot(y[i],y[i+1]) < 0:# %一定有交点，用一次插值
        yzero[i] = np.dot(abs(y[i]) * y_line[i+1] + abs(y[i+1])*y_line[i], 1/(abs(y[i+1])+abs(y[i])))
        xzero[i] = (yzero[i]-b)/k
    else:
        pass            

for i in range(nLen):
    if xzero[i]==0 and (yzero[i]==0):#     %除掉不是交点的部分
        xzero[i]=np.nan
        yzero[i]=np.nan

print(xzero)
print(yzero)

plt.plot(x1, y1, 'o-')
plt.plot(x_line,y_line,xzero,yzero,'o')
plt.show()
