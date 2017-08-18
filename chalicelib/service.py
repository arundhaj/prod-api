from chalicelib.models import Task, TaskProject, TaskCategory, TaskStatus, TaskGoal
#from playhouse.shortcuts import model_to_dict, dict_to_model

def get_all_projects():
    projects = TaskProject.select()
    
    resp = list()
    
    for project in projects:
        project_dict = dict()
        
        project_dict['id'] = project.id
        project_dict['name'] = project.name
        project_dict['description'] = project.description
        
        resp.append(project_dict)
        
    return resp


def get_all_categories():
    categories = TaskCategory.select()
    
    resp = list()
    
    for category in categories:
        category_dict = dict()
        
        category_dict['id'] = category.id
        category_dict['name'] = category.name
        category_dict['description'] = category.description
        
        resp.append(category_dict)
        
    return resp


def get_all_statuses():
    statuses = TaskStatus.select()
    
    resp = list()
    
    for status in statuses:
        status_dict = dict()
        
        status_dict['id'] = status.id
        status_dict['name'] = status.name
        status_dict['description'] = status.description
        
        resp.append(status_dict)
        
    return resp


def get_all_goals():
    goals = TaskGoal().select()
    
    resp = list()
    
    for goal in goals:
        goal_dict = dict()
        
        goal_dict['id'] = goal.id
        goal_dict['name'] = goal.name
        goal_dict['description'] = goal.description
        
        resp.append(goal_dict)
        
    return resp


def get_all_tasks():
    tasks = Task.select()

    resp = list()

    for task in tasks:
        task_dict = dict()
        task_dict['id'] = task.id
        task_dict['assign_date'] = task.assign_date
        task_dict['assigned_by'] = task.assigned_by
        task_dict['project_id'] = task.project.id
        task_dict['project'] = task.project.name
        task_dict['take_action'] = task.take_action
        task_dict['assigned_to'] = task.assigned_to
        task_dict['category_id'] = task.category.id
        task_dict['category'] = task.category.name
        task_dict['status_id'] = task.status.id
        task_dict['status'] = task.status.name
        task_dict['edoc'] = task.edoc
        task_dict['doc'] = task.doc
        task_dict['goal_id'] = task.goal.id
        task_dict['goal'] = task.goal.name
        task_dict['action_taken'] = task.action_taken
        task_dict['assumption'] = task.assumption
        # task_dict = model_to_dict(task, recurse=False)
        resp.append(task_dict)
    
    return resp


def get_task(task_id):
    task = Task.select().where(Task.id == task_id).get()
    
    task_dict = dict()
    task_dict['id'] = task.id
    task_dict['assign_date'] = task.assign_date
    task_dict['assigned_by'] = task.assigned_by
    task_dict['project_id'] = task.project.id
    task_dict['project'] = task.project.name
    task_dict['take_action'] = task.take_action
    task_dict['assigned_to'] = task.assigned_to
    task_dict['category_id'] = task.category.id
    task_dict['category'] = task.category.name
    task_dict['status_id'] = task.status.id
    task_dict['status'] = task.status.name
    task_dict['edoc'] = task.edoc
    task_dict['doc'] = task.doc
    task_dict['goal_id'] = task.goal.id
    task_dict['goal'] = task.goal.name
    task_dict['action_taken'] = task.action_taken
    task_dict['assumption'] = task.assumption
    
    return task_dict


def add_task():
    pass
