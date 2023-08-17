from ...configurations.Database import DB
from ..Tables import CDA011, SysUser

"""
Classe Dao para funções de consulta de logs
@tables - SysUser, CDA011
@author - Fabio
@version - 1.0
@since - 16/08/2023
"""

class ConsultaLogFuncDao:

    def consultaLogsFuncInsert(self) -> CDA011:
        logs = DB.session.query(CDA011.id_logFunc, CDA011.lfu_acao, CDA011.lfu_dataHora, CDA011.lfu_dadosNovos, SysUser.us_nome.label("nomeUser"))\
            .join(SysUser, CDA011.lfu_idUsua == SysUser.id)\
                .filter(CDA011.lfu_acao=="INSERT")\
                    .order_by(CDA011.lfu_dataHora)

        return logs
    

    def consultaLogsFuncUpdate(self) -> CDA011:
        logs = DB.session.query(CDA011.id_logFunc, CDA011.lfu_acao, CDA011.lfu_dataHora, CDA011.lfu_dadosNovos, SysUser.us_nome.label("nomeUser"))\
            .join(SysUser, CDA011.lfu_idUsua == SysUser.id)\
                .filter(CDA011.lfu_acao=="UPDATE")\
                    .order_by(CDA011.lfu_dataHora)

        return logs
    

    def consultaLogsFuncDelete(self) -> CDA011:
        logs = DB.session.query(CDA011.id_logFunc, CDA011.lfu_acao, CDA011.lfu_dataHora, CDA011.lfu_dadosAntigos, SysUser.us_nome.label("nomeUser"))\
            .join(SysUser, CDA011.lfu_idUsua == SysUser.id)\
                .filter(CDA011.lfu_acao=="DELETE")\
                    .order_by(CDA011.lfu_dataHora)

        return logs
    

    def consultaLogsFuncActive(self) -> CDA011:
        logs = DB.session.query(CDA011.id_logFunc, CDA011.lfu_acao, CDA011.lfu_dataHora, CDA011.lfu_dadosAntigos, SysUser.us_nome.label("nomeUser"))\
            .join(SysUser, CDA011.lfu_idUsua == SysUser.id)\
                .filter(CDA011.lfu_acao=="ACTIVE")\
                    .order_by(CDA011.lfu_dataHora)

        return logs