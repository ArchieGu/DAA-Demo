from Path.Map.utils import load_province, is_in_province,load_specific_province
import numpy as np
import matplotlib.pyplot as plt

provices_point = load_province()
'''
point = (32770658,6998678)
for prov, points in provices_point.items():
    if is_in_province(provices_point, prov, point):
        print('point in province: {}'.format(prov))
'''
for prov,points in provices_point.items():
    plt.plot(points['lon'],points['lat'],'o-')
plt.show()
