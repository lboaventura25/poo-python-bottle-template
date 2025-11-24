from bottle import Bottle
from controllers.user_controller import user_routes
from controllers.activity_controller import activity_routes
from controllers.animal_controller import animal_route

def init_controllers(app: Bottle):
    app.merge(user_routes)
    app.merge(activity_routes)
    app.merge(animal_route)
