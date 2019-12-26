"""

Hybrid A* path planning

author: Zheng Zh (@Zhengzh)

"""

import heapq
import scipy.spatial
import numpy as np
import math
import matplotlib.pyplot as plt
import sys
from time import time
from BackEnd.Path.Map.Map import prov_airp,get_obstacles
from scipy.spatial import ConvexHull, convex_hull_plot_2d
from BackEnd.Path.Map.utils import load_specific_province, millerToXY

try:
    from BackEnd.Path.HybridAStar.hybrid_a_star import *
    from BackEnd.Path.HybridAStar.a_star import dp_planning  # , calc_obstacle_map
    import BackEnd.Path.ReedsSheppPath.reeds_shepp_path_planning as rs
    from BackEnd.Path.HybridAStar.uav import move, check_uav_collision, MAX_STEER, WB, plot_uav
    from BackEnd.Path.Map.Map import *
except:
    raise

PI = 3.1415926535898
XY_GRID_RESOLUTION = 10000.0  # [corrdinate to km]
YAW_GRID_RESOLUTION = np.deg2rad(15.0)  # [rad]
MOTION_RESOLUTION = 2000  # [m] path interporate resolution
N_STEER = 20.0  # number of steer command
H_COST = 1.0
VR = 5000.0  # robot radius

SB_COST = 100.0  # switch back penalty cost
BACK_COST = 500000.0  # backward penalty cost
STEER_CHANGE_COST = 5.0  # steer angle change penalty cost
STEER_COST = 1.0  # steer angle change penalty cost
H_COST = 5.0  # Heuristic cost

show_animation = True


class Node:

    def __init__(self, xind, yind, yawind, direction,
                 xlist, ylist, yawlist, directions,
                 steer=0.0, pind=None, cost=None):
        self.xind = xind
        self.yind = yind
        self.yawind = yawind
        self.direction = direction
        self.xlist = xlist
        self.ylist = ylist
        self.yawlist = yawlist
        self.directions = directions
        self.steer = steer
        self.pind = pind
        self.cost = cost


class Path:

    def __init__(self, xlist, ylist, yawlist, directionlist, cost):
        self.xlist = xlist
        self.ylist = ylist
        self.yawlist = yawlist
        self.directionlist = directionlist
        self.cost = cost


class KDTree:
    """
    Nearest neighbor search class with KDTree
    """

    def __init__(self, data):
        # store kd-tree
        self.tree = scipy.spatial.cKDTree(data)

    def search(self, inp, k=1):
        """
        Search NN
        inp: input data, single frame or multi frame
        """
        if len(inp.shape) >= 2:  # multi input
            index = []
            dist = []
            for i in inp.T:
                idist, iindex = self.tree.query(i, k=k)
                index.append(iindex)
                dist.append(idist)

            return index, dist

        dist, index = self.tree.query(inp, k=k)
        return index, dist

    def search_in_distance(self, inp, r):
        """
        find points with in a distance r
        """

        index = self.tree.query_ball_point(inp, r)
        return index


class Config:

    def __init__(self, ox, oy, xyreso, yawreso):
        min_x_m = min(ox)
        min_y_m = min(oy)
        max_x_m = max(ox)
        max_y_m = max(oy)
 
        ox.append(min_x_m)
        oy.append(min_y_m)
        ox.append(max_x_m)
        oy.append(max_y_m)

        self.minx = round(min_x_m / xyreso)
        self.miny = round(min_y_m / xyreso)
        self.maxx = round(max_x_m / xyreso)
        self.maxy = round(max_y_m / xyreso)
        self.xw = round(self.maxx - self.minx)
        self.yw = round(self.maxy - self.miny)

        self.minyaw = round(- math.pi / yawreso) - 1
        self.maxyaw = round(math.pi / yawreso)
        self.yaww = round(self.maxyaw - self.minyaw)


def calc_motion_inputs():

    for steer in np.concatenate((np.linspace(-MAX_STEER, MAX_STEER, N_STEER),[0.0])):
        for d in [1, -1]:
            yield [steer, d]


