from bottle import Bottle
from .base_controller import BaseController
from models.animal import Animal, AnimalModel

class AnimalController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.setup_routes()
        self.animal_model = AnimalModel()
    

    def setup_routes(self):
        self.app.route('/animal', method=['GET'], callback=self.list_animals)

    
    def list_animals(self):
        animals = self.animal_model.get_all_animals()
        print(animals)
        
        print("--> Navegador tentando acessar a rota '/animal' com Metodo GET")
        return self.render('animal', animals=animals)


animal_route = Bottle()
animal_controller = AnimalController(animal_route)