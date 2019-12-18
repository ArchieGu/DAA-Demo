from matplotlib import path
import math
import numpy as np
from provinces import *

Provinces = ['ShangHai','YunNan','NeiMengGu','Beijing','JiLin','SiChuan','TianJin','NingXia','AnHui','ShanDong',
'ShanXi','GuangDong','GuangXi','XinJiang','JiangSu','JiangXi','HeBei','HeNan','ZheJiang','HaiNan','HuBei','HuNan',
'GanSu','FuJian','XiZang','GuiZhou','LiaoNing','ChongQing','ShanXi2','QingHai','HeiLongJiang']


Lon = [ShangHai_Lon,YunNan_Lon,NeiMengGu_Lon,Beijing_Lon,JiLin_Lon,SiChuan_Lon,TianJin_Lon,NingXia_Lon,AnHui_Lon,ShanDong_Lon,
ShanXi_Lon,GuangDong_Lon,GuangXi_Lon,XinJiang_Lon,JiangSu_Lon,JiangXi_Lon,HeBei_Lon,HeNan_Lon,ZheJiang_Lon,HaiNan_Lon,HuBei_Lon,HuNan_Lon,
GanSu_Lon,FuJian_Lon,XiZang_Lon,GuiZhou_Lon,LiaoNing_Lon,ChongQing_Lon,ShanXi2_Lon,QingHai_Lon,HeiLongJiang_Lon]

Lat = [ShangHai_Lat,YunNan_Lat,NeiMengGu_Lat,Beijing_Lat,JiLin_Lat,SiChuan_Lat,TianJin_Lat,NingXia_Lat,AnHui_Lat,ShanDong_Lat,
ShanXi_Lat,GuangDong_Lat,GuangXi_Lat,XinJiang_Lat,JiangSu_Lat,JiangXi_Lat,HeBei_Lat,HeNan_Lat,ZheJiang_Lat,HaiNan_Lat,HuBei_Lat,HuNan_Lat,
GanSu_Lat,FuJian_Lat,XiZang_Lat,GuiZhou_Lat,LiaoNing_Lat,ChongQing_Lat,ShanXi2_Lat,QingHai_Lat,HeiLongJiang_Lat]

def millerToXY (lon, lat):
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
'''
x, y = millerToXY(ShangHai_Lon,ShangHai_Lat)
ShangHai = np.hstack((x,y))
boarder = path.Path(ShangHai)
print(boarder.contains_points([(36780058,7395678)]))
'''
for i in range(len(Lon)):
    x, y = millerToXY(Lon[i],Lat[i])
    province = np.hstack((x,y))
    boarder = path.Path(province)
    if boarder.contains_points([(36770658,7398678)]):
        print('Point is in %s', Provinces[i])
        break
    else:
        print('Point is not in', Provinces[i])