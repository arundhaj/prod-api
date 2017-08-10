import json
import logging
import sys

from chalice import Chalice

from chalicelib import service
from chalicelib.helpers import DateTimeEncoder


app = Chalice(app_name='prod-api')
app.debug = True

logger = logging.getLogger()
logger.setLevel(logging.INFO)


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/task', methods=['GET', 'POST'], cors=True)
def get_task():
    request = app.current_request
    
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        resp = service.get_all_tasks()
    
        try:
            json_resp = json.dumps(resp, cls=DateTimeEncoder)
        except:
            logger.log(sys.exc_info())
    
        return json_resp