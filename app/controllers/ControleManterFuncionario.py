from ..models.dao.ManterFuncionarioDao import ManterFuncionarioDao
from ..models.dao.ConsultaIdsDao import ConsultaIds
from ..models.dao.GeraLogDao import GeraLogDao
from ..models.entity.Funcionario import Funcionario
from ..models.entity.Usuario import Usuario
from ..models.entity.Log import Log
from datetime import datetime
from flask import session


class ControleManterFuncionario:

    def mostarFuncionarios(self) -> list[dict]:
        manterFuncionarioDao = ManterFuncionarioDao()
        respDao = manterFuncionarioDao.mostarFuncionarios()
        listaFuncionarios = []
        for funcionario in respDao:
            dicFunc ={
                "id": funcionario.id_Funcionarios,
                "cracha": funcionario.fu_cracha,
                "nome": funcionario.fu_nome,
                "maquina": funcionario.fu_maquina,
                "gerente": "SIM" if funcionario.fu_gerente else "NÃO"
            }

            listaFuncionarios.append(dicFunc)
        
        return listaFuncionarios


    def mostraFuncionarioDetalhado(self, id: int) -> Funcionario:
        manterFuncionarioDao = ManterFuncionarioDao()
        respDao = manterFuncionarioDao.mostarFuncionarioDetalhado(id)

        return respDao
    
    def incluirFuncionario(self, nome: str, cracha: str, maquina: str, gerente: bool) -> bool:
        self.funcionarioNovo = Funcionario()
        self.usuarioLogado = Usuario()
        self.funcionarioNovo.cracha = cracha
        self.funcionarioNovo.nome = nome
        self.funcionarioNovo.maquina = maquina
        self.funcionarioNovo.gerente = gerente
        self.funcionarioNovo.ativo = False
        self.funcionarioNovo.delete = False

        self.usuarioLogado = Usuario()

        manterFuncionarioDao = ManterFuncionarioDao()
        consultaIdUser = ConsultaIds()
        if manterFuncionarioDao.inserirFuncionario(self.funcionarioNovo): #Verifica o retorno do banco
            consultaIdUser = ConsultaIds()
            #Consulta id do usuário logado
            self.usuarioLogado.id = consultaIdUser.consultaIdUserLogado(session["usuario"])
            #Consulta o ultimo id da tabela
            self.funcionarioNovo.id = consultaIdUser.consultaIdFinalUser()
            #Gera Log
            self.geraLogFuncionario("INSERT")
            return True
        else:
            return False
    

    def editarFuncionario(self, id: int, nome: str, cracha: str, maquina: str, gerente: bool):
        self.funcionarioNovo = Funcionario()
        self.usuarioLogado = Usuario()
        self.funcionarioAntigo = Funcionario()
        manterFuncionarioDao = ManterFuncionarioDao()
        consultaIdUser = ConsultaIds()

        self.funcionarioAntigo = manterFuncionarioDao.mostarFuncionarioDetalhado(id)

        self.funcionarioNovo.id = id
        self.funcionarioNovo.cracha = cracha
        self.funcionarioNovo.nome = nome
        self.funcionarioNovo.maquina = maquina
        self.funcionarioNovo.gerente = gerente
        self.funcionarioNovo.ativo = False
        self.funcionarioNovo.delete = False

        if manterFuncionarioDao.editarFuncionario(self.funcionarioNovo):
            #Consulta id do usuário logado
            self.usuarioLogado.id = consultaIdUser.consultaIdUserLogado(session["usuario"])
            #Gera Log
            self.geraLogFuncionario("UPDATE")
            return True
        

    def geraLogFuncionario(self, acao: str):
        #########################################################################################
        # Essa função gera log do INSERT, UPDATE e DELETE do usuário.
        
        # PARAMETROS:
        #   acao = Ação que foi efetuada.
        
        # RETORNOS:
        #   Não tem retorno.
        #########################################################################################

        log = Log()
        log.acao = acao
        log.dataHora = datetime.now()
        log.observacao = ""
        log.usuario = self.usuarioLogado

        if acao == "INSERT":
            log.dadosAntigos = {"vazio": 0}
            log.dadosNovos = self.funcionarioNovo.toJson()
        elif acao == "UPDATE":
            log.dadosAntigos = self.funcionarioAntigo.toJson()
            log.dadosNovos = self.funcionarioNovo.toJson()
        else:
            log.dadosAntigos = self.funcionarioAntigo.toJson()
            log.dadosNovos = {"vazio": 0}

        logDao = GeraLogDao()
        logDao.inserirLogFuncionario(log)
