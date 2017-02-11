import math, io, ast, numpy as np
masterDict = np.load('nodeVecDict.npy').item()
earthrad = 2.0904e+7
distDict={}
def dist(p1, p2): #haversine
    cv = math.pi/180
    dN = (p1[0]-p2[0])*cv
    dW = (p1[1]-p2[1])*cv
    dRo = 2*math.asin(math.sqrt((math.sin(dN/2))**2+
        math.cos(p1[0]*cv)*math.cos(p2[0]*cv)*(math.sin(dW/2))**2))
    return dRo*earthrad
keys=masterDict.keys()
tempDict={}
tempList=[]
for key1 in keys:
    for key2 in keys:
        if key1==key2:continue
        tempDict[key1]=key2
        tempDict['distance']=dist(masterDict[key1],masterDict[key2]) 
        tempList+=[tempDict]
        tempDict={}
output={0:tempList}
np.save('distList.npy', output)
print(output)