from bottle import request
from models.activity import ActivityModel, Activity

class ActivityService:
    def __init__(self):
        self.activity_model = ActivityModel()

    def get_all(self):
        return self.activity_model.get_all()

    def save(self):
        last_id = max([a.id for a in self.activity_model.get_all()], default=0)
        new_id = last_id + 1
        name = request.forms.get('name')
        description = request.forms.get('description')
        done = request.forms.get('done') == 'on'
        activity = Activity(new_id, name, description, done)
        self.activity_model.add(activity)

    def get_by_id(self, activity_id):
        return self.activity_model.get_by_id(activity_id)

    def edit(self, activity):
        activity.name = request.forms.get('name')
        activity.description = request.forms.get('description')
        activity.done = request.forms.get('done') == 'on'
        self.activity_model.update(activity)

    def delete(self, activity_id):
        self.activity_model.delete(activity_id)