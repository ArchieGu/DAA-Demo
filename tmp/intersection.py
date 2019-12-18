from shapely.geometry import LineString
import matplotlib.pyplot as plt 
import numpy as np 

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
# line1 = LineString([(0,0), (1,2), (2,4), (3, 5), (4, 3), (5, 2), (6, 1), (7, 0), (8, 0), (9, 0), (10, 0)])
# line2 = LineString([(1,1.5), (2,3)])

# print(line1.intersection(line2))