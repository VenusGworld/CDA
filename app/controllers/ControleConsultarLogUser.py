from ..models.dao.ManterUsuarioDao import ManterUsuarioDao
from ..models.dao.ConsultaLogUserDao import ConsultaLogUserDao
from ..extensions.FiltrosJson import filtroDataHora, filtroNome
from ..models.entity.Log import Log
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
        Consulta e retorna uma lista de logs de inserção de usuários.

        :return: Uma lista de dicionários contendo informações sobre os logs de inserção de usuários.
            Cada dicionário possui chaves "id", "dataHora", "acao", "resp" e "usuario".
        """

        consultaLogDao = ConsultaLogUserDao()
        respDao = consultaLogDao.consultaLogsUserInsert()
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
        Consulta e retorna uma lista de logs de alteração de usuários.

        :return: Uma lista de dicionários contendo informações sobre os logs de alteração de usuários.
            Cada dicionário possui chaves "id", "dataHora", "acao", "resp" e "usuario".
        """

        consultaLogDao = ConsultaLogUserDao()
        respDao = consultaLogDao.consultaLogsUserUpdate()
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
        Consulta e retorna uma lista de logs de exclusão de usuários.

        :return: Uma lista de dicionários contendo informações sobre os logs de exclusão de usuários.
            Cada dicionário possui chaves "id", "dataHora", "acao", "resp" e "usuario".
        """

        consultaLogDao = ConsultaLogUserDao()
        respDao = consultaLogDao.consultaLogsUserDelete()
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
        Consulta e retorna uma lista de logs de ativação de usuários.

        :return: Uma lista de dicionários contendo informações sobre os logs de ativação de usuários.
            Cada dicionário possui chaves "id", "dataHora", "acao", "resp" e "usuario".
        """

        consultaLogDao = ConsultaLogUserDao()
        respDao = consultaLogDao.consultaLogsUserActive()
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
        
        
    def consultaLogUsertDetelhado(self, id: int):
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
