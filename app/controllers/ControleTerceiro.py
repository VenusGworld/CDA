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

class ControleTerceiro:
    """
    Classe Controller para funções relacionadas ao controle de Terceiro
    @author - Fabio
    @version - 1.0
    @since - 27/07/2023
    """

    def inserirEntrada(self, cpf: str, nome: str, empesa: str, placa: str, veiculo: str, motivo: str, pessoaVisit: str, dtEnt: str, hrEnt: str, acomps: list[dict]) -> bool:
        """
        Insere um movimento de entrada para um terceiro (visitante) no sistema.
        
        :param cpf: CPF do terceiro visitante.
        :param nome: Nome do terceiro visitante.
        :param empesa: Nome da empresa do terceiro visitante.
        :param placa: Placa do veículo do terceiro visitante.
        :param veiculo: Modelo do veículo do terceiro visitante.
        :param motivo: Motivo da visita do terceiro.
        :param pessoaVisit: Informações sobre a pessoa que visita (funcionário).
        :param dtEnt: Data de entrada no formato 'YYYY-MM-DD'.
        :param hrEnt: Hora de entrada no formato 'hh:mm'.
        :param acomps: Lista de dicionários contendo informações sobre acompanhantes (caso haja).
        """

        
        funcionario = Funcionario()
        self.usuarioLogado = Usuario()
        manterFuncionarioDao = ManterFuncionarioDao()
        funcionario = manterFuncionarioDao.consultarFuncionarioDetalhadoCracha(list(pessoaVisit.split())[0])
        self.movimentoTercNovo = MovimentoTerceiro(pessoaVisit=funcionario, empresa=empesa.upper().strip(), placa=placa.upper().strip(),
                                                   veiculo=veiculo.upper().strip(), motivo=motivo.upper().strip(), dataEnt=dtEnt.replace("-", ""),
                                                   horaEnt=hrEnt, delete=False) 
        
        pesquisaDao = PesquisaDao()
        manterTerceiroDao = ManterTerceiroDao()
        controleManterTerceiro = ControleManterTerceiro()
        terceiro = pesquisaDao.pesquisaCpfTercFormMov(''.join(filter(str.isdigit, cpf)))

        #Verifica se o terceiro exsite no banco
        if terceiro:
            terceiroMov = manterTerceiroDao.consultarTerceiroDetalhadoCpf(''.join(filter(str.isdigit, cpf)))
            self.movimentoTercNovo.terceiro = terceiroMov
        else:
            #Inclui o terceiro no banco
            codigo = controleManterTerceiro.incrementaCodigoTerc()
            controleManterTerceiro.incluirTerceiro(codigo, nome.upper().strip(), cpf)
            terceiroMov = manterTerceiroDao.consultarTerceiroDetalhadoCpf(''.join(filter(str.isdigit, cpf)))
            self.movimentoTercNovo.terceiro = terceiroMov

        listaAcomps = []
        for acomp in acomps:
            acompanhante = pesquisaDao.pesquisaCpfTercFormMov(''.join(filter(str.isdigit, acomp["cpf"])))
            #Verifica se o terceiro exsite no banco
            if acompanhante:
                acompMov = manterTerceiroDao.consultarTerceiroDetalhadoCpf(''.join(filter(str.isdigit, acomp["cpf"])))
                listaAcomps.append(acompMov)
            else:
                #Inclui o terceiro no banco
                codigo = controleManterTerceiro.incrementaCodigoTerc()
                controleManterTerceiro.incluirTerceiro(codigo, acomp["nome"].upper().strip(), acomp["cpf"])
                acompMov = manterTerceiroDao.consultarTerceiroDetalhadoCpf(''.join(filter(str.isdigit, acomp["cpf"])))
                listaAcomps.append(acompMov)

        self.movimentoTercNovo.acomps = listaAcomps
        controleTerceiroDao = ControleTerceiroDao()
        consultaIdsDao = ConsultaIdsDao()
        controleTerceiroDao.inserirEntrada(self.movimentoTercNovo)
        self.movimentoTercNovo.id = consultaIdsDao.consultaIdFinalMovTerc()

        #Inclui o id do terceiro e do movimento na tabela de relação entra as duas tabelas
        controleTerceiroDao.inserirVisitante(self.movimentoTercNovo.terceiro, self.movimentoTercNovo)
        if len(listaAcomps) != 0:
            for acomp in listaAcomps:
                controleTerceiroDao.inserirVisitante(acomp, self.movimentoTercNovo)
        
        consultaIds = ConsultaIdsDao()
        #Verifica se o usuário que efetuou a acão é do grupo ADM
        if session["grupo"] == "ADM":
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuario"])
        else:
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuarioVIG"])

        self.geraLogControleTerceiro("ENTRADA", "")

        return True
    

    def consultaMovTercDetalhado(self, id: int) -> MovimentoTerceiro:
        """
        Consulta e retorna os detalhes de um movimento de terceiro específico.

        :param id: O ID do movimento de terceiro a ser consultado.

        :return: Uma instância de MovimentoTerceiro contendo os detalhes do movimento.
        """

        controleTerceiroDao = ControleTerceiroDao()
        manterFuncionarioDao = ManterFuncionarioDao()
        manterTerceiroDao = ManterTerceiroDao()
        terceiroDao = TerceiroDao()
        movimento = controleTerceiroDao.consultaMovTercDetalhado(id)

        funcionario = manterFuncionarioDao.consultarFuncionarioDetalhado(controleTerceiroDao.consultaIdFuncMovTerc(movimento.id))
        movimento.pessoaVisit = funcionario

        listaTerc = []
        #Conulta dos IDs dos terceiros que fizeram as visita
        ids = terceiroDao.terceirosMovimento(movimento.id)
        if len(ids) != 0:
            for i, id in enumerate(ids):
                if i == 0:
                    movimento.terceiro = manterTerceiroDao.consultarTerceiroDetalhadoId(id)
                else:
                    listaTerc.append(manterTerceiroDao.consultarTerceiroDetalhadoId(id))

        movimento.acomps = listaTerc

        return movimento


    def inserirSaida(self, id: int, dataSaid: str, horaSaid: str, cpf: str, acomps: list, cracha: str) -> bool:
        """
        Insere um registro de saída para um movimento de terceiro específico.

        :param id: O ID do movimento de terceiro.
        :param dataSaid: Data da saída no formato 'YYYY-MM-DD'.
        :param horaSaid: Hora da saída no formato 'HH:MM'.
        :param cpf: CPF do terceiro visitante.
        :param acomps: Lista de dicionários contendo informações sobre acompanhantes (caso haja).
        :param cracha: Número do crachá do funcionário visitado.
        """
        
        controleTerceiroDao = ControleTerceiroDao()
        self.usuarioLogado = Usuario()
        manterTerceiroDao = ManterTerceiroDao()
        manterFuncionario = ManterFuncionarioDao()

        self.movimentoTercNovo = controleTerceiroDao.consultaMovTercDetalhado(id)
        self.movimentoTercNovo.terceiro = manterTerceiroDao.consultarTerceiroDetalhadoCpf(''.join(filter(str.isdigit, cpf)))
        self.movimentoTercNovo.pessoaVisit = manterFuncionario.consultarFuncionarioDetalhadoCracha(cracha)
        self.movimentoTercNovo.dataSai = dataSaid.replace("-", "")
        self.movimentoTercNovo.horaSai = horaSaid

        listaAcomps = []
        if len(acomps) > 0:
            for acomp in acomps:
                acompanhante = manterTerceiroDao.consultarTerceiroDetalhadoCpf(''.join(filter(str.isdigit, acomp["cpf"])))
                listaAcomps.append(acompanhante)

        self.movimentoTercNovo.acomps = listaAcomps

        if controleTerceiroDao.inserirSaida(self.movimentoTercNovo):
            consultaIds = ConsultaIdsDao()
            #Verifica se o usuário que efetuou a acão é do grupo ADM
            if session["grupo"] == "ADM":
                self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuario"])
            else:
                self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuarioVIG"])

            self.geraLogControleTerceiro("SAIDA", "")
        
        return True


    def consultaTerceirosEntrada(self) -> list[dict]:
        """
        Consulta e retorna uma lista de terceiros com entradas registradas.

        :return: Uma lista de dicionários contendo informações sobre terceiros com entradas.
            Cada dicionário possui chaves "id", "nomeTerc", "entrada", "visitado" e "empresa".
        """
        
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
        """
        Gera um registro de log para ações relacionadas ao controle de terceiros.

        :param acao: Ação realizada (ENTRADA, SAIDA, UPDATE, DELETE).
        :param observacao: Observações adicionais sobre a ação (obrigatorio para usuários do grupo VIG).

        :return: Nenhum valor é retornado.
        """

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