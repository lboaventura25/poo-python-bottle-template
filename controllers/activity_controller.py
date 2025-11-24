from bottle import Bottle, request
from .base_controller import BaseController
from services.activity_service import ActivityService

class ActivityController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.activity_service = ActivityService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/activities', method='GET', callback=self.list_activities)
        self.app.route('/activities/add', method=['GET', 'POST'], callback=self.add_activity)
        self.app.route('/activities/edit/<activity_id:int>', method=['GET', 'POST'], callback=self.edit_activity)
        self.app.route('/activities/delete/<activity_id:int>', method='POST', callback=self.delete_activity)

    def list_activities(self):
        activities = self.activity_service.get_all()
        return self.render('activities', activities=activities)

    def add_activity(self):
        if request.method == 'GET':
            return self.render('activity_form', activity=None, action='/activities/add')
        else:
            self.activity_service.save()
            self.redirect('/activities')

    def edit_activity(self, activity_id):
        activity = self.activity_service.get_by_id(activity_id)
        if request.method == 'GET':
            return self.render('activity_form', activity=activity, action=f'/activities/edit/{activity_id}')
        else:
            self.activity_service.edit(activity)
            self.redirect('/activities')

    def delete_activity(self, activity_id):
        self.activity_service.delete(activity_id)
        self.redirect('/activities')

activity_routes = Bottle()
activity_controller = ActivityController(activity_routes)