import numpy as np
import matplotlib.pyplot as plt
from utils import *

res = {
    'x': [],
    'y': [],
}

x_start = 33547259
x_end = 33121518
y_start = 7606963
y_end = 6789409

k = (y_end - y_start)/(x_end-x_start)

b = y_start-x_start*k

provices_point = load_province()
for prov,points in provices_point.items():
    x1 = points['lon']
    y1 = points['lat']

    x1,y1 = millerToXY(x1,y1)
    x_line =np.linspace(x_start, x_end, len(x1))
    y_line = x_line * k +b
    y=y1-y_line
    nLen=len(x1)
    xzero=np.zeros((nLen,))
    yzero=np.zeros((nLen,))
    for i in range(nLen-1):
        if np.dot(y[i], y[i+1]) == 0:#   %等于0的情况
            if y[i]==0:
                res['x'].append(i)
                res['y'].append(0)
            if y[i+1] == 0:
                res['x'].append(i+1)
                res['y'].append(0)
        if np.dot(y[i],y[i+1]) < 0:# %一定有交点，用一次插值
            yy = np.dot(abs(y[i]) * y_line[i+1] + abs(y[i+1])*y_line[i], 1/(abs(y[i+1])+abs(y[i])))
            res['x'].append((yy-b)/k)
            res['y'].append(yy)
        plt.plot(x1, y1, 'o-')
        plt.plot(x_line,y_line,xzero,yzero,'o') 
        
                  
'''
for i in range(nLen):
    if xzero[i]==0 and (yzero[i]==0):#     %除掉不是交点的部分
        xzero[i]=np.nan
        yzero[i]=np.nan
'''
print(res['x'])
print(res['y'])

plt.show()
