from ..models.dao.ConsultaLogChaveDao import ConsultaLogChaveDao
from ..models.dao.ManterUsuarioDao import ManterUsuarioDao
from ..extensions.FiltrosJson import filtroDataHora
from ..models.entity.Log import Log
import json as js

class ControleConsultarLogChave:
    """
    Classe Controller para as funções de consulta de logs da chave
    @author - Fabio
    @version - 1.0
    @since - 05/09/2023
    """

    def consultaLogChaveInsert(self) -> list[dict]:
        """
        Consulta e retorna uma lista de logs de inserção de chaves.

        :return: Uma lista de dicionários contendo informações sobre os logs de inserção de chaves.
            Cada dicionário possui chaves "id", "dataHora", "acao", "resp" e "chave".
        """

        consultaLogDao = ConsultaLogChaveDao()
        respDao = consultaLogDao.consultaLogsChaveInsert()
        listaLogs = []

        for log in respDao:
            dictLog = {
                "id": log.id_logChave,
                "dataHora": filtroDataHora(log.lch_dataHora),
                "acao": log.lch_acao,
                "resp": log.nomeUser,
                "chave": js.loads(log.lch_dadosNovos.decode("utf-8"))
            }

            listaLogs.append(dictLog)

        return listaLogs    


    def consultaLogChaveUpdate(self) -> list[dict]:
        """
        Consulta e retorna uma lista de logs de alteração de chaves.

        :return: Uma lista de dicionários contendo informações sobre os logs de alteração de chaves.
            Cada dicionário possui chaves "id", "dataHora", "acao", "resp" e "chave".
        """

        consultaLogDao = ConsultaLogChaveDao()
        respDao = consultaLogDao.consultaLogsChaveUpdate()
        listaLogs = []

        for log in respDao:
            dictLog = {
                "id": log.id_logChave,
                "dataHora": filtroDataHora(log.lch_dataHora),
                "acao": log.lch_acao,
                "resp": log.nomeUser,
                "chave": js.loads(log.lch_dadosNovos.decode("utf-8"))
            }

            listaLogs.append(dictLog)

        return listaLogs 


    def consultaLogChaveDelete(self) -> list[dict]:
        """
        Consulta e retorna uma lista de logs de exclusão de chaves.

        :return: Uma lista de dicionários contendo informações sobre os logs de exclusão de chaves.
            Cada dicionário possui chaves "id", "dataHora", "acao", "resp" e "chave".
        """

        consultaLogDao = ConsultaLogChaveDao()
        respDao = consultaLogDao.consultaLogsChaveDelete()
        listaLogs = []

        for log in respDao:
            dictLog = {
                "id": log.id_logChave,
                "dataHora": filtroDataHora(log.lch_dataHora),
                "acao": log.lch_acao,
                "resp": log.nomeUser,
                "chave": js.loads(log.lch_dadosAntigos.decode("utf-8"))
            }

            listaLogs.append(dictLog)

        return listaLogs  
    

    def consultaLogChaveActive(self) -> list[dict]:
        """
        Consulta e retorna uma lista de logs de ativação de chaves.

        :return: Uma lista de dicionários contendo informações sobre os logs de ativação de chaves.
            Cada dicionário possui chaves "id", "dataHora", "acao", "resp" e "chave".
        """

        consultaLogDao = ConsultaLogChaveDao()
        respDao = consultaLogDao.consultaLogsChaveActive()
        listaLogs = []

        for log in respDao:
            dictLog = {
                "id": log.id_logChave,
                "dataHora": filtroDataHora(log.lch_dataHora),
                "acao": log.lch_acao,
                "resp": log.nomeUser,
                "chave": js.loads(log.lch_dadosAntigos.decode("utf-8"))
            }

            listaLogs.append(dictLog)

        return listaLogs  
        
        
    def consultaLogChaveDetelhado(self, id: int) -> Log:
        """
        Consulta e retorna detalhes de um registro de log de chave específico.

        :param id: O ID do registro de log de chave.
        
        :return: Um objeto Log contendo detalhes do registro de log de chave.
        """

        consultaLogDao = ConsultaLogChaveDao()
        manterUsuarioDao = ManterUsuarioDao()
        respDao = consultaLogDao.consultaLogsChaveDetalhado(id)
        
        usuario = manterUsuarioDao.consultarUsuarioDetalhado(respDao.lch_idUsua)
        logChave = Log(id=respDao.id_logChave, dataHora=respDao.lch_dataHora, acao=respDao.lch_acao, usuario=usuario)
        logChave.converteDictDadosAntigos(respDao.lch_dadosAntigos)
        logChave.converteDictDadosNovos(respDao.lch_dadosNovos)

        return logChave
