from ..models.dao.ConsultaParametrosDao import ConsultaParametrosDao
from ..models.dao.ConsultaLogTercDao import ConsultaLogTercDao
from ..models.dao.ManterUsuarioDao import ManterUsuarioDao
from ..extensions.FiltrosJson import filtroDataHora
from dateutil.relativedelta import relativedelta
from ..models.entity.Log import Log
from datetime import datetime
import json as js

class ControleConsultarLogTerc:
    """
    Classe Controller para as funções de consulta de logs do terceiro
    @author - Fabio
    @version - 1.0
    @since - 05/09/2023
    """

    def consultaLogTerc(self, acao: str) -> list[dict]:
        """
        Consulta e retorna uma lista de logs de inserção de tercerios de acordo com a data na tabela de parâmetros('PAR_LOG_MANT_TERC').

        :return: Uma lista de dicionários contendo informações sobre os logs de inserção de tercerios.
            Cada dicionário possui tercerios "id", "dataHora", "acao", "resp" e "terc".
        """

        #Consulta a data na tabela de parametros para fazer a pesquisa apartir desta data
        consultaParametro = ConsultaParametrosDao()
        mesesAtras = consultaParametro.consultaParametros("PAR_LOG_MANT_TERC")
        dataDe = datetime.now()
        dataDe = dataDe - relativedelta(months=mesesAtras)
        dataDe = dataDe.strftime("%Y-%m-01")

        consultaLogDao = ConsultaLogTercDao()
        respDao = consultaLogDao.consultaLogsTerc(dataDe, acao)
        listaLogs = []

        for log in respDao:
            dictLog = {
                "id": log.id_logTerc,
                "dataHora": filtroDataHora(log.lte_dataHora),
                "acao": log.lte_acao,
                "resp": log.nomeUser,
                "terc": js.loads(log.lte_dadosAntigos.decode("utf-8")) if acao in ["ACTIVE", "DELETE"] else js.loads(log.lte_dadosNovos.decode("utf-8"))
            }

            listaLogs.append(dictLog)

        return listaLogs     
        
        
    def consultaLogTercDetelhado(self, id: int):
        """
        Consulta e retorna detalhes de um registro de log de terceiro específico.

        :param id: O ID do registro de log de terceiro.
        
        :return: Um objeto Log contendo detalhes do registro de log de terceiro.
        """

        consultaLogDao = ConsultaLogTercDao()
        manterUsuarioDao = ManterUsuarioDao()
        respDao = consultaLogDao.consultaLogsTercDetalhado(id)
        
        usuario = manterUsuarioDao.consultarUsuarioDetalhado(respDao.lte_idUsua)
        logUser = Log(id=respDao.id_logTerc, dataHora=respDao.lte_dataHora, acao=respDao.lte_acao, observacao=respDao.lte_observacao, usuario=usuario)
        logUser.converteDictDadosAntigos(respDao.lte_dadosAntigos)
        logUser.converteDictDadosNovos(respDao.lte_dadosNovos)

        return logUser
