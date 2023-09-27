from ...configurations.Database import DB
from ..Tables import CDA012, SysUser

class ConsultaLogTercDao:
    """
    Classe Dao para funções de consulta de logs do manter terceiro
    @tables - SysUser, CDA012
    @author - Fabio
    @version - 1.0
    @since - 05/09/2023
    """

    def consultaLogsTerc(self, data: str, acao: str) -> CDA012:
        logs = DB.session.query(CDA012.id_logTerc, CDA012.lte_acao, CDA012.lte_dataHora, CDA012.lte_dadosNovos, CDA012.lte_dadosAntigos, SysUser.us_usuario.label("nomeUser"))\
            .join(SysUser, CDA012.lte_idUsua == SysUser.id)\
                .filter(CDA012.lte_acao==acao, CDA012.lte_dataHora>=data)\
                    .order_by(CDA012.lte_dataHora)

        return logs
    

    def consultaLogsTercDetalhado(self, id: int) -> CDA012:
        log = DB.session.query(CDA012.id_logTerc, CDA012.lte_acao, CDA012.lte_dataHora, CDA012.lte_dadosNovos, CDA012.lte_dadosAntigos, CDA012.lte_observacao, CDA012.lte_idUsua)\
            .filter(CDA012.id_logTerc==id)\
                .first()
        
        return log
