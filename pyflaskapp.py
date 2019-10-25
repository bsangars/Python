import flask 
from flask import Flask, render_template,jsonify, url_for
application= Flask(__name__)
import pyodbc
import sys

@application.route('/welcome')
def welcome():
    return "Welcome to the Flask app!"

tasks = [
    {'id': 1,
     'TaskName': u'Go workout',
     'description': u'Running, Strength Training, Power Cardio, Pilates, Game',
     'done': False 
    },
    {'id': 2,
     'TaskName': u'Finish Commercial',
     'description': u'Fix the Detail Row Duplicates, Sum for the Claim Totals',
     'done': True
    }
]


@application.route('/mytasks/v1/task/<int:task_id>', methods=['GET'])
def get_tasks(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) ==0:
        abort(404)
    return jsonify({'task':task[0]})

if __name__ =='__main__':
    application.run(debug=True)

