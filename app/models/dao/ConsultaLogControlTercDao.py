from ...configurations.Database import DB
from ..Tables import CDA008, SysUser

class ConsultaLogControlTercDao:
    """
    Classe Dao para funções de consulta de logs do controle de terceiros
    @tables - SysUser, CDA008
    @author - Fabio
    @version - 1.0
    @since - 18/09/2023
    """

    def consultaLogsControlTercEntrada(self, data: str) -> CDA008:
        logs = DB.session.query(CDA008.id_logTerc, CDA008.lmte_acao, CDA008.lmte_dataHora, CDA008.lmte_dadosNovos, SysUser.us_usuario.label("nomeUser"))\
            .join(SysUser, CDA008.lmte_idUsua == SysUser.id)\
                .filter(CDA008.lmte_acao=="ENTRADA", CDA008.lmte_dataHora>=data)\
                    .order_by(CDA008.lmte_dataHora)

        return logs
    

    def consultaLogsControlTercSaida(self, data: str) -> CDA008:
        logs = DB.session.query(CDA008.id_logTerc, CDA008.lmte_acao, CDA008.lmte_dataHora, CDA008.lmte_dadosNovos, SysUser.us_usuario.label("nomeUser"))\
            .join(SysUser, CDA008.lmte_idUsua == SysUser.id)\
                .filter(CDA008.lmte_acao=="SAIDA", CDA008.lmte_dataHora>=data)\
                    .order_by(CDA008.lmte_dataHora)

        return logs
    

    def consultaLogsControlTercUpdate(self, data: str) -> CDA008:
        logs = DB.session.query(CDA008.id_logTerc, CDA008.lmte_acao, CDA008.lmte_dataHora, CDA008.lmte_dadosAntigos, SysUser.us_usuario.label("nomeUser"))\
            .join(SysUser, CDA008.lmte_idUsua == SysUser.id)\
                .filter(CDA008.lmte_acao=="UPDATE", CDA008.lmte_dataHora>=data)\
                    .order_by(CDA008.lmte_dataHora)

        return logs
    

    def consultaLogsControlTercDelete(self, data: str) -> CDA008:
        logs = DB.session.query(CDA008.id_logTerc, CDA008.lmte_acao, CDA008.lmte_dataHora, CDA008.lmte_dadosAntigos, SysUser.us_usuario.label("nomeUser"))\
            .join(SysUser, CDA008.lmte_idUsua == SysUser.id)\
                .filter(CDA008.lmte_acao=="DELETE", CDA008.lmte_dataHora>=data)\
                    .order_by(CDA008.lmte_dataHora)
        
        return logs
    

    def consultaLogsControlTercDetalhado(self, id: int) -> CDA008:
        log = DB.session.query(CDA008.id_logTerc, CDA008.lmte_acao, CDA008.lmte_dataHora, CDA008.lmte_dadosNovos, CDA008.lmte_dadosAntigos, CDA008.lmte_observacao, CDA008.lmte_idUsua)\
            .filter(CDA008.id_logTerc==id)\
                .first()
        
        return log
