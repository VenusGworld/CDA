from app.models.entity.Log import Log
from ..Tables import CDA013
from ...extensions.Database import DB
import sys

"""
Classe Dao para gerar de log
@tables - CDA013
@author - Fabio
@version - 1.0
@since - 05/06/2023
"""

class GeraLogUsuarioDao:

    def inserirLog(self, log: Log) -> bool:
        #########################################################################################
        # Essa Função insere o log no banco.
        
        # PARAMETROS:
        #   log = Instancia da classe Log com os dados para inserir o log.
        
        # RETORNOS:
        #   return True = Retorna True caso foi inserido com sucesso;
        #   return False = Retorna False caso ocorra erro na inserção.
        #########################################################################################

        logUser = CDA013(dataHora=log.get_dataHora(), acao=log.get_acao(), 
                         dadosAntigos=log.converteDadosAntigos(), 
                         dadosNovos=log.converteDadosNovos(), idUsua=log.get_usuario().get_id())
        
        try:
            DB.session.add(logUser)
            DB.session.commit()
            return True
        except Exception as erro:
            print(erro, sys.exc_info()[0])
            return False
        