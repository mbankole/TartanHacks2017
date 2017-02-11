# database operations shit goes here

from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode

__author__ = "Bolaji Bankole"


config = {
  'user': 'jeff',
  'password': 'potato salad',
  # 'host': '10.0.0.10',
  'host': 'antel.mbankole.com',
  'database': 'places',
  'raise_on_warnings': False,
}


def get_cnx():
    """returns a connection object.
    This could use some further obfuscation for speedups"""
    print("connecting to database '" + config['database'] + "' on '" + config['host'] + "'")
    try:
        cnx = mysql.connector.connect(**config)
        print("connected")
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        exit()


def init(cnx):
    cursor = cnx.cursor()
    query = 'CREATE TABLE IF NOT EXISTS `points` (name VARCHAR(128), longitude FLOAT, latitude FLOAT)'
    cursor.execute(query)
    query = 'CREATE TABLE IF NOT EXISTS `locations` (name VARCHAR(128), longitude FLOAT, latitude FLOAT, adjacents TEXT)'
    cursor.execute(query)
    cursor.close()
    cnx.commit()


def add_location(name, lon, lat, adjacents, cnx):
    """Adds a user to the users table"""
    for i in range(len(adjacents)):
        adjacents[i] = adjacents[i]['name'] + " |-| " + str(adjacents[i]['distance'])
    # print adjacents
    adj_text = "|, ".join(adjacents)
    cursor = cnx.cursor()
    query = "DELETE FROM locations WHERE name = '{name}'".format(name = name)
    cursor.execute(query)
    query = "INSERT INTO locations VALUES ('{name}', {longtude}, {latitude}, '{adj}')".format(
        name = name,
        longtude = lon,
        latitude = lat,
        adj = adj_text
    )
    # print(query)
    cursor.execute(query)
    cursor.close()
    cnx.commit()


def get_locations(cnx):
    cursor = cnx.cursor()
    query = 'SELECT * FROM locations'
    cursor.execute(query)
    info = []
    for point in cursor:
        data = point[3]
        adjacents = data.split('|, ')
        for i in range(len(adjacents)):
            adj_data = adjacents[i].split(' |-| ')
            try:
                adjacents[i] = {
                    'name': adj_data[0],
                    'distance': float(adj_data[1])
                }
            except:
                adjacents[i] = {
                    'name': adj_data[0],

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
        data = point[3]
        adjacents = data.split('|, ')
        for i in range(len(adjacents)):
            adj_data = adjacents[i].split(' |-| ')
            adjacents[i] = {
                'name': adj_data[0],
                'distance': float(adj_data[1])
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

def add_point(name, lon, lat, cnx):
    """Adds a user to the users table"""
    cursor = cnx.cursor()
    query = "DELETE FROM points WHERE name='{name}'".format(name = name)
    print(query)
    cursor.execute(query)
    query = "INSERT INTO points VALUES ('{name}', {longtude}, {latitude})".format(
        name = name,
        longtude = lon,
        latitude = lat
    )
    # print(query)
    cursor.execute(query)
    cursor.close()
    cnx.commit()


def get_points(cnx):
    cursor = cnx.cursor()
    query = 'SELECT * FROM points'
    cursor.execute(query)
    info = []
    for point in cursor:
        data = {
            'name': point[0],
            'coords' : [point[1], point[2]],
            'elevation' : point[3]
        }
        info.append(data)
    cursor.close()
    return info


def get_point(name, cnx):
    cursor = cnx.cursor()
    query = 'SELECT * FROM points WHERE name = "{name}"'.format(name = name)
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