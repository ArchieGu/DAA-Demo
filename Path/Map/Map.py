# -*- coding: utf-8 -*-
from scipy.spatial import ConvexHull, convex_hull_plot_2d
import math
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import json

xy_coordinate = [] # XY cordinate after conversion
boarder_coordinate = []
lonlat_coordinate = []
def get_obstacles(airportName):
    Test = pd.read_csv('Path/Map/pos_mod.csv', index_col = 0)
    Ob = Test.loc[airportName]
    ox = Ob.values[0:26:2].tolist()
    oy = Ob.values[1:26:2].tolist()
    return ox,oy

prov_airp = {'上海':['上海/虹桥','上海/浦东'],'北京':['北京/首都'],'四川':['稻城/亚丁','宁蒗/泸沽湖','成都/双流','攀枝花/保安营','宜宾/菜坝','西昌/青山','广元/盘龙','达州/河市'],
'云南':['腾冲/驼峰','澜沧/景迈','昆明/长水','丽江/三义','德宏/芒市','保山','西双版纳/嘎洒','普洱/思茅','临沧/博尚'],'贵州':['贵阳/龙洞堡','铜仁/凤凰','兴义/万峰林','黎平'],
'江苏':['淮安/涟水','扬州/泰州','南京/禄口','南通/兴东','常州/奔牛','徐州/观音','连云港/白塔埠'],'浙江':['台州/路桥','杭州/萧山','宁波/栎社','温州/龙湾','衢州','义乌'],'山东':
['日照/山字河','济南/遥墙','青岛/流亭','烟台/蓬莱','临沂/沭埠岭','潍坊','东营','济宁/曲阜'],'福建':['三明/沙县','福州/长乐','厦门/高崎','泉州/晋江'],'江西':['宜春/明月山','上饶/三清山','南昌/昌北','赣州/黄金','景德镇/罗家','井冈山'],
'安徽':['池州/九华山','合肥/新桥','黄山/屯溪','安庆'],'天津':['天津/滨海'],'河北':['唐山/三女河','石家庄/正定','秦皇岛/北戴河'],'山西':['临汾/乔李','太原/武宿','大同/云冈'],'内蒙古':['阿尔山/伊尔施','鄂尔多斯/伊金霍洛','扎兰屯/成吉思汗','巴彦淖尔/天吉泰','博乐/阿拉山口','二连浩特/赛乌素','乌兰察布/集宁','呼和浩特/白塔','呼伦贝尔/海拉尔','赤峰/玉龙','满洲里/西郊','乌兰浩特/依勒力特','锡林浩特','乌海','包头'],
'辽宁':['鞍山/腾鳌','营口/兰旗','沈阳/桃仙','大连/周水子','锦州/锦州湾','丹东/浪头','朝阳'],'吉林':['通化/三源浦','白山/长白山','白城/长安','长春/龙嘉','延吉/朝阳川'],'黑龙江':['鸡西/兴凯湖','漠河/古莲','抚远/东极','大庆/萨尔图','加格达奇/嘎仙','伊春/林都','哈尔滨/太平','齐齐哈尔/三家子','佳木斯','牡丹江/海浪','黑河/瑷珲'],'陕西':['西安/咸阳','汉中/城固','榆林/榆阳'],'甘肃':['金昌/金川','甘南/夏河','张掖/甘州','兰州/中川','敦煌','嘉峪关','庆阳/西峰'],
'青海':['玉树/巴塘','海西/德令哈','海西/花土沟','果洛/玛沁','西宁/曹家堡'],'宁夏':['固原/六盘山','中卫/沙坡头','银川/河东'],'新疆':['石河子/花园','布尔津/喀纳斯','克拉玛依','且末/玉都','乌鲁木齐/地窝堡','阿克苏/温宿','喀什','伊宁','塔城','阿勒泰','库车/龟兹','且末/玉都','和田','新源/那拉提','富蕴/可可托海','吐鲁番/交河'],'广东':['揭阳/潮汕','广州/白云','深圳/宝安','珠海/金湾','湛江','梅县/长岗岌'],'广西':['百色/巴马','南宁/吴圩','桂林/两江',
'柳州/白莲','北海/福成','梧州','河池/金城江'],'海南':['琼海/博鳌','海口/美兰','三亚/凤凰'],'湖北':['神农架/红坪','十堰/武当山','武汉/天河','宜昌/三峡','襄阳/刘集','恩施/许家坪'],'湖南':['衡阳/南岳','长沙/黄花','张家界/荷花','常德/桃花源','永州/零陵','怀化/芷江'],'河南':['郑州/新郑','洛阳','南阳/姜营'],'重庆':['黔江/武陵山','重庆/江北','万州/五桥']}    

