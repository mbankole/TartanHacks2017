import math, io, ast, numpy as np
masterDict = np.load('my_file.npy').item()
earthrad = 2.0904e+7
distDict={}
def dist(p1, p2): #haversine
    cv = math.pi/180
    dN = (p1[0]-p2[0])*cv
    dW = (p1[1]-p2[1])*cv
    dRo = 2*math.asin(math.sqrt((math.sin(dN/2))**2+
        math.cos(p1[0]*cv)*math.cos(p2[0]*cv)*(math.sin(dW/2))**2))
    print(dRo)
    return dRo*earthrad
keys=masterDict.keys()
for key1 in keys:
    for key2 in keys:
        if key1==key2:continue
        distDict[key1]=dist(masterDict[key1],masterDict[key2]) 
print(distDict)