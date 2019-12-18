from Path.Map.utils import load_province, is_in_province

provices_point = load_province()
point = (32770658,6998678)
for prov, points in provices_point.items():
    if is_in_province(provices_point, prov, point):
        print('point in province: {}'.format(prov))

