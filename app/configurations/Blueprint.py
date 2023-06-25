
#Adicionando as rotas principais 
def rotasMain(app):
    from ..routes.public.Autenticacao import autenticacaoBlue
    app.register_blueprint(autenticacaoBlue)
    
    from ..routes.public.Index import indexBlue
    app.register_blueprint(indexBlue)

    from ..routes.public.Filtros import filtrosBlue
    app.register_blueprint(filtrosBlue)

    from ..routes.public.EsqueciSenha import esqueciSenhaBlue
    app.register_blueprint(esqueciSenhaBlue)

    from ..routes.public.Pesquisa import pesquisaBlue
    app.register_blueprint(pesquisaBlue)

    from ..routes.public.PreencheTabelas import preencheTabelasBlue
    app.register_blueprint(preencheTabelasBlue)

    from ..routes.public.Erros import errosBlue
    app.register_blueprint(errosBlue)


#Adicionando as rotas relcionadas ao Administrador
def rotasAdm(app):
    #Rota para a DashBoard do Administrador
    from ..routes.administrador.Dashboard import dashAdmBlue
    app.register_blueprint(dashAdmBlue, url_prefix="/admin")
    #Rota relacionadas ao usuários do sistema
    from ..routes.administrador.Usuarios import usuarioAdmBlue
    app.register_blueprint(usuarioAdmBlue, url_prefix="/admin")
    #Rota relacionadas ao Funcionários do sistema
    from ..routes.administrador.Funcionarios import funcionarioAdmBlue
    app.register_blueprint(funcionarioAdmBlue, url_prefix="/admin")
    #Rotas para o controle de Chaves
    from ..routes.vigAdm.ControleChave import controleChaveVigcBlue
    app.register_blueprint(controleChaveVigcBlue, url_prefix="/admin", name="controleChaveAdmcBlue")


#Adicionando as rotas relcionadas ao Tec. de Segurança
def rotasTec(app):
    #Rota para a DashBoard do Tec. de Segurança
    from ..routes.tecSeguranca.Dashboard import dashTecBlue
    app.register_blueprint(dashTecBlue, url_prefix="/tec")


#Adicionando as rotas relcionadas ao Vigilante
def rotasVig(app):
    #Rota para a DashBoard do Vigilante
    from ..routes.vigilante.Dashboard import dashVigBlue
    app.register_blueprint(dashVigBlue, url_prefix="/vig")

    #Rotas para o controle de Chaves
    from ..routes.vigAdm.ControleChave import controleChaveVigcBlue
    app.register_blueprint(controleChaveVigcBlue, url_prefix="/vig")