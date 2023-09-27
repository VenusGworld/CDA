from ...configurations.Database import DB
from ..Tables import CDA006, SysUser

class ConsultaLogControlGerDao:
    """
    Classe Dao para funções de consulta de logs do controle de gerentes
    @tables - SysUser, CDA006
    @author - Fabio
    @version - 1.0
    @since - 18/09/2023
    """

    def consultaLogsControlGer(self, data: str, acao: str) -> CDA006:
        logs = DB.session.query(CDA006.id_logGere, CDA006.lmge_acao, CDA006.lmge_dataHora, CDA006.lmge_dadosNovos, CDA006.lmge_dadosAntigos, SysUser.us_usuario.label("nomeUser"))\
            .join(SysUser, CDA006.lmge_idUsua == SysUser.id)\
                .filter(CDA006.lmge_acao==acao, CDA006.lmge_dataHora>=data)\
                    .order_by(CDA006.lmge_dataHora)

        return logs
    

    def consultaLogsControlGerDetalhado(self, id: int) -> CDA006:
        log = DB.session.query(CDA006.id_logGere, CDA006.lmge_acao, CDA006.lmge_dataHora, CDA006.lmge_dadosNovos, CDA006.lmge_dadosAntigos, CDA006.lmge_observacao, CDA006.lmge_idUsua)\
            .filter(CDA006.id_logGere==id)\
                .first()
        
        return log
