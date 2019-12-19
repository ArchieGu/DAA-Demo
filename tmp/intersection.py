from shapely.geometry import LineString
import matplotlib.pyplot as plt 
import numpy as np 
from Path.Map.utils import *
'''
x = [0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0]
y = [0, 2, 4, 5, 4, 2, 1.8, 1.6, 1.5, 0, 0, 0, 0]

x1 = [0.5, 1, 2]
y1 = [-1, 1.5, 6]
plt.plot(x ,y)
plt.plot(x1, y1)
plt.show()

l1 = np.dstack((x, y))[0]
l2 = np.dstack((x1, y1))[0]
print(l1)
print(l2)

l11 = LineString(l1)
l22 = LineString(l2)
print(l11.intersection(l22))
'''

Beijing_lon, Beijing_lat = load_specific_province('北京')
Beijing_lon, Beijing_lat = millerToXY(Beijing_lon, Beijing_lat)

l1_test = np.dstack((Beijing_lon, Beijing_lat))[0]

x_start = 33547259
x_end = 33121518
y_start = 7606963
y_end = 6789409
k = (y_end - y_start)/(x_end-x_start)
b = y_start-x_start*k

x_line =np.linspace(x_start, x_end, len(Beijing_lon))
y_line = x_line * k +b
l2_test = np.dstack((x_line,y_line))[0]
plt.plot(Beijing_lon, Beijing_lat)
plt.plot(x_line, y_line)
plt.show()

l11_test = LineString(l1_test)
l22_test = LineString(l2_test)
