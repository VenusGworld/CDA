
#Adicionando as rotas principais 
def rotasMain(app):
    from ..routes.Autenticacao import autenticacaoBlue
    app.register_blueprint(autenticacaoBlue)
    
    from ..routes.Index import indexBlue
    app.register_blueprint(indexBlue)

    from ..routes.Filtros import filtrosBlue
    app.register_blueprint(filtrosBlue)

    from ..routes.EsqueciSenha import esqueciSenhaBlue
    app.register_blueprint(esqueciSenhaBlue)


#Adicionando as rotas relcionadas ao Administrador
def rotasAdm(app):
    #Rota para a DashBoard do Administrador
    from ..routes.administrador.Dashboard import dashAdmBlue
    app.register_blueprint(dashAdmBlue)
    #Rota relacionadas ao usuários do sistema
    from ..routes.administrador.Usuarios import usuarioAdmBlue
    app.register_blueprint(usuarioAdmBlue)


#Adicionando as rotas relcionadas ao Tec. de Segurança
def rotasTec(app):
    #Rota para a DashBoard do Tec. de Segurança
    from ..routes.tecSeguranca.Dashboard import dashTecBlue
    app.register_blueprint(dashTecBlue)


#Adicionando as rotas relcionadas ao Vigilante
def rotasVig(app):
    #Rota para a DashBoard do Vigilante
    from ..routes.vigilante.Dashboard import dashVigBlue
    app.register_blueprint(dashVigBlue)