from ..models.dao.ConsultaLogControlGerDao import ConsultaLogControlGerDao
from ..models.dao.ConsultaParametrosDao import ConsultaParametrosDao
from ..models.dao.ManterUsuarioDao import ManterUsuarioDao
from ..extensions.FiltrosJson import filtroDataHora
from dateutil.relativedelta import relativedelta
from ..models.entity.Log import Log
from datetime import datetime
import json as js

class ControleConsultarLogControlGer:
    """
    Classe Controller para as funções de consulta de logs do controle de gerentes
    @author - Fabio
    @version - 1.0
    @since - 18/09/2023
    """

    def consultaLogControlGer(self, acao: str) -> list[dict]:
        """
        Consulta e retorna uma lista de logs de inserção de gerentes de acordo com a data na tabela de parâmetros('PAR_MANUT_CONTROL_GER').

        :return: Uma lista de dicionários contendo informações sobre os logs de inserção de gerentes.
            Cada dicionário possui as chaves "id", "dataHora", "acao", "resp" e "movGer".
        """

        #Consulta a data na tabela de parametros para fazer a pesquisa apartir desta data
        consultaParametro = ConsultaParametrosDao()
        mesesAtras = consultaParametro.consultaParametros("PAR_MANUT_CONTROL_GER")
        dataDe = datetime.now()
        dataDe = dataDe - relativedelta(months=mesesAtras)
        dataDe = dataDe.strftime("%Y-%m-01")

        consultaControleGerDao = ConsultaLogControlGerDao()
        respDao = consultaControleGerDao.consultaLogsControlGer(dataDe, acao)
        listaLogs = []

        for log in respDao:
            dictLog = {
                "id": log.id_logGere,
                "dataHora": filtroDataHora(log.lmge_dataHora),
                "acao": log.lmge_acao,
                "resp": log.nomeUser,
                "movGer": js.loads(log.lmge_dadosAntigos.decode("utf-8")) if acao in ["UPDATE", "DELETE"] else js.loads(log.lmge_dadosNovos.decode("utf-8")) 
            }

            listaLogs.append(dictLog)

        return listaLogs    
        
        
    def consultaLogControlGerDetelhado(self, id: int) -> Log:
        """
        Consulta e retorna detalhes de um registro de log do controle de dgerentes.

        :param id: O ID do registro de log de controle de dgerentes.
        
        :return: Um objeto Log contendo detalhes do registro de log de controle de dgerentes.
        """

        consultaControleGerDao = ConsultaLogControlGerDao()
        manterUsuarioDao = ManterUsuarioDao()
        respDao = consultaControleGerDao.consultaLogsControlGerDetalhado(id)
        
        usuario = manterUsuarioDao.consultarUsuarioDetalhado(respDao.lmge_idUsua)
        logControlChav = Log(id=respDao.id_logGere, dataHora=respDao.lmge_dataHora, acao=respDao.lmge_acao, observacao=respDao.lmge_observacao, usuario=usuario)
        logControlChav.converteDictDadosAntigos(respDao.lmge_dadosAntigos)
        logControlChav.converteDictDadosNovos(respDao.lmge_dadosNovos)

        return logControlChav
