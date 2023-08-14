from ..controllers.ControleManterTerceiro import ControleManterTerceiro
from ..models.dao.ManterFuncionarioDao import ManterFuncionarioDao
from ..models.dao.ControleTerceiroDao import ControleTerceiroDao
from ..models.entity.MovimentoTerceiro import MovimentoTerceiro
from ..models.dao.ManterTerceiroDao import ManterTerceiroDao
from ..extensions.FiltrosJson import filtroData, filtroNome
from ..models.dao.ConsultaIdsDao import ConsultaIdsDao
from ..models.entity.Funcionario import Funcionario
from ..models.dao.PesquisaDao import PesquisaDao
from ..models.dao.TerceiroDao import TerceiroDao
from ..models.dao.GeraLogDao import GeraLogDao
from ..models.entity.Usuario import Usuario
from ..models.entity.Log import Log
from datetime import datetime
from flask import session

"""
Classe Controller para controle de Terceiro
@author - Fabio
@version - 1.0
@since - 27/07/2023
"""

class ControleTerceiro:

    def inserirEntrada(self, cpf: str, nome: str, empesa: str, placa: str, veiculo: str, motivo: str, pessoaVisit: str, dtEnt: str, hrEnt: str, acomps: list[dict]) -> bool:
        self.movimentoTercNovo = MovimentoTerceiro()
        funcionario = Funcionario()
        self.usuarioLogado = Usuario()
        manterFuncionarioDao = ManterFuncionarioDao()
        funcionario = manterFuncionarioDao.mostarFuncionarioDetalhadoCracha(list(pessoaVisit.split())[0])
        self.movimentoTercNovo.pessoaVisit = funcionario
        self.movimentoTercNovo.empresa = empesa.upper().strip()
        self.movimentoTercNovo.placa = placa.upper().strip()
        self.movimentoTercNovo.veiculo = veiculo.upper().strip()
        self.movimentoTercNovo.motivo = motivo.upper().strip()
        self.movimentoTercNovo.dataEnt = dtEnt.replace("-", "")
        self.movimentoTercNovo.horaEnt = hrEnt
        self.movimentoTercNovo.delete = False
        
        pesquisaDao = PesquisaDao()
        manterTerceiroDao = ManterTerceiroDao()
        controleManterTerceiro = ControleManterTerceiro()
        terceiro = pesquisaDao.pesquisaCpfTercFormMov(''.join(filter(str.isdigit, cpf)))

        if terceiro:
            terceiroMov = manterTerceiroDao.mostrarTerceiroDetalhadoCpf(''.join(filter(str.isdigit, cpf)))
            self.movimentoTercNovo.terceiro = terceiroMov
        else:
            codigo = controleManterTerceiro.incrementaCodigo()
            controleManterTerceiro.incluirTerceiro(codigo, nome.upper().strip(), cpf)
            terceiroMov = manterTerceiroDao.mostrarTerceiroDetalhadoCpf(''.join(filter(str.isdigit, cpf)))
            self.movimentoTercNovo.terceiro = terceiroMov

        listaAcomps = []
        for acomp in acomps:
            acompanhante = pesquisaDao.pesquisaCpfTercFormMov(''.join(filter(str.isdigit, acomp["cpf"])))
            if acompanhante:
                acompMov = manterTerceiroDao.mostrarTerceiroDetalhadoCpf(''.join(filter(str.isdigit, acomp["cpf"])))
                listaAcomps.append(acompMov)
            else:
                codigo = controleManterTerceiro.incrementaCodigo()
                controleManterTerceiro.incluirTerceiro(codigo, acomp["nome"].upper().strip(), acomp["cpf"])
                acompMov = manterTerceiroDao.mostrarTerceiroDetalhadoCpf(''.join(filter(str.isdigit, acomp["cpf"])))
                listaAcomps.append(acompMov)

        self.movimentoTercNovo.acomps = listaAcomps
        controleTerceiroDao = ControleTerceiroDao()
        consultaIdsDao = ConsultaIdsDao()
        controleTerceiroDao.inserirEntrada(self.movimentoTercNovo)
        self.movimentoTercNovo.id = consultaIdsDao.consultaIdFinalMovTerc()

        controleTerceiroDao.inserirVisitante(self.movimentoTercNovo.terceiro, self.movimentoTercNovo)
        if len(listaAcomps) != 0:
            for acomp in listaAcomps:
                controleTerceiroDao.inserirVisitante(acomp, self.movimentoTercNovo)
        
        consultaIds = ConsultaIdsDao()
        if session["grupo"] == "ADM":
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuario"])
        else:
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuarioVIG"])

        self.geraLogControleTerceiro("ENTRADA", "")

        return True
    

    def consultaMovTercDetalhado(self, id: int) -> MovimentoTerceiro:
        controleTerceiroDao = ControleTerceiroDao()
        manterFuncionarioDao = ManterFuncionarioDao()
        manterTerceiroDao = ManterTerceiroDao()
        terceiroDao = TerceiroDao()
        movimento = controleTerceiroDao.consultaMovTercDetalhado(id)

        funcionario = manterFuncionarioDao.mostarFuncionarioDetalhado(controleTerceiroDao.consultaIdFuncMovTerc(movimento.id))
        movimento.pessoaVisit = funcionario

        listaTerc = []
        ids = terceiroDao.terceirosMovimento(movimento.id)
        if len(ids) != 0:
            for i, id in enumerate(ids):
                if i == 0:
                    movimento.terceiro = manterTerceiroDao.mostrarTerceiroDetalhadoId(id)
                else:
                    listaTerc.append(manterTerceiroDao.mostrarTerceiroDetalhadoId(id))

        movimento.acomps = listaTerc

        return movimento


    def inserirSaida(self, id: int, dataSaid: str, horaSaid: str, cpf: str, acomps: list, cracha: str) -> bool:
        controleTerceiroDao = ControleTerceiroDao()
        self.movimentoTercNovo = MovimentoTerceiro()
        self.usuarioLogado = Usuario()
        manterTerceiroDao = ManterTerceiroDao()
        manterFuncionario = ManterFuncionarioDao()

        self.movimentoTercNovo = controleTerceiroDao.consultaMovTercDetalhado(id)
        self.movimentoTercNovo.terceiro = manterTerceiroDao.mostrarTerceiroDetalhadoCpf(''.join(filter(str.isdigit, cpf)))
        self.movimentoTercNovo.pessoaVisit = manterFuncionario.mostarFuncionarioDetalhadoCracha(cracha)
        self.movimentoTercNovo.dataSai = dataSaid.replace("-", "")
        self.movimentoTercNovo.horaSai = horaSaid

        listaAcomps = []
        if len(acomps) > 0:
            for acomp in acomps:
                acompanhante = manterTerceiroDao.mostrarTerceiroDetalhadoCpf(''.join(filter(str.isdigit, acomp["cpf"])))
                listaAcomps.append(acompanhante)

        self.movimentoTercNovo.acomps = listaAcomps

        if controleTerceiroDao.inserirSaida(self.movimentoTercNovo):
            consultaIds = ConsultaIdsDao()
            if session["grupo"] == "ADM":
                self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuario"])
            else:
                self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuarioVIG"])

            self.geraLogControleTerceiro("SAIDA", "")
        
        return True


    def consultaTerceirosEntrada(self) -> list[dict]:
        controleTerceiroDao = ControleTerceiroDao()
        movimentos = controleTerceiroDao.consultaTerceirosEntrada()
        manterTerceiroDao = ManterTerceiroDao()
        listaMovimentos = []
        for movimento in movimentos:
            nometerc = manterTerceiroDao.consultaTerceiro(movimento.id_movTerc)
            dicMovimento = {
                "id": movimento.id_movTerc,
                "nomeTerc": filtroNome(nometerc[0]),
                "entrada": f"{filtroData(movimento.mte_dataEntra)} {movimento.mte_horaEntra}",
                "visitado": filtroNome(movimento.nomeFunc),
                "empresa": movimento.mte_empresa
            }

            listaMovimentos.append(dicMovimento)

        return listaMovimentos
    

    def geraLogControleTerceiro(self, acao: str, observacao: str) -> None:
        log = Log()
        log.acao = acao
        log.dataHora = datetime.now()
        log.observacao = observacao
        log.usuario = self.usuarioLogado

        if acao == "ENTRADA" or acao == "SAIDA":
            log.dadosAntigos = {"vazio": 0}
            log.dadosNovos = self.movimentoTercNovo.toJson()
        elif acao == "UPDATE":
            log.dadosAntigos = self.movimentoChaveAntigo.toJson()
            log.dadosNovos = self.movimentoTercNovo.toJson()
        else:
            log.dadosAntigos = self.movimentoTercNovo.toJson()
            log.dadosNovos = {"vazio": 0}

        logDao = GeraLogDao()
        logDao.inserirLogControleTerceiro(log)