import Database_Ops, numpy as np
bigList = np.load('bigListFIN.npy').item()[0]
#print(bigList)
def update():
    cnx = Database_Ops.get_cnx()
    Database_Ops.init(cnx)
    for dict in bigList:
        Database_Ops.add_location(dict['name'],dict['coords'][0],
            dict['coords'][1],dict['adjacents'],cnx)
update()