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
output=[]
temp={}
def getDist(name1, name2):
    for dict in distList:
        if name1 in dict and name2==dict[name1]:
            return dict['distance']
    #raise Exception('no dist???')
def unfuck(adjList):
    for map in adjList:
        tempD={}
        for key in map:
            for adjName in map[key]:
                tempD={'name':adjName,'distance':getDist(adjName,key)}
                for dict in bigList:
                    if dict['name']==key:
                        dict['adjacents']=dict.get('adjacents')+[tempD] if dict.get('adjacents')!=None else [tempD]
                        break
                
unfuck(adjList)
np.save('bigListFIN.npy', {0:bigList}) 
print(len(bigList))
  


