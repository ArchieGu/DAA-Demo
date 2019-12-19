import os 
import math
import random 
from shapely.geometry import LineString
import numpy as np
from matplotlib import path



def load_province():
    """加载省的边界数据点"""
    provinces_point = dict()
    for f_name in os.listdir('china'):
        if not f_name.endswith('.txt'):
            continue
        f_path = os.path.join('china', f_name)
        province = f_name.split('.')[0]
        data = np.loadtxt(f_path) 
        data = np.reshape(data,(-1,2))

        lon = data[:,:1]
        lat = data[:,1:2]
        pos = {
            'lon': lon.flatten(),
            'lat': lat.flatten()
        }
        provinces_point[province] = pos 

    return provinces_point

def load_specific_province():
    """加载省的边界数据点"""
    provinces_point = dict()
    for f_name in os.listdir('china'):
        if not f_name.endswith('.txt'):
            continue
        f_path = os.path.join('china', f_name)
        province = f_name.split('.')[0]
        data = np.loadtxt(f_path) 
        data = np.reshape(data,(-1,2))

        lon = data[:,:1]
        lat = data[:,1:2]

    return lon, lat

def millerToXY (lon, lat):
    """经纬度转换为平面点"""
    L = 6381372*math.pi*2
    W = L
    H = L/2
    mill = 2.3
    x = lon*math.pi/180
    y = lat*math.pi/180
    y = 1.25*np.log(np.tan(0.25*math.pi+0.4*y))
    x = (W/2)+(W/(2*math.pi))*x
    y = (H/2)-(H/(2*mill))*y
    return x,y


def is_in_province(provinces_point, province, point):
    """某个平面点是否在某个省内"""
    points = provinces_point.get(province)
    lat = points.get('lat')
    lon = points.get('lon')
    lon, lat = millerToXY(lon,lat)
    points = np.dstack((lon, lat))[0]
    boarder = path.Path(points)
    return boarder.contains_points([point])

def gen_line(start, end):
    x_start, y_start = start  
    x_end, y_end = end 
    k = (y_end - y_start) / (x_end - x_start)
    # 暂时设为 1000个点，后面根据长度调整
    if x_start > x_end:
        x = np.arange(x_start, x_end, -1000)
    else:
        x = np.arange(x_start, x_end, 1000)

    b = y_start - x_start*k 
    y = x * k + b 
    return x, y 

def gen_cross_point(line, polygen):
    """
    line: list: [(x, y)]
    polygen: list: [(x, y)]
    """
    line = LineString(line)
    polygen = LineString(polygen)
    return line.intersection(polygen) 


def gen_random_province():
    """
    返回随机的中文省份名，比如四川。
    省份集合根据 china 包获得。
    """
    provinces = list()
    for f_name in os.listdir('china'):
        if not f_name.endswith('.txt'):
            continue
        province = f_name.split('.')[0]
        provinces.append(province)

    return random.choice(provinces)
