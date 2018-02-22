#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/html/faithinnothing.me/pathfindr/")

from pathfindr import app as application
application.secret_key = 'Add your secret key'


activate_this = '/var/www/html/faithinnothing.me/pathfindr/pathfindr/venv/bin/activate_this.py'
with open(activate_this) as file_:
        exec(file_.read(), dict(__file__=activate_this))


