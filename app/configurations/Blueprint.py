
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

    from ..routes.public.Relatorio import relatorioBlue
    app.register_blueprint(relatorioBlue)

    from ..routes.public.Parametros import parametrosBlue
    app.register_blueprint(parametrosBlue)



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
    from ..routes.vigAdm.ControleChave import controleChaveVigBlue
    app.register_blueprint(controleChaveVigBlue, url_prefix="/admin", name="controleChaveAdmBlue")

    #Rotas relaciondas ao CRUD de Chave com usuário admin
    from ..routes.vigAdm.Chave import chaveVigBlue
    app.register_blueprint(chaveVigBlue, url_prefix="/admin", name="chaveAdmBlue")

    #Rotas relaciondas ao log de Usuários
    from ..routes.administrador.LogManterUsuario import logUserAdmBlue
    app.register_blueprint(logUserAdmBlue, url_prefix="/admin")

    #Rotas relacionadas ao CRUD de terceiros com usuário admin
    from ..routes.vigAdm.Terceiro import terceiroVigBlue
    app.register_blueprint(terceiroVigBlue, url_prefix="/admin", name="terceiroAdmBlue")

    #Rotas relacionadas ao controle de Terceiros com usuário admin
    from ..routes.vigAdm.ControleTerceiro import controleTercVigBlue
    app.register_blueprint(controleTercVigBlue, url_prefix="/admin", name="controleTercAdmBlue")

    #Rotas relacionadas ao controle de Gerenetes com usuário admin
    from ..routes.vigAdm.ControleGerente import controleGerVigBlue
    app.register_blueprint(controleGerVigBlue, url_prefix="/admin", name="controleGerAdmBlue")

    #Rotas recionadas ao enviar mensagem
    from ..routes.administrador.Mensagem import mensagemAdmBlue
    app.register_blueprint(mensagemAdmBlue, url_prefix="/admin")

    #Rotas relaciondas ao log de Funcionário
    from ..routes.administrador.LogManterFunc import logFuncAdmBlue
    app.register_blueprint(logFuncAdmBlue, url_prefix="/admin")

    #Rotas relaciondas ao log de Funcionário
    from ..routes.administrador.LogMensagem import logMenAdmBlue
    app.register_blueprint(logMenAdmBlue, url_prefix="/admin")

    #Rota para os logs do manter Chave com usuário admin
    from ..routes.tecAdm.LogManterChave import logChavTecBlue
    app.register_blueprint(logChavTecBlue, url_prefix="/admin", name="logChavAdmBlue")

    #Rota para os logs do manter Terceiro com usuário tec
    from ..routes.tecAdm.LogManterTerceiro import logTercTecBlue
    app.register_blueprint(logTercTecBlue, url_prefix="/admin", name="logTercAdmBlue")



#Adicionando as rotas relcionadas ao Tec. de Segurança
def rotasTec(app):
    #Rota para a DashBoard do Tec. de Segurança
    from ..routes.tecSeguranca.Dashboard import dashTecBlue
    app.register_blueprint(dashTecBlue, url_prefix="/tec")

    #Rota para os logs do manter Chave com usuário tec
    from ..routes.tecAdm.LogManterChave import logChavTecBlue
    app.register_blueprint(logChavTecBlue, url_prefix="/tec")

    #Rota para os logs do manter Terceiro com usuário tec
    from ..routes.tecAdm.LogManterTerceiro import logTercTecBlue
    app.register_blueprint(logTercTecBlue, url_prefix="/tec")



#Adicionando as rotas relcionadas ao Vigilante
def rotasVig(app):
    #Rota para a DashBoard do Vigilante
    from ..routes.vigAdm.Dashboard import dashVigBlue
    app.register_blueprint(dashVigBlue, url_prefix="/vig")

    #Rotas relacionadas ao controle de Chaves com usuário vig
    from ..routes.vigAdm.ControleChave import controleChaveVigBlue
    app.register_blueprint(controleChaveVigBlue, url_prefix="/vig")

    #Rotas relacionadas ao CRUD de Chave com usuário vig
    from ..routes.vigAdm.Chave import chaveVigBlue
    app.register_blueprint(chaveVigBlue, url_prefix="/vig")

    #Rotas relacionadas ao CRUD de terceiros com usuário vig
    from ..routes.vigAdm.Terceiro import terceiroVigBlue
    app.register_blueprint(terceiroVigBlue, url_prefix="/vig")

    #Rotas relacionadas ao controle de Terceiros com usuário vig
    from ..routes.vigAdm.ControleTerceiro import controleTercVigBlue
    app.register_blueprint(controleTercVigBlue, url_prefix="/vig")

    #Rotas relacionadas ao controle de Gerenetes com usuário vig
    from ..routes.vigAdm.ControleGerente import controleGerVigBlue
    app.register_blueprint(controleGerVigBlue, url_prefix="/vig")