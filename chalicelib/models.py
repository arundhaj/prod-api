import os
from peewee import MySQLDatabase, Model, CharField, ForeignKeyField, DateTimeField, TextField


db = MySQLDatabase(os.environ.get('DB_NAME'), user=os.environ.get('DB_USERNAME'), password=os.environ.get('DB_PASSWORD'),
                    host=os.environ.get('DB_HOST'))


class BaseModel(Model):
    class Meta:
        database = db


# class ExpenseCategory(BaseModel):
#     name = CharField()
#     description = CharField()
#
#
# class Expense(BaseModel):
#     description = CharField()
#     amount = CharField()
#     date = DateTimeField()
#     category = ForeignKeyField(ExpenseCategory, related_name='expenses')


class TaskProject(BaseModel):
    name = CharField()
    description = CharField()


class TaskCategory(BaseModel):
    name = CharField()
    description = CharField()


class TaskStatus(BaseModel):
    name = CharField()
    description = CharField()


class TaskGoal(BaseModel):
    name = CharField()
    description = CharField()


class Task(BaseModel):
    assign_date = DateTimeField()
    assigned_by = CharField()
    project = ForeignKeyField(TaskProject, related_name='tasks')
    take_action = TextField()
    assigned_to = CharField()
    category = ForeignKeyField(TaskCategory, related_name='tasks')
    status = ForeignKeyField(TaskStatus, related_name='tasks')
    edoc = DateTimeField()
    doc = DateTimeField()
    goal = ForeignKeyField(TaskGoal, related_name='tasks')
    action_taken = TextField()
    assumption = TextField()


# ExpenseCategory.create_table(True)
# Expense.create_table(True)

try:
    db.connect()
    TaskProject.create_table(True)
    TaskCategory.create_table(True)
    TaskStatus.create_table(True)
    TaskGoal.create_table(True)
    Task.create_table(True)
except:
    pass