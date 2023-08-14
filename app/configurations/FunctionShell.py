from flask import Blueprint

functionShellBlue = Blueprint('functionShellBlue', __name__)

def criarBanco():
    from app.models import Tables 
    from app import create_app
    from app.configurations.Database import DB

    DB.create_all()


def apagarBanco():
    from app.models import Tables 
    from app import create_app
    from app.configurations.Database import DB

    DB.drop_all()


@functionShellBlue.app_context_processor
def criaBanco():
    return dict(criarBanco=criarBanco())


@functionShellBlue.app_context_processor
def apagaBanco():
    return {'apagarBanco': apagarBanco}