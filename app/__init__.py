from flask import Flask
from .configurations import Database
from .configurations import Auth
from .configurations import Configuration
from .configurations import Blueprint
from .configurations.Scheduler import Scheduler
from flask_sock import Sock


def create_app():
    app = Flask(__name__)
    
    #Configurações da plicação
    Configuration.init_app(app)
    Database.init_app(app)
    Auth.init_app(app)
    #scheduler = Scheduler()
    #scheduler.start()
    #Adicionando as rotas
    Blueprint.rotasMain(app)
    Blueprint.rotasAdm(app)
    Blueprint.rotasTec(app)
    Blueprint.rotasVig(app)
    
    return app