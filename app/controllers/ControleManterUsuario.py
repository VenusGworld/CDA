from ..models.entity.Usuario import Usuario
from ..models.entity.Log import Log
from ..models.dao.ManterUsuarioDao import ManterUsuarioDao
from ..models.dao.ConsultaIdsDao import ConsultaIds
from ..models.dao.GeraLogUsuarioDao import GeraLogUsuarioDao
from ..models.dao.VerificamovimentoDao import VerificaMovimentoDao
from datetime import datetime
from flask import session

"""
Classe Controller para o CRUD do usuário
@author - Fabio
@version - 1.0
@since - 23/05/2023
"""

class ControleManterUsuario:

    def mostarUsuarios(self) -> list:
        #########################################################################################
        # Essa função recupera os dados dos usuários de um objeto "ManterUsuarioDao" e cria uma 
        # lista de dicionários, onde cada dicionário representa um usuário e contém seu ID, nome, 
        # nome de usuário e grupo.
        
        # PARAMETROS:
        #   Não tem parametros.
        
        # RETORNOS:
        #   return listaDados = Retorna uma lista com dicinário dos usuário que retornaram do banco.
        #########################################################################################
        
        manterUsuarioDao = ManterUsuarioDao()
        usuarios = manterUsuarioDao.mostarUsuarios()
        listaDados = []
        for usuario in usuarios:
            dicUser = {
                "id": usuario.get_id(),
                "nome": usuario.get_nome(),
                "usuario": usuario.get_usuario(),
                "grupo": usuario.get_grupo(),
            }

            listaDados.append(dicUser)

        return listaDados
    

    def mostarUsuarioDetalhado(self, id: int) -> Usuario:
        #########################################################################################
        # Essa função recebe um ID como entarda e utiliza-o para buscar informações detalhadas
        # sobre um usuário específico a partir de um objeto "ManterUsuarioDao".
        
        # PARAMETROS:
        #   id = ID do usuário que foi slecionado.
        
        # RETORNOS:
        #   return usuario = Retorna as informações detalhadas do usuário solicitado.
        #########################################################################################

        manterUsuarioDao = ManterUsuarioDao()
        usuario = manterUsuarioDao.mostarUsuarioDetalhado(id)
        
        return usuario

    
    def incluirUsuario(self, nome: str, user: str, email: str, grupo: str, senha: str) -> bool:
        #########################################################################################
        # Essa função recebe os dados do usuário a ser incluido.
        
        # PARAMETROS:
        #   nome = Nome do usuário informado no form de cadastro;
        #   user = Username do usuário informado no form de cadastro;
        #   email = E-mail do usuário informado no form de cadastro;
        #   grupo = Grupo do usuário informado no form de cadastro;
        #   senha = Senha do usuário informado no form de cadastro.
        
        # RETORNOS:
        #   return True = Retorna True em caso de sucesso na inclusão do usuário;
        #   return False = Retorna False em caso de fracasso na inclusão do usuário.
        #########################################################################################

        self.usuarioNovo = Usuario()
        self.usuarioNovo.set_nome(nome)
        self.usuarioNovo.set_email(email)
        self.usuarioNovo.set_usuario(user)
        self.usuarioNovo.set_grupo(grupo)
        self.usuarioNovo.gerarSenha(senha)
        self.usuarioNovo.set_hashSenhaNova("")
        self.usuarioNovo.set_senhaNova(False)
        self.usuarioNovo.set_ativo(False)
        self.usuarioNovo.set_delete(False)

        self.usuarioLogado = Usuario()

        manterUsuarioDao = ManterUsuarioDao()
        if manterUsuarioDao.inserirUsuario(self.usuarioNovo): #Verifica o retorno do banco
            consultaIdUser = ConsultaIds()
            #Consulta id do usuário logado
            self.usuarioLogado.set_id(consultaIdUser.consultaIdUserLogado(session["usuario"]))
            #Consulta o ultimo id da tabela
            self.usuarioNovo.set_id(consultaIdUser.consultaIdFinalUser())
            #Gera Log
            self.geraLogUsuario("INSERT")
            return True
        else:
            return False
        
    def editarUsuario(self, id: int, nome: str, user: str, email: str, grupo: str, senha: str) -> bool:
        #########################################################################################
        # Essa função recebe os dados de um usuário existente para a alterção.
        
        # PARAMETROS:
        #   id = ID do usário que foi selecionado para a alterção;
        #   nome = Nome do usuário informado no form de cadastro;
        #   user = Username do usuário informado no form de cadastro;
        #   email = E-mail do usuário informado no form de cadastro;
        #   grupo = Grupo do usuário informado no form de cadastro;
        #   senha = Senha do usuário informado no form de cadastro.
        
        # RETORNOS:
        #   return True = Retorna True em caso de sucesso na alteração do usuário;
        #   return False = Retorna False em caso de fracasso na alteração do usuário.
        #########################################################################################

        self.usuarioNovo = Usuario()
        self.usuarioLogado = Usuario()
        self.usuarioAntigo = Usuario()
        manterUsuarioDao = ManterUsuarioDao()
        consultaIdUser = ConsultaIds()    

        self.usuarioAntigo = manterUsuarioDao.mostarUsuarioDetalhado(id)

        self.usuarioNovo.set_id(id)
        self.usuarioNovo.set_nome(nome)
        self.usuarioNovo.set_email(email)
        self.usuarioNovo.set_usuario(user)
        self.usuarioNovo.set_grupo(grupo)
        self.usuarioNovo.set_senha(senha)
        self.usuarioNovo.set_ativo(False)
        self.usuarioNovo.set_delete(False)
        self.usuarioNovo.set_complex(self.usuarioAntigo.get_complex())

        #Verifica se a senha teve alteração, se teve é gerada novo hash da senha nova
        if self.usuarioAntigo.get_senha() != self.usuarioNovo.get_senha(): 
            self.usuarioNovo.gerarSenha(senha.upper())

        if manterUsuarioDao.editarUsuario(self.usuarioNovo):
            #Consulta id do usuário logado
            self.usuarioLogado.set_id(consultaIdUser.consultaIdUserLogado(session["usuario"]))
            #Gera Log
            self.geraLogUsuario("UPDATE")
            return True
        else:
            return False
        
    
    def excluirUsuario(self, id: int) -> int:
        #########################################################################################
        # Essa função recebe o id do usuário a ser excluido, mas caso o usuário já tenha efetuado
        # alguma movimentação no sistema ele é desativado.
        
        # PARAMETROS:
        #   id = ID do usário que foi selecionado para a exclusão ou desativação.
        
        # RETORNOS:
        #   return 1 = Retorna 1 caso o usuário que foi selecionada seja o mesmo usuário que está
        #     logado;
        #   return 2 = Retorna 2 em caso de sucesso na exclusão/desativação do usuário;
        #   return 0 = Retorna 0 em caso de fracasso na exclusão/desativação do usuário.
        #########################################################################################

        manterUsuarioDao = ManterUsuarioDao()
        verificaMovimentoDao = VerificaMovimentoDao()
        consultaIdUser = ConsultaIds()
        self.usuarioLogado = Usuario()
        self.usuarioAntigo = Usuario()

        self.usuarioAntigo = manterUsuarioDao.mostarUsuarioDetalhado(id)

        self.usuarioLogado.set_id(consultaIdUser.consultaIdUserLogado(session["usuario"]))
        
        #Verifica se o usuário selecionado é o mesmo que o usuário logado
        if id == self.usuarioLogado.get_id():
            return 1
        else:
            if verificaMovimentoDao.verificaMovimentoUsuario(id):
                if manterUsuarioDao.inativaUsuario(id):
                    self.geraLogUsuario("ACTIVE")
                    return 3
                else:
                    return 0
                
            else:
                if manterUsuarioDao.excluirUsuario(id):
                    self.geraLogUsuario("DELETE")
                    return 2
                else:
                    return 0


    def geraLogUsuario(self, acao: str):
        #########################################################################################
        # Essa função gera log do INSERT, UPDATE e DELETE do usuário.
        
        # PARAMETROS:
        #   acao = Ação que foi efetuada.
        
        # RETORNOS:
        #   Não tem retorno.
        #########################################################################################

        log = Log()
        log.set_acao(acao)
        log.set_dataHora(datetime.now())
        log.set_observacao("")
        log.set_usuario(self.usuarioLogado)

        if acao == "INSERT":
            log.set_dadosAntigos({"vazio": 0})
            log.set_dadosNovos(self.usuarioNovo.toJson())
        elif acao == "UPDATE":
            log.set_dadosAntigos(self.usuarioAntigo.toJson())
            log.set_dadosNovos(self.usuarioNovo.toJson())
        else:
            log.set_dadosAntigos(self.usuarioAntigo.toJson())
            log.set_dadosNovos({"vazio": 0})

        logDao = GeraLogUsuarioDao()
        logDao.inserirLog(log)