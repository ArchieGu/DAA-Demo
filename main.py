from Path.Map.utils import (
    load_province, 
    is_in_province,
    load_specific_province,
    millerToXY,
    millerToCoor,
    get_random_point_in_polygon,
    gen_cross_point,
    gen_line,
    gen_random_province,
    gen_start_end_point,
    get_path,
    uav_model_init
)

import numpy as np
from shapely.geometry import Polygon, Point
import matplotlib.pyplot as plt
import math
import random

try:

    from Path.HybridAStar.hybrid_a_star import *
    from Path.HybridAStar.a_star import dp_planning  # , calc_obstacle_map
    import Path.ReedsSheppPath.reeds_shepp_path_planning as rs
    from Path.HybridAStar.uav import move, check_uav_collision, MAX_STEER, WB, plot_uav
    from Path.Map.Map import *
    from DAAUI.daa_test import Display
except:
    raise

def main():
    '''
    prov_start, point_start = gen_start_end_point()
    print(prov_start,point_start)

    prov_end, point_end = gen_start_end_point()
    print(prov_end, point_end)
    '''

    point_start = (33172400.000, 6903700.00)
    point_end = (33111518.000000,6789409.0)

    prov_start = '天津'
    prov_end = '北京'
    provices_point = load_province()

    for prov, points in provices_point.items():
        if is_in_province(provices_point, prov, point_start):
            print('Start point is in province: {}'.format(prov))
            start_prov = prov
        if is_in_province(provices_point,prov,point_end):
            print('End point is in province: {}'.format(prov))
            end_prov = prov
    
    x, y = gen_line(point_start, point_end)
    line = np.dstack((x, y))[0]

    prov_inter_points = {}

    for prov, points in provices_point.items():
        lat = points.get('lat')
        lon = points.get('lon')
        lon, lat = millerToXY(lon, lat)
        print('-----------------')
        print(prov)
        points = np.dstack((lon, lat))[0]

        cross_point_list = gen_cross_point(line, points)
        interaction_points = cross_point_list.bounds
        if interaction_points:
            prov_inter_points[prov] = interaction_points
            print(interaction_points)

    path_combine_x,path_combine_y = [],[]

    for key in prov_inter_points:
        if key == prov_start:
            inter_start = point_start[0],point_start[1]
            inter_end = prov_inter_points[key][0],prov_inter_points[key][1]
        elif key == prov_end:
            inter_start = prov_inter_points[key][0],prov_inter_points[key][1]
            inter_end = point_end[0],point_end[1]
        else:
            inter_start = prov_inter_points[key][0],prov_inter_points[key][1]
            inter_end = prov_inter_points[key][2],prov_inter_points[key][3]
        print("-----------One Province Test-----------")
        print("Province:",key)
        data = {
            'start': inter_start,
            'end': inter_end,
            'province': key
        }
        path = get_path(data)
        path_x = np.array(path.get('data').get('x'))
        path_y = np.array(path.get('data').get('y'))
        path_lon,path_lat = millerToCoor(path_x,path_y)
               
if __name__ == '__main__':
    print('--------DAA Demo---------')
    #Ownship = uav_model_init()
    #main()
    Display()

