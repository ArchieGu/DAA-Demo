#coding=utf-8  
import sys,os,time  
  
class Point:  
    lng = ''  
    lat = ''  
  
    def __init__(self,lng,lat):  
        self.lng = lng  
        self.lat = lat  
  
    def show(self):  
        print (self.lng,"\t",self.lat)
  
#求外包矩形  
def getPolygonBounds(points):  
    length = len(points)  
    top = down = left = right = points[0]  
    for i in range(1,length):  
        if points[i].lng > top.lng:  
            top = points[i]  
        elif points[i].lng < down.lng:  
            down = points[i]  
        else:  
            pass  
        if points[i].lat > right.lat:  
            right = points[i]  
        elif points[i].lat < left.lat:  
            left = points[i]  
        else:  
            pass  
  
    point0 = Point(top.lng,left.lat)  
    point1 = Point(top.lng,right.lat)  
    point2 = Point(down.lng,right.lat)  
    point3 = Point(down.lng,left.lat)  
    polygonBounds = [point0,point1,point2,point3]  
    return polygonBounds  
  
#判断点是否在外包矩形外  
def isPointInRect(point,polygonBounds):  
    #print "%f>=%f %f<=%f %f>=%f %f<=%f"  % (point.lng,polygonBounds[3].lng,point.lng,polygonBounds[0].lng,point.lat,polygonBounds[3].lat,point.lat,polygonBounds[2].lat)   
    if point.lng >= polygonBounds[3].lng and point.lng <= polygonBounds[0].lng and point.lat >= polygonBounds[3].lat and point.lat <= polygonBounds[2].lat:  
        return True  
    else:  
        return False  
  
#采用射线法判断点集里的每个点是否在多边形集内，返回在多边形集内的点集  
def isPointsInPolygons(xyset,polygonset):  
    inpolygonsetxyList = []  
    for points in polygonset:  
        #求外包矩形  
        polygonBounds = getPolygonBounds(points)  
        for point in xyset:  
            #判断是否在外包矩形内，如果不在，直接返回false  
            if not isPointInRect(point,polygonBounds):  
                #print "out of the Rect"  
                continue  
  
            length = len(points)  
            p = point  
            p1 = points[0]  
            flag = False  
            for i in range(1,length):  
                p2 = points[i]  
                #点与多边形顶点重合  
                if (p.lng == p1.lng and p.lat == p1.lat) or (p.lng == p2.lng and p.lat == p2.lat):  
                    #print "On the Vertex"  
                    inpolygonsetxyList.append(p)  
                    break  
                #判断线段两端点是否在射线两侧  
                if (p2.lat < p.lat and p1.lat >= p.lat) or (p2.lat >= p.lat and p1.lat < p.lat):  
                    #print "On both sides"  
                    #线段上与射线 Y 坐标相同的点的 X 坐标  
                    if (p2.lat == p1.lat):  
                        x = (p1.lng + p2.lng)/2  
                    else:  
                        #x = p2.lng + (p.lat - p2.lat)*(p1.lng - p2.lng)/(p1.lat -p.lat)  
                        x = p2.lng - (p2.lat - p.lat)*(p2.lng - p1.lng)/(p2.lat - p1.lat)  
                    #点在多边形的边上  
                    if (x == p.lng):  
                        #print "On the Edge"  
                        inpolygonsetxyList.append(p)  
                        break  
                    #射线穿过多边形的边界  
                    if (x > p.lng):  
                        #print "i:[%d] throw p1[%f %f] p2[%f %f]" % (i,p1.lng,p1.lat,p2.lng,p2.lat)  
                        flag = not flag  
                    else:  
                        #print "i:[%d] not throw p1[%f %f] p2[%f %f]" % (i,p1.lng,p1.lat,p2.lng,p2.lat)  
                        pass  
                else:  
                    #print "i:[%d] not on both sides p1[%f %f] p2[%f %f]" % (i,p1.lng,p1.lat,p2.lng,p2.lat)  
                    pass  
          
                p1 = p2  
            if flag:  
                inpolygonsetxyList.append(p)  
    return inpolygonsetxyList  
  
if __name__ == "__main__":  
    xyset = []  
    polygonset = []  
     
    #加载所有的多边形到polygonset  
    polyList = ["116.325011 31.068331 116.441755 31.525895 117.184675 31.290317 116.882203 30.927891 116.500131 31.086453 116.325011 31.068331","116.393091 39.921916 116.393413 39.914510 116.393091 39.921916"]  
    for line in polyList:  
        line = line.strip()  
        points = []  
        strList = line.split()  
        pointslen = len(strList)   
        if (pointslen%2 != 0):  
            #print "ERROR: invalid pointslen[%d]" % pointslen  
            continue  
        for i in range(0,pointslen,2):  
            temp = Point(float(strList[i]),float(strList[i+1]))  
            points.append(temp)  
        mid=int(pointslen/2) - 1  
        #print "mid:[%d]" % mid  
        if (points[0].lng != points[mid].lng or points[0].lat != points[mid].lat):  
            #print "ERROR: invalid polygon,begin[%f,%f],end[%f,%f]" % (points[0].lng,points[0].lat,points[pointslen/2].lng,points[pointslen/2].lat)  
            continue  
        polygonset.append(points)  
  
    #加载map的所有输入点到点集xyset  
    xyList = ["116.860971 31.467001","116.256027 32.074063","116.616875 31.195181"]  
    for line in xyList:  
        line = line.strip()  
        xy = line.split()  
        if len(xy) != 2:  
            continue  
        try:  
            x = float(xy[0])  
            y = float(xy[1])  
        except ValueError:  
            continue  
        point = Point(x,y)  
        xyset.append(point)  
    if not xyset:  
        sys.exit(0)  
          
    inpolygonList = isPointsInPolygons(xyset,polygonset)  
    
    for point in inpolygonList:  
        point.show() 