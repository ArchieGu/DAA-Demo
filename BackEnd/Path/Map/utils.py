import os 
import numpy as np
from matplotlib import path
import math
from shapely.geometry import LineString
from shapely.geometry import Polygon, Point
import random
import requests 

from config import cal_nodes

def load_province():
    """加载省的边界数据点"""
    provinces_point = dict()
    for f_name in os.listdir('BackEnd/china'):
        if not f_name.endswith('.txt'):
            continue
        f_path = os.path.join('BackEnd/china', f_name)
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
    for f_name in os.listdir('BackEnd/china'):
        if f_name == ProvinceName+'.txt':
            f_path = os.path.join('BackEnd/china', f_name)
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

def millerToCoor(x,y):
    """平面点转换为经纬度"""
    L = 6381372 * math.pi*2
    W = L
    H = L/2
    mill = 2.3
    lat = ((H/2-y)*2*mill)/(1.25*H)
    lat = ((np.arctan(np.exp(lat))-0.25*math.pi)*180)/(0.4*math.pi)
    lon = (x-W/2)*360/W
    lat = np.around(lat,decimals=4)
    lon = np.around(lon,decimals=4)
    return lon,lat


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
    for f_name in os.listdir('BackEnd/china'):
        if not f_name.endswith('.txt'):
            continue
        province = f_name.split('.')[0]
        provinces.append(province)

    return random.choice(provinces)

def gen_start_end_point():
    prov = gen_random_province()
    assert prov!= ""
    polygon = load_specific_province(prov)
    p = Polygon(polygon)
    point_in_poly = str(get_random_point_in_polygon(p))[7:-1]
    point = [float(point_in_poly.split(' ')[0]),float(point_in_poly.split(' ')[1])]
    point = millerToXY(point[0],point[1])
    return prov, point

def calculate_path(data):
    """
    根据data计算路径，可以供本地调用，server 也主要调用它计算.
    data: {'province': '四川', 'start': (104, 30), 'end': (108, 33)}
    """
    # TODO：循环依赖，后面再修改
    from BackEnd.Path.HybridAStar.hybrid_a_star import  hybrid_path_planning
    start = data.get('start')
    end = data.get('end')
    province = data.get('province')
    return hybrid_path_planning(start, end, province)


def get_path(data):
    """
    根据发送的数据获取路径数据
    data: {'province': '四川', 'start': (104, 30), 'end': (108, 33)}
    """
    try:
        prov = data.get('province')
        node = cal_nodes.get(prov)
        if not node:
            node = cal_nodes.get('default')
        host = node.get('host')
        port = node.get('port')
        
        return http_post(data, host, port)
    except:
        raise Exception("Error: get path failed, host: {}, port: {}".format(host, port))
    

def http_post(data, host, port):
    path = 'cal_path'
    url = 'http://{}:{}/{}'.format(host, port, path)
    r = requests.post(url, json=data)
    return r.json() 

class aircraft:
    def __init__(self, ICAO, mode, lon, lat,
                 alt, heading, speed):
        self.ICAO = ICAO
        self.mode = mode
        self.lon = lon
        self.lat = lat
        self.alt = alt
        self.heading = heading
        self.speed = speed

def uav_model_init():
    print("\nGive the initial conditions for your aircraft:\n")
    while(True):
        print('Would you like to use the default values?\n')
        Ownship = aircraft('QFA50','A',117.84167359617524,38.94488085591196,22000,-118.04390959391104,2000)
        print('Ownship ICAO:',Ownship.ICAO)
        print('Ownship Mode:',Ownship.mode)
        print('Ownship lon:',Ownship.lon)
        print('Ownship lat:',Ownship.lat)
        print('Ownship alt:',Ownship.alt)
        print('Ownship heading:',Ownship.heading)
        print('Ownship speed:',Ownship.speed)
        valid = input('Please enter (Y/N)')
        if valid == 'Y' or valid == 'y':
            return Ownship
            break
        elif valid == 'N' or valid =='n':
            pass
        else:
            print("Invalid input, please choose again.")
    
        
