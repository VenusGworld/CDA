from ...configurations.Database import DB
from ..Tables import CDA013, SysUser

class ConsultaLogUserDao:
    """
    Classe Dao para funções de consulta de logs
    @tables - SysUser, CDA013
    @author - Fabio
    @version - 1.0
    @since - 07/07/2023
    """

    def consultaLogsUser(self, dataDe: str, acao: str) -> CDA013:
        logs = DB.session.query(CDA013.id_logUsua, CDA013.lus_acao, CDA013.lus_dataHora, CDA013.lus_dadosNovos,  CDA013.lus_dadosAntigos, SysUser.us_nome.label("nomeUser"))\
            .join(SysUser, CDA013.lus_idUsua == SysUser.id)\
                .filter(CDA013.lus_acao==acao, CDA013.lus_dataHora>=dataDe)\
                    .order_by(CDA013.lus_dataHora)

        return logs
    

    def consultaLogsUserDetalhado(self, id: int) -> CDA013:
        log = DB.session.query(CDA013.id_logUsua, CDA013.lus_acao, CDA013.lus_dataHora, CDA013.lus_dadosNovos, CDA013.lus_dadosAntigos, CDA013.lus_idUsua)\
            .filter(CDA013.id_logUsua==id)\
                .first()

        return log