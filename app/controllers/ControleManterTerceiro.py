from ..models.dao.VerificamovimentoDao import VerificaMovimentoDao
from ..models.dao.ControleTerceiroDao import ControleTerceiroDao
from ..models.dao.ManterTerceiroDao import ManterTerceiroDao
from ..models.dao.ConsultaIdsDao import ConsultaIdsDao
from ..extensions.FiltrosJson import filtroCpf
from ..models.dao.GeraLogDao import GeraLogDao
from ..models.entity.Terceiro import Terceiro
from ..models.entity.Usuario import Usuario
from ..models.entity.Log import Log
from datetime import datetime
from flask import session

"""
Classe Controller para o CRUD do Terceiro
@author - Fabio
@version - 1.0
@since - 26/07/2023
"""

class ControleManterTerceiro:

    def mostrarTerceiros(self) -> list[dict]:
        #########################################################################################
        # Essa função recupera os dados das chaves de um objeto "ManterChaveDao" e cria uma 
        # lista de dicionários, onde cada dicionário representa uma chave e contém seu ID, código 
        # e nome.
        
        # PARAMETROS:
        #   Não tem parametros.
        
        # RETORNOS:
        #   return listaChaves = Retorna uma lista com dicinário das chaves que retornaram do banco.
        #########################################################################################
        
        manterTerceiroDao = ManterTerceiroDao()
        respDao = manterTerceiroDao.mostarTerceiros()
        listaTerceiros = []
        for terceiro in respDao:
            dicTerceiro ={
                "id": terceiro.id_terceiro,
                "codigo": terceiro.te_codigo,
                "nome": terceiro.te_nome,
                "cpf": filtroCpf(terceiro.te_cpf)
            }

            listaTerceiros.append(dicTerceiro)
        
        return listaTerceiros


    def incluirTerceiro(self, codigo: str, nome: str, cpf: str) -> bool:
        #########################################################################################
        # Essa função recebe os dados do funcionário a ser incluido.
        
        # PARAMETROS:
        #   nome = Nome da chave informado no form de cadastro;
        #   codigo = Código da chave gerado pelo sistma.
        
        # RETORNOS:
        #   return True = Retorna True em caso de sucesso na inclusão da chave.
        #########################################################################################

        manterTerceiroDao = ManterTerceiroDao()
        self.terceiroNovo = Terceiro()
        consultaIds = ConsultaIdsDao()
        self.usuarioLogado = Usuario()

        self.terceiroNovo.codigo = codigo
        self.terceiroNovo.nome = nome
        cpf = ''.join(filter(str.isdigit, cpf))
        self.terceiroNovo.cpf = cpf
        self.terceiroNovo.ativo = False
        self.terceiroNovo.delete = False

        if session["grupo"] == "ADM":
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuario"])
        else:
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuarioVIG"])
        
        if manterTerceiroDao.incluirTerceiro(self.terceiroNovo):
            self.terceiroNovo.id = consultaIds.consultaIdFinalTerc()
            self.geraLogTerceiro("INSERT", "")

            return True
        

    def editarTerceiro(self, id: int, codigo: str, cpf: str, nome: str, observacao: str) -> bool:
        manterTerceiroDao = ManterTerceiroDao()
        consultaIds = ConsultaIdsDao()
        self.usuarioLogado = Usuario()
        self.terceiroNovo = Terceiro()
        self.terceiroAntigo = Terceiro()

        self.terceiroAntigo = manterTerceiroDao.mostrarTerceiroDetalhadoId(id)

        self.terceiroNovo.id = id
        self.terceiroNovo.codigo = codigo
        self.terceiroNovo.nome = nome
        self.terceiroNovo.cpf = ''.join(filter(str.isdigit, cpf))
        self.terceiroNovo.ativo = False
        self.terceiroNovo.delete = False

        if session["grupo"] == "ADM":
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuario"])
        else:
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuarioVIG"])

        manterTerceiroDao.editarTerceiro(self.terceiroNovo)
        self.geraLogTerceiro("UPDATE", observacao)

        return True
    

    def excluirTerceiro(self, id: int, observacao: str) -> int:
        manterTerceiroDao = ManterTerceiroDao()
        controleTerceiroDao = ControleTerceiroDao()
        #Verifica se o terceiro a ser excluido está em um movimento aberto
        idsMov = manterTerceiroDao.verificaMovAbertoTerceiro(id)
        for idMov in idsMov:
            if controleTerceiroDao.consultaMovAbertoTerc(idMov[0]):
                return 3

        verificaMovimentoDao = VerificaMovimentoDao()
        consultaIds = ConsultaIdsDao()
        self.usuarioLogado = Usuario()
        self.terceiroAntigo = Terceiro()

        self.terceiroAntigo = manterTerceiroDao.mostrarTerceiroDetalhadoId(id)

        if session["grupo"] == "ADM":
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuario"])
        else:
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuarioVIG"])

        if verificaMovimentoDao.verificaMovimentoTerceiro(id):
            if manterTerceiroDao.inativarTerceiro(id):
                self.geraLogTerceiro("ACTIVE", observacao)
                return 2
        else:
            if manterTerceiroDao.excluirTerceiro(id):
                self.geraLogTerceiro("DELETE", observacao)
                return 1
        
        
    def mostraTerceiroDetalhadoId(self, id: int) -> Terceiro:
        manterTerceiroDao = ManterTerceiroDao()
        
        return manterTerceiroDao.mostrarTerceiroDetalhadoId(id)


    def incrementaCodigo(self) -> str:
        #########################################################################################
        # Essa função consulta o último código que tem no banco e imcrementa 1 para a próximo terceiro.
        
        # PARAMETROS:
        #   Não tem parametros.
        
        # RETORNOS:
        #   return codigo = Retorna o código com o imcrmento de um número.
        #   return "TE0001" = Retorna "TE0001" caso não exista registro no banco.
        #########################################################################################

        consultaIds = ConsultaIdsDao()
        respDao = consultaIds.consultaCodFinalTerc()
        if respDao:
            parteInt = int(respDao[0][2:])
            parteInt += 1
            codigo = f"{respDao[0][:2]}{str(parteInt).zfill(4)}"

            return codigo
        else:
            return "TE0001"


    def geraLogTerceiro(self, acao: str, observacao: str) -> None:
        #########################################################################################
        # Essa função gera log do INSERT, UPDATE e DELETE do tereceiro.
        
        # PARAMETROS:
        #   acao = Ação que foi efetuada.
        
        # RETORNOS:
        #   Não tem retorno.
        #########################################################################################

        log = Log()
        log.acao = acao
        log.dataHora = datetime.now()
        log.observacao = observacao
        log.usuario = self.usuarioLogado

        if acao == "INSERT":
            log.dadosAntigos = {"vazio": 0}
            log.dadosNovos = self.terceiroNovo.toJson()
        elif acao == "UPDATE":
            log.dadosAntigos = self.terceiroAntigo.toJson()
            log.dadosNovos = self.terceiroNovo.toJson()
        else:
            log.dadosAntigos = self.terceiroAntigo.toJson()
            log.dadosNovos = {"vazio": 0}

        logDao = GeraLogDao()
        logDao.inserirLogTerceiro(log)