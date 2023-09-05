from ..models.dao.VerificaMovimentoDao import VerificaMovimentoDao
from ..models.dao.ControleChaveDao import ControleChaveDao
from ..models.dao.ManterChaveDao import ManterChaveDao
from ..models.dao.ConsultaIdsDao import ConsultaIdsDao
from ..models.dao.GeraLogDao import GeraLogDao
from ..models.entity.Usuario import Usuario
from ..models.entity.Chave import Chave
from ..models.entity.Log import Log
from datetime import datetime
from flask import session

class ControleManterChave:
    """
    Classe Controller para as funções relacionadas ao CRUD de chave
    @author - Fabio
    @version - 1.0
    @since - 04/07/2023
    """

    def consultaChaves(self) -> list[dict]:
        """
        Consulta e retorna uma lista de dicionários contendo informações resumidas de todas as chaves.

        :return: Lista de dicionários contendo informações das chaves.
            Cada dicionário possui chaves "id", "codigo" e "nome".
        """
        
        manterChaveDao = ManterChaveDao()
        respDao = manterChaveDao.consultaChaves()
        listaChaves = []
        for chave in respDao:
            dicChave ={
                "id": chave.id_chave,
                "codigo": chave.ch_codigo,
                "nome": chave.ch_nome
            }

            listaChaves.append(dicChave)
        
        return listaChaves
    
    
    def consultaChaveDetalhadaId(self, id: int) -> Chave:
        """
        Consulta detalhes de uma chave pelo ID.

        :param id: O ID da chave a ser consultada.

        :return: Um objeto Chave contendo os detalhes da chave consultada.
        """
        
        manterChaveDao = ManterChaveDao()
        chave = manterChaveDao.consultarChaveDetalhadaId(id)

        return chave
    

    def incluirChave(self, codigo: str, nome: str) -> bool:
        """
        Inclui uma nova chave no sistema.

        :param codigo: O código da nova chave.
        :param nome: O nome da nova chave.

        :return: True se a inclusão for bem-sucedida, False caso contrário.
        """
        
        manterChaveDao = ManterChaveDao()
        consultaIds = ConsultaIdsDao()
        self.usuarioLogado = Usuario()

        self.chaveNova = Chave(codigo=codigo, nome=nome, ativo=False, delete=False)

        #Verifica se o usuário que efetuou a acão é do grupo ADM
        if session["grupo"] == "ADM":
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuario"])
        else:
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuarioVIG"])
            
        if manterChaveDao.incluirChave(self.chaveNova):
            self.chaveNova.id = manterChaveDao.consultaUltimoId()
            self.geraLogChave("INSERT", "")
        
        return True
        
    
    def editarChave(self, id: int, codigo: str, nome: str, observacao: str) -> bool:
        """
        Edita os detalhes de uma chave com base no ID fornecido.

        :param id: O ID da chave a ser editada.
        :param codigo: O novo código da chave.
        :param nome: O novo nome da chave.
        :param observacao: A observação relacionada à edição da chave (obrigatorio para usuários do grupo VIG).

        :return: True se a edição for bem-sucedida, False caso contrário.
        """

        manterChaveDao = ManterChaveDao()
        consultaIds = ConsultaIdsDao()
        self.usuarioLogado = Usuario()
        
        self.chaveAntiga = Chave()
        self.chaveAntiga = manterChaveDao.consultarChaveDetalhadaId(id)
        
        self.chaveNova = Chave(id=id, codigo=codigo, nome=nome, ativo=False, delete=False)

        #Verifica se o usuário que efetuou a acão é do grupo ADM
        if session["grupo"] == "ADM":
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuario"])
        else:
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuarioVIG"])

        if manterChaveDao.editarChave(self.chaveNova):
            self.geraLogChave("UPDATE", observacao)

        return True
        
    
    def excluirChave(self, id: int, observacao: str) -> int:
        """
        Exclui uma chave com base no ID fornecido.

        :param id: O ID da chave a ser excluída.
        :param observacao: A observação relacionada à exclusão da chave (obrigatorio para usuários do grupo VIG).

        :return: Um código indicando o resultado da operação:
            - 1 se a chave foi excluída com sucesso.
            - 2 se a chave foi inativada com sucesso.
            - 3 se existem movimentos em aberto associados à chave.
        """

        manterChaveDao = ManterChaveDao()
        controleChaveDao = ControleChaveDao()
        #Consulta os ids dos movimentos
        idsMov = controleChaveDao.verificaMovAbertoChave(id)
        for idMov in idsMov:
            #Verifica se existe algum movimento em abeto
            if controleChaveDao.consultaMovAbertoChave(idMov[0]):
                return 3
            
        verificaMovimentoDao = VerificaMovimentoDao()
        consultaIds = ConsultaIdsDao()
        self.usuarioLogado = Usuario()
        self.chaveAntiga = Chave()

        self.chaveAntiga = manterChaveDao.consultarChaveDetalhadaId(id)

        #Verifica se o usuário que efetuou a acão é do grupo ADM
        if session["grupo"] == "ADM":
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuario"])
        else:
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuarioVIG"])

        if verificaMovimentoDao.verificaMovimentoChave(id):
            if manterChaveDao.inativarChave(id):
                self.geraLogChave("ACTIVE", observacao)
                return 2
        else:   
            if manterChaveDao.excuirChave(id):
                self.geraLogChave("DELETE", observacao)
                return 1
    

    def incrementaCodigoChave(self) -> str:
        """
        Incrementa o código da chave com base no último código existente.

        :return: O próximo código de chave a ser usado.
        """

        manterChaveDao = ManterChaveDao()
        respDao = manterChaveDao.consultaUltimoCodigo()
        if respDao:
            parteInt = int(respDao[0][2:])
            parteInt += 1
            codigo = f"{respDao[0][:2]}{str(parteInt).zfill(4)}"

            return codigo
        else:
            return "CH0001"
    

    def geraLogChave(self, acao: str, observacao: str) -> None:
        """
        Gera um registro de log para ações relacionadas ao manter chave.

        :param acao: Ação realizada (INSERT, UPDATE, DELETE).
        :param observacao: Observações adicionais sobre a ação (obrigatorio para usuários do grupo VIG).

        :return: Nenhum valor é retornado.
        """

        log = Log(acao=acao, dataHora=datetime.now(), observacao=observacao, usuario=self.usuarioLogado)

        if acao == "INSERT":
            log.dadosAntigos = {"vazio": 0}
            log.dadosNovos = self.chaveNova.toJson()
        elif acao == "UPDATE":
            log.dadosAntigos = self.chaveAntiga.toJson()
            log.dadosNovos = self.chaveNova.toJson()
        else:
            log.dadosAntigos = self.chaveAntiga.toJson()
            log.dadosNovos = {"vazio": 0}

        logDao = GeraLogDao()
        logDao.inserirLogChave(log)