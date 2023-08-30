from ...configurations.Database import DB
from ..Tables import CDA014, SysUser

class ConsultaLogMenDao:
    """
    Classe Dao para funções de consulta de logs
    @tables - SysUser, CDA014
    @author - Fabio
    @version - 1.0
    @since - 16/08/2023
    """

    def consultaLogsMen(self) -> CDA014:
        """
        Consulta e retorna uma lista de registros contendo os logs de mensagens enviadas.
        
        :return: Uma lista contendos os logs de mensagens enviadas.
        """

        logs = DB.session.query(CDA014.id_logMens, CDA014.lme_dataHora, CDA014.lme_mensagem, SysUser.us_nome.label("nomeUser"))\
            .join(SysUser, CDA014.lme_idUsua == SysUser.id)\
                .order_by(CDA014.lme_dataHora)

        return logs
    

    def consultaLogMenDetalhado(self, id: int) -> CDA014:
        """
        Consulta e retorna um registro contendo o log de mensagens enviada específico.

        :parm id: O ID do log escolhido para a vizualização
        
        :return: Uma lista contendos os logs de mensagens enviadas.
        """

        log = DB.session.query(CDA014.id_logMens, CDA014.lme_dataHora, CDA014.lme_mensagem, CDA014.lme_idUsua)\
            .filter(CDA014.id_logMens == id).first()
        
        return log
