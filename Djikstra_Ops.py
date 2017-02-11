import numpy as np
nodeVecDict = np.load('nodeVecDict.npy').item()
distList = np.load('distList.npy').item()[0]
relativeDist=200
def isAdj(name1, name2, dist):
    name1,name2=name1.strip(),name2.strip()
    print((name1[0:3]==name2[0:3] or dist<relativeDist))
    return (name1[0:3]==name2[0:3] or dist<relativeDist)
def getAdjList(distList):
    adjList=[]
    adjDict={}
    names = nodeVecDict.keys()
    for name in names:
        adjDict[name]=[]
        for dict in distList:
            if name not in dict: continue
            if isAdj(name, dict[name],dict['distance']):
                adjDict[name]=adjDict.get(name)+[dict[name]]
        adjList+=[adjDict]        
        adjDict={}
    return adjList
print(distList)
def find_path():
    #takes in starting node, end node
    pass


