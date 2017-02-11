#  Actual webserver shit here
from __future__ import print_function
import flask
import Database_Ops
import Djikstra_Ops
from flask import render_template
from flask import send_from_directory

app = flask.Flask(__name__)
app.secret_key = 'such sekret'

icnx = Database_Ops.get_cnx()
Database_Ops.init(icnx)
icnx.close()

#def hello():
#    list = ["a", "b", "c"]
#    return render_template("whateveryouwant.html", list = list)

@app.route("/copy")
def copy():
    return render_template("COPY.html")

@app.route("/")
def main():
    return render_template("general.html")

@app.route("/map", methods=['GET', 'POST'])
def map():
    points = []
    if flask.request.method == 'GET':

        return render_template("map.html", points = points)
    print("got something")
    start = flask.request.form['start']
    end = flask.request.form['end']
    print("Path requested from " + start + " to " + end)
    cnx = Database_Ops.get_cnx()
    path = Djikstra_Ops.find_paths(start, end, cnx)
    print(path)
    length = path[0]
    path_nodes = path[1:len(path)]
    for node in path_nodes:
        ndata = Database_Ops.get_location(node, cnx)
        points.append({'longitude':ndata['coords'][0], 'latitude':ndata['coords'][1]})
    print(points)
    return render_template("map.html", points = points)

if __name__ == '__main__':
    app.run(host="0.0.0.0")