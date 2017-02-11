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
  'database': 'img4',
  'raise_on_warnings': False,
}

"""
def init(cnx):
    cursor = cnx.cursor()
    query = 'CREATE TABLE IF NOT EXISTS `users` (uid INT, username VARCHAR(64), password VARCHAR(128), ' \
            'email VARCHAR(64))'
    cursor.execute(query)
    query = 'CREATE TABLE IF NOT EXISTS `rooms` (room VARCHAR(64), description TINYTEXT)'
    cursor.execute(query)
    cursor.close()
    cnx.commit()
"""