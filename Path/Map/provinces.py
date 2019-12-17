import numpy as np

ShangHai_Lon = []
ShangHai_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/上海.txt') 
data = np.reshape(data,(-1,2))
ShangHai_Lon = data[:,:1]
ShangHai_Lat = data[:,1:2]


YunNan_Lon = []
YunNan_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/云南.txt') 
data = np.reshape(data,(-1,2))
YunNan_Lon = data[:,:1]
YunNan_Lat = data[:,1:2]

NeiMengGu_Lon = []
NeiMengGu_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/内蒙古.txt') 
data = np.reshape(data,(-1,2))

NeiMengGu_Lon = data[:,:1]
NeiMengGu_Lat = data[:,1:2]

Beijing_Lon = []
Beijing_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/北京.txt') 
data = np.reshape(data,(-1,2))

Beijing_Lon = data[:,:1]
Beijing_Lat = data[:,1:2]

JiLin_Lon = []
JiLin_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/吉林.txt') 
data = np.reshape(data,(-1,2))

JiLin_Lon = data[:,:1]
JiLin_Lat = data[:,1:2]


SiChuan_Lon = []
SiChuan_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/四川.txt') 
data = np.reshape(data,(-1,2))

SiChuan_Lon = data[:,:1]
SiChuan_Lat = data[:,1:2]

TianJin_Lon = []
TianJin_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/天津.txt') 
data = np.reshape(data,(-1,2))

TianJin_Lon = data[:,:1]
TianJin_Lat = data[:,1:2]

NingXia_Lon = []
NingXia_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/宁夏.txt') 
data = np.reshape(data,(-1,2))

NingXia_Lon = data[:,:1]
NingXia_Lat = data[:,1:2]

AnHui_Lon = []
AnHui_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/安徽.txt') 
data = np.reshape(data,(-1,2))

AnHui_Lon = data[:,:1]
AnHui_Lat = data[:,1:2]

ShanDong_Lon = []
ShanDong_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/山东.txt') 
data = np.reshape(data,(-1,2))

ShanDong_Lon = data[:,:1]
ShanDong_Lat = data[:,1:2]

ShanXi_Lon = []
ShanXi_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/山西.txt') 
data = np.reshape(data,(-1,2))

ShanXi_Lon = data[:,:1]
ShanXi_Lat = data[:,1:2]


GuangDong_Lon = []
GuangDong_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/广东.txt') 
data = np.reshape(data,(-1,2))

GuangDong_Lon = data[:,:1]
GuangDong_Lat = data[:,1:2]

GuangXi_Lon = []
GuangXi_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/广西.txt') 
data = np.reshape(data,(-1,2))

GuangXi_Lon = data[:,:1]
GuangXi_Lat = data[:,1:2]

XinJiang_Lon = []
XinJiang_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/新疆.txt') 
data = np.reshape(data,(-1,2))

XinJiang_Lon = data[:,:1]
XinJiang_Lat = data[:,1:2]

JiangSu_Lon = []
JiangSu_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/江苏.txt') 
data = np.reshape(data,(-1,2))

JiangSu_Lon = data[:,:1]
JiangSu_Lat = data[:,1:2]

JiangXi_Lon = []
JiangXi_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/江西.txt') 
data = np.reshape(data,(-1,2))

JiangXi_Lon = data[:,:1]
JiangXi_Lat = data[:,1:2]

HeBei_Lon = []
HeBei_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/河北.txt') 
data = np.reshape(data,(-1,2))

HeBei_Lon = data[:,:1]
HeBei_Lat = data[:,1:2]

HeNan_Lon = []
HeNan_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/河南.txt') 
data = np.reshape(data,(-1,2))

HeNan_Lon = data[:,:1]
HeNan_Lat = data[:,1:2]

ZheJiang_Lon = []
ZheJiang_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/浙江.txt') 
data = np.reshape(data,(-1,2))

ZheJiang_Lon = data[:,:1]
ZheJiang_Lat = data[:,1:2]

HaiNan_Lon = []
HaiNan_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/海南.txt') 
data = np.reshape(data,(-1,2))

HaiNan_Lon = data[:,:1]
HaiNan_Lat = data[:,1:2]

HuBei_Lon = []
HuBei_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/湖北.txt') 
data = np.reshape(data,(-1,2))

HuBei_Lon = data[:,:1]
HuBei_Lat = data[:,1:2]


HuNan_Lon = []
HuNan_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/湖南.txt') 
data = np.reshape(data,(-1,2))

HuNan_Lon = data[:,:1]
HuNan_Lat = data[:,1:2]

GanSu_Lon = []
GanSu_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/甘肃.txt') 
data = np.reshape(data,(-1,2))

GanSu_Lon = data[:,:1]
GanSu_Lat = data[:,1:2]

FuJian_Lon = []
FuJian_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/福建.txt') 
data = np.reshape(data,(-1,2))

FuJian_Lon = data[:,:1]
FuJian_Lat = data[:,1:2]

XiZang_Lon = []
XiZang_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/西藏.txt') 
data = np.reshape(data,(-1,2))

XiZang_Lon = data[:,:1]
XiZang_Lat = data[:,1:2]

GuiZhou_Lon = []
GuiZhou_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/贵州.txt') 
data = np.reshape(data,(-1,2))

GuiZhou_Lon = data[:,:1]
GuiZhou_Lat = data[:,1:2]

LiaoNing_Lon = []
LiaoNing_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/辽宁.txt') 
data = np.reshape(data,(-1,2))

LiaoNing_Lon = data[:,:1]
LiaoNing_Lat = data[:,1:2]

ChongQing_Lon = []
ChongQing_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/重庆.txt') 
data = np.reshape(data,(-1,2))

ChongQing_Lon = data[:,:1]
ChongQing_Lat = data[:,1:2]

ShanXi2_Lon = []
ShanXi2_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/陕西.txt') 
data = np.reshape(data,(-1,2))

ShanXi2_Lon = data[:,:1]
ShanXi2_Lat = data[:,1:2]

QingHai_Lon = []
QingHai_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/青海.txt') 
data = np.reshape(data,(-1,2))

QingHai_Lon = data[:,:1]
QingHai_Lat = data[:,1:2]

HeiLongJiang_Lon = []
HeiLongJiang_Lat = []
data = np.loadtxt('/Users/tianyuli/Documents/BUAA/创新港工作/china/黑龙江.txt') 
data = np.reshape(data,(-1,2))

HeiLongJiang_Lon = data[:,:1]
HeiLongJiang_Lat = data[:,1:2]










        

        
        