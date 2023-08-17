from ...configurations.Database import DB
from ..Tables import CDA014, SysUser

"""
Classe Dao para funções de consulta de logs
@tables - SysUser, CDA014
@author - Fabio
@version - 1.0
@since - 16/08/2023
"""

class ConsultaLogMenDao:

    def consultaLogsMen(self) -> CDA014:
        logs = DB.session.query(CDA014.id_logMens, CDA014.lme_dataHora, CDA014.lme_mensagem, SysUser.us_nome.label("nomeUser"))\
            .join(SysUser, CDA014.lme_idUsua == SysUser.id)\
                .order_by(CDA014.lme_dataHora)

        return logs