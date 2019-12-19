# -*- coding: utf-8 -*-
from scipy.spatial import ConvexHull, convex_hull_plot_2d
import math
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import json

xy_coordinate = [] # XY cordinate after conversion
boarder_coordinate = []
lonlat_coordinate = []

Test = pd.read_csv('pos_mod.csv', index_col = 0)
print(Test.head(2))
print(Test.loc['上海/虹桥'])

'''
prov_airp = {'上海':'上海/虹桥','上海/浦东';'北京':'北京/首都';}    

ox_all, oy_all = [], []
for lenth in range(0,int(len(xy_coordinate)/13)):
    temp = np.array(xy_coordinate[lenth*13:lenth*13+13])
    points_x, points_y = [], []

    hull = ConvexHull(temp)
    for simplex in hull.simplices:
        plt.plot(temp[simplex, 0], temp[simplex, 1], 'k')
        #plt.plot(temp[hull.vertices,0], temp[hull.vertices,1], '.k')
        #    
    points_x = np.array(temp[hull.vertices,0])
    points_y = np.array(temp[hull.vertices,1])
    
    for i in range(len(points_x)-1):
        ox_all.append(points_x[i])
        oy_all.append(points_y[i])
        countx = points_x[i+1] - points_x[i]
        county = points_y[i+1] - points_y[i]
        if county == 0:
            for j in range(0,countx,1000):
                ox_all.append(points_x[i]+j)
                oy_all.append(points_y[i])
        elif countx == 0:
            for j in range(0,county,1000):
                ox_all.append(points_x[i])
                oy_all.append(points_y[i]+j)
        elif countx > 0:
            k = county/countx
            for j in range(0,abs(int(county/k)),1000):
                ox_all.append(points_x[i]+j)
                oy_all.append(points_y[i]+j*k)
        else:
            k = county/countx
            for j in range(0,abs(int(county/k)),1000):
                ox_all.append(points_x[i]-j)
                oy_all.append(points_y[i]-j*k)
    countx = points_x[len(points_x)-1] - points_x[0]
    county = points_y[len(points_x)-1] - points_y[0]
    if county == 0:
        if countx < 0 :
            for j in range(0,countx,1000):
                ox_all.append(points_x[len(points_x)-1]+j)
                oy_all.append(points_y[len(points_x)-1])
        else: 
            for j in range(0,countx,1000):
                ox_all.append(points_x[0]+j)
                oy_all.append(points_y[0])
    elif countx == 0:
        if county < 0 :
            for j in range(0,county,1000):
                ox_all.append(points_x[len(points_x)-1])
                oy_all.append(points_y[len(points_x)-1]+j)
        else:
            for j in range(0,county,1000):
                ox_all.append(points_x[0])
                oy_all.append(points_y[0]+j)
    else:
        k = county/countx
        if k > 0:
            if countx < 0 :
                for j in range(0,abs(int(county/k)),1000):
                    ox_all.append(points_x[len(points_x)-1]+j)
                    oy_all.append(points_y[len(points_x)-1]+j*k)
            else:
                for j in range(0,abs(int(county/k)),1000):
                    ox_all.append(points_x[0]+j)
                    oy_all.append(points_y[0]+j*k)
        else:
            if countx < 0 :
                for j in range(0,abs(int(county/k)),1000):
                    ox_all.append(points_x[len(points_x)-1]+j)
                    oy_all.append(points_y[len(points_x)-1]+j*k)
            else:
                for j in range(0,abs(int(county/k)),1000):
                    ox_all.append(points_x[0]+j)
                    oy_all.append(points_y[0]+j*k)

for i in range(len(boarder_coordinate)):
    ox_all.append(boarder_coordinate[i][0])
    oy_all.append(boarder_coordinate[i][1])


plt.plot(ox_all,oy_all,".k")
plt.show()
'''    