'''

ox_all, oy_all = [], []
for lenth in range(0,int(len(xy_coordinate)/13)):
    temp = np.array(xy_coordinate[lenth*13:lenth*13+13])
    points_x, points_y = [], []

    hull = ConvexHull(temp)
    for simplex in hull.simplices:
        plt.plot(temp[simplex, 0], temp[simplex, 1], 'k')
        #plt.plot(temp[hull.vertices,0], temp[hull.vertices,1], '.k')
        #    
    points_x = np.array(temp[hull.vertices,0])
    points_y = np.array(temp[hull.vertices,1])
    
    for i in range(len(points_x)-1):
        ox_all.append(points_x[i])
        oy_all.append(points_y[i])
        countx = points_x[i+1] - points_x[i]
        county = points_y[i+1] - points_y[i]
        if county == 0:
            for j in range(0,countx,1000):
                ox_all.append(points_x[i]+j)
                oy_all.append(points_y[i])
        elif countx == 0:
            for j in range(0,county,1000):
                ox_all.append(points_x[i])
                oy_all.append(points_y[i]+j)
        elif countx > 0:
            k = county/countx
            for j in range(0,abs(int(county/k)),1000):
                ox_all.append(points_x[i]+j)
                oy_all.append(points_y[i]+j*k)
        else:
            k = county/countx
            for j in range(0,abs(int(county/k)),1000):
                ox_all.append(points_x[i]-j)
                oy_all.append(points_y[i]-j*k)
    countx = points_x[len(points_x)-1] - points_x[0]
    county = points_y[len(points_x)-1] - points_y[0]
    if county == 0:
        if countx < 0 :
            for j in range(0,countx,1000):
                ox_all.append(points_x[len(points_x)-1]+j)
                oy_all.append(points_y[len(points_x)-1])
        else: 
            for j in range(0,countx,1000):
                ox_all.append(points_x[0]+j)
                oy_all.append(points_y[0])
    elif countx == 0:
        if county < 0 :
            for j in range(0,county,1000):
                ox_all.append(points_x[len(points_x)-1])
                oy_all.append(points_y[len(points_x)-1]+j)
        else:
            for j in range(0,county,1000):
                ox_all.append(points_x[0])
                oy_all.append(points_y[0]+j)
    else:
        k = county/countx
        if k > 0:
            if countx < 0 :
                for j in range(0,abs(int(county/k)),1000):
                    ox_all.append(points_x[len(points_x)-1]+j)
                    oy_all.append(points_y[len(points_x)-1]+j*k)
            else:
                for j in range(0,abs(int(county/k)),1000):
                    ox_all.append(points_x[0]+j)
                    oy_all.append(points_y[0]+j*k)
        else:
            if countx < 0 :
                for j in range(0,abs(int(county/k)),1000):
                    ox_all.append(points_x[len(points_x)-1]+j)
                    oy_all.append(points_y[len(points_x)-1]+j*k)
            else:
                for j in range(0,abs(int(county/k)),1000):
                    ox_all.append(points_x[0]+j)
                    oy_all.append(points_y[0]+j*k)

for i in range(len(boarder_coordinate)):
    ox_all.append(boarder_coordinate[i][0])
    oy_all.append(boarder_coordinate[i][1])


plt.plot(ox_all,oy_all,".k")
plt.show()
'''    
