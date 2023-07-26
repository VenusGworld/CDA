
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
    from ..routes.vigAdm.Dashboard import dashVigBlue
    app.register_blueprint(dashVigBlue, url_prefix="/admin", name="dashAdmBlue")

    #Rota relacionadas ao CRUD Usuários
    from ..routes.administrador.Usuarios import usuarioAdmBlue
    app.register_blueprint(usuarioAdmBlue, url_prefix="/admin")

    #Rota relacionadas ao CRUD de Funcionários
    from ..routes.administrador.Funcionarios import funcionarioAdmBlue
    app.register_blueprint(funcionarioAdmBlue, url_prefix="/admin")

    #Rotas relacionadas ao controle de Chaves com usuário admin
    from ..routes.vigAdm.ControleChave import controleChaveVigcBlue
    app.register_blueprint(controleChaveVigcBlue, url_prefix="/admin", name="controleChaveAdmcBlue")

    #Rotas relaciondas ao CRUD de Chave com usuário admin
    from ..routes.vigAdm.Chaves import chaveVigBlue
    app.register_blueprint(chaveVigBlue, url_prefix="/admin", name="chaveAdmBlue")

    #Rotas relaciondas ao log de Usuários
    from ..routes.administrador.LogManterUsuario import logUserAdmBlue
    app.register_blueprint(logUserAdmBlue, url_prefix="/admin")



#Adicionando as rotas relcionadas ao Tec. de Segurança
def rotasTec(app):
    #Rota para a DashBoard do Tec. de Segurança
    from ..routes.tecSeguranca.Dashboard import dashTecBlue
    app.register_blueprint(dashTecBlue, url_prefix="/tec")



#Adicionando as rotas relcionadas ao Vigilante
def rotasVig(app):
    #Rota para a DashBoard do Vigilante
    from ..routes.vigAdm.Dashboard import dashVigBlue
    app.register_blueprint(dashVigBlue, url_prefix="/vig")

    #Rotas relacionadas ao controle de Chaves com usuário vig
    from ..routes.vigAdm.ControleChave import controleChaveVigcBlue
    app.register_blueprint(controleChaveVigcBlue, url_prefix="/vig")

    #Rotas relaciondas ao CRUD de Chave com usuário vig
    from ..routes.vigAdm.Chaves import chaveVigBlue
    app.register_blueprint(chaveVigBlue, url_prefix="/vig")