def get_neighbors(current, config, ox, oy, kdtree):

    for steer, d in calc_motion_inputs():
        node = calc_next_node(current, steer, d, config, ox, oy, kdtree)
        if node and verify_index(node, config):
            yield node


def calc_next_node(current, steer, direction, config, ox, oy, kdtree):
    x, y, yaw = current.xlist[-1], current.ylist[-1], current.yawlist[-1]

    arc_l = XY_GRID_RESOLUTION * 1.5
    xlist, ylist, yawlist = [], [], []
    for dist in np.arange(0, arc_l, MOTION_RESOLUTION):
        x, y, yaw = move(x, y, yaw, MOTION_RESOLUTION * direction, steer)
        xlist.append(x)
        ylist.append(y)
        yawlist.append(yaw)

    if not check_uav_collision(xlist, ylist, yawlist, ox, oy, kdtree):
        return None

    d = direction == 1
    xind = round(x / XY_GRID_RESOLUTION)
    yind = round(y / XY_GRID_RESOLUTION)
    yawind = round(yaw / YAW_GRID_RESOLUTION)

    addedcost = 0.0

    if d != current.direction:
        addedcost += SB_COST

    # steer penalty
    addedcost += STEER_COST * abs(steer)

    # steer change penalty
    addedcost += STEER_CHANGE_COST * abs(current.steer - steer)

    cost = current.cost + addedcost + arc_l

    node = Node(xind, yind, yawind, d, xlist,
                ylist, yawlist, [d],
                pind=calc_index(current, config),
                cost=cost, steer=steer)

    return node


def is_same_grid(n1, n2):
    if n1.xind == n2.xind and n1.yind == n2.yind and n1.yawind == n2.yawind:
        return True
    return False


def analytic_expantion(current, goal, c, ox, oy, kdtree):

    sx = current.xlist[-1]
    sy = current.ylist[-1]
    syaw = current.yawlist[-1]

    gx = goal.xlist[-1]
    gy = goal.ylist[-1]
    gyaw = goal.yawlist[-1]

    max_curvature = math.tan(MAX_STEER) / WB
    paths = rs.calc_paths(sx, sy, syaw, gx, gy, gyaw,
                          max_curvature, step_size=MOTION_RESOLUTION)

    if not paths:
        return None

    best_path, best = None, None
    for path in paths:
        
        if check_uav_collision(path.x, path.y, path.yaw, ox, oy, kdtree):
            cost = calc_rs_path_cost(path)
            if not best or best > cost:
                best = cost
                best_path = path
    return best_path


def update_node_with_analystic_expantion(current, goal,
                                         c, ox, oy, kdtree):
    apath = analytic_expantion(current, goal, c, ox, oy, kdtree)

    if apath:
        plt.plot(apath.x, apath.y)
        fx = apath.x[1:]
        fy = apath.y[1:]
        fyaw = apath.yaw[1:]

        fcost = current.cost + calc_rs_path_cost(apath)
        fpind = calc_index(current, c)
        fd = []
        for d in apath.directions[1:]:
            fd.append(d >= 0)

        fsteer = 0.0
        fpath = Node(current.xind, current.yind, current.yawind,
                     current.direction, fx, fy, fyaw, fd,
                     cost=fcost, pind=fpind, steer=fsteer)
        return True, fpath

    return False, None


def calc_rs_path_cost(rspath):

    cost = 0.0
    for l in rspath.lengths:
        if l >= 0:  # forward
            cost += l
        else:  # back
            cost += abs(l) * BACK_COST
    # swich back penalty
    for i in range(len(rspath.lengths) - 1):
        if rspath.lengths[i] * rspath.lengths[i + 1] < 0.0:  # switch back
            cost += SB_COST

    # steer penalyty
    for ctype in rspath.ctypes:
        if ctype != "S":  # curve
            cost += STEER_COST * abs(MAX_STEER)

    # ==steer change penalty
    # calc steer profile
    nctypes = len(rspath.ctypes)
    ulist = [0.0] * nctypes
    for i in range(nctypes):
        if rspath.ctypes[i] == "R":
            ulist[i] = - MAX_STEER
        elif rspath.ctypes[i] == "L":
            ulist[i] = MAX_STEER

    for i in range(len(rspath.ctypes) - 1):
        cost += STEER_CHANGE_COST * abs(ulist[i + 1] - ulist[i])

    return cost


