import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([712,653,625,605,617,635,677,762,800,872,947,1025,1111,1218,1309, 500])
y1 = np.array([2022,1876,1710,1544,1347,1309,1025,995,850,723,705,710,761,873,1050, 2000])

x_start = np.min(x1)
x_end = np.max(x1)+1

x_line = x1.copy()
y_line = x_line * 0.9 + 500

y=y1-y_line
nLen=len(x1)

res = {
    'x': [],
    'y': [],
}
for i in range(nLen-1):
    if np.dot(y[i], y[i+1]) == 0:#   %等于0的情况
        if y[i]==0:
            res['x'].append(i)
            res['y'].append(0)
        if y[i+1] == 0:
            res['x'].append(i+1)
            res['y'].append(0)
    
    if np.dot(y[i],y[i+1]) < 0:# %一定有交点，用一次插值
        res['x'].append(x_line[i])
        res['y'].append(y_line[i])
        res['x'].append(x_line[i+1])
        res['y'].append(y_line[i+1])
        # yy = np.dot(abs(y[i]) * y_line[i+1] + abs(y[i+1])*y_line[i], 1/(abs(y[i+1])+abs(y[i])))
        # res['x'].append((yy-500)/0.9)
        # res['y'].append(yy)

print(res['x'])
print(res['y'])

plt.plot(x1, y1, 'o-')
plt.plot(x_line,y_line,res['x'],res['y'],'o')
plt.show()