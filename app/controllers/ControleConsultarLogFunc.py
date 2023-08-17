from ..models.dao.ConsultaLogFuncDao import ConsultaLogFuncDao
from ..models.dao.ManterUsuarioDao import ManterUsuarioDao
from ..extensions.FiltrosJson import filtroDataHora
from ..models.entity.Log import Log
import json as js

"""
Classe Controller para a consulta de logs do funcionário
@author - Fabio
@version - 1.0
@since - 16/08/2023
"""

class ControleConsultarLogFunc:

    def consultaLogFuncInsert(self) -> list[dict]:
        consultaLogDao = ConsultaLogFuncDao()
        respDao = consultaLogDao.consultaLogsFuncInsert()
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
        consultaLogDao = ConsultaLogFuncDao()
        respDao = consultaLogDao.consultaLogsFuncUpdate()
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
        consultaLogDao = ConsultaLogFuncDao()
        respDao = consultaLogDao.consultaLogsFuncDelete()
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
        consultaLogDao = ConsultaLogFuncDao()
        respDao = consultaLogDao.consultaLogsFuncActive()
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
        consultaLogDao = ConsultaLogFuncDao()
        manterUsuarioDao = ManterUsuarioDao()
        respDao = consultaLogDao.consultaLogsFuncInsert()

        for log in respDao:
            logUser = Log()
            logUser.id = log.id_logFunc
            logUser.dataHora = log.lfu_dataHora
            logUser.acao = log.lfu_acao
            logUser.converteDictDadosAntigos(log.lfu_dadosAntigos)
            logUser.converteDictDadosNovos(log.lfu_dadosNovos)
            logUser.usuario = manterUsuarioDao.mostarUsuarioDetalhado(log.lus_idUsua)
