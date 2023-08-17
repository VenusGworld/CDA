from ..models.dao.ManterFuncionarioDao import ManterFuncionarioDao
from ..models.dao.ControleGerenteDao import ControleGerenteDao
from ..models.entity.MovimentoGerente import MovimentoGerente
from ..extensions.FiltrosJson import filtroData, filtroNome
from ..models.dao.ConsultaIdsDao import ConsultaIdsDao
from ..models.entity.Funcionario import Funcionario
from ..models.dao.GeraLogDao import GeraLogDao
from ..models.entity.Usuario import Usuario
from ..models.entity.Log import Log
from datetime import datetime
from flask import session

"""
Classe Controller para o controle de Gerente
@author - Fabio
@version - 1.0
@since - 11/08/2023
"""

class ControleDeGerente:

    def inserirEntrada(self, dataEnt: str, horaEnt: str, gerente: str) -> bool:
        self.movimentoGerNovo = MovimentoGerente()
        controleGerenteDao = ControleGerenteDao()
        manterFuncionarioDao = ManterFuncionarioDao()
        self.usuarioLogado = Usuario()

        self.movimentoGerNovo.dataEnt = dataEnt.replace("-", "")
        self.movimentoGerNovo.horaEnt = horaEnt
        self.movimentoGerNovo.gerente = manterFuncionarioDao.mostarFuncionarioDetalhadoCracha(list(gerente.split())[0])
        self.movimentoGerNovo.delete = False

        if controleGerenteDao.inserirEntrada(self.movimentoGerNovo):
            consultaIds = ConsultaIdsDao()
            if session["grupo"] == "ADM":
                self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuario"])
            else:
                self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuarioVIG"])

            self.movimentoGerNovo.id = consultaIds.consultaIdFinalMovGer()
            self.geraLogControleGerente("ENTRADA", "")

        return True
    

    def inserirSaida(self, id: int, dataSai: str, horaSai: str, cracha: str) -> bool:
        self.movimentoGerNovo = MovimentoGerente()
        controleGerenteDao = ControleGerenteDao()
        manterFuncionarioDao = ManterFuncionarioDao()
        self.usuarioLogado = Usuario()

        self.movimentoGerNovo = controleGerenteDao.consultaMovimentoDetalhado(id)
        self.movimentoGerNovo.dataSai = dataSai.replace("-", "")
        self.movimentoGerNovo.horaSai = horaSai
        self.movimentoGerNovo.gerente = manterFuncionarioDao.mostarFuncionarioDetalhadoCracha(cracha)

        if controleGerenteDao.inserirSaida(self.movimentoGerNovo):
            consultaIds = ConsultaIdsDao()
            if session["grupo"] == "ADM":
                self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuario"])
            else:
                self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuarioVIG"])

            self.movimentoGerNovo.id = consultaIds.consultaIdFinalMovGer()
            self.geraLogControleGerente("SAIDA", "")

        return True
    

    def consultaGerentesEntrada(self) -> list[dict]:
        controleGerenteDao = ControleGerenteDao()
        respDao = controleGerenteDao.consultaGerentesEntrada()
        movimentosGerente = []
        for gerente in respDao:
            dictMov = {
                "id": gerente.id_movGere,
                "nome": filtroNome(gerente.nomeGer),
                "entrada": f"{filtroData(gerente.mge_dataEntra)} {gerente.mge_horaEntra}"
            }
            movimentosGerente.append(dictMov)
        
        return movimentosGerente
    

    def listaGerentesManut(self) -> list[dict]:
        controleGerenteDao = ControleGerenteDao()
        respDao = controleGerenteDao.consultaGerentesManut()
        movimentosGerente = []
        for gerente in respDao:
            dictMov = {
                "id": gerente.id_movGere,
                "nome": filtroNome(gerente.nomeGer),
                "entrada": f"{filtroData(gerente.mge_dataEntra)} {gerente.mge_horaEntra}",
                "saida": f"{filtroData(gerente.mge_dataSaid)} {gerente.mge_horaSaid}"
            }
            movimentosGerente.append(dictMov)
        
        return movimentosGerente


    def consultaMovimentoDetalhado(self, id: int) -> MovimentoGerente:
        controleGerenteDao = ControleGerenteDao()
        manterFuncionarioDao = ManterFuncionarioDao()
        idGerMov = controleGerenteDao.consultaIdGerMov(id)
        movimento = controleGerenteDao.consultaMovimentoDetalhado(id)
        movimento.gerente = manterFuncionarioDao.mostarFuncionarioDetalhado(idGerMov)

        return movimento


    def geraLogControleGerente(self, acao: str, observacao: str) -> None:
        log = Log()
        log.acao = acao
        log.dataHora = datetime.now()
        log.observacao = observacao
        log.usuario = self.usuarioLogado

        if acao == "ENTRADA" or acao == "SAIDA":
            log.dadosAntigos = {"vazio": 0}
            log.dadosNovos = self.movimentoGerNovo.toJson()
        elif acao == "UPDATE":
            log.dadosAntigos = self.movimentoGerAntigo.toJson()
            log.dadosNovos = self.movimentoGerNovo.toJson()
        else:
            log.dadosAntigos = self.movimentoGerAntigo.toJson()
            log.dadosNovos = {"vazio": 0}

        logDao = GeraLogDao()
        logDao.inserirLogControleGerente(log)