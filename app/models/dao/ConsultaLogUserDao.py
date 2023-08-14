from ...configurations.Database import DB
from ..Tables import CDA013, SysUser

"""
Classe Dao para funções de consulta de logs
@tables - SysUser
@author - Fabio
@version - 1.0
@since - 07/07/2023
"""


class ConsultaLogUserDao:

    def consultaLogsUserInsert(self) -> CDA013:
        logs = DB.session.query(CDA013.id_logUsua, CDA013.lus_acao, CDA013.lus_dataHora, CDA013.lus_dadosNovos, SysUser.us_nome.label("nomeUser"))\
            .join(SysUser, CDA013.lus_idUsua == SysUser.id)\
                .filter(CDA013.lus_acao=="INSERT")\
                    .order_by(CDA013.lus_dataHora)

        return logs
    

    def consultaLogsUserUpdate(self) -> CDA013:
        logs = DB.session.query(CDA013.id_logUsua, CDA013.lus_acao, CDA013.lus_dataHora, CDA013.lus_dadosNovos, SysUser.us_nome.label("nomeUser"))\
            .join(SysUser, CDA013.lus_idUsua == SysUser.id)\
                .filter(CDA013.lus_acao=="UPDATE")\
                    .order_by(CDA013.lus_dataHora)

        return logs
    

    def consultaLogsUserDelete(self) -> CDA013:
        logs = DB.session.query(CDA013.id_logUsua, CDA013.lus_acao, CDA013.lus_dataHora, CDA013.lus_dadosAntigos, SysUser.us_nome.label("nomeUser"))\
            .join(SysUser, CDA013.lus_idUsua == SysUser.id)\
                .filter(CDA013.lus_acao=="DELETE")\
                    .order_by(CDA013.lus_dataHora)

        return logs
    

    def consultaLogsUserActive(self) -> CDA013:
        logs = DB.session.query(CDA013.id_logUsua, CDA013.lus_acao, CDA013.lus_dataHora, CDA013.lus_dadosAntigos, SysUser.us_nome.label("nomeUser"))\
            .join(SysUser, CDA013.lus_idUsua == SysUser.id)\
                .filter(CDA013.lus_acao=="ACTIVE")\
                    .order_by(CDA013.lus_dataHora)

        return logs