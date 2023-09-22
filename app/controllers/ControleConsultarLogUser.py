from ..models.dao.ConsultaParametrosDao import ConsultaParametrosDao
from ..extensions.FiltrosJson import filtroDataHora, filtroNome
from ..models.dao.ConsultaLogUserDao import ConsultaLogUserDao
from ..models.dao.ManterUsuarioDao import ManterUsuarioDao
from dateutil.relativedelta import relativedelta
from ..models.entity.Log import Log
from datetime import datetime
import json as js

class ControleConsultarLogUser:
    """
    Classe Controller para as funções de consultas de logs do usuário no sistema
    @author - Fabio
    @version - 1.0
    @since - 07/07/2023
    """

    def consultaLogUserInsert(self) -> list[dict]:
        """
        Consulta e retorna uma lista de logs de inserção de usuários de acordo com a data na tabela de parâmetros('PAR_LOG_MANT_USER').

        :return: Uma lista de dicionários contendo informações sobre os logs de inserção de usuários.
            Cada dicionário possui chaves "id", "dataHora", "acao", "resp" e "usuario".
        """

        #Consulta a data na tabela de parametros para fazer a pesquisa apartir desta data
        consultaParametro = ConsultaParametrosDao()
        mesesAtras = consultaParametro.consultaParametros("PAR_LOG_MANT_USER")
        dataDe = datetime.now()
        dataDe = dataDe - relativedelta(months=mesesAtras)
        dataDe = dataDe.strftime("%Y-%m-01")

        consultaLogDao = ConsultaLogUserDao()
        respDao = consultaLogDao.consultaLogsUserInsert(dataDe)
        listaLogs = []

        for log in respDao:
            dictLog = {
                "id": log.id_logUsua,
                "dataHora": filtroDataHora(log.lus_dataHora),
                "acao": log.lus_acao,
                "resp": filtroNome(log.nomeUser),
                "usuario": js.loads(log.lus_dadosNovos.decode("utf-8"))
            }

            listaLogs.append(dictLog)

        return listaLogs    


    def consultaLogUserUpdate(self) -> list[dict]:
        """
        Consulta e retorna uma lista de logs de alteração de usuários de acordo com a data na tabela de parâmetros('PAR_LOG_MANT_USER').

        :return: Uma lista de dicionários contendo informações sobre os logs de alteração de usuários.
            Cada dicionário possui chaves "id", "dataHora", "acao", "resp" e "usuario".
        """

        #Consulta a data na tabela de parametros para fazer a pesquisa apartir desta data
        consultaParametro = ConsultaParametrosDao()
        mesesAtras = consultaParametro.consultaParametros("PAR_LOG_MANT_USER")
        dataDe = datetime.now()
        dataDe = dataDe - relativedelta(months=mesesAtras)
        dataDe = dataDe.strftime("%Y-%m-01")

        consultaLogDao = ConsultaLogUserDao()
        respDao = consultaLogDao.consultaLogsUserUpdate(dataDe)
        listaLogs = []

        for log in respDao:
            dictLog = {
                "id": log.id_logUsua,
                "dataHora": filtroDataHora(log.lus_dataHora),
                "acao": log.lus_acao,
                "resp": filtroNome(log.nomeUser),
                "usuario": js.loads(log.lus_dadosNovos.decode("utf-8"))
            }

            listaLogs.append(dictLog)

        return listaLogs 


    def consultaLogUserDelete(self) -> list[dict]:
        """
        Consulta e retorna uma lista de logs de exclusão de usuários de acordo com a data na tabela de parâmetros('PAR_LOG_MANT_USER').

        :return: Uma lista de dicionários contendo informações sobre os logs de exclusão de usuários.
            Cada dicionário possui chaves "id", "dataHora", "acao", "resp" e "usuario".
        """

        #Consulta a data na tabela de parametros para fazer a pesquisa apartir desta data
        consultaParametro = ConsultaParametrosDao()
        mesesAtras = consultaParametro.consultaParametros("PAR_LOG_MANT_USER")
        dataDe = datetime.now()
        dataDe = dataDe - relativedelta(months=mesesAtras)
        dataDe = dataDe.strftime("%Y-%m-01")

        consultaLogDao = ConsultaLogUserDao()
        respDao = consultaLogDao.consultaLogsUserDelete(dataDe)
        listaLogs = []

        for log in respDao:
            dictLog = {
                "id": log.id_logUsua,
                "dataHora": filtroDataHora(log.lus_dataHora),
                "acao": log.lus_acao,
                "resp": filtroNome(log.nomeUser),
                "usuario": js.loads(log.lus_dadosAntigos.decode("utf-8"))
            }

            listaLogs.append(dictLog)

        return listaLogs  
    

    def consultaLogUserActive(self) -> list[dict]:
        """
        Consulta e retorna uma lista de logs de ativação de usuários de acordo com a data na tabela de parâmetros('PAR_LOG_MANT_USER').

        :return: Uma lista de dicionários contendo informações sobre os logs de ativação de usuários.
            Cada dicionário possui chaves "id", "dataHora", "acao", "resp" e "usuario".
        """

        #Consulta a data na tabela de parametros para fazer a pesquisa apartir desta data
        consultaParametro = ConsultaParametrosDao()
        mesesAtras = consultaParametro.consultaParametros("PAR_LOG_MANT_USER")
        dataDe = datetime.now()
        dataDe = dataDe - relativedelta(months=mesesAtras)
        dataDe = dataDe.strftime("%Y-%m-01")

        consultaLogDao = ConsultaLogUserDao()
        respDao = consultaLogDao.consultaLogsUserActive(dataDe)
        listaLogs = []

        for log in respDao:
            dictLog = {
                "id": log.id_logUsua,
                "dataHora": filtroDataHora(log.lus_dataHora),
                "acao": log.lus_acao,
                "resp": filtroNome(log.nomeUser),
                "usuario": js.loads(log.lus_dadosAntigos.decode("utf-8"))
            }

            listaLogs.append(dictLog)

        return listaLogs  
        
        
    def consultaLogUsertDetelhado(self, id: int) -> Log:
        """
        Consulta e retorna detalhes de um registro de log de usuário específico.

        :param id: O ID do registro de log de usuário.
        
        :return: Um objeto Log contendo detalhes do registro de log de usuário.
        """

        consultaLogDao = ConsultaLogUserDao()
        manterUsuarioDao = ManterUsuarioDao()
        respDao = consultaLogDao.consultaLogsUserDetalhado(id)
        
        usuario = manterUsuarioDao.consultarUsuarioDetalhado(respDao.lus_idUsua)
        logUser = Log(id=respDao.id_logUsua, dataHora=respDao.lus_dataHora, acao=respDao.lus_acao, usuario=usuario)
        logUser.converteDictDadosAntigos(respDao.lus_dadosAntigos)
        logUser.converteDictDadosNovos(respDao.lus_dadosNovos)

        return logUser
