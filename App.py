#  Actual webserver shit here
from __future__ import print_function
import flask
import Database_Ops
import Djikstra_Ops
from flask import render_template
from flask import send_from_directory
from flask_socketio import emit, join_room, leave_room
from flask_socketio import SocketIO


from flask import Flask, session
from flask.sessions import SessionInterface
from beaker.middleware import SessionMiddleware

session_opts = {
    'session.type': 'ext:memcached',
    'session.url': '127.0.0.1:11211',
    'session.data_dir': './cache',
}

class BeakerSessionInterface(SessionInterface):
    def open_session(self, app, request):
        session = request.environ['beaker.session']
        return session

    def save_session(self, app, session, response):
        session.save()


app = flask.Flask(__name__)
app.secret_key = 'such sekret'
socketio = SocketIO(app)

icnx = Database_Ops.get_cnx()
Database_Ops.init(icnx)
icnx.close()

#def hello():
#    list = ["a", "b", "c"]
#    return render_template("whateveryouwant.html", list = list)

@app.route("/copy")
def copy():
    return render_template("COPY.html")

@app.route("/",  methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return render_template("general.html")
    # print(flask.request.form)
    keys = flask.request.form.keys()
    bkeys = []
    rkeys = []
    for key in keys:
        if key[0] == 'b':
            bkeys.append(key)
        if key[0] == 'r':
            rkeys.append(key)
    buildings = []
    bkeys.sort()
    for bkey in bkeys:
        buildings.append(flask.request.form[bkey])
    print(buildings)
    path =[]
    cnx = Database_Ops.get_cnx()
    for i in range(len(buildings) - 1):
        start = buildings[i]
        end = buildings[i+1]
        # print("pathing from " + start + " to " + end)
        path += (Djikstra_Ops.find_paths(start, end, cnx)[1:-1])
    # print(path)
    session['route'] = path
    return flask.redirect(flask.url_for('map'))

@app.route("/map")
def map():
    points = []
    cnx = Database_Ops.get_cnx()
    path = session['route']
    print(path)
    length = path[0]
    path_nodes = path
    for node in path_nodes:
        ndata = Database_Ops.get_location(node, cnx)
        points.append({'longitude':ndata['coords'][0], 'latitude':ndata['coords'][1]})
    #print(points)
    return render_template("map.html", points = points)


@app.route("/test", methods=['GET', 'POST'])
def test():
    points = []
    if flask.request.method == 'GET':
        return render_template("map.html", points = points)
    print("got something")
    start = flask.request.form['start'].strip()
    end = flask.request.form['end'].strip()
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
    return render_template("test.html", points = points)





if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0")