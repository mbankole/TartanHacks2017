#  Actual webserver shit here
from __future__ import print_function
import flask
import Database_Ops
from flask import render_template
from flask import send_from_directory

app = flask.Flask(__name__)
app.secret_key = 'such sekret'

icnx = Database_Ops.get_cnx()
Database_Ops.init(icnx)
icnx.close()


@app.route("/")
def main():
    return "HELLLELELELEELELELE"


if __name__ == '__main__':
    app.run()