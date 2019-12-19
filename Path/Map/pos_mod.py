import math
import pandas as pd
import numpy as np
import csv

Test = pd.read_csv('/Users/tianyuli/Documents/BUAA Code/Map/position.csv', names = ['Airport','POS1','POS2','POS3','POS4','POS5','POS6','POS7','POS8','POS9','POS10','POS11','POS12'])

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
    y = 1.25*np.log(np.tan(np.array(0.25*math.pi+0.4*y, dtype=float)))
    x = (W/2)+(W/(2*math.pi))*x
    y = (H/2)-(H/(2*mill))*y
    return x,y

for i in range(1,13):
    Test['POS'+str(i)+'Lon'],Test['POS'+str(i)+'Lat'] = Test['POS'+str(i)].apply(lambda x:x.split(',')[1]),Test['POS'+str(i)].apply(lambda x:x.split(',')[0])
    Test['POS13Lon'],Test['POS13Lat'] = Test['POS1Lon'],Test['POS1Lat']
    Test = Test.drop(['POS'+str(i)],axis=1)


for i in range(1,14):
    for j in range(0,len(Test['POS1Lon'])):
        Test['POS'+str(i)+'Lon'][j],Test['POS'+str(i)+'Lat'][j] = round(Dms2D(Test['POS'+str(i)+'Lon'][j]),5),round(Dms2D(Test['POS'+str(i)+'Lat'][j]),5)

for i in range(1,14):
    Lon = np.asarray(Test['POS'+str(i)+'Lon'])
    Lat = np.asarray(Test['POS'+str(i)+'Lat'])
    x, y = millerToXY(Lon,Lat)
    Test['POS'+str(i)+'Lon'] = pd.DataFrame(x)
    Test['POS'+str(i)+'Lat'] = pd.DataFrame(y)
print(Test.head(2))
Test.to_csv('pos_mod.csv',mode='w',index=False)
