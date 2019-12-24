from Path.Map.utils import (
    load_province, 
    is_in_province,
    load_specific_province,
    millerToXY,
    get_random_point_in_polygon,
    gen_cross_point,
    gen_line,
    gen_random_province
)
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
except:
    raise



def gen_start_end_point():
    prov = gen_random_province()
    assert prov!= ""
    polygon = load_specific_province(prov)
    p = Polygon(polygon)
    point_in_poly = str(get_random_point_in_polygon(p))[7:-1]
    point = [float(point_in_poly.split(' ')[0]),float(point_in_poly.split(' ')[1])]
    point = millerToXY(point[0],point[1])
    return prov, point

def main():
    prov_start, point_start = gen_start_end_point()
    print(prov_start,point_start)

    prov_end, point_end = gen_start_end_point()
    print(prov_end, point_end)

    porv_inter = []

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
        porv_inter.append(prov)
        points = np.dstack((lon, lat))[0]
        cross_point_list = gen_cross_point(line, points)
        interaction_points = cross_point_list.bounds
        if interaction_points:
            prov_inter_points[prov] = interaction_points
            print(interaction_points)
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
        hybrid_path_planning(inter_start,inter_end,key)
        break


if __name__ == '__main__':
    main()