def hybrid_a_star_planning(start, goal, ox, oy, xyreso, yawreso):
    """
    start
    goal
    ox: x position list of Obstacles [m]
    oy: y position list of Obstacles [m]
    xyreso: grid resolution [m]
    yawreso: yaw angle resolution [rad]
    """
    start[2], goal[2] = rs.pi_2_pi(start[2]), rs.pi_2_pi(goal[2])

    tox, toy = ox[:], oy[:]
    obkdtree = KDTree(np.vstack((tox, toy)).T)
    
    config = Config(tox, toy, xyreso, yawreso)

    nstart = Node(round(start[0] / xyreso), round(start[1] / xyreso), round(start[2] / yawreso),
                  True, [start[0]], [start[1]], [start[2]], [True], cost=0)            
    ngoal = Node(round(goal[0] / xyreso), round(goal[1] / xyreso), round(goal[2] / yawreso),
                 True, [goal[0]], [goal[1]], [goal[2]], [True])

    openList, closedList = {}, {}

    _, _, h_dp = dp_planning(nstart.xlist[-1], nstart.ylist[-1],
                             ngoal.xlist[-1], ngoal.ylist[-1], ox, oy, xyreso, VR)

    pq = []
    openList[calc_index(nstart, config)] = nstart
    heapq.heappush(pq, (calc_cost(nstart, h_dp, ngoal, config),
                        calc_index(nstart, config)))

    while True:
        if not openList:
            print("Error: Cannot find path, No open set")
            return [], [], []

        cost, c_id = heapq.heappop(pq)
        if c_id in openList:
            current = openList.pop(c_id)
            closedList[c_id] = current
        else:
            continue

        if show_animation:  # pragma: no cover
            plt.plot(current.xlist[-1], current.ylist[-1], "xc")
            if len(closedList.keys()) % 10 == 0:
                plt.pause(0.001)

        isupdated, fpath = update_node_with_analystic_expantion(
            current, ngoal, config, ox, oy, obkdtree)

        if isupdated:
            break

        for neighbor in get_neighbors(current, config, ox, oy, obkdtree):
            neighbor_index = calc_index(neighbor, config)
            if neighbor_index in closedList:
                continue
            if neighbor not in openList \
                    or openList[neighbor_index].cost > neighbor.cost:
                heapq.heappush(
                    pq, (calc_cost(neighbor, h_dp, ngoal, config),
                         neighbor_index))
                openList[neighbor_index] = neighbor

    path = get_final_path(closedList, fpath, nstart, config)
    return path


def calc_cost(n, h_dp, goal, c):
    ind = (n.yind - c.miny) * c.xw + (n.xind - c.minx)
    if ind not in h_dp:
        return n.cost + 999999999  # collision cost
    return n.cost + H_COST * h_dp[ind].cost


def get_final_path(closed, ngoal, nstart, config):
    rx, ry, ryaw = list(reversed(ngoal.xlist)), list(
        reversed(ngoal.ylist)), list(reversed(ngoal.yawlist))
    direction = list(reversed(ngoal.directions))
    nid = ngoal.pind
    finalcost = ngoal.cost

    while nid:
        n = closed[nid]
        rx.extend(list(reversed(n.xlist)))
        ry.extend(list(reversed(n.ylist)))
        ryaw.extend(list(reversed(n.yawlist)))
        direction.extend(list(reversed(n.directions)))

        nid = n.pind

    rx = list(reversed(rx))
    ry = list(reversed(ry))
    ryaw = list(reversed(ryaw))
    direction = list(reversed(direction))

    # adjust first direction
    direction[0] = direction[1]
    path = Path(rx, ry, ryaw, direction, finalcost)
    return path

