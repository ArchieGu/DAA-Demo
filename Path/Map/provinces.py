import numpy as np

ShangHai_Lon = []
ShangHai_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/上海.txt') 
data = np.reshape(data,(-1,2))

for i in range(len(data)):
    ShangHai_Lon.append(data[i][0])
    ShangHai_Lat.append(data[i][1])

YunNan_Lon = []
YunNan_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/云南.txt') 
data = np.reshape(data,(-1,2))

for i in range(len(data)):
    YunNan_Lon.append(data[i][0])
    YunNan_Lat.append(data[i][1])

NeiMengGu_Lon = []
NeiMengGu_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/内蒙古.txt') 
data = np.reshape(data,(-1,2))

for i in range(len(data)):
    NeiMengGu_Lon.append(data[i][0])
    NeiMengGu_Lat.append(data[i][1])

Beijing_Lon = []
Beijing_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/北京.txt') 
data = np.reshape(data,(-1,2))

for i in range(len(data)):
    Beijing_Lon.append(data[i][0])
    Beijing_Lat.append(data[i][1])

JiLin_Lon = []
JiLin_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/吉林.txt') 
data = np.reshape(data,(-1,2))

for i in range(len(data)):
    JiLin_Lon.append(data[i][0])
    JiLin_Lat.append(data[i][1])


SiChuan_Lon = []
SiChuan_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/四川.txt') 
data = np.reshape(data,(-1,2))

for i in range(len(data)):
    SiChuan_Lon.append(data[i][0])
    SiChuan_Lat.append(data[i][1])

TianJin_Lon = []
TianJin_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/天津.txt') 
data = np.reshape(data,(-1,2))

for i in range(len(data)):
    TianJin_Lon.append(data[i][0])
    TianJin_Lat.append(data[i][1])

NingXia_Lon = []
NingXia_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/宁夏.txt') 
data = np.reshape(data,(-1,2))

for i in range(len(data)):
    NingXia_Lon.append(data[i][0])
    NingXia_Lat.append(data[i][1])

AnHui_Lon = []
AnHui_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/安徽.txt') 
data = np.reshape(data,(-1,2))

for i in range(len(data)):
    AnHui_Lon.append(data[i][0])
    AnHui_Lat.append(data[i][1])

ShanDong_Lon = []
ShanDong_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/山东.txt') 
data = np.reshape(data,(-1,2))

for i in range(len(data)):
    ShanDong_Lon.append(data[i][0])
    ShanDong_Lat.append(data[i][1])

ShanXi_Lon = []
ShanXi_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/山西.txt') 
data = np.reshape(data,(-1,2))

for i in range(len(data)):
    ShanXi_Lon.append(data[i][0])
    ShanXi_Lat.append(data[i][1])

GuangDong_Lon = []
GuangDong_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/广东.txt') 
data = np.reshape(data,(-1,2))

for i in range(len(data)):
    GuangDong_Lon.append(data[i][0])
    GuangDong_Lat.append(data[i][1])

GuangXi_Lon = []
GuangXi_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/广西.txt') 
data = np.reshape(data,(-1,2))

for i in range(len(data)):
    GuangXi_Lon.append(data[i][0])
    GuangXi_Lat.append(data[i][1])

XinJiang_Lon = []
XinJiang_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/新疆.txt') 
data = np.reshape(data,(-1,2))

for i in range(len(data)):
    XinJiang_Lon.append(data[i][0])
    XinJiang_Lat.append(data[i][1])

JiangSu_Lon = []
JiangSu_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/江苏.txt') 
data = np.reshape(data,(-1,2))

for i in range(len(data)):
    JiangSu_Lon.append(data[i][0])
    JiangSu_Lat.append(data[i][1])

JiangXi_Lon = []
JiangXi_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/江西.txt') 
data = np.reshape(data,(-1,2))

for i in range(len(data)):
    JiangXi_Lon.append(data[i][0])
    JiangXi_Lat.append(data[i][1])

HeBei_Lon = []
HeBei_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/河北.txt') 
data = np.reshape(data,(-1,2))

for i in range(len(data)):
    HeBei_Lon.append(data[i][0])
    HeBei_Lat.append(data[i][1])

HeNan_Lon = []
HeNan_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/河南.txt') 
data = np.reshape(data,(-1,2))

for i in range(len(data)):
    HeNan_Lon.append(data[i][0])
    HeNan_Lat.append(data[i][1])

ZheJiang_Lon = []
ZheJiang_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/浙江.txt') 
data = np.reshape(data,(-1,2))

for i in range(len(data)):
    ZheJiang_Lon.append(data[i][0])
    ZheJiang_Lat.append(data[i][1])

HaiNan_Lon = []
HaiNan_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/海南.txt') 
data = np.reshape(data,(-1,2))

for i in range(len(data)):
    HaiNan_Lon.append(data[i][0])
    HaiNan_Lat.append(data[i][1])

HuBei_Lon = []
HuBei_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/湖北.txt') 
data = np.reshape(data,(-1,2))

for i in range(len(data)):
    HuBei_Lon.append(data[i][0])
    HuBei_Lat.append(data[i][1])

HuNan_Lon = []
HuNan_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/湖南.txt') 
data = np.reshape(data,(-1,2))

for i in range(len(data)):
    HuNan_Lon.append(data[i][0])
    HuNan_Lat.append(data[i][1])

GanSu_Lon = []
GanSu_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/甘肃.txt') 
data = np.reshape(data,(-1,2))

for i in range(len(data)):
    GanSu_Lon.append(data[i][0])
    GanSu_Lat.append(data[i][1])

FuJian_Lon = []
FuJian_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/福建.txt') 
data = np.reshape(data,(-1,2))

for i in range(len(data)):
    FuJian_Lon.append(data[i][0])
    FuJian_Lat.append(data[i][1])

XiZang_Lon = []
XiZang_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/西藏.txt') 
data = np.reshape(data,(-1,2))

for i in range(len(data)):
    XiZang_Lon.append(data[i][0])
    XiZang_Lat.append(data[i][1])

GuiZhou_Lon = []
GuiZhou_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/贵州.txt') 
data = np.reshape(data,(-1,2))

for i in range(len(data)):
    GuiZhou_Lon.append(data[i][0])
    GuiZhou_Lat.append(data[i][1])

LiaoNing_Lon = []
LiaoNing_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/辽宁.txt') 
data = np.reshape(data,(-1,2))

for i in range(len(data)):
    LiaoNing_Lon.append(data[i][0])
    LiaoNing_Lat.append(data[i][1])

ChongQing_Lon = []
ChongQing_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/重庆.txt') 
data = np.reshape(data,(-1,2))

for i in range(len(data)):
    ChongQing_Lon.append(data[i][0])
    ChongQing_Lat.append(data[i][1])

ShanXi2_Lon = []
ShanXi2_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/陕西.txt') 
data = np.reshape(data,(-1,2))

for i in range(len(data)):
    ShanXi2_Lon.append(data[i][0])
    ShanXi2_Lat.append(data[i][1])

QingHai_Lon = []
QingHai_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/青海.txt') 
data = np.reshape(data,(-1,2))

for i in range(len(data)):
    QingHai_Lon.append(data[i][0])
    QingHai_Lat.append(data[i][1])

HeiLongJiang_Lon = []
HeiLongJiang_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/黑龙江.txt') 
data = np.reshape(data,(-1,2))

for i in range(len(data)):
    HeiLongJiang_Lon.append(data[i][0])
    HeiLongJiang_Lat.append(data[i][1])










        

        
        