from ..models.dao.ConsultaParametrosDao import ConsultaParametrosDao
from ..models.dao.ConsultaLogFuncDao import ConsultaLogFuncDao
from ..models.dao.ManterUsuarioDao import ManterUsuarioDao
from ..extensions.FiltrosJson import filtroDataHora
from dateutil.relativedelta import relativedelta
from ..models.entity.Log import Log
from datetime import datetime
import json as js

class ControleConsultarLogFunc:
    """
    Classe Controller para as funções de consulta de logs do funcionário
    @author - Fabio
    @version - 1.0
    @since - 16/08/2023
    """

    def consultaLogFuncInsert(self) -> list[dict]:
        """
        Consulta e retorna uma lista de logs de inserção de funcionários de acordo com a data na tabela de parâmetros('PAR_LOG_MANT_FUNC').

        :return: Uma lista de dicionários contendo informações sobre os logs de inserção de funcionários.
            Cada dicionário possui chaves "id", "dataHora", "acao", "resp" e "func".
        """

        #Consulta a data na tabela de parametros para fazer a pesquisa apartir desta data
        consultaParametro = ConsultaParametrosDao()
        mesesAtras = consultaParametro.consultaParametros("PAR_LOG_MANT_FUNC")
        dataDe = datetime.now()
        dataDe = dataDe - relativedelta(months=mesesAtras)
        dataDe = dataDe.strftime("%Y-%m-01")

        consultaLogDao = ConsultaLogFuncDao()
        respDao = consultaLogDao.consultaLogsFuncInsert(dataDe)
        listaLogs = []

        for log in respDao:
            dictLog = {
                "id": log.id_logFunc,
                "dataHora": filtroDataHora(log.lfu_dataHora),
                "acao": log.lfu_acao,
                "resp": log.nomeUser,
                "func": js.loads(log.lfu_dadosNovos.decode("utf-8"))
            }

            listaLogs.append(dictLog)

        return listaLogs    


    def consultaLogFuncUpdate(self) -> list[dict]:
        """
        Consulta e retorna uma lista de logs de alteração de funcionários de acordo com a data na tabela de parâmetros('PAR_LOG_MANT_FUNC').

        :return: Uma lista de dicionários contendo informações sobre os logs de alteração de funcionários.
            Cada dicionário possui chaves "id", "dataHora", "acao", "resp" e "func".
        """

        #Consulta a data na tabela de parametros para fazer a pesquisa apartir desta data
        consultaParametro = ConsultaParametrosDao()
        mesesAtras = consultaParametro.consultaParametros("PAR_LOG_MANT_FUNC")
        dataDe = datetime.now()
        dataDe = dataDe - relativedelta(months=mesesAtras)
        dataDe = dataDe.strftime("%Y-%m-01")

        consultaLogDao = ConsultaLogFuncDao()
        respDao = consultaLogDao.consultaLogsFuncUpdate(dataDe)
        listaLogs = []

        for log in respDao:
            dictLog = {
                "id": log.id_logFunc,
                "dataHora": filtroDataHora(log.lfu_dataHora),
                "acao": log.lfu_acao,
                "resp": log.nomeUser,
                "func": js.loads(log.lfu_dadosNovos.decode("utf-8"))
            }

            listaLogs.append(dictLog)

        return listaLogs 


    def consultaLogFuncDelete(self) -> list[dict]:
        """
        Consulta e retorna uma lista de logs de exclusão de funcionários de acordo com a data na tabela de parâmetros('PAR_LOG_MANT_FUNC').

        :return: Uma lista de dicionários contendo informações sobre os logs de exclusão de funcionários.
            Cada dicionário possui chaves "id", "dataHora", "acao", "resp" e "func".
        """

        #Consulta a data na tabela de parametros para fazer a pesquisa apartir desta data
        consultaParametro = ConsultaParametrosDao()
        mesesAtras = consultaParametro.consultaParametros("PAR_LOG_MANT_FUNC")
        dataDe = datetime.now()
        dataDe = dataDe - relativedelta(months=mesesAtras)
        dataDe = dataDe.strftime("%Y-%m-01")

        consultaLogDao = ConsultaLogFuncDao()
        respDao = consultaLogDao.consultaLogsFuncDelete(dataDe)
        listaLogs = []

        for log in respDao:
            dictLog = {
                "id": log.id_logFunc,
                "dataHora": filtroDataHora(log.lfu_dataHora),
                "acao": log.lfu_acao,
                "resp": log.nomeUser,
                "func": js.loads(log.lfu_dadosAntigos.decode("utf-8"))
            }

            listaLogs.append(dictLog)

        return listaLogs  
    

    def consultaLogFuncActive(self) -> list[dict]:
        """
        Consulta e retorna uma lista de logs de ativação de funcionários de acordo com a data na tabela de parâmetros('PAR_LOG_MANT_FUNC').

        :return: Uma lista de dicionários contendo informações sobre os logs de ativação de funcionários.
            Cada dicionário possui chaves "id", "dataHora", "acao", "resp" e "func".
        """

        #Consulta a data na tabela de parametros para fazer a pesquisa apartir desta data
        consultaParametro = ConsultaParametrosDao()
        mesesAtras = consultaParametro.consultaParametros("PAR_LOG_MANT_FUNC")
        dataDe = datetime.now()
        dataDe = dataDe - relativedelta(months=mesesAtras)
        dataDe = dataDe.strftime("%Y-%m-01")

        consultaLogDao = ConsultaLogFuncDao()
        respDao = consultaLogDao.consultaLogsFuncActive(dataDe)
        listaLogs = []

        for log in respDao:
            dictLog = {
                "id": log.id_logFunc,
                "dataHora": filtroDataHora(log.lfu_dataHora),
                "acao": log.lfu_acao,
                "resp": log.nomeUser,
                "func": js.loads(log.lfu_dadosAntigos.decode("utf-8"))
            }

            listaLogs.append(dictLog)

        return listaLogs  
        
        
    def consultaLogFuncInsertDetelhado(self, id: int):
        """
        Consulta e retorna detalhes de um registro de log de funcionário específico.

        :param id: O ID do registro de log de funcionário.
        
        :return: Um objeto Log contendo detalhes do registro de log de funcionário.
        """

        consultaLogDao = ConsultaLogFuncDao()
        manterUsuarioDao = ManterUsuarioDao()
        respDao = consultaLogDao.consultaLogsFuncDetalhado(id)
        
        usuario = manterUsuarioDao.consultarUsuarioDetalhado(respDao.lfu_idUsua)
        logFunc = Log(id=respDao.id_logFunc, dataHora=respDao.lfu_dataHora, acao=respDao.lfu_acao, usuario=usuario)
        logFunc.converteDictDadosAntigos(respDao.lfu_dadosAntigos)
        logFunc.converteDictDadosNovos(respDao.lfu_dadosNovos)

        return logFunc
