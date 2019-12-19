import os 
import numpy as np
from matplotlib import path
import math
from shapely.geometry import LineString
from shapely.geometry import Polygon, Point
import random
import requests 

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

def load_specific_province(ProvinceName):
    """加载省的边界数据点"""
    provinces_point = dict()
    for f_name in os.listdir('china'):
        if f_name == ProvinceName+'.txt':
            f_path = os.path.join('china', f_name)
            province = f_name.split('.')[0]
            data = np.loadtxt(f_path) 
            data = np.reshape(data,(-1,2))

    return data

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

def get_random_point_in_polygon(poly):
    minx, miny, maxx, maxy = poly.bounds
    while True:
        p = Point(random.uniform(minx, maxx), random.uniform(miny, maxy))
        if poly.contains(p):
            return p 

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

def calculate_path(data):
    """
    根据data计算路径，可以供本地调用，server 也主要调用它计算
    """
    return []

    
def get_path(data, host, port):
    """
    根据发送的数据获取路径数据
    """
    try:
        return http_post(data, host, port)
    except:
        raise Exception("Error: get path failed, host: {}, port: {}".format(host, port))
    

def http_post(data, host, port):
    path = 'cal_path'
    url = 'http://{}:{}/{}'.format(host, port, path)
    r = requests.post(url, json=data)
    return r.json() 
