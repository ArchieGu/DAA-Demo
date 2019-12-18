import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([712,653,625,605,617,635,677,762,800,872,947,1025,1111,1218,1309, 500])
y1 = np.array([2022,1876,1710,1544,1347,1309,1025,995,850,723,705,710,761,873,1050, 2000])

x_line = x1.copy()
y_line = x_line * 0.9 + 500

# y=y1-y_line
# nLen=len(x1)

# res = {
#     'x': [],
#     'y': [],
# }
# for i in range(nLen-1):
#     if np.dot(y[i], y[i+1]) == 0:#   %等于0的情况
#         if y[i]==0:
#             res['x'].append(i)
#             res['y'].append(0)
#         if y[i+1] == 0:
#             res['x'].append(i+1)
#             res['y'].append(0)
    
#     if np.dot(y[i],y[i+1]) < 0:# %一定有交点，用一次插值
#         yy = np.dot(abs(y[i]) * y_line[i+1] + abs(y[i+1])*y_line[i], 1/(abs(y[i+1])+abs(y[i])))
#         res['x'].append((yy-500)/0.9)
#         res['y'].append(yy)


def gen_cross_point(x1, y1, x2, y2):
    y=y1-y2
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
            yy = np.dot(abs(y[i]) * y2[i+1] + abs(y[i+1])*y2[i], 1/(abs(y[i+1])+abs(y[i])))
            res['x'].append((yy-500)/0.9)
            res['y'].append(yy)

    return res 


def gen_cross_point2(polygon, line):
    """
    polygen: dict, 曲线的，包含 x, y 轴
    line: dict, 起始点描述一条线
    """
    k = (line.y_end - line.y_start) / (line.x_end - line.x_start)
    x_line = np.arange(line.x_start, line.x_end, len(polygon['x']))
    b = line.y_start - line.x_start*k 
    y_line = x_line * k + b 
    return x_line, y_line, k, b 


print(gen_cross_point(x1, y1, ))
