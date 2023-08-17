from ..extensions.FiltrosJson import filtroDataHora, filtroMensagem, filtroNome
from ..models.dao.ConsultaLogMenDao import ConsultaLogMenDao

"""
Classe Controller para a consulta de logs de mensagens
@author - Fabio
@version - 1.0
@since - 17/08/2023
"""

class ControleConsultarLogMen:

    def consultaLogMen(self) -> list[dict]:
        consultaLogMenDao = ConsultaLogMenDao()
        respDao = consultaLogMenDao.consultaLogsMen()
        listaLogs = []

        for log in respDao:
            dictLog = {
                "id": log.id_logMens,
                "dataHora": filtroDataHora(log.lme_dataHora),
                "resp": filtroNome(log.nomeUser),
                "msg": filtroMensagem(log.lme_mensagem)
            }

            listaLogs.append(dictLog)

        return listaLogs   