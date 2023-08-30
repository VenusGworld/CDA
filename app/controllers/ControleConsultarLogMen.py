from ..extensions.FiltrosJson import filtroDataHora, filtroMensagem, filtroNome
from ..models.dao.ConsultaLogMenDao import ConsultaLogMenDao
from ..models.dao.ManterUsuarioDao import ManterUsuarioDao
from ..models.entity.Log import Log

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


    def consultaLogMenDetalhado(self, id: int) -> Log:   
        """
        Consulta e retorna detalhes de um registro de log de mensagem específico.

        :param id: O ID do registro de log de mensagem.
        
        :return: Um objeto Log contendo detalhes do registro de log de mensagem.
        """

        consultaLogMenDao = ConsultaLogMenDao()
        manterUsuarioDao = ManterUsuarioDao()

        respDao = consultaLogMenDao.consultaLogMenDetalhado(id)
        usuario = manterUsuarioDao.consultarUsuarioDetalhado(respDao.lme_idUsua)
        logMen = Log(id=respDao.id_logMens, dataHora=respDao.lme_dataHora, observacao=respDao.lme_mensagem, usuario=usuario)

        return logMen