def verify_index(node, c):
    xind, yind = node.xind, node.yind
    if xind >= c.minx and xind <= c.maxx and yind >= c.miny \
            and yind <= c.maxy:
        return True

    return False


def calc_index(node, c):
    ind = (node.yawind - c.minyaw) * c.xw * c.yw + \
        (node.yind - c.miny) * c.xw + (node.xind - c.minx)
    if ind <= 0:
        print("Error(calc_index):", ind)

def getEquidistantPoints(p1, p2, parts):
    return np.linspace(p1[0], p2[0], parts+1),np.linspace(p1[1], p2[1], parts+1)
    #return zip(np.linspace(p1[0], p2[0], parts+1), np.linspace(p1[1], p2[1], parts+1))

def obstacles_process(ox,oy):
    coor_array = np.concatenate((ox,oy),axis=1)
    extend_points_x,extend_points_y = [],[]
    for lenth in range(0,int(len(coor_array)/13)):
        temp = coor_array[lenth*13:lenth*13+13]

        hull = ConvexHull(temp)
        '''
        for simplex in hull.simplices:
            plt.plot(temp[simplex, 0], temp[simplex, 1], 'k')
            plt.plot(temp[hull.vertices,0], temp[hull.vertices,1], '.k')
        '''    
        bound_points = np.array(temp[hull.vertices])
        
        for i in range(len(bound_points)-1):
            temp_points_x , temp_points_y = getEquidistantPoints(bound_points[i],bound_points[i+1],2000)
            extend_points_x.append(temp_points_x)
            extend_points_y.append(temp_points_y) 
        temp_points_x , temp_points_y = getEquidistantPoints(bound_points[0],bound_points[-1],2000)
        extend_points_x.append(temp_points_x)
        extend_points_y.append(temp_points_y) 
    extend_points_x = np.array(extend_points_x)
    extend_points_y = np.array(extend_points_y)
    return extend_points_x,extend_points_y

def load_province_boarder(province):
    province_points = load_specific_province(province)
    prov_lon = province_points[:,:1]
    prov_lat = province_points[:,1:2]
    prov_lon, prov_lat = millerToXY(prov_lon,prov_lat)
    return prov_lon, prov_lat


def hybrid_path_planning(point_start,point_end,province):
    start_time = time()
    ox, oy = [],[]
    if province not in prov_airp:
        ox,oy = load_province_boarder(province)
    else:
        for airport in prov_airp[province]:
            ox.append(get_obstacles(airport)[0])
            oy.append(get_obstacles(airport)[1]) 
    ox = np.reshape(ox,(-1,1))
    oy = np.reshape(oy,(-1,1))

    extend_points_x, extend_points_y = obstacles_process(ox,oy)
    extend_points_x = np.reshape(extend_points_x,(-1,1))
    extend_points_y = np.reshape(extend_points_y,(-1,1))
    
    ox = np.vstack((ox,extend_points_x)).flatten().tolist()
    oy = np.vstack((oy,extend_points_y)).flatten().tolist()

    minx_bound = min(min(ox),point_start[0],point_end[0])
    miny_bound = min(min(oy),point_start[1],point_end[1])
    maxx_bound = max(max(ox),point_start[0],point_end[0])
    maxy_bound = max(max(oy),point_start[1],point_end[1])

    ox.append(minx_bound-20000)
    ox.append(maxx_bound+20000)
    oy.append(miny_bound-5000)
    oy.append(maxy_bound+5000)

    prov_lon, prov_lat = load_province_boarder(province)

    degree = math.atan2(point_end[1]- point_start[1], point_end[0]-point_start[0])*180/PI

    start = [point_start[0], point_start[1], degree]
    goal = [point_end[0], point_end[1], degree]
    path = hybrid_a_star_planning(
        start, goal, ox, oy, XY_GRID_RESOLUTION, YAW_GRID_RESOLUTION)

    x = path.xlist
    y = path.ylist
    yaw = path.yawlist

    return {
        'x': x,
        'y': y,
        'yaw': yaw,
        'heading':degree
    }
