from ...configurations.Database import DB
from ..Tables import CDA010, SysUser

class ConsultaLogChaveDao:
    """
    Classe Dao para funções de consulta de logs do manter chave
    @tables - SysUser, CDA010
    @author - Fabio
    @version - 1.0
    @since - 05/09/2023
    """

    def consultaLogsChaveInsert(self) -> CDA010:
        logs = DB.session.query(CDA010.id_logChave, CDA010.lch_acao, CDA010.lch_dataHora, CDA010.lch_dadosNovos, SysUser.us_usuario.label("nomeUser"))\
            .join(SysUser, CDA010.lch_idUsua == SysUser.id)\
                .filter(CDA010.lch_acao=="INSERT")\
                    .order_by(CDA010.lch_dataHora)

        return logs
    

    def consultaLogsChaveUpdate(self) -> CDA010:
        logs = DB.session.query(CDA010.id_logChave, CDA010.lch_acao, CDA010.lch_dataHora, CDA010.lch_dadosNovos, SysUser.us_usuario.label("nomeUser"))\
            .join(SysUser, CDA010.lch_idUsua == SysUser.id)\
                .filter(CDA010.lch_acao=="UPDATE")\
                    .order_by(CDA010.lch_dataHora)

        return logs
    

    def consultaLogsChaveDelete(self) -> CDA010:
        logs = DB.session.query(CDA010.id_logChave, CDA010.lch_acao, CDA010.lch_dataHora, CDA010.lch_dadosAntigos, SysUser.us_usuario.label("nomeUser"))\
            .join(SysUser, CDA010.lch_idUsua == SysUser.id)\
                .filter(CDA010.lch_acao=="DELETE")\
                    .order_by(CDA010.lch_dataHora)

        return logs
    

    def consultaLogsChaveActive(self) -> CDA010:
        logs = DB.session.query(CDA010.id_logChave, CDA010.lch_acao, CDA010.lch_dataHora, CDA010.lch_dadosAntigos, SysUser.us_usuario.label("nomeUser"))\
            .join(SysUser, CDA010.lch_idUsua == SysUser.id)\
                .filter(CDA010.lch_acao=="ACTIVE")\
                    .order_by(CDA010.lch_dataHora)
        return logs
    
    
    def consultaLogsChaveDetalhado(self, id: int) -> CDA010:
        log = DB.session.query(CDA010.id_logChave, CDA010.lch_acao, CDA010.lch_dataHora, CDA010.lch_dadosNovos, CDA010.lch_dadosAntigos, CDA010.lch_idUsua)\
            .filter(CDA010.id_logChave==id)\
                .first()

        return log