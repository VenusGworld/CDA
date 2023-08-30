from ..models.dao.VerificamovimentoDao import VerificaMovimentoDao
from ..models.dao.ManterUsuarioDao import ManterUsuarioDao
from ..models.dao.ConsultaIdsDao import ConsultaIdsDao
from ..models.dao.GeraLogDao import GeraLogDao
from ..models.entity.Usuario import Usuario
from ..models.entity.Log import Log
from datetime import datetime
from flask import session

class ControleManterUsuario:
    """
    Classe Controller para funções recionadas ao CRUD de usuário
    @author - Fabio
    @version - 1.0
    @since - 23/05/2023
    """

    def consultarUsuarios(self) -> list[dict]:
        """
        Consulta e retorna uma lista de dicionários contendo informações resumidas de todos os usuários.

        :return: Uma lista de dicionários contendo informações sobre os usuários.
            Cada dicionário possui chaves "id", "nome", "usuario" e "grupo".
        """
        
        manterUsuarioDao = ManterUsuarioDao()
        usuarios = manterUsuarioDao.consultarUsuarios()
        listaDados = []
        for usuario in usuarios:
            dicUser = {
                "id": usuario.id,
                "nome": usuario.nome,
                "usuario": usuario.usuario,
                "grupo": usuario.grupo,
            }

            listaDados.append(dicUser)

        return listaDados
    

    def consultarUsuarioDetalhado(self, id: int) -> Usuario:
        """
        Consulta os detalhes de um usuário específico.

        :param id: O ID do usuário a ser consultado.

        :return: Um objeto Usuario contendo as informações detalhadas do usuário.
        """

        manterUsuarioDao = ManterUsuarioDao()
        usuario = manterUsuarioDao.consultarUsuarioDetalhado(id)
        
        return usuario

    
    def incluirUsuario(self, nome: str, user: str, email: str, grupo: str, senha: str) -> bool:
        """
        Inclui um novo usuário no sistema.

        :param nome: O nome do novo usuário.
        :param user: O nome de usuário do novo usuário.
        :param email: O endereço de e-mail do novo usuário.
        :param grupo: O grupo ao qual o novo usuário pertence (ADM, TEC, VIG).
        :param senha: A senha inicial do novo usuário.

        :return: True se a inclusão for bem-sucedida, False caso contrário.
        """

        self.usuarioNovo = Usuario(nome=nome, email=email, usuario=user, grupo=grupo, hashSenhaNova="", senhaNova=False, ativo=False, delete=False)
        self.usuarioNovo.gerarSenha(senha)

        self.usuarioLogado = Usuario()

        manterUsuarioDao = ManterUsuarioDao()
        if manterUsuarioDao.inserirUsuario(self.usuarioNovo):
            consultaIdUser = ConsultaIdsDao()
            self.usuarioLogado.id = consultaIdUser.consultaIdUserLogado(session["usuario"])
            self.usuarioNovo.id = consultaIdUser.consultaIdFinalUser()
            self.geraLogUsuario("INSERT")
        
        return True
        
        
    def editarUsuario(self, id: int, nome: str, user: str, email: str, grupo: str, senha: str) -> bool:
        """
        Edita as informações de um usuário existente no sistema.

        :param id: O ID do usuário a ser editado.
        :param nome: O novo nome do usuário.
        :param user: O novo nome de usuário do usuário.
        :param email: O novo endereço de e-mail do usuário.
        :param grupo: O novo grupo ao qual o usuário pertence (ADM, TEC, VIG).
        :param senha: A nova senha do usuário.

        :return: True se a edição for bem-sucedida, False caso contrário.
        """

        self.usuarioLogado = Usuario()
        manterUsuarioDao = ManterUsuarioDao()
        consultaIdUser = ConsultaIdsDao()    

        self.usuarioAntigo = manterUsuarioDao.consultarUsuarioDetalhado(id)

        self.usuarioNovo = Usuario(id=id, nome=nome, email=email, usuario=user, grupo=grupo,
                                     senha=senha, ativo=False, delete=False, complex=self.usuarioAntigo.complex)

        #Verifica se a senha teve alteração, se teve é gerada novo hash da senha nova
        if self.usuarioAntigo.senha != self.usuarioNovo.senha: 
            self.usuarioNovo.gerarSenha(senha.upper())

        if manterUsuarioDao.editarUsuario(self.usuarioNovo):
            self.usuarioLogado.id = consultaIdUser.consultaIdUserLogado(session["usuario"])
            self.geraLogUsuario("UPDATE")
        
        return True
        
        
    def excluirUsuario(self, id: int) -> int:
        """
        Exclui ou Inativa um usuário do sistema.

        :param id: O ID do usuário a ser excluído.

        :return: Um código de retorno indicando o resultado da ação:
            - 1: Tentativa de excluir o próprio usuário logado.
            - 2: usuário excluído com sucesso.
            - 3: usuário inativado (quando usuário tem movimentação no sistema).
        """

        manterUsuarioDao = ManterUsuarioDao()
        verificaMovimentoDao = VerificaMovimentoDao()
        consultaIdUser = ConsultaIdsDao()
        self.usuarioLogado = Usuario()
        self.usuarioAntigo = Usuario()

        self.usuarioAntigo = manterUsuarioDao.consultarUsuarioDetalhado(id)

        self.usuarioLogado.id = consultaIdUser.consultaIdUserLogado(session["usuario"])
        
        #Verifica se o usuário selecionado é o mesmo que o usuário logado
        if id == self.usuarioLogado.id:
            return 1
        else:
            if verificaMovimentoDao.verificaMovimentoUsuario(id):
                if manterUsuarioDao.inativarUsuario(id):
                    self.geraLogUsuario("ACTIVE")
                    return 3
                
            else:
                if manterUsuarioDao.excluirUsuario(id):
                    self.geraLogUsuario("DELETE")
                    return 2


    def geraLogUsuario(self, acao: str) -> None:
        """
        Gera um registro de log para ações relacionadas ao manter usuário.

        :param acao: Ação realizada (INSERT, UPDATE, DELETE).

        :return: Nenhum valor é retornado.
        """

        log = Log(acao=acao, dataHora=datetime.now(), observacao="", usuario=self.usuarioLogado)

        if acao == "INSERT":
            log.dadosAntigos = {"vazio": 0}
            log.dadosNovos = self.usuarioNovo.toJson()
        elif acao == "UPDATE":
            log.dadosAntigos = self.usuarioAntigo.toJson()
            log.dadosNovos = self.usuarioNovo.toJson()
        else:
            log.dadosAntigos = self.usuarioAntigo.toJson()
            log.dadosNovos = {"vazio": 0}

        logDao = GeraLogDao()
        logDao.inserirLogUsuario(log)