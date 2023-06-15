from flask import Flask, session
from .extensions import Database
from .extensions import Auth
from .extensions import Configuration
from flask_sock import Sock
import os
import urllib


def create_app():
    app = Flask(__name__)
    
    #Configurações da plicação
    #basedir = os.path.abspath(os.path.dirname(__file__))
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'Port.db')
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #app.config["SECRET_KEY"] = 'pbkdf2:sha256:260000$9C1lotTLZookpgaC$cd1fb937818bee2ec8c5a8a1f8e7f3b40c49ddd452a63ca1bec553c2d03724da'
    #app.config['SOCK_SERVER_OPTIONS'] = {'ping_interval': 1}
    Configuration.init_app(app)
    Database.init_app(app)
    Auth.init_app(app)
    
    from .routes.Autenticacao import autenticacao
    app.register_blueprint(autenticacao)
    
    from .routes.Index import index
    app.register_blueprint(index)
    
    routesAdm(app)

    routesTec(app)

    routesVig(app)

    return app
    
#Adicionando as rotas relcionadas ao Administrador
def routesAdm(app):
    #Rota para a DashBoard do Administrador
    from .routes.administrador.Dashboard import dashAdm
    app.register_blueprint(dashAdm)
    #Rota relacionadas ao usuários do sistema
    from .routes.administrador.Usuarios import usuarioAdm
    app.register_blueprint(usuarioAdm)

#Adicionando as rotas relcionadas ao Tec. de Segurança
def routesTec(app):
    #Rota para a DashBoard do Tec. de Segurança
    from .routes.tecSeguranca.Dashboard import dashTec
    app.register_blueprint(dashTec)

#Adicionando as rotas relcionadas ao Vigilante
def routesVig(app):
    #Rota para a DashBoard do igilante
    from .routes.vigilante.Dashboard import dashVig
    app.register_blueprint(dashVig)