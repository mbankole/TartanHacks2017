import numpy as np, math
nodeVecDict = np.load('nodeVecDict.npy').item()
distList = np.load('distList.npy').item()[0]
bigList = np.load('bigList.npy').item()[0]
relativeDist=200
def isAdj(name1, name2, dist):
    name1,name2=name1.strip(),name2.strip()
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
adjList=getAdjList(distList)
def find_path(sourcename):
    Q = nodeVecDict.keys()
    unvisited=Q
    dist={}
    prev={}
    for v in Q:
        dist[v]=math.inf if v!=sourcename else 0
        prev[v]='~~~' #undefined
    while len(Q)>=1:
        u = getMin(dist)
        Q.pop(u)
        for dict in adjList:
            if u in dict:
                for neighbor in dict[u]:
                    alt=dict['distance']+dist[u]
                    if alt<dist[neighbor]:
                        dist[neighbor]=alt
                        prev[neighbor]=u
    return dist, prev
output=[]
temp={}
def getDist(name1, name2):
    for dict in distList:
        if name1 in dict and name2==dict[name1]:
            return dict['distance']
    raise Exception('no dist???')

def unfuck(adjList):
    tempL=[]
    k=0
    j=0
    for bigdict in bigList:
        for dict in adjList:
            j+=1
            for key in dict:
                for adjName in adjList[j]:
                    if adjName==bigdict['name']:continue
                    tempL+=[{'name':adjName, 'distance':getDist(adjName, bigList[k]['name'])}]
                bigdict['adjacents'] = tempL
                tempL=[]
                k+=0
            j=0
unfuck(adjList)
np.save('bigListFIN.npy', bigList) 

  


