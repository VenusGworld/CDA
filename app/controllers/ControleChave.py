from flask import session
from ..models.entity.MovimentoChave import MovimentoChave
from ..models.entity.Log import Log
from ..models.entity.Usuario import Usuario
from ..models.entity.Funcionario import Funcionario
from ..models.dao.ControleChaveDao import ControleChaveDao
from ..models.dao.ManterFuncionarioDao import ManterFuncionarioDao
from ..models.dao.ManterChaveDao import ManterChaveDao
from ..models.dao.GeraLogDao import GeraLogDao
from ..models.dao.ConsultaIdsDao import ConsultaIdsDao
from ..extensions.FiltrosJson import filtroData, filtroNome
from datetime import datetime

"""
Classe Controller para o controle de Chave
@author - Fabio
@version - 1.0
@since - 23/05/2023
"""

class ControleCrontoleDeChave:

    def inserirRetirada(self, dataRet: str, horaRet: str, codChave: str, crachaFun: str) -> bool:
        self.movimentoChaveNovo = MovimentoChave()
        controleChaveDao = ControleChaveDao()
        manterFuncionarioDao = ManterFuncionarioDao()
        manterChaveDao = ManterChaveDao()
        self.usuarioLogado = Usuario()
        funcionario = manterFuncionarioDao.mostarFuncionarioDetalhadoCracha(list(crachaFun.split())[0])
        chave = manterChaveDao.mostrarChaveDetalhadaCodigo(list(codChave.split())[0])
        self.movimentoChaveNovo.dataRet = dataRet.replace("-", "")
        self.movimentoChaveNovo.horaRet = horaRet
        self.movimentoChaveNovo.chave = chave
        self.movimentoChaveNovo.respRet = funcionario
        self.movimentoChaveNovo.dataDev = ""
        self.movimentoChaveNovo.horaDev = ""
        self.movimentoChaveNovo.respDev = Funcionario()
        self.movimentoChaveNovo.delete = False

        if controleChaveDao.inserirRetirada(self.movimentoChaveNovo):
            consultaIds = ConsultaIdsDao()
            if session["grupo"] == "ADM":
                self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuario"])
            else:
                self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuarioVIG"])

            self.movimentoChaveNovo.id = consultaIds.consultaIdFinalMovChave()
            self.geraLogControleChave("RETIRADA", "")
            
            return True
        
    
    def inserirDevolucao(self, id: int, dataDev: str, horaDev: str, respDev: str, checkbox) -> bool:
        self.movimentoChaveNovo = MovimentoChave()
        controleChaveDao = ControleChaveDao()
        manterFuncionarioDao = ManterFuncionarioDao()
        self.usuarioLogado = Usuario()
        self.movimentoChaveNovo = controleChaveDao.consultaMovimentoChaveDetalhado(int(id))
        self.movimentoChaveNovo.dataDev = dataDev.replace("-", "")
        self.movimentoChaveNovo.horaDev = horaDev
        if checkbox:
            self.movimentoChaveNovo.respDev = manterFuncionarioDao.mostarFuncionarioDetalhadoCracha(list(respDev.split())[0])
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
        

    def consultaMovimentoDetalhado(self, id: int) -> MovimentoChave:
        controleChaveDao = ControleChaveDao()
        return controleChaveDao.consultaMovimentoChaveDetalhado(id)


    def listaChavesRetiradas(self) -> list[dict]:
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
        controleChaveDao = ControleChaveDao()
        respDao = controleChaveDao.consultaChavesManut()
        listaChave = []
        for movimento in respDao:
            dicChave ={
                "id": movimento.id_movChave,
                "nome": movimento.nomeChave,
                "retirada": f"{filtroData(movimento.mch_dataRet)} {movimento.mch_horaRet}",
                "devolucao": f"{filtroData(movimento.mch_dataDev)} {movimento.mch_horaDev}",
                "respRet": filtroNome(movimento.nomeResp)          
            }

            listaChave.append(dicChave)
        
        return listaChave


    def geraLogControleChave(self, acao: str, observacao: str) -> None:
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

