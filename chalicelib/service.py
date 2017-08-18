from chalicelib.models import Task, TaskProject, TaskCategory, TaskStatus, TaskGoal
#from playhouse.shortcuts import model_to_dict, dict_to_model

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
