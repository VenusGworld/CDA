from app.models.entity.Log import Log
from ..Tables import CDA013
from ...extensions.Database import DB


class GeraLogUsuarioDao:

    def inserirLog(self, log: Log):
        logUser = CDA013(dataHora=log.get_dataHora(), acao=log.get_acao(), 
                         dadosAntigos=log.converteDadosAntigos(), 
                         dadosNovos=log.converteDadosNovos(), idUsua=log.get_usuario().get_id())
        
        DB.session.add(logUser)
        DB.session.commit()
        