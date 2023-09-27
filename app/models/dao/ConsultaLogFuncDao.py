from ...configurations.Database import DB
from ..Tables import CDA011, SysUser

class ConsultaLogFuncDao:
    """
    Classe Dao para funções de consulta de logs do manter funcionário
    @tables - SysUser, CDA011
    @author - Fabio
    @version - 1.0
    @since - 16/08/2023
    """

    def consultaLogsFunc(self, data: str, acao: str) -> CDA011:
        logs = DB.session.query(CDA011.id_logFunc, CDA011.lfu_acao, CDA011.lfu_dataHora, CDA011.lfu_dadosNovos, CDA011.lfu_dadosAntigos,  SysUser.us_usuario.label("nomeUser"))\
            .join(SysUser, CDA011.lfu_idUsua == SysUser.id)\
                .filter(CDA011.lfu_acao==acao, CDA011.lfu_dataHora>=data)\
                    .order_by(CDA011.lfu_dataHora)

        return logs
    

    def consultaLogsFuncDetalhado(self, id: int) -> CDA011:
        log = DB.session.query(CDA011.id_logFunc, CDA011.lfu_acao, CDA011.lfu_dataHora, CDA011.lfu_dadosNovos, CDA011.lfu_dadosAntigos, CDA011.lfu_idUsua)\
                .filter(CDA011.id_logFunc==id)\
                    .first()

        return log