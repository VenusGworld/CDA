from ..models.dao.VerificaMovimentoDao import VerificaMovimentoDao
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

class ControleManterTerceiro:
    """
    Classe Controller para funções relacionadas ao CRUD de terceiro
    @author - Fabio
    @version - 1.0
    @since - 26/07/2023
    """

    def consultarTerceiros(self) -> list[dict]:
        """
        Consulta e retorna uma lista de dicionários contendo informações resumidas de todos os terceiros.

        :return: Uma lista de dicionários contendo informações sobre os terceiro.
            Cada dicionário possui chaves "id", "codigo", "nome" e "cpf".
        """
        
        manterTerceiroDao = ManterTerceiroDao()
        respDao = manterTerceiroDao.consultarTerceiros()
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
    

    def consultaTerceiroDetalhadoId(self, id: int) -> Terceiro:
        """
        Consulta os detalhes de um terceiro pelo ID.

        :param id: O ID do terceiro a ser consultado.

        :return: Um objeto da classe Terceiro com os detalhes do terceiro.
        """

        manterTerceiroDao = ManterTerceiroDao()
        terceiro = manterTerceiroDao.consultarTerceiroDetalhadoId(id)
        
        return terceiro
    

    def consultaTerceiroDetalhadoCodigo(self, codigo: str) -> Terceiro:
        """
        Consulta os detalhes de um terceiro pelo código.

        :param codigo: O código do terceiro a ser consultado.

        :return: Um objeto da classe Terceiro com os detalhes do terceiro.
        """

        manterTerceiroDao = ManterTerceiroDao()
        terceiro = manterTerceiroDao.consultarTerceiroDetalhadoCodigo(codigo)
        
        return terceiro


    def incluirTerceiro(self, codigo: str, nome: str, cpf: str) -> bool:
        """
        Inclui um novo terceiro no sistema.

        :param codigo: O código do terceiro a ser incluído.
        :param nome: O nome do terceiro.
        :param cpf: O CPF do terceiro.

        :return: True se a inclusão for bem-sucedida, False caso contrário.
        """

        manterTerceiroDao = ManterTerceiroDao()
        consultaIds = ConsultaIdsDao()
        self.usuarioLogado = Usuario()

        cpf = ''.join(filter(str.isdigit, cpf))
        self.terceiroNovo = Terceiro(codigo=codigo, nome=nome, cpf=cpf, ativo=False, delete=False)

        #Verifica se o usuário que efetuou a acão é do grupo ADM
        if session["grupo"] == "ADM":
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuario"])
        else:
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuarioVIG"])
        
        if manterTerceiroDao.incluirTerceiro(self.terceiroNovo):
            self.terceiroNovo.id = consultaIds.consultaIdFinalTerc()
            self.geraLogTerceiro("INSERT", "")

        return True
        

    def editarTerceiro(self, id: int, codigo: str, cpf: str, nome: str, observacao: str) -> bool:
        """
        Edita as informações de um terceiro no sistema.

        :param id: O ID do terceiro a ser editado.
        :param codigo: O novo código do terceiro.
        :param cpf: O novo CPF do terceiro.
        :param nome: O novo nome do terceiro.
        :param observacao: A observação relacionada à alteração da chave (obrigatorio para usuários do grupo VIG).

        :return: True se a edição for bem-sucedida, False caso contrário.
        """

        manterTerceiroDao = ManterTerceiroDao()
        consultaIds = ConsultaIdsDao()
        self.usuarioLogado = Usuario()
        self.terceiroAntigo = Terceiro()

        self.terceiroAntigo = manterTerceiroDao.consultarTerceiroDetalhadoId(id)

        cpf = ''.join(filter(str.isdigit, cpf))
        self.terceiroNovo = Terceiro(id=id, codigo=codigo, nome=nome, cpf=cpf, ativo=False, delete=False)

        #Verifica se o usuário que efetuou a acão é do grupo ADM
        if session["grupo"] == "ADM":
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuario"])
        else:
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuarioVIG"])

        manterTerceiroDao.editarTerceiro(self.terceiroNovo)
        self.geraLogTerceiro("UPDATE", observacao)

        return True
    

    def excluirTerceiro(self, id: int, observacao: str) -> int:
        """
        Exclui ou Inativa um terceiro do sistema.

        :param id: O ID do terceiro a ser excluído.
        :param observacao: A observação relacionada à exclusão da chave (obrigatorio para usuários do grupo VIG).

        :return: Um valor inteiro representando o resultado da exclusão:
            - 1: terceiro excluído com sucesso.
            - 2: terceiro inativado (quando funcionário tem movimentação no sistema).
            - 3: Existem movimentos abertos associados ao terceiro.
        """

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

        self.terceiroAntigo = manterTerceiroDao.consultarTerceiroDetalhadoId(id)

        #Verifica se o usuário que efetuou a acão é do grupo ADM
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
        
        
    def incrementaCodigoTerc(self) -> str:
        """
        Gera e retorna um novo código para um terceiro, incrementando o último código existente.

        :return: Um novo código para um terceiro.
        """
        
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
        """
        Gera um registro de log para ações relacionadas ao manter terceiro.

        :param acao: Ação realizada (INSERT, UPDATE, DELETE).

        :return: Nenhum valor é retornado.
        """

        log = Log(acao=acao, dataHora=datetime.now(), observacao=observacao, usuario=self.usuarioLogado)

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