from ..models.dao.ManterUsuarioDao import ManterUsuarioDao
from ..models.dao.ConsultaLogUserDao import ConsultaLogUserDao
from ..extensions.FiltrosJson import filtroDataHora
from ..models.entity.Log import Log
import json as js

"""
Classe Controller para a consulta de logs do sistema
@author - Fabio
@version - 1.0
@since - 07/07/2023
"""

class ControleConsultarLogUser:

    def consultaLogUserInsert(self) -> list[dict]:
        consultaLogDao = ConsultaLogUserDao()
        respDao = consultaLogDao.consultaLogsUserInsert()
        listaLogs = []

        for log in respDao:
            dictLog = {
                "id": log.id_logUsua,
                "dataHora": filtroDataHora(log.lus_dataHora),
                "acao": log.lus_acao,
                "resp": log.nomeUser,
                "usuario": js.loads(log.lus_dadosNovos.decode("utf-8"))
            }

            listaLogs.append(dictLog)

        return listaLogs    


    def consultaLogUserUpdate(self) -> list[dict]:
        consultaLogDao = ConsultaLogUserDao()
        respDao = consultaLogDao.consultaLogsUserUpdate()
        listaLogs = []

        for log in respDao:
            dictLog = {
                "id": log.id_logUsua,
                "dataHora": filtroDataHora(log.lus_dataHora),
                "acao": log.lus_acao,
                "resp": log.nomeUser,
                "usuario": js.loads(log.lus_dadosNovos.decode("utf-8"))
            }

            listaLogs.append(dictLog)

        return listaLogs 


    def consultaLogUserDelete(self) -> list[dict]:
        consultaLogDao = ConsultaLogUserDao()
        respDao = consultaLogDao.consultaLogsUserDelete()
        listaLogs = []

        for log in respDao:
            dictLog = {
                "id": log.id_logUsua,
                "dataHora": filtroDataHora(log.lus_dataHora),
                "acao": log.lus_acao,
                "resp": log.nomeUser,
                "usuario": js.loads(log.lus_dadosAntigos.decode("utf-8"))
            }

            listaLogs.append(dictLog)

        return listaLogs  
    

    def consultaLogUserActive(self) -> list[dict]:
        consultaLogDao = ConsultaLogUserDao()
        respDao = consultaLogDao.consultaLogsUserActive()
        listaLogs = []

        for log in respDao:
            dictLog = {
                "id": log.id_logUsua,
                "dataHora": filtroDataHora(log.lus_dataHora),
                "acao": log.lus_acao,
                "resp": log.nomeUser,
                "usuario": js.loads(log.lus_dadosAntigos.decode("utf-8"))
            }

            listaLogs.append(dictLog)

        return listaLogs  
        
        
    def consultaLogUserInsertDetelhado(self, id: int):
        consultaLogDao = ConsultaLogUserDao()
        manterUsuarioDao = ManterUsuarioDao()
        respDao = consultaLogDao.consultaLogsUserInsert()

        for log in respDao:
            logUser = Log()
            logUser.id = log.id_logUsua
            logUser.dataHora = log.lus_dataHora
            logUser.acao = log.lus_acao
            logUser.converteDictDadosAntigos(log.lus_dadosAntigos)
            logUser.converteDictDadosNovos(log.lus_dadosNovos)
            logUser.usuario = manterUsuarioDao.mostarUsuarioDetalhado(log.lus_idUsua)
