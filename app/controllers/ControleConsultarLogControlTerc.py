from ..models.dao.ConsultaLogControlTercDao import ConsultaLogControlTercDao
from ..models.dao.ConsultaParametrosDao import ConsultaParametrosDao
from ..models.dao.ManterUsuarioDao import ManterUsuarioDao
from ..extensions.FiltrosJson import filtroDataHora
from dateutil.relativedelta import relativedelta
from ..models.entity.Log import Log
from datetime import datetime
import json as js

class ControleConsultarLogControlTerc:
    """
    Classe Controller para as funções de consulta de logs do controle de terceiros
    @author - Fabio
    @version - 1.0
    @since - 18/09/2023
    """

    def consultaLogControlTercEnt(self, acao: str) -> list[dict]:
        """
        Consulta e retorna uma lista de logs de inserção de tercerios de acordo com a data na tabela de parâmetros('PAR_MANUT_CONTROL_TERC').

        :return: Uma lista de dicionários contendo informações sobre os logs de inserção de tercerios.
            Cada dicionário possui tercerios "id", "dataHora", "acao", "resp" e "movTerc".
        """

        #Consulta a data na tabela de parametros para fazer a pesquisa apartir desta data
        consultaParametro = ConsultaParametrosDao()
        mesesAtras = consultaParametro.consultaParametros("PAR_MANUT_CONTROL_TERC")
        dataDe = datetime.now()
        dataDe = dataDe - relativedelta(months=mesesAtras)
        dataDe = dataDe.strftime("%Y-%m-01")

        consultaControleTercDao = ConsultaLogControlTercDao()
        respDao = consultaControleTercDao.consultaLogsControlTerc(dataDe, acao)
        listaLogs = []

        for log in respDao:
            dictLog = {
                "id": log.id_logTerc,
                "dataHora": filtroDataHora(log.lmte_dataHora),
                "acao": log.lmte_acao,
                "resp": log.nomeUser,
                "movTerc": js.loads(log.lmte_dadosAntigos.decode("utf-8")) if acao in ["UPDATE", "DELETE"] else js.loads(log.lmte_dadosNovos.decode("utf-8"))
            }

            listaLogs.append(dictLog)

        return listaLogs
        
        
    def consultaLogControlTercDetelhado(self, id: int) -> Log:
        """
        Consulta e retorna detalhes de um registro de log do controle de terceiros.

        :param id: O ID do registro de log de controle de terceiros.
        
        :return: Um objeto Log contendo detalhes do registro de log de controle de terceiros.
        """

        consultaControleTercDao = ConsultaLogControlTercDao()
        manterUsuarioDao = ManterUsuarioDao()
        respDao = consultaControleTercDao.consultaLogsControlTercDetalhado(id)
        
        usuario = manterUsuarioDao.consultarUsuarioDetalhado(respDao.lmte_idUsua)
        logControlChav = Log(id=respDao.id_logTerc, dataHora=respDao.lmte_dataHora, acao=respDao.lmte_acao, observacao=respDao.lmte_observacao, usuario=usuario)
        logControlChav.converteDictDadosAntigos(respDao.lmte_dadosAntigos)
        logControlChav.converteDictDadosNovos(respDao.lmte_dadosNovos)

        return logControlChav
