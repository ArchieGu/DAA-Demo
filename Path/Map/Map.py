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

Test = pd.read_csv('/Users/tianyuli/Documents/BUAA Code/Map/position.csv', names = ['Airport','POS1','POS2','POS3','POS4','POS5','POS6','POS7','POS8','POS9','POS10','POS11','POS12'])
with open('/Users/tianyuli/Desktop/Path/Map/china.json','r') as load_f:
    Boarder = json.load(load_f)
load_f.close()



def millerToXY_Boarder (coordinate):
    L = 6381372*math.pi*2
    W = L
    H = L/2
    mill = 2.3
    x = coordinate[0]*math.pi/180
    y = coordinate[1]*math.pi/180
    y = 1.25*math.log(math.tan(0.25*math.pi+0.4*y))
    x = (W/2)+(W/(2*math.pi))*x
    y = (H/2)-(H/(2*mill))*y
    boarder_coordinate.append([int(round(x)),int(round(y))])
    return boarder_coordinate

for i in range(len(Boarder)):
    millerToXY_Boarder(Boarder[i])

for i in range(1,13):
    Test['POS'+str(i)+'Lon'],Test['POS'+str(i)+'Lat'] = Test['POS'+str(i)].apply(lambda x:x.split(',')[1]),Test['POS'+str(i)].apply(lambda x:x.split(',')[0])
    Test['POS13Lon'],Test['POS13Lat'] = Test['POS1Lon'],Test['POS1Lat']
    Test = Test.drop(['POS'+str(i)],axis=1)
    
    
    
def Dms2D(dms_data):
    integral = int(dms_data.split("°")[0])
    decimal = float(dms_data.split("°")[1][:-1])
    D_data = integral+decimal/60
    return D_data



def millerToXY (lon, lat):
    L = 6381372*math.pi*2
    W = L
    H = L/2
    mill = 2.3
    x = lon*math.pi/180
    y = lat*math.pi/180
    y = 1.25*math.log(math.tan(0.25*math.pi+0.4*y))
    x = (W/2)+(W/(2*math.pi))*x
    y = (H/2)-(H/(2*mill))*y
    xy_coordinate.append([int(round(x)),int(round(y))])
    return xy_coordinate

def millerToLonLat(x,y):
    L = 6381372 * math.pi*2
    W = L
    H = L/2
    mill = 2.3
    lat = ((H/2-y)*2*mill)/(1.25*H)
    lat = ((math.atan(math.exp(lat))-0.25*math.pi)*180)/(0.4*math.pi)
    lon = (x-W/2)*360/W
    lonlat_coordinate.append([round(lon,7),round(lat,7)])
    return lonlat_coordinate     

for i in range(1,14):
    for j in range(0,len(Test['POS1Lon'])):
        Test['POS'+str(i)+'Lon'][j],Test['POS'+str(i)+'Lat'][j] = round(Dms2D(Test['POS'+str(i)+'Lon'][j]),5),round(Dms2D(Test['POS'+str(i)+'Lat'][j]),5)

for i in range(0,len(Test['POS1Lon'])):
    for j in range(1,14):
        millerToXY(Test['POS'+str(j)+'Lon'][i],Test['POS'+str(j)+'Lat'][i])

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
'''
for i in range(len(boarder_coordinate)):
    ox_all.append(boarder_coordinate[i][0])
    oy_all.append(boarder_coordinate[i][1])


plt.plot(ox_all,oy_all,".k")
plt.show()
'''    
