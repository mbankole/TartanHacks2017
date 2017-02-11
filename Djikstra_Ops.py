# pathing shit here
import math, io, ast, numpy as np
earthrad = 2.0904e+7


def find_path():
    """takes in starting node, end node, """
    pass


def dist(p1, p2): #haversine
    cv = math.pi/180
    dN = (p1[0]-p2[0])*cv
    dW = (p1[1]-p2[1])*cv
    dRo = 2*math.asin(math.sqrt((math.sin(dN/2))**2+
        math.cos(p1[0]*cv)*math.cos(p2[0]*cv)*(math.sin(dW/2))**2))
    print(dRo)
    return dRo*earthrad

