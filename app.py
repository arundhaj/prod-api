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
def get_tasks():
    request = app.current_request
    
    if request.method == 'GET':
        resp = service.get_all_tasks()
    
        try:
            json_resp = json.dumps(resp, cls=DateTimeEncoder)
        except:
            logger.log(sys.exc_info())
    
        return json_resp
    elif request.method == 'POST':
        pass

    
@app.route('/task/{task_id}', methods=['GET', 'PUT'], cors=True)
def get_task(task_id):
    request = app.current_request
    
    if request.method == 'GET':
        resp = service.get_task(task_id)
        json_resp = json.dumps(resp, cls=DateTimeEncoder)
        
        return json_resp
    elif request.method == 'PUT':
        pass
    
