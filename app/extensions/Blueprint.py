
#Adicionando as rotas principais 
def rotasMain(app):
    from ..routes.Autenticacao import autenticacao
    app.register_blueprint(autenticacao)
    
    from ..routes.Index import index
    app.register_blueprint(index)

    from ..routes.Filtros import filtros
    app.register_blueprint(filtros)


#Adicionando as rotas relcionadas ao Administrador
def rotasAdm(app):
    #Rota para a DashBoard do Administrador
    from ..routes.administrador.Dashboard import dashAdm
    app.register_blueprint(dashAdm)
    #Rota relacionadas ao usuários do sistema
    from ..routes.administrador.Usuarios import usuarioAdm
    app.register_blueprint(usuarioAdm)


#Adicionando as rotas relcionadas ao Tec. de Segurança
def rotasTec(app):
    #Rota para a DashBoard do Tec. de Segurança
    from ..routes.tecSeguranca.Dashboard import dashTec
    app.register_blueprint(dashTec)


#Adicionando as rotas relcionadas ao Vigilante
def rotasVig(app):
    #Rota para a DashBoard do igilante
    from ..routes.vigilante.Dashboard import dashVig
    app.register_blueprint(dashVig)