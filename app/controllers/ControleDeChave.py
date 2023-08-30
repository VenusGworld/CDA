from ..models.dao.ManterFuncionarioDao import ManterFuncionarioDao
from ..extensions.FiltrosJson import filtroData, filtroNome
from ..models.dao.ControleChaveDao import ControleChaveDao
from ..models.entity.MovimentoChave import MovimentoChave
from ..models.dao.ManterChaveDao import ManterChaveDao
from ..models.dao.ConsultaIdsDao import ConsultaIdsDao
from ..models.entity.Funcionario import Funcionario
from ..models.dao.GeraLogDao import GeraLogDao
from ..models.entity.Usuario import Usuario
from ..models.entity.Log import Log
from datetime import datetime
from flask import session

class ControleDeChave:
    """
    Classe Controller para as funções relacionadas ao controle de chaves
    @author - Fabio
    @version - 1.0
    @since - 23/05/2023
    """

    def inserirRetirada(self, dataRet: str, horaRet: str, codChave: str, crachaFun: str) -> bool:
        """
        Insere um registro de retirada de chave no sistema.

        :param dataRet: Data da retirada da chave no formato 'YYYY-MM-DD'.
        :param horaRet: Hora da retirada da chave no formato 'HH:MM'.
        :param codChave: Código da chave a ser retirada.
        :param crachaFun: Crachá do funcionário que está retirando a chave.

        :return: True se a inserção for bem-sucedida, False caso contrário.
        """
        
        controleChaveDao = ControleChaveDao()
        manterFuncionarioDao = ManterFuncionarioDao()
        manterChaveDao = ManterChaveDao()
        self.usuarioLogado = Usuario()
        funcionario = manterFuncionarioDao.consultarFuncionarioDetalhadoCracha(list(crachaFun.split())[0])
        chave = manterChaveDao.consultarChaveDetalhadaCodigo(list(codChave.split())[0])
        self.movimentoChaveNovo = MovimentoChave(dataRet=dataRet.replace("-", ""), horaRet=horaRet, chave=chave, respRet=funcionario, respDev=Funcionario(), delete=False)

        if controleChaveDao.inserirRetirada(self.movimentoChaveNovo):
            consultaIds = ConsultaIdsDao()
            if session["grupo"] == "ADM":
                self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuario"])
            else:
                self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuarioVIG"])

            self.movimentoChaveNovo.id = consultaIds.consultaIdFinalMovChave()
            self.geraLogControleChave("RETIRADA", "")
            
        return True
        
    
    def inserirDevolucao(self, id: int, dataDev: str, horaDev: str, respDev: str, checkbox: bool) -> bool:
        """
        Insere um registro de devolução de chave no sistema.

        :param id: O ID do registro de movimento de chave a ser atualizado.
        :param dataDev: Data da devolução da chave no formato 'YYYY-MM-DD'.
        :param horaDev: Hora da devolução da chave no formato 'HH:MM'.
        :param respDev: Crachá do responsável pela devolução da chave.
        :param checkbox: Indica se a mesma pessoa que retirou a chave está realizando a devolução.
        """
        
        controleChaveDao = ControleChaveDao()
        manterFuncionarioDao = ManterFuncionarioDao()
        self.usuarioLogado = Usuario()
        self.movimentoChaveNovo = controleChaveDao.consultaMovimentoChaveDetalhado(int(id))
        self.movimentoChaveNovo.dataDev = dataDev.replace("-", "")
        self.movimentoChaveNovo.horaDev = horaDev
        if checkbox:
            self.movimentoChaveNovo.respDev = manterFuncionarioDao.consultarFuncionarioDetalhadoCracha(list(respDev.split())[0])
        else:
            self.movimentoChaveNovo.respDev = self.movimentoChaveNovo.respRet
        
        if controleChaveDao.inserirDevolucao(self.movimentoChaveNovo):
            consultaIds = ConsultaIdsDao()
            if session["grupo"] == "ADM":
                self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuario"])
            else:
                self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuarioVIG"])

            self.geraLogControleChave("DEVOLUCAO", "")
            
        return True
    

    def editarMovimentoChave(self, id: int, dataRet: str, horaRet: str, crachaRet: str, dataDev: str, horaDev: str, crachaDev: str, codigoChave: str, observacao: str) -> bool:
        """
        Altera um movimento de chave específico

        :param id: O ID do registro de movimento de chave a ser alterado.
        :param dataRet: Data da devolução da chave no formato 'YYYY-MM-DD'.
        :param horaRet: Hora da devolução da chave no formato 'HH:MM'.
        :param crachaRet: Crachá do responsável pela retirada da chave.
        :param dataDev: Data da devolução da chave no formato 'YYYY-MM-DD'.
        :param horaDev: Hora da devolução da chave no formato 'HH:MM'.
        :param crachaDev: Crachá do responsável pela devolução da chave.
        :param codigoChave: Chave que pertence ao movimento.

        :return: True se a edição for bem-sucedida, False caso contrário.
        """
        
        controleChaveDao = ControleChaveDao()
        self.usuarioLogado = Usuario()
        manterFuncionarioDao = ManterFuncionarioDao()
        manterChaveDao = ManterChaveDao()

        respRet = manterFuncionarioDao.consultarFuncionarioDetalhadoCracha(crachaRet)
        respDev = manterFuncionarioDao.consultarFuncionarioDetalhadoCracha(crachaDev)
        chave = manterChaveDao.consultarChaveDetalhadaCodigo(codigoChave)

        self.movimentoChaveNovo = MovimentoChave(id=id, dataRet=dataRet.replace("-", ""), horaRet=horaRet, respRet=respRet, 
                                                 dataDev=dataDev.replace("-", ""), horaDev=horaDev, respDev=respDev, chave=chave)
        
        self.movimentoChaveAntigo = controleChaveDao.consultaMovimentoChaveDetalhado(id)

        controleChaveDao.editarMovimentoChave(self.movimentoChaveNovo)

        consultaIds = ConsultaIdsDao()
        if session["grupo"] == "ADM":
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuario"])
        else:
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuarioVIG"])

        self.geraLogControleChave("UPDATE", observacao)

        return True
    

    def excluirMovimentoChave(self, id: int, observacao: str) -> bool:
        controleChaveDao = ControleChaveDao()
        self.usuarioLogado = Usuario()
        self.movimentoChaveAntigo = controleChaveDao.consultaMovimentoChaveDetalhado(id)

        controleChaveDao.excluirMovimentoChave(self.movimentoChaveAntigo)

        consultaIds = ConsultaIdsDao()
        if session["grupo"] == "ADM":
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuario"])
        else:
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuarioVIG"])

        self.geraLogControleChave("DELETE", observacao)

        return True


    def consultaMovimentoDetalhado(self, id: int) -> MovimentoChave:
        """
        Consulta e retorna os detalhes de um registro de movimento de chave específico.

        :param id: O ID do registro de movimento de chave a ser consultado.

        :return: Um objeto MovimentoChave contendo detalhes do registro de movimento de chave.
        """

        controleChaveDao = ControleChaveDao()
        return controleChaveDao.consultaMovimentoChaveDetalhado(id)


    def listaChavesRetiradas(self) -> list[dict]:
        """
        Consulta e retorna uma lista de chaves que foram retiradas.

        :return: Uma lista de dicionários contendo informações sobre as chaves retiradas.
            Cada dicionário possui chaves "id", "nome", "retirada" e "responsavel".
        """
        
        controleChaveDao = ControleChaveDao()
        respDao = controleChaveDao.consultaChavesRetiradas()
        listaChave = []
        for chave in respDao:
            dicChave ={
                "id": chave.id_movChave,
                "nome": chave.nomeChave,
                "retirada": f"{filtroData(chave.mch_dataRet)} {chave.mch_horaRet}",
                "responsavel": chave.nomeResp           
            }

            listaChave.append(dicChave)
        
        return listaChave
    
    
    def listaChavesManut(self) -> list[dict]:
        """
        Consulta e retorna uma lista de chaves que foram retiradas e devolvidas para manutenção.

        :return: Uma lista de dicionários contendo informações sobre as chaves retiradas e devolvidas.
            Cada dicionário possui chaves "id", "nome", "retirada", "devolucao" e "respRet".
        """
        
        controleChaveDao = ControleChaveDao()
        respDao = controleChaveDao.consultaChavesManut()
        listaChave = []
        for movimento in respDao:
            dicChave ={
                "id": movimento.id_movChave,
                "nome": filtroNome(movimento.nomeChave),
                "retirada": f"{filtroData(movimento.mch_dataRet)} {movimento.mch_horaRet}",
                "devolucao": f"{filtroData(movimento.mch_dataDev)} {movimento.mch_horaDev}",
                "respRet": filtroNome(movimento.nomeResp)          
            }

            listaChave.append(dicChave)
        
        return listaChave


    def geraLogControleChave(self, acao: str, observacao: str) -> None:
        """
        Gera um registro de log para ações relacionadas ao controle de chaves.

        :param acao: Ação realizada (RETIRADA, DEVOLUCAO, UPDATE, DELETE).
        :param observacao: Observações adicionais sobre a ação (obrigatorio para usuários do grupo VIG).

        :return: Nenhum valor é retornado.
        """

        log = Log()
        log.acao = acao
        log.dataHora = datetime.now()
        log.observacao = observacao
        log.usuario = self.usuarioLogado

        if acao == "RETIRADA" or acao == "DEVOLUCAO":
            log.dadosAntigos = {"vazio": 0}
            log.dadosNovos = self.movimentoChaveNovo.toJson()
        elif acao == "UPDATE":
            log.dadosAntigos = self.movimentoChaveAntigo.toJson()
            log.dadosNovos = self.movimentoChaveNovo.toJson()
        else:
            log.dadosAntigos = self.movimentoChaveAntigo.toJson()
            log.dadosNovos = {"vazio": 0}

        logDao = GeraLogDao()
        logDao.inserirLogControleChave(log)

