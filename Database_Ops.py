# database operations shit goes here

from __future__ import print_function
# import mysql.connector
# from mysql.connector import errorcode

__author__ = "Bolaji Bankole"


config = {
  'user': 'jeff',
  'password': 'potato salad',
  # 'host': '10.0.0.10',
  'host': 'antel.mbankole.com',
  'database': 'places',
  'raise_on_warnings': False,
}


def init(cnx):
    cursor = cnx.cursor()
    query = 'CREATE TABLE IF NOT EXISTS `points` (name VARCHAR(128), longitude FLOAT, latitude FLOAT)'
    cursor.execute(query)
    query = 'CREATE TABLE IF NOT EXISTS `locations` (name VARCHAR(128), longitude FLOAT, latitude FLOAT, adjacents TEXT)'
    cursor.execute(query)
    cursor.close()
    cnx.commit()


def get_locations(cnx):
    cursor = cnx.cursor()
    query = 'SELECT * FROM locations'
    cursor.execute(query)
    info = []
    for point in cursor:
        data = cursor[3]
        adjacents = data.split(', ')
        for i in range(len(adjacents)):
            adj_data = adjacents[i].split(' - ')
            adjacents[i] = {
                'name': adj_data[0],
                'distance': adj_data[1]
            }
        data = {
            'name': point[0],
            'coords' : [point[1], point[2]],
            'adjacents': adjacents
        }
        info.append(data)
    cursor.close()
    return info


def get_location(name, cnx):
    cursor = cnx.cursor()
    query = 'SELECT * FROM locations WHERE name = "{name}"'.format(name = name)
    cursor.execute(query)
    for point in cursor:
        data = cursor[3]
        adjacents = data.split(', ')
        for i in range(len(adjacents)):
            adj_data = adjacents[i].split(' - ')
            adjacents[i] = {
                'name': adj_data[0],
                'distance': adj_data[1]
            }
        data = {
            'name': point[0],
            'coords': [point[1], point[2]],
            'adjacents': adjacents
        }
        cursor.close()
        return data
    cursor.close()
    return None


def get_points(cnx):
    cursor = cnx.cursor()
    query = 'SELECT * FROM points'
    cursor.execute(query)
    info = []
    for point in cursor:
        data = {
            'name': point[0],
            'coords' : [point[1], point[2]]
        }
        info.append(data)
    cursor.close()
    return info


def get_point(name, cnx):
    cursor = cnx.cursor()
    query = 'SELECT * FROM points WHERE name="{name}"'.format(name = name)
    cursor.execute(query)
    info = []
    for point in cursor:
        data = {
            'name': point[0],
            'coords' : [point[1], point[2]]
        }
        cursor.close()
        return data
    cursor.close()
    return None