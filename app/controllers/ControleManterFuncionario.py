from ..models.dao.ManterFuncionarioDao import ManterFuncionarioDao
from ..models.dao.VerificamovimentoDao import VerificaMovimentoDao
from ..models.dao.ConsultaIdsDao import ConsultaIdsDao
from ..models.entity.Funcionario import Funcionario
from ..models.dao.GeraLogDao import GeraLogDao
from ..models.entity.Usuario import Usuario
from ..models.entity.Log import Log
from datetime import datetime
from flask import session


class ControleManterFuncionario:

    def mostarFuncionarios(self) -> list[dict]:
        #########################################################################################
        # Essa função recupera os dados dos funcionários de um objeto "ManterFuncionarioDao" 
        # e cria uma lista de dicionários, onde cada dicionário representa um funcionário 
        # e contém seu ID, cracha, nome, maquina e se é gerente ou não.
        
        # PARAMETROS:
        #   Não tem parametros.
        
        # RETORNOS:
        #   return listaFuncionarios = Retorna uma lista com dicinário dos funcionários 
        #     que retornaram do banco.
        #########################################################################################

        manterFuncionarioDao = ManterFuncionarioDao()
        respDao = manterFuncionarioDao.mostarFuncionarios()
        listaFuncionarios = []
        for funcionario in respDao:
            dicFunc ={
                "id": funcionario.id_funcionarios,
                "cracha": funcionario.fu_cracha,
                "nome": funcionario.fu_nome,
                "maquina": funcionario.fu_maquina,
                "gerente": "SIM" if funcionario.fu_gerente else "NÃO"
            }

            listaFuncionarios.append(dicFunc)
        
        return listaFuncionarios


    def mostraFuncionarioDetalhado(self, id: int) -> Funcionario:
        #########################################################################################
        # Essa função recebe um ID como entarda e utiliza-o para buscar informações detalhadas
        # sobre um funcionário específico a partir de um objeto "ManterUsuarioDao".
        
        # PARAMETROS:
        #   id = ID do funcionário que foi slecionado.
        
        # RETORNOS:
        #   return funcionario = Retorna as informações detalhadas do funcionário solicitado.
        #########################################################################################

        manterFuncionarioDao = ManterFuncionarioDao()
        funcionario = manterFuncionarioDao.mostarFuncionarioDetalhado(id)

        return funcionario
    

    def incluirFuncionario(self, nome: str, cracha: str, maquina: str, gerente: bool) -> bool:
        #########################################################################################
        # Essa função recebe os dados do funcionário a ser incluido.
        
        # PARAMETROS:
        #   nome = Nome do funcionário informado no form de cadastro;
        #   cracha = Cracha do funcionário informado no form de cadastro;
        #   maquina = O nome da máquina do funcionário informado no form de cadastro;
        #   gerente = Um idenfificador para saber se o funcionário é gerente.
        
        # RETORNOS:
        #   return True = Retorna True em caso de sucesso na inclusão do funcionário;
        #   return False = Retorna False em caso de fracasso na inclusão do funcionário.
        #########################################################################################

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
        consultaIdUser = ConsultaIdsDao()
        if manterFuncionarioDao.inserirFuncionario(self.funcionarioNovo): #Verifica o retorno do banco
            consultaIdUser = ConsultaIdsDao()
            #Consulta id do usuário logado
            self.usuarioLogado.id = consultaIdUser.consultaIdUserLogado(session["usuario"])
            #Consulta o ultimo id da tabela
            self.funcionarioNovo.id = consultaIdUser.consultaIdFinalFunc()
            #Gera Log
            self.geraLogFuncionario("INSERT")
            return True
        else:
            return False
    

    def editarFuncionario(self, id: int, nome: str, cracha: str, maquina: str, gerente: bool):
        #########################################################################################
        # Essa função recebe os dados de um funcionário existente para a alterção.
        
        # PARAMETROS:
        #   id = ID do funcionário que foi selecionado para a alterção;
        #   nome = Nome do funcionário informado no form de alterção;
        #   cracha = Cracha do funcionário informado no form de alterção;
        #   maquina = Nome da máquina do funcionário informado no form de alterção;
        #   gerente = Um idenfificador para saber se o funcionário é gerente.
        
        # RETORNOS:
        #   return True = Retorna True em caso de sucesso na alteração do funcionário.
        #########################################################################################


        self.funcionarioNovo = Funcionario()
        self.usuarioLogado = Usuario()
        self.funcionarioAntigo = Funcionario()
        manterFuncionarioDao = ManterFuncionarioDao()
        consultaIdUser = ConsultaIdsDao()

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


    def excluirFuncionario(self, id: int) -> int:
        #########################################################################################
        # Essa função recebe o id do usuário a ser excluido, mas caso o usuário já tenha efetuado
        # alguma movimentação no sistema ele é desativado.
        
        # PARAMETROS:
        #   id = ID do usário que foi selecionado para a exclusão ou desativação.
        
        # RETORNOS:
        #   return 1 = Retorna 1 em caso de sucesso na exclusão do funcionário;
        #   return 2 = Retorna 2 em caso de sucesso na inativação do funcionário.
        #########################################################################################

        manterFuncionarioDao = ManterFuncionarioDao()
        verificaMovimento = VerificaMovimentoDao()
        consultaIdUser = ConsultaIdsDao()
        self.usuarioLogado = Usuario()
        self.funcionarioAntigo = Funcionario()

        self.funcionarioAntigo = manterFuncionarioDao.mostarFuncionarioDetalhado(id)

        self.usuarioLogado.id = consultaIdUser.consultaIdUserLogado(session["usuario"])

        if verificaMovimento.verificaMovimentoFuncionario(id):
            if manterFuncionarioDao.inativarFuncionario(id):
                self.geraLogFuncionario("ACTIVE")
                return 2
        else:
            if manterFuncionarioDao.excluirFuncionario(id):
                self.geraLogFuncionario("DELETE")
                return 1  


    def geraLogFuncionario(self, acao: str):
        #########################################################################################
        # Essa função gera log do INSERT, UPDATE e DELETE do funcionário.
        
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
