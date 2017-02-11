import numpy as np, math
import numpy as np
import Database_Ops
import copy


def find_location(locations, name):
    for i in range(len(locations)):
        if locations[i]['name'].lower() == name.lower():
            return i
    return None


def find_paths(start_name, end_name, cnx):
    #takes in starting node, end node
    print("path requested from " + start_name + " to " + end_name)
    locations = Database_Ops.get_locations(cnx)
    start = locations[find_location(locations, start_name)]
    paths = []
    good_paths = []
    for adj in start['adjacents']:
        paths.append([adj['distance'], start_name, adj['name']])
    new_paths = paths
    #while finding:

    for i in range(10):
        old_paths = copy.deepcopy(new_paths)
        new_paths = []
        dones = 0
        for path in old_paths[:]:
            # print(path)
            last = path[-1]
            if last == 'done':
                dones += 1
                if dones > 1:
                    min_length = 2353252532532
                    index = 0
                    for i in range(1, len(good_paths)):
                        if good_paths[i][0] < min_length:
                            min_length = good_paths[i][0]
                            index = i
                    good_paths[index].pop()
                    return good_paths[index]
            else:
                lastl = locations[find_location(locations, last)]
                for adj in lastl['adjacents']:
                    if adj['name'] not in path:
                        new_path = copy.deepcopy(path)
                        new_path[0] += adj['distance']
                        new_path.append(adj['name'])
                        if adj['name'].lower() == end_name.lower():
                            new_path.append("done")
                            good_paths.append(new_path)
                        new_paths.append(new_path)

    min_length = 329532855395
    index = -1
    for i in range(1, len(good_paths)):
        if good_paths[i][0] < min_length:
            min_length = good_paths[i][0]
            index = i
    if index == -1:
        return None
    good_paths[index].pop()
    return good_paths[index]



  



