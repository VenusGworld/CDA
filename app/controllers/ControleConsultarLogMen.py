from ..extensions.FiltrosJson import filtroDataHora, filtroMensagem, filtroNome
from ..models.dao.ConsultaLogMenDao import ConsultaLogMenDao

class ControleConsultarLogMen:
    """
    Classe Controller para as funções de consulta de logs do envio de mensagem
    @author - Fabio
    @version - 1.0
    @since - 17/08/2023
    """

    def consultaLogMen(self) -> list[dict]:
        """
        Consulta e retorna uma lista de logs de mensagens envidas.

        :return: Uma lista de dicionários contendo informações sobre os logs de mensagens envidas.
            Cada dicionário possui chaves "id", "dataHora", "resp" e "msg".
        """
        
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