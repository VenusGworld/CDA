from ..extensions.FiltrosJson import filtroDataHora, filtroNome
from ..models.dao.ConsultaLogTercDao import ConsultaLogTercDao
from ..models.dao.ManterUsuarioDao import ManterUsuarioDao
from ..models.entity.Log import Log
import json as js

class ControleConsultarLogTerc:
    """
    Classe Controller para as funções de consulta de logs da terceiro
    @author - Fabio
    @version - 1.0
    @since - 05/09/2023
    """

    def consultaLogTercInsert(self) -> list[dict]:
        """
        Consulta e retorna uma lista de logs de inserção de tercerios.

        :return: Uma lista de dicionários contendo informações sobre os logs de inserção de tercerios.
            Cada dicionário possui tercerios "id", "dataHora", "acao", "resp" e "terc".
        """

        consultaLogDao = ConsultaLogTercDao()
        respDao = consultaLogDao.consultaLogsTercInsert()
        listaLogs = []

        for log in respDao:
            dictLog = {
                "id": log.id_logTerc,
                "dataHora": filtroDataHora(log.lte_dataHora),
                "acao": log.lte_acao,
                "resp": log.nomeUser,
                "terc": js.loads(log.lte_dadosNovos.decode("utf-8"))
            }

            listaLogs.append(dictLog)

        return listaLogs    


    def consultaLogTercUpdate(self) -> list[dict]:
        """
        Consulta e retorna uma lista de logs de alteração de tercerios.

        :return: Uma lista de dicionários contendo informações sobre os logs de alteração de tercerios.
            Cada dicionário possui tercerios "id", "dataHora", "acao", "resp" e "terc".
        """

        consultaLogDao = ConsultaLogTercDao()
        respDao = consultaLogDao.consultaLogsTercUpdate()
        listaLogs = []

        for log in respDao:
            dictLog = {
                "id": log.id_logTerc,
                "dataHora": filtroDataHora(log.lte_dataHora),
                "acao": log.lte_acao,
                "resp": log.nomeUser,
                "terc": js.loads(log.lte_dadosNovos.decode("utf-8"))
            }

            listaLogs.append(dictLog)

        return listaLogs 


    def consultaLogTercDelete(self) -> list[dict]:
        """
        Consulta e retorna uma lista de logs de exclusão de tercerios.

        :return: Uma lista de dicionários contendo informações sobre os logs de exclusão de tercerios.
            Cada dicionário possui tercerios "id", "dataHora", "acao", "resp" e "terc".
        """

        consultaLogDao = ConsultaLogTercDao()
        respDao = consultaLogDao.consultaLogsTercDelete()
        listaLogs = []

        for log in respDao:
            dictLog = {
                "id": log.id_logTerc,
                "dataHora": filtroDataHora(log.lte_dataHora),
                "acao": log.lte_acao,
                "resp": log.nomeUser,
                "terc": js.loads(log.lte_dadosAntigos.decode("utf-8"))
            }

            listaLogs.append(dictLog)

        return listaLogs  
    

    def consultaLogTercActive(self) -> list[dict]:
        """
        Consulta e retorna uma lista de logs de ativação de tercerios.

        :return: Uma lista de dicionários contendo informações sobre os logs de ativação de tercerios.
            Cada dicionário possui tercerios "id", "dataHora", "acao", "resp" e "terc".
        """

        consultaLogDao = ConsultaLogTercDao()
        respDao = consultaLogDao.consultaLogsTercActive()
        listaLogs = []

        for log in respDao:
            dictLog = {
                "id": log.id_logTerc,
                "dataHora": filtroDataHora(log.lte_dataHora),
                "acao": log.lte_acao,
                "resp": log.nomeUser,
                "terc": js.loads(log.lte_dadosAntigos.decode("utf-8"))
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
        logUser = Log(id=respDao.id_logTerc, dataHora=respDao.lte_dataHora, acao=respDao.lte_acao, usuario=usuario)
        logUser.converteDictDadosAntigos(respDao.lte_dadosAntigos)
        logUser.converteDictDadosNovos(respDao.lte_dadosNovos)

        return logUser
