from ..models.dao.VerificamovimentoDao import VerificaMovimentoDao
from ..models.dao.ControleChaveDao import ControleChaveDao
from ..models.dao.ManterChaveDao import ManterChaveDao
from ..models.dao.ConsultaIdsDao import ConsultaIdsDao
from ..models.dao.GeraLogDao import GeraLogDao
from ..models.entity.Usuario import Usuario
from ..models.entity.Chave import Chave
from ..models.entity.Log import Log
from datetime import datetime
from flask import session

"""
Classe Controller para o CRUD da Chave
@author - Fabio
@version - 1.0
@since - 04/07/2023
"""

class ControleManterChave:

    def mostraChaves(self) -> list[dict]:
        #########################################################################################
        # Essa função recupera os dados das chaves de um objeto "ManterChaveDao" e cria uma 
        # lista de dicionários, onde cada dicionário representa uma chave e contém seu ID, código 
        # e nome.
        
        # PARAMETROS:
        #   Não tem parametros.
        
        # RETORNOS:
        #   return listaChaves = Retorna uma lista com dicinário das chaves que retornaram do banco.
        #########################################################################################
        
        manterChaveDao = ManterChaveDao()
        respDao = manterChaveDao.mostraChaves()
        listaChaves = []
        for chave in respDao:
            dicChave ={
                "id": chave.id_chave,
                "codigo": chave.ch_codigo,
                "nome": chave.ch_nome
            }

            listaChaves.append(dicChave)
        
        return listaChaves
    
    
    def mostraChaveDetalhadaId(self, id: int) -> Chave:
        manterChaveDao = ManterChaveDao()
        chave = manterChaveDao.mostrarChaveDetalhadaId(id)

        return chave
    

    def incluirChave(self, codigo: str, nome: str) -> bool:
        #########################################################################################
        # Essa função recebe os dados da chave a ser incluida.
        
        # PARAMETROS:
        #   nome = Nome da chave informado no form de cadastro;
        #   codigo = Código da chave gerado pelo sistma.
        
        # RETORNOS:
        #   return True = Retorna True em caso de sucesso na inclusão da chave.
        #########################################################################################

        manterChaveDao = ManterChaveDao()
        self.chaveNova = Chave()
        consultaIds = ConsultaIdsDao()
        self.usuarioLogado = Usuario()

        self.chaveNova .codigo = codigo
        self.chaveNova .nome = nome
        self.chaveNova .ativo = False
        self.chaveNova .delete = False

        if session["grupo"] == "ADM":
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuario"])
        else:
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuarioVIG"])
            
        if manterChaveDao.incluirChave(self.chaveNova):
            self.chaveNova.id = manterChaveDao.consultaUltimoId()
            self.geraLogChave("INSERT", "")
            return True
        
    
    def editarChave(self, id: int, codigo: str, nome: str, observacao: str) -> bool:
        #########################################################################################
        # Essa função recebe os dados de uma chave existente para a alterção.
        
        # PARAMETROS:
        #   id = ID da chave que foi selecionado para a alterção;
        #   codigo = Código da chave informado no form de alteração;
        #   nome = Nome da chave informado no form de alteração;
        #   observacao = Observação da alteração da chave informado no form de alteração.
        
        # RETORNOS:
        #   return True = Retorna True em caso de sucesso na alteração da chave.
        #########################################################################################

        manterChaveDao = ManterChaveDao()
        consultaIds = ConsultaIdsDao()
        self.usuarioLogado = Usuario()
        self.chaveNova = Chave()
        self.chaveAntiga = Chave()

        self.chaveAntiga = manterChaveDao.mostrarChaveDetalhadaId(id)
        
        self.chaveNova.id = id
        self.chaveNova.codigo = codigo
        self.chaveNova.nome = nome
        self.chaveNova.ativo = False
        self.chaveNova.delete = False

        if session["grupo"] == "ADM":
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuario"])
        else:
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuarioVIG"])

        if manterChaveDao.editarChave(self.chaveNova):
            self.geraLogChave("UPDATE", observacao)

            return True
        
    
    def excluirChave(self, id: int, observacao: str) -> int:
        #########################################################################################
        # Essa função recebe o id da chave a ser excluida, mas caso a chave já tenha sido usada 
        # para movimentação no sistema ela é desativada.
        
        # PARAMETROS:
        #   id = ID do usário que foi selecionado para a exclusão ou desativação.
        
        # RETORNOS:
        #   return 1 = Retorna 2 em caso de sucesso na exclusão/desativação do usuário.;
        #   return 2 = Retorna 2 em caso de sucesso na exclusão/desativação do usuário.
        #########################################################################################

        manterChaveDao = ManterChaveDao()
        controleChaveDao = ControleChaveDao()

        idsMov = controleChaveDao.verificaMovAbertoChave(id)
        for idMov in idsMov:
            if controleChaveDao.consultaMovAbertoChave(idMov[0]):
                return 3
            
        verificaMovimentoDao = VerificaMovimentoDao()
        consultaIds = ConsultaIdsDao()
        self.usuarioLogado = Usuario()
        self.chaveAntiga = Chave()

        self.chaveAntiga = manterChaveDao.mostrarChaveDetalhadaId(id)

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
    

    def incrementaCodigo(self) -> str:
        #########################################################################################
        # Essa função consulta o último código que tem no banco e imcrementa 1 para a próxima chave.
        
        # PARAMETROS:
        #   Não tem parametros.
        
        # RETORNOS:
        #   return codigo = Retorna o código com o imcrmento de um número.
        #   return "CH0001" = Retorna "CH0001" caso não exista registro no banco.
        #########################################################################################

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
        #########################################################################################
        # Essa função gera log do INSERT, UPDATE e DELETE da chave.
        
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
            log.dadosNovos = self.chaveNova.toJson()
        elif acao == "UPDATE":
            log.dadosAntigos = self.chaveAntiga.toJson()
            log.dadosNovos = self.chaveNova.toJson()
        else:
            log.dadosAntigos = self.chaveAntiga.toJson()
            log.dadosNovos = {"vazio": 0}

        logDao = GeraLogDao()
        logDao.inserirLogChave(log)