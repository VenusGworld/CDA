from flask import Flask
from .extensions import Database
from .extensions import Auth
from .extensions import Configuration
from .extensions import Blueprint
from flask_sock import Sock


def create_app():
    app = Flask(__name__)
    
    #Configurações da plicação
    Configuration.init_app(app)
    Database.init_app(app)
    Auth.init_app(app)
    #Adicionando as rotas
    Blueprint.rotasMain(app)
    Blueprint.rotasAdm(app)
    Blueprint.rotasTec(app)
    Blueprint.rotasVig(app)
    
    return app