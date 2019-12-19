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
import numpy as np
import matplotlib.pyplot as plt

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

    prov_inter_points = {}

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

if __name__ == '__main__':
    main()

