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


@app.route('/project', methods=['GET', 'POST'], cors=True)
def projects():
    request = app.current_request
    
    if request.method == 'GET':
        resp = service.get_all_projects()
    
        try:
            json_resp = json.dumps(resp)
        except:
            logger.log(sys.exc_info())
    
        return json_resp
    elif request.method == 'POST':
        pass


@app.route('/category', methods=['GET', 'POST'], cors=True)
def categories():
    request = app.current_request
    
    if request.method == 'GET':
        resp = service.get_all_categories()
    
        try:
            json_resp = json.dumps(resp)
        except:
            logger.log(sys.exc_info())
    
        return json_resp
    elif request.method == 'POST':
        pass


@app.route('/goal', methods=['GET', 'POST'], cors=True)
def goals():
    request = app.current_request
    
    if request.method == 'GET':
        resp = service.get_all_goals()
    
        try:
            json_resp = json.dumps(resp)
        except:
            logger.log(sys.exc_info())
    
        return json_resp
    elif request.method == 'POST':
        pass


@app.route('/status', methods=['GET', 'POST'], cors=True)
def statuses():
    request = app.current_request
    
    if request.method == 'GET':
        resp = service.get_all_statuses()
    
        try:
            json_resp = json.dumps(resp)
        except:
            logger.log(sys.exc_info())
    
        return json_resp
    elif request.method == 'POST':
        pass


@app.route('/task', methods=['GET', 'POST'], cors=True)
def tasks():
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
def task(task_id):
    request = app.current_request
    
    if request.method == 'GET':
        resp = service.get_task(task_id)
        json_resp = json.dumps(resp, cls=DateTimeEncoder)
        
        return json_resp
    elif request.method == 'PUT':
        pass
    
