import Database_Ops
import Djikstra_Ops

# import cmu_course_api

#data = cmu_course_api.get_course_data('S')
#print(data)
cnx = Database_Ops.get_cnx()
#Database_Ops.init(cnx)
"""
Database_Ops.add_location("p1", 335235, 232522.2, [
        {
            'name':'p2',
            'distance':1,
        },
        {
            'name':'p4',
            'distance':1,
        }],cnx)
Database_Ops.add_location("p2", 335235, 232522.2, [
        {
            'name':'p1',
            'distance':1,
        },
        {
            'name':'p5',
            'distance':2,
        },
        {
            'name':'p3',
            'distance':1,
        },
        ],cnx)
Database_Ops.add_location("p3", 335235, 232522.2, [
        {
            'name':'p2',
            'distance':1,
        },
        {
            'name':'p6',
            'distance':1,
        },
        ],cnx)
Database_Ops.add_location("p4", 335235, 232522.2, [
        {
            'name':'p1',
            'distance':1,
        },
        {
            'name':'p7',
            'distance':1,
        },
        {
            'name':'p5',
            'distance':1,
        },
        ],cnx)
Database_Ops.add_location("p5", 335235, 232522.2, [
        {
            'name':'p2',
            'distance':2,
        },
        {
            'name':'p6',
            'distance':3,
        },
        {
            'name':'p8',
            'distance':1,
        },
        {
            'name':'p4',
            'distance':1,
        },
        ],cnx)
Database_Ops.add_location("p6", 335235, 232522.2, [
        {
            'name':'p3',
            'distance':1,
        },
        {
            'name':'p5',
            'distance':3,
        },
        {
            'name':'p9',
            'distance':7,
        },
        ],cnx)
Database_Ops.add_location("p7", 335235, 232522.2, [
        {
            'name':'p4',
            'distance':1,
        },
        {
            'name':'p8',
            'distance':1,
        },
        ],cnx)
Database_Ops.add_location("p8", 335235, 232522.2, [
        {
            'name':'p5',
            'distance':1,
        },
        {
            'name':'p7',
            'distance':1,
        },
        {
            'name':'p9',
            'distance':1,
        },
        ],cnx)
Database_Ops.add_location("p9", 335235, 232522.2, [
        {
            'name':'p8',
            'distance':1,
        },
        {
            'name':'p6',
            'distance':7,
        },
        ],cnx)"""
#print(Database_Ops.get_location('p5',cnx))
#print(Database_Ops.get_locations(cnx))
path = Djikstra_Ops.find_paths('WEAN S (q)','RESNIK E', cnx)
print(path)
#print(Database_Ops.get_location("WIEGAND", cnx))
#print(len(Database_Ops.get_location("WIEGAND", cnx)['adjacents']))