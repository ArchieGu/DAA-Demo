from Path.Map.utils import (
    load_province, 
    is_in_province,
    load_specific_province,
    millerToXY,
)
import numpy as np
import matplotlib.pyplot as plt

from Path.Map.utils import gen_cross_point, gen_line

provices_point = load_province()
'''
point = (32770658,6998678)
for prov, points in provices_point.items():
    if is_in_province(provices_point, prov, point):
        print('point in province: {}'.format(prov))
'''
# for prov,points in provices_point.items():
#     plt.plot(points['lon'],points['lat'],'o-')
# plt.show()

start = (33547259,7606963)
end = (33121518, 6789409)
x, y = gen_line(start, end)
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
        print(interaction_points)
