from ..models.dao.ConsultaParametrosDao import ConsultaParametrosDao
from ..models.dao.ConsultaLogChaveDao import ConsultaLogChaveDao
from ..models.dao.ManterUsuarioDao import ManterUsuarioDao
from ..extensions.FiltrosJson import filtroDataHora
from dateutil.relativedelta import relativedelta
from ..models.entity.Log import Log
from datetime import datetime
import json as js

class ControleConsultarLogChave:
    """
    Classe Controller para as funções de consulta de logs da chave
    @author - Fabio
    @version - 1.0
    @since - 05/09/2023
    """

    def consultaLogChave(self, acao: str) -> list[dict]:
        """
        Consulta e retorna uma lista de logs de inserção de chaves de acordo com a data na tabela de parâmetros('PAR_LOG_MANT_CHAV').

        :return: Uma lista de dicionários contendo informações sobre os logs de inserção de chaves.
            Cada dicionário possui chaves "id", "dataHora", "acao", "resp" e "chave".
        """

        #Consulta a data na tabela de parametros para fazer a pesquisa apartir desta data
        consultaParametro = ConsultaParametrosDao()
        mesesAtras = consultaParametro.consultaParametros("PAR_LOG_MANT_CHAV")
        dataDe = datetime.now()
        dataDe = dataDe - relativedelta(months=mesesAtras)
        dataDe = dataDe.strftime("%Y-%m-01")

        consultaLogDao = ConsultaLogChaveDao()
        respDao = consultaLogDao.consultaLogsChave(dataDe, acao)
        listaLogs = []

        for log in respDao:
            dictLog = {
                "id": log.id_logChave,
                "dataHora": filtroDataHora(log.lch_dataHora),
                "acao": log.lch_acao,
                "resp": log.nomeUser,
                "chave": js.loads(log.lch_dadosAntigos.decode("utf-8")) if acao in ["ACTIVE", "DELETE"] else js.loads(log.lch_dadosNovos.decode("utf-8"))
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
        logChave = Log(id=respDao.id_logChave, dataHora=respDao.lch_dataHora, acao=respDao.lch_acao, observacao=respDao.lch_observacao, usuario=usuario)
        logChave.converteDictDadosAntigos(respDao.lch_dadosAntigos)
        logChave.converteDictDadosNovos(respDao.lch_dadosNovos)

        return logChave
