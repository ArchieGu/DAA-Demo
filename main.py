from Path.Map.utils import (
    load_province, 
    is_in_province,
    load_specific_province,
    millerToXY,
    get_random_point_in_polygon,
    gen_cross_point,
    gen_line
)
from shapely.geometry import Polygon, Point
import numpy as np
import matplotlib.pyplot as plt

def main():

    data1 = load_specific_province('北京')
    data2 = load_specific_province('上海')
    p = Polygon(data1)
    point_in_poly = str(get_random_point_in_polygon(p))[7:-1]
    point_start = [float(point_in_poly.split(' ')[0]),float(point_in_poly.split(' ')[1])]
    point_start = np.dstack(millerToXY(point_start[0],point_start[1]))
    print(point_start[0][0][0])
    
    
    '''
    prov_inter_points = {}
    point_start = (32770658,6998678)
    point_end = (33121518, 6789409)

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
    print(prov_inter_points)
'''
if __name__ == '__main__':
    main